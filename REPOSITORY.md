# Repository map

This document explains what every top-level folder in the Writing Style Library is for, so a newcomer can find their way without reverse-engineering the build. It is the overview that sits above the per-folder READMEs.

## How to read this repo in one sentence

The catalog source lives in `taxonomy/` and `examples/`; the tools in `tools/` validate it; the scripts in `scripts/` generate the catalog into `site/src/content/docs/`; and Astro (under `site/`) builds it into the live site.

```
taxonomy/ + examples/        source of truth, directly maintained
        |
   tools/validate.py         integrity gate (7 checks)
   tools/build-indexes.py -> taxonomy.json    machine-readable index
        |
   scripts/gen-site.mjs -> site/src/content/docs/   generated catalog (gitignored, rebuilt each build)
        |
   astro build (under site/) -> the live site
```

## Folders at a glance

| Folder | Role | Kind | Audience |
|---|---|---|---|
| `taxonomy/` | The catalog. 60 `ENTRY.md` files across `voices/`, `tones/`, `styles/`, `formats/` (15 each). | Source of truth | Catalog author |
| `examples/` | Worked output examples: `vertical-slices/`, `horizontal-slices/`, `diff-pairs/`. | Source of truth | Catalog author |
| `schemas/` | JSON Schema for each entry and example type (7 files). The catalog's data contract. | Source of truth | Developer |
| `tools/` | Catalog integrity, source-side: `validate.py`, `build-indexes.py`, `diff-pair-generator.py`, `taxonomy.py`. | Build (validate) | Build / developer |
| `scripts/` | Documentation generation, output-side: `gen-site.mjs` (zero-dependency Node generator). | Build (publish) | Build / developer |
| `tests/` | Tests for the site generator (`gen-site.test.mjs`, run with `node --test`). | Build | Developer |
| `site/` | The Astro app (Pattern S): `astro.config.mjs`, `package.json`, `src/` (`components/`, `styles/`, `content.config.ts`, `content/docs/`), `public/`. | Build | Developer |
| `docs/` | Governance only: `internal/` (ADRs, notes) and `superpowers/` (specs, plans). Not built by Astro; site content lives in `site/src/content/docs/`. | Governance | Maintainer |
| `taxonomy.json` | Generated machine index of the catalog (from `tools/build-indexes.py`). | Generated | Agent / downstream |
| `.claude-plugin/` | Plugin manifest and marketplace config (`plugin.json`, `marketplace.json`). | Distribution | Agent |
| `skills/` | The `compose-instruction` skill (`writing-instruction-builder/`). | Source of truth | Agent / end user |
| `.github/` | CI workflows and issue templates. | Build | Maintainer |
| `docs/internal/` | Committed governance: ADRs, working notes, UI mockups, strategy docs. Not published to the site. | Governance | Maintainer |
| `_agent-context/` | Agent working material; `session-log/` is gitignored. | Research | Agent |
| `_LOCAL/` | Gitignored research and scratch: audit reports, AI-chat transcripts, planning drafts. | Research | Maintainer |
| `packages/` | Empty SDK stubs (`.gitkeep` only). Slated for removal; see the roadmap. | Stub | n/a |
| `recipes/` | Empty stub (`.gitkeep` only). The real recipes are generated into `site/src/content/docs/recipes/`. | Stub | n/a |

## Reading the groups

**Source of truth (directly maintained, never generated).** `taxonomy/`, `examples/`, `schemas/`, the authored pages in `docs/`, and the `compose-instruction` skill. Edits start here.

**Generated (do not hand-edit; regenerate instead).** `taxonomy.json` and the generated catalog under `site/src/content/docs/` (`reference/`, `examples/`, `recipes/`, `templates/`). The catalog is gitignored and rebuilt on every site build (Pattern S), so editing it by hand is wasted effort; `taxonomy.json` is committed and guarded by a `git diff` check in CI.

**Build and tooling.** `tools/` (validate the catalog), `scripts/` (generate the site), `tests/`, the `site/` app (`astro.config.mjs`, `package.json`, `src/`, `public/`), `.github/`, and the repo-root config (`.nvmrc`, `.pre-commit-config.yaml`, `requirements-dev.txt`).

**Governance and decisions.** `docs/internal/` holds the committed decision trail (ADRs in `adr/`, working notes in `_working/`, mockups in `ui-mockups/`). It is append-only: new ADRs and plans are added, existing archives are not edited.

**Research and scratch.** `_LOCAL/` and `_agent-context/session-log/` are gitignored. Pre-decision analysis lives here until it earns a durable home.

## The site content subfolders (`site/src/content/docs/`)

| Subfolder | Authored or generated | Diataxis role |
|---|---|---|
| `concepts/` | Authored (committed) | Explanation (the mental models) |
| `guides/` | Authored (committed) | How-to and tutorial |
| `design-standards/` | Authored (committed) | Explanation (house style) |
| `governance/` | Authored (committed) | Explanation (contributing) |
| `reference/` | Generated (gitignored) | Reference |
| `examples/` | Generated (gitignored) | Reference |
| `recipes/` | Generated (gitignored) | Reference |
| `templates/` | Generated (gitignored) | Reference |

Repo-root `docs/` holds governance only, not built by Astro:

| Subfolder | Role |
|---|---|
| `docs/internal/` | ADRs, working notes, mockups, strategy docs (maintainer governance) |
| `docs/superpowers/` | Specs and plans |

## Conventions

- **Source folders carry a README; generated folders do not.** A folder README explains the folder's role to a contributor browsing the repo on GitHub. A generated folder would only restate its generator, so it gets no README.
- **One canonical home per fact.** Per ADR 0013, structured facts live in exactly one place and the human-facing view is generated from or linked to it, never duplicated. This map is the top-level human view; the per-folder READMEs are the next level down. Folder structure changes rarely, so this file is hand-maintained for now; the roadmap tracks moving it to a generated, guarded form.
