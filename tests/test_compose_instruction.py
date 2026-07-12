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


def test_not_found_error_teaches_recovery_with_list_hint():
    """A wrong id must not dead-end: the error names --list as the fix."""
    report = bi.compose_report(voice="definitely-not-a-real-entry-id")

    assert report["errors"]
    assert "Entry not found: voice/definitely-not-a-real-entry-id" in report["errors"][0]
    assert "--list" in report["errors"][0]


def test_not_found_error_detects_cross_axis_ids():
    """The most common real mistake: a valid id on the wrong axis flag.
    'candid' is a tone; passing it as --voice must say so."""
    report = bi.compose_report(voice="candid")

    assert report["errors"]
    assert "exists as a tone" in report["errors"][0]
    assert "--tone candid" in report["errors"][0]


GOLDEN_PATH = Path(__file__).resolve().parent / "golden-outputs" / "compose-pa-candid-ps-adr.golden.txt"


def _normalized(text: str) -> str:
    # Newline- and trailing-whitespace-insensitive so the committed golden can
    # pass through pre-commit's mixed-line-ending / trailing-whitespace fixers
    # without ever desyncing from live CLI output.
    lines = text.replace("\r\n", "\n").split("\n")
    return "\n".join(line.rstrip() for line in lines).strip()


def test_cli_composed_output_matches_golden():
    """Golden regression for the composed instruction TEXT: a change to the
    llm_instruction_phrasing wiring or the compose template must be a
    deliberate golden-file update, never silent drift. The chosen stack is
    fully affirmed (six pairs_well_with notes, zero conflicts), so stderr
    noise stays out of the assertion."""
    result = subprocess.run(
        [
            sys.executable,
            str(MODULE_PATH),
            "--voice", "pragmatic-architect",
            "--tone", "candid",
            "--style", "problem-solution",
            "--format", "adr",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert _normalized(result.stdout) == _normalized(GOLDEN_PATH.read_text(encoding="utf-8"))
    assert "conflict" not in result.stderr.lower()


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
