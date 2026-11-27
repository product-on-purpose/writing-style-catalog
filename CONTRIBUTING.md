# Contributing to Writing Style Library

Thank you for contributing. Writing has more voices than one maintainer knows, so the most valuable contribution is an entry the catalog is missing. This guide covers how to propose one, how to build one, the bar an entry has to clear, and what happens to it after it merges.

---

## Start Here: Three Ways to Contribute

| If you want to... | Do this | Code needed? |
| --- | --- | --- |
| Suggest a voice, tone, style, or format the catalog lacks | [Propose an entry](https://github.com/product-on-purpose/writing-style-catalog/issues/new?template=entry_proposal.yml) | No |
| Build an entry yourself | Path 1 below | Yes, YAML and Markdown |
| Add a worked example or a diff-pair | Path 2 below | Yes, Markdown |
| Fix docs, tooling, or a bug | Open a PR, or [report a bug](https://github.com/product-on-purpose/writing-style-catalog/issues/new?template=bug_report.yml) | Depends |

A proposal is the right first step even if you plan to build the entry. The hardest question about a new entry is whether it is distinct from the entries that already exist, and a proposal settles that before anyone writes YAML. Issues labelled `good first issue` are small, well-scoped tasks that the maintainer has picked out for newcomers.

---

## The Entry Bar

An entry has to clear four tests before it can ship. The first two are editorial. The last two are enforced by `python tools/validate.py`.

### 1. It belongs on exactly one axis

- **Voice** is who is speaking: a persistent identity.
- **Tone** is the register for this piece.
- **Style** is how the ideas are sequenced.
- **Format** is the container the writing arrives in.

If a proposed entry seems to fit two axes, it is usually two entries. The test for an axis is the same everywhere: hold the other three axes constant, change this one value, and the output should change in a way you can point at.

### 2. It is distinct from its nearest neighbour

Every entry lists the entries it is most easily confused with in `confusable_with`. A new entry has to say what separates it from each one, in a sentence a reader could check against a sample. "Candid names the hard truth and gives a path forward; matter-of-fact states it with no frame at all" is the kind of distinction that works. If you cannot write that sentence, the entry is probably a variant of one that already exists.

`confusable_with` is symmetric across the catalog. If your entry lists `matter-of-fact`, then `matter-of-fact` must list your entry too.

### 3. It teaches how to recognise and misuse it (ADR 0009)

Three fields are required on every entry by [ADR 0009](docs/internal/adr/0009-pedagogical-entry-bar.md). They are the pedagogical bar, and they are what the blind judge in the adherence tests reads when it decides whether a sample is faithful or a caricature.

- **`tells`**, 5 to 7 items: the phrases, syntactic moves, or structural markers by which a reader spots the entry in the wild.
- **`anti_patterns`**, 2 to 4 items, each with a `pattern` and a `why`: a common misuse, and why it counts as misapplying the entry. A good anti-pattern usually describes a neighbouring entry by mistake.
- **`failure_modes`**, 2 to 3 items, each with a `mode` and a `mitigation`: how the entry breaks when it is done too hard. A failure mode is the entry over-hitting its own register, such as candour sliding into contempt. It is not a description of using the wrong entry, which belongs in `anti_patterns`.

The schema checks that these fields exist and have the right shape. The validator checks that their content is substantive.

### 4. It renders on every anchor topic

To ship, an entry must have a worked sample on all twelve anchor topics under `examples/vertical-slices/`. This is called Gate 2. A draft does not need all twelve: one sample is enough to open a PR.

---

## The Review Ladder (ADR 0021)

Every entry carries a `review_status`, and every status means exactly what it says. The reasons for this ladder are in [ADR 0021](docs/internal/adr/0021-honest-middle-review-status.md).

| Status | Means | Who sets it | Ships in the plugin? |
| --- | --- | --- | --- |
| `draft` | Initial content, still a candidate | Anyone. New entries start here | No |
| `machine-verified` | Passes every automated check, including all twelve samples. **No maintainer has read it yet** | Tooling: `python tools/promote.py <id>` | Yes |
| `stable` | The maintainer read this entry and approved it | **Maintainer only**: `python tools/promote.py --reviewed <id>` | Yes |
| `reference-quality` | Exemplary, maintainer-reviewed | **Maintainer only** | Yes |
| `deprecated` | Superseded by another entry | Maintainer | No |

`reviewed` also appears in the enum. It is unused for taxonomy entries and kept only for compatibility.

Two rules follow from the ladder:

- **Always submit a new entry as `draft`.** Do not set any status above `draft` by hand. `promote.py` refuses an entry that has not cleared Gate 2.
- **Never set `stable` or `reference-quality` yourself.** Those statuses record a maintainer's reading, and `promote.py --reviewed` only takes named entries, one decision at a time. If you think an entry deserves promotion, open an issue with the case.

---

## Path 1 - New Taxonomy Entry

A taxonomy entry is a directory under `taxonomy/voices/`, `taxonomy/tones/`, `taxonomy/styles/`, or `taxonomy/formats/`. The directory is named with the entry's kebab-case ID and contains exactly one file, `ENTRY.md`. For example: `taxonomy/tones/candid/ENTRY.md`.

Worked examples do not live inside the entry folder. They are separate files under the top-level `examples/` tree (see Path 2).

The fastest way to get an entry right is to copy an existing entry from the same axis and edit it. The [Add an Entry guide](https://product-on-purpose.github.io/writing-style-catalog/guides/add-entry/) walks through every step, and the [schema reference](https://product-on-purpose.github.io/writing-style-catalog/reference/schema/) lists every field.

### Required frontmatter

Every entry needs these fields, defined in `schemas/entry.universal.schema.json`:

```yaml
---
id: <kebab-case-id>            # must match the folder name
name: <Human Readable Name>
axis: voice | tone | style | format   # singular, and must match the folder
one_liner: <under 200 characters>
description: |
  <one to three paragraphs; the load-bearing claim goes first>
pairs_well_with: [<ids>]       # at least one
avoid_with: [<ids>]            # may be empty
confusable_with: [<ids>]       # may be empty; must be symmetric
when_to_use: [<situations>]    # at least one
when_not_to_use: [<situations>]
tells: [<5 to 7 spottable markers>]
anti_patterns:                 # 2 to 4
  - pattern: <a common misuse>
    why: <why it misapplies the entry>
failure_modes:                 # 2 to 3
  - mode: <how the entry over-hits its own register>
    mitigation: <how to recognise and correct it>
llm_instruction_phrasing: |
  <the text the builder puts into the composed prompt>
tags: [<tags>]
review_status: draft
---
```

Each axis adds its own required fields:

| Axis | Also requires | Schema |
| --- | --- | --- |
| Voice | `language_patterns`, `family` | `schemas/voice.schema.json` |
| Tone | `markers` | `schemas/tone.schema.json` |
| Style | `structural_conventions` | `schemas/style.schema.json` |
| Format | `domain`, `family` | `schemas/format.schema.json` |

The permitted `domain` and `family` values live in `tools/taxonomy.py` ([ADR 0010](docs/internal/adr/0010-domain-and-family-organization.md)).

### Body

The Markdown body after the frontmatter mirrors the existing entries:

- A `## {Name}` heading that matches the `name` field
- The description paragraphs
- The axis-specific section: `### Language patterns` (voice), `### Markers` (tone), `### Structural conventions` (style), or `### Canonical template` (format)
- `### When to use` and `### When not to use`
- `### Pairs well with`, as a list of backticked IDs
- `### Often confused with`, with one short block for each `confusable_with` ID that says how the two differ

Specific and observable beats abstract every time. The [Style Tells](https://product-on-purpose.github.io/writing-style-catalog/design-standards/style-tells/) page lists patterns to keep out of entry prose.

---

## Path 2 - New Example

An example is a worked output file under `examples/vertical-slices/`, `examples/horizontal-slices/`, or `examples/diff-pairs/`. Examples show what a composed instruction produces in practice.

A vertical-slice sample for a new entry goes in `examples/vertical-slices/<topic-slug>/<axis>-<entry-id>.md`. Pick one of the twelve existing anchor topics and reuse its shared scenario: the same people, situation, and dates that every other sample on that topic uses. See `examples/vertical-slices/async-standups/voice-pragmatic-architect.md` for the format.

Example frontmatter requires `entry_id`, `axis`, `topic_slug`, `topic_label`, `author_type`, and `review_status` (`schemas/example.schema.json`). If a model wrote the sample, set `author_type: llm` and record the model in `llm_model`. LLM-written samples are welcome, and labelling them honestly is required ([ADR 0007](docs/internal/adr/0007-llm-example-author-policy.md)).

---

## Dev Loop

```bash
# Clone the repo
git clone https://github.com/product-on-purpose/writing-style-catalog.git
cd writing-style-catalog

# Install Python dev dependencies (includes pre-commit and validation tools)
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Make your changes, then validate
python tools/validate.py

# Rebuild the indexes after adding or editing an entry
python tools/build-indexes.py

# Run tests
python -m pytest -q
```

`python tools/validate.py` checks, among other things:

- Frontmatter against the axis-specific JSON Schema, including the ADR 0009 fields
- That every cross-reference resolves to an entry that exists
- That `review_status` is a valid value
- That every admitted entry renders on all twelve anchor topics (Gate 2)
- That no file contains an em-dash (U+2014) or en-dash (U+2013)

The test suite adds two catalog-wide checks: `confusable_with` must be symmetric, and every `confusable_with` ID needs an `### Often confused with` block in the body. The guide's [When validation fails](https://product-on-purpose.github.io/writing-style-catalog/guides/add-entry/#when-validation-fails) section explains the common errors.

---

## PR Requirements

Before opening a pull request:

- [ ] `python tools/validate.py` passes with no errors
- [ ] `python -m pytest -q` passes
- [ ] No em-dashes (U+2014) or en-dashes (U+2013) in any file
- [ ] Commit messages follow Conventional Commits, for example `feat(taxonomy): add <entry-id> <axis> entry`

For a new taxonomy entry, also:

- [ ] `review_status` is `draft`
- [ ] `tells`, `anti_patterns`, and `failure_modes` are filled in with real content
- [ ] Each `confusable_with` entry lists yours back, and the body explains how the two differ
- [ ] At least one worked sample on an anchor topic, under `examples/vertical-slices/`

PRs that fail validation will not be merged.

---

## Code of Conduct

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) Code of Conduct. Please read it before participating.

---

## License Agreement

By submitting a pull request to this repository, you agree that:

- Code contributions (schemas, scripts, tools, skill code) are licensed under the [Apache License 2.0](LICENSE).
- Content contributions (taxonomy entries, examples, documentation) are licensed under [Creative Commons Attribution 4.0 International (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/).

If your contribution includes LLM-generated content, say so in the frontmatter: `author_type: llm` and `llm_model` on examples.
