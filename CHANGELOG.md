# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.0] - 2026-07-02

Wave 2 completes the Stream-B promotion program. The 23 remaining professional and public format candidates - marketing copy, correspondence-at-work, opinion pieces, and the rest of professional communication - are promoted into the stable catalog, each rendered across all 12 anchor topics and date-gated against the real calendar. Format axis growth: 29 to 52 stable. Only the Hold-20 (personal, ceremonial, contemplative - deliberately off the current PM/builder beachhead) remain as drafts, staged for a future audience-expansion release. Rolls up everything merged since v0.4.0.

### Added

- **10 more stable format entries (Wave 2A)**, taking the Format axis from 29 to 39 and the catalog from 74 to 84 curated entries: `user-manual`, `resume`, `bio`, `performance-review`, `memo`, `cold-outreach`, `cover-letter`, `recommendation-letter`, `support-reply`, and `review-response`. These are the rest of the professional formats (correspondence-at-work, appraisal, and response), promoted from the Stream-B breadth drafts. Each was rendered across all 12 anchor topics and date-gated against the real calendar, adding 120 worked examples (888 to 1008 vertical-slice samples).
- **13 more stable format entries (Wave 2B)**, taking the Format axis from 39 to 52 and the catalog from 84 to 97 curated entries: `press-release`, `newsletter`, `listicle`, `customer-story`, `landing-page`, `ad-copy`, `product-description`, `testimonial`, `op-ed`, `editorial`, `manifesto`, `open-letter`, and `public-statement`. These are the rest of the public formats (marketing, opinion, and outward-facing copy), completing Wave 2. Each was rendered across all 12 anchor topics and date-gated against the real calendar, adding 156 worked examples (1008 to 1164 vertical-slice samples). The library now ships 97 curated entries and 1193 worked examples. This closes Stream-B Wave 1 + Wave 2: 57 draft candidates down to 20, all off the PM/builder beachhead and held for a future audience-expansion release.

### Fixed

- **Six date and internal-consistency slips**, surfaced by a per-format date gate against the real calendar (one checker per dated format across Wave 2A and Wave 2B): a `memo` and several other samples were checked clean; two `retirement-send-off` samples independently mislabeled a Saturday as a Friday; a `team-milestone-celebration` newsletter's stated start date contradicted its own fourteen-month span; an onboarding `listicle` miscounted a 32-day gap as six weeks; and a `customer-story` headline contradicted its own body on how long a manual process took.
- **Three fabricated internal links** in an onboarding-a-new-hire `newsletter` sample, caught by the PR-time rendered-link checker: `../`-prefixed links pointed at a fictional team's documentation with no corresponding site page. Corrected to the bare-relative convention already used elsewhere in the same file for illustrative, non-navigational example links.

## [0.4.0] - 2026-06-27

The Format axis nearly doubles. A gated Stream-B breadth program produced 57 new format candidates; the strongest 14 - the documents PMs and builders reach for most - are promoted into the stable catalog this release, each rendered across all 12 anchor topics. A whole-corpus de-duplication audit hardened the catalog, and the docs site now marks draft candidates. Rolls up everything merged since v0.3.0.

### Added

- **14 new stable format entries**, taking the Format axis from 15 to 29 and the catalog from 60 to 74 curated entries: `design-doc`, `rfc`, `postmortem`, `retrospective`, `incident-report`, `runbook`, `how-to-guide`, `faq`, `meeting-agenda`, `proposal`, `project-brief`, `pitch-deck`, `announcement`, and `release-notes`. Each was produced by the gated Stream-B breadth program - a per-entry cross-vendor distinguishability gate plus a whole-corpus de-duplication audit - and then rendered across all 12 anchor topics, adding 168 worked examples (720 to 888 vertical-slice samples). The library now ships 74 curated entries and 917 worked examples.
- **43 further format candidates under review** (`review_status: draft`), spanning all five domains (professional, public, personal, ceremonial, contemplative) so every format family now has at least two members and the previously-empty `response` and `copy` families are filled. Each carries the full pedagogical bar (tells, anti_patterns, failure_modes). The inventory and the draft-to-stable promotion proposal live under `docs/internal/release-plans/`.
- **Draft marking on the docs site** (`scripts/gen-site.mjs`): generated reference and template pages render a "Draft - under review" callout for any entry whose `review_status` is `draft`, so the live site distinguishes the candidates from the stable catalog.

### Fixed

- **Stale "Often confused with" sections on baseline entries**, surfaced by a whole-corpus de-duplication audit (all 72 formats reviewed by family cluster, not just against each entry's one declared neighbor). Three stable entries had a body disambiguation that contradicted their own `confusable_with` frontmatter: `blog-post-long-form` now contrasts `whitepaper` instead of adr/prd, `slack-message` now contrasts `email` instead of prd/adr, and `devotional-entry` now contrasts `sermon`. `technical-reference` had its `confusable_with` reconciled with the neighbors its body actually discusses. The audit also sharpened `op-ed` vs `editorial` so their output diverges on substance rather than byline, and added five missing reciprocal `confusable_with` links.

## [0.3.0] - 2026-06-25

A personal `style-profile` skill, a first batch of agentic recipes, a pedagogical bar on every entry (each one now teaches its own tells and failure modes), the v2 taxonomy with domain and family facets, and the deterministic substrate of the adherence gate that will govern the catalog's gated expansion. Rolls up everything merged since v0.2.0.

### Added

- **`style-profile` skill** - guides a user to a personal writing-style profile: a saved selection across the Voice, Tone, Style, and Format axes, confirmed with a generated A/B-tested sample and saved to gitignored local user state. Four intake modes (infer from your writing via paste or file globs, recognize from examples, interview, or fill a template). It is selection-only: it composes existing catalog entries via the writing-instruction-builder and never authors new style text. Invoke with `/writing-style-catalog:style-profile`.
- **Five new recipes** under `examples/horizontal-slices/`: `product-candid-prd`, `consultant-diplomatic-one-pager`, `techwriter-plain-readme`, `researcher-confident-whitepaper`, and `storyteller-celebratory-announcement`. Each is a coherent multi-axis stack with two worked outputs, bringing the recipe count from 5 to 10.
- **A pedagogical bar on every entry** (ADR 0009): all 60 entries now carry `tells` (spottable markers), `anti_patterns`, and `failure_modes` (the caricature the register tips into when overdone). These render on each entry's reference page and are required by the schema, so every entry now teaches its distinction rather than only steering toward it.
- **Adherence-gate tooling** (`tools/adherence_gate.py`, `tools/anchor_topics.py`, `tools/gate_pilot.py`): a deterministic neighbor lookup, a two-tier anchor-topic pool, and a blind cross-vendor judge pilot harness - the quality machinery that gates the catalog's expansion. Developer-facing; not part of the runtime skill path.
- **Conflict-aware composition** in the writing-instruction builder (see ADR 0016). The builder now reads each selected entry's `avoid_with` and `pairs_well_with` relationships instead of blindly concatenating phrasings: it warns (without blocking) when a selected pair is marked `avoid_with`, using a symmetric rule so the warning never depends on which entry recorded the link; it confirms good pairings; and it assembles the instruction in a deterministic voice -> tone -> style -> format precedence. Warnings and notes print to stderr so stdout stays a clean, pipeable prompt. The skill's `metadata.version` is bumped to 0.2.0.
- Canonical `library.json` at the repository root, the plugin manifest required by the family Standard (`agent-skills-toolkit/STANDARD.md` Section 5). It pins `standard: "0.11"`, declares `tier: "universal"`, and indexes the single skill component. This moves the repo from "loose components" to a conformant universal-tier (Bronze) plugin and is the source of truth `.claude-plugin/plugin.json` is kept consistent with. The release ZIP now ships `library.json` at the archive root.
- The skill frontmatter now carries `metadata.version: 0.2.0` (Standard 3.7: every component carries a `version` at every tier).

### Changed

- **The v2 taxonomy facets** (ADR 0010): every entry now carries a `domain` and a `family`, both required and shown on its reference page. The `relational` domain is renamed `personal`, and the Voice axis is organized into five families (the former `pastoral` voice becomes a member of the `care` family). These facets make the catalog's neighbor structure explicit and drive the adherence gate's neighbor selection.
- **Two style ids are renamed** to keep document-type vocabulary off the Style axis (taxonomy decision A1, register item Q9): `how-to-tutorial` becomes `procedural` and `frequently-asked-questions` becomes `question-and-answer`. User-facing: select `--style procedural` or `--style question-and-answer`. The rename avoids a name collision with the planned `tutorial` / `how-to-guide` / `faq` instruction formats. The corresponding reference URLs change (`/reference/styles/procedural/`, `/reference/styles/question-and-answer/`); no redirect is provided for the old paths, since the catalog is pre-1.0 and the rename ships within the v0.3.0 taxonomy work.
- **The skill slug is renamed from `compose-instruction` to `writing-instruction-builder`** (see ADR 0015), completing the rename its directory already carried and satisfying the Standard's name == directory rule. User-facing: the invocation is now `/writing-style-catalog:writing-instruction-builder ...`. All current install and usage surfaces (README, QUICKSTART, docs site, release notes) are updated; historical documents keep the old name as a point-in-time record.
- The plugin description in `plugin.json` is canonicalized to the `library.json` wording (one shared string, per the manifest consistency rule). The registry listing in `product-on-purpose/agent-plugins` picks the new string up at its next re-pin.
- `scripts/validate-plugin-manifest.mjs` now validates `library.json` (required fields, SemVer, component entries against disk), asserts `plugin.json` agrees with it (name/version/description), enforces skill name == directory plus `metadata.version`, and fails if an embedded self-listing marketplace reappears.

### Removed

- The embedded self-listing marketplace (`.claude-plugin/marketplace.json`), the family Standard's Section 12 anti-pattern (packet decision D4). The plugin is listed solely in the external Product on Purpose registry: install with `/plugin marketplace add product-on-purpose/agent-plugins` then `/plugin install writing-style-catalog@product-on-purpose`. The direct-from-repo fallback install path is retired with it; the Claude.ai / Claude Desktop ZIP path remains.

## [0.2.0] - 2026-06-02

First release under the `writing-style-catalog` name. Headline: the plugin is now genuinely installable through the Product on Purpose marketplace, and every install surface reflects it. Rolls up the rename and the Astro Starlight migration merged since v0.1.0.

### Added

- Marketplace listing: `writing-style-catalog` is listed in the Product on Purpose marketplace (`product-on-purpose/agent-plugins`), installable with `/plugin marketplace add product-on-purpose/agent-plugins` then `/plugin install writing-style-catalog@product-on-purpose`. The self-hosted single-plugin marketplace and a direct-from-repo path remain as fallbacks.
- Standardized plugin CI: a zero-dependency plugin-manifest validator (`scripts/validate-plugin-manifest.mjs`) wired into the required `validate` job and a dedicated `validate-plugin` workflow; a tag-driven `release` workflow that builds the plugin ZIP and publishes the GitHub Release; a `release-zips` rebuild helper; and CodeQL for JavaScript and Python.
- A reproducible release artifact (`scripts/build-release.sh` / `scripts/build-release.ps1`) that bundles the plugin manifest, the `compose-instruction` skill, and the `taxonomy/` catalog the skill reads at runtime, for the Claude.ai / Claude Desktop upload path.
- An installation guide on the docs site (`guides/install`) and a root `QUICKSTART.md`.
- Build-aware link and route integrity checks for the docs site (family astro-sites standard, clause 14.11): a rendered-link checker with `#anchor` enforcement and a route-parity guard against a committed route manifest, run in both the PR build and the deploy build. A CI em/en-dash check (`scripts/check-no-dashes.mjs`) now enforces the no-dash house rule in CI, not just the pre-commit hook.

### Changed

- Documentation site migrated from MkDocs Material to Astro Starlight (Pattern S): the Astro app lives in `site/`, and catalog pages (entries, examples, diff-pairs, recipes, templates) are generated from `taxonomy/` and `examples/` by a zero-dependency Node generator and rendered by the stock Starlight `docsLoader()`. Every entry page embeds its examples and cross-reference links. The validator's YAML parsing moved to PyYAML (see ADR 0012). The site deploys to GitHub Pages (see ADR 0011).
- Repository renamed from `writing-style-library` to `writing-style-catalog` (see ADR 0014). The slug, GitHub Pages base path, package/plugin/marketplace identifiers, and the `compose-instruction` skill namespace change accordingly; the display title "Writing Style Library" is retained. The old GitHub URL auto-redirects; the published install path becomes `writing-style-catalog@product-on-purpose`.
- Plugin manifest descriptions de-versioned to a single canonical string shared by `plugin.json`, the self-hosted marketplace, and the registry listing, so they no longer drift each release.
- The self-hosted `marketplace.json` source now pins the released tag (`ref: v0.2.0`) instead of tracking `main`, so the direct fallback matches its declared version.
- Mermaid diagrams in the docs site branded to the family accent (`#5C7CFA`).

### Fixed

- A divergent, likely non-working install command (`claude plugin install ...`) on the `compose-instruction` docs page, replaced with the canonical marketplace flow.
- 16 broken internal links on the documentation site. Hand-authored cross-page links used file-relative `.md` paths that 404'd on the live site (Starlight serves extensionless directory URLs one level deeper than the source file); rewritten to relative-slug URLs. The new 14.11 rendered-link guard prevents regressions.

## [0.1.0] - 2026-05-31

First catalog release, distributed through the Product on Purpose marketplace (`product-on-purpose/agent-plugins`).

### Added

- Three-axis composable model (Voice and Tone, Style, Format) with four catalog directories under `taxonomy/`
- 60 taxonomy entries, 15 per axis, each with frontmatter, language patterns, cross-references (`pairs_well_with`, `avoid_with`, `confusable_with`), `when_to_use` / `when_not_to_use`, and an `llm_instruction_phrasing` block
- `compose-instruction` skill (`skills/writing-instruction-builder/`) that assembles a prompt prefix from selected axis entries
- 195 worked examples across three anchor topics (async-standups, morning-routine, service-database-choice), 12 diff-pairs, and 5 horizontal-slice recipes
- JSON Schemas for all entry types and a 9-check validation suite (`tools/validate.py`) plus an index builder (`tools/build-indexes.py`), both wired into CI
- Dual license: Apache-2.0 for code, CC-BY-4.0 for content (see `NOTICE`)
- Repository scaffold, root documentation, contribution guide, and eight Architecture Decision Records

### Notes

- Distributed via the Product on Purpose marketplace registry and a self-hosted single-plugin marketplace in `.claude-plugin/marketplace.json`
- This is an early catalog release; see `ROADMAP.md` for what is planned next
