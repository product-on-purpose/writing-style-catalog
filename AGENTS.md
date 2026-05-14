# AGENTS.md - Instructions for LLMs Working in This Repo

## Project Purpose

The Writing Style Library is a composable catalog of writing instructions organized along three orthogonal axes: Voice & Tone, Style/Mode/Genre, and Format/Output Structure. The goal is to allow any combination of axis values to be assembled into a structured prompt prefix that shapes LLM writing output toward a specific register, rhetorical pattern, and layout. The library is packaged as a Claude Code plugin with a `compose-instruction` skill, and will grow to include a TypeScript/Python SDK and a Composer SPA in later phases.

---

## The Three-Axis Taxonomy Model

**Axis 1 - Voice & Tone**: Voice and Tone are two dimensions within the first axis. Voice captures persistent identity (how you always sound); Tone captures situational register (how you sound right now). They are kept as separate catalog directories because they have different frontmatter and entry counts, but they belong to the same conceptual axis.

- **Voice** (`taxonomy/voices/`): The persistent identity of the writer. Voice captures worldview, characteristic concerns, and professional archetype. It is stable across contexts. Example seed entries: `pragmatic-architect`, `product-thinker`, `ops-realist`.
- **Tone** (`taxonomy/tones/`): Situational register layered on top of voice. Tone is orthogonal to voice and can be mixed freely. Example seed entries: `candid`, `mentoring`, `optimistic-realist`.

**Axis 2 - Style** (`taxonomy/styles/`): The cognitive and rhetorical pattern of the writing. How ideas are sequenced and structured. Example seed entries: `problem-solution`, `layered-disclosure`, `decision-log`.

**Axis 3 - Format** (`taxonomy/formats/`): The visual and structural container. Defines headings, bullet depth, table layouts, section templates. Example seed entries: `adr`, `daily-standup`, `slack-thread`.

---

## Key Conventions

### Atomic-Folder Pattern

Each taxonomy entry lives in its own folder: `taxonomy/<axis>/<entry-id>/`. The folder contains at minimum `ENTRY.md` (the entry body and frontmatter) plus an `examples/` subdirectory. Additional files such as `variants/` may be added alongside `ENTRY.md`.

### Frontmatter-First

Every entry file must begin with a YAML frontmatter block. The block must include at minimum: `id`, `axis`, `name`, `version`, `review_status`, `tags`, `created`, `author`. Validate against the axis-specific schema in `schemas/` before committing.

### No Em-Dashes, No En-Dashes

This is a hard rule with no exceptions. Do not use U+2014 (em-dash) or U+2013 (en-dash) anywhere in any file you create or modify - including entry bodies, documentation, commit messages, and comments. Use " - " (space-hyphen-space) as the substitute. A pre-commit hook enforces this rule; do not attempt to disable it.

### Review Status Progression

New entries must start at `draft`. The progression is: `draft` -> `reviewed` -> `stable` -> `reference-quality`. Do not set a new entry to `stable` or `reference-quality` without maintainer approval.

---

## How to Add an Entry

1. Create a new folder: `taxonomy/<axis>/<kebab-case-id>/`
2. Create `ENTRY.md` inside that folder
3. Add the required frontmatter fields (see CONTRIBUTING.md for the full list)
4. Write the entry body: definition sentence, "When to use" bullets, "Instruction block" section, optional "Do not use when" section
5. Add at least one example file (vertical slice preferred)
6. Run `python tools/validate.py` and confirm it passes
7. Commit with a Conventional Commits message: `feat(taxonomy): add <entry-id> <axis> entry`

---

## Validation

Always run validation before committing:

```bash
python tools/validate.py
```

This checks frontmatter completeness, schema conformance, no em-dash/en-dash characters, valid `review_status` values, and resolving cross-references.

---

## Schema Safety

Do not modify any file in `schemas/` without also updating every existing taxonomy entry that references that schema version. Schema changes require a version bump and an ADR entry in `docs/internal/adr/`. If you are unsure whether a schema change is safe, open a draft PR and ask for review rather than committing directly.

---

## Paths to Know

| Path | What it contains |
|------|-----------------|
| `taxonomy/` | All axis entries |
| `examples/` | Worked output examples |
| `schemas/` | JSON Schema definitions for entry types |
| `skills/writing-instruction-builder/` | Claude Code plugin skill code |
| `tools/validate.py` | Validation script |
| `docs/` | MkDocs site source |
| `docs/internal/adr/` | Architecture Decision Records |
| `recipes/` | Curated axis combinations for common use cases |
| `_LOCAL/` | Source research - read-only, do not modify |
| `docs/internal/` | Internal strategy docs - read-only, do not modify |
