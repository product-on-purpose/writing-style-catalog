---
adr_id: "0013"
title: Repository documentation legibility convention
date: 2026-06-01
status: Accepted
---

# 0013 - Repository documentation legibility convention

## Status

Accepted

## Context

The maintainer wants every artifact in the repository to be legible, including to a non-technical reader, and wants a single convention that holds across the product-on-purpose family rather than a decision re-made in each repo. The initial proposal was a same-named `.md` sidecar for every code and config file (`.py`, `.json`, `.mjs`, `.yml`, and similar), each describing what the file does, why it matters, and what uses it.

Taken literally, that convention would create roughly 27 sidecar files in this repo, doubling the tracked code and config surface. About 24 of those 27 files are self-evident industry-standard configs, generated artifacts, or already self-describing JSON Schemas (a non-technical explainer for `package-lock.json` or the generated `taxonomy.json` is noise). The convention's maintenance budget would be spent mostly on files that need nothing.

More decisively, this repository's quality model is generate-and-guard: generated docs in `docs/` are protected by `scripts/check_generated_fresh.py`, which fails the build when a committed copy drifts from its source. No equivalent guard exists for hand-written sidecars. When `validate.py` changes behavior, a `validate.py.md` silently becomes wrong and nothing catches it. A wrong doc is worse than a missing one, because the next reader trusts it.

The family already answers this question. The sibling standard (`agent-skills-toolkit/STANDARD.md`) states the principle as normative:
- Section 10.3 (dual representation, single source of truth): structured facts MUST live in exactly one canonical place; the other view is generated from or linked to it, never duplicated, and tooling MUST flag drift.
- Section 10.4 (public docs): the Diataxis information architecture (tutorials, how-to, reference, explanation).

A same-named `.md` beside every code file is the duplicated-view anti-pattern that Section 10.3 exists to prevent.

## Decision

Adopt a three-layer documentation convention, at the altitude appropriate for a content catalog rather than full plugin conformance:

1. **Repository map.** One `REPOSITORY.md` mapping every top-level folder to its role, kind, and audience. Hand-maintained for now because folder structure is low-churn; tracked for later generation and drift-guarding.
2. **Folder READMEs on source directories** (`taxonomy/`, `examples/`, `schemas/`, `tools/`, `scripts/`, `src/`). Generated folders do not get one, because a README there would only restate the generator.
3. **In-file documentation.** A module docstring at the top of every `.py`, and a header comment on `.mjs`, `.ts`, and `.astro` files. Technical intent lives with the code, where it cannot drift far from what it describes.

Reject the per-file `.md` sidecar convention. It duplicates a view that Section 10.3 requires to be single-sourced, and it has no drift guard in a repo whose quality model is generate-and-guard. Where richer per-file explanation is genuinely warranted (the site generator, the validator, the schema set), prefer a module docstring or a single `schemas/README.md`, not a sidecar.

The canonical source of this convention is `STANDARD.md` Sections 10.3 and 10.4; this ADR records its adoption here. A clause naming the sidecar pattern as an anti-pattern is proposed for `STANDARD.md` so the convention is inherited family-wide rather than re-decided per repo. That clause is drafted separately for maintainer review and is not applied as part of this decision.

## Consequences

### Positive

- Roughly 8 documents instead of 27, covering the same ground with far less drift surface.
- Consistent with the repository's existing generate-and-guard doctrine and with the family standard.
- Non-technical legibility is delivered as one coherent narrative (`REPOSITORY.md` plus folder READMEs) rather than 27 fragments a reader must assemble.
- Decided once and traceable. Future repos reference this rather than re-arguing it.

### Negative

- `REPOSITORY.md` and the folder READMEs are hand-maintained until a generation step lands, so they can drift. The risk is low because folder structure changes rarely.
- The module-docstring expectation is not yet CI-enforced, so until it is, coverage relies on review.

### Neutral

- Full conformance to `STANDARD.md` (tiers, generated `INDEX.md`, eval coverage) is explicitly out of scope. This repository is a content catalog, not a Gold-tier plugin. Only the documentation-legibility and Diataxis principles are adopted.
- Optional enforcement (a docstring-presence check, and a `REPOSITORY.md` coverage check against `git ls-files`, both mirroring `check_generated_fresh.py`) is recorded here for a later decision, not built now.
