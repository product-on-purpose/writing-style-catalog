"""Tests for the diff-pair generator (tools/diff-pair-generator.py).

The generator assembles a diff-pair from two existing vertical-slice renders.
It emits a placeholder "What to notice" section, but that section is the one
part of a diff-pair a human is expected to replace: the render bodies are
mechanical, the teaching commentary is not.

The behaviour these tests pin down is that regenerating a diff-pair refreshes
the render bodies without destroying authored commentary. Without it, a single
re-run silently reverts hand-written teaching text to boilerplate, which makes
authoring it a trap rather than an improvement.
"""
import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = REPO_ROOT / "tools"
sys.path.insert(0, str(TOOLS_DIR))

# The module name has hyphens, so it cannot be imported by name.
_spec = importlib.util.spec_from_file_location(
    "diff_pair_generator", TOOLS_DIR / "diff-pair-generator.py"
)
dpg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dpg)


# A real pair that exists in the catalog, used so the generator has renders to read.
TOPIC = "service-database-choice"
AXIS = "tone"
ENTRY_A = "candid"
ENTRY_B = "diplomatic"


# ---------------------------------------------------------------------------
# Extracting the authored section
# ---------------------------------------------------------------------------

def test_extract_what_to_notice_returns_the_section_body():
    doc = (
        "---\nkey: value\n---\n\n"
        "# Diff Pair: heading\n\n"
        "## What to notice\n\n"
        "Authored commentary here.\n\n"
        "---\n\n"
        "## A: `x`\n\nrender a\n"
    )
    assert dpg.extract_what_to_notice(doc) == "Authored commentary here."


def test_extract_what_to_notice_returns_none_when_section_absent():
    assert dpg.extract_what_to_notice("# no sections here\n") is None


def test_extract_what_to_notice_ignores_the_generic_placeholder():
    """The generator's own boilerplate is not authored content worth preserving."""
    generated = dpg.build_diff_pair(TOPIC, AXIS, ENTRY_A, ENTRY_B)
    assert dpg.extract_what_to_notice(generated) is None


# ---------------------------------------------------------------------------
# Preservation on regeneration
# ---------------------------------------------------------------------------

def test_build_diff_pair_uses_the_placeholder_when_nothing_is_preserved():
    out = dpg.build_diff_pair(TOPIC, AXIS, ENTRY_A, ENTRY_B)
    assert "swap is the entire cause of those differences" in out


def test_build_diff_pair_substitutes_preserved_commentary():
    authored = "**The sharpest tell.** A commits; B proposes."
    out = dpg.build_diff_pair(TOPIC, AXIS, ENTRY_A, ENTRY_B, preserved_notice=authored)
    assert authored in out
    assert "swap is the entire cause of those differences" not in out


def test_preserved_commentary_survives_a_full_regeneration_round_trip(tmp_path):
    """The actual regression: generate, author, regenerate, commentary still there."""
    authored = "**Authored.** This must survive a second generator run."

    first = dpg.build_diff_pair(TOPIC, AXIS, ENTRY_A, ENTRY_B)
    edited = first.replace(dpg.placeholder_notice(AXIS), authored)
    assert authored in edited

    target = tmp_path / "tone-candid-vs-diplomatic.md"
    target.write_text(edited, encoding="utf-8")

    regenerated = dpg.build_diff_pair(
        TOPIC, AXIS, ENTRY_A, ENTRY_B,
        preserved_notice=dpg.extract_what_to_notice(target.read_text(encoding="utf-8")),
    )
    assert authored in regenerated
    assert "swap is the entire cause of those differences" not in regenerated


def test_regeneration_still_refreshes_the_render_bodies():
    """Preserving commentary must not mean preserving stale renders."""
    out = dpg.build_diff_pair(
        TOPIC, AXIS, ENTRY_A, ENTRY_B, preserved_notice="authored text"
    )
    _, body_a = dpg.load_example(TOPIC, AXIS, ENTRY_A)
    _, body_b = dpg.load_example(TOPIC, AXIS, ENTRY_B)
    assert body_a in out
    assert body_b in out


# ---------------------------------------------------------------------------
# The four authored pairs in the catalog are protected by this behaviour
# ---------------------------------------------------------------------------

AUTHORED_PAIRS = sorted(
    (REPO_ROOT / "examples" / "diff-pairs" / "service-database-choice").glob("*.md")
)


@pytest.mark.parametrize("path", AUTHORED_PAIRS, ids=lambda p: p.stem)
def test_service_database_choice_pairs_carry_authored_commentary(path):
    """These four were authored by hand; a regression to boilerplate should fail."""
    text = path.read_text(encoding="utf-8")
    assert dpg.extract_what_to_notice(text) is not None, (
        f"{path.name} has lost its authored commentary and fallen back to the "
        "generator placeholder"
    )
