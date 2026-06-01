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


def test_mdx_escape_prose_escapes_outside_code():
    src = "Email <a@b.com> and a brace {x}.\n\n`<code>` stays.\n\n```\n<raw> {kept}\n```\n"
    out = gsp.mdx_escape_prose(src)
    assert "&lt;a@b.com&gt;" not in out  # we only escape < and {, not >
    assert "&lt;a@b.com>" in out         # the < is escaped, > left as-is
    assert "&lbrace;x}" in out           # the { is escaped
    assert "`<code>`" in out             # inline code span untouched
    assert "<raw> {kept}" in out         # fenced code untouched


def test_render_entry_page_is_mdx_safe_banner_and_examples():
    cat = gsp.load_catalog()
    pairs = gsp.load_diff_pairs()
    md = gsp.render_entry_page(cat, pairs, cat["by_id"]["email"])
    # MDX comment form, not HTML comment
    assert "{/* GENERATED" in md
    assert "<!--" not in md
    # the email angle-address is escaped in the embedded example
    assert "&lt;" in md


def test_render_entry_page_has_examples_and_links():
    cat = gsp.load_catalog()
    pairs = gsp.load_diff_pairs()
    md = gsp.render_entry_page(cat, pairs, cat["by_id"]["pragmatic-architect"])
    # Starlight frontmatter
    assert md.startswith("---\n")
    assert "title:" in md
    # generated banner
    assert "GENERATED by" in md
    # llm_instruction_phrasing rendered as a code block
    assert "```text" in md
    # examples tabbed by topic via Starlight Tabs
    assert "<Tabs>" in md and "import { Tabs, TabItem }" in md
    assert "async-standups" in md
    # cross-reference links are base-relative slugs, not GitHub-relative
    assert "/writing-style-library/reference/" in md
    assert "ENTRY.md" not in md  # never emit source-file links


def test_render_diff_pair_page_uses_component_and_is_mdx_safe():
    pairs = gsp.load_diff_pairs()
    md = gsp.render_diff_pair_page(gsp.load_catalog(), pairs[0])
    assert "import DiffPair from '../../../src/components/DiffPair.astro'" in md
    assert "<DiffPair" in md
    assert 'slot="a"' in md and 'slot="b"' in md
    assert "What to notice" in md
    assert "{/* GENERATED" in md   # MDX comment form
    assert "<!--" not in md         # no HTML comment in an MDX file


def test_render_template_page_has_code_block():
    cat = gsp.load_catalog()
    fmt = cat["by_id"]["adr"]
    md = gsp.render_template_page(fmt)
    assert "```" in md
    assert "## Status" in md  # adr canonical_template content
    assert "<!-- GENERATED" in md  # plain .md uses HTML-comment banner


def test_render_recipe_page_renders_readme():
    md = gsp.render_recipe_page(gsp.load_catalog(), "architect-candid-adr")
    assert "Composition" in md
    assert "/writing-style-library/reference/" in md  # entry names linked


def test_strip_local_md_links_neutralizes_relative_md():
    assert gsp._strip_local_md_links("see [REST to GraphQL](rest-to-graphql.md)") == "see REST to GraphQL"
    assert gsp._strip_local_md_links("see [x](./foo.md)") == "see x"
    # leaves http and site-absolute links intact
    assert gsp._strip_local_md_links("[e](https://x.com/y.md)") == "[e](https://x.com/y.md)"
    assert gsp._strip_local_md_links("[c](/writing-style-library/reference/voices/coach/)") == "[c](/writing-style-library/reference/voices/coach/)"


def test_recipe_page_has_no_dangling_md_links():
    md = gsp.render_recipe_page(gsp.load_catalog(), "architect-candid-adr")
    import re as _re
    # no remaining relative .md links (markdown link whose target ends in .md and is not http/site-absolute)
    dangling = [m.group(0) for m in _re.finditer(r"\[[^\]]+\]\(([^)]+)\)", md)
                if not m.group(1).startswith("http") and not m.group(1).startswith("/") and m.group(1).split("#")[0].endswith(".md")]
    assert dangling == [], f"dangling md links: {dangling}"


def test_list_recipes_finds_all_five():
    assert len(gsp.list_recipes()) == 5
    assert "architect-candid-adr" in gsp.list_recipes()


def test_render_reference_index_lists_axes():
    cat = gsp.load_catalog()
    md = gsp.render_reference_index(cat)
    assert "## Voices" in md and "## Formats" in md
    assert "/writing-style-library/reference/voices/coach/" in md


def test_render_diff_pair_index_groups_by_axis():
    md = gsp.render_diff_pair_index(gsp.load_diff_pairs())
    assert "tone" in md.lower()
    assert "/writing-style-library/examples/diff-pairs/" in md


def test_fidelity_lint_flags_orphan_period():
    bad = "This sentence ends oddly . Then continues."
    hits = gsp.fidelity_warnings(bad)
    assert any("orphan" in h.lower() or "space before period" in h.lower() for h in hits)


def test_fidelity_lint_clean_text_no_warnings():
    assert gsp.fidelity_warnings("A normal clean sentence. Another one.") == []


def test_fidelity_lint_still_flags_true_doubled_period():
    assert any("doubled period" in h for h in gsp.fidelity_warnings("the end.. next"))


def test_fidelity_lint_ignores_ellipsis():
    assert gsp.fidelity_warnings("One way to think about this is...") == []
    assert gsp.fidelity_warnings("Wait... really? And more....") == []
