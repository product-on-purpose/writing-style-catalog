# Astro Starlight Documentation Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the MkDocs Material docs stack with an Astro Starlight site whose catalog pages (entries, examples, diff-pairs, recipes, templates) are generated from `taxonomy/` and `examples/` by a Python generator, so every entry page embeds its worked examples and live cross-references, then deploy it to GitHub Pages.

**Architecture:** Approach A from ADR 0011: a Python generator (`scripts/generate_site_pages.py`) reads the catalog with PyYAML and writes committed Markdown/MDX into the Starlight `docs/` tree, emitting Starlight-correct slug links in-generator (no post-build rewriter). Starlight's native autogenerate sidebar renders the committed pages. A freshness guard regenerates and `git diff`s in CI. The MkDocs stack is removed entirely. Site deploys to `product-on-purpose.github.io/writing-style-library`.

**Tech Stack:** Astro `^6.3`, `@astrojs/starlight ~0.39`, `astro-mermaid`, `sharp`, Node >=22.12 (present: v22.12.0, npm 10.9.0); Python 3.12 + PyYAML 6.0.3 (present) for the generator; GitHub Actions + official Pages actions for deploy.

---

## Reference facts (verified on disk 2026-05-31)

- Catalog: 60 entries (`taxonomy/{voices,tones,styles,formats}/<id>/ENTRY.md`), every entry has exactly 3 vertical-slice examples. 180 vertical slices, 12 diff-pairs, 5 recipes, 15 format `canonical_template`s.
- Anchor topics (dir slugs under `examples/vertical-slices/`): `async-standups`, `morning-routine`, `service-database-choice`.
- Vertical-slice filename pattern: `examples/vertical-slices/<topic>/<axis>-<id>.md` (e.g. `voice-pragmatic-architect.md`). Frontmatter keys: `entry_id, axis, topic_slug, topic_label, author_type, llm_model, review_status`.
- Diff-pair files: `examples/diff-pairs/<topic>/*.md`. Frontmatter: `diff_pair_id, topic_slug, topic_label, axis_varied, entry_a, entry_b, generator, review_status`. Body H2 order is `## What to notice` FIRST, then `## A: \`<id>\`` then `## B: \`<id>\``. The split must key off the header text, not position.
- Recipe folders: `examples/horizontal-slices/<recipe>/README.md` + worked-output `.md` files. README has `## When to use`, `## When to use something else`, `## Composition` (a markdown table: Axis / Entry / Why).
- Entry frontmatter (all axes): `id, name, axis, one_liner, description, language_patterns, pairs_well_with, avoid_with, confusable_with, when_to_use, when_not_to_use, llm_instruction_phrasing, tags, review_status`. Formats add `canonical_template, typical_voices, typical_tones, digital_or_print`. Voices may add `diction, sentence_style, default_pov, typical_tones` (inconsistently present).
- Existing root `package.json` is `@product-on-purpose/writing-style-library` (private) with scripts `validate` and `build-site`. It MUST be edited, not overwritten - the Astro deps and scripts are added to it.
- Authored pages today: `docs/index.md`, `docs/concepts/{three-axis-model,composition,glossary}.md`, `docs/how-to/{compose-instruction,pick-voice,add-entry}.md`, `docs/design-standards/{voice-and-tone,naming-conventions,style-tells}.md`, `docs/governance/contribution-process.md`. The spec IA renames `how-to/` to `guides/`.
- `tools/build-indexes.py` writes `taxonomy.json` (KEEP) and `docs/reference/index.md` (RETIRE - replaced by generated reference).
- Hard rule: no em-dashes (U+2014) or en-dashes (U+2013) anywhere, enforced by a pre-commit hook and `validate.py`. All generated output and all files in this plan must use " - ".

## File structure (what gets created / modified)

**Created:**
- `astro.config.mjs` - Starlight config (site, base, integrations, sidebar, editLink).
- `src/content.config.ts` - docs collection via Starlight `docsLoader()`.
- `src/styles/custom.css` - minimal brand CSS.
- `src/components/DiffPair.astro` - side-by-side A/B renderer.
- `scripts/generate_site_pages.py` - THE generator (catalog -> committed docs pages).
- `scripts/check_generated_fresh.py` - regenerate + `git diff --exit-code` guard.
- `tests/test_generate_site_pages.py` - pytest for the generator's pure functions.
- `docs/index.mdx` - home (converted from `docs/index.md`).
- Generated trees: `docs/reference/{voices,tones,styles,formats}/<id>.md`, `docs/examples/<topic>/index.md`, `docs/examples/diff-pairs/*.mdx` + `index.md`, `docs/recipes/*.md` + `index.md`, `docs/templates/*.md` + `index.md`.
- `.github/workflows/build-site.yml` - REPLACES the MkDocs one (build + deploy).

**Modified:**
- `package.json` (root) - add `type: module`, Astro deps, `dev`/`build`/`preview` scripts.
- `requirements-dev.txt` - drop mkdocs deps, add `pyyaml`, `pytest`.
- `tools/build-indexes.py` - stop writing `docs/reference/index.md`; keep `taxonomy.json`.
- `.gitignore` - add `.astro/`.
- Move authored `docs/how-to/*` to `docs/guides/*`.

**Deleted:**
- `mkdocs.yml`, `docs/reference/index.md` (regenerated as a tree), `docs/*/.gitkeep` where a real page now exists.

---

## Task 1: Scaffold the Astro Starlight project

**Files:**
- Modify: `package.json`
- Create: `astro.config.mjs`, `src/content.config.ts`, `src/styles/custom.css`
- Modify: `.gitignore`

- [ ] **Step 1: Add Astro deps and scripts to the existing package.json**

Edit `package.json` to this (keep name/version/license; add `type`, `engines`, deps, and dev/build/preview scripts; keep `validate`):

```json
{
  "name": "@product-on-purpose/writing-style-library",
  "version": "0.1.0",
  "description": "A composable catalog of writing instructions organized along three axes",
  "private": true,
  "type": "module",
  "license": "Apache-2.0",
  "engines": { "node": ">=22.12.0" },
  "scripts": {
    "validate": "python tools/validate.py",
    "generate": "python scripts/generate_site_pages.py",
    "dev": "npm run generate && astro dev",
    "build": "npm run generate && astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "@astrojs/starlight": "~0.39.0",
    "astro": "^6.3.0",
    "astro-mermaid": "~2.0.1",
    "sharp": "^0.34.5"
  },
  "overrides": {
    "mermaid": "^11.15.0"
  }
}
```

- [ ] **Step 2: Install dependencies**

Run: `npm install`
Expected: `node_modules/` created, `package-lock.json` written, exit 0.

- [ ] **Step 3: Add `.astro/` to .gitignore**

Append to `.gitignore` under the `# Node` section (the file already ignores `node_modules/` and `dist/`):

```
# Astro
.astro/
```

- [ ] **Step 4: Write astro.config.mjs**

Create `astro.config.mjs`:

```js
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import mermaid from 'astro-mermaid';

export default defineConfig({
  site: 'https://product-on-purpose.github.io',
  base: '/writing-style-library',
  integrations: [
    // astro-mermaid must come BEFORE starlight (integration-order rule).
    mermaid({ theme: 'default', autoTheme: true }),
    starlight({
      title: 'Writing Style Library',
      description: 'Composable writing instructions on four orthogonal axes: Voice, Tone, Style, Format.',
      editLink: { baseUrl: 'https://github.com/product-on-purpose/writing-style-library/edit/main/' },
      customCss: ['./src/styles/custom.css'],
      // Starlight 0.39: autogenerate must be wrapped in items: [].
      sidebar: [
        { label: 'Home', link: '/' },
        { label: 'Concepts', items: [{ autogenerate: { directory: 'concepts' } }] },
        { label: 'Guides', items: [{ autogenerate: { directory: 'guides' } }] },
        { label: 'Reference', items: [{ autogenerate: { directory: 'reference' } }] },
        { label: 'Examples', items: [{ autogenerate: { directory: 'examples' } }] },
        { label: 'Recipes', items: [{ autogenerate: { directory: 'recipes' } }] },
        { label: 'Templates', items: [{ autogenerate: { directory: 'templates' } }] },
        { label: 'Design Standards', items: [{ autogenerate: { directory: 'design-standards' } }] },
        { label: 'Contributing', items: [{ autogenerate: { directory: 'governance' } }] },
      ],
    }),
  ],
});
```

- [ ] **Step 5: Write src/content.config.ts**

Create `src/content.config.ts`:

```ts
import { defineCollection } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

export const collections = {
  docs: defineCollection({ loader: docsLoader(), schema: docsSchema() }),
};
```

- [ ] **Step 6: Write minimal custom.css**

Create `src/styles/custom.css`:

```css
/* Writing Style Library brand accents. Kept minimal; expand later. */
:root {
  --sl-color-accent-low: #2a1a4a;
  --sl-color-accent: #7c3aed;
  --sl-color-accent-high: #c4b5fd;
}
```

- [ ] **Step 7: Commit**

```bash
git add package.json package-lock.json astro.config.mjs src/content.config.ts src/styles/custom.css .gitignore
git commit -m "feat(site): scaffold Astro Starlight project shell"
```

---

## Task 2: Generator core - frontmatter loading with PyYAML

Build the data layer first, test-driven. This is the foundation the page emitters use.

**Files:**
- Create: `scripts/generate_site_pages.py`
- Create: `tests/test_generate_site_pages.py`
- Modify: `requirements-dev.txt`

- [ ] **Step 1: Update requirements-dev.txt**

Replace the contents of `requirements-dev.txt` with:

```
pyyaml>=6.0
jsonschema>=4.18.0
referencing>=0.30.0
pytest>=8.0.0
pre-commit>=3.0.0
```

(Drops `mkdocs`, `mkdocs-material`, `pymdown-extensions`; adds `pyyaml`, `pytest`, and declares `referencing` which `validate.py` already imports. Bumps `jsonschema` floor to the `referencing`-split version.)

Run: `pip install -r requirements-dev.txt`
Expected: installs cleanly, exit 0.

- [ ] **Step 2: Write the failing test for frontmatter loading**

Create `tests/test_generate_site_pages.py`:

```python
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
```

- [ ] **Step 3: Run the test to verify it fails**

Run: `pytest tests/test_generate_site_pages.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'generate_site_pages'` (the script does not exist yet).

- [ ] **Step 4: Write the generator scaffolding and load_markdown**

Create `scripts/generate_site_pages.py`:

```python
#!/usr/bin/env python3
"""Generate Starlight docs pages from the writing-style-library catalog.

Reads taxonomy/ and examples/ (with PyYAML, NOT the repo's hand-rolled parser)
and writes committed Markdown/MDX into docs/ where Starlight's autogenerate
sidebar renders it. Emits Starlight-correct slug links in-generator; there is
NO post-build link rewriter (see ADR 0011 and the design spec section 5.5).

Usage:
    python scripts/generate_site_pages.py            # write into docs/
    python scripts/generate_site_pages.py --out DIR  # write into DIR (used by the freshness check)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
TAXONOMY = REPO_ROOT / "taxonomy"
EXAMPLES = REPO_ROOT / "examples"
DOCS = REPO_ROOT / "docs"

AXES = ["voice", "tone", "style", "format"]
AXIS_DIR = {"voice": "voices", "tone": "tones", "style": "styles", "format": "formats"}
TOPICS = ["async-standups", "morning-routine", "service-database-choice"]

GENERATED_BANNER = (
    "<!-- GENERATED by scripts/generate_site_pages.py - do not edit by hand. "
    "Edit the source under taxonomy/ or examples/ and regenerate. -->"
)

_FM_SPLIT = re.compile(r"(?ms)\A---[ \t]*\n(.*?)\n---[ \t]*\n?(.*)\Z")


def load_markdown(raw: str) -> tuple[dict, str]:
    """Split a frontmatter markdown string into (frontmatter dict, body)."""
    m = _FM_SPLIT.match(raw)
    if not m:
        raise ValueError("no frontmatter block found")
    fm = yaml.safe_load(m.group(1)) or {}
    return fm, m.group(2)


def read_entry(axis: str, entry_dir: Path) -> dict:
    fm, body = load_markdown((entry_dir / "ENTRY.md").read_text(encoding="utf-8"))
    fm["_axis"] = axis
    fm["_body"] = body
    return fm
```

- [ ] **Step 5: Run the test to verify it passes**

Run: `pytest tests/test_generate_site_pages.py -v`
Expected: all 4 tests PASS.

- [ ] **Step 6: Commit**

```bash
git add scripts/generate_site_pages.py tests/test_generate_site_pages.py requirements-dev.txt
git commit -m "feat(site): generator frontmatter loading with PyYAML"
```

---

## Task 3: Slug-link helpers and the catalog index

The link strategy (spec 5.5) lives here: pure functions that map an entry id to its site URL. Tested so links never regress to GitHub-relative.

**Files:**
- Modify: `scripts/generate_site_pages.py`
- Modify: `tests/test_generate_site_pages.py`

- [ ] **Step 1: Write failing tests for the slug-link helpers**

Append to `tests/test_generate_site_pages.py`:

```python
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
```

- [ ] **Step 2: Run to verify failure**

Run: `pytest tests/test_generate_site_pages.py -v`
Expected: FAIL with `AttributeError: module 'generate_site_pages' has no attribute 'entry_url'`.

- [ ] **Step 3: Implement entry_url, BASE, and load_catalog**

Add to `scripts/generate_site_pages.py` (after `read_entry`):

```python
BASE = "/writing-style-library"


def entry_url(axis: str, entry_id: str) -> str:
    """Starlight slug URL for an entry's reference page (trailing slash)."""
    return f"{BASE}/reference/{AXIS_DIR[axis]}/{entry_id}/"


def entry_link(catalog: dict, entry_id: str) -> str:
    """Markdown link to an entry by id, using its display name. Falls back to the id."""
    entry = catalog["by_id"].get(entry_id)
    if not entry:
        return f"`{entry_id}`"
    return f"[{entry['name']}]({entry_url(entry['_axis'], entry_id)})"


def load_catalog() -> dict:
    by_id: dict[str, dict] = {}
    by_axis: dict[str, list[dict]] = {a: [] for a in AXES}
    for axis in AXES:
        axis_path = TAXONOMY / AXIS_DIR[axis]
        for entry_dir in sorted(axis_path.iterdir()):
            if not entry_dir.is_dir():
                continue
            entry = read_entry(axis, entry_dir)
            by_id[entry["id"]] = entry
            by_axis[axis].append(entry)
    return {"by_id": by_id, "by_axis": by_axis}
```

- [ ] **Step 4: Run to verify pass**

Run: `pytest tests/test_generate_site_pages.py -v`
Expected: all tests PASS (now 6).

- [ ] **Step 5: Commit**

```bash
git add scripts/generate_site_pages.py tests/test_generate_site_pages.py
git commit -m "feat(site): slug-link helpers and catalog index loader"
```

---

## Task 4: Example and diff-pair indexing helpers

Reverse lookups: which examples belong to an entry, which diff-pairs an entry appears in, parsing a diff-pair body into its three parts.

**Files:**
- Modify: `scripts/generate_site_pages.py`
- Modify: `tests/test_generate_site_pages.py`

- [ ] **Step 1: Write failing tests**

Append to `tests/test_generate_site_pages.py`:

```python
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
```

- [ ] **Step 2: Run to verify failure**

Run: `pytest tests/test_generate_site_pages.py -v`
Expected: FAIL with `AttributeError` on `examples_for_entry`.

- [ ] **Step 3: Implement the helpers**

Add to `scripts/generate_site_pages.py`:

```python
def examples_for_entry(entry_id: str) -> dict:
    """Map topic-slug -> {body, topic_label} for an entry's vertical slices."""
    out: dict[str, dict] = {}
    for topic in TOPICS:
        topic_dir = EXAMPLES / "vertical-slices" / topic
        if not topic_dir.exists():
            continue
        for md in sorted(topic_dir.glob("*.md")):
            fm, body = load_markdown(md.read_text(encoding="utf-8"))
            if fm.get("entry_id") == entry_id:
                out[topic] = {"body": body, "topic_label": fm.get("topic_label", topic)}
                break
    return out


# Diff-pair body has H2s in the order: "What to notice", "A: `id`", "B: `id`".
_H2 = re.compile(r"(?m)^##\s+(.*?)\s*$")


def parse_diff_pair(raw: str) -> dict:
    fm, body = load_markdown(raw)
    # Split body on H2 headers, keyed by normalized header text.
    sections: dict[str, str] = {}
    matches = list(_H2.finditer(body))
    for i, mt in enumerate(matches):
        start = mt.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        header = mt.group(1).lower()
        text = body[start:end].strip()
        if header.startswith("what to notice"):
            sections["what_to_notice"] = text
        elif header.startswith("a:"):
            sections["passage_a"] = text
        elif header.startswith("b:"):
            sections["passage_b"] = text
    return {
        "entry_a": fm.get("entry_a"),
        "entry_b": fm.get("entry_b"),
        "axis_varied": fm.get("axis_varied"),
        "topic_label": fm.get("topic_label", ""),
        "diff_pair_id": fm.get("diff_pair_id", ""),
        "what_to_notice": sections.get("what_to_notice", ""),
        "passage_a": sections.get("passage_a", ""),
        "passage_b": sections.get("passage_b", ""),
    }


def load_diff_pairs() -> list[dict]:
    out = []
    base = EXAMPLES / "diff-pairs"
    if not base.exists():
        return out
    for md in sorted(base.rglob("*.md")):
        if md.name == "README.md":
            continue
        out.append(parse_diff_pair(md.read_text(encoding="utf-8")))
    return out


def diff_pairs_for_entry(pairs: list[dict], entry_id: str) -> list[dict]:
    return [p for p in pairs if entry_id in (p["entry_a"], p["entry_b"])]
```

- [ ] **Step 4: Run to verify pass**

Run: `pytest tests/test_generate_site_pages.py -v`
Expected: all PASS (now 9).

- [ ] **Step 5: Commit**

```bash
git add scripts/generate_site_pages.py tests/test_generate_site_pages.py
git commit -m "feat(site): example and diff-pair indexing helpers"
```

---

## Task 5: Entry-page emitter

The centerpiece: render one entry to a Starlight markdown page with embedded examples (tabbed by topic) and live cross-reference links.

**Files:**
- Modify: `scripts/generate_site_pages.py`
- Modify: `tests/test_generate_site_pages.py`

- [ ] **Step 1: Write failing test for the entry-page renderer**

Append to `tests/test_generate_site_pages.py`:

```python
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
```

- [ ] **Step 2: Run to verify failure**

Run: `pytest tests/test_generate_site_pages.py -v`
Expected: FAIL with `AttributeError` on `render_entry_page`.

- [ ] **Step 3: Implement render_entry_page**

Add to `scripts/generate_site_pages.py`:

```python
def _yaml_title(text: str) -> str:
    """Safe single-line YAML scalar for a frontmatter title/description."""
    return '"' + text.replace('"', "'") + '"'


def _xref_block(catalog: dict, entry: dict, field: str, heading: str) -> str:
    ids = entry.get(field) or []
    if not ids:
        return ""
    links = ", ".join(entry_link(catalog, i) for i in ids)
    return f"### {heading}\n\n{links}\n\n"


def render_entry_page(catalog: dict, pairs: list[dict], entry: dict) -> str:
    axis = entry["_axis"]
    out = []
    out.append("---")
    out.append(f"title: {_yaml_title(entry['name'])}")
    out.append(f"description: {_yaml_title(entry.get('one_liner', ''))}")
    out.append("---")
    out.append("")
    out.append(GENERATED_BANNER)
    out.append("")
    out.append("import { Tabs, TabItem } from '@astrojs/starlight/components';")
    out.append("")
    out.append(f"> {entry.get('one_liner', '')}")
    out.append("")
    out.append(entry.get("_body", "").strip())
    out.append("")

    # llm_instruction_phrasing as a copy-buttoned code block
    phrasing = entry.get("llm_instruction_phrasing", "").strip()
    if phrasing:
        out.append("## Instruction")
        out.append("")
        out.append("```text")
        out.append(phrasing)
        out.append("```")
        out.append("")

    # Format-only: canonical template + link to template gallery page
    if axis == "format" and entry.get("canonical_template"):
        out.append("## Template")
        out.append("")
        out.append(f"See the [{entry['name']} template]({BASE}/templates/{entry['id']}/).")
        out.append("")

    # Cross-references as live links
    xref = ""
    xref += _xref_block(catalog, entry, "pairs_well_with", "Pairs well with")
    xref += _xref_block(catalog, entry, "avoid_with", "Avoid with")
    xref += _xref_block(catalog, entry, "confusable_with", "Often confused with")
    if xref:
        out.append("## Related")
        out.append("")
        out.append(xref.rstrip())
        out.append("")

    # Embedded examples tabbed by anchor topic
    examples = examples_for_entry(entry["id"])
    if examples:
        out.append("## Examples")
        out.append("")
        out.append("<Tabs>")
        for topic in TOPICS:
            rec = examples.get(topic)
            if not rec:
                continue
            out.append(f'<TabItem label="{rec["topic_label"]}">')
            out.append("")
            out.append(rec["body"].strip())
            out.append("")
            out.append("</TabItem>")
        out.append("</Tabs>")
        out.append("")

    # Appears-in diff-pairs
    appears = diff_pairs_for_entry(pairs, entry["id"])
    if appears:
        out.append("## Appears in diff-pairs")
        out.append("")
        for p in appears:
            other = p["entry_b"] if p["entry_a"] == entry["id"] else p["entry_a"]
            out.append(
                f"- [{entry['id']} vs {other}]"
                f"({BASE}/examples/diff-pairs/{p['diff_pair_id']}/) "
                f"(varies {p['axis_varied']})"
            )
        out.append("")

    return "\n".join(out).rstrip() + "\n"
```

NOTE: a `.md` file containing `import ...` and `<Tabs>` must be authored as `.mdx`. Entry pages are written with the `.mdx` extension in Task 8.

- [ ] **Step 4: Run to verify pass**

Run: `pytest tests/test_generate_site_pages.py -v`
Expected: all PASS (now 10).

- [ ] **Step 5: Commit**

```bash
git add scripts/generate_site_pages.py tests/test_generate_site_pages.py
git commit -m "feat(site): entry-page emitter with embedded examples and xref links"
```

---

## Task 6: Diff-pair, recipe, and template emitters + the DiffPair component

**Files:**
- Modify: `scripts/generate_site_pages.py`
- Create: `src/components/DiffPair.astro`
- Modify: `tests/test_generate_site_pages.py`

- [ ] **Step 1: Write the DiffPair component**

Create `src/components/DiffPair.astro`:

```astro
---
interface Props { labelA: string; labelB: string; }
const { labelA, labelB } = Astro.props;
---
<div class="diff-pair">
  <div class="diff-col">
    <h3>{labelA}</h3>
    <slot name="a" />
  </div>
  <div class="diff-col">
    <h3>{labelB}</h3>
    <slot name="b" />
  </div>
</div>
<style>
  .diff-pair { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
  .diff-col { border: 1px solid var(--sl-color-gray-5); border-radius: 0.5rem; padding: 1rem; }
  @media (max-width: 72rem) { .diff-pair { grid-template-columns: 1fr; } }
</style>
```

- [ ] **Step 2: Write failing tests for the three emitters**

Append to `tests/test_generate_site_pages.py`:

```python
def test_render_diff_pair_page_uses_component():
    pairs = gsp.load_diff_pairs()
    md = gsp.render_diff_pair_page(gsp.load_catalog(), pairs[0])
    assert "import DiffPair" in md
    assert "<DiffPair" in md
    assert 'slot="a"' in md and 'slot="b"' in md
    assert "What to notice" in md


def test_render_template_page_has_code_block():
    cat = gsp.load_catalog()
    fmt = cat["by_id"]["adr"]
    md = gsp.render_template_page(fmt)
    assert "```" in md
    assert "## Status" in md  # adr canonical_template content


def test_render_recipe_page_renders_readme():
    md = gsp.render_recipe_page(gsp.load_catalog(), "architect-candid-adr")
    assert "Composition" in md
    assert "/writing-style-library/reference/" in md  # entry names linked
```

- [ ] **Step 3: Run to verify failure**

Run: `pytest tests/test_generate_site_pages.py -v`
Expected: FAIL with `AttributeError` on `render_diff_pair_page`.

- [ ] **Step 4: Implement the three emitters**

Add to `scripts/generate_site_pages.py`:

```python
RECIPES_DIR = EXAMPLES / "horizontal-slices"


def render_diff_pair_page(catalog: dict, dp: dict) -> str:
    a_link = entry_link(catalog, dp["entry_a"])
    b_link = entry_link(catalog, dp["entry_b"])
    title = f"{dp['entry_a']} vs {dp['entry_b']}"
    out = [
        "---",
        f"title: {_yaml_title(title)}",
        f"description: {_yaml_title(dp['topic_label'])}",
        "---",
        "",
        GENERATED_BANNER,
        "",
        "import DiffPair from '../../../components/DiffPair.astro';",
        "",
        f"**Topic:** {dp['topic_label']}  ",
        f"**Axis varied:** {dp['axis_varied']}  ",
        f"**A:** {a_link}  **B:** {b_link}",
        "",
        "## What to notice",
        "",
        dp["what_to_notice"],
        "",
        f'<DiffPair labelA="A: {dp["entry_a"]}" labelB="B: {dp["entry_b"]}">',
        '<div slot="a">',
        "",
        dp["passage_a"],
        "",
        "</div>",
        '<div slot="b">',
        "",
        dp["passage_b"],
        "",
        "</div>",
        "</DiffPair>",
        "",
    ]
    return "\n".join(out).rstrip() + "\n"


def render_template_page(fmt: dict) -> str:
    template = (fmt.get("canonical_template") or "").rstrip()
    out = [
        "---",
        f"title: {_yaml_title(fmt['name'] + ' template')}",
        f"description: {_yaml_title('Canonical template for the ' + fmt['name'] + ' format.')}",
        "---",
        "",
        GENERATED_BANNER,
        "",
        f"Canonical template for the [{fmt['name']}]({entry_url('format', fmt['id'])}) format.",
        "",
        "```markdown",
        template,
        "```",
        "",
    ]
    return "\n".join(out).rstrip() + "\n"


def _link_entry_names_in_table(catalog: dict, text: str) -> str:
    """Replace `id` backtick tokens in a recipe README with entry links."""
    def repl(m):
        token = m.group(1)
        return entry_link(catalog, token) if token in catalog["by_id"] else m.group(0)
    return re.sub(r"`([a-z][a-z0-9-]*)`", repl, text)


def render_recipe_page(catalog: dict, recipe_slug: str) -> str:
    readme = (RECIPES_DIR / recipe_slug / "README.md").read_text(encoding="utf-8")
    # README has no frontmatter; first line is "# Recipe: <slug>".
    lines = readme.splitlines()
    heading = lines[0].lstrip("# ").strip() if lines else recipe_slug
    body = "\n".join(lines[1:]).strip()
    body = _link_entry_names_in_table(catalog, body)
    out = [
        "---",
        f"title: {_yaml_title(heading)}",
        "---",
        "",
        GENERATED_BANNER,
        "",
        body,
        "",
    ]
    return "\n".join(out).rstrip() + "\n"


def list_recipes() -> list[str]:
    if not RECIPES_DIR.exists():
        return []
    return sorted(d.name for d in RECIPES_DIR.iterdir() if d.is_dir() and (d / "README.md").exists())
```

- [ ] **Step 5: Run to verify pass**

Run: `pytest tests/test_generate_site_pages.py -v`
Expected: all PASS (now 13).

- [ ] **Step 6: Commit**

```bash
git add scripts/generate_site_pages.py src/components/DiffPair.astro tests/test_generate_site_pages.py
git commit -m "feat(site): diff-pair, recipe, template emitters and DiffPair component"
```

---

## Task 7: Index pages for galleries

Each generated section needs an `index.md` so the sidebar group has a landing page.

**Files:**
- Modify: `scripts/generate_site_pages.py`
- Modify: `tests/test_generate_site_pages.py`

- [ ] **Step 1: Write failing test**

Append to `tests/test_generate_site_pages.py`:

```python
def test_render_reference_index_lists_axes():
    cat = gsp.load_catalog()
    md = gsp.render_reference_index(cat)
    assert "## Voices" in md and "## Formats" in md
    assert "/writing-style-library/reference/voices/coach/" in md


def test_render_diff_pair_index_groups_by_axis():
    md = gsp.render_diff_pair_index(gsp.load_diff_pairs())
    assert "tone" in md.lower()
    assert "/writing-style-library/examples/diff-pairs/" in md
```

- [ ] **Step 2: Run to verify failure**

Run: `pytest tests/test_generate_site_pages.py -v`
Expected: FAIL with `AttributeError` on `render_reference_index`.

- [ ] **Step 3: Implement the index renderers**

Add to `scripts/generate_site_pages.py`:

```python
AXIS_LABEL = {"voice": "Voices", "tone": "Tones", "style": "Styles", "format": "Formats"}


def _page(title: str, description: str, body: str) -> str:
    out = [
        "---",
        f"title: {_yaml_title(title)}",
        f"description: {_yaml_title(description)}",
        "---",
        "",
        GENERATED_BANNER,
        "",
        body.strip(),
        "",
    ]
    return "\n".join(out).rstrip() + "\n"


def render_reference_index(catalog: dict) -> str:
    parts = []
    for axis in AXES:
        parts.append(f"## {AXIS_LABEL[axis]}")
        parts.append("")
        for e in catalog["by_axis"][axis]:
            parts.append(f"- [{e['name']}]({entry_url(axis, e['id'])}) - {e.get('one_liner', '')}")
        parts.append("")
    return _page("Reference", "Every entry across the four axes.", "\n".join(parts))


def render_diff_pair_index(pairs: list[dict]) -> str:
    by_axis: dict[str, list[dict]] = {}
    for p in pairs:
        by_axis.setdefault(p["axis_varied"], []).append(p)
    parts = []
    for axis in sorted(by_axis):
        parts.append(f"## Varying {axis}")
        parts.append("")
        for p in by_axis[axis]:
            parts.append(
                f"- [{p['entry_a']} vs {p['entry_b']}]"
                f"({BASE}/examples/diff-pairs/{p['diff_pair_id']}/) - {p['topic_label']}"
            )
        parts.append("")
    return _page("Diff-pairs", "Side-by-side single-axis contrasts.", "\n".join(parts))


def render_recipe_index(catalog: dict) -> str:
    parts = []
    for slug in list_recipes():
        parts.append(f"- [{slug}]({BASE}/recipes/{slug}/)")
    return _page("Recipes", "Curated four-axis compositions.", "\n".join(parts))


def render_template_index(catalog: dict) -> str:
    parts = []
    for e in catalog["by_axis"]["format"]:
        if e.get("canonical_template"):
            parts.append(f"- [{e['name']}]({BASE}/templates/{e['id']}/)")
    return _page("Templates", "Canonical format templates.", "\n".join(parts))


def render_examples_topic_index(catalog: dict, topic: str) -> str:
    parts = [f"Vertical-slice examples for this topic, one per entry. "
             f"Each is also embedded on its entry's reference page.", ""]
    return _page(topic, f"Examples for the {topic} anchor topic.", "\n".join(parts))
```

- [ ] **Step 4: Run to verify pass**

Run: `pytest tests/test_generate_site_pages.py -v`
Expected: all PASS (now 15).

- [ ] **Step 5: Commit**

```bash
git add scripts/generate_site_pages.py tests/test_generate_site_pages.py
git commit -m "feat(site): gallery index-page renderers"
```

---

## Task 8: The write-everything main() and run it

Wire the emitters into a deterministic `main()` that writes the full tree, then run it against the real catalog.

**Files:**
- Modify: `scripts/generate_site_pages.py`

- [ ] **Step 1: Implement main() and the writer**

Add to `scripts/generate_site_pages.py`:

```python
def _write(out_root: Path, rel: str, content: str) -> None:
    path = out_root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def generate(out_root: Path) -> int:
    catalog = load_catalog()
    pairs = load_diff_pairs()
    n = 0

    # Entry pages (.mdx because they import components / use <Tabs>)
    for axis in AXES:
        for entry in catalog["by_axis"][axis]:
            rel = f"reference/{AXIS_DIR[axis]}/{entry['id']}.mdx"
            _write(out_root, rel, render_entry_page(catalog, pairs, entry))
            n += 1
    _write(out_root, "reference/index.md", render_reference_index(catalog))

    # Diff-pair pages (.mdx, import DiffPair)
    for dp in pairs:
        _write(out_root, f"examples/diff-pairs/{dp['diff_pair_id']}.mdx",
               render_diff_pair_page(catalog, dp))
        n += 1
    _write(out_root, "examples/diff-pairs/index.md", render_diff_pair_index(pairs))

    # Example topic index pages
    for topic in TOPICS:
        _write(out_root, f"examples/{topic}/index.md",
               render_examples_topic_index(catalog, topic))

    # Recipes
    for slug in list_recipes():
        _write(out_root, f"recipes/{slug}.md", render_recipe_page(catalog, slug))
        n += 1
    _write(out_root, "recipes/index.md", render_recipe_index(catalog))

    # Templates
    for e in catalog["by_axis"]["format"]:
        if e.get("canonical_template"):
            _write(out_root, f"templates/{e['id']}.md", render_template_page(e))
            n += 1
    _write(out_root, "templates/index.md", render_template_index(catalog))

    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(DOCS), help="output docs root")
    args = ap.parse_args()
    out_root = Path(args.out)
    count = generate(out_root)
    print(f"[OK] generated {count} catalog pages into {out_root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Run the generator against the real catalog**

Run: `python scripts/generate_site_pages.py`
Expected: `[OK] generated 92 catalog pages into .../docs` (60 entries + 12 diff-pairs + 5 recipes + 15 templates = 92), exit 0, no traceback.

- [ ] **Step 3: Spot-check the de-orphaning success criterion**

Run: `grep -c "TabItem" docs/reference/voices/pragmatic-architect.mdx`
Expected: at least 3 (one tab per topic).
Run: `grep -c "ENTRY.md" docs/reference/voices/pragmatic-architect.mdx`
Expected: 0 (no GitHub-relative source links).

- [ ] **Step 4: Verify no em/en-dashes in generated output**

Run: `python tools/validate.py`
Expected: the no-em-dash check PASSES over the new `docs/` pages (the catalog source is already clean, so generated copies are clean). If it fails, a source file has a dash - fix at source, do not edit generated pages.

- [ ] **Step 5: Commit the generator and the generated pages**

```bash
git add scripts/generate_site_pages.py docs/reference docs/examples docs/recipes docs/templates
git commit -m "feat(site): write full catalog page tree from source (92 pages)"
```

---

## Task 9: Freshness guard

CI must fail if committed generated pages drift from source.

**Files:**
- Create: `scripts/check_generated_fresh.py`

- [ ] **Step 1: Write the freshness checker**

Create `scripts/check_generated_fresh.py`:

```python
#!/usr/bin/env python3
"""Fail if committed generated docs pages differ from a fresh generation.

Regenerates into a temp dir and compares file-by-file against the committed
docs/ generated trees. Exit 1 on any difference (stale pages) so CI blocks.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_site_pages as gsp  # noqa: E402

GENERATED_SUBDIRS = ["reference", "examples", "recipes", "templates"]


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_root = Path(tmp)
        gsp.generate(tmp_root)
        stale = []
        committed_root = gsp.DOCS
        # Compare fresh -> committed (every freshly generated file must match)
        for fresh in tmp_root.rglob("*"):
            if not fresh.is_file():
                continue
            rel = fresh.relative_to(tmp_root)
            committed = committed_root / rel
            if not committed.exists():
                stale.append(f"missing committed page: docs/{rel}")
            elif committed.read_text(encoding="utf-8") != fresh.read_text(encoding="utf-8"):
                stale.append(f"stale committed page: docs/{rel}")
    if stale:
        print("[FAIL] generated docs are stale - run: python scripts/generate_site_pages.py")
        for s in stale:
            print("  " + s)
        return 1
    print("[OK] generated docs match source")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Run it on the clean tree (should pass)**

Run: `python scripts/check_generated_fresh.py`
Expected: `[OK] generated docs match source`, exit 0.

- [ ] **Step 3: Prove the guard works (negative test)**

Run:
```bash
printf "\nhand edit\n" >> docs/templates/adr.md
python scripts/check_generated_fresh.py; echo "exit=$?"
git checkout docs/templates/adr.md
```
Expected: `[FAIL] ... stale committed page: docs/templates/adr.md`, `exit=1`. Then the checkout restores it.

- [ ] **Step 4: Commit**

```bash
git add scripts/check_generated_fresh.py
git commit -m "feat(site): freshness guard for generated docs pages"
```

---

## Task 10: Migrate authored pages and home

Move hand-written narrative into the Starlight tree and convert the home page.

**Files:**
- Create: `docs/index.mdx`
- Move: `docs/how-to/*` to `docs/guides/*`
- Delete: `docs/index.md`, stale `.gitkeep` files

- [ ] **Step 1: Convert the home page to index.mdx with frontmatter**

Read `docs/index.md`, then create `docs/index.mdx` with a Starlight splash-or-doc frontmatter at the top followed by the existing body. Minimum frontmatter:

```mdx
---
title: Writing Style Library
description: Composable writing instructions on four orthogonal axes - Voice, Tone, Style, Format.
---

<!-- body migrated from the former docs/index.md -->
```

Paste the prior `docs/index.md` body beneath the frontmatter. Then delete `docs/index.md`.

Run: `git rm docs/index.md` (after creating index.mdx).

- [ ] **Step 2: Move how-to pages to guides/ (IA rename per spec)**

Run:
```bash
git mv docs/how-to docs/guides
```
Then confirm each file under `docs/guides/` has a `title:` in frontmatter (Starlight requires it). If any lacks frontmatter, add:
```
---
title: <Human Title>
---
```
at the top (e.g. `Compose an Instruction`, `Pick a Voice`, `Add an Entry`).

- [ ] **Step 3: Ensure authored concept/design/governance pages have title frontmatter**

For each of `docs/concepts/{three-axis-model,composition,glossary}.md`, `docs/design-standards/{voice-and-tone,naming-conventions,style-tells}.md`, `docs/governance/contribution-process.md`: confirm a `title:` frontmatter exists; add one if missing. (Starlight fails the build on a docs page without a title.)

- [ ] **Step 4: Remove stale .gitkeep files where real pages now exist**

Run:
```bash
git rm -f docs/reference/.gitkeep docs/concepts/.gitkeep docs/design-standards/.gitkeep docs/governance/.gitkeep
```
(Leave any `.gitkeep` in a dir that has no committed page yet.)

- [ ] **Step 5: Commit**

```bash
git add docs/index.mdx docs/guides docs/concepts docs/design-standards docs/governance
git commit -m "feat(site): migrate authored pages into the Starlight tree"
```

---

## Task 11: Build the site locally and fix link/build errors

**Files:**
- Possibly modify: authored pages, `scripts/generate_site_pages.py` (only if a real bug surfaces)

- [ ] **Step 1: Run the full build**

Run: `npm run build`
Expected: the generator runs, then `astro build` completes. Starlight fails the build on broken internal links and missing titles - this step surfaces them.

- [ ] **Step 2: Fix any broken-link or missing-title errors**

For each error Astro reports:
- Missing title on an authored page: add `title:` frontmatter.
- Broken internal link from a generated page: fix the URL computation in the relevant emitter (`entry_url`, the diff-pair/recipe/template link strings), regenerate (`python scripts/generate_site_pages.py`), rebuild. Do NOT hand-edit generated pages.
- Broken link from an authored page: fix the authored markdown link to the correct Starlight slug.

Re-run `npm run build` until it exits 0 with no broken links.

- [ ] **Step 3: Visual spot check**

Run: `npm run preview`
Open the local URL and confirm:
- A voice entry page (e.g. `/reference/voices/pragmatic-architect/`) shows tabbed examples and clickable cross-reference links.
- The diff-pair gallery renders side-by-side.
- A template page has a copy button on the code block.

- [ ] **Step 4: Commit any fixes**

```bash
git add -A
git commit -m "fix(site): resolve build and link errors for clean astro build --strict"
```

---

## Task 12: Replace the deploy workflow and deprecate MkDocs

**Files:**
- Replace: `.github/workflows/build-site.yml`
- Delete: `mkdocs.yml`
- Modify: `tools/build-indexes.py`

- [ ] **Step 1: Stop build-indexes.py from writing docs/reference/index.md**

In `tools/build-indexes.py`, remove the `build_reference_index(entries)` call from `main()` (keep `build_taxonomy_json`). Leave the function defined but uncalled, or delete it; the generated Starlight `reference/index.md` replaces it. Verify:

Run: `python tools/build-indexes.py`
Expected: writes `taxonomy.json`, does NOT recreate `docs/reference/index.md`.

- [ ] **Step 2: Delete mkdocs.yml**

Run: `git rm mkdocs.yml`

- [ ] **Step 3: Replace the site workflow with Astro build + Pages deploy**

Overwrite `.github/workflows/build-site.yml`:

```yaml
name: Build and Deploy Site

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install -r requirements-dev.txt
      - name: Validate catalog
        run: python tools/validate.py
      - name: Check generated docs are fresh
        run: python scripts/check_generated_fresh.py
      - uses: actions/setup-node@v4
        with: { node-version: "22.12.0" }
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-pages-artifact@v3
        with: { path: ./dist }

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/build-site.yml tools/build-indexes.py
git rm mkdocs.yml
git commit -m "feat(site): Astro build+deploy workflow; deprecate MkDocs"
```

- [ ] **Step 5: Enable GitHub Pages (manual, one-time)**

In the GitHub repo settings -> Pages, set Source = "GitHub Actions". (This cannot be done from the plan; note it for the maintainer.) After the next push to `main`, confirm the workflow's deploy job succeeds and the site is live at `https://product-on-purpose.github.io/writing-style-library`.

---

## Task 13: Content-fidelity lint and final verification

**Files:**
- Modify: `tools/validate.py` (add a content-fidelity check) OR `scripts/generate_site_pages.py`
- Modify: `tests/test_generate_site_pages.py`

- [ ] **Step 1: Write a failing test for the fidelity lint**

Append to `tests/test_generate_site_pages.py`:

```python
def test_fidelity_lint_flags_orphan_period():
    bad = "This sentence ends oddly . Then continues."
    hits = gsp.fidelity_warnings(bad)
    assert any("orphan" in h.lower() or "space before period" in h.lower() for h in hits)


def test_fidelity_lint_clean_text_no_warnings():
    assert gsp.fidelity_warnings("A normal clean sentence. Another one.") == []
```

- [ ] **Step 2: Run to verify failure**

Run: `pytest tests/test_generate_site_pages.py -v`
Expected: FAIL with `AttributeError` on `fidelity_warnings`.

- [ ] **Step 3: Implement fidelity_warnings**

Add to `scripts/generate_site_pages.py`:

```python
# Source-prose defect patterns that would render verbatim on the live site.
_FIDELITY_PATTERNS = [
    (re.compile(r"\s\."), "space before period (orphan period, e.g. stray em-dash sweep)"),
    (re.compile(r"\.\.(?!\.)"), "doubled period"),
    (re.compile(r",,"), "doubled comma"),
    (re.compile(r"\bTODO\b|\bTKTK\b"), "unfinished marker"),
]


def fidelity_warnings(text: str) -> list[str]:
    hits = []
    for rx, msg in _FIDELITY_PATTERNS:
        if rx.search(text):
            hits.append(msg)
    return hits
```

- [ ] **Step 4: Run to verify pass**

Run: `pytest tests/test_generate_site_pages.py -v`
Expected: all PASS (now 17).

- [ ] **Step 5: Run the fidelity lint across the real catalog (report-only)**

Add a small `--lint` path to `main()` in `scripts/generate_site_pages.py`: when `--lint` is passed, iterate every entry body and every example body through `fidelity_warnings` and print `path: warning` lines; exit 0 (advisory) so it does not block, matching the spec's "fix at source" intent.

```python
    ap.add_argument("--lint", action="store_true", help="report source-prose fidelity warnings and exit")
    # ... after parsing:
    if args.lint:
        cat = load_catalog()
        total = 0
        for axis in AXES:
            for e in cat["by_axis"][axis]:
                for w in fidelity_warnings(e.get("_body", "")):
                    print(f"taxonomy/{AXIS_DIR[axis]}/{e['id']}/ENTRY.md: {w}")
                    total += 1
        print(f"[lint] {total} fidelity warning(s)")
        return 0
```

Run: `python scripts/generate_site_pages.py --lint`
Expected: prints any warnings and a count, exit 0. Fix any flagged source files (in `taxonomy/` or `examples/`), then regenerate.

- [ ] **Step 6: Full verification sweep**

Run each and confirm:
```bash
pytest tests/test_generate_site_pages.py -v   # all pass
python tools/validate.py                       # all checks pass
python scripts/generate_site_pages.py          # 92 pages
python scripts/check_generated_fresh.py        # OK
npm run build                                  # astro build clean, no broken links
```

- [ ] **Step 7: Commit**

```bash
git add scripts/generate_site_pages.py tests/test_generate_site_pages.py
git commit -m "feat(site): content-fidelity lint for source prose"
```

---

## Task 14: Update root docs and pre-commit wiring

**Files:**
- Modify: `.pre-commit-config.yaml`, `README.md`, `CHANGELOG.md`, `AGENTS.md`/`CLAUDE.md` (key-commands section)

- [ ] **Step 1: Add the freshness guard to pre-commit (optional but recommended)**

In `.pre-commit-config.yaml`, add a local hook that runs the freshness check so a commit with stale generated pages is caught before CI:

```yaml
  - repo: local
    hooks:
      - id: generated-docs-fresh
        name: generated docs fresh
        entry: python scripts/check_generated_fresh.py
        language: system
        pass_filenames: false
```

- [ ] **Step 2: Update README project-structure and remove MkDocs mentions**

In `README.md`: change any "MkDocs" reference to the Astro Starlight site; update the project-structure table row for `docs/` to note the generated vs authored split; mention the site URL (`product-on-purpose.github.io/writing-style-library`). Keep the existing experimental warning callout.

- [ ] **Step 3: Update the key-commands docs**

In `CLAUDE.md` (and `AGENTS.md` if it lists commands), add the site commands next to the existing validate/build commands:
```
# Generate the docs site pages from the catalog
python scripts/generate_site_pages.py
# Build the site
npm run build
```
and remove the `mkdocs build` reference.

- [ ] **Step 4: Add a CHANGELOG entry under [Unreleased]**

In `CHANGELOG.md`, under `## [Unreleased]`, add:
```
### Changed
- Documentation site migrated from MkDocs Material to Astro Starlight. Catalog pages (entries, examples, diff-pairs, recipes, templates) are generated from taxonomy/ and examples/ by scripts/generate_site_pages.py; every entry page now embeds its examples and cross-reference links. Site deploys to GitHub Pages.
```

- [ ] **Step 5: Commit**

```bash
git add .pre-commit-config.yaml README.md CHANGELOG.md CLAUDE.md AGENTS.md
git commit -m "docs: update root docs and pre-commit for the Starlight site"
```

- [ ] **Step 6: Final push**

```bash
git push origin main
```
Then confirm the GitHub Actions run is green and (after Task 12 Step 5's Pages setting) the site is live.

---

## Self-review notes

- **Spec coverage:** Section 4 layout -> Task 1. Generator + PyYAML -> Tasks 2-8. In-generator slug links (5.5) -> Task 3 + tested in Task 5 (`ENTRY.md not in md`). Entry page with embedded examples + xrefs (5.1) -> Task 5. Diff-pair/recipe/template (5.2-5.4) -> Task 6. IA/sidebar (6) -> Task 1 astro.config + Task 10 migration. Deploy (7) -> Task 12. MkDocs removal (8) -> Task 12. Testing/freshness (9) -> Tasks 9, 11, 13. Content-fidelity lint -> Task 13. ADR 0011 already committed.
- **Committed-generated decision (4.3):** generated pages are committed (Task 8 Step 5) and guarded (Task 9); `.astro/` is gitignored (Task 1) but generated `docs/` subtrees are not.
- **Known follow-ups not in this plan (out of scope, fine to defer):** filtering islands on galleries; richer home splash; Mermaid diagrams in concept pages; converting the example topic index into a full per-topic gallery (currently a stub index page since examples are embedded on entry pages, which satisfies the de-orphaning goal).
- **Page count check:** 60 entry + 12 diff-pair + 5 recipe + 15 template = 92 generated content pages, plus index pages.
- **No placeholders:** every code step shows complete code; every run step shows the exact command and expected result.
