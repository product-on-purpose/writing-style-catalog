---
title: Entry Recommender Skill - release plan
date: 2026-07-02
status: executing - maintainer approved 2026-07-03; built, hardened across 7 rounds of code-level adversarial review, hygiene gates passing; v0.6.0 tag in progress
author: agent (recommendation drafted 2026-07-02; build and release executed 2026-07-03 under maintainer direction)
related:
  - docs/internal/entry-recommender-spec.md (what it does, why - read this first)
  - docs/internal/release-plans/entry-recommender-implementation-plan.md (how to build it)
  - docs/internal/backlog.md (S4 entry)
  - docs/internal/release-plans/promotion-and-release-runbook.md (the release mechanics this plan reuses)
---

# Entry Recommender Skill - Release Plan

This plan covers how the `entry-recommender` skill (spec: `docs/internal/entry-recommender-spec.md`) ships. The maintainer approved building it on 2026-07-03; this document now records what actually happened, not just what was planned.

## What ships

One new Claude Code skill, `skills/entry-recommender/`, registered as a third component in `library.json` / `.claude-plugin/plugin.json` alongside `writing-instruction-builder` and `style-profile`. No taxonomy or example changes; this is purely a skill-layer addition, so none of the Wave-1/Wave-2 promotion machinery (Gate 2, anchor-topic rendering, date gates) applies. Also touches `skills/writing-instruction-builder/scripts/build-instruction.py` (additive `--json` support on the compose path) and `scripts/build-release.sh`/`build-release.ps1` (ship `taxonomy.json`) - see the spec's Revisions 9 through 14 for why.

## Target release

**v0.6.0** (minor bump). This is a genuinely new user-facing capability (a new invokable skill), not a bug fix or a content addition - SemVer's own convention calls for a minor bump, matching how `style-profile`'s v0.3.0 launch was scoped as a new skill, not a patch. Recommend NOT bundling this with any pending content-promotion wave (for example a future Hold-20 decision) - the two are independent decisions on independent timelines, and bundling them would make either one block on the other for no reason.

## Sequencing

1. **Maintainer approves the spec.** `status: draft` -> `status: committed` in `docs/internal/entry-recommender-spec.md`'s frontmatter, per the spec skill's own lifecycle rule that promotion to `committed` is a human action, never automatic.
2. **Build.** Follow `docs/internal/release-plans/entry-recommender-implementation-plan.md` phase by phase.
3. **New-skill hygiene** - see Hygiene Gates below.
4. **Version bump + CHANGELOG + tag**, following the exact mechanics already proven in `docs/internal/release-plans/promotion-and-release-runbook.md` steps 12-13: bump `library.json`/`plugin.json`, roll `CHANGELOG.md` `[Unreleased]` into `[0.6.0]`, tag, push - `release.yml` publishes.
5. **Marketplace registry re-pin**, the same separate-repo manual step already exercised for v0.5.0/v0.5.1 in `product-on-purpose/agent-plugins`.

## Hygiene gates (must pass before tagging)

- [x] `python tools/validate.py` passes (no schema/dash/cross-reference regressions).
- [x] `node scripts/validate-plugin-manifest.mjs` passes - the new skill's `SKILL.md` frontmatter carries `name`, `description`, and `metadata.version`, and `library.json`'s new component entry matches it exactly.
- [x] `library.json` and `.claude-plugin/plugin.json` descriptions stay byte-identical.
- [x] The new skill installs cleanly and its example invocations in `SKILL.md` actually run - smoke-tested by an independent agent with no prior design context against all 7 spec examples (Phase 8), which found and both of us fixed 2 real scorer bugs and 2 `SKILL.md` clarity gaps; the implementation was then adversarially reviewed 7 more times against the real code, finding and fixing 2 packaging/dependency bugs, 2 defense-in-depth gaps (an AC-6 bypass, a raw-score conflict-resolution weakening), a short-list ranking gap, and 2 genuine security issues (shell injection, path traversal) - full detail in the spec's Revisions 9 through 14.
- [x] Every spec AC (AC-1 through AC-7) has a corresponding `Done` row in the implementation plan's completion-status table; AC-8 correctly deferred as nice-to-have, not built.
- [x] `STRICT_ANCHORS=1 node scripts/check-rendered-links.mjs site/dist` and `node scripts/check-route-parity.mjs site/dist` both pass - the new usage guide page (`guides/recommend-entries.md`) needed one relative-link depth fix, caught by this exact gate.

## Doc-update checklist (gates the tag)

- [x] `README.md` - entry-recommender added alongside the other two skills.
- [x] `QUICKSTART.md` - same.
- [x] `AGENTS.md` - confirmed no change needed, per this checklist's own prediction: the file references skills only implicitly through content-tooling sections, not a skill-by-skill list.
- [x] `CHANGELOG.md` - `[0.6.0]` entry describing the new skill, its purpose, and pointing at the spec, plus a Security section calling out the two security-relevant fixes specifically.
- [x] `docs/internal/backlog.md` - S4 flipped from proposed to shipped, v0.6.0.
- [x] `site/src/content/docs/index.mdx` - a brief mention added alongside the existing Quick Start section; no new "How to read this site" card, since those four cards are about navigating catalog CONTENT (browse/diff-pairs/recipes/templates), not skills, and entry-recommender is a different kind of thing.

## What this plan deliberately does not cover

- Whether to build this at all - that is the maintainer's decision, gated on reviewing the spec first.
- The Hold-20 promotion decision - unrelated, independent timeline (see Target Release above).
- The MCP server (backlog S2) - explicitly out of scope per the spec's Non-Goals; remains "reach, not commitment."
