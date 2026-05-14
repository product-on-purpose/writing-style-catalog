---
adr_id: "0003"
title: Apache-2.0 for Code, CC-BY-4.0 for Content
date: 2026-05-10
status: Accepted
---

# 0003 - Apache-2.0 for Code, CC-BY-4.0 for Content

## Status

Accepted

## Context

The repository contains three kinds of artifact, each with different appropriate license conventions:

1. Code artifacts: validators, build scripts, SDK, CI configuration. Code users typically expect permissive open-source licenses with a patent grant. Apache-2.0 is the standard for developer tooling in the ecosystem and is explicitly preferred over MIT when a patent grant is important.

2. Structured content artifacts: ENTRY.md files, JSON Schemas, recipe YAML, documentation prose. Content users typically expect Creative Commons licenses that preserve attribution while permitting broad reuse. CC-BY-4.0 is the standard for educational and reference content and matches the agentskills.io ecosystem documentation convention.

3. LLM-generated examples: example files produced by running a language model against a prompt. These create a license gray area. In most jurisdictions as of 2026, the copyright status of LLM outputs is unsettled. A human who prompted the model and curated the output has some claim; the model provider has some claim; no single party has an unambiguous claim. The safest downstream posture is to know what you have - which requires recording generation lineage.

Using a single license for the entire repository forces a compromise that serves neither code users nor content users well. Using dual licenses with clear per-artifact rules is more complex but more precise.

## Decision

Apache-2.0 applies to all code artifacts: scripts in `tools/`, the SDK in `sdk/`, validators, CI configuration files, and any other executable or machine-interpreted files.

CC-BY-4.0 applies to all content artifacts: taxonomy entry files (`taxonomy/**/ENTRY.md`), example files, documentation in `docs/`, and any other prose or structured data intended for human or LLM consumption rather than execution.

LLM-generated examples must include three frontmatter fields:

- `author_type: llm`
- `llm_model`: the model identifier used for generation (e.g., `claude-opus-4-7`)
- `llm_prompt_file`: the relative path to the prompt file used for generation

These fields are required, not optional. A validation script rejects example files with `author_type: llm` that are missing any of the three fields.

The NOTICE file and CONTRIBUTING.md both state the dual-license policy. Contributors submit their contributions under both licenses simultaneously, as stated in the contribution agreement in CONTRIBUTING.md.

## Consequences

### Positive
- Maximally permissive for downstream use under both licenses. Users of the code get a patent grant; users of the content get attribution-preserving reuse rights.
- The attribution requirement in CC-BY-4.0 is preserved for content, keeping the catalog's origins traceable.
- The `author_type`, `llm_model`, and `llm_prompt_file` fields create an auditable generation lineage for LLM-generated content - useful if the legal landscape changes.
- Patent grant for code users is provided by Apache-2.0 explicitly, which MIT does not provide.

### Negative
- Dual license is more complex than a single license for contributors to understand. The "which license applies to my contribution?" question requires checking whether the contribution is code or content.
- The license gray area on LLM-generated content persists at the legal level. The `author_type` fields address auditability and transparency, not copyright ownership. Downstream users who need a strong copyright claim on LLM-generated content cannot get one from this repository.

### Neutral
- The repository is public from Phase 0, so the license applies immediately to all published content. There is no private-to-public transition to manage.
- The `author_type: hybrid` value is reserved for content that is LLM-generated and then substantively edited by a human. Hybrid content has the same required fields as `author_type: llm` plus a `reviewer` field.
