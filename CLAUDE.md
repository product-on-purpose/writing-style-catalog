# CLAUDE.md - Claude Code Instructions for Writing Style Library

See `AGENTS.md` for the full multi-agent reference. This file adds Claude Code-specific guidance.

## Quick orientation

This repo is a composable catalog of writing instructions organized into four directories (Voice, Tone, Style, Format):
- **Voice** (`taxonomy/voices/`) - persistent writer identity
- **Tone** (`taxonomy/tones/`) - situational register
- **Style** (`taxonomy/styles/`) - rhetorical and cognitive pattern
- **Format** (`taxonomy/formats/`) - visual/structural container

Each entry lives in its own folder with an `ENTRY.md` file (atomic-folder pattern).

## Key commands

```bash
# Validate all entries (run before every commit)
python tools/validate.py

# Rebuild taxonomy.json (run after adding/editing entries)
python tools/build-indexes.py

# Generate the docs site pages from the catalog (after editing taxonomy/ or examples/)
node scripts/gen-site.mjs

# Build the site locally (runs the generator, then astro build)
cd site && npm run build
```

## Hard rules

- **No em-dashes (U+2014) or en-dashes (U+2013)** anywhere - not in prose, code comments, commit messages, or doc files. Use " - " (space-hyphen-space). This is enforced by a pre-commit hook.
- **`docs/internal/` is a living planning area** (ADRs, release-plan trackers, specs, the backlog) - maintained under direct maintainer direction as work proceeds, not read-only. `docs/internal/_working/` and `_LOCAL/` are frozen historical/research snapshots - read-only, do not modify.
- **Never set `review_status` to `stable` or `reference-quality`** without maintainer review. New entries start at `draft`. (The 60-entry v0.1.0 seed catalog was reviewed and set to `stable` as the baseline; this rule governs new entries.)
- **Conventional Commits** format for all commits: `feat(taxonomy): add <entry-id> <axis> entry`.

## When adding an entry

1. Create `taxonomy/<axis>/<kebab-case-id>/ENTRY.md`
2. Follow the frontmatter schema in `schemas/<axis>.schema.json`
3. Cross-references (`pairs_well_with`, `avoid_with`, `confusable_with`) must use IDs that already exist in the catalog
4. Run `python tools/validate.py` - every check must pass
5. Run `python tools/build-indexes.py` to update the indexes

## Schema changes

Require a version bump and a new ADR in `docs/internal/adr/`. See `AGENTS.md` - Schema Safety section.
