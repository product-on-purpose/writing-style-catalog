---
title: Contribution Process
description: The end-to-end process for contributing, from before-PR checks to the review lifecycle.
---

This is the end-to-end process for contributing to the Writing Style Library. It covers what to do before opening a PR, what happens during review, and how entries move through the review status lifecycle after they land.

For the authoring mechanics, see [How to Add an Entry](../../guides/add-entry/). This page is about the process around the authoring.

---

## Before opening a PR

### Decide what kind of contribution

The repo accepts three kinds of contributions, each with a different review bar:

1. **New taxonomy entry.** A new voice, tone, style, or format. Requires editorial review for distinctness, schema validation, and at least one worked example.
2. **New example.** A new example file for an existing entry. Requires the example to demonstrate the entry recognizably and to use the shared anchor topic scenario (if vertical-slice).
3. **Tooling, schema, or documentation change.** Includes changes to `tools/`, `schemas/`, `docs/`, and the build pipeline. Requires a corresponding ADR if the change affects how entries are authored or validated.

### Run the local checks

Before pushing, run both:

```bash
python tools/validate.py
python tools/build-indexes.py
```

The validator must report zero errors. The indexer must produce no surprise changes - if it modifies `taxonomy.json` or `docs/reference/index.md` in ways you did not expect, investigate before committing.

The pre-commit hook runs the validator and indexer automatically if you installed it (`pre-commit install`). The CI pipeline runs both on every PR.

---

## Opening the PR

### Branch and commit conventions

Work on a feature branch off `main`. Branch names should describe the work in short form: `feat/voice-coach`, `fix/yaml-parser-tables`, `docs/composition-page`.

Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/). See [Naming Conventions](../../design-standards/naming-conventions/) for the types in use.

### What the PR description should include

- A one-sentence summary of what the PR does
- A bulleted list of the files added or changed at the entry level (not every modified file)
- Any cross-references that were added or changed
- For new entries, the rationale for the entry's existence: what gap does it fill?

PRs that change the schema or the validator must also link to a draft ADR explaining the change.

---

## During review

### What reviewers check

For a new taxonomy entry, a reviewer will check:

1. The entry passes the [distinctness test](../../design-standards/voice-and-tone/) against its `confusable_with` entries.
2. The `llm_instruction_phrasing` field would actually shape an LLM's output if used as a prompt prefix.
3. The cross-references are reciprocal where appropriate.
4. The `description` and body do not contain style tells (see [Style Tells to Avoid](../../design-standards/style-tells/)).
5. At least one worked example exists and is recognizable as the entry rendering its topic.

For a new example, a reviewer will check:

1. The frontmatter has all required fields (`entry_id`, `axis`, `topic_slug`, `topic_label`, `author_type`, `review_status`, and `llm_model` if applicable).
2. The example is in the named voice/tone/style/format, not a generic LLM register.
3. For vertical-slice examples, the example uses the shared scenario for the topic.

### Review iteration

Reviewers leave comments on the PR. The author addresses them in additional commits (not force-pushes; this repo prefers a clean commit history that shows the review process).

A reviewer can mark an entry "approved with notes" - meaning the PR can merge, but follow-up work is expected. The notes go into the PR description as a checklist for after-merge work.

---

## After merge

### Initial state

A merged entry starts at `review_status: draft`. This signals that the entry is in the catalog but has not yet been validated through real use.

### Promotion lifecycle

Entries move through four states:

| State | Meaning | Promotion criteria |
|-------|---------|--------------------|
| `draft` | Initial submission, in the catalog but unproven | One maintainer review |
| `reviewed` | Editorially checked, ready for use | Schema valid, examples present, no open issues |
| `stable` | Validated in active use | Two of: worked example exists, used in at least one composed instruction in the wild, two months without revision |
| `reference-quality` | Exemplary - included in onboarding material | Maintainer judgment, rare |

A `deprecated` state exists separately for superseded entries. Deprecated entries remain in the catalog but should set `deprecated_in_favor_of` to point to the replacement.

Promotion to `stable` or `reference-quality` is a maintainer action, never a self-promotion. If you believe one of your entries deserves promotion, open an issue with the case.

### Deprecating an entry

To deprecate an entry, open a PR that:

1. Sets `review_status: deprecated` in the entry's frontmatter
2. Adds `deprecated_in_favor_of: <replacement-id>` if there is a replacement
3. Updates the entry body to explain the deprecation reason
4. Updates cross-references in other entries to point to the replacement

The deprecated entry stays in the catalog. Removing entries is a separate, higher-bar process that requires an ADR.

---

## Maintainer responsibilities

Maintainers are listed in `CODEOWNERS` (when present) or in the `package.json` author field. Their responsibilities:

1. Review and merge PRs against the standards in this document
2. Promote entries through the review status lifecycle when criteria are met
3. Author or approve ADRs for schema and process changes
4. Cut releases when the catalog reaches stable inflection points

Becoming a maintainer is by invitation, typically after sustained high-quality contribution.

---

## Code of conduct

All contributors and maintainers follow the [Contributor Covenant](https://www.contributor-covenant.org) Code of Conduct, as documented in [CODE_OF_CONDUCT.md](https://github.com/product-on-purpose/writing-style-catalog/blob/main/CODE_OF_CONDUCT.md).

Disagreements about entries (which voice should exist, how a style is defined) are normal. Disagreements about people are not.
