import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

import gate_pilot as gp  # noqa: E402


def test_render_instruction_appends_topic():
    fm = {"llm_instruction_phrasing": "Write in a test voice.  "}
    out = gp.render_instruction(fm, "Choosing Postgres vs DynamoDB for a new service")
    assert out == (
        "Write in a test voice.\n\n"
        "Write about: Choosing Postgres vs DynamoDB for a new service"
    )


def test_render_instruction_handles_missing_phrasing():
    out = gp.render_instruction({}, "Some topic")
    assert out == "\n\nWrite about: Some topic"


def _entry(axis, **fields):
    """A minimal (axis, frontmatter) tuple, as id_map stores it."""
    return (axis, fields)


# A real anchor-topic slug so label lookup resolves; its label is fixed data.
TOPIC = "service-database-choice"
TOPIC_LABEL = "Choosing Postgres vs DynamoDB for a new service"


def _voice_map():
    return {
        "pragmatic-architect": _entry("voice", llm_instruction_phrasing="PA phrasing"),
        "senior-consultant": _entry("voice", llm_instruction_phrasing="SC phrasing"),
        "operator": _entry("voice", llm_instruction_phrasing="OP phrasing"),
    }


def test_packet_has_one_slot_per_entry_candidate_included():
    packet = gp.build_render_packet(
        "pragmatic-architect", ["senior-consultant", "operator"], TOPIC, _voice_map()
    )
    assert packet.candidate == "pragmatic-architect"
    assert packet.axis == "voice"
    assert packet.topic_label == TOPIC_LABEL
    assert len(packet.slots) == 3
    assert {s.entry_id for s in packet.slots} == {
        "pragmatic-architect", "senior-consultant", "operator"
    }
    # Labels are A, B, C in order.
    assert [s.label for s in packet.slots] == ["A", "B", "C"]


def test_packet_mapping_is_the_hidden_key():
    packet = gp.build_render_packet(
        "pragmatic-architect", ["senior-consultant", "operator"], TOPIC, _voice_map()
    )
    assert packet.mapping == {s.label: s.entry_id for s in packet.slots}
    # Each slot's instruction is that entry's render.
    for s in packet.slots:
        assert s.instruction.endswith(f"Write about: {TOPIC_LABEL}")


def test_packet_shuffle_is_deterministic_by_seed():
    args = ("pragmatic-architect", ["senior-consultant", "operator"], TOPIC, _voice_map())
    order0 = [s.entry_id for s in gp.build_render_packet(*args, seed=0).slots]
    order0b = [s.entry_id for s in gp.build_render_packet(*args, seed=0).slots]
    order7 = [s.entry_id for s in gp.build_render_packet(*args, seed=7).slots]
    assert order0 == order0b           # same seed, same order
    assert set(order0) == set(order7)  # same membership regardless of seed


def test_packet_dedups_and_drops_candidate_from_neighbors():
    packet = gp.build_render_packet(
        "pragmatic-architect",
        ["senior-consultant", "senior-consultant", "pragmatic-architect"],
        TOPIC, _voice_map(),
    )
    assert {s.entry_id for s in packet.slots} == {
        "pragmatic-architect", "senior-consultant"
    }


def test_packet_unknown_topic_raises():
    import pytest
    with pytest.raises(ValueError):
        gp.build_render_packet(
            "pragmatic-architect", ["senior-consultant"], "no-such-topic", _voice_map()
        )


def _voice_map_rich():
    return {
        "pragmatic-architect": _entry(
            "voice",
            name="Pragmatic Architect",
            one_liner="Leads with the decision, names constraints.",
            llm_instruction_phrasing="PA phrasing",
            failure_modes=[
                {"mode": "Tips into bossy", "mitigation": "Keep the reasoning visible"},
            ],
        ),
        "senior-consultant": _entry(
            "voice",
            name="Senior Consultant",
            one_liner="Diagnoses against a framework before recommending.",
            llm_instruction_phrasing="SC phrasing",
            failure_modes=[
                {"mode": "Framework theater", "mitigation": "Use a model only where it places the situation"},
            ],
        ),
    }


def _packet_and_samples():
    id_map = _voice_map_rich()
    packet = gp.build_render_packet(
        "pragmatic-architect", ["senior-consultant"], TOPIC, id_map, seed=0
    )
    samples = {s.label: f"sample prose for slot {s.label}" for s in packet.slots}
    return packet, samples, id_map


def test_judge_prompt_lists_options_with_failure_modes():
    packet, samples, id_map = _packet_and_samples()
    prompt = gp.build_judge_prompt(packet, samples, id_map)
    assert "AXIS UNDER TEST: voice" in prompt
    assert "Pragmatic Architect" in prompt
    assert "Senior Consultant" in prompt
    assert "Tips into bossy" in prompt          # PA failure mode
    assert "Framework theater" in prompt        # SC failure mode
    assert packet.topic_label in prompt


def test_judge_prompt_includes_each_sample_under_its_label():
    packet, samples, id_map = _packet_and_samples()
    prompt = gp.build_judge_prompt(packet, samples, id_map)
    for label, text in samples.items():
        assert f"[{label}]" in prompt
        assert text in prompt


def test_judge_prompt_does_not_reveal_the_mapping():
    packet, samples, id_map = _packet_and_samples()
    prompt = gp.build_judge_prompt(packet, samples, id_map)
    # The answer key must not appear as "<label>: <entry_id>" or "<label> = <entry_id>".
    for label, entry_id in packet.mapping.items():
        assert f"{label}: {entry_id}" not in prompt
        assert f"{label} = {entry_id}" not in prompt
    # Options are listed in alphabetical id order, independent of slot order.
    pa_pos = prompt.index("pragmatic-architect")
    sc_pos = prompt.index("senior-consultant")
    assert pa_pos < sc_pos
    # Blindness through content: the samples region must leak no entry id.
    samples_region = prompt.split("THE SAMPLES:", 1)[1]
    for entry_id in packet.mapping.values():
        assert entry_id not in samples_region


def test_judge_prompt_demands_json_keys():
    packet, samples, id_map = _packet_and_samples()
    prompt = gp.build_judge_prompt(packet, samples, id_map)
    for key in ("attribution", "distinguishability", "restraint", "rationale"):
        assert key in prompt


def test_score_all_correct():
    packet, _samples, _id_map = _packet_and_samples()
    truth = packet.mapping
    score = gp.score_attribution(packet, dict(truth))
    assert score["correct"] == score["n"] == len(truth)
    assert score["accuracy"] == 1.0
    assert all(slot["correct"] for slot in score["per_slot"])


def test_score_one_wrong():
    packet, _samples, _id_map = _packet_and_samples()
    truth = packet.mapping
    guess = dict(truth)
    # Flip the two labels' guesses to force both wrong.
    labels = list(truth.keys())
    guess[labels[0]], guess[labels[1]] = truth[labels[1]], truth[labels[0]]
    score = gp.score_attribution(packet, guess)
    assert score["correct"] == 0
    assert score["accuracy"] == 0.0


def test_score_handles_missing_guess():
    packet, _samples, _id_map = _packet_and_samples()
    score = gp.score_attribution(packet, {})  # judge returned nothing
    assert score["correct"] == 0
    assert all(slot["guess"] is None for slot in score["per_slot"])


def test_run_record_round_trips_through_json():
    import json
    packet, samples, id_map = _packet_and_samples()
    judge_json = {
        "attribution": dict(packet.mapping),
        "distinguishability": "subtle",
        "restraint": {s.label: "pass" for s in packet.slots},
        "rationale": "Test rationale.",
    }
    score = gp.score_attribution(packet, judge_json["attribution"])
    record = gp.build_run_record(packet, samples, judge_json, score)
    blob = json.dumps(record)            # must be serializable
    back = json.loads(blob)
    assert back["candidate"] == "pragmatic-architect"
    assert back["score"]["accuracy"] == 1.0
    assert back["distinguishability"] == "subtle"
    assert back["mapping"] == packet.mapping


def test_nearest_neighbors_prefers_confusable_then_caps():
    id_map = gp.load_catalog()
    near = gp.nearest_neighbors("senior-consultant", id_map, limit=2)
    assert len(near) == 2
    # senior-consultant declares pragmatic-architect and executive as confusable;
    # the nearest set must draw from its declared confusables first.
    assert "pragmatic-architect" in near or "executive" in near
    assert "senior-consultant" not in near
    # Confusable-first contract: senior-consultant declares executive and
    # pragmatic-architect as confusable, so the first returned neighbor must be
    # one of its declared confusables, not a plain sibling.
    ns = gp.gate_neighbors("senior-consultant", id_map)
    assert near[0] in ns.confusable


def test_smoke_pragmatic_architect_packet_builds_on_real_catalog():
    id_map = gp.load_catalog()
    near = gp.nearest_neighbors("pragmatic-architect", id_map, limit=2)
    packet = gp.build_render_packet(
        "pragmatic-architect", near, "service-database-choice", id_map
    )
    assert packet.axis == "voice"
    assert len(packet.slots) == 3
    # Every rendered instruction carries real phrasing and the topic.
    for s in packet.slots:
        assert "Write about: Choosing Postgres vs DynamoDB" in s.instruction
        assert len(s.instruction) > 60  # real phrasing, not empty


def test_smoke_judge_prompt_builds_with_placeholder_samples():
    id_map = gp.load_catalog()
    near = gp.nearest_neighbors("pragmatic-architect", id_map, limit=2)
    packet = gp.build_render_packet(
        "pragmatic-architect", near, "service-database-choice", id_map
    )
    samples = {s.label: f"<placeholder for {s.label}>" for s in packet.slots}
    prompt = gp.build_judge_prompt(packet, samples, id_map)
    assert "AXIS UNDER TEST: voice" in prompt
    assert "Pragmatic Architect" in prompt
