"""Tests for the GATE 1 review-packet generator (tools/review_packet.py).

The tool's value is entirely in its precision. A packet generator that flags
every entry has not triaged anything, and a flag that turns out to be wrong
teaches the reviewer to skip flags. Both failures happened while building it:

  - The first version flagged one-way `avoid_with` and produced 253 false
    positives, roughly one per entry. ADR 0016 made `avoid_with` symmetric at
    COMPOSITION time (build-instruction.py applies a symmetric union), so one-way
    data is correct by design and there was nothing to flag.
  - A "failure_mode has no over-hit signal" heuristic fired on 38% of failure
    modes with no precision.
  - The misuse detector flagged `user-manual` on the generic phrase "reader who",
    when its failure mode ("the commitment to covering the whole product surface
    drives the manual into exhaustive edge-case documentation") is a textbook
    over-hit.

So these tests pin precision, not just behaviour.
"""
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import review_packet as rp  # noqa: E402


@pytest.fixture(scope="module")
def catalog():
    return rp.load_all()


@pytest.fixture(scope="module")
def stable(catalog):
    return {k: v for k, v in catalog.items() if v[1].get("review_status") == "stable"}


# ---------------------------------------------------------------------------
# Precision: the tool must not flag everything
# ---------------------------------------------------------------------------

def test_most_stable_entries_carry_no_flags(catalog, stable):
    """A triage tool that flags the whole corpus has ranked nothing."""
    flagged = sum(1 for eid, (axis, fm) in stable.items()
                  if rp.compute_flags(eid, axis, fm, catalog))
    ratio = flagged / len(stable)
    assert ratio < 0.20, (
        f"{flagged}/{len(stable)} stable entries flagged ({ratio:.0%}). Above ~20% the "
        "flags stop being triage and start being noise; tighten the heuristics."
    )


def test_one_way_avoid_with_is_never_flagged(catalog, stable):
    """ADR 0016 B1: avoid_with is symmetric at composition time, so one-way data is fine.

    Regression guard for the 253-false-positive version.
    """
    offenders = []
    for eid, (axis, fm) in stable.items():
        for flag in rp.compute_flags(eid, axis, fm, catalog):
            if "avoid_with" in flag:
                offenders.append(f"{eid}: {flag[:80]}")
    assert not offenders, (
        "one-way avoid_with is flagged again. ADR 0016 applies a symmetric union in "
        "build-instruction.py, so a conflict never depends on which side declares it:\n"
        + "\n".join(offenders[:5])
    )


def test_overhit_failure_modes_are_not_flagged_as_misuse(catalog):
    """The user-manual regression: reader-harm language is not a misuse marker."""
    overhit_samples = [
        "Over-comprehensive - the commitment to covering the whole product surface drives "
        "the manual into exhaustive edge-case documentation, so every common task is buried "
        "in variant tables that serve no reader who has just arrived with a single question",
        "Tips from decisive into bossy, asserting calls as if dissent were illegitimate",
        "Warmth thickens until the message is all reassurance and no information",
    ]
    for sample in overhit_samples:
        fm = {"failure_modes": [{"mode": sample, "mitigation": "x"}]}
        flags = rp.compute_flags("probe", "voice", fm, {})
        misuse = [f for f in flags if "misuse" in f]
        assert not misuse, f"over-hit description flagged as misuse: {sample[:70]}"


def test_a_real_misuse_phrasing_is_still_caught():
    """The heuristic must not be tightened into uselessness."""
    fm = {"failure_modes": [
        {"mode": "Applied to a casual internal note, the format reads as bureaucratic",
         "mitigation": "x"}
    ]}
    flags = rp.compute_flags("probe", "format", fm, {})
    assert any("misuse" in f for f in flags), (
        "a failure mode naming an external misapplication should still be flagged"
    )


# ---------------------------------------------------------------------------
# Catalog-level findings stay out of per-entry packets
# ---------------------------------------------------------------------------

def test_confusable_with_is_symmetric_across_the_catalog(catalog):
    """All 101 one-way links were closed on 2026-07-30; keep it that way.

    This assertion was originally the inverse: it pinned the gap's existence so
    the batch task could not be forgotten. The batch is done, so it now guards
    the fixed state. A new one-way link means an entry gained a `confusable_with`
    id without the partner gaining one back, and a reader arriving from that
    partner gets no warning about the confusion.
    """
    one_way = rp.catalog_level_findings(catalog)["one_way_confusable"]
    assert not one_way, (
        "one-way confusable_with links reappeared. Confusability is mutual, and each "
        "back-reference also needs an 'Often confused with' block in the entry body:\n"
        + "\n".join(f"  {e} ({a}) lists {o}, not returned" for e, a, o in one_way[:10])
    )


def test_systematic_findings_stay_out_of_per_entry_packets(catalog, stable):
    """A finding spanning many entries belongs in one report, not in every packet."""
    in_packets = sum(
        1 for eid, (axis, fm) in stable.items()
        for f in rp.compute_flags(eid, axis, fm, catalog)
        if "confusable_with" in f and "one-way" in f
    )
    assert in_packets == 0, (
        "one-way confusable_with is back in per-entry packets; it belongs in "
        "CATALOG-FINDINGS.md so it reads as one task, not a hundred"
    )


def test_every_confusable_id_has_a_prose_block(catalog):
    """The glossary's rule: each confusable id needs an 'Often confused with' block.

    This is why the back-references were prose work rather than a data edit, and
    it is the invariant that makes the packets' neighbour comparison useful.
    """
    import re

    missing = []
    for eid, (axis, fm) in catalog.items():
        ids = fm.get("confusable_with") or []
        if not ids:
            continue
        path = rp.AXES[axis] / eid / "ENTRY.md"
        body = path.read_text(encoding="utf-8")
        section = re.search(r"### Often confused with\n(.*?)(?=\n#{2,3} |\Z)", body, re.DOTALL)
        blocks = set(re.findall(r"\*\*([a-z0-9-]+)\*\*:", section.group(1))) if section else set()
        for cid in ids:
            if cid not in blocks:
                missing.append(f"{eid} ({axis}) lists {cid} with no prose block")
    assert not missing, (
        "confusable_with ids without an 'Often confused with' block:\n" + "\n".join(missing[:15])
    )


# ---------------------------------------------------------------------------
# Packet content
# ---------------------------------------------------------------------------

def test_packet_separates_settled_facts_from_judgment(catalog):
    eid = "pragmatic-architect"
    axis, fm = catalog[eid]
    body, _ = rp.render_packet(eid, axis, fm, catalog)
    assert "## Already checked, do not re-check" in body
    assert "## Decide" in body
    # The judgment section must not re-ask what validate.py already enforces.
    decide = body[body.index("## Decide"):]
    for machine_checked in ("schema-valid", "resolves to a real entry", "em-dashes"):
        assert machine_checked not in decide, (
            f"the decide section re-asks a machine-checked fact: {machine_checked}"
        )


def test_packet_shows_the_actual_model_instruction(catalog):
    """The instruction phrasing is the thing the whole catalog rests on."""
    eid = "pragmatic-architect"
    axis, fm = catalog[eid]
    body, _ = rp.render_packet(eid, axis, fm, catalog)
    assert "The instruction a model actually receives" in body
    assert str(fm["llm_instruction_phrasing"]).strip()[:40] in body


def test_packet_includes_confusable_neighbours_for_the_distinguishability_call(catalog):
    eid = "pragmatic-architect"
    axis, fm = catalog[eid]
    body, _ = rp.render_packet(eid, axis, fm, catalog)
    for n in fm.get("confusable_with") or []:
        assert f"`{n}`" in body, f"neighbour {n} missing from the packet"


def test_every_stable_entry_renders_a_packet_without_error(stable, catalog):
    for eid, (axis, fm) in stable.items():
        body, _ = rp.render_packet(eid, axis, fm, catalog)
        assert body.startswith(f"# Review packet: `{eid}`")
        assert len(body) > 500, f"{eid}: packet suspiciously short"


def test_ledger_lists_every_stable_entry(stable, catalog):
    results = {eid: [] for eid in stable}
    ledger = rp.write_ledger(catalog, results)
    for eid in stable:
        assert f"`{eid}`" in ledger, f"{eid} missing from the ledger"
    assert "draft" in ledger and "slips" in ledger, (
        "the ledger should state the honest-fallback rule and that the launch slips "
        "rather than entries being relabelled"
    )
