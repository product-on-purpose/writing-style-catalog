"""Tests for the recommender's --verbose score trace (audit finding D-7).

The JSON payload already reports which tokens matched. What it could not show
was what those matches were worth, or which of the two independent gates
rejected a candidate, and both are the questions that come up when a score looks
wrong.

The motivating case is real and recent. Teaching `friendly-mentor` the word
"child" gave it a single match worth 10.43, comfortably over the 3.0 threshold,
and it still did not qualify because MIN_DISTINCT_MATCHES is 2. From the JSON
alone that reads as an inexplicable miss. The trace names the gate.

The contract these tests protect above all: **stdout stays clean JSON**. The
skill parses stdout, so a trace written to the wrong stream would break the
shipped workflow rather than merely being unhelpful.
"""
import importlib.util
import io
import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "skills" / "entry-recommender" / "scripts" / "recommend.py"

_spec = importlib.util.spec_from_file_location("recommend", SCRIPT)
rec = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rec)

SITUATION = "Explain how kubernetes autoscaling works to an eight year old child."


def _run(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--situation", SITUATION, "--json", *args],
        capture_output=True, text=True, check=True,
    )


# ---------------------------------------------------------------------------
# The contract that matters most
# ---------------------------------------------------------------------------

def test_stdout_is_still_parseable_json_with_verbose_on():
    """The skill parses stdout. A trace on the wrong stream breaks the workflow."""
    out = _run("--verbose")
    payload = json.loads(out.stdout)          # raises if the trace leaked
    assert "axes" in payload


def test_the_trace_goes_to_stderr_and_is_absent_without_the_flag():
    with_flag = _run("--verbose")
    without = _run()
    assert "[trace]" in with_flag.stderr
    assert "[trace]" not in with_flag.stdout
    assert "[trace]" not in without.stderr
    assert "[trace]" not in without.stdout


def test_verbose_does_not_change_the_payload():
    """Diagnostics must observe, not alter, what the scorer decided."""
    assert json.loads(_run("--verbose").stdout) == json.loads(_run().stdout)


# ---------------------------------------------------------------------------
# What the trace has to explain
# ---------------------------------------------------------------------------

def _trace_for(ranked, threshold=3.0):
    buf = io.StringIO()
    entries = rec.load_all_stable_entries()
    idf = rec.build_idf_table(entries)
    toks = set(rec._situation_tokens(SITUATION, None, None))
    rec.emit_score_trace("voice", toks, ranked, idf, threshold, stream=buf)
    return buf.getvalue()


def _ranked(axis="voice", threshold=3.0):
    entries = rec.load_all_stable_entries()
    idf = rec.build_idf_table(entries)
    toks = set(rec._situation_tokens(SITUATION, None, None))
    return rec.build_ranked_list(axis, toks, entries, idf, threshold), toks, idf


def test_trace_reports_per_token_idf_so_a_weak_match_is_visible():
    ranked, _, _ = _ranked()
    text = _trace_for(ranked)
    assert "situation tokens" in text
    assert "idf=" in text and "df=" in text
    # "how" is common across the corpus and must be visibly cheap next to a rare token.
    assert "how" in text and "kubernetes" in text


def test_trace_shows_weighted_contribution_per_matched_token():
    ranked, _, _ = _ranked()
    text = _trace_for(ranked)
    qualifying = [r for r in ranked if r["above_threshold"]]
    assert qualifying, "expected at least one qualifying voice for this situation"
    # A contribution is printed as token(value), e.g. child(10.43).
    assert "child(" in text


def test_a_rejected_candidate_names_which_gate_it_failed():
    ranked, _, _ = _ranked()
    text = _trace_for(ranked)
    assert "REJECTED" in text
    assert "<" in text, "the rejection reason should show the failing comparison"


def test_the_distinct_gate_is_reported_separately_from_the_score_gate():
    """The D-7 motivating case: over the score bar, under the distinct-match gate.

    Synthesised rather than found in the live catalog, because the whole point
    of the P-4 enrichment was to stop this happening to `friendly-mentor`.
    """
    ranked = [{
        "id": "synthetic-one-match",
        "score": 10.43,
        "distinct_matches": 1,
        "above_threshold": False,
        "one_liner": "",
        "matched_tokens": {"when_to_use": ["child"], "tells": [],
                           "one_liner": [], "facets": []},
    }]
    text = _trace_for(ranked)
    assert "REJECTED" in text
    assert f"distinct 1 < {rec.MIN_DISTINCT_MATCHES}" in text
    assert "score" not in text.split("REJECTED")[1].split(")")[0], (
        "a candidate over the score bar must not be reported as failing it"
    )


def test_a_candidate_failing_both_gates_reports_both():
    ranked = [{
        "id": "synthetic-nothing",
        "score": 0.0,
        "distinct_matches": 0,
        "above_threshold": False,
        "one_liner": "",
        "matched_tokens": {"when_to_use": [], "tells": [], "one_liner": [], "facets": []},
    }]
    text = _trace_for(ranked)
    reason = text.split("REJECTED (")[1].split(")")[0]
    assert "score" in reason and "distinct" in reason


def test_qualifying_candidates_are_always_shown_even_past_the_limit():
    """The limit trims rejects, never the candidates that actually qualified."""
    ranked = [
        {"id": f"q{i}", "score": 99.0, "distinct_matches": 5, "above_threshold": True,
         "one_liner": "", "matched_tokens": {"when_to_use": ["child"], "tells": [],
                                             "one_liner": [], "facets": []}}
        for i in range(12)
    ]
    text = _trace_for(ranked)
    for i in range(12):
        assert f"q{i} " in text or f"q{i}\n" in text or f"q{i:<28}" in text.replace("  ", " ")


def test_field_weights_used_by_the_trace_match_the_scorer():
    """A trace that reports a different weight than the scorer applies would lie."""
    assert rec._FIELD_WEIGHTS["when_to_use"] == rec.WHEN_TO_USE_WEIGHT
    assert rec._FIELD_WEIGHTS["tells"] == rec.TELLS_WEIGHT
    assert rec._FIELD_WEIGHTS["one_liner"] == rec.ONE_LINER_WEIGHT
    assert rec._FIELD_WEIGHTS["facets"] == rec.FACET_WEIGHT
