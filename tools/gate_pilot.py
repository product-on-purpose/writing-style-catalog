"""Gate pilot: a no-new-infra prototype of the E1 adherence gate's Gate 1
(blind distinguishability) plus the C1 restraint check, run against the
trusted 60.

This is NOT the production tools/adherence-gate.py (Slices 2-3 of the gate
build). It is a deterministic harness the maintainer drives by hand with
subagents: isolated Claude subagents render samples, the Codex companion
judges blind, and this module assembles and scores the packet. Its purpose is
to prove the judge architecture works and to calibrate the C1 bar against the
60 before any paid LLM integration (option C) is decided.

Reuses adherence_gate (neighbors) and anchor_topics (topic); never re-parses
entries. Renders one axis at a time (voice for the first run).
"""
from __future__ import annotations

import random
import string
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from adherence_gate import load_catalog, gate_neighbors  # noqa: E402,F401
import anchor_topics  # noqa: E402


def render_instruction(fm: dict, topic_label: str) -> str:
    """The single-axis render prompt for one entry.

    Concatenates the entry's llm_instruction_phrasing with the fixed writing
    task, the same shape build-instruction.compose_instruction produces for a
    one-axis selection, but from the frontmatter dict load_catalog already
    holds (no file re-read).
    """
    phrasing = (fm.get("llm_instruction_phrasing") or "").strip()
    return f"{phrasing}\n\nWrite about: {topic_label}"


@dataclass(frozen=True)
class Slot:
    """One presentation slot: a blind label, the entry it secretly renders,
    and that entry's render instruction."""
    label: str
    entry_id: str
    instruction: str


@dataclass(frozen=True)
class RenderPacket:
    """A blind render packet: the candidate, the axis under test, the topic,
    and the shuffled labeled slots. `mapping` is the hidden answer key the
    judge never sees."""
    candidate: str
    axis: str
    topic_slug: str
    topic_label: str
    slots: tuple[Slot, ...]

    @property
    def mapping(self) -> dict[str, str]:
        return {s.label: s.entry_id for s in self.slots}


def build_render_packet(candidate_id, neighbor_ids, topic_slug, id_map, seed=0):
    """Render the candidate plus its neighbors into shuffled, labeled slots.

    Entries are deduped, candidate-first; the candidate is removed from the
    neighbor list if present. The order is shuffled deterministically by `seed`
    so the judge cannot infer attribution from position, while tests stay
    reproducible.
    """
    axis, _ = id_map[candidate_id]
    topic_label = anchor_topics.label_of(topic_slug)
    if topic_label is None:
        raise ValueError(f"unknown anchor topic: {topic_slug}")

    # Candidate first, then neighbors; dedup preserves first occurrence, so a
    # neighbor equal to the candidate is dropped (the candidate is already seen).
    ordered: list[str] = []
    seen: set[str] = set()
    for eid in [candidate_id] + list(neighbor_ids):
        if eid in seen:
            continue
        seen.add(eid)
        ordered.append(eid)

    shuffled = list(ordered)
    random.Random(seed).shuffle(shuffled)

    labels = list(string.ascii_uppercase)
    slots = tuple(
        Slot(label=labels[i], entry_id=eid,
             instruction=render_instruction(id_map[eid][1], topic_label))
        for i, eid in enumerate(shuffled)
    )
    return RenderPacket(
        candidate=candidate_id, axis=axis,
        topic_slug=topic_slug, topic_label=topic_label, slots=slots,
    )


def _format_failure_modes(fm: dict) -> str:
    """Format the failure_modes array from a frontmatter dict as indented list."""
    lines = []
    for item in fm.get("failure_modes") or []:
        mode = (item.get("mode") or "").strip()
        mitigation = (item.get("mitigation") or "").strip()
        lines.append(f"      - {mode} (mitigation: {mitigation})")
    return "\n".join(lines) if lines else "      - (none declared)"


def build_judge_prompt(packet: RenderPacket, samples: dict, id_map: dict) -> str:
    """Build the blind judge prompt.

    Lists the N options in alphabetical id order (so option order leaks nothing
    about slot order), presents the samples by label, and asks for strict JSON.
    The label-to-entry mapping is never stated.
    """
    option_ids = sorted(s.entry_id for s in packet.slots)
    option_lines = []
    for i, eid in enumerate(option_ids, start=1):
        fm = id_map[eid][1]
        name = fm.get("name", eid)
        one_liner = (fm.get("one_liner") or "").strip()
        option_lines.append(
            f"  {i}. {name} ({eid}): {one_liner}\n"
            f"     Known failure modes (over-doing this {packet.axis}):\n"
            f"{_format_failure_modes(fm)}"
        )
    options_block = "\n".join(option_lines)

    sample_lines = []
    for s in packet.slots:
        sample_lines.append(f"[{s.label}]\n{samples[s.label]}")
    samples_block = "\n\n".join(sample_lines)

    n = len(packet.slots)
    axis = packet.axis
    return (
        "You are a blind judge in a writing-style attribution test. Judge only "
        "the prose; the sample order is randomized and carries no signal.\n\n"
        f"AXIS UNDER TEST: {axis}\n"
        f"All {n} samples were written about the same topic: "
        f"\"{packet.topic_label}\". They differ only in {axis}.\n\n"
        f"THE {n} POSSIBLE {axis.upper()}S (alphabetical; exactly one sample is "
        f"written in each):\n"
        f"{options_block}\n\n"
        "THE SAMPLES:\n\n"
        f"{samples_block}\n\n"
        "TASKS:\n"
        f"1. ATTRIBUTION (forced choice, one-to-one): match each sample label to "
        f"exactly one {axis} id from the list above.\n"
        "2. DISTINGUISHABILITY: rate the set as \"identical\", \"subtle\", or "
        "\"clear\".\n"
        f"3. RESTRAINT: for each sample, judged ONLY against the failure modes of "
        f"the {axis} you attributed it to, is it the genuine register (\"pass\"), "
        "a borderline over-hit (\"weak\"), or a caricature of its own failure mode "
        "(\"fail\")?\n\n"
        "Return ONLY this JSON, nothing outside it:\n"
        "{\n"
        '  "attribution": {"A": "<id>", ...},\n'
        '  "distinguishability": "identical|subtle|clear",\n'
        '  "restraint": {"A": "pass|weak|fail", ...},\n'
        '  "rationale": "<2-4 sentences>"\n'
        "}\n"
    )


def score_attribution(packet: RenderPacket, attribution: dict) -> dict:
    """Compare the judge's attribution to the hidden answer key."""
    truth = packet.mapping
    per_slot = []
    correct = 0
    for label in sorted(truth):
        true_id = truth[label]
        guess = attribution.get(label)
        ok = guess == true_id
        correct += 1 if ok else 0
        per_slot.append(
            {"label": label, "true": true_id, "guess": guess, "correct": ok}
        )
    n = len(truth)
    return {
        "n": n,
        "correct": correct,
        "accuracy": (correct / n) if n else 0.0,
        "per_slot": per_slot,
    }


def build_run_record(packet, samples, judge_json, score) -> dict:
    """Assemble the full inspectable run record (JSON-serializable)."""
    return {
        "candidate": packet.candidate,
        "axis": packet.axis,
        "topic_slug": packet.topic_slug,
        "topic_label": packet.topic_label,
        "mapping": packet.mapping,
        "samples": dict(samples),
        "attribution": judge_json.get("attribution", {}),
        "distinguishability": judge_json.get("distinguishability"),
        "restraint": judge_json.get("restraint", {}),
        "rationale": judge_json.get("rationale", ""),
        "score": score,
    }


def nearest_neighbors(candidate_id, id_map, limit=2) -> list[str]:
    """The candidate's nearest gate adversaries: declared confusables first,
    then remaining tree neighbors, truncated to `limit`. Mirrors the smoke
    test's '2-3 nearest neighbors' framing."""
    ns = gate_neighbors(candidate_id, id_map)
    ordered = list(ns.confusable) + [n for n in ns.neighbors if n not in ns.confusable]
    return ordered[:limit]


def main(argv=None) -> int:
    import argparse
    parser = argparse.ArgumentParser(
        description="Inspect a gate-pilot render packet and judge prompt."
    )
    parser.add_argument("--candidate", required=True, help="Candidate entry id")
    parser.add_argument("--topic", required=True, help="Anchor-topic slug")
    parser.add_argument("--limit", type=int, default=2, help="Nearest neighbors")
    parser.add_argument("--seed", type=int, default=0, help="Shuffle seed")
    args = parser.parse_args(argv)

    id_map = load_catalog()
    if args.candidate not in id_map:
        print(f"[ERROR] unknown entry id: {args.candidate}", file=sys.stderr)
        return 1

    near = nearest_neighbors(args.candidate, id_map, limit=args.limit)
    packet = build_render_packet(args.candidate, near, args.topic, id_map, seed=args.seed)

    print(f"candidate: {packet.candidate} (axis: {packet.axis})")
    print(f"topic: {packet.topic_slug} - {packet.topic_label}")
    print(f"neighbors: {', '.join(near)}\n")
    for s in packet.slots:
        print(f"=== SLOT {s.label} -> {s.entry_id} ===")
        print(s.instruction)
        print()
    placeholders = {s.label: f"<SAMPLE label={s.label} - paste generated prose here>"
                    for s in packet.slots}
    print("=== BLIND JUDGE PROMPT ===")
    print(build_judge_prompt(packet, placeholders, id_map))
    return 0


if __name__ == "__main__":
    sys.exit(main())
