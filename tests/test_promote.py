"""Regression tests for the transactional promotion tool (tools/promote.py).

Covers the pure-function invariants the audit flagged as untested (D-6):
- flip_text: the exactly-one-column-0-draft-line rule, CRLF preservation, the
  block-scalar lookalike guard, and body immutability
- preflight status classification against the real catalog (read-only)
- all_draft_ids ordering and admitted-entry exclusion
- the two-rung ladder (ADR 0021): tooling flips draft -> machine-verified, the
  maintainer rung flips machine-verified -> stable and refuses a bulk flip

The write/rollback path is deliberately NOT exercised here: it operates on the
real catalog via a module-level ROOT and is protected by the staged-write
design plus preflight; testing it would require mutating real entries.

Loads the module by path, mirroring tests/test_compose_instruction.py.
"""
import importlib.util
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "promote.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("promote", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


promote = _load_module()


def _entry(frontmatter_lines, body="\nBody text here.\n"):
    return "---\n" + "\n".join(frontmatter_lines) + "\n---\n" + body


# --- flip_text -------------------------------------------------------------


def test_flip_text_flips_the_single_draft_line():
    text = _entry(["id: sample", "axis: voice", "review_status: draft"])
    flipped = promote.flip_text(text)
    assert "review_status: machine-verified" in flipped
    assert "review_status: draft" not in flipped
    assert flipped.endswith("\nBody text here.\n")


def test_flip_text_preserves_crlf_line_endings():
    text = _entry(["id: sample", "review_status: draft"]).replace("\n", "\r\n")
    flipped = promote.flip_text(text)
    assert "review_status: machine-verified\r\n" in flipped
    assert "\n" not in flipped.replace("\r\n", "")  # no bare LF introduced


def test_flip_text_rejects_text_without_frontmatter():
    with pytest.raises(ValueError, match="no frontmatter block"):
        promote.flip_text("just a body, no frontmatter\n")


def test_flip_text_rejects_zero_draft_lines():
    text = _entry(["id: sample", "review_status: stable"])
    with pytest.raises(ValueError, match="found 0"):
        promote.flip_text(text)


def test_flip_text_rejects_multiple_draft_lines():
    text = _entry(["review_status: draft", "review_status: draft"])
    with pytest.raises(ValueError, match="found 2"):
        promote.flip_text(text)


def test_flip_text_ignores_indented_lookalike_inside_block_scalar():
    text = _entry(
        [
            "id: sample",
            "notes: |",
            "  review_status: draft",
            "review_status: draft",
        ]
    )
    flipped = promote.flip_text(text)
    # the real column-0 field flipped
    assert "\nreview_status: machine-verified\n" in flipped
    # the indented lookalike inside the block scalar untouched
    assert "  review_status: draft" in flipped


def test_flip_text_does_not_touch_body_occurrences():
    text = _entry(
        ["id: sample", "review_status: draft"],
        body="\nThe docs say entries start at\nreview_status: draft\nby default.\n",
    )
    flipped = promote.flip_text(text)
    # frontmatter flipped, body occurrence intact
    assert flipped.count("review_status: machine-verified") == 1
    assert "review_status: draft\nby default." in flipped


# --- preflight and inventory against the real catalog (read-only) ----------


def test_preflight_rejects_an_admitted_entry_on_the_tooling_rung():
    status, detail = promote.preflight("pragmatic-architect")
    assert status == "wrong_rung"
    assert "draft" in detail


def test_preflight_reports_unknown_ids_as_not_found():
    status, detail = promote.preflight("definitely-not-a-real-entry-id")
    assert status == "not_found"
    assert "taxonomy" in detail


def test_all_draft_ids_is_sorted_and_excludes_admitted_entries():
    ids = promote.all_draft_ids()
    assert ids == sorted(ids)
    assert "pragmatic-architect" not in ids


def test_preflight_classifies_a_real_draft_sanely():
    ids = promote.all_draft_ids()
    if not ids:
        pytest.skip("no draft entries in the catalog to test against")
    status, detail = promote.preflight(ids[0])
    # a real draft is either fully rendered (ready) or missing samples
    assert status in {"ready", "incomplete"}
    assert isinstance(detail, str) and detail


def test_missing_samples_empty_for_a_gate2_admitted_entry():
    # Gate 2 (validate.py) enforces 12/12 samples for every admitted entry, so an
    # admitted seed entry must report nothing missing.
    assert promote.missing_samples("voice", "pragmatic-architect") == []


# --- the maintainer rung (ADR 0021) ----------------------------------------


def test_maintainer_rung_flips_machine_verified_to_stable():
    text = _entry(["id: sample", "review_status: machine-verified"])
    flipped = promote.flip_text(text, promote.MAINTAINER_RUNG)
    assert "review_status: stable" in flipped
    assert "machine-verified" not in flipped


def test_maintainer_rung_cannot_skip_the_tooling_rung():
    # A draft has not passed the enforced checks; it cannot jump straight to stable.
    text = _entry(["id: sample", "review_status: draft"])
    with pytest.raises(ValueError, match="review_status: machine-verified"):
        promote.flip_text(text, promote.MAINTAINER_RUNG)


def test_preflight_accepts_a_machine_verified_entry_on_the_maintainer_rung():
    status, _ = promote.preflight("pragmatic-architect", promote.MAINTAINER_RUNG)
    assert status == "ready"


def test_reviewed_refuses_all_ready(monkeypatch, capsys):
    # A bulk flip to stable would claim a reading that did not happen.
    monkeypatch.setattr("sys.argv", ["promote.py", "--reviewed", "--all-ready"])
    assert promote.main() == 1
    assert "named ids only" in capsys.readouterr().out
