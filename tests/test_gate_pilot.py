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
