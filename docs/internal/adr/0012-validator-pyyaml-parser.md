---
adr_id: "0012"
title: Replace hand-rolled YAML parser in the validator with PyYAML
date: 2026-05-31
status: Accepted
---

# 0012 - Replace hand-rolled YAML parser in the validator with PyYAML

## Status

Accepted

## Context

The validator (`tools/validate.py`) parsed ENTRY.md and example frontmatter with a hand-rolled function, `_parse_simple_yaml`. That function treated every `  - ` line as a plain string and applied only minimal coercion. It was not a compliant YAML parser, so it silently accepted frontmatter that is not valid YAML.

Two classes of malformed frontmatter slipped through as a result. 35 entries had list items with unquoted embedded colons, which a compliant parser reads as nested mappings rather than strings. 60 examples had unquoted dates, which a compliant parser coerces to date objects rather than strings. The hand-rolled parser saw all of these as plain strings and raised no error. All of them were corrected in prior commits (881b017 and 2b2bb9a) so that the frontmatter is now valid YAML, which means switching parsers no longer changes any parse result for current data.

The new Astro Starlight site generator (ADR 0011) parses frontmatter with PyYAML. That surfaced the divergence: the validator and the generator disagreed on what counted as valid frontmatter. The validator passed files that the generator could not parse the same way, so a file could be "valid" by CI and still be wrong by the generator's reading. A single source of truth for "is this frontmatter valid" is needed across both tools.

`tools/build-indexes.py` imports `_extract_frontmatter` from `tools/validate.py`, so both tools already share a single frontmatter-reading chokepoint. The fix only needs to land at that one function.

## Decision

Parse frontmatter with PyYAML `yaml.safe_load` at the single `_extract_frontmatter` chokepoint in `tools/validate.py`. The existing fence split (the `(?m)^---[ \t]*$` regex that isolates the frontmatter block and correctly handles `---` inside block scalars) is kept; only the parse of the isolated frontmatter text changes. Newlines are normalized to `\n` before parsing because the repo ships CRLF.

Invalid YAML now returns `None` from `_extract_frontmatter`, which `check_frontmatter_parseable` reports as an error and which fails the build. The hand-rolled `_parse_simple_yaml` function is deleted. Because `build-indexes.py` imports `_extract_frontmatter`, this single change fixes both tools without duplicating logic.

PyYAML is already a project dependency (it is listed in `requirements-dev.txt` and is what ADR 0011's generator uses), so no new dependency is introduced.

## Consequences

### Positive
- The validator and the site generator now agree on what frontmatter is valid, because both use PyYAML. CI "valid" and generator "parseable" are the same judgment.
- Real YAML errors are caught at validation time instead of being silently accepted, so malformed frontmatter fails the build rather than producing wrong downstream data.
- One fewer hand-rolled parser to maintain in `tools/`. The behavior is now defined by a maintained, spec-compliant library.
- No new dependency: PyYAML is already declared in `requirements-dev.txt`.

### Negative
- PyYAML is now a hard runtime dependency of `tools/validate.py`. It was already required for development, but the validator previously had no import of it. A developer without PyYAML installed will now see an import error from the validator.

### Neutral
- Type coercion is now PyYAML's. The downstream fields the checks read (ids, axis values, cross-reference lists) are strings and lists either way, so the schema and cross-reference checks are unaffected. Fields like dates are now native date objects rather than strings, which matches the generator's view and does not affect any current check.
- A second, independent copy of `_parse_simple_yaml` still lives in `skills/writing-instruction-builder/scripts/build-instruction.py`. It was out of scope for this change and is left as-is, noted here for a future cleanup.
