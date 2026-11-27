"""Tests for the distinguishability band harness (tools/distinguishability.py).

Two things these pin, because both are ways the measurement could be quietly
worthless rather than merely wrong:

1. **Blindness.** A packet built from a render whose body names the entry must
   raise, not warn. Several committed renders do open with a heading that names
   the entry, so this is a live condition and not a theoretical one.
2. **The band scale.** The four bands and their order are the measurement.
   `worst_band` has to be a floor over trials, and an unknown band string must
   not silently score as a known one.
"""
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import distinguishability as D  # noqa: E402

TOPIC = "service-database-choice"
TOPIC_LABEL = "Choosing Postgres vs DynamoDB for a new service"


# ---------------------------------------------------------------------------
# Reading renders
# ---------------------------------------------------------------------------

def test_render_path_follows_the_vertical_slice_convention():
    p = D.render_path(TOPIC, "voice", "pragmatic-architect")
    assert p == D.RENDERS_DIR / TOPIC / "voice-pragmatic-architect.md"


def test_split_frontmatter_body_matches_the_column_zero_fence():
    raw = "---\nid: x\nblock: |\n  ---\n  still frontmatter\n---\nbody line\n"
    assert D._split_frontmatter_body(raw) == "body line"


def test_split_frontmatter_body_passes_through_a_file_with_none():
    assert D._split_frontmatter_body("just prose\n") == "just prose\n"


def test_strip_attribution_heading_removes_a_heading_that_names_the_entry():
    body = "## Senior Consultant on: Choosing a database\n\nThe diagnosis is clear.\n"
    out, stripped = D.strip_attribution_heading(body, "Senior Consultant")
    assert out == "The diagnosis is clear."
    assert stripped == "## Senior Consultant on: Choosing a database"


def test_strip_attribution_heading_keeps_a_structural_heading():
    """An ADR's `## Context` is part of the format, not an attribution leak."""
    body = "## Context\n\nWe need a datastore.\n"
    out, stripped = D.strip_attribution_heading(body, "ADR")
    assert out == body
    assert stripped is None


def test_strip_attribution_heading_ignores_a_body_with_no_heading():
    body = "In January, I was running two things at once.\n"
    assert D.strip_attribution_heading(body, "Narrative Case Study") == (body, None)


# ---------------------------------------------------------------------------
# The leak check
# ---------------------------------------------------------------------------

def test_find_leaks_matches_the_name_case_insensitively():
    assert D.find_leaks("A senior consultant would say so.", ["Senior Consultant"]) == [
        "Senior Consultant"
    ]


def test_find_leaks_matches_a_hyphenated_id_as_spaced_words():
    assert D.find_leaks("This is a narrative case study.", ["narrative case study"]) == [
        "narrative case study"
    ]


def test_find_leaks_requires_a_word_boundary():
    """`coach` must not fire on `coaching`-free prose like `approach`."""
    assert D.find_leaks("The approach was reasonable.", ["coach"]) == []


def test_find_leaks_returns_empty_on_clean_prose():
    assert D.find_leaks("January: the project was in its seventh month.", ["coach"]) == []


def test_terms_for_keeps_a_three_letter_id():
    """No length floor: `adr`, `bio`, `faq`, `prd` and `rfc` are real ids.

    The first version of this check dropped terms under four characters, which
    exempted every three-letter id in the catalog and let a leaking packet
    through. A false positive costs a refused topic; a false negative costs the
    measurement.
    """
    assert "adr" in D._terms_for("adr", {"name": "Architecture Decision Record"})


def test_find_leaks_catches_a_three_letter_id_used_as_a_heading():
    """The real leak: the `adr` render opens `# ADR-0023: ...`."""
    body = "# ADR-0023: Use Postgres for the Notification Service\n\n## Context\n"
    assert D.find_leaks(body, D._terms_for("adr", {"name": "Architecture Decision Record"})) == ["adr"]


# ---------------------------------------------------------------------------
# Trials
# ---------------------------------------------------------------------------

def _id_map():
    """A synthetic two-entry id_map; the real catalog is exercised separately."""
    return {
        "alpha": ("style", {"name": "Alpha", "one_liner": "Alpha one-liner.",
                            "failure_modes": [{"mode": "over-alpha"}]}),
        "beta": ("style", {"name": "Beta", "one_liner": "Beta one-liner.",
                           "failure_modes": [{"mode": "over-beta"}]}),
    }


def _patch_renders(monkeypatch, bodies):
    def fake_load(topic_slug, axis, entry_id, entry_name):
        return D.Render(
            entry_id=entry_id, axis=axis, topic_slug=topic_slug,
            topic_label=TOPIC_LABEL, generator_model="test-model",
            generated_at="2026-01-01", path=Path(f"{axis}-{entry_id}.md"),
            body=bodies[entry_id], stripped_heading=None,
        )
    monkeypatch.setattr(D, "load_render", fake_load)


def test_build_trial_shuffles_deterministically_by_seed(monkeypatch):
    _patch_renders(monkeypatch, {"alpha": "A prose.", "beta": "B prose."})
    first = D.build_trial("alpha", "beta", TOPIC, _id_map(), order_seed=0).mapping
    again = D.build_trial("alpha", "beta", TOPIC, _id_map(), order_seed=0).mapping
    assert first == again


def test_build_trial_seeds_produce_both_presentation_orders(monkeypatch):
    _patch_renders(monkeypatch, {"alpha": "A prose.", "beta": "B prose."})
    mappings = {
        D.build_trial("alpha", "beta", TOPIC, _id_map(), order_seed=s).mapping["A"]
        for s in (0, 1)
    }
    assert mappings == {"alpha", "beta"}


def test_build_trial_raises_when_a_body_names_its_own_entry(monkeypatch):
    _patch_renders(monkeypatch, {"alpha": "Written in Alpha, obviously.", "beta": "B prose."})
    with pytest.raises(ValueError, match="name its own answer"):
        D.build_trial("alpha", "beta", TOPIC, _id_map(), order_seed=0)


def test_build_trial_raises_when_a_body_names_the_other_entry(monkeypatch):
    """Naming the neighbor is as much of a leak as naming yourself."""
    _patch_renders(monkeypatch, {"alpha": "A prose.", "beta": "Unlike Alpha, this is plain."})
    with pytest.raises(ValueError, match="name its own answer"):
        D.build_trial("alpha", "beta", TOPIC, _id_map(), order_seed=0)


def test_build_trial_rejects_a_cross_axis_pair(monkeypatch):
    _patch_renders(monkeypatch, {"alpha": "A prose.", "beta": "B prose."})
    id_map = _id_map()
    id_map["beta"] = ("tone", id_map["beta"][1])
    with pytest.raises(ValueError, match="cross-axis"):
        D.build_trial("alpha", "beta", TOPIC, id_map, order_seed=0)


def test_build_trial_rejects_an_unknown_topic(monkeypatch):
    _patch_renders(monkeypatch, {"alpha": "A prose.", "beta": "B prose."})
    with pytest.raises(ValueError, match="unknown anchor topic"):
        D.build_trial("alpha", "beta", "not-a-topic", _id_map(), order_seed=0)


def test_build_trial_rejects_an_entry_against_itself(monkeypatch):
    _patch_renders(monkeypatch, {"alpha": "A prose."})
    with pytest.raises(ValueError, match="two different entries"):
        D.build_trial("alpha", "alpha", TOPIC, _id_map(), order_seed=0)


def test_build_trials_covers_every_topic_and_order(monkeypatch):
    _patch_renders(monkeypatch, {"alpha": "A prose.", "beta": "B prose."})
    trials = D.build_trials(
        "alpha", "beta", [TOPIC, "async-standups"], _id_map(), seeds=(0, 1)
    )
    assert len(trials) == 4
    assert len({t.trial_id for t in trials}) == 4


# ---------------------------------------------------------------------------
# The judge prompt
# ---------------------------------------------------------------------------

def test_judge_prompt_never_states_the_mapping(monkeypatch):
    _patch_renders(monkeypatch, {"alpha": "A prose.", "beta": "B prose."})
    trial = D.build_trial("alpha", "beta", TOPIC, _id_map(), order_seed=0)
    prompt = D.build_judge_prompt(trial, _id_map())
    for label, eid in trial.mapping.items():
        assert f"[{label}]\n{eid}" not in prompt
        assert f"{label}: {eid}" not in prompt
        assert f'"{label}": "{eid}"' not in prompt


def test_judge_prompt_lists_options_alphabetically_not_in_slot_order(monkeypatch):
    """Option order must not correlate with slot order, or it leaks."""
    _patch_renders(monkeypatch, {"alpha": "A prose.", "beta": "B prose."})
    for seed in (0, 1):
        trial = D.build_trial("alpha", "beta", TOPIC, _id_map(), order_seed=seed)
        prompt = D.build_judge_prompt(trial, _id_map())
        assert prompt.index("`alpha`") < prompt.index("`beta`")


def test_judge_prompt_offers_all_four_bands(monkeypatch):
    _patch_renders(monkeypatch, {"alpha": "A prose.", "beta": "B prose."})
    trial = D.build_trial("alpha", "beta", TOPIC, _id_map(), order_seed=0)
    prompt = D.build_judge_prompt(trial, _id_map())
    for band in D.BANDS:
        assert f'"{band}"' in prompt


def test_judge_prompt_carries_the_failure_modes_the_restraint_check_grades_on(monkeypatch):
    _patch_renders(monkeypatch, {"alpha": "A prose.", "beta": "B prose."})
    trial = D.build_trial("alpha", "beta", TOPIC, _id_map(), order_seed=0)
    prompt = D.build_judge_prompt(trial, _id_map())
    assert "over-alpha" in prompt and "over-beta" in prompt


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def test_bands_run_worst_to_best():
    assert D.BANDS == ("identical", "subtle", "clear", "dramatic")


def test_worst_band_is_a_floor_over_trials():
    assert D.worst_band(["clear", "subtle", "dramatic"]) == "subtle"


def test_worst_band_ignores_an_unrecognised_string():
    assert D.worst_band(["clear", "very clear"]) == "clear"


def test_worst_band_is_none_when_nothing_is_recognised():
    assert D.worst_band(["very clear"]) is None


def _trial(monkeypatch, seed=0):
    _patch_renders(monkeypatch, {"alpha": "A prose.", "beta": "B prose."})
    return D.build_trial("alpha", "beta", TOPIC, _id_map(), order_seed=seed)


def test_score_trial_credits_a_correct_forced_choice(monkeypatch):
    trial = _trial(monkeypatch)
    verdict = {"attribution": dict(trial.mapping), "band": "clear",
               "restraint": {"A": "pass", "B": "pass"}}
    score = D.score_trial(trial, verdict)
    assert score["attribution_correct"] is True
    assert score["slots_correct"] == 2
    assert score["band"] == "clear"


def test_score_trial_marks_a_swapped_answer_wrong(monkeypatch):
    trial = _trial(monkeypatch)
    swapped = {lbl: eid for lbl, eid in zip("BA", trial.mapping.values())}
    score = D.score_trial(trial, {"attribution": swapped, "band": "subtle"})
    assert score["attribution_correct"] is False
    assert score["slots_correct"] == 0


def test_score_trial_keeps_an_unrecognised_band_out_of_the_scale(monkeypatch):
    trial = _trial(monkeypatch)
    score = D.score_trial(trial, {"attribution": dict(trial.mapping), "band": "very clear"})
    assert score["band"] is None
    assert score["band_reported"] == "very clear"


def test_score_trial_handles_a_missing_attribution(monkeypatch):
    trial = _trial(monkeypatch)
    score = D.score_trial(trial, {"band": "clear"})
    assert score["attribution_correct"] is False


def test_aggregate_reports_the_trial_count_beside_the_score():
    scores = [
        {"attribution_correct": True, "band": "clear", "restraint": {"A": "pass"}},
        {"attribution_correct": True, "band": "subtle", "restraint": {"A": "weak"}},
    ]
    agg = D.aggregate(scores)
    assert agg["trials"] == 2
    assert agg["attribution_correct"] == 2
    assert agg["score"] == 1.0
    assert agg["band"] == "subtle"
    assert agg["bands_observed"] == ["subtle", "clear"]
    assert agg["restraint_pass"] == 1 and agg["restraint_weak"] == 1


def test_aggregate_flags_a_floor_below_the_gate_bar():
    scores = [{"attribution_correct": True, "band": "identical", "restraint": {}}]
    agg = D.aggregate(scores)
    assert agg["clears_gate_floor"] is False


def test_aggregate_clears_the_floor_at_subtle():
    """`subtle` passes the gate; only `identical` auto-fails."""
    scores = [{"attribution_correct": True, "band": "subtle", "restraint": {}}]
    assert D.aggregate(scores)["clears_gate_floor"] is True


def test_aggregate_of_nothing_does_not_invent_a_score():
    agg = D.aggregate([])
    assert agg["trials"] == 0 and agg["score"] is None and agg["band"] is None


# ---------------------------------------------------------------------------
# Against the real catalog
# ---------------------------------------------------------------------------

def test_every_entry_has_a_declared_same_axis_neighbor_to_test_against():
    """The field cannot be produced for an entry with no declared neighbor."""
    id_map = D.load_catalog()
    missing = [eid for eid in id_map if D.declared_neighbor(eid, id_map) is None]
    assert missing == []


def test_the_required_subtle_style_pair_builds_a_clean_blind_trial():
    """The 2026-05-31 smoke test's subtle style pair, on a contemplative topic."""
    id_map = D.load_catalog()
    trial = D.build_trial(
        "narrative-case-study", "chronological-narrative",
        "a-hard-year-in-review", id_map, order_seed=0,
    )
    assert set(trial.mapping.values()) == {"narrative-case-study", "chronological-narrative"}
    assert all(len(s.body) > 500 for s in trial.slots)


def test_the_adr_render_is_refused_rather_than_judged():
    """A regression pin on the leak that got through the first run.

    `examples/vertical-slices/service-database-choice/format-adr.md` opens
    `# ADR-0023: Use Postgres for the Notification Service`. The heading names
    the format, the strip rule does not remove it (the entry's name is
    "Architecture Decision Record", which the heading does not contain), and
    the first version of the leak check exempted three-letter ids. The packet
    was built and judged. It must now raise instead.
    """
    id_map = D.load_catalog()
    with pytest.raises(ValueError, match="name its own answer"):
        D.build_trial("adr", "design-doc", "service-database-choice", id_map, order_seed=0)


def test_prepare_emits_machine_readable_packets(capsys):
    rc = D.main([
        "prepare", "--entry", "narrative-case-study",
        "--topics", "a-hard-year-in-review", "--orders", "2", "--json",
    ])
    assert rc == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["neighbor"] == "chronological-narrative"
    assert len(payload["trials"]) == 2


def test_prepare_rejects_an_unknown_entry(capsys):
    assert D.main(["prepare", "--entry", "not-an-entry"]) == 1
