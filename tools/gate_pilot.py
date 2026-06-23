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
