# Astro Starlight Documentation Site - Design Spec

- **Date:** 2026-05-31
- **Status:** draft - awaiting maintainer review
- **Author:** Claude Opus 4.8 (brainstorming) with jprisant
- **Supersedes:** the MkDocs Material site (`mkdocs.yml`, `.github/workflows/build-site.yml`), which this design fully deprecates

## 1. Goal

Replace the MkDocs Material documentation stack with an Astro Starlight site that turns the catalog into "an incredibly rich and thoughtful library of all the examples, types, and templates." The site's job is to make the catalog's most valuable and currently-invisible assets - 60 entries, 195 worked examples, 12 diff-pairs, 5 recipes, and 15 format templates - browsable, cross-linked, and teachable. Today only 1 of 60 entries links to its examples and the reference page is a flat four-column table; the examples are effectively orphaned. This site fixes that.

A secondary goal is family consistency: the sibling repo `pm-skills` runs Astro 6.3 + Starlight 0.39 with Python generators feeding a `docs/` content tree. This design mirrors that pattern so the two repos share conventions and tooling shape.

## 2. Scope

**In scope:**
- Astro Starlight site at the repo root (Astro `^6.3`, `@astrojs/starlight ~0.39`, `astro-mermaid`, `sharp`).
- A Python generator that renders catalog pages from `taxonomy/` and `examples/` into the `docs/` content tree (Option 1: generate the catalog, hand-author the narrative).
- Hand-authored narrative pages (concepts, guides, design standards, governance) in MDX/Markdown.
- A freshness/untouched CI guard so generated pages cannot silently drift from source or be hand-edited.
- A GitHub Actions workflow that builds the site and deploys it live to GitHub Pages (the repo is public).
- Full removal of the MkDocs stack.

**Out of scope (named so they are not assumed):**
- The Composer web app, MCP server, and SDKs (separate future efforts).
- Conflict-aware composition in the skill (a separate, already-identified piece of work).
- Any catalog content expansion (no new entries/examples); this is a presentation-layer project.
- The public `agent-plugins` marketplace listing (deferred by maintainer decision until plugin value is proven).
- Custom domain; the site lives at the GitHub Pages project URL.

## 3. Approach decision

Three approaches were considered:

- **A - Mirror pm-skills (chosen).** Starlight at repo root; `docs/` is the Starlight content directory read in place; a Python generator writes catalog pages into `docs/`; narrative pages hand-authored. Lowest risk, family-consistent, reuses this repo's existing Python frontmatter tooling.
- **B - Astro Content Layer loaders.** Typed collections loaded directly from `taxonomy/`/`examples/`, rendered by Astro components, no intermediate markdown. More native and component-rich but diverges from pm-skills and is more upfront Astro work. *Rejected as the primary architecture; one idea borrowed - a small component for the diff-pair side-by-side.*
- **C - Astro in a `site/` subdir.** Isolates the Node toolchain but breaks family consistency and complicates generator paths. *Rejected.*

**Chosen: A.** The generator is Python (mirroring pm-skills' `generate-skill-pages.py` and this repo's `validate.py`/`build-indexes.py`), not Node, so it reuses the existing `_extract_frontmatter` machinery and keeps the content pipeline in one language. Note: the existing hand-rolled YAML parser silently drops nested mappings (a known defect from the audit); the generator MUST use a real YAML parser (PyYAML) so it can read fields like the format `typical_length` object and `canonical_template` block scalars correctly.

## 4. Architecture

### 4.1 Repository layout (additions at root, mirroring pm-skills)

```
astro.config.mjs           # Starlight config: site, base, integrations, sidebar, redirects
package.json               # name "writing-style-library-docs", private, type module, Node >=22.12
src/
  content.config.ts        # Starlight content collection, loader points in place at docs/
  styles/custom.css        # minimal brand CSS
  components/
    DiffPair.astro         # side-by-side A/B renderer for diff-pair pages
scripts/
  generate-site-pages.py   # THE generator: taxonomy/ + examples/ -> docs/ catalog pages
  check-generated-fresh.py # CI guard: regenerate to a temp dir, fail if it differs from a fresh run
docs/                      # Starlight content root (mix of generated + authored)
```

### 4.2 The `docs/` content tree

Generated subtrees (written by `generate-site-pages.py`, gitignored as build artifacts, never hand-edited):
- `docs/reference/voices|tones|styles|formats/<id>.md` - one page per entry (60 pages)
- `docs/examples/<topic-slug>/` - vertical-slice galleries per anchor topic
- `docs/examples/diff-pairs/` - the diff-pair gallery
- `docs/recipes/<recipe>.md` - horizontal-slice recipe pages
- `docs/templates/<format-id>.md` - the `canonical_template` gallery

Authored subtrees (committed, hand-written, never touched by the generator):
- `docs/index.mdx` - home
- `docs/concepts/` - three-axis-model, composition, glossary
- `docs/guides/` - compose-an-instruction, pick-a-voice, add-an-entry
- `docs/design-standards/` - voice-and-tone, naming-conventions, style-tells
- `docs/governance/` - contribution-process
- `docs/internal/` - excluded from the build (as today)

To keep the boundary unambiguous, the generator owns whole directories (`reference/`, `examples/`, `recipes/`, `templates/`); authored content lives in different directories. No directory mixes generated and authored files.

### 4.3 Generated/authored boundary enforcement

The generated catalog pages are **committed** to the repo (not gitignored), mirroring pm-skills, whose `docs/skills/` pages are tracked. This is the coherent choice: it makes the git-diff freshness guard meaningful, lets a fresh clone run `astro dev` and see the full site, and makes the catalog browsable on GitHub. The trade-off accepted is a larger diff when entries change; that is acceptable because catalog edits are infrequent and the diff is reviewable evidence of what the change produced.

- The generator runs at `prebuild` (`npm run build` runs `python scripts/generate-site-pages.py` then `astro build`) and committed, and the maintainer also runs it after any `taxonomy/` or `examples/` edit and commits the regenerated pages alongside the source edit - the same discipline the repo already uses for `taxonomy.json` via `build-indexes.py`.
- `scripts/check-generated-fresh.py` (run in CI) regenerates the pages and runs `git diff --exit-code` over the generated directories; a non-empty diff fails CI, proving the committed pages match the current source + generator. This mirrors both pm-skills' freshness guard and this repo's existing `taxonomy.json` staleness check in `validate.yml`.
- The boundary stays unambiguous because the generator owns whole directories (`reference/`, `examples/`, `recipes/`, `templates/`) that contain no authored files; authored narrative lives only in the other directories (`concepts/`, `guides/`, `design-standards/`, `governance/`, `index.mdx`). A header comment in each generated file marks it as generated and not to be hand-edited.

## 5. Generated page templates (the core of "rich and thoughtful")

### 5.1 Entry page (`docs/reference/<axis>/<id>.md`)
Source: `taxonomy/<axis>/<id>/ENTRY.md` frontmatter + body, plus a reverse-lookup over `examples/` and `examples/diff-pairs/`.

Renders, in order:
- Title + one-liner + tags.
- Description (the prose body).
- Language patterns (list).
- When to use / When not to use.
- **Cross-references as live links**: `pairs_well_with`, `avoid_with`, `confusable_with` each rendered as links to the neighbor entry pages, with the "Often confused with" distinction prose where present. This makes the cross-reference graph navigable, which the audit flagged as the catalog's latent moat.
- **The `llm_instruction_phrasing`** in a fenced code block with Starlight's copy button.
- For formats: the `canonical_template` (and a link to its template-gallery page).
- For voices: the optional `diction` / `sentence_style` / `default_pov` / `typical_tones` where present (inconsistently populated today - render only when present).
- **Embedded Examples section**: every vertical-slice example whose `entry_id` matches this entry, tabbed by anchor topic (async-standups / morning-routine / service-database-choice). This is the change that de-orphans the 195 examples - each example appears on the page of the entry it demonstrates.
- **Appears in diff-pairs**: links to any diff-pair where this entry is `entry_a` or `entry_b`.

### 5.2 Diff-pair page + gallery
Source: `examples/diff-pairs/<topic>/*.md` (frontmatter: `entry_a`, `entry_b`, `axis_varied`, `topic_label`; body: "what to notice" + the A and B passages).
- A gallery index grouped by `axis_varied`.
- Each pair rendered via the `DiffPair.astro` component: the two passages side by side, the axis-varied label, links to both entry pages, and the "what to notice" prose. (Honest-labeling note: the existing diff-pairs assert other axes are held constant but the generator concatenated them independently; the page will describe the varied axis without overclaiming strict constancy.)

### 5.3 Recipe page
Source: `examples/horizontal-slices/<recipe>/README.md` + the worked-output files in that folder.
- The four-axis composition table (axis / entry / why), with entry names linked to their reference pages.
- When-to-use / when-to-use-something-else prose.
- The worked outputs rendered or linked.

### 5.4 Template gallery
Source: the `canonical_template` field on all 15 format entries.
- One page per format template plus an index, each in a copy-buttoned code block, linked back to the format's reference page.

## 6. Information architecture (Starlight sidebar)

Manual top-level order, autogenerate within sections (Starlight 0.39 `items: [{ autogenerate: { directory } }]` form):

1. **Home** (`index.mdx`)
2. **Concepts** - three-axis model, composition, glossary *(authored)*
3. **Guides** - compose an instruction, pick a voice, add an entry *(authored)*
4. **Reference** - Voices, Tones, Styles, Formats *(generated; one page per entry)*
5. **Examples** - vertical-slice galleries by topic; diff-pair gallery *(generated)*
6. **Recipes** *(generated)*
7. **Templates** *(generated)*
8. **Design Standards** - voice-and-tone, naming, style-tells *(authored)*
9. **Contributing** *(authored)*

## 7. Deployment

- New `.github/workflows/build-site.yml` (replacing the MkDocs one): on push to `main`, set up Node >=22.12, `npm ci`, `npm run build` (which runs the Python generator then `astro build --strict`), then deploy.
- Deploy uses the official GitHub Pages Actions (`actions/upload-pages-artifact` + `actions/deploy-pages`) targeting a `github-pages` environment.
- Live target: `https://product-on-purpose.github.io/writing-style-library` (so `astro.config.mjs` sets `site: 'https://product-on-purpose.github.io'`, `base: '/writing-style-library'`). The repo is public, so this deploys live on merge to `main`.
- GitHub Pages must be set to "GitHub Actions" as the source in repo settings (a one-time manual step, noted in the implementation plan).
- The CI build also runs the existing `python tools/validate.py` so a content error fails the site build too.

## 8. MkDocs deprecation (complete removal)

- Delete `mkdocs.yml`.
- Replace `.github/workflows/build-site.yml` (MkDocs) with the Astro workflow above.
- Remove MkDocs deps from `requirements-dev.txt` (`mkdocs`, `mkdocs-material`, `pymdown-extensions`), keeping `jsonschema` and `pre-commit`.
- Retire `build-indexes.py`'s `docs/reference/index.md` output (the generated Starlight reference replaces it). Keep its `taxonomy.json` generation (the build artifact the plugin/skill ecosystem uses). Update its CI staleness check accordingly.
- Port the MkDocs nav intent into the Starlight sidebar (Section 6). No content is lost; authored pages move from `docs/<x>.md` into the same paths under the Starlight tree.
- Add Starlight redirects for any MkDocs URL that external links may already point at (low risk - the MkDocs site was never deployed, so there are no live inbound links; redirects are belt-and-suspenders only and may be skipped).
- `.gitignore` additions: `.astro/` (Astro's cache) and confirm `node_modules/` and `dist/` (already covered). The generated `docs/` subtrees are committed, not ignored (see 4.3).

## 9. Testing and verification

- `python scripts/generate-site-pages.py` produces all expected pages (60 entry pages, example galleries for 3 topics, 12 diff-pair pages, 5 recipe pages, 15 template pages) with zero crashes on the real catalog.
- `python tools/validate.py` still passes (unchanged).
- `npm run build` completes `astro build --strict` with zero broken internal links (Starlight fails strict build on broken links).
- `scripts/check-generated-fresh.py` passes on a clean tree and fails when a generated page is hand-edited (proves the guard works).
- Local `npm run preview` renders: an entry page shows its embedded examples and live cross-reference links; the diff-pair gallery renders side-by-side; the template gallery copy buttons work.
- Spot-check: the `pragmatic-architect` entry page embeds its vertical slices across all three topics and links to the diff-pairs it appears in (the de-orphaning success criterion).

## 10. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Node toolchain in a Python repo adds maintenance surface | Mirror pm-skills exactly (same versions, same shape); pin versions; keep the generator in Python so only the site shell is Node |
| Generator drift / stale committed pages | `check-generated-fresh.py` runs the generator and `git diff --exit-code` in CI; a stale page fails the build (same pattern as the existing taxonomy.json staleness check) |
| Hand-rolled YAML parser drops nested fields (canonical_template, typical_length) | Generator uses PyYAML, not the repo's `_parse_simple_yaml` |
| Diff-pair "held constant" overclaim leaks into the site | Page copy describes the varied axis only; does not assert strict constancy of other axes |
| Starlight 0.39 sidebar breaking-change (autogenerate shorthand removed) | Use the `items: [{ autogenerate }]` form from the start (learned from pm-skills) |
| Deploying a broken/empty site publicly | Build runs validate.py + strict astro build; deploy only on green `main`; site only goes live once the generated content renders |

## 11. Success criteria

The project is done when:
- The MkDocs stack is fully removed and the Astro Starlight site builds with `astro build --strict`, zero broken links.
- Every one of the 60 entries has a generated reference page that embeds its examples and renders its cross-references as working links.
- The diff-pair gallery, recipe pages, and template gallery all render from source.
- The generated/authored boundary is enforced by a passing freshness check in CI.
- The site deploys live to `product-on-purpose.github.io/writing-style-library` on merge to `main`.
- `tools/validate.py` and the `taxonomy.json` build artifact are unaffected.
