"""Regression tests for the entry-recommender scorer (recommend.py).

Covers the invariants adversarial review found and fixed before v0.6.0, none of
which had test protection until now, plus the tiered payload invariants added in
v0.2.0 (B-1 and B-2 audit findings):

- tokenization (stopword removal, short-fragment drop, the one safe "-ies"
  singularization and its deliberate non-extension to bare "-s")
- IDF weighting (a corpus-rare token outweighs a corpus-common one) and the
  when_to_use > one_liner field weighting
- the all-qualifying short-list guarantee (short_list_size pads, never truncates)
- the above_threshold AND-gate (score alone is not enough; MIN_DISTINCT_MATCHES
  distinct tokens are also required)
- recommend()'s structural invariants against the real catalog (v0.2.0 concise
  mode): C1 guarantee (all qualifying candidates visible across both tiers),
  read-tier size, lean rows carry the "fields": "fetch" marker and physically
  lack full-text fields, full_ranked absent by default / present with debug=True
- recommend()'s structural invariants in detailed mode (legacy): nothing
  above_threshold hides in full_ranked, every short-list entry surfaces
  when_not_to_use
- fetch_one's stable-membership gate: draft refusal, unknown-axis refusal, and
  path-traversal rejection (the confirmed "../voices/..." axis escape)
- fetch_many: batch fetch returns one result per id, each routed through the
  same gate as fetch_one - path-traversal and draft refusal per id
- all three --ephemeral-input-file safety conditions, and that every refusal
  message says nothing was read or deleted
- --debug flag: full_ranked absent in concise mode by default, present with
  debug=True; full_ranked in debug mode contains only non-qualifying entries

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


def test_recommend_structural_invariants_concise_mode():
    """Concise-mode (default) structural invariants for the B-1 tiering design.

    Full fields go ONLY to the first short_list_size above_threshold rows
    (read tier). All other rows are lean - this covers BOTH qualifying
    candidates beyond short_list_size (lean triage) AND non-qualifying padding
    rows (lean padding). The "fields": "fetch" sentinel physically enforces
    the rule: a lean row cannot be picked without a fetch.

    Tiers are identified by above_threshold and position within the qualifying
    group, NOT by the presence of the fields being asserted on. Filtering on
    "when_to_use" in r before asserting "when_to_use" in r is circular: an
    empty filter list makes every assertion a no-op and cannot catch a
    regression that removes the field entirely.

    Three situations exercise the three possible cases:
    - postmortem: all four axes have qualifying < short_list_size -> padding rows
      exist for all axes, and those padding rows must be lean (the B-1 fix).
    - feature-cut: format axis has qualifying > short_list_size -> triage rows
      exist and must be lean.
    Both the read-tier and lean-row assertions must be non-vacuous.

    C1 (every qualifying candidate appears in short_list) is tested separately
    by test_recommend_tiering_c1_guarantee_on_real_catalog.
    """
    situations = [
        "a blameless postmortem for a production outage, for the engineering team",
        # feature-cut: format reliably produces > short_list_size qualifying rows
        (
            "I need to tell my team we are cutting a feature they spent "
            "two months building, and explain why, without crushing morale"
        ),
    ]
    read_tier_exercised = False
    lean_triage_exercised = False
    lean_padding_exercised = False

    for situation in situations:
        res = rec.recommend(situation=situation)
        assert set(res["axes"].keys()) == {"voice", "tone", "style", "format"}
        k = res["short_list_size"]
        for axis, out in res["axes"].items():
            assert out["fixed"] is None
            assert out["candidate_count"] == len(rec.load_stable_ids(axis))

            # full_ranked must be absent in default concise mode.
            assert "full_ranked" not in out, (
                f"{axis}: full_ranked must be absent in default concise mode"
            )

            short_list = out["short_list"]

            # Identify tiers by above_threshold and position within the qualifying
            # group - not by the presence of the fields being asserted on.
            # qualifying_rows[:k] = read tier (first k qualifying, full fields).
            # qualifying_rows[k:] = lean triage (qualifying beyond k, lean).
            # non_qualifying_rows     = lean padding (always lean - B-1 fix).
            qualifying_rows = [r for r in short_list if r["above_threshold"]]
            non_qualifying_rows = [r for r in short_list if not r["above_threshold"]]
            read_tier = qualifying_rows[:k]
            lean_triage = qualifying_rows[k:]
            lean_padding = non_qualifying_rows

            # Read-tier rows must carry all three full-text fields and no marker.
            for r in read_tier:
                read_tier_exercised = True
                assert "when_to_use" in r, f"{axis}: read-tier row missing when_to_use"
                assert "tells" in r, f"{axis}: read-tier row missing tells"
                assert "when_not_to_use" in r, f"{axis}: read-tier row missing when_not_to_use"
                assert "fields" not in r, f"{axis}: read-tier row must not carry fields marker"

            # Lean triage rows (qualifying beyond k): fetch marker, no full-text.
            for r in lean_triage:
                lean_triage_exercised = True
                assert r["fields"] == "fetch", (
                    f"{axis}: lean triage row missing fields marker"
                )
                assert "when_to_use" not in r, (
                    f"{axis}: lean triage row must not carry when_to_use"
                )
                assert "tells" not in r, (
                    f"{axis}: lean triage row must not carry tells"
                )
                assert "when_not_to_use" not in r, (
                    f"{axis}: lean triage row must not carry when_not_to_use"
                )
                assert r["above_threshold"] is True, (
                    f"{axis}: lean triage row must be above_threshold"
                )

            # Lean padding rows (non-qualifying): fetch marker, no full-text.
            # This is the B-1 fix: these were full rows before; now they are lean.
            for r in lean_padding:
                lean_padding_exercised = True
                assert r["fields"] == "fetch", (
                    f"{axis}: lean padding row missing fields marker"
                )
                assert "when_to_use" not in r, (
                    f"{axis}: lean padding row must not carry when_to_use"
                )
                assert "tells" not in r, (
                    f"{axis}: lean padding row must not carry tells"
                )
                assert "when_not_to_use" not in r, (
                    f"{axis}: lean padding row must not carry when_not_to_use"
                )
                assert r["above_threshold"] is False, (
                    f"{axis}: lean padding row must not be above_threshold"
                )

    # Guards: ensure all three assertion groups were non-vacuous.
    assert read_tier_exercised, (
        "no read-tier rows produced across all situations; read-tier assertions never ran"
    )
    assert lean_triage_exercised, (
        "no lean triage rows produced across all situations; "
        "lean-triage assertions never ran - use a richer situation"
    )
    assert lean_padding_exercised, (
        "no lean padding rows produced across all situations; "
        "lean-padding (B-1) assertions never ran"
    )


def test_recommend_tiering_c1_guarantee_on_real_catalog():
    """C1 guarantee: every above_threshold candidate appears somewhere in the
    emitted short_list (read tier or triage tier). Nothing qualifying may be
    silently dropped by the tiering code.

    Proved by comparing the ACTUALLY EMITTED concise-mode short_list against
    an independently-derived qualifying set: detailed mode produces the same
    qualifying candidates WITHOUT executing the tiering code under test, so it
    is a mutation-safe reference. If the tiering code drops triage-tier entries
    (e.g. by setting triage_tier = []), the emitted short_list shrinks while
    the detailed-mode reference stays complete, and the test fails.

    The feature-cut situation is used because it reliably produces more
    qualifying format candidates than short_list_size, so the triage tier is
    exercised and C1 is a non-trivial constraint for at least one axis. A
    situation that produces no triage entries at all makes C1 vacuously true
    and cannot catch the triage_tier = [] mutation.
    """
    situation = (
        "I need to tell my team we are cutting a feature they spent "
        "two months building, and explain why, without crushing morale"
    )
    # Independent reference: detailed mode puts ALL qualifying candidates in
    # short_list and does not execute the concise-mode tiering code at all.
    ref = rec.recommend(situation=situation, response_format="detailed")
    # System under test: default concise mode (tiering code active).
    res = rec.recommend(situation=situation, response_format="concise")

    triage_exercised = False
    for axis, out in res["axes"].items():
        ref_out = ref["axes"][axis]
        # Qualifying set derived from detailed mode - independent of tiering code.
        expected_qualifying_ids = {
            r["id"] for r in ref_out["short_list"] if r["above_threshold"]
        }
        if not expected_qualifying_ids:
            continue  # no qualifying candidates for this axis; C1 trivially holds

        # Every qualifying id must appear somewhere in the emitted short_list
        # (either as a read-tier full row or a triage-tier lean row).
        emitted_ids = {r["id"] for r in out["short_list"]}
        missing = expected_qualifying_ids - emitted_ids
        assert not missing, (
            f"{axis}: C1 violated - {len(missing)} qualifying candidate(s) absent "
            f"from the emitted short_list: {sorted(missing)}"
        )

        k = res["short_list_size"]
        if len(out["short_list"]) > k:
            triage_exercised = True

    # The test is only meaningful if triage tier was actually exercised for at
    # least one axis. If this fails, the situation no longer produces enough
    # qualifying candidates to exercise triage - pick a richer situation.
    assert triage_exercised, (
        "no axis produced a triage tier for the feature-cut situation; "
        "C1 was never non-trivially tested"
    )


def test_recommend_structural_invariants_detailed_mode():
    """detailed mode (legacy): full fields for every short_list entry, full_ranked
    always emitted, nothing above_threshold hidden in full_ranked."""
    res = rec.recommend(
        situation="a blameless postmortem for a production outage, for the engineering team",
        response_format="detailed",
    )
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


# --- tiering on a high-qualifying-count axis ----------------------------------


def test_tiering_splits_correctly_when_qualifying_exceeds_short_list_size():
    """When an axis has more qualifying candidates than short_list_size, the
    first short_list_size qualifying rows go into the read tier (full fields),
    the rest go into the lean triage tier. Format routinely produces 20-30+
    qualifying candidates on real situations.

    Tiers are identified by above_threshold and position within the qualifying
    group - not by the presence of the field being asserted on. Identifying
    read rows by "when_to_use" in r and then asserting "when_to_use" in r is
    circular: if the field disappears, the filter returns [] and no assertion
    ever runs. Instead: qualifying_rows[:k] = read tier, qualifying_rows[k:] =
    lean triage.
    """
    situation = (
        "I need to tell my team we are cutting a feature they spent "
        "two months building, and explain why, without crushing morale"
    )
    k = 6
    res = rec.recommend(situation=situation, short_list_size=k, response_format="concise")
    fmt = res["axes"]["format"]
    short_list = fmt["short_list"]

    # Identify tiers by above_threshold and position - not by the field asserted on.
    qualifying_rows = [r for r in short_list if r["above_threshold"]]
    non_qualifying_rows = [r for r in short_list if not r["above_threshold"]]
    read_tier = qualifying_rows[:k]
    lean_triage = qualifying_rows[k:]

    # The feature-cut situation reliably produces > 6 qualifying format entries.
    assert len(lean_triage) > 0, (
        "expected lean triage rows for format axis on feature-cut situation"
    )
    # No padding when qualifying > short_list_size.
    assert len(non_qualifying_rows) == 0, (
        "expected no non-qualifying padding when qualifying > short_list_size"
    )

    # Read tier must not exceed short_list_size.
    assert len(read_tier) == k

    # Every read-tier row carries the three full-text fields and no fetch marker.
    full_text_fields = {"when_to_use", "tells", "when_not_to_use"}
    for r in read_tier:
        assert full_text_fields.issubset(r.keys()), (
            f"read-tier row {r['id']!r} missing full-text fields"
        )
        assert "fields" not in r, (
            f"read-tier row {r['id']!r} must not carry fields marker"
        )

    # Every lean triage row is above_threshold and physically lacks full-text fields.
    for r in lean_triage:
        assert r["above_threshold"] is True, (
            f"lean triage row {r['id']!r} must be above_threshold"
        )
        assert r.get("fields") == "fetch", (
            f"lean triage row {r['id']!r} missing fields marker"
        )
        assert not full_text_fields.intersection(r.keys()), (
            f"lean triage row {r['id']!r} unexpectedly carries full-text fields"
        )

    # C1: qualifying candidates total = read tier + all lean triage rows.
    total_qualifying_in_sl = len(read_tier) + len(lean_triage)
    # Compare against detailed mode to confirm no qualifying candidate was lost.
    res_detailed = rec.recommend(situation=situation, short_list_size=k, response_format="detailed")
    detailed_qualifying = sum(
        1 for r in res_detailed["axes"]["format"]["short_list"] if r["above_threshold"]
    )
    assert total_qualifying_in_sl == detailed_qualifying, (
        f"C1 broken: concise mode has {total_qualifying_in_sl} qualifying, "
        f"detailed mode has {detailed_qualifying}"
    )


# --- debug flag -----------------------------------------------------------


def test_debug_flag_controls_full_ranked_presence():
    """--debug (debug=True) restores full_ranked in concise mode; without it,
    full_ranked is absent. In both cases, nothing above_threshold may appear
    in full_ranked (C1)."""
    situation = "a blameless postmortem for a production outage, for the engineering team"

    without_debug = rec.recommend(situation=situation, response_format="concise", debug=False)
    for axis, out in without_debug["axes"].items():
        assert "full_ranked" not in out, f"{axis}: full_ranked must be absent without debug"

    with_debug = rec.recommend(situation=situation, response_format="concise", debug=True)
    for axis, out in with_debug["axes"].items():
        assert "full_ranked" in out, f"{axis}: full_ranked must be present with debug=True"
        qualifying_in_fr = [r for r in out["full_ranked"] if r["above_threshold"]]
        assert qualifying_in_fr == [], (
            f"{axis}: qualifying candidates found in full_ranked even with debug=True: "
            f"{[r['id'] for r in qualifying_in_fr]}"
        )


# --- fetch_many gate tests ------------------------------------------------


def test_fetch_many_returns_full_fields_for_stable_entries():
    """fetch_many returns one result per id in the same order, each with full
    fields when the id is a valid stable entry."""
    results = rec.fetch_many("voice", ["pragmatic-architect", "senior-consultant"])
    assert len(results) == 2
    for r in results:
        assert r["found"] is True
        assert r["review_status"] in rec.STABLE_STATUSES
        assert r["when_to_use"]
        assert "when_not_to_use" in r
    assert results[0]["id"] == "pragmatic-architect"
    assert results[1]["id"] == "senior-consultant"


def test_fetch_many_rejects_path_traversal_per_id():
    """Each id in fetch_many passes through the same membership gate as
    fetch_one. A path-traversal attempt per id must be rejected."""
    results = rec.fetch_many("format", ["../voices/pragmatic-architect"])
    assert len(results) == 1
    assert results[0]["found"] is False
    assert "not a stable" in results[0]["error"]


def test_fetch_many_rejects_draft_entries_per_id():
    """Each id in fetch_many passes through the same draft refusal as fetch_one."""
    all_format_ids = rec.build_instruction.list_entries().get("format", [])
    stable = set(rec.load_stable_ids("format"))
    draft_ids = [i for i in all_format_ids if i not in stable]
    if not draft_ids:
        pytest.skip("no draft entries in the catalog to test against")
    results = rec.fetch_many("format", [draft_ids[0]])
    assert len(results) == 1
    assert results[0]["found"] is False
    assert "not a stable" in results[0]["error"]


def test_fetch_many_unknown_axis_per_result():
    """An unknown axis in fetch_many is rejected per id, same as fetch_one."""
    results = rec.fetch_many("nonsense", ["anything"])
    assert len(results) == 1
    assert results[0]["found"] is False
    assert "unknown axis" in results[0]["error"]


def test_fetch_many_mixed_valid_and_invalid_ids():
    """fetch_many processes each id independently: valid ids succeed, invalid
    ids fail, and the order matches the input."""
    results = rec.fetch_many("voice", ["pragmatic-architect", "../voices/bad", "totally-fake"])
    assert len(results) == 3
    assert results[0]["found"] is True
    assert results[0]["id"] == "pragmatic-architect"
    assert results[1]["found"] is False  # path traversal
    assert results[2]["found"] is False  # unknown id


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


# --- B-1 tiering: floor case and mixed case -----------------------------------


def test_floor_case_no_qualifying_yields_all_lean_rows():
    """Floor case (B-1 fix): when 0 candidates clear above_threshold, every
    short_list row must be lean (fields: "fetch"). No row may carry full-text
    fields. This was the core waste the B-1 audit found: 100% of the floor
    payload was non-qualifying padding rows loaded with full when_to_use/tells/
    when_not_to_use text.

    Uses threshold=999.0 (impossibly high) to force 0 qualifying rows
    deterministically, independent of catalog content. This tests the structural
    invariant - that 0 qualifying implies 0 full-field loads - reliably.

    MUTATION PROOF: if the read_tier computation reverts to the old
    all_short_list_entries[:short_list_size] (position-based, including padding),
    non-qualifying padding rows would be loaded with full fields and added to the
    read tier. The assertion that no row carries "when_to_use" would then fail,
    catching the regression.
    """
    result = rec.recommend(
        situation="write something nice for my coworker",
        threshold=999.0,  # impossibly high -> 0 above_threshold rows on every axis
    )
    full_text_fields = {"when_to_use", "tells", "when_not_to_use"}
    for axis, out in result["axes"].items():
        if out.get("fixed"):
            continue
        short_list = out["short_list"]
        # Verify the floor case: all rows must be non-qualifying.
        assert all(not r["above_threshold"] for r in short_list), (
            f"{axis}: expected 0 above_threshold rows with threshold=999.0"
        )
        # Every row must be lean (fields: "fetch").
        for r in short_list:
            assert r.get("fields") == "fetch", (
                f"{axis}: floor-case row {r['id']!r} expected lean but missing fields marker"
            )
        # No row may carry full-text fields.
        for r in short_list:
            present = full_text_fields.intersection(r.keys())
            assert not present, (
                f"{axis}: floor-case row {r['id']!r} carries full-text field(s): {present} - "
                f"non-qualifying padding rows must be lean (B-1 fix)"
            )


def test_mixed_case_qualifying_rows_full_padding_rows_lean():
    """Mixed case (B-1 fix): when qualifying < short_list_size, qualifying rows
    get full fields (read tier) and non-qualifying padding rows are lean.

    Tiers are identified by above_threshold, NOT by the presence of the fields
    being asserted on. Filtering by "when_to_use" in r before asserting it is
    circular; an empty result makes every assertion a no-op.

    Uses threshold=999.0 with one deliberately-planted qualifying row by
    injecting a below-threshold result set: this is tested purely via the public
    recommend() function against the real catalog, so instead we use a two-phase
    approach - first find an axis where qualifying < k on a real situation, then
    assert the split.

    Uses the feature-cut situation, which produces 2-4 qualifying rows on voice/
    tone/style (confirmed < k=6). Qualifying rows must carry full fields; the
    non-qualifying padding rows that fill the rest of short_list_size must be lean.

    MUTATION PROOF: if the read_tier computation reverts to position-based
    (all_short_list_entries[:k]), non-qualifying padding rows would receive full
    fields and appear in what this test calls "read_tier". The assertion that
    non-qualifying rows carry "fields": "fetch" and lack full-text fields would
    then fail, catching the regression.
    """
    situation = (
        "I need to tell my team we are cutting a feature they spent "
        "two months building, and explain why, without crushing morale"
    )
    k = 6
    result = rec.recommend(situation=situation, short_list_size=k, response_format="concise")
    full_text_fields = {"when_to_use", "tells", "when_not_to_use"}

    mixed_exercised = False
    for axis, out in result["axes"].items():
        if out.get("fixed"):
            continue
        short_list = out["short_list"]
        qualifying_rows = [r for r in short_list if r["above_threshold"]]
        non_qualifying_rows = [r for r in short_list if not r["above_threshold"]]

        # Only exercise axes where 0 < qualifying < k (the mixed case).
        if not (0 < len(qualifying_rows) < k):
            continue

        mixed_exercised = True
        # Qualifying rows -> read tier: must carry full-text fields, no fetch marker.
        # Identified by above_threshold (not by the presence of the asserted fields).
        for r in qualifying_rows:
            assert full_text_fields.issubset(r.keys()), (
                f"{axis}: qualifying row {r['id']!r} missing full-text fields"
            )
            assert "fields" not in r, (
                f"{axis}: qualifying row {r['id']!r} must not carry fields marker"
            )
        # Non-qualifying padding rows -> lean: fetch marker, no full-text.
        # This is the B-1 fix: these rows were full in the old design.
        for r in non_qualifying_rows:
            assert r.get("fields") == "fetch", (
                f"{axis}: non-qualifying padding row {r['id']!r} missing fields marker"
            )
            present = full_text_fields.intersection(r.keys())
            assert not present, (
                f"{axis}: non-qualifying padding row {r['id']!r} carries full-text "
                f"field(s): {present} - padding rows must be lean (B-1 fix)"
            )

    assert mixed_exercised, (
        "no axis produced the mixed case (0 < qualifying < k) for the feature-cut "
        "situation; verify the situation still produces qualifying < short_list_size "
        "on at least one axis"
    )
