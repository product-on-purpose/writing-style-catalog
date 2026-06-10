---
adr_id: "0015"
title: Skill slug canonicalization to writing-instruction-builder
date: 2026-06-10
status: Accepted
---

# 0015 - Skill slug canonicalization to writing-instruction-builder

## Status

Accepted - the skill's frontmatter `name` is aligned to its directory, `writing-instruction-builder` (2026-06-10).

## Context

The plugin's single skill lived in `skills/writing-instruction-builder/` while its `SKILL.md` frontmatter declared `name: compose-instruction`. The family Standard (`agent-skills-toolkit/STANDARD.md`) requires the skill `name` to equal its parent directory at every tier (Section 2.5), and treats the name as the component's stable identity (Section 8.2). The mismatch was a Bronze (universal-tier) blocker for the `library.json` convergence work tracked in the agent-plugins packet `docs/internal/convergence/writing-style-catalog-library-json.md`.

Two resolutions were possible: complete the rename to `writing-instruction-builder` (the directory already carried it, and the name is more descriptive), or revert the directory to `compose-instruction` (preserving the published invocation slug).

## Decision

The maintainer chose to complete the rename (packet decision D3, option a, confirmed 2026-06-10). The frontmatter `name`, the invocation examples, and every user-facing "compose-instruction skill" reference move to `writing-instruction-builder`. The skill carries `metadata.version: 0.1.0` from this change onward (Standard 3.7).

This is a user-facing change: the invocation becomes `/writing-style-catalog:writing-instruction-builder ...`. It lands in the `CHANGELOG.md` Unreleased section and ships with the next release. Historical documents (earlier ADRs, release plans, working notes, released CHANGELOG entries) keep the old name as a point-in-time record, per the append-only convention for `docs/internal/`. The docs-site guide route `guides/compose-instruction/` is unchanged: it names the activity (compose an instruction), not the skill, and renaming a published route would require a redirect under the route-parity guard for no reader benefit.

## Consequences

### Positive

- The skill satisfies the Standard's name == directory requirement, unblocking honest universal-tier conformance and the canonical `library.json`.
- The slug now describes what the skill is (a writing-instruction builder), matching the directory and the plugin description.

### Negative

- Users of the old `/writing-style-catalog:compose-instruction` invocation must switch to the new slug after updating; the plugin is early and experimental (v0.2.x), so the blast radius is small and accepted.
