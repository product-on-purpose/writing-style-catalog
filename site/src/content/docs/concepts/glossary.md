---
title: Glossary
description: Definitions for terms used throughout the Writing Style Library.
---

Definitions for terms used throughout the Writing Style Library. Terms are grouped by category; cross-references link to fuller explanations elsewhere in the docs.

---

## Core taxonomy terms

**Axis** - One of the three orthogonal dimensions of a writing instruction. The catalog has three axes: Voice & Tone (a paired axis covering identity and register), Style, and Format. See [The Three-Axis Model](../three-axis-model/).

**Voice** - The persistent identity of the writer. Stable across contexts. Captures professional archetype, characteristic concerns, and assumed reader. Lives in `taxonomy/voices/`.

**Tone** - Situational register layered on voice. Changes with context and message intent. Lives in `taxonomy/tones/`. Voice and Tone are distinct catalog directories but part of the same conceptual axis.

**Style** - The cognitive and rhetorical pattern of the writing. How ideas are sequenced and structured. Lives in `taxonomy/styles/`.

**Format** - The visual and structural container. Defines headings, bullet depth, table layouts, section templates. Lives in `taxonomy/formats/`.

**Entry** - A single unit in the catalog. Lives in its own folder with an `ENTRY.md` file containing frontmatter and a Markdown body. See [How to Add an Entry](../../guides/add-entry/).

---

## Composition terms

**Composition** - The act of combining one entry from each axis into a single structured prompt prefix. See [Composing Instructions](../composition/).

**Composed instruction** - The output of composition: a multi-section prompt prefix that can be prepended to any writing task. Each section is drawn from the matching entry's `llm_instruction_phrasing` field.

**Instruction prefix** - The composed instruction as it appears at the top of a prompt, before the actual writing task. Synonymous with "composed instruction" in most contexts.

**Recipe** - A named, pre-validated combination of entries for a specific use case. Recipes live in `recipes/` and ship with example output.

---

## Example terms

**Vertical slice** - A single anchor topic rendered across many catalog entries. Lets a reader compare how the same situation reads through different voices, tones, styles, or formats. The Phase 0 anchor topic is "Should we adopt async-first standups?" Lives in `examples/vertical-slices/<topic-slug>/`.

**Horizontal slice** - A single combination of entries (a recipe) rendered across many topics. Lets a reader confirm that the recipe produces consistent output regardless of subject matter. Lives in `examples/horizontal-slices/<recipe-id>/`.

**Diff pair** - Two examples that differ on exactly one axis, holding the others constant. Used to teach the distinguishing power of a single dimension. Lives in `examples/diff-pairs/`.

**Anchor topic** - A topic chosen to be the basis of a vertical slice. Anchor topics should bend naturally to most voices in the catalog.

---

## Cross-reference terms

**`pairs_well_with`** - Frontmatter field listing entry IDs that compose well with this entry. Used by the Composer to suggest likely good combinations.

**`avoid_with`** - Frontmatter field listing entry IDs that conflict with this entry or produce poor results when composed.

**`confusable_with`** - Frontmatter field listing entry IDs commonly mistaken for this one. Each confusable entry should have a corresponding "Often confused with" section in the entry body explaining the functional difference.

---

## Authoring and process terms

**Atomic-folder pattern** - The convention that each entry lives in its own folder (`taxonomy/<axis>/<id>/`) rather than in a flat file or a YAML monolith. Allows examples, variants, and assets to be co-located with the entry.

**Frontmatter** - The YAML block at the top of every `ENTRY.md` file, delimited by `---` lines. Contains the entry's metadata and is validated against an axis-specific JSON Schema.

**Review status** - The lifecycle state of an entry. Progression: `draft` -> `reviewed` -> `stable` -> `reference-quality`. New entries start at `draft`. Promotion requires maintainer review. A separate `deprecated` state marks superseded entries. See [Contribution Process](../../governance/contribution-process/).

---

## Tooling terms

**`validate.py`** - The Python script that runs the seven catalog checks: slug format, ENTRY.md presence, frontmatter parsing, JSON Schema validation, cross-reference integrity, em-dash/en-dash linting, and draft-status warnings. Must pass before any commit.

**`build-indexes.py`** - The Python script that generates `taxonomy.json` (machine-readable index) and `docs/reference/index.md` (human-readable entry table) from all `ENTRY.md` files.

**Schema** - A JSON Schema file in `schemas/` defining the required and optional frontmatter fields for an axis. Schemas extend the universal base schema via `allOf`.

---

## Related external references

- **Diataxis** - The documentation framework that distinguishes tutorial, how-to, reference, and explanation modes. The `diataxis-explanation` style entry is named for this framework.
- **NN/g tone profile** - The Nielsen Norman Group's classification of tone into `funny | neutral | serious`. Used in the `nn_g_profile` field of tone entries.
- **Toulmin argument** - The structure of claim, grounds, warrant, and rebuttal used by the `classical-argument` style entry.
