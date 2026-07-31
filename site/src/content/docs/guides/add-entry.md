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

See [Naming Conventions](../../design-standards/naming-conventions/) for the full rule set.

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

The fastest way to get the frontmatter right is to copy an existing entry from the same axis and edit it. See [Voice and Tone Standards](../../design-standards/voice-and-tone/) for authoring guidance.

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

The validator runs a series of checks (schema validity, cross-references, dash policy, examples, review status, taxonomy membership, pedagogical substance, and more). All must pass. Common failures:

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

This regenerates the machine-readable indexes (`taxonomy.json` and `coverage.json`). The site's reference pages under `site/src/content/docs/reference/` are generated separately by `scripts/gen-site.mjs` at site build time. The pre-commit hook runs the indexer automatically, but running it manually lets you see the changes before staging.

---

## Step 7 - Add at least one example

Every new entry should ship with at least one worked example when it is created as a draft. For new entries, vertical-slice examples are preferred: pick one of the twelve existing anchor topics (for example `async-standups`) and write a new example file showing the new entry rendering that topic. Promotion from `draft` to `stable` is a separate, later step that requires the entry to render across all twelve anchor topics (see [Contribution Process](../../governance/contribution-process/)) - one example is enough to start, not enough to promote.

The file goes in `examples/vertical-slices/<topic-slug>/<axis>-<entry-id>.md`. See `examples/vertical-slices/async-standups/voice-pragmatic-architect.md` for the format.

---

## Step 8 - Commit and open a PR

Use Conventional Commits format for the commit message:

```
feat(taxonomy): add <entry-id> <axis> entry
```

Open a PR against `main`. See the [Contribution Process](../../governance/contribution-process/) for what happens next.

## When validation fails

`python tools/validate.py` prints one `[ERROR]` line per problem and exits non-zero. The
common ones, keyed to the text it actually prints.

### `[ERROR] <path>: schema validation failed: <detail>`

The entry does not match its axis schema. The detail names the offending field. The two that
catch people first:

- **`'tells' is a required property`** and the same for `anti_patterns` and `failure_modes`.
  These three are required on every entry by [ADR 0009](https://github.com/product-on-purpose/writing-style-catalog/blob/main/docs/internal/adr/0009-pedagogical-entry-bar.md),
  and `tells` must carry 5 to 7 items. They are the pedagogical bar, not optional polish.
- **`'domain' is a required property`** on a format, or `family` on a format or voice. These
  come from [ADR 0010](https://github.com/product-on-purpose/writing-style-catalog/blob/main/docs/internal/adr/0010-domain-and-family-organization.md);
  the permitted values live in `tools/taxonomy.py`, not in free text.

The full field list, generated from the schemas themselves, is the
[schema reference](../../reference/schema/).

### `[ERROR] <path>: <field> references unknown entry ID '<id>'`

A `pairs_well_with`, `avoid_with`, or `confusable_with` names an entry that does not exist.
Usually a typo or a plural: ids are singular and kebab-case. Note the referenced entry must
exist, but it does **not** have to be `stable`.

If you added a `confusable_with`, add the matching `### Often confused with` block in the body
too. Every entry in the catalog has one for each id it lists, and a reference with no prose
leaves a reader with a pointer and no explanation.

### `[ERROR] <path>: could not parse frontmatter (missing --- delimiters?)`

The block must open on line 1 with `---` alone and close with `---` alone. A common cause is a
value containing a colon left unquoted, which YAML reads as a nested key:

```yaml
one_liner: A voice that leads with tradeoffs: named, priced, and owned   # breaks
one_liner: "A voice that leads with tradeoffs: named, priced, and owned" # fine
```

### `[ERROR] <path> '<id>': Gate 2: missing worked samples on <topics>`

A `stable` entry must render on all 12 anchor topics. **Drafts are exempt**, which is the
intended path: add the entry as `review_status: draft`, render the samples, then promote with
`python tools/promote.py`. Flipping the status by hand before the renders exist is what
produces this error.

### `[ERROR] <path>: axis '<a>' does not match entry's actual axis '<b>'`

The `axis` field disagrees with the directory the file is in. `taxonomy/voices/` holds
`axis: voice`, singular.

### The dash check fails

```text
FAIL: 1 file(s) contain an em-dash or en-dash; use a hyphen, " - ", or restructure:
```

Neither character is permitted anywhere, including inside quoted material. Use ` - `. A
pre-commit hook enforces this, so the failure usually arrives at commit time rather than from
the validator.

### Nothing fails, but the recommender never surfaces the entry

Validation passing means the entry is well-formed, not that it is reachable. Two reasons an
entry stays invisible:

1. **It is still `draft`.** The recommender scores only `stable` and `reference-quality`.
2. **Its wording does not match how people describe the situation.** The scorer is keyword
   overlap over `when_to_use`, `tells`, `one_liner`, and facets, with no stemmer, so "Layoffs"
   does not match a user who typed "laying off". Run the trace to see exactly what matched and
   which threshold rejected it:

   ```bash
   python skills/entry-recommender/scripts/recommend.py --situation "your text here" --verbose
   ```

   It prints each candidate's matched tokens with their weighted contribution, and for a
   rejected one, whether it failed the score bar, the two-distinct-match gate, or both.
