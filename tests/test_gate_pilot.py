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
