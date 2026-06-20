"""Tests for Phase 1 taxonomy codification.

Covers the v2 controlled vocabulary in tools/taxonomy.py (ratified A1:
5 format domains with `personal` not `relational`, 16 domain-scoped
families, 5 voice families with `pastoral` folded into `care`, the
governed 7-facet enum, and coverage bands), the optional-with-warning
cross-field checks in tools/validate.py (check_taxonomy_membership and
check_faceted_tags, both warnings per F2), and the per-cell coverage
ledger in tools/build-indexes.py.
"""
import importlib.util
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

import taxonomy  # noqa: E402
import validate  # noqa: E402


def _load_build_indexes():
    """Load the hyphenated build-indexes.py module by path."""
    spec = importlib.util.spec_from_file_location(
        "build_indexes", TOOLS_DIR / "build-indexes.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _entry(axis, **fields):
    """A minimal (axis, frontmatter) tuple as id_map stores it."""
    return (axis, fields)


# ---------------------------------------------------------------------------
# taxonomy.py - the v2 controlled vocabulary
# ---------------------------------------------------------------------------

def test_format_domains_are_the_five_v2_values():
    assert set(taxonomy.FORMAT_DOMAINS) == {
        "professional", "public", "personal", "ceremonial", "contemplative",
    }


def test_relational_domain_was_renamed_personal():
    assert taxonomy.is_valid_format_domain("personal")
    assert not taxonomy.is_valid_format_domain("relational")


def test_family_is_scoped_to_its_domain():
    assert taxonomy.is_valid_format_family("professional", "instruction")
    assert taxonomy.is_valid_format_family("personal", "correspondence")
    # correspondence belongs to personal, not professional
    assert not taxonomy.is_valid_format_family("professional", "correspondence")


def test_voice_families_are_the_five_with_pastoral_folded_into_care():
    assert set(taxonomy.VOICE_FAMILIES) == {
        "expert", "care", "principal", "witness", "dissident",
    }
    assert taxonomy.is_valid_voice_family("care")
    # pastoral is no longer a top-level family; it is a care subfamily
    assert not taxonomy.is_valid_voice_family("pastoral")
    assert taxonomy.is_valid_voice_subfamily("care", "pastoral")


def test_faceted_tag_validates_against_the_closed_enum():
    assert taxonomy.is_valid_facet_tag("channel:slack")
    assert taxonomy.is_valid_facet_tag("modality:prose")
    # value outside the enum fails
    assert not taxonomy.is_valid_facet_tag("channel:carrier-pigeon")
    # unknown facet prefix fails
    assert not taxonomy.is_valid_facet_tag("vibe:cozy")


def test_free_text_tags_are_not_faceted():
    assert not taxonomy.is_faceted_tag("longform")
    assert taxonomy.is_faceted_tag("channel:email")


# ---------------------------------------------------------------------------
# validate.py - check_taxonomy_membership (warnings, never errors)
# ---------------------------------------------------------------------------

def test_membership_clean_when_family_belongs_to_domain():
    id_map = {
        "readme": _entry("format", domain="professional", family="instruction"),
        "coach": _entry("voice", family="care"),
    }
    warnings = validate.check_taxonomy_membership(id_map)
    assert warnings == []


def test_membership_warns_when_family_not_in_domain():
    id_map = {
        "x": _entry("format", domain="professional", family="correspondence"),
    }
    warnings = validate.check_taxonomy_membership(id_map)
    assert any("correspondence" in w and "professional" in w for w in warnings)


def test_membership_warns_when_format_has_family_without_domain():
    id_map = {
        "x": _entry("format", family="instruction"),
    }
    warnings = validate.check_taxonomy_membership(id_map)
    assert any("domain" in w.lower() for w in warnings)


def test_membership_warns_on_invalid_voice_family():
    id_map = {
        "x": _entry("voice", family="pastoral"),
    }
    warnings = validate.check_taxonomy_membership(id_map)
    assert any("pastoral" in w for w in warnings)


def test_membership_violations_are_errors_after_tightening():
    """F2 phase 3: with the backfill complete and A1 ratified, domain/family
    membership is tightened from optional-with-warning to required - a
    violation is an [ERROR] that contributes to the error count."""
    id_map = {"x": _entry("voice", family="not-a-family")}
    issues = validate.check_taxonomy_membership(id_map)
    assert issues
    assert all(i.startswith("[ERROR]") for i in issues)


def test_real_catalog_passes_under_required_mode():
    """Every backfilled entry must validate clean once membership is an
    error-level check, or tightening would break the build."""
    errors = validate.run_all_checks()
    assert errors == []


# ---------------------------------------------------------------------------
# validate.py - check_faceted_tags (warnings, never errors)
# ---------------------------------------------------------------------------

def test_faceted_tags_clean_for_valid_facets():
    id_map = {"x": _entry("format", tags=["channel:slack", "longform"])}
    warnings = validate.check_faceted_tags(id_map)
    assert warnings == []


def test_faceted_tags_warn_on_unknown_facet_or_value():
    id_map = {
        "x": _entry("format", tags=["channel:carrier-pigeon"]),
        "y": _entry("voice", tags=["vibe:cozy"]),
    }
    warnings = validate.check_faceted_tags(id_map)
    assert len(warnings) == 2


def test_faceted_tags_ignore_free_text():
    id_map = {"x": _entry("style", tags=["dialectic", "rhetoric", "longform"])}
    warnings = validate.check_faceted_tags(id_map)
    assert warnings == []


# ---------------------------------------------------------------------------
# build-indexes.py - the per-cell coverage ledger
# ---------------------------------------------------------------------------

def test_coverage_ledger_counts_filled_cells():
    bi = _load_build_indexes()
    entries = [
        {"axis": "format", "domain": "professional", "family": "instruction"},
        {"axis": "format", "domain": "professional", "family": "instruction"},
        {"axis": "format", "domain": "personal", "family": "correspondence"},
        {"axis": "voice", "family": "expert"},
    ]
    ledger = bi.build_coverage_ledger(entries)

    cell = next(
        c for c in ledger["format_cells"]
        if c["domain"] == "professional" and c["family"] == "instruction"
    )
    assert cell["filled"] == 2
    expert = next(f for f in ledger["voice_families"] if f["family"] == "expert")
    assert expert["filled"] == 1


def test_coverage_ledger_counts_unassigned_entries():
    bi = _load_build_indexes()
    entries = [
        {"axis": "format"},  # no domain/family yet (pre-backfill)
        {"axis": "voice"},
    ]
    ledger = bi.build_coverage_ledger(entries)
    assert ledger["unassigned"]["format"] == 1
    assert ledger["unassigned"]["voice"] == 1


# ---------------------------------------------------------------------------
# schemas must mirror the taxonomy.py vocabulary (ADR 0010 section 5.1: the
# enums duplicate the vocab so the schema catches typos; this guards drift)
# ---------------------------------------------------------------------------

def _load_schema(name):
    import json
    p = Path(__file__).resolve().parents[1] / "schemas" / name
    return json.loads(p.read_text(encoding="utf-8"))


def test_format_schema_domain_and_family_enums_match_taxonomy():
    props = _load_schema("format.schema.json")["properties"]
    assert set(props["domain"]["enum"]) == set(taxonomy.FORMAT_DOMAINS)
    assert set(props["family"]["enum"]) == set(taxonomy.all_format_families())


def test_voice_schema_family_enum_matches_taxonomy():
    props = _load_schema("voice.schema.json")["properties"]
    assert set(props["family"]["enum"]) == set(taxonomy.VOICE_FAMILIES)


def test_format_schema_requires_domain_and_family():
    """F2 phase 3: domain and family are required on format entries."""
    schema = _load_schema("format.schema.json")
    assert "domain" in schema.get("required", [])
    assert "family" in schema.get("required", [])


def test_voice_schema_requires_family():
    """F2 phase 3: family is required on voice entries."""
    schema = _load_schema("voice.schema.json")
    assert "family" in schema.get("required", [])
