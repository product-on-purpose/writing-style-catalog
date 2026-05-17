---
title: Phase 2 Decisions Pending - Navigation Aid
date: 2026-05-16
status: current
type: decision-checklist
related:
  - docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md
  - docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md
  - docs/internal/_working/catalog-inventory-aspirational_2026-05-16.md
  - docs/internal/_working/phase-0-exemplar-candidates_2026-05-15.md
  - docs/internal/_working/0009-pedagogical-entry-bar.md
  - docs/internal/_working/0010-domain-and-family-organization.md
  - docs/internal/_working/plan-comparison_2026-05-15.md
---

# Phase 2 Decisions Pending - Navigation Aid

## Purpose

Standalone "where you stand and what to decide" doc to come back to when the working set of design docs feels overwhelming. Three decisions are pending; one umbrella choice precedes them. Each decision lists what to read, what to choose between, and what it unblocks.

This doc captures the current state as of 2026-05-16. It is meant to be updated as decisions are locked, or replaced when Phase 2 either starts or is abandoned.

## Current catalog state (the floor)

The repo is already in a strong, shippable state regardless of Phase 2:

- 60 taxonomy entries (15 per axis)
- 195 vertical-slice examples spanning 3 anchor topics (async-standups, morning-routine, service-database-choice)
- 12 diff-pairs covering all four axes
- 5 horizontal-slice recipes
- Working `compose-instruction` skill in `skills/writing-instruction-builder/`
- 9 validators green, including taxonomy schemas, example schema, diff-pair schema, no-em-dash linting across taxonomy/examples/docs
- 8 published ADRs

Phase 2 is ambition, not necessity. The "do nothing more" path stays available.

## Umbrella choice

**Do you want to keep pushing Phase 2 catalog expansion at all?**

| Choice | What it means |
|---|---|
| No | Stop here. Use the catalog for your own writing. Revisit Phase 2 only when observed friction tells you where to expand. The strategy roadmap at `docs/internal/strategy-approach-roadmap_2026-05-08.md:246` explicitly recommends this. |
| Yes | Follow the three-decision path below. |

## The three Phase 2 decisions, in dependency order

### Decision 1: Taxonomy direction

**What to read:** `docs/internal/_working/catalog-inventory-aspirational_2026-05-16.md` (the ~195-format, ~68-voice inventory grouped by v2 categories).

**Choose one:**

| Option | Choice |
|---|---|
| A | v2 cuts and names are right; lock taxonomy as-is |
| B | v2 cuts are right but rename specific families (tell me which and what to rename to) |
| C | v2 cuts are wrong; re-cut (tell me how, or ask me to propose v3 with a different organizing principle) |
| D | Drop the domain layer entirely; use only family with evocative names |
| E | Drop the whole taxonomy idea; the catalog stays flat. Solve the heterogeneity problem differently or live with it |

**What this unblocks:** ADR 0010 sync, `tools/taxonomy.py` sync, Phase 0 exemplars sync to new family names, Phase 1 schema codification scope, Phase 6d curation doc structure.

**Effort:** read the inventory carefully (60-90 minutes), then maybe a short Q&A. The inventory is where the rubber meets the road.

### Decision 2: Design spec direction

**What to read:** `docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md` (the 8-phase plan).

**Choose one:**

| Option | Choice |
|---|---|
| A | Approve as-is; I draft the implementation plan via writing-plans |
| B | Approve with revisions (tell me which phases and how) |
| C | Shrink: do only some phases (e.g., Phase 0-2: upgrade existing 60 entries to the new bar, stop there) |
| D | Abandon; pick a smaller item from somewhere else |

**Open sub-decisions inside (if you approve):**
- Anchor topic 3 - already shipped (`service-database-choice`). Spec text needs a small update to reflect this.
- Branch strategy: one feature branch with phase commits, or PR per phase. Recommendation: one branch (solo work).

**What this unblocks:** the implementation plan can be drafted; Phase 0 can start once Decision 1 is also locked.

**Effort:** read the spec (45-60 minutes), answer 2 open sub-decisions.

### Decision 3: Phase 0 exemplar picks

**What to read:** `docs/internal/_working/phase-0-exemplar-candidates_2026-05-15.md`.

**Choose one:**

| Option | Choice |
|---|---|
| A | Approve the 5 picks (whitepaper, socratic-inquiry, confessional, caregiver, pragmatic-architect) and the recommended order (format first, stress case last) |
| B | Substitute specific entries (tell me which) |
| C | Defer; pick later when Phase 0 actually starts |

**What this unblocks:** Phase 0 execution. (Phase 0 is also blocked by Decisions 1 and 2.)

**Effort:** read the candidates doc (15-20 minutes). Smallest decision of the three.

## Recommended sequence

1. **Read the inventory** → Decision 1 (taxonomy)
2. **Read the design spec** → Decision 2 (the plan)
3. **Read the exemplar candidates doc** → Decision 3 (Phase 0 picks)

Inverse-stakes alternative: do #3 first (small, fast, gives momentum), then #2, then #1 last (the biggest think).

Decisions 1 and 2 are mostly independent. You can approve the design spec without locking taxonomy if you want to start moving; the implementation plan would just defer the taxonomy-dependent pieces (Phase 1 schema, Phase 6d curation) until you decide.

## Three "lightest commitment" doors

If you want to keep moving without committing to the full Phase 2 ambition:

| Door | What it means |
|---|---|
| Lightest | Approve only Decision 1 (taxonomy) and the smallest part of Decision 2 (schema codification for new fields). Then stop. Locks the structure without committing to 120 entries. |
| Medium | Approve Decisions 1 + 2 with scope shrunk to Phase 0-2 only (upgrade existing 60 entries to the new bar; defer breadth expansion). |
| Full | Approve Decisions 1, 2, 3 with full scope; I draft the implementation plan and execution starts. |

All three are revisable. None lock you out of stopping later.

## State summary of every working doc

| Doc | Path | Status |
|---|---|---|
| Phase 2 design spec | `phase-2-catalog-expansion_2026-05-15.md` | Draft, awaiting approval |
| Original-vs-revised plan comparison | `plan-comparison_2026-05-15.md` | Reference only |
| Taxonomy proposal v2 | `domain-and-family-taxonomy_2026-05-15.md` | Draft, awaiting approval |
| Aspirational catalog inventory | `catalog-inventory-aspirational_2026-05-16.md` | Working material for Decision 1 |
| Phase 0 exemplar candidates | `phase-0-exemplar-candidates_2026-05-15.md` | Draft, awaiting approval (references v1 family names, will need sync) |
| ADR 0009 (pedagogical bar) | `0009-pedagogical-entry-bar.md` | Draft, awaiting Decision 2 |
| ADR 0010 (domain/family) | `0010-domain-and-family-organization.md` | Draft, awaiting Decision 1 (references v1 family names, will need sync) |
| This doc | `phase-2-decisions-pending_2026-05-16.md` | Current navigation aid |

All other working docs are reference. The three decisions above are the gate.

## What to do with this doc after you decide

- **If you decide all three:** delete this doc; the design spec and ADRs become canonical and graduate to `docs/internal/`.
- **If you decide partially:** update this doc to reflect what's locked vs still pending.
- **If you abandon Phase 2:** delete this doc; the working docs become decision-trail evidence in git history and the repo stays at its current strong floor.
