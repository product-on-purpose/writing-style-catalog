# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
