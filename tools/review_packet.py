#!/usr/bin/env python3
"""Generate per-entry review packets for the GATE 1 catalog review.

GATE 1 of the v1.0 readiness gates requires that `review_status` be honestly
promoted. The repo rule forbids setting `stable` without maintainer review, so
the review itself cannot be delegated. What CAN be delegated is the preparation:
the marketing plan's R1 effort names "prepare a per-entry review packet (the
entry, its examples, its cross-refs, a checklist) so each decision is a fast
yes/edit."

The design principle is that a packet should **pre-answer everything a machine
can decide and ask only what needs a human**. Schema conformance, cross-reference
resolution, pedagogical-field presence, and sample coverage are all already
enforced by `tools/validate.py`; re-asking them of a human wastes the scarce
resource. So those appear as settled facts, and the checklist covers only
judgment: does the instruction phrasing actually steer a model, is the entry
distinct from its nearest neighbours, is it in the right axis.

The packets also carry FLAGS: cheap heuristics for the specific mistakes this
catalog has actually made before, so review attention lands where it pays.

Output goes to _local/review-packets/ (gitignored working artifacts). The
decisions belong in a tracked ledger; see --ledger.

Usage:
    python tools/review_packet.py                  # every stable entry
    python tools/review_packet.py --axis voice     # one axis
    python tools/review_packet.py --entry candid   # one entry
    python tools/review_packet.py --ledger         # (re)write the decision ledger
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate import _extract_frontmatter, AXES, REPO_ROOT  # noqa: E402

OUT_DIR = REPO_ROOT / "_local" / "review-packets"
EXAMPLES_DIR = REPO_ROOT / "examples" / "vertical-slices"
LEDGER = REPO_ROOT / "docs" / "internal" / "review-ledger.md"

# Phrasings that suggest a failure_mode was written as a MISUSE ("someone applied
# this entry to the wrong situation") rather than as the entry over-hitting its
# own register. A full Codex content review caught roughly seven of these per
# batch that spot-checks missed, so it is worth flagging mechanically.
# Kept deliberately narrow. A misuse-shaped failure mode names an external actor
# applying the entry somewhere it does not belong. Generic reader-harm language
# ("serves no reader who arrived with one question") describes the entry
# over-hitting and must NOT match: an earlier, looser list flagged `user-manual`
# on the phrase "reader who" when its failure mode was a textbook over-hit.
MISUSE_MARKERS = [
    r"\bused for\b", r"\bapplied to\b", r"\bmisused?\b", r"\bmisapplied\b",
    r"\bwrong (?:context|audience|situation|topic|format|genre)\b",
    r"\bin (?:a )?(?:context|setting|situation)s? (?:that|where|it)\b",
    r"\bfor (?:an? )?audiences? (?:that|who|which)\b",
]
# Phrasings typical of a correct failure_mode: the register turned up too far.
# Broad on purpose. A miss here only costs a flag that should not have fired.
OVERHIT_MARKERS = [
    r"\btips? (?:over )?into\b", r"\bslides? into\b", r"\bbecomes?\b", r"\bcurdles?\b",
    r"\bso (?:far|much|hard)\b", r"\bat the expense of\b", r"\bovershoots?\b",
    r"\bcollapses? into\b", r"\bturns? into\b", r"\bdrifts? into\b", r"\bhardens? into\b",
    r"\bcrosses (?:over )?into\b", r"\bshades? into\b", r"\bmanufactures?\b",
    r"\bstops\b", r"\bloses\b", r"\bburie[sd]\b", r"\bflattens?\b", r"\bover-\w+",
    r"\bdrives? .{0,30}into\b", r"\bpushes? .{0,30}into\b", r"\bcrowds? out\b",
    r"\bswamps?\b", r"\bsmothers?\b", r"\bexhaustive\b", r"\bevery\b",
]

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in", "is", "it",
    "its", "of", "on", "or", "that", "the", "their", "them", "they", "this", "to",
    "with", "without", "you", "your", "who", "when", "not", "but", "into", "than",
}


def load_all():
    """Return {entry_id: (axis, frontmatter)} for every entry in the catalog."""
    out = {}
    for axis, axis_dir in AXES.items():
        if not axis_dir.exists():
            continue
        for d in sorted(axis_dir.iterdir()):
            if not d.is_dir():
                continue
            fm = _extract_frontmatter(d / "ENTRY.md")
            if fm:
                out[fm.get("id", d.name)] = (axis, fm)
    return out


def _words(text):
    return {w for w in re.findall(r"[a-z]{4,}", (text or "").lower()) if w not in STOPWORDS}


def compute_flags(entry_id, axis, fm, catalog):
    """Cheap heuristics for mistakes this catalog has actually made."""
    flags = []

    # 1. failure_mode written as a misuse rather than over-hitting its own register.
    for item in fm.get("failure_modes", []) or []:
        mode = item.get("mode", "") if isinstance(item, dict) else str(item)
        low = mode.lower()
        hit_misuse = any(re.search(m, low) for m in MISUSE_MARKERS)
        hit_overhit = any(re.search(m, low) for m in OVERHIT_MARKERS)
        if hit_misuse and not hit_overhit:
            flags.append(
                f"**failure_mode may describe a misuse, not over-hitting.** "
                f'"{mode[:90]}" - a failure mode should be this entry turned up too far, '
                f"not someone applying it to the wrong situation."
            )
        # Deliberately NOT flagged: a failure_mode with neither marker. That fires on
        # 38% of them with no precision, which buries the 1% that are genuinely
        # misuse-shaped. A heuristic that flags a third of the corpus is not triage.

    # NOT flagged: one-way `avoid_with`. ADR 0016 decision B1 made avoid_with
    # symmetric AT COMPOSITION TIME - build-instruction.py applies a symmetric
    # union, so "a conflict never depends on which" side declares it. One-way data
    # is therefore correct by design, not a gap. An earlier version of this tool
    # flagged it and produced 253 false positives, one on nearly every entry.
    # Do not re-add it.

    # 2. Near-duplicate one_liner within the same axis (the de-dup concern at scale).
    mine = _words(fm.get("one_liner"))
    if mine:
        for other_id, (other_axis, other_fm) in catalog.items():
            if other_id == entry_id or other_axis != axis:
                continue
            theirs = _words(other_fm.get("one_liner"))
            if not theirs:
                continue
            overlap = len(mine & theirs) / max(1, min(len(mine), len(theirs)))
            if overlap >= 0.5:
                flags.append(
                    f"**one_liner overlaps `{other_id}` ({overlap:.0%} of the shorter one).** "
                    f"Check these are genuinely distinct entries and not two names for one idea."
                )

    # 3. Axis placement, the ADR 0018 rule. Voice is what does not change; tone is
    #    what changes per piece. A voice described in situational language is suspect.
    if axis == "voice":
        situational = re.search(
            r"\b(right now|in this moment|situational|for this (?:message|piece)|depending on)\b",
            (fm.get("one_liner", "") + " " + str(fm.get("description", ""))).lower(),
        )
        if situational:
            flags.append(
                "**Reads situational for a voice.** ADR 0018: voice is what does not change "
                "across a year of writing; tone is what changes per piece. Confirm this "
                "belongs in `taxonomy/voices/`."
            )

    return flags


def catalog_level_findings(catalog):
    """Systematic issues that span many entries.

    These do not belong in a per-entry packet. An issue affecting 80 entries
    repeated 80 times reads as 80 problems and drowns the flags that are specific
    to one entry; collected once, it reads as what it is, a single batch task.
    """
    one_way = []
    for entry_id, (axis, fm) in sorted(catalog.items()):
        for other in fm.get("confusable_with") or []:
            if other in catalog and entry_id not in (catalog[other][1].get("confusable_with") or []):
                one_way.append((entry_id, axis, other))

    no_neighbour = sorted(
        entry_id for entry_id, (_, fm) in catalog.items()
        if fm.get("review_status") == "stable" and not (fm.get("confusable_with") or [])
    )
    return {"one_way_confusable": one_way, "no_confusable": no_neighbour}


def render_catalog_report(catalog, findings):
    ow = findings["one_way_confusable"]
    nn = findings["no_confusable"]
    L = ["# Catalog-level findings", "",
         "Issues that span many entries. Handle these as one batch rather than "
         "deciding them 97 times inside individual packets.", ""]

    L += [f"## One-way `confusable_with` ({len(ow)})", "",
          "Confusability is largely mutual: if A reads like B, B reads like A. Where only one "
          "side declares it, a reader arriving from the other side gets no warning.", "",
          "**This is prose work, not a data edit.** The glossary requires that every "
          "`confusable_with` id have a matching `### Often confused with` block in the entry "
          "body explaining the functional difference, and all 117 entries honour that. So "
          "each missing back-reference is a short authored section written from the other "
          "entry's side, not a one-line frontmatter addition. Batch it by axis.", "",
          "Note this is **not** the same as one-way `avoid_with`, which is fine: ADR 0016 "
          "applies a symmetric union at composition time, so the composer warns both ways "
          "regardless of which side declares it.", "",
          "| Entry | Axis | Lists | but not back |", "|---|---|---|---|"]
    for entry_id, axis, other in ow:
        L.append(f"| `{entry_id}` | {axis} | `{other}` | yes |")
    L += ["",
          f"## Stable entries with no declared near-neighbour ({len(nn)})", "",
          "At 117 entries an entry with no `confusable_with` is either genuinely distinctive "
          "or under-cross-referenced. Worth a sweep, low priority.", ""]
    L += [", ".join(f"`{e}`" for e in nn) or "None.", ""]
    return "\n".join(L)


def sample_topics(entry_id, axis):
    """Which anchor topics this entry has a worked render on."""
    found = []
    for topic_dir in sorted(EXAMPLES_DIR.iterdir()) if EXAMPLES_DIR.exists() else []:
        if (topic_dir / f"{axis}-{entry_id}.md").exists():
            found.append(topic_dir.name)
    return found


def render_packet(entry_id, axis, fm, catalog):
    flags = compute_flags(entry_id, axis, fm, catalog)
    topics = sample_topics(entry_id, axis)
    status = fm.get("review_status", "?")

    L = []
    L.append(f"# Review packet: `{entry_id}`")
    L.append("")
    L.append(f"- **Axis:** {axis}  |  **Family:** {fm.get('family', '-')}  "
             f"|  **Current status:** `{status}`")
    L.append(f"- **Source:** `taxonomy/{AXES[axis].name}/{entry_id}/ENTRY.md`")
    L.append(f"- **Worked renders:** {len(topics)} of 12 anchor topics")
    L.append("")

    L.append("## Already checked, do not re-check")
    L.append("")
    L.append("`tools/validate.py` passes on the whole catalog, which means for this entry:")
    L.append("")
    L.append("- Schema-valid against the frozen contract, and every `pairs_well_with` / "
             "`avoid_with` / `confusable_with` id resolves to a real entry")
    L.append("- `tells`, `anti_patterns`, and `failure_modes` are present and pass the "
             "ADR 0009 substance check")
    L.append(f"- Renders on all 12 anchor topics (Gate 2 sample count){'' if len(topics) == 12 else ' - **NOT MET for this entry**'}")
    L.append("- No em-dashes or en-dashes")
    L.append("")

    if flags:
        L.append(f"## Flags ({len(flags)})")
        L.append("")
        L.append("Heuristics, not verdicts. Each points at a mistake this catalog has made before.")
        L.append("")
        for f in flags:
            L.append(f"- {f}")
        L.append("")
    else:
        L.append("## Flags")
        L.append("")
        L.append("None. Nothing mechanical to object to; this is a pure judgment call.")
        L.append("")

    L.append("## The entry")
    L.append("")
    L.append(f"**One-liner:** {fm.get('one_liner', '-')}")
    L.append("")
    desc = str(fm.get("description", "")).strip()
    if desc:
        L.append("**Description:**")
        L.append("")
        for line in desc.split("\n"):
            L.append(f"> {line}" if line.strip() else ">")
        L.append("")

    L.append("**The instruction a model actually receives:**")
    L.append("")
    L.append("```text")
    L.append(str(fm.get("llm_instruction_phrasing", "")).strip())
    L.append("```")
    L.append("")

    for field, label in (("tells", "Tells"), ("when_to_use", "When to use"),
                         ("when_not_to_use", "When not to use")):
        vals = fm.get(field) or []
        if vals:
            L.append(f"**{label}:**")
            L.append("")
            for v in vals:
                L.append(f"- {v}")
            L.append("")

    for field, label, key in (("anti_patterns", "Anti-patterns", "pattern"),
                              ("failure_modes", "Failure modes", "mode")):
        vals = fm.get(field) or []
        if vals:
            L.append(f"**{label}:**")
            L.append("")
            for v in vals:
                if isinstance(v, dict):
                    head = v.get(key, "")
                    tail = v.get("why") or v.get("mitigation") or ""
                    L.append(f"- **{head}**")
                    if tail:
                        L.append(f"  - {tail}")
                else:
                    L.append(f"- {v}")
            L.append("")

    neighbours = [n for n in (fm.get("confusable_with") or []) if n in catalog]
    L.append("## Nearest neighbours (the distinguishability question)")
    L.append("")
    if neighbours:
        L.append("This is the seam the adherence test measures. If these read as the same "
                 "instruction, the entry is not earning its place.")
        L.append("")
        for n in neighbours:
            n_axis, n_fm = catalog[n]
            L.append(f"### vs `{n}` ({n_axis})")
            L.append("")
            L.append(f"- **Its one-liner:** {n_fm.get('one_liner', '-')}")
            L.append(f"- **Its instruction opens:** "
                     f"{' '.join(str(n_fm.get('llm_instruction_phrasing', '')).split())[:220]}...")
            L.append("")
    else:
        L.append("No `confusable_with` declared. That is itself worth a moment: at 117 entries, "
                 "an entry with no declared near-neighbour is either genuinely distinctive or "
                 "under-cross-referenced.")
        L.append("")

    if topics:
        L.append("## Worked renders")
        L.append("")
        for t in topics:
            L.append(f"- `examples/vertical-slices/{t}/{axis}-{entry_id}.md`")
        L.append("")

    L.append("## Decide")
    L.append("")
    L.append("Machine-checkable things are settled above. These are not:")
    L.append("")
    L.append("1. **Does the instruction phrasing actually steer a model?** Read the block above "
             "as if you were the model. Would it change what you wrote?")
    L.append(f"2. **Is `{entry_id}` distinct from its neighbours?** Could a blind reader "
             "attribute a render to it rather than to the entry beside it?")
    L.append("3. **Are the failure modes this entry over-hitting itself**, rather than someone "
             "misusing it?")
    L.append("4. **Do the tells describe what the renders actually do?** Spot-check one render.")
    L.append(f"5. **Is `{axis}` the right axis?** Voice is what does not change; tone is what "
             "changes per piece.")
    L.append("6. **Would you defend `stable` on this publicly?** If not, `draft` is the honest "
             "answer and costs nothing.")
    L.append("")
    L.append("```")
    L.append(f"entry:    {entry_id}")
    L.append(f"decision: stable | draft | edit-then-stable")
    L.append(f"notes:")
    L.append("```")
    L.append("")
    return "\n".join(L), flags


def write_ledger(catalog, results):
    """A tracked record of what was decided. The packets are scaffolding; this is the audit trail."""
    L = []
    L.append("# GATE 1 review ledger")
    L.append("")
    L.append("> The audit trail for the v1.0 `review_status` review (GATE 1). Packets are")
    L.append("> generated working artifacts under gitignored `_local/review-packets/`; this")
    L.append("> file is the tracked record of what was actually decided and why.")
    L.append(">")
    L.append("> Regenerate packets with `python tools/review_packet.py`.")
    L.append("")
    L.append("**Rule:** an entry may only be `stable` after a maintainer has reviewed it. "
             "`draft` is always the honest fallback and costs nothing. Per the marketing "
             "plan, if the review cannot be completed in a reasonable window the launch "
             "slips; entries are not relabelled to make a gate go green.")
    L.append("")
    flagged = sum(1 for _, f in results.items() if f)
    L.append(f"**Scope:** {len(results)} entries carrying `review_status: stable`. "
             f"{flagged} carry at least one flag.")
    L.append("")
    L.append("## Decisions")
    L.append("")
    L.append("| Entry | Axis | Flags | Decision | Date | Notes |")
    L.append("|---|---|---|---|---|---|")
    for entry_id in sorted(results):
        axis, _ = catalog[entry_id]
        n = len(results[entry_id])
        L.append(f"| `{entry_id}` | {axis} | {n if n else '-'} | | | |")
    L.append("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0])
    ap.add_argument("--axis", choices=sorted(AXES), help="Only this axis")
    ap.add_argument("--entry", help="Only this entry id")
    ap.add_argument("--status", default="stable",
                    help="Only entries at this review_status (default: stable; 'any' for all)")
    ap.add_argument("--ledger", action="store_true", help="Also (re)write the tracked ledger")
    args = ap.parse_args()

    catalog = load_all()
    targets = {}
    for entry_id, (axis, fm) in catalog.items():
        if args.axis and axis != args.axis:
            continue
        if args.entry and entry_id != args.entry:
            continue
        if args.status != "any" and fm.get("review_status") != args.status:
            continue
        targets[entry_id] = (axis, fm)

    if not targets:
        print("[WARN] no entries matched", file=sys.stderr)
        return 1

    results = {}
    for entry_id, (axis, fm) in sorted(targets.items()):
        body, flags = render_packet(entry_id, axis, fm, catalog)
        out = OUT_DIR / axis / f"{entry_id}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body, encoding="utf-8")
        results[entry_id] = flags

    flagged = {k: v for k, v in results.items() if v}
    total_flags = sum(len(v) for v in results.values())

    # An index ordered by flag count: the entries most likely to need a real
    # decision come first, so a partial review session still spends its time well.
    idx = ["# Review packets", "",
           f"{len(results)} entries, {total_flags} flags across {len(flagged)} of them.",
           "", "Ordered by flag count: start at the top, where the questions are.", "",
           "| Entry | Axis | Flags | Packet |", "|---|---|---|---|"]
    for entry_id in sorted(results, key=lambda e: (-len(results[e]), e)):
        axis = targets[entry_id][0]
        idx.append(f"| `{entry_id}` | {axis} | {len(results[entry_id]) or '-'} | "
                   f"[{axis}/{entry_id}.md]({axis}/{entry_id}.md) |")
    findings = catalog_level_findings(catalog)
    idx += [
        "",
        "## Catalog-level findings",
        "",
        f"Handled once rather than re-decided in every packet: "
        f"{len(findings['one_way_confusable'])} one-way `confusable_with` links, and "
        f"{len(findings['no_confusable'])} stable entries with no declared near-neighbour. "
        f"See [CATALOG-FINDINGS.md](CATALOG-FINDINGS.md).",
    ]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "INDEX.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    (OUT_DIR / "CATALOG-FINDINGS.md").write_text(
        render_catalog_report(catalog, findings), encoding="utf-8"
    )

    print(f"[OK] wrote {len(results)} packets to {OUT_DIR.relative_to(REPO_ROOT)}")
    print(f"[OK] catalog-level: {len(findings['one_way_confusable'])} one-way confusable_with, "
          f"{len(findings['no_confusable'])} with no near-neighbour")
    print(f"[OK] {total_flags} flags across {len(flagged)} entries "
          f"({len(results) - len(flagged)} clean)")
    if flagged:
        top = Counter({k: len(v) for k, v in flagged.items()}).most_common(5)
        print("     most-flagged: " + ", ".join(f"{k} ({n})" for k, n in top))

    if args.ledger:
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        LEDGER.write_text(write_ledger(catalog, results), encoding="utf-8")
        print(f"[OK] wrote ledger to {LEDGER.relative_to(REPO_ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
