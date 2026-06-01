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


def test_entry_url_is_base_relative_slug():
    assert gsp.entry_url("voice", "coach") == "/writing-style-library/reference/voices/coach/"
    assert gsp.entry_url("format", "adr") == "/writing-style-library/reference/formats/adr/"


def test_load_catalog_indexes_all_entries():
    cat = gsp.load_catalog()
    assert len(cat["by_id"]) == 60
    assert cat["by_id"]["coach"]["_axis"] == "voice"
    # axis buckets
    assert len(cat["by_axis"]["voice"]) == 15
    assert len(cat["by_axis"]["format"]) == 15


def test_examples_for_entry_returns_three_topics():
    ex = gsp.examples_for_entry("pragmatic-architect")
    assert set(ex.keys()) == {"async-standups", "morning-routine", "service-database-choice"}
    for topic, rec in ex.items():
        assert rec["body"].strip()
        assert rec["topic_label"]


def test_parse_diff_pair_splits_three_sections():
    raw = (
        "---\nentry_a: candid\nentry_b: warm\naxis_varied: tone\n"
        "topic_label: T\n---\n"
        "## What to notice\nNotice prose.\n\n"
        "## A: `candid`\nText A.\n\n"
        "## B: `warm`\nText B.\n"
    )
    dp = gsp.parse_diff_pair(raw)
    assert dp["entry_a"] == "candid"
    assert dp["entry_b"] == "warm"
    assert "Notice prose." in dp["what_to_notice"]
    assert dp["passage_a"].strip() == "Text A."
    assert dp["passage_b"].strip() == "Text B."


def test_diff_pairs_for_entry():
    pairs = gsp.diff_pairs_for_entry(gsp.load_diff_pairs(), "candid")
    assert len(pairs) >= 1
    assert all("candid" in (p["entry_a"], p["entry_b"]) for p in pairs)


def test_parse_diff_pair_keeps_nested_h2_in_passages():
    # Real diff-pairs (e.g. adr vs whitepaper) have passages whose bodies
    # contain their own ## headers; those must stay inside the passage, not
    # truncate it.
    raw = (
        "---\nentry_a: adr\nentry_b: whitepaper\naxis_varied: format\n"
        "topic_label: T\n---\n"
        "## What to notice\nNotice prose.\n\n---\n\n"
        "## A: `adr`\nIntro A.\n\n## Status\nProposed.\n\n## Context\nForces.\n\n---\n\n"
        "## B: `whitepaper`\nIntro B.\n\n## Executive summary\nSummary.\n\n## Background\nHistory.\n"
    )
    dp = gsp.parse_diff_pair(raw)
    # passage_a must include its nested ## Status / ## Context content
    assert "Intro A." in dp["passage_a"]
    assert "## Status" in dp["passage_a"]
    assert "Proposed." in dp["passage_a"]
    assert "## Context" in dp["passage_a"]
    assert "Forces." in dp["passage_a"]
    # passage_a must NOT bleed into passage B
    assert "Intro B." not in dp["passage_a"]
    assert "Executive summary" not in dp["passage_a"]
    # passage_b must include its nested headers
    assert "Intro B." in dp["passage_b"]
    assert "## Executive summary" in dp["passage_b"]
    assert "## Background" in dp["passage_b"]
    assert "History." in dp["passage_b"]
