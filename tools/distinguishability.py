"""Distinguishability band harness: compute a band for one entry against its
declared `confusable_with` neighbor, from the renders already in the repo.

This is the producer for the per-entry `distinguishability` field proposed in
ADR 0022 (per-entry distinguishability). It is deliberately narrower than
`tools/gate_pilot.py`, which it does not replace:

- `gate_pilot.py` runs the admission shape of Gate 1 - a candidate against its
  2-3 nearest neighbors, on freshly generated renders, scored N-way. It is the
  calibrated instrument (`_agent-context/gate-pilot/CALIBRATION.md`) and it is
  left untouched: its judge prompt offers three bands, so it cannot emit the
  `dramatic` end of the smoke-test scale.
- This module runs the *field* shape: one entry against ONE declared neighbor,
  on a fixed anchor topic, scored pairwise over repeated trials, with the four
  bands the 2026-05-31 smoke test produced (`dramatic` / `clear` / `subtle` /
  `identical`). That is the shape the frontmatter field records.

Two properties make it cheap enough to run by hand on free infrastructure, the
standing "free by default" principle of the agentic factory spec:

1. **It generates nothing.** Both sides of every pair are read from
   `examples/vertical-slices/<topic>/<axis>-<id>.md`, which already covers
   every entry on all twelve anchor topics. No generator call, no API key.
2. **Only the judge is a model call**, and the validated judge is a free
   cross-vendor in-session subagent (the Codex companion, per CALIBRATION.md).

The module itself is deterministic and testable: `prepare` builds the blind
packets and judge prompts and refuses to emit a packet that leaks the answer;
`record` scores pasted verdicts against the hidden mapping. The maintainer (or
an agent) carries the prompt to the judge in between. Nothing here writes to an
ENTRY.md: populating the field is a separate, later decision that ADR 0022 puts
to the maintainer.
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from adherence_gate import load_catalog, gate_neighbors  # noqa: E402
from validate import _extract_frontmatter  # noqa: E402
import anchor_topics  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
RENDERS_DIR = REPO_ROOT / "examples" / "vertical-slices"

# The four bands the 2026-05-31 smoke test produced, worst to best. Ordered, so
# a set of trials can be summarised by its worst observed band.
BANDS: tuple[str, ...] = ("identical", "subtle", "clear", "dramatic")

# Gate 1's floor (adherence-gate-spec.md): `identical` is an automatic fail,
# `subtle` passes but routes to mandatory human review.
FLOOR_BAND = "subtle"


# ---------------------------------------------------------------------------
# Reading the renders that already exist
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Render:
    """One existing vertical-slice render, de-identified for blind judging."""
    entry_id: str
    axis: str
    topic_slug: str
    topic_label: str
    generator_model: str
    generated_at: str
    path: Path
    body: str
    stripped_heading: str | None


def render_path(topic_slug: str, axis: str, entry_id: str) -> Path:
    return RENDERS_DIR / topic_slug / f"{axis}-{entry_id}.md"


def _split_frontmatter_body(raw: str) -> str:
    """Return the body after a column-0 `---` fenced frontmatter block.

    Entry and sample frontmatter may contain block scalars holding their own
    `---` line, so the fence is matched at column 0 only - the same rule
    `tools/promote.py` follows.
    """
    lines = raw.splitlines()
    if not lines or lines[0].rstrip() != "---":
        return raw
    for i in range(1, len(lines)):
        if lines[i].rstrip() == "---":
            return "\n".join(lines[i + 1:]).strip("\n")
    return raw


_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(?P<text>.*?)\s*$")


def strip_attribution_heading(body: str, entry_name: str) -> tuple[str, str | None]:
    """Drop a leading heading that names the entry, and report what was dropped.

    Many renders open with a generator artifact of the form
    `## Senior Consultant on: Choosing between Postgres and DynamoDB`. That
    heading states the answer, so a blind packet built from the raw body would
    be void. Only a heading in the first non-empty line is considered, and only
    when it names the entry; a heading that is genuinely part of the format
    (an ADR's `## Context`, say) is left in place.
    """
    lines = body.split("\n")
    idx = next((i for i, ln in enumerate(lines) if ln.strip()), None)
    if idx is None:
        return body, None
    m = _HEADING_RE.match(lines[idx])
    if not m:
        return body, None
    text = m.group("text")
    if entry_name and entry_name.lower() not in text.lower():
        return body, None
    rest = "\n".join(lines[idx + 1:]).strip("\n")
    return rest, lines[idx].strip()


def load_render(topic_slug: str, axis: str, entry_id: str, entry_name: str) -> Render:
    path = render_path(topic_slug, axis, entry_id)
    if not path.is_file():
        raise FileNotFoundError(f"no render for {axis}/{entry_id} on {topic_slug}: {path}")
    fm = _extract_frontmatter(path) or {}
    raw = path.read_text(encoding="utf-8")
    body, stripped = strip_attribution_heading(_split_frontmatter_body(raw), entry_name)
    return Render(
        entry_id=entry_id,
        axis=axis,
        topic_slug=topic_slug,
        topic_label=fm.get("topic_label") or anchor_topics.label_of(topic_slug) or "",
        generator_model=fm.get("llm_model") or "unknown",
        generated_at=str(fm.get("generated_at") or ""),
        path=path,
        body=body.strip(),
        stripped_heading=stripped,
    )


# ---------------------------------------------------------------------------
# The leak check: a blind packet that names its own answer is worthless
# ---------------------------------------------------------------------------

def _terms_for(entry_id: str, fm: dict) -> list[str]:
    """Strings whose presence in a sample body would name the entry."""
    terms = {entry_id, entry_id.replace("-", " ")}
    name = (fm.get("name") or "").strip()
    if name:
        terms.add(name)
    return sorted(t for t in terms if len(t) >= 4)


def find_leaks(text: str, terms: list[str]) -> list[str]:
    """Terms that appear in `text`, case-insensitively, on a word boundary."""
    hits = []
    low = text.lower()
    for term in terms:
        pattern = r"\b" + re.escape(term.lower()).replace(r"\ ", r"\s+") + r"\b"
        if re.search(pattern, low):
            hits.append(term)
    return hits


# ---------------------------------------------------------------------------
# Trials
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Slot:
    label: str
    entry_id: str
    body: str


@dataclass(frozen=True)
class Trial:
    """One blind presentation of the pair: a topic, an order, two slots.

    A pairwise forced choice is all-right or all-wrong, so a single trial
    scores 0 or 1. `trials` is therefore part of the measurement, not a
    footnote: a band and a score are only meaningful beside the N they came
    from. Trials vary presentation order and (optionally) the anchor topic.
    """
    trial_id: str
    entry_a: str
    entry_b: str
    axis: str
    topic_slug: str
    topic_label: str
    order_seed: int
    slots: tuple[Slot, ...]
    leaks: tuple[str, ...] = field(default=())

    @property
    def mapping(self) -> dict[str, str]:
        """The hidden answer key. Never rendered into a judge prompt."""
        return {s.label: s.entry_id for s in self.slots}


def declared_neighbor(entry_id: str, id_map: dict) -> str | None:
    """The entry's alphabetically first declared same-axis `confusable_with` edge.

    The field the ADR proposes records one neighbor, and `confusable_with` is
    the curated answer to "which entry is this one most likely to collapse
    into". Where an entry declares several, taking the alphabetically first
    (the order `gate_neighbors` already returns) keeps the default
    reproducible rather than a judgement the harness makes silently; pass
    `--neighbor` to test a different declared edge.
    """
    ns = gate_neighbors(entry_id, id_map)
    return ns.confusable[0] if ns.confusable else None


def build_trial(entry_a, entry_b, topic_slug, id_map, order_seed=0) -> Trial:
    """Build one blind trial, refusing to leak the answer key.

    Raises on a leak rather than returning a flagged packet: a packet that
    names its own answer must not reach a judge by accident.
    """
    if entry_a == entry_b:
        raise ValueError("a pair needs two different entries")
    axis_a, fm_a = id_map[entry_a]
    axis_b, fm_b = id_map[entry_b]
    if axis_a != axis_b:
        raise ValueError(
            f"cross-axis pair {entry_a} ({axis_a}) vs {entry_b} ({axis_b}): Gate 1 "
            "varies exactly one axis"
        )
    if anchor_topics.label_of(topic_slug) is None:
        raise ValueError(f"unknown anchor topic: {topic_slug}")

    renders = {
        entry_a: load_render(topic_slug, axis_a, entry_a, fm_a.get("name") or ""),
        entry_b: load_render(topic_slug, axis_b, entry_b, fm_b.get("name") or ""),
    }
    terms = _terms_for(entry_a, fm_a) + _terms_for(entry_b, fm_b)
    leaks = []
    for eid, r in renders.items():
        for hit in find_leaks(r.body, terms):
            leaks.append(f"{r.path.name}: '{hit}'")
    if leaks:
        raise ValueError(
            "blind packet would name its own answer; fix the render or widen the "
            "strip rule before judging: " + "; ".join(sorted(leaks))
        )

    ordered = [entry_a, entry_b]
    random.Random(order_seed).shuffle(ordered)
    slots = tuple(
        Slot(label=label, entry_id=eid, body=renders[eid].body)
        for label, eid in zip("AB", ordered)
    )
    return Trial(
        trial_id=f"{axis_a}-{entry_a}-vs-{entry_b}-{topic_slug}-s{order_seed}",
        entry_a=entry_a, entry_b=entry_b, axis=axis_a,
        topic_slug=topic_slug,
        topic_label=renders[entry_a].topic_label,
        order_seed=order_seed, slots=slots,
    )


def build_trials(entry_a, entry_b, topics, id_map, seeds=(0, 1)) -> list[Trial]:
    """One trial per (topic, order seed) cell."""
    return [
        build_trial(entry_a, entry_b, topic, id_map, order_seed=seed)
        for topic in topics
        for seed in seeds
    ]


# ---------------------------------------------------------------------------
# The judge prompt: four bands, pairwise forced choice
# ---------------------------------------------------------------------------

def build_judge_prompt(trial: Trial, id_map: dict) -> str:
    """The blind judge prompt for one trial.

    Mirrors the 2026-05-31 smoke test's judge: the two unlabeled passages, the
    axis under test, and the two candidate descriptions, with a forced
    one-to-one choice and a four-band rating. It adds the restraint question
    the gate pilot validated, graded against each entry's own declared
    `failure_modes`, because that rides the same call for free.

    Options are listed in alphabetical id order so option order leaks nothing
    about slot order, and the mapping is never stated.
    """
    option_lines = []
    for eid in sorted((trial.entry_a, trial.entry_b)):
        fm = id_map[eid][1]
        name = fm.get("name") or eid
        one_liner = (fm.get("one_liner") or "").strip()
        modes = []
        for item in fm.get("failure_modes") or []:
            mode = (item.get("mode") or "").strip()
            if mode:
                modes.append(f"       - {mode}")
        option_lines.append(
            f"  - {name} (`{eid}`): {one_liner}\n"
            f"     Known failure modes (this {trial.axis} over-hitting its own register):\n"
            + ("\n".join(modes) if modes else "       - (none declared)")
        )
    options_block = "\n".join(option_lines)
    samples_block = "\n\n".join(f"[{s.label}]\n{s.body}" for s in trial.slots)

    return (
        "You are a blind judge in a writing-style attribution test. Judge only the "
        "prose. Use no tools and read no files: everything you need is in this "
        "message. The presentation order is randomized and carries no signal.\n\n"
        f"AXIS UNDER TEST: {trial.axis}\n"
        f"Both passages were written about the same topic: \"{trial.topic_label}\". "
        f"They differ only in {trial.axis}.\n\n"
        f"THE TWO POSSIBLE {trial.axis.upper()}S (alphabetical; exactly one passage "
        "is written in each):\n"
        f"{options_block}\n\n"
        "THE PASSAGES:\n\n"
        f"{samples_block}\n\n"
        "TASKS:\n"
        f"1. ATTRIBUTION (forced choice, one-to-one): assign each passage label to "
        f"exactly one {trial.axis} id. Both ids must be used exactly once.\n"
        "2. BAND: how distinguishable are the two passages on this axis?\n"
        "   - \"dramatic\": different on sight, from structure or stance alone.\n"
        "   - \"clear\": plainly different registers on an ordinary read.\n"
        "   - \"subtle\": genuinely different but only on close reading.\n"
        "   - \"identical\": you cannot tell them apart on this axis.\n"
        "3. RESTRAINT: for each passage, judged ONLY against the failure modes of "
        "the id you attributed it to, is it the genuine register (\"pass\"), a "
        "borderline over-hit (\"weak\"), or a caricature of its own failure mode "
        "(\"fail\")?\n\n"
        "Return ONLY this JSON, nothing outside it:\n"
        "{\n"
        '  "attribution": {"A": "<id>", "B": "<id>"},\n'
        '  "band": "dramatic|clear|subtle|identical",\n'
        '  "restraint": {"A": "pass|weak|fail", "B": "pass|weak|fail"},\n'
        '  "rationale": "<2-4 sentences naming what you keyed on>"\n'
        "}\n"
    )


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def worst_band(bands) -> str | None:
    """The lowest band observed, by the BANDS order.

    Worst-case rather than mean: the field is a floor claim ("a blind judge
    distinguishes this entry from its neighbor at least this well"), and the
    gate's own rule auto-fails on a single `identical`.
    """
    known = [b for b in bands if b in BANDS]
    if not known:
        return None
    return min(known, key=BANDS.index)


def score_trial(trial: Trial, verdict: dict) -> dict:
    """Score one judge verdict against the hidden mapping."""
    truth = trial.mapping
    attribution = verdict.get("attribution") or {}
    per_slot = []
    correct = 0
    for label in sorted(truth):
        guess = attribution.get(label)
        ok = guess == truth[label]
        correct += 1 if ok else 0
        per_slot.append({"label": label, "true": truth[label], "guess": guess, "correct": ok})
    band = verdict.get("band")
    return {
        "trial_id": trial.trial_id,
        "topic_slug": trial.topic_slug,
        "order_seed": trial.order_seed,
        "slots_correct": correct,
        "slots": len(truth),
        # A one-to-one forced choice over two slots is right or wrong as a whole;
        # one slot right and one wrong is not a possible verdict.
        "attribution_correct": correct == len(truth),
        "band": band if band in BANDS else None,
        "band_reported": band,
        "restraint": verdict.get("restraint") or {},
        "rationale": verdict.get("rationale", ""),
        "per_slot": per_slot,
    }


def aggregate(trial_scores: list[dict]) -> dict:
    """Roll trial scores into the shape the proposed field records."""
    n = len(trial_scores)
    hits = sum(1 for s in trial_scores if s["attribution_correct"])
    bands = [s["band"] for s in trial_scores if s["band"]]
    floor = worst_band(bands)
    restraint = [v for s in trial_scores for v in s["restraint"].values()]
    return {
        "trials": n,
        "attribution_correct": hits,
        "score": round(hits / n, 4) if n else None,
        "chance_baseline": 0.5,
        "band": floor,
        "band_is_floor": True,
        "bands_observed": sorted(set(bands), key=BANDS.index),
        "clears_gate_floor": (
            BANDS.index(floor) >= BANDS.index(FLOOR_BAND) if floor else None
        ),
        "restraint_pass": sum(1 for v in restraint if v == "pass"),
        "restraint_weak": sum(1 for v in restraint if v == "weak"),
        "restraint_fail": sum(1 for v in restraint if v == "fail"),
    }


def build_record(entry_a, entry_b, axis, trials, trial_scores, judge, id_map) -> dict:
    """The full inspectable run record for one pair."""
    first = trials[0] if trials else None
    gen_models = sorted({
        load_render(t.topic_slug, t.axis, eid, id_map[eid][1].get("name") or "").generator_model
        for t in trials for eid in (t.entry_a, t.entry_b)
    })
    return {
        "entry": entry_a,
        "neighbor": entry_b,
        "axis": axis,
        "topics": sorted({t.topic_slug for t in trials}),
        "primary_topic": first.topic_slug if first else None,
        "judge_model": judge,
        "generator_models": gen_models,
        "render_source": "examples/vertical-slices (committed renders, not regenerated)",
        "harness": "tools/distinguishability.py",
        "summary": aggregate(trial_scores),
        "trials": trial_scores,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _cmd_prepare(args, id_map) -> int:
    entry = args.entry
    if entry not in id_map:
        print(f"[ERROR] unknown entry id: {entry}", file=sys.stderr)
        return 1
    neighbor = args.neighbor or declared_neighbor(entry, id_map)
    if neighbor is None:
        print(
            f"[ERROR] {entry} declares no same-axis confusable_with neighbor; pass "
            "--neighbor explicitly",
            file=sys.stderr,
        )
        return 1
    if neighbor not in id_map:
        print(f"[ERROR] unknown neighbor id: {neighbor}", file=sys.stderr)
        return 1
    topics = args.topics or [anchor_topics.ANCHOR_TOPICS[0].slug]
    seeds = tuple(range(args.orders))
    trials = build_trials(entry, neighbor, topics, id_map, seeds=seeds)

    if args.json:
        payload = {
            "entry": entry,
            "neighbor": neighbor,
            "axis": trials[0].axis,
            "trials": [
                {
                    "trial_id": t.trial_id,
                    "topic_slug": t.topic_slug,
                    "order_seed": t.order_seed,
                    "mapping": t.mapping,
                    "prompt": build_judge_prompt(t, id_map),
                }
                for t in trials
            ],
        }
        print(json.dumps(payload, indent=2))
        return 0

    print(f"pair: {entry} vs {neighbor} (axis: {trials[0].axis})")
    print(f"trials: {len(trials)} ({len(topics)} topic(s) x {args.orders} order(s))\n")
    for t in trials:
        print(f"=== TRIAL {t.trial_id} ===")
        print(f"(hidden mapping: {t.mapping})\n")
        print(build_judge_prompt(t, id_map))
        print()
    return 0


def _cmd_record(args, id_map) -> int:
    payload = json.loads(Path(args.verdicts).read_text(encoding="utf-8"))
    entry = payload["entry"]
    neighbor = payload["neighbor"]
    verdicts = payload["verdicts"]
    trials = []
    scores = []
    for item in verdicts:
        trial = build_trial(
            entry, neighbor, item["topic_slug"], id_map,
            order_seed=item.get("order_seed", 0),
        )
        trials.append(trial)
        scores.append(score_trial(trial, item["verdict"]))
    record = build_record(
        entry, neighbor, trials[0].axis, trials, scores,
        payload.get("judge_model", "unknown"), id_map,
    )
    out = json.dumps(record, indent=2)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(out + "\n", encoding="utf-8")
        print(f"wrote {args.out}")
        print(json.dumps(record["summary"], indent=2))
    else:
        print(out)
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Compute a distinguishability band for an entry against its declared "
            "confusable_with neighbor, from the committed renders."
        )
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("prepare", help="build blind judge prompts for one pair")
    p.add_argument("--entry", required=True)
    p.add_argument("--neighbor", help="default: first declared confusable_with")
    p.add_argument("--topics", nargs="+", help="anchor topic slugs (default: the first core topic)")
    p.add_argument("--orders", type=int, default=2, help="presentation orders per topic")
    p.add_argument("--json", action="store_true", help="emit machine-readable packets")

    r = sub.add_parser("record", help="score pasted judge verdicts")
    r.add_argument("--verdicts", required=True, help="path to a verdicts JSON file")
    r.add_argument("--out", help="write the run record here (gitignored path)")

    args = parser.parse_args(argv)
    id_map = load_catalog()
    if args.cmd == "prepare":
        return _cmd_prepare(args, id_map)
    return _cmd_record(args, id_map)


if __name__ == "__main__":
    sys.exit(main())
