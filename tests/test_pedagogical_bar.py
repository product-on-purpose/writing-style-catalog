"""Tests for the pedagogical entry bar (ADR 0009, gate-critical subset).

ADR 0009 adopts three axis-neutral, optional frontmatter fields that the E1
adherence gate consumes: `failure_modes` (the C1 restraint check renders against
it), `anti_patterns` and `tells` (Gate 2). They live in the universal base
schema. Optional now (an entry may omit them), shape-enforced when present, and
tightened to required once the 60 are backfilled (the F2 optional-then-tighten
path). These tests pin the schema contract: present-and-well-formed validates,
absent validates, present-and-malformed is rejected.
"""
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[1]
UNIVERSAL_SCHEMA = REPO_ROOT / "schemas" / "entry.universal.schema.json"


def _validator():
    schema = json.loads(UNIVERSAL_SCHEMA.read_text(encoding="utf-8"))
    return Draft202012Validator(schema)


def _base(**overrides):
    """A minimal instance satisfying the universal schema's required fields."""
    entry = {
        "id": "test-entry",
        "name": "Test Entry",
        "axis": "voice",
        "one_liner": "A test entry.",
        "description": "A test entry used to exercise the schema.",
        "pairs_well_with": ["other-entry"],
        "avoid_with": [],
        "confusable_with": [],
        "when_to_use": ["when testing"],
        "when_not_to_use": ["in production"],
        "llm_instruction_phrasing": "Write like a test.",
        "tags": [],
        "review_status": "draft",
    }
    entry.update(overrides)
    return entry


def _is_valid(instance):
    return _validator().is_valid(instance)


# Well-formed sample fields (the shapes ADR 0009 specifies).
GOOD_TELLS = [f"tell {i}" for i in range(5)]  # 5 strings (in the 5-7 band)
GOOD_ANTI_PATTERNS = [
    {"pattern": "overusing the move", "why": "it stops being distinctive"},
    {"pattern": "ignoring the reader", "why": "it breaks the register"},
]
GOOD_FAILURE_MODES = [
    {"mode": "tips into caricature", "mitigation": "pull back to the genuine register"},
    {"mode": "loses the throughline", "mitigation": "restate the core claim"},
]


# ---------------------------------------------------------------------------
# Optional: absent fields still validate
# ---------------------------------------------------------------------------

def test_entry_without_pedagogical_fields_is_valid():
    assert _is_valid(_base())


# ---------------------------------------------------------------------------
# Present and well-formed validates
# ---------------------------------------------------------------------------

def test_entry_with_all_three_fields_is_valid():
    assert _is_valid(_base(
        tells=GOOD_TELLS,
        anti_patterns=GOOD_ANTI_PATTERNS,
        failure_modes=GOOD_FAILURE_MODES,
    ))


# ---------------------------------------------------------------------------
# Present and malformed is rejected (the shape constraints)
# ---------------------------------------------------------------------------

def test_anti_pattern_missing_why_is_rejected():
    assert not _is_valid(_base(anti_patterns=[{"pattern": "no why given"}]))


def test_failure_mode_missing_mitigation_is_rejected():
    assert not _is_valid(_base(failure_modes=[{"mode": "no mitigation given"}]))


def test_tells_must_be_strings():
    assert not _is_valid(_base(tells=[1, 2, 3, 4, 5]))


def test_too_few_tells_is_rejected():
    assert not _is_valid(_base(tells=["only", "four", "tells", "here"]))  # 4 < 5


def test_too_many_failure_modes_is_rejected():
    four = [{"mode": f"m{i}", "mitigation": f"x{i}"} for i in range(4)]  # 4 > 3
    assert not _is_valid(_base(failure_modes=four))


def test_too_few_anti_patterns_is_rejected():
    assert not _is_valid(_base(anti_patterns=[{"pattern": "only one", "why": "x"}]))  # 1 < 2
