# Repository map

This document explains what every top-level folder in the Writing Style Library is for, so a newcomer can find their way without reverse-engineering the build. It is the overview that sits above the per-folder READMEs.

## How to read this repo in one sentence

The catalog source lives in `taxonomy/` and `examples/`; the tools in `tools/` validate it; the scripts in `scripts/` publish it into `docs/`; and Astro builds `docs/` into the live site.

```
taxonomy/ + examples/        source of truth, hand-authored
        |
   tools/validate.py         integrity gate (7 checks)
   tools/build-indexes.py -> taxonomy.json    machine-readable index
        |
   scripts/generate_site_pages.py -> docs/    generated catalog pages
   scripts/check_generated_fresh.py           guard: committed docs must match source
        |
   astro build (src/, public/, astro.config.mjs) -> the live site
```

## Folders at a glance

| Folder | Role | Kind | Audience |
|---|---|---|---|
| `taxonomy/` | The catalog. 60 `ENTRY.md` files across `voices/`, `tones/`, `styles/`, `formats/` (15 each). | Source of truth | Catalog author |
| `examples/` | Worked output examples: `vertical-slices/`, `horizontal-slices/`, `diff-pairs/`. | Source of truth | Catalog author |
| `schemas/` | JSON Schema for each entry and example type (7 files). The catalog's data contract. | Source of truth | Developer |
| `tools/` | Catalog integrity, source-side: `validate.py`, `build-indexes.py`, `diff-pair-generator.py`, `taxonomy.py`. | Build (validate) | Build / developer |
| `scripts/` | Documentation generation, output-side: `generate_site_pages.py`, `check_generated_fresh.py`. | Build (publish) | Build / developer |
| `tests/` | Pytest suite for the site generator. | Build | Developer |
| `src/` | Astro site source: `components/`, `styles/`, `content.config.ts`. | Build | Developer |
| `public/` | Static site assets (currently `favicon.svg`). | Build | Build |
| `docs/` | The Astro Starlight site content: authored narrative pages plus generated catalog pages. | Mixed (see below) | End user |
| `taxonomy.json` | Generated machine index of the catalog (from `tools/build-indexes.py`). | Generated | Agent / downstream |
| `.claude-plugin/` | Plugin manifest and marketplace config (`plugin.json`, `marketplace.json`). | Distribution | Agent |
| `skills/` | The `compose-instruction` skill (`writing-instruction-builder/`). | Source of truth | Agent / end user |
| `.github/` | CI workflows and issue templates. | Build | Maintainer |
| `docs/internal/` | Committed governance: ADRs, working notes, UI mockups, strategy docs. Not published to the site. | Governance | Maintainer |
| `_agent-context/` | Agent working material; `session-log/` is gitignored. | Research | Agent |
| `_LOCAL/` | Gitignored research and scratch: audit reports, AI-chat transcripts, planning drafts. | Research | Maintainer |
| `packages/` | Empty SDK stubs (`.gitkeep` only). Slated for removal; see the roadmap. | Stub | n/a |
| `recipes/` | Empty stub (`.gitkeep` only). The real recipes are generated into `docs/recipes/`. | Stub | n/a |

## Reading the groups

**Source of truth (hand-authored, never generated).** `taxonomy/`, `examples/`, `schemas/`, the authored pages in `docs/`, and the `compose-instruction` skill. Edits start here.

**Generated (do not hand-edit; regenerate instead).** `taxonomy.json` and the generated trees under `docs/` (`docs/reference/`, `docs/examples/`, `docs/recipes/`, `docs/templates/`). A freshness guard fails the build if these drift from source, so editing them by hand is wasted effort.

**Build and tooling.** `tools/` (validate the catalog), `scripts/` (publish it), `tests/`, `src/`, `public/`, `.github/`, and the root config files (`astro.config.mjs`, `package.json`, `.pre-commit-config.yaml`, `requirements-dev.txt`).

**Governance and decisions.** `docs/internal/` holds the committed decision trail (ADRs in `adr/`, working notes in `_working/`, mockups in `ui-mockups/`). It is append-only: new ADRs and plans are added, existing archives are not edited.

**Research and scratch.** `_LOCAL/` and `_agent-context/session-log/` are gitignored. Pre-decision analysis lives here until it earns a durable home.

## The `docs/` subfolders

| Subfolder | Authored or generated | Diataxis role |
|---|---|---|
| `docs/concepts/` | Authored | Explanation (the mental models) |
| `docs/guides/` | Authored | How-to and tutorial |
| `docs/design-standards/` | Authored | Explanation (house style) |
| `docs/governance/` | Authored | Explanation (contributing) |
| `docs/reference/` | Generated | Reference |
| `docs/examples/` | Generated | Reference |
| `docs/recipes/` | Generated | Reference |
| `docs/templates/` | Generated | Reference |
| `docs/internal/` | Authored | Not published (maintainer governance) |
| `docs/superpowers/` | Authored | Not published (specs and plans) |

## Conventions

- **Source folders carry a README; generated folders do not.** A folder README explains the folder's role to a contributor browsing the repo on GitHub. A generated folder would only restate its generator, so it gets no README.
- **One canonical home per fact.** Per ADR 0013, structured facts live in exactly one place and the human-facing view is generated from or linked to it, never duplicated. This map is the top-level human view; the per-folder READMEs are the next level down. Folder structure changes rarely, so this file is hand-maintained for now; the roadmap tracks moving it to a generated, guarded form.
