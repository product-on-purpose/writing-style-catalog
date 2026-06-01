import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import generate_site_pages as gsp  # noqa: E402

REPO = Path(__file__).resolve().parents[1]


def test_load_markdown_splits_frontmatter_and_body():
    raw = "---\nid: coach\nname: Coach\n---\n\nBody text here.\n"
    fm, body = gsp.load_markdown(raw)
    assert fm["id"] == "coach"
    assert fm["name"] == "Coach"
    assert body.strip() == "Body text here."


def test_load_markdown_parses_nested_mapping():
    # PyYAML must parse nested mappings the hand-rolled parser dropped.
    raw = "---\ntypical_length:\n  min: 300\n  max: 600\n  unit: words\n---\nx\n"
    fm, _ = gsp.load_markdown(raw)
    assert fm["typical_length"] == {"min": 300, "max": 600, "unit": "words"}


def test_load_markdown_parses_block_scalar():
    raw = "---\ncanonical_template: |\n  # Title\n  ## Section\n---\nbody\n"
    fm, _ = gsp.load_markdown(raw)
    assert "# Title" in fm["canonical_template"]
    assert "## Section" in fm["canonical_template"]


def test_load_markdown_no_frontmatter_raises():
    import pytest
    with pytest.raises(ValueError):
        gsp.load_markdown("no frontmatter here\n")


def test_load_markdown_handles_crlf():
    # Repo ships CRLF files; load_markdown must not depend on the caller
    # having stripped CR first.
    raw = "---\r\nid: coach\r\nname: Coach\r\n---\r\n\r\nBody text here.\r\n"
    fm, body = gsp.load_markdown(raw)
    assert fm["id"] == "coach"
    assert fm["name"] == "Coach"
    assert body.strip() == "Body text here."
