"""Tests for Gate 2 - the pedagogical-bar SUBSTANCE check in tools/validate.py.

ADR 0009 (gate-critical subset) ratified three frontmatter fields the E1
adherence gate consumes: `tells`, `anti_patterns`, `failure_modes`. Ownership
is split:

- The universal JSON schema owns PRESENCE, COUNT BAND, item TYPE, and object
  SHAPE (the fields are required, with minItems/maxItems and per-item required
  subkeys). `check_schema_validation` reports those, once.
- `check_pedagogical_bar` (this module's target) owns the one bar the schema
  cannot express: SUBSTANCE. A JSON string can be "" or "   " and still satisfy
  a string-type + count-band check, yet carry no real content.

To avoid duplicating schema errors (the P3 finding from the 2026-06-22 review),
the substance check stays silent on mis-shaped values (absent field, non-list,
non-string item, missing/non-string subfield) and reports an empty/whitespace
string only where the surrounding shape is otherwise valid. These tests pin
that boundary.

id_map maps entry ID -> (axis, frontmatter_dict), the same convention as
test_taxonomy_codification.py.
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
# Substance: the gap only this check can close
# ---------------------------------------------------------------------------

def test_empty_string_tell_is_error():
    errors = validate.check_pedagogical_bar(_id_map(tells=["a", "b", "c", "d", ""]))
    assert any("tells" in e for e in errors)


def test_whitespace_only_tell_is_error():
    errors = validate.check_pedagogical_bar(_id_map(tells=["a", "b", "c", "d", "   "]))
    assert any("tells" in e for e in errors)


def test_empty_anti_pattern_why_is_error():
    errors = validate.check_pedagogical_bar(_id_map(anti_patterns=[
        {"pattern": "p1", "why": ""},
        {"pattern": "p2", "why": "w2"},
    ]))
    assert any("anti_patterns" in e and "why" in e for e in errors)


def test_whitespace_only_failure_mode_mitigation_is_error():
    errors = validate.check_pedagogical_bar(_id_map(failure_modes=[
        {"mode": "m1", "mitigation": "   "},
        {"mode": "m2", "mitigation": "x2"},
    ]))
    assert any("failure_modes" in e and "mitigation" in e for e in errors)


# ---------------------------------------------------------------------------
# Severity: substance violations are error-level (they fail the build)
# ---------------------------------------------------------------------------

def test_substance_violations_are_errors():
    errors = validate.check_pedagogical_bar(_id_map(tells=["a", "b", "c", "d", ""]))
    assert errors
    assert all(e.startswith("[ERROR]") for e in errors)


# ---------------------------------------------------------------------------
# Ownership boundary: shape violations belong to the schema, NOT this check,
# so this check does not double-report them (the P3 finding, 2026-06-22).
# ---------------------------------------------------------------------------

def test_missing_field_is_left_to_the_schema():
    # An absent field is the schema's required-check to report; Gate 2 stays
    # silent so a single root cause is not flagged twice.
    assert validate.check_pedagogical_bar(_id_map_missing("tells")) == []


def test_count_band_violation_is_left_to_the_schema():
    # Too few tells (4 < 5) is the schema's minItems job, not a substance issue.
    assert validate.check_pedagogical_bar(_id_map(tells=["a", "b", "c", "d"])) == []


def test_non_list_field_is_left_to_the_schema():
    assert validate.check_pedagogical_bar(_id_map(tells="not a list")) == []


def test_missing_subfield_is_left_to_the_schema():
    # A missing `why` key is the schema's required-subkey job; only a PRESENT
    # but empty string is a substance violation.
    errors = validate.check_pedagogical_bar(_id_map(anti_patterns=[
        {"pattern": "p1"},  # no why key
        {"pattern": "p2", "why": "w2"},
    ]))
    assert errors == []


# ---------------------------------------------------------------------------
# The real catalog must pass Gate 2 (or the tightening breaks the build)
# ---------------------------------------------------------------------------

def test_real_catalog_passes_gate2():
    _, id_map = validate.check_frontmatter_parseable()
    assert validate.check_pedagogical_bar(id_map) == []
