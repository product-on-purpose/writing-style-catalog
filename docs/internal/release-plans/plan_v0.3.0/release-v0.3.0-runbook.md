---
title: "Release runbook: v0.3.0"
type: release-runbook
version: 0.3.0
date: 2026-06-25
status: ready for tag (pending maintainer go-ahead)
---

# Release Runbook: v0.3.0

This is the release-hygiene record and tag/publish procedure for the v0.3.0 tag. It is distinct from
`release-plan.md` (the broader expansion roadmap); this doc governs the act of cutting v0.3.0.

## What ships in v0.3.0

A foundation-plus-first-agentic-content release. Rolls up everything merged to `main` since v0.2.0
(PRs #15 through the v0.3.0 release PR). Headline items (full list in `CHANGELOG.md`):

- **`style-profile` skill** - a personalization front-end that captures a user's default writing
  style as a saved, A/B-confirmed personal recipe. Selection-only; gitignored local state.
- **Five new recipes** (`examples/horizontal-slices/`), the first hand-driven generation batch, taking
  recipes from 5 to 10 and worked examples to 205.
- **The ADR 0009 pedagogical bar** - every entry now carries `tells` / `anti_patterns` /
  `failure_modes`, rendered and schema-required.
- **The v2 taxonomy** (ADR 0010) - domain/family facets on all 60, the `relational` -> `personal`
  rename, the five voice families.
- **Adherence-gate tooling** (`tools/adherence_gate.py`, `anchor_topics.py`, `gate_pilot.py`) - the
  deterministic substrate plus the validated blind cross-vendor judge pilot (developer-facing).

## Version

`0.2.0 -> 0.3.0` (minor: new skill, schema changes, new content). Bumped in `.claude-plugin/plugin.json`
and `library.json` (kept identical per the manifest consistency rule). Skill component versions are
independent: `writing-instruction-builder` stays `0.2.0`; `style-profile` ships at `0.1.0`.

## Pre-tag verification (done on the release branch)

- [x] `python tools/validate.py` - all checks pass (60 entries clean under the required pedagogical bar).
- [x] `python tools/build-indexes.py` - no drift (taxonomy.json 60 entries; coverage.json stable).
- [x] `python -m pytest tests/ -q` - green.
- [x] `node scripts/check-no-dashes.mjs` - no em/en dashes in tracked text.
- [x] `node scripts/validate-plugin-manifest.mjs` - manifest valid; plugin.json and library.json agree.
- [x] Site builds; `node scripts/check-route-parity.mjs site/dist` - baseline updated to 117 routes
      (5 new recipe routes added; no route removed).
- [x] New skill: functional test (correct attribution, process adherence, selection-only) + cross-vendor
      Codex adversarial review (3 P0 / 10 P1 / 2 P2, all fixed).
- [x] New recipes: cross-vendor Codex quality review - stack fidelity passed 10/10; 4 outputs that
      fabricated statistics attributed to real firms were rewritten to marshal evidence structurally.
- [x] Release CI green on the release PR (validate, validate-plugin, build-site, CodeQL, Analyze).

## Tag and publish procedure

The `release.yml` workflow is tag-driven: pushing a `v*` tag builds the plugin ZIP and publishes the
GitHub Release. After the release PR merges to `main` on green CI:

1. `git checkout main && git pull --ff-only` (be on the merged release commit).
2. Re-run the local validators once on `main` (validate.py, pytest, check-no-dashes, validate-plugin-manifest).
3. Tag the exact merged SHA: `git tag -a v0.3.0 -m "v0.3.0: style-profile skill, agentic recipes, pedagogical bar, v2 taxonomy"`.
4. `git push origin v0.3.0` - this fires `release.yml` (builds the ZIP, publishes the GitHub Release).
5. Verify the release workflow run is green and the GitHub Release + ZIP artifact exist.

## Post-tag hygiene

- The `product-on-purpose/agent-plugins` registry re-pins `writing-style-catalog` to `v0.3.0` at its
  next refresh (it tracks the released tag, not `main`).
- Move the `## [Unreleased]` CHANGELOG header back to empty above `## [0.3.0]` (already done in this release).
- The hand-driven generation program continues post-0.3.0 per
  `_agent-context/plans/2026-06-25-master-plan-hand-driven-generation.md` (depth-first, gate-governed).

## Notes

- The big v0.3.0 expansion (the model-calling gate slices and the breadth push toward the ~600-entry
  soft target) is NOT in this tag and continues after it. v0.3.0 ships the foundation + the first
  agentic skill and content batch; the gate's paid-automation decision remains explicitly deferred.
