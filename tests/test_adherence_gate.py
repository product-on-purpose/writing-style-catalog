"""Tests for the E1 adherence gate (tools/adherence_gate.py).

Slice 1 covers the deterministic neighbor lookup: given a candidate entry and
the catalog id_map, compute the gate neighbor set Gate 1 renders against, per
the ratified taxonomy rules (Q4 tree-siblings-plus-confusable, Gate 1
same-family/same-subfamily, Q5 whole-axis for flat tone/style). All logic is
deterministic and unit-tested against hand-built synthetic catalogs, plus smoke
tests against the real 60.
"""
import sys
from pathlib import Path

import pytest

TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

import adherence_gate as gate  # noqa: E402


def _entry(axis, **fields):
    """A minimal (axis, frontmatter) tuple as id_map stores it."""
    return (axis, fields)


# ---------------------------------------------------------------------------
# load_catalog - the quiet id_map builder
# ---------------------------------------------------------------------------

def test_load_catalog_indexes_real_entries():
    id_map = gate.load_catalog()
    # The frozen baseline is 60 entries across four axes.
    assert len(id_map) >= 60
    axes = {axis for axis, _ in id_map.values()}
    assert axes == {"voice", "tone", "style", "format"}
    for axis, fm in id_map.values():
        assert axis in ("voice", "tone", "style", "format")
        assert isinstance(fm, dict)


# ---------------------------------------------------------------------------
# gate_neighbors - tree siblings (Gate 1, family/domain scoped)
# ---------------------------------------------------------------------------

def test_format_siblings_share_domain_and_family():
    id_map = {
        "readme": _entry("format", domain="professional", family="instruction"),
        "tutorial": _entry("format", domain="professional", family="instruction"),
        "adr": _entry("format", domain="professional", family="deliberation"),
        "love-letter": _entry("format", domain="personal", family="correspondence"),
    }
    ns = gate.gate_neighbors("readme", id_map)
    assert ns.siblings == ("tutorial",)        # same domain + family
    assert "adr" not in ns.neighbors           # different family
    assert "love-letter" not in ns.neighbors   # different domain


def test_voice_siblings_share_family():
    id_map = {
        "coach": _entry("voice", family="care"),
        "mentor": _entry("voice", family="care"),
        "scholar": _entry("voice", family="expert"),
    }
    ns = gate.gate_neighbors("coach", id_map)
    assert ns.siblings == ("mentor",)
    assert "scholar" not in ns.neighbors


def test_candidate_excluded_from_neighbors():
    id_map = {"a": _entry("voice", family="care"), "b": _entry("voice", family="care")}
    ns = gate.gate_neighbors("a", id_map)
    assert "a" not in ns.neighbors


# ---------------------------------------------------------------------------
# gate_neighbors - declared confusable_with (Q4), same-axis only
# ---------------------------------------------------------------------------

def test_declared_confusable_included():
    id_map = {
        "one-pager": _entry("format", domain="professional", family="brief",
                            confusable_with=["prd"]),
        "prd": _entry("format", domain="professional", family="deliberation"),
    }
    ns = gate.gate_neighbors("one-pager", id_map)
    assert "prd" in ns.confusable
    assert "prd" in ns.neighbors  # cross-family but declared confusable (Q4)


def test_cross_axis_confusable_excluded():
    # Gate 1 is single-axis-varied; a cross-axis edge is not a Gate-1 adversary.
    id_map = {
        "decision-log": _entry("style", confusable_with=["adr"]),
        "adr": _entry("format", domain="professional", family="deliberation"),
    }
    ns = gate.gate_neighbors("decision-log", id_map)
    assert "adr" not in ns.neighbors


def test_unknown_confusable_ref_ignored():
    id_map = {"a": _entry("voice", family="care", confusable_with=["ghost"])}
    ns = gate.gate_neighbors("a", id_map)
    assert ns.confusable == ()


def test_neighbors_union_dedupes_sibling_that_is_also_confusable():
    id_map = {
        "a": _entry("voice", family="care", confusable_with=["b"]),
        "b": _entry("voice", family="care"),
    }
    ns = gate.gate_neighbors("a", id_map)
    assert ns.neighbors == ("b",)  # b is both a sibling and declared; counted once


# ---------------------------------------------------------------------------
# gate_neighbors - flat axes (Q5) and subfamily narrowing (Gate 1 / A2)
# ---------------------------------------------------------------------------

def test_flat_axis_renders_whole_axis():
    id_map = {
        "terse": _entry("tone"),
        "warm": _entry("tone"),
        "playful": _entry("tone"),
        "dialectic": _entry("style"),  # different axis, excluded
    }
    ns = gate.gate_neighbors("terse", id_map)
    assert set(ns.siblings) == {"warm", "playful"}
    assert "dialectic" not in ns.neighbors


def test_subfamily_narrowing_past_trigger():
    # A 12-member family narrows to same-subfamily neighbors.
    id_map = {}
    for i in range(6):
        id_map[f"ref{i}"] = _entry("format", domain="professional",
                                   family="instruction", subfamily="reference")
    for i in range(6):
        id_map[f"tut{i}"] = _entry("format", domain="professional",
                                   family="instruction", subfamily="tutorial")
    ns = gate.gate_neighbors("ref0", id_map)
    # 12 members total -> narrowed to the 5 other `reference` siblings only.
    assert set(ns.siblings) == {"ref1", "ref2", "ref3", "ref4", "ref5"}


def test_below_trigger_keeps_whole_family():
    id_map = {
        "ref0": _entry("format", domain="professional", family="instruction",
                       subfamily="reference"),
        "tut0": _entry("format", domain="professional", family="instruction",
                       subfamily="tutorial"),
    }
    ns = gate.gate_neighbors("ref0", id_map)
    assert set(ns.siblings) == {"tut0"}  # 2 members, no narrowing


def test_trigger_with_missing_candidate_subfamily_raises():
    # A 12+ member family whose candidate lacks a subfamily is an invalid
    # catalog state (validate.py errors on it). The gate must fail loud, not
    # silently fall back to a too-broad whole-family neighbor set.
    id_map = {}
    for i in range(11):
        id_map[f"m{i}"] = _entry("format", domain="professional",
                                 family="instruction", subfamily="reference")
    id_map["candidate"] = _entry("format", domain="professional",
                                 family="instruction")  # no subfamily, family at 12
    with pytest.raises(ValueError):
        gate.gate_neighbors("candidate", id_map)


# ---------------------------------------------------------------------------
# CLI - the inspector entry point
# ---------------------------------------------------------------------------

def test_cli_prints_neighbor_report_for_real_entry(capsys):
    some_entry = next(iter(gate.load_catalog()))
    rc = gate.main(["--entry", some_entry])
    out = capsys.readouterr().out
    assert rc == 0
    assert some_entry in out
    assert "neighbors" in out


def test_cli_errors_on_unknown_entry(capsys):
    rc = gate.main(["--entry", "no-such-entry-xyz"])
    err = capsys.readouterr().err
    assert rc == 1
    assert "unknown entry" in err


# ---------------------------------------------------------------------------
# Real-catalog properties (every entry yields a valid, same-axis neighbor set)
# ---------------------------------------------------------------------------

def test_every_real_entry_has_a_computable_neighbor_set():
    id_map = gate.load_catalog()
    for entry_id in id_map:
        ns = gate.gate_neighbors(entry_id, id_map)
        assert ns.candidate == entry_id
        assert entry_id not in ns.neighbors
        for n in ns.neighbors:
            assert n in id_map
            assert id_map[n][0] == ns.axis  # neighbors are same-axis


def test_real_confusable_edges_resolve_within_axis():
    id_map = gate.load_catalog()
    for entry_id, (axis, _fm) in id_map.items():
        ns = gate.gate_neighbors(entry_id, id_map)
        for c in ns.confusable:
            assert id_map[c][0] == axis
