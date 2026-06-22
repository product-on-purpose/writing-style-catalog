"""Tests for Gate 2 - the pedagogical-bar substance check in tools/validate.py.

ADR 0009 (gate-critical subset) ratified three frontmatter fields the E1
adherence gate consumes: `tells`, `anti_patterns`, `failure_modes`. The JSON
schema enforces their presence, count band, and shape once they are required
(F2 tighten-to-required, 2026-06-22). What the schema cannot express is
SUBSTANCE: a JSON string can be "" or "   " and still satisfy a string-type
plus count-band check. `check_pedagogical_bar` (Gate 2) closes that gap with
error-level, gate-named messages, mirroring how `check_taxonomy_membership`
adds the cross-field rules the schema cannot express.

These tests follow the same id_map convention as test_taxonomy_codification.py:
id_map maps entry ID -> (axis, frontmatter_dict).
"""
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

import validate  # noqa: E402


def _good_fields(**overrides):
    """A frontmatter dict carrying all three pedagogical fields, well-formed."""
    fields = {
        "tells": [f"tell {i}" for i in range(5)],  # 5 in the 5-7 band
        "anti_patterns": [
            {"pattern": "overusing the move", "why": "it stops being distinctive"},
            {"pattern": "ignoring the reader", "why": "it breaks the register"},
        ],
        "failure_modes": [
            {"mode": "tips into caricature", "mitigation": "pull back to the register"},
            {"mode": "loses the throughline", "mitigation": "restate the core claim"},
        ],
    }
    fields.update(overrides)
    return fields


def _id_map(**overrides):
    return {"x": ("voice", _good_fields(**overrides))}


def _id_map_missing(field):
    fields = _good_fields()
    del fields[field]
    return {"x": ("voice", fields)}


# ---------------------------------------------------------------------------
# Clean entries pass
# ---------------------------------------------------------------------------

def test_clean_entry_has_no_errors():
    assert validate.check_pedagogical_bar(_id_map()) == []


# ---------------------------------------------------------------------------
# Presence: a missing field is an error
# ---------------------------------------------------------------------------

def test_missing_tells_is_error():
    errors = validate.check_pedagogical_bar(_id_map_missing("tells"))
    assert any("tells" in e for e in errors)


def test_missing_anti_patterns_is_error():
    errors = validate.check_pedagogical_bar(_id_map_missing("anti_patterns"))
    assert any("anti_patterns" in e for e in errors)


def test_missing_failure_modes_is_error():
    errors = validate.check_pedagogical_bar(_id_map_missing("failure_modes"))
    assert any("failure_modes" in e for e in errors)


# ---------------------------------------------------------------------------
# Substance: the gap the schema cannot express
# ---------------------------------------------------------------------------

def test_empty_string_tell_is_error():
    errors = validate.check_pedagogical_bar(_id_map(tells=["a", "b", "c", "d", ""]))
    assert errors


def test_whitespace_only_tell_is_error():
    errors = validate.check_pedagogical_bar(_id_map(tells=["a", "b", "c", "d", "   "]))
    assert errors


def test_empty_anti_pattern_why_is_error():
    errors = validate.check_pedagogical_bar(_id_map(anti_patterns=[
        {"pattern": "p1", "why": ""},
        {"pattern": "p2", "why": "w2"},
    ]))
    assert errors


def test_whitespace_only_failure_mode_mitigation_is_error():
    errors = validate.check_pedagogical_bar(_id_map(failure_modes=[
        {"mode": "m1", "mitigation": "   "},
        {"mode": "m2", "mitigation": "x2"},
    ]))
    assert errors


# ---------------------------------------------------------------------------
# Count band
# ---------------------------------------------------------------------------

def test_too_few_tells_is_error():
    errors = validate.check_pedagogical_bar(_id_map(tells=["a", "b", "c", "d"]))  # 4 < 5
    assert any("tells" in e for e in errors)


def test_too_many_failure_modes_is_error():
    four = [{"mode": f"m{i}", "mitigation": f"x{i}"} for i in range(4)]  # 4 > 3
    errors = validate.check_pedagogical_bar(_id_map(failure_modes=four))
    assert any("failure_modes" in e for e in errors)


# ---------------------------------------------------------------------------
# Severity: violations are error-level (they contribute to the exit code)
# ---------------------------------------------------------------------------

def test_violations_are_errors():
    errors = validate.check_pedagogical_bar(_id_map(tells=[]))
    assert errors
    assert all(e.startswith("[ERROR]") for e in errors)


# ---------------------------------------------------------------------------
# The real catalog must pass Gate 2 (or the tightening breaks the build)
# ---------------------------------------------------------------------------

def test_real_catalog_passes_gate2():
    _, id_map = validate.check_frontmatter_parseable()
    assert validate.check_pedagogical_bar(id_map) == []
