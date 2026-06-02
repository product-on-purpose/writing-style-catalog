---
title: Add an Entry
description: The step-by-step process for adding a new taxonomy entry, from axis choice to PR.
---

This is the step-by-step process for adding a new taxonomy entry. It assumes you have already cloned the repo and installed dev dependencies (see [CONTRIBUTING.md](https://github.com/product-on-purpose/writing-style-catalog/blob/main/CONTRIBUTING.md)).

---

## Step 1 - Decide which axis

The first decision is which of the four axes the new entry belongs to:

- **Voice** if the entry describes who is writing (an identity).
- **Tone** if the entry describes how the writer feels right now (a register).
- **Style** if the entry describes how ideas are organized (a rhetorical pattern).
- **Format** if the entry describes the structural container (an output type).

If the entry seems to fit two axes, it probably needs to be split into two entries. The orthogonality of the axes is load-bearing - mixing voice traits into a format entry, for instance, breaks composability for everyone downstream.

When in doubt, read the closest existing entries in each candidate axis. The axis where the new entry feels most at home is usually the right one.

---

## Step 2 - Pick the ID and create the folder

Entry IDs are kebab-case. They must match the pattern `^[a-z][a-z0-9-]*[a-z0-9]$`. Good IDs are descriptive without being long: `pragmatic-architect`, `decision-log`, `one-pager`.

Create the folder:

```
taxonomy/<axis>/<your-kebab-case-id>/ENTRY.md
```

For example: `taxonomy/styles/timeline-narrative/ENTRY.md`. Do not put the axis name in the ID itself - the folder structure already tells you the axis.

See [Naming Conventions](../design-standards/naming-conventions.md) for the full rule set.

---

## Step 3 - Author the frontmatter

The frontmatter is a YAML block at the top of `ENTRY.md`, delimited by `---` lines on their own.

Required fields for every entry (universal schema):

- `id`
- `name`
- `axis` (must match the folder)
- `one_liner` (under 200 characters)
- `description` (use a YAML literal block scalar with `|`)
- `pairs_well_with` (list, at least one entry)
- `avoid_with` (list, can be empty)
- `confusable_with` (list, can be empty)
- `when_to_use` (list, at least one)
- `when_not_to_use` (list, at least one)
- `llm_instruction_phrasing` (use `|` block scalar)
- `tags` (list)
- `review_status` (start at `draft`)

Each axis has additional required fields - see `schemas/voice.schema.json`, `tone.schema.json`, `style.schema.json`, `format.schema.json`.

The fastest way to get the frontmatter right is to copy an existing entry from the same axis and edit it. See [Voice and Tone Standards](../design-standards/voice-and-tone.md) for authoring guidance.

---

## Step 4 - Write the body

The Markdown body that follows the frontmatter mirrors the structure of existing entries. Standard sections:

- `## {Name}` heading (matches the `name` field)
- One to three description paragraphs (same content as the `description` frontmatter field)
- Axis-specific section: `### Language patterns` (voice), `### Markers` (tone), `### Structural conventions` (style), `### Canonical template` (format)
- `### When to use` paragraph
- `### When not to use` paragraph
- `### Pairs well with` (backticked ID list)
- `### Often confused with` (one entry per `confusable_with` ID, with a sentence distinguishing the two)

Aim for 80-120 lines including frontmatter. Specific, observable, concrete beats abstract every time.

---

## Step 5 - Validate

Run the validator before committing:

```bash
python tools/validate.py
```

The validator runs seven checks. All must pass. Common failures:

- Cross-reference to an ID that does not exist in the catalog (typo or wrong axis)
- An em-dash (U+2014) or en-dash (U+2013) somewhere in the file
- A required frontmatter field missing
- The `axis` field does not match the folder location

---

## Step 6 - Rebuild indexes

After validation passes, rebuild the catalog indexes:

```bash
python tools/build-indexes.py
```

This regenerates `taxonomy.json` and `docs/reference/index.md` so the new entry appears in both. The pre-commit hook does this automatically, but running it manually lets you see the changes before staging.

---

## Step 7 - Add at least one example

Every new entry should ship with at least one worked example. For new entries, vertical-slice examples are preferred: pick a topic that the catalog already has examples for (currently `async-standups`) and write a new example file showing the new entry rendering that topic.

The file goes in `examples/vertical-slices/<topic-slug>/<axis>-<entry-id>.md`. See `examples/vertical-slices/async-standups/voice-pragmatic-architect.md` for the format.

---

## Step 8 - Commit and open a PR

Use Conventional Commits format for the commit message:

```
feat(taxonomy): add <entry-id> <axis> entry
```

Open a PR against `main`. See the [Contribution Process](../governance/contribution-process.md) for what happens next.
