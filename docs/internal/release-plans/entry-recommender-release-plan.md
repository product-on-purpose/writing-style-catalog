---
title: Entry Recommender Skill - release plan
date: 2026-07-02
status: proposal - awaiting maintainer decision to build
author: agent (recommendation only; building and releasing is the maintainer's call)
related:
  - docs/internal/entry-recommender-spec.md (what it does, why - read this first)
  - docs/internal/release-plans/entry-recommender-implementation-plan.md (how to build it)
  - docs/internal/backlog.md (S4 entry)
  - docs/internal/release-plans/promotion-and-release-runbook.md (the release mechanics this plan reuses)
---

# Entry Recommender Skill - Release Plan

This plan covers how the `entry-recommender` skill (spec: `docs/internal/entry-recommender-spec.md`) ships, once the maintainer approves building it. It is a proposal, not a commitment - nothing here is built yet.

## What ships

One new Claude Code skill, `skills/entry-recommender/` (name pending - see the spec's Open Questions), registered as a third component in `library.json` / `.claude-plugin/plugin.json` alongside `writing-instruction-builder` and `style-profile`. No taxonomy or example changes; this is purely a skill-layer addition, so none of the Wave-1/Wave-2 promotion machinery (Gate 2, anchor-topic rendering, date gates) applies.

## Target release

**v0.6.0** (minor bump). This is a genuinely new user-facing capability (a new invokable skill), not a bug fix or a content addition - SemVer's own convention calls for a minor bump, matching how `style-profile`'s v0.3.0 launch was scoped as a new skill, not a patch. Recommend NOT bundling this with any pending content-promotion wave (for example a future Hold-20 decision) - the two are independent decisions on independent timelines, and bundling them would make either one block on the other for no reason.

## Sequencing

1. **Maintainer approves the spec.** `status: draft` -> `status: committed` in `docs/internal/entry-recommender-spec.md`'s frontmatter, per the spec skill's own lifecycle rule that promotion to `committed` is a human action, never automatic.
2. **Build.** Follow `docs/internal/release-plans/entry-recommender-implementation-plan.md` phase by phase.
3. **New-skill hygiene** - see Hygiene Gates below.
4. **Version bump + CHANGELOG + tag**, following the exact mechanics already proven in `docs/internal/release-plans/promotion-and-release-runbook.md` steps 12-13: bump `library.json`/`plugin.json`, roll `CHANGELOG.md` `[Unreleased]` into `[0.6.0]`, tag, push - `release.yml` publishes.
5. **Marketplace registry re-pin**, the same separate-repo manual step already exercised for v0.5.0/v0.5.1 in `product-on-purpose/agent-plugins`.

## Hygiene gates (must pass before tagging)

- [ ] `python tools/validate.py` passes (no schema/dash/cross-reference regressions).
- [ ] `node scripts/validate-plugin-manifest.mjs` passes - the new skill's `SKILL.md` frontmatter carries `name`, `description`, and `metadata.version`, and `library.json`'s new component entry matches it exactly (the validator enforces `frontmatter.name == entry.name` and `frontmatter.metadata.version == entry.version`).
- [ ] `library.json` and `.claude-plugin/plugin.json` descriptions stay byte-identical (the validator's existing parity check).
- [ ] The new skill installs cleanly and its example invocations in `SKILL.md` actually run (manual smoke test - no automated skill-invocation test harness exists in this repo yet).
- [ ] Every spec AC (AC-1 through AC-7; AC-8 optional) has a corresponding `Done` row in the implementation plan's completion-status table before the spec is marked `fulfilled`.
- [ ] `STRICT_ANCHORS=1 node scripts/check-rendered-links.mjs site/dist` and `node scripts/check-route-parity.mjs site/dist` both pass if the site build changes at all (a new skill likely does not touch generated catalog pages, but the docs site's hand-authored guides might gain a cross-link - see the spec's Open Question 3).

## Doc-update checklist (gates the tag)

- [ ] `README.md` - add the new skill to whatever section currently lists `writing-instruction-builder` and `style-profile` (check both the feature list and any install/usage examples).
- [ ] `QUICKSTART.md` - same, if it names specific skills anywhere.
- [ ] `AGENTS.md` - confirm whether this doc's skill references need updating (currently it references the two existing skills only implicitly through the "Generating and Promoting Content at Scale" section, which is about content tooling, not skills - likely no change needed, confirm during implementation).
- [ ] `CHANGELOG.md` - `[0.6.0]` entry describing the new skill, its purpose, and pointing at the spec.
- [ ] `docs/internal/backlog.md` - flip the S4 entry (added alongside this planning pass) from open to shipped, with the release version.
- [ ] `site/src/content/docs/index.mdx` - if the homepage's "How to read this site" cards or skill mentions need a fourth entry.

## What this plan deliberately does not cover

- Whether to build this at all - that is the maintainer's decision, gated on reviewing the spec first.
- The Hold-20 promotion decision - unrelated, independent timeline (see Target Release above).
- The MCP server (backlog S2) - explicitly out of scope per the spec's Non-Goals; remains "reach, not commitment."
