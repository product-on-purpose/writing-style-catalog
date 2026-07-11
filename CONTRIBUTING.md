# Contributing to Writing Style Library

Thank you for contributing. This guide covers the two main contribution paths: adding taxonomy entries and adding examples.

---

## Two Contribution Paths

### Path 1 - New Taxonomy Entry

A taxonomy entry is a directory under `taxonomy/voices/`, `taxonomy/tones/`, `taxonomy/styles/`, or `taxonomy/formats/`. Each entry directory is named with a kebab-case ID and contains exactly one file:

- `ENTRY.md` - the entry body and frontmatter

Worked examples do not live inside the entry folder. They are separate files under the top-level `examples/` tree - for a new entry, `examples/vertical-slices/<topic-slug>/<axis>-<entry-id>.md` (see Path 2 below).

For example: `taxonomy/voices/pragmatic-architect/ENTRY.md`. Each entry defines one reusable writing instruction component.

### Path 2 - New Example

An example is a worked output file under `examples/vertical-slices/`, `examples/horizontal-slices/`, or `examples/diff-pairs/`. Examples demonstrate what composed instructions produce in practice.

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

# Run tests
pytest tests/
```

Validation (`python tools/validate.py`) checks:
- Frontmatter completeness against the axis-specific JSON Schema
- No em-dashes (U+2014) or en-dashes (U+2013) anywhere in content
- `review_status` is a valid progression value
- All cross-references to other entries resolve

---

## Entry Authoring Checklist

### Required Frontmatter Fields

All taxonomy entries must include these frontmatter fields at the top of the file (YAML block between `---` markers):

```yaml
---
id: <kebab-case-unique-id>
axis: voices | tones | styles | formats
name: <Human Readable Name>
version: "1.0"
review_status: draft
tags: []
created: YYYY-MM-DD
author: <github-handle or name>
---
```

Additional fields vary by axis (see `schemas/` for the full JSON Schema per axis).

### Body Standards

- Lead with a one-sentence definition: what this entry is and what problem it solves.
- Follow with a "When to use" section (2-5 bullet points).
- Include an "Instruction block" section containing the exact text to inject into a prompt.
- Optionally include a "Do not use when" section.
- No em-dashes or en-dashes anywhere in the file.
- Maximum 600 words per entry body.

### Example Requirements

Every new taxonomy entry should be accompanied by at least one example file. Vertical-slice examples are preferred for new entries: pick a real-world topic and show the full composed output.

---

## PR Requirements

Before opening a pull request:

- [ ] `python tools/validate.py` passes with no errors
- [ ] `python -m pytest tests` passes
- [ ] No em-dashes (U+2014) or en-dashes (U+2013) in any file
- [ ] At least one anchor example using the new entry
- [ ] Schema validation passes for all modified entries
- [ ] `review_status` is set to `draft` for new entries
- [ ] Commit message follows Conventional Commits format

PRs that fail schema validation will not be merged.

---

## Review Status Progression

Entries move through these states as they are reviewed:

| Status | Meaning |
|--------|---------|
| `draft` | Initial submission, not yet reviewed |
| `reviewed` | At least one maintainer review complete |
| `stable` | Validated against multiple real examples, no open issues |
| `reference-quality` | Exemplary entry, included in generated documentation |

---

## Code of Conduct

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) Code of Conduct. Please read it before participating.

---

## License Agreement

By submitting a pull request to this repository, you agree that:

- Code contributions (schemas, scripts, tools, skill code) are licensed under the [Apache License 2.0](LICENSE).
- Content contributions (taxonomy entries, examples, documentation) are licensed under [Creative Commons Attribution 4.0 International (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/).

If your contribution includes LLM-generated content, include `llm_model` and `llm_prompt_file` fields in the frontmatter.
