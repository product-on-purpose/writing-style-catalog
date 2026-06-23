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
