---
title: Phase 2 Catalog Expansion - Design
date: 2026-05-15
author: claude (Opus 4.7) in collaboration with jprisant
status: draft - awaiting user review
type: design-spec
related:
  - docs/internal/strategy-approach-roadmap_2026-05-08.md
  - docs/internal/overbuilt-v1-execution-plan_2026-05-09.md
  - AGENTS/session-log/2026-05-14_20-00_claude_phase-1-completion.md
  - skills/writing-instruction-builder/SKILL.md
---

# Phase 2 Catalog Expansion - Design

## Context

Phase 1 is structurally complete. The catalog stands at:

- 60 taxonomy entries (15 per axis: voices, tones, styles, formats)
- 135 examples (60 vertical-slice on `async-standups`, 60 on `morning-routine`, 15 inside horizontal-slice recipes)
- 5 horizontal-slice recipes with worked examples
- 4 seed diff-pairs (one per axis)
- 8 ADRs, 11 authored public docs, working `compose-instruction` skill, `validate.py` with 8 checks, `build-indexes.py`
- Branch `main` at `9f5c7de`, pushed to origin; one chore commit (`896fead`) for the Phase 1 session log

The strategy roadmap at `docs/internal/strategy-approach-roadmap_2026-05-08.md` originally scoped 15/axis as Phase 1 and 30/axis as Phase 2, alongside SDK, MCP server, and Composer SPA surfaces. This design intentionally defers all Phase 2 *tooling surfaces* (SDK, MCP, Composer) and instead expands the *content base and structure* of the repo, on the explicit user direction:

> "I want to further expand / extend the richness of the content base and structure before building an MCP server or composer."

The rationale: the catalog is the substrate every later surface consumes. Surfaces built on a thin or uneven catalog inherit those weaknesses. Investing in catalog quality and comprehensiveness first compounds the value of every later surface.

## Goal

Take the catalog from "structurally complete at 60 entries / one bar" to "uniformly rich at 120 entries / pedagogical bar / three anchor topics / dense diff-pair coverage / full meta-layer."

A reader landing on any single entry should find enough material to (a) understand what the entry is, (b) recognize it in the wild, (c) avoid common misapplications, (d) see it instantiated on multiple topics, and (e) navigate from it to compatible, contrasting, and confusable neighbors.

## Locked decisions

The following were settled during brainstorming and are inputs to this design, not open questions:

| Dimension | Decision |
|---|---|
| Primary levers | Balanced expansion (breadth + depth) AND structural/meta layer |
| Catalog size target | 30 entries per axis - 120 total |
| Per-entry bar | Full pedagogical: tells + anti-patterns + failure modes + dense cross-references + mini-glossary + before/after example pair |
| Meta-layer scope | Navigation aids + visual taxonomy diagrams + richer governance docs + per-axis curation rationale (all four; sequencing TBD) |

## Approach decision

Three candidate approaches were evaluated:

| Dimension | A - Scale first | B - Depth first | C - Schema first |
|---|---|---|---|
| Rework risk if bar shifts | High - 60 new entries to patch | Medium - audit in-flight | Low - exemplars catch it |
| Speed to "120 entries" milestone | Fastest | Slowest | Middle |
| Speed to "uniform high quality" | Slowest | Fastest if you stop mid-flight | Fastest end-to-end |
| Visible week-1 progress | Big counts | Polish (looks like nothing) | Schema (looks like less than nothing) |
| Stopping point if energy fades | 120 mixed-quality entries | 60 polished entries | 5 polished entries + schema |
| Worst case | Patching 60 entries demoralizes; abandon at "looks done, isn't" | Audit completes; new entries surface schema gaps; partial rework | Schema thrash before any content ships |

The original Approach C (schema-first) had the lowest rework risk but a real failure mode: schema designed in the abstract without exercising it on real content. Approach B (depth-first) had a "discover through use" advantage but only on already-shipped content, missing edge cases that fresh writing would surface.

**Refined recommendation: exemplar-driven schema.** Write 5 exemplar entries *first* (one per axis plus one stress-case), let the act of writing them force every design decision, codify the schema from what worked, then scale. This combines Approach B's discovery advantage with Approach C's rework protection.

Precedent: session-log commit `e0fb1d4` documents a real case where a content batch was generated before the validator caught a schema issue, and 20 examples needed rework. At 120 entries each carrying ~8 new fields plus a before/after example, getting schema wrong before generation could cost a multiple of that.

## Execution plan - 8 phases

### Phase 0 - Exemplar craft

Pick 5 entries and upgrade each by hand to the full pedagogical bar with no schema constraints. Candidates:

- One voice (e.g., `caregiver` - emotional register stress)
- One tone (e.g., `confessional` - intimate register stress)
- One style (e.g., `socratic-inquiry` - rhetorical pattern stress)
- One format (e.g., `whitepaper` - long-form structural stress)
- One stress case crossing axes (TBD during execution)

For each exemplar, produce:
- The full upgraded entry with all new fields populated
- Before/after example (50-100 word passage written without and with the entry applied)
- Worked notes on what was hard, what felt forced, what shape each field wants to take

Deliverable: 5 exemplar entries + a short field-shape memo in the design doc.

### Phase 1 - Schema codification

Read across the 5 exemplars. Codify what worked into entry schemas. Likely changes:

- New required fields: `tells` (array of 5-7 strings), `anti_patterns` (array of 2-4 objects with `pattern` and `why`), `failure_modes` (array of 2-3 objects with `mode` and `mitigation`), `before_after_example` (object with `before`, `after`, optional `commentary`)
- Tighten cross-references: `pairs_well_with`, `avoid_with`, `confusable_with` upgrade from bare ID arrays to objects with `id` and `rationale`
- New required field: `mini_glossary` (object/array of 2-3 term/definition pairs)
- Per-axis divergence handled in axis-specific schemas where field shapes differ

Migration strategy: add new fields as **optional** during this phase so the existing 55 entries don't fail validation mid-flight. Tighten to required after Phase 2 completes.

Update `validate.py` to enforce new fields. Update `build-indexes.py` to surface new fields in the public index. Write a new ADR `0009-pedagogical-entry-bar.md` documenting the schema change rationale (required by AGENTS.md:68 for schema changes).

Deliverable: updated schemas, validator, build-indexes, ADR. All 5 exemplars validate green.

### Phase 2 - Audit-and-upgrade existing 55

Four parallel agents, one per axis (voices, tones, styles, formats), each upgrading their 14-15 entries (15 minus any exemplars from that axis) to the full pedagogical bar. The exemplars go in each agent's prompt as canonical templates.

Specific watch-outs derived from Phase 1 sessions:
- Re-state any field-shape conventions that agents have historically drifted on (the `entry_id` axis-prefix bug from `e0fb1d4`)
- Validator runs after each agent's batch to catch drift early
- Exemplars from other axes also go in the prompt as cross-axis reference

After this phase: tighten schema fields from optional to required. Run full validator. All 60 entries now at full bar.

Deliverable: 60 entries at full pedagogical bar; validator green with new fields required; build-indexes regenerated.

### Phase 3 - Generate 60 new entries to hit 30/axis

Same parallel-agent pattern as Phase 2, generating rather than upgrading. Each agent generates 15 new entries in its axis, written directly at the new bar. Schema enforcement is now required, so validator catches drift in real time.

Selection criteria for the new 15 per axis - to be locked in the per-axis curation rationale doc (Phase 6) but sketched here:

- **Voices** (15 more, to reach 30): cover ranges currently thin - e.g., satirist, polemicist, historian, naturalist, contrarian, ethicist, beginner-explainer, insider-confidant, optimist, pragmatist-skeptic, outsider, elder, peer, advocate, witness
- **Tones** (15 more): grateful, weary, reverent, hopeful, defiant, deferential, exasperated, sober, tender, bemused, vigilant, cautious, exuberant, restrained, contemplative
- **Styles** (15 more): comparison-contrast, cause-effect, first-principles-derivation, anecdote-then-principle, prediction-and-rationale, retrospective-analysis, hypothesis-and-test, taxonomy, debunking, manifesto, postmortem, parable, field-notes, position-paper, primer
- **Formats** (15 more): linkedin-post, podcast-show-notes, newsletter-issue, talk-abstract, conference-proposal, eulogy, wedding-toast, performance-review, peer-feedback-note, design-doc, RFC, error-message, microcopy, onboarding-walkthrough, FAQ

The lists above are starting candidates, not commitments. Per-axis selection will be re-grounded during Phase 6 curation work.

Deliverable: 120 entries total, all at full pedagogical bar, all validators green.

### Phase 4 - Third anchor topic

Pick the third anchor topic (see Open Decisions). Dispatch four parallel agents to generate 120 examples (one per entry) on the new topic. Anchor topics now cover three distinct content territories, exercising different parts of the catalog.

After this phase, every entry has:
- An own before/after example (inside the entry)
- Three vertical-slice examples (one per anchor topic)

Total examples after Phase 4: 360 vertical-slice + 15 horizontal-slice = 375 (up from 135).

Deliverable: 120 new examples; `examples/vertical-slices/<topic-3>/` populated; validator green.

### Phase 5 - Diff-pair expansion to ~16

Target 4 diff-pairs per axis, focused on within-axis confusables that are pedagogically valuable. Candidates:

- Voices: `pragmatic-architect` vs `senior-consultant`, `coach` vs `friendly-mentor`, `journalist` vs `storyteller`, `direct-communicator` vs `executive`
- Tones: `candid` vs `confident`, `warm` vs `empathetic`, `urgent` vs `resolute`, `playful` vs `celebratory`
- Styles: `narrative-case-study` vs `chronological-narrative`, `executive-summary` vs `layered-disclosure`, `socratic-inquiry` vs `dialectic`, `decision-log` vs `frequently-asked-questions`
- Formats: `adr` vs `whitepaper`, `slack-message` vs `email`, `readme` vs `technical-reference`, `tweet-thread` vs `blog-post-long-form`

(All entry IDs above verified against the current catalog at HEAD `896fead`.)

Also in this phase:
- Add `schemas/diff-pair.schema.json`
- Add `check_diff_pairs()` to `validate.py` (closes the known non-blocker noted in the Phase 1 session log)

Deliverable: 16 diff-pairs covering all four axes with explicit within-axis confusable focus; diff-pair schema and validator in place.

### Phase 6 - Meta-layer

Four sub-deliverables (sequence can be parallelized across sessions):

**6a. Navigation aids.** Three documents under `docs/how-to/` and `docs/concepts/`:
- `how-to/choose-voice-tone-style-format.md` - decision aid: "when X, consider Y"
- `concepts/voice-tone-interaction.md` - grid showing voice x tone combinations (coherent / neutral / awkward / contradictory)
- `concepts/style-format-compatibility.md` - grid showing style x format combinations (natural-fit / possible-but-awkward / genre-violation)

**6b. Visual taxonomy diagrams.** Mermaid diagrams under `docs/concepts/`:
- Three-axis model diagram
- Entry relationship diagram (sample neighborhood: `pragmatic-architect` and its `pairs_well_with` / `avoid_with` / `confusable_with` neighbors)
- Anchor topic coverage diagram (which entries are exercised by which topic; visualizes gaps)

**6c. Richer governance docs.** Expand `docs/governance/`:
- Existing: `contribution-process.md`
- Add: `contribution-checklist.md`, `review-rubric.md`, `deprecation-policy.md`, `schema-evolution-policy.md`

**6d. Per-axis curation rationale.** One doc per axis under `docs/internal/curation/`:
- `voices.md`, `tones.md`, `styles.md`, `formats.md`
- Each explains selection logic for the chosen 30, gaps deliberately left, criteria for accepting new proposals

Deliverable: full meta-layer artifacts; public site rebuilds cleanly under mkdocs.

### Phase 7 - Release plumbing

- Run all validators end-to-end
- Rebuild indexes (`build-indexes.py`)
- Update public docs index, README badges/counts, AGENTS.md statistics
- Update CHANGELOG with Phase 2 release notes
- Tag `v0.2.0` (or whatever the next minor is)
- Push to origin

Deliverable: tagged release, clean main branch, complete documentation reflecting new state.

## Schema and validator changes

Documented in detail in the ADR `0009-pedagogical-entry-bar.md` (to be written in Phase 1). Summary:

| Change | Phase added | Phase enforced as required |
|---|---|---|
| `tells` field | 1 (optional) | 2 (required) |
| `anti_patterns` field | 1 (optional) | 2 (required) |
| `failure_modes` field | 1 (optional) | 2 (required) |
| `before_after_example` field | 1 (optional) | 2 (required) |
| `mini_glossary` field | 1 (optional) | 2 (required) |
| Cross-references upgrade (id->object with rationale) | 1 (optional both shapes accepted) | 2 (required object shape) |
| New `check_diff_pairs()` validator | 5 | 5 |
| New `diff-pair.schema.json` | 5 | 5 |

## Stopping points - energy-fade resilience

In rough order from worst to best stopping state:

| Stop after | State | Recoverable? |
|---|---|---|
| Phase 0 | 5 exemplars in working state | Yes - exemplars become canonical even without scale |
| Phase 1 | 5 exemplars + locked schema; 55 entries flagged missing-fields | Yes - schema is the deliverable |
| Phase 2 | 60 entries at full bar | Yes - clean product, strong public artifact |
| Phase 3 | 120 entries at full bar | Phase 2 milestone hit |
| Phase 4 | 120 entries + 3 anchor topics | Strong content depth |
| Phase 5 | + 16 diff-pairs + diff-pair schema | All axes covered |
| Phase 6 | + full meta-layer | Phase 2 catalog work complete |
| Phase 7 | Tagged release | Done |

Phase 2 is the natural early stopping point: 60 polished entries is a clean shippable product even if the breadth expansion never happens.

## Open decisions

These need user input before execution. Marked here rather than guessed-and-revised-later:

### 1. Third anchor topic

Candidates:

- **"Choosing between Postgres and DynamoDB for a new service"** - exercises architect/operator voices, candid/diplomatic tones, decision-log/dialectic styles, ADR/whitepaper/RFC formats. Contrasts cleanly with both existing anchor topics (workplace decision vs lifestyle vs technical decision).
- **"Onboarding a new team member"** - exercises mentor/coach voices, encouraging/instructional tones, how-to-tutorial/checklist styles, runbook/email/walkthrough formats. Contrasts with existing topics on register and audience.
- **"Public statement after a service outage"** - exercises executive/operator voices, accountable/confident/diplomatic tones, urgent/resolute tones, executive-summary/incident-report formats. Contrasts on stakes and audience.
- **"The discipline of rest"** - candidate from Phase 1 session log. Risk: too close to `morning-routine` in audience/register; may not exercise different parts of the catalog enough.

Recommendation: **Postgres vs DynamoDB**. It pulls hardest on parts of the catalog the first two topics undersell (technical decision-making, RFC/whitepaper formats, dialectic/comparison-contrast styles).

### 2. Branch and PR strategy

- **Option A: One feature branch with phase commits.** `feat/phase-2-catalog-expansion`. Push commits per phase. Fast-forward merge to main at the end. Simpler for solo work.
- **Option B: PR per phase to main.** Seven PRs. Better for reviewability if a contributor joins. More overhead solo.
- **Option C: Phase 0-1 on a branch, phases 2+ direct commits to main.** Schema work is risky and deserves PR review structure; downstream phases are routine content. Hybrid.

Recommendation: **Option A**. Solo work, no second reviewer; the session log shows the Phase 1 branch pattern worked well.

## Risks

| Risk | Mitigation |
|---|---|
| Schema designed wrong despite exemplars | Phase 1 keeps fields optional initially; Phase 2's audit pass on 55 entries is itself a stress test before tightening |
| Parallel agents drift on field shapes | Exemplars in every prompt as canonical templates; per-batch validator runs |
| Scope creep into Phase 6 (meta-layer) | Phase 6 is the most expandable; explicit sub-deliverable list above; resist adding more without revising this doc |
| Per-axis curation rationale becomes marketing | The doc rubric in 6d says "honest curation thinking, not marketing" - reread before each curation doc to enforce |
| Effort fatigue before Phase 6 | Phase 2 stopping point is shippable; Phase 5 is shippable; the design is fade-resilient |
| Anchor topic 3 choice constrains examples | Topic should be picked before Phase 4 starts, not earlier; current design holds it open |
| em/en-dash regression in agent-generated content | Hook + validator already enforce; remind agents in prompts |

## Out of scope

Explicitly excluded from this design and deferred to a later cycle:

- Phase 2 *tooling* surfaces: TypeScript SDK, Python SDK, MCP server, Composer SPA (deferred per user direction; revisit after this catalog work)
- Eval harness with Promptfoo
- Browser extension
- Fourth anchor topic
- Translation / non-English entries
- Marketplace submission and packaging
- Skill pack distribution polish (the existing `compose-instruction` skill is in repo; further packaging is later)

## Verification at completion

The plan is complete when all of the following are true:

- `python tools/validate.py` reports green on all checks including the new `check_diff_pairs()`
- `python tools/build-indexes.py` produces a clean `taxonomy.json` and `docs/reference/index.md`
- 120 entries in `taxonomy/`, 30 per axis
- Every entry has all required pedagogical fields populated
- Every entry has at least 3 anchor-topic examples and its own before/after pair
- At least 16 diff-pairs covering all 4 axes with within-axis focus
- `docs/concepts/`, `docs/how-to/`, `docs/governance/` reflect new meta-layer artifacts
- ADRs `0009` (and any others needed) committed under `docs/internal/adr/`
- CHANGELOG updated, tag pushed

## Approval gate

This is a draft awaiting user review. The two open decisions above (anchor topic 3, branch strategy) need answers before the implementation plan is generated. Once approved, the next step is to invoke the writing-plans skill to translate these 8 phases into a concrete task plan with checkpoints.
