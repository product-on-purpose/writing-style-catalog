"""Regression tests for the entry-recommender scorer (recommend.py).

Covers the invariants adversarial review found and fixed before v0.6.0, none of
which had test protection until now:

- tokenization (stopword removal, short-fragment drop, the one safe "-ies"
  singularization and its deliberate non-extension to bare "-s")
- IDF weighting (a corpus-rare token outweighs a corpus-common one) and the
  when_to_use > one_liner field weighting
- the all-qualifying short-list guarantee (short_list_size pads, never truncates)
- the above_threshold AND-gate (score alone is not enough; MIN_DISTINCT_MATCHES
  distinct tokens are also required)
- recommend()'s structural invariants against the real catalog, including that
  nothing above_threshold ever hides in full_ranked (the hidden-qualifying-
  candidates bug) and that short-list entries surface when_not_to_use
- fetch_one's stable-membership gate: draft refusal, unknown-axis refusal, and
  path-traversal rejection (the confirmed "../voices/..." axis escape)
- all three --ephemeral-input-file safety conditions, and that every refusal
  message says nothing was read or deleted

Loads the module by path, mirroring tests/test_compose_instruction.py.
"""
import importlib.util
from pathlib import Path

import pytest

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "entry-recommender"
    / "scripts"
    / "recommend.py"
)


def _load_module():
    spec = importlib.util.spec_from_file_location("recommend", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


rec = _load_module()


# --- tokenization ---------------------------------------------------------


def test_tokenize_removes_stopwords_and_short_fragments():
    tokens = rec.tokenize("I need to write an announcement for the team's launch")
    assert "announcement" in tokens
    assert "launch" in tokens
    assert "team" in tokens
    # stopwords and generic verbs never survive
    assert {"i", "need", "to", "write", "an", "the", "for"}.isdisjoint(tokens)
    # possessive fragments ("team's" -> stray "s") are dropped by the length rule
    assert all(len(t) >= 2 for t in tokens)


def test_tokenize_accepts_lists_and_none():
    assert rec.tokenize(None) == set()
    tokens = rec.tokenize(["Eulogies", "for family"])
    assert "eulogy" in tokens  # -ies singularized
    assert "family" in tokens


def test_singularize_is_ies_only_and_length_guarded():
    assert rec._singularize("eulogies") == "eulogy"
    assert rec._singularize("categories") == "category"
    # deliberately NOT bare-s stripping
    assert rec._singularize("status") == "status"
    assert rec._singularize("process") == "process"
    # length guard: "ties" (len 4) is not mangled into "ty"
    assert rec._singularize("ties") == "ties"


# --- scoring --------------------------------------------------------------


def test_rare_token_outscores_common_token():
    idf_table = {"doc_count": 100, "df": {"migration": 1, "reader": 90}}
    entry = {"when_to_use": ["database migration status for a reader"], "tells": [], "one_liner": ""}
    rare = rec.score_entry({"migration"}, "style", entry, idf_table)
    common = rec.score_entry({"reader"}, "style", entry, idf_table)
    assert rare["score"] > common["score"]
    assert rare["distinct_matches"] == 1
    assert rare["matched_tokens"]["when_to_use"] == ["migration"]


def test_when_to_use_outweighs_one_liner_for_the_same_token():
    idf_table = {"doc_count": 100, "df": {"postmortem": 1}}
    in_when = {"when_to_use": ["postmortem"], "tells": [], "one_liner": ""}
    in_liner = {"when_to_use": [], "tells": [], "one_liner": "postmortem"}
    s_when = rec.score_entry({"postmortem"}, "style", in_when, idf_table)
    s_liner = rec.score_entry({"postmortem"}, "style", in_liner, idf_table)
    assert s_when["score"] > s_liner["score"]


def _synthetic_style_entries():
    """Five synthetic style entries; 'aa' is the only one carrying the
    distinctive tokens the tests match against."""
    texts = {
        "aa": "migration plan rollout",
        "bb": "onboarding welcome checklist",
        "cc": "quarterly budget summary",
        "dd": "holiday greeting card",
        "ee": "workshop agenda outline",
    }
    return {
        "style": {
            entry_id: {"when_to_use": [text], "tells": [], "one_liner": ""}
            for entry_id, text in texts.items()
        }
    }


def test_above_threshold_requires_both_score_and_distinct_matches():
    all_entries = _synthetic_style_entries()
    idf_table = rec.build_idf_table(all_entries)
    # one matching distinct token: score can clear a low threshold, the
    # distinct-match gate must still reject it
    ranked_one = rec.build_ranked_list("style", {"migration"}, all_entries, idf_table, threshold=0.1)
    top_one = ranked_one[0]
    assert top_one["id"] == "aa"
    assert top_one["score"] >= 0.1
    assert top_one["distinct_matches"] == 1
    assert top_one["above_threshold"] is False
    # two matching distinct tokens: both conditions hold
    ranked_two = rec.build_ranked_list("style", {"migration", "rollout"}, all_entries, idf_table, threshold=0.1)
    top_two = ranked_two[0]
    assert top_two["id"] == "aa"
    assert top_two["distinct_matches"] == 2
    assert top_two["above_threshold"] is True


def test_short_list_never_truncates_qualifying_candidates():
    ranked = [{"id": f"q{i}", "above_threshold": True} for i in range(10)] + [
        {"id": f"n{i}", "above_threshold": False} for i in range(5)
    ]
    short = rec._select_short_list(ranked, short_list_size=3)
    assert len(short) == 10
    assert all(r["above_threshold"] for r in short)


def test_short_list_pads_with_non_qualifying_only_up_to_size():
    ranked = [{"id": f"q{i}", "above_threshold": True} for i in range(2)] + [
        {"id": f"n{i}", "above_threshold": False} for i in range(8)
    ]
    short = rec._select_short_list(ranked, short_list_size=6)
    assert len(short) == 6
    assert [r["id"] for r in short[:2]] == ["q0", "q1"]
    # padding preserves ranked order of the non-qualifying group
    assert [r["id"] for r in short[2:]] == ["n0", "n1", "n2", "n3"]


# --- recommend() against the real catalog ---------------------------------


def test_recommend_structural_invariants_on_real_catalog():
    res = rec.recommend(situation="a blameless postmortem for a production outage, for the engineering team")
    assert set(res["axes"].keys()) == {"voice", "tone", "style", "format"}
    for axis, out in res["axes"].items():
        assert out["fixed"] is None
        assert out["candidate_count"] == len(rec.load_stable_ids(axis))
        # the hidden-qualifying-candidates regression: nothing above_threshold
        # may ever sit in full_ranked
        assert all(not r["above_threshold"] for r in out["full_ranked"])
        # every short-list entry surfaces the negative field too
        for r in out["short_list"]:
            assert "when_to_use" in r
            assert "tells" in r
            assert "when_not_to_use" in r


def test_recommend_validates_fixed_axes_against_stable_pool():
    ok = rec.recommend(situation="anything", fixed={"voice": "pragmatic-architect"})
    assert ok["axes"]["voice"] == {"fixed": "pragmatic-architect", "valid": True}
    assert ok["errors"] == []

    bad = rec.recommend(situation="anything", fixed={"voice": "totally-fake-id"})
    assert bad["axes"]["voice"] == {"fixed": "totally-fake-id", "valid": False}
    assert bad["errors"]


# --- fetch_one gates ------------------------------------------------------


def test_fetch_one_returns_full_fields_for_a_stable_entry():
    out = rec.fetch_one("voice", "pragmatic-architect")
    assert out["found"] is True
    assert out["review_status"] in rec.STABLE_STATUSES
    assert out["when_to_use"]
    assert "when_not_to_use" in out


def test_fetch_one_rejects_path_traversal():
    out = rec.fetch_one("format", "../voices/pragmatic-architect")
    assert out["found"] is False
    assert "not a stable" in out["error"]


def test_fetch_one_rejects_unknown_axis():
    out = rec.fetch_one("nonsense", "anything")
    assert out["found"] is False
    assert "unknown axis" in out["error"]


def test_fetch_one_refuses_draft_entries():
    all_format_ids = rec.build_instruction.list_entries().get("format", [])
    stable = set(rec.load_stable_ids("format"))
    draft_ids = [i for i in all_format_ids if i not in stable]
    if not draft_ids:
        pytest.skip("no draft entries in the catalog to test against")
    out = rec.fetch_one("format", draft_ids[0])
    assert out["found"] is False
    assert "not a stable" in out["error"]


# --- --ephemeral-input-file safety conditions ------------------------------


def test_ephemeral_path_accepts_a_conforming_temp_file(tmp_path):
    p = tmp_path / "situation.entry-recommender-input.json"
    p.write_text("{}", encoding="utf-8")
    resolved = rec._require_ephemeral_path_is_safe(p)
    assert resolved == p.resolve()
    assert p.exists()  # validation must not itself delete anything


def test_ephemeral_path_rejects_wrong_suffix(tmp_path):
    p = tmp_path / "situation.json"
    with pytest.raises(ValueError) as excinfo:
        rec._require_ephemeral_path_is_safe(p)
    assert "nothing was read or deleted" in str(excinfo.value)


def test_ephemeral_path_rejects_paths_inside_the_repo():
    p = rec.REPO_ROOT / "never-created.entry-recommender-input.json"
    with pytest.raises(ValueError) as excinfo:
        rec._require_ephemeral_path_is_safe(p)
    assert "inside the repository" in str(excinfo.value)
    assert "nothing was read or deleted" in str(excinfo.value)


def test_ephemeral_path_rejects_paths_outside_system_temp():
    p = Path.home() / "never-created.entry-recommender-input.json"
    with pytest.raises(ValueError) as excinfo:
        rec._require_ephemeral_path_is_safe(p)
    assert "system temp" in str(excinfo.value)
    assert "nothing was read or deleted" in str(excinfo.value)
