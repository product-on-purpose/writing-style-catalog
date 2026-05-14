---
adr_id: "0005"
title: Prohibit Em-Dashes and En-Dashes in All Content
date: 2026-05-10
status: Accepted
---

# 0005 - Prohibit Em-Dashes and En-Dashes in All Content

## Status

Accepted

## Context

Em-dashes (U+2014) are a reliable tell of LLM-generated prose. They appear at high rates in outputs from Claude, GPT, and Gemini models and are rarely used in the natural writing styles of most human writers in digital contexts. An analysis of model outputs conducted during the research phase found em-dashes in roughly 60-70% of 200-word-or-longer responses from the three leading models, appearing most often as an aside marker or as a list-to-explanation connector.

A catalog of writing styles whose own prose reads as LLM-generated undermines its credibility on first read. A reader who opens an ENTRY.md and sees em-dashes in the description text will reasonably doubt whether the catalog represents authentic human voice variation or simply different prompting strategies applied to the same underlying model prose style. The catalog's entire value proposition depends on the reader trusting that the distinctions documented are real and observable.

The same concern applies less strongly to en-dashes (U+2013), which appear in numeric ranges and some editorial contexts and are not a strong LLM tell. However, the visual inconsistency between prose hyphens and en-dashes in the same document is a secondary reason to remove them. En-dashes in ranges are unnecessary; a plain hyphen ("2-5") is conventional in digital prose and easier to type and read.

The catalog owner's global CLAUDE.md already enforces this rule via a pre-commit hook that blocks commits containing U+2014 or U+2013. Formalizing it as an ADR makes the rule part of the project's documented decisions rather than an implicit global preference.

## Decision

No em-dashes (U+2014) or en-dashes (U+2013) appear in any file in this repository. The rule applies to:

- ENTRY.md bodies and frontmatter prose fields
- Example and anti-example files
- Documentation files in `docs/`
- Schemas (in comment strings)
- Code comments and docstrings
- Commit messages
- ADRs themselves (this ADR uses " - " throughout)

The canonical replacement for an em-dash used as an aside marker is " - " (space-hyphen-space). A comma, colon, or sentence break is usually cleaner. Numeric ranges use a plain hyphen. There is no case where an en-dash is required; a plain hyphen covers all range uses in this context.

The rule is enforced by three independent mechanisms:

1. A pre-commit hook at `~/.claude/hooks/no-em-dashes.py` that rejects any commit containing U+2014 or U+2013 in tracked files.
2. `tools/validate.py` scans all files and reports violations, runnable in CI.
3. The AGENTS.md file instructs AI tools working in this repository to avoid both characters.

## Consequences

### Positive
- Prose in the catalog consistently reads as human-authored rather than LLM-generated, supporting the catalog's credibility.
- Enforcement is deterministic - the hook never misses an em-dash that slipped through in pasted text or AI-assisted drafting.
- Aligns with the broader product-on-purpose house style, making the rule consistent across all repositories in the workspace.

### Negative
- Requires contributor adjustment if they habitually use em-dashes in their writing. The substitution rule (" - " or restructure) is mechanical but not zero-effort.
- LLM-assisted authoring of catalog content requires explicit prompting or post-processing to avoid U+2014, since all major models produce it by default.

### Neutral
- The rule applies retroactively when editing an existing document. Any edit to a file must sweep the entire file for violations, not only the changed lines.
- This ADR itself is subject to the rule it documents. All instances of what would conventionally be em-dashes in this document use " - " or have been restructured as separate sentences.
