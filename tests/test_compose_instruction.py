"""Tests for conflict-aware composition in build-instruction.py (S1).

Loads the hyphenated script module by path. The feature under test:
compose_instruction must read each selected entry's avoid_with /
pairs_well_with relationships, flag conflicts with a symmetric (union)
rule per decision B1, and warn without blocking per decision B2, while
applying voice -> tone -> style -> format precedence.
"""
import importlib.util
import subprocess
import sys
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "writing-instruction-builder"
    / "scripts"
    / "build-instruction.py"
)


def _load_module():
    spec = importlib.util.spec_from_file_location("build_instruction", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


bi = _load_module()


def _sel(axis, entry_id, **fields):
    return {"axis": axis, "id": entry_id, "entry": fields}


def test_avoid_with_is_symmetric_when_only_one_side_lists_the_other():
    """B1: a conflict is a property of the pair. If voice A lists tone B in
    avoid_with but B does not list A back, the pair is still flagged."""
    selections = [
        _sel("voice", "a-voice", avoid_with=["b-tone"]),
        _sel("tone", "b-tone", avoid_with=[]),
    ]

    report = bi.analyze_relationships(selections)

    flagged = {frozenset((c["a"], c["b"])) for c in report["conflicts"]}
    assert frozenset(("a-voice", "b-tone")) in flagged


def test_no_conflict_when_neither_entry_lists_the_other():
    selections = [
        _sel("voice", "a-voice", avoid_with=[]),
        _sel("tone", "b-tone", avoid_with=[]),
    ]

    report = bi.analyze_relationships(selections)

    assert report["conflicts"] == []


def test_real_catalog_pragmatic_architect_and_reverent_conflict():
    """The canonical conflict case named in the v0.3.0 release plan, run
    against the actual frozen entries rather than synthetic fixtures."""
    pa = bi.load_entry("voice", "pragmatic-architect")
    rev = bi.load_entry("tone", "reverent")
    selections = [
        {"axis": "voice", "id": "pragmatic-architect", "entry": pa},
        {"axis": "tone", "id": "reverent", "entry": rev},
    ]

    report = bi.analyze_relationships(selections)

    flagged = {frozenset((c["a"], c["b"])) for c in report["conflicts"]}
    assert frozenset(("pragmatic-architect", "reverent")) in flagged


def test_pairs_well_with_is_affirmed():
    selections = [
        _sel("voice", "a-voice", pairs_well_with=["b-tone"]),
        _sel("tone", "b-tone", pairs_well_with=[]),
    ]

    report = bi.analyze_relationships(selections)

    affirmed = {frozenset((p["a"], p["b"])) for p in report["affirmations"]}
    assert frozenset(("a-voice", "b-tone")) in affirmed


def test_compose_report_flags_conflict_but_still_composes():
    """B2: warn, never block. A conflicting selection is flagged AND still
    produces the full composed instruction."""
    result = bi.compose_report(
        voice="pragmatic-architect", tone="reverent", topic="a deployment decision"
    )

    flagged = {frozenset((c["a"], c["b"])) for c in result["conflicts"]}
    assert frozenset(("pragmatic-architect", "reverent")) in flagged
    assert result["instruction"]
    assert "Write about: a deployment decision" in result["instruction"]


def test_resolve_selections_applies_voice_tone_style_format_precedence():
    """Precedence order is deterministic regardless of argument order."""
    resolved = bi.resolve_selections(
        style="problem-solution",
        voice="pragmatic-architect",
        fmt="adr",
        tone="reverent",
    )

    assert [r["axis"] for r in resolved] == ["voice", "tone", "style", "format"]


def test_cli_warns_on_conflict_to_stderr_and_still_prints_instruction():
    """End to end through the CLI: a conflicting selection prints the full
    instruction on stdout and a conflict warning on stderr, exit code 0."""
    result = subprocess.run(
        [
            sys.executable,
            str(MODULE_PATH),
            "--voice", "pragmatic-architect",
            "--tone", "reverent",
            "--topic", "x",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Write about: x" in result.stdout
    assert "conflict" in result.stderr.lower()
    assert "reverent" in result.stderr
