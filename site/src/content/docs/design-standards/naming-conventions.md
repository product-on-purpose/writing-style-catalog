---
title: Naming Conventions
description: Every naming rule that has to hold across the repo, from entry IDs to commit messages.
---

Consistent naming is what makes the catalog navigable. This page collects every rule that has to hold across the repo.

---

## Entry IDs

Entry IDs are the kebab-case slug used in the folder name, the `id` frontmatter field, and every cross-reference.

**Pattern:** `^[a-z][a-z0-9-]*[a-z0-9]$`

This means:

- All lowercase
- Letters, digits, and single hyphens only
- Must start with a letter
- Must end with a letter or digit (no trailing hyphens)
- No double hyphens, no leading hyphens, no underscores, no spaces

**Examples that pass:** `pragmatic-architect`, `decision-log`, `one-pager`, `prd`, `slack-message`, `procedural`

**Examples that fail:** `Pragmatic-Architect` (uppercase), `pragmatic_architect` (underscore), `1-page` (leading digit), `pragmatic--architect` (double hyphen), `voice-pragmatic-architect` (axis prefix - see below)

The validator runs this pattern check on every entry directory.

---

## No axis prefix in IDs

This is the rule most often violated. Entry IDs do not include their axis. The folder structure (`taxonomy/<axis>/<id>/`) already tells you the axis - putting it in the ID is redundant and noisy at cross-reference time.

| Correct | Incorrect |
| --- | --- |
| `taxonomy/voices/pragmatic-architect/` | `taxonomy/voices/voice-pragmatic-architect/` |
| `taxonomy/tones/candid/` | `taxonomy/tones/tone-candid/` |
| `taxonomy/formats/adr/` | `taxonomy/formats/format-adr/` |

The exception is example files (see below), where the axis prefix is part of the filename pattern, not the ID.

---

## ID uniqueness

IDs must be unique within an axis. Across axes, IDs can theoretically collide, but in practice the catalog avoids it. If you find yourself wanting to add `taxonomy/styles/decision-log` while `taxonomy/formats/decision-log` exists, stop and pick one - the collision creates ambiguity at composition time.

The format `adr` and style `decision-log` are deliberately distinct names even though they describe overlapping concepts. Choose names that signal which axis they belong to.

---

## Folder names

Folder names match the entry ID exactly. The path `taxonomy/voices/pragmatic-architect/ENTRY.md` is the only valid location for the `pragmatic-architect` voice entry.

The required file inside each entry folder is `ENTRY.md` (uppercase, exact spelling). Additional files in the folder are allowed - `variants/`, an `examples/` subdirectory, etc. - but `ENTRY.md` is the canonical entry file.

---

## Example file naming

Example files live under `examples/vertical-slices/<topic-slug>/`, `examples/horizontal-slices/<recipe-id>/`, or `examples/diff-pairs/`.

For vertical slices, the pattern is `<axis>-<entry-id>.md`:

- `voice-pragmatic-architect.md`
- `tone-candid.md`
- `style-problem-solution.md`
- `format-adr.md`

The axis prefix is what makes the example file findable from the file listing - you can scan a topic directory and see at a glance which entries are demonstrated.

Topic slugs follow the same kebab-case pattern as entry IDs: `async-standups`, `morning-routine`, `discipline-of-rest`.

---

## Tags

The `tags` frontmatter field on each entry uses kebab-case strings. No spaces, no underscores, no capitals. Use existing tags where possible - check `taxonomy.json` for the set of tags already in use - and resist adding many new tags per entry. Three to six tags is a healthy range.

Tags are search aids, not classifications. Do not use tags to encode axis membership (the axis is already explicit) or to duplicate cross-references.

---

## Topic slugs

Anchor topic slugs name vertical slices. They appear in `topic_slug` frontmatter fields on example files and in directory names under `examples/vertical-slices/`. Use a short kebab-case phrase that describes the topic, not the genre. `async-standups` beats `team-coordination` (too generic) and `should-we-adopt-async-first-standups` (too long).

The matching `topic_label` field is the human-readable form: "Should we adopt async-first standups?"

---

## Schema file names

JSON Schema files in `schemas/` use the pattern `<name>.schema.json`:

- `entry.universal.schema.json` (the shared base)
- `voice.schema.json`, `tone.schema.json`, `style.schema.json`, `format.schema.json` (axis-specific)
- `example.schema.json` (example file frontmatter)

The `.schema.json` suffix is part of the convention and is used by editors and validators for schema detection.

---

## Commit messages

Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/). The types used in this repo:

- `feat(taxonomy):` - new entries or new examples
- `feat:` - new tooling or significant content not in the taxonomy
- `fix:` - bug fixes (parser bugs, validation failures)
- `chore:` - housekeeping (commits of internal docs, dependency updates)
- `refactor:` - moving or restructuring without changing content
- `docs:` - documentation-only changes

The scope (the part in parentheses) is optional but encouraged for taxonomy work.
