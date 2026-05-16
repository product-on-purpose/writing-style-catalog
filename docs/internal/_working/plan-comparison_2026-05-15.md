---
title: Original "Next" List vs Revised Phase 2 Plan - Orientation and Comparison
date: 2026-05-15
status: orientation doc
type: comparison
related:
  - AGENTS/session-log/2026-05-14_20-00_claude_phase-1-completion.md
  - docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md
  - docs/internal/strategy-approach-roadmap_2026-05-08.md
  - docs/internal/overbuilt-v1-execution-plan_2026-05-09.md
---

# Where the project is and how the two plans differ

## Purpose of this doc

You said you'd gotten lost. This document re-anchors you. It does three things:

1. Summarizes where the project actually is right now (state, not narrative)
2. Compares the original "next" list against the revised Phase 2 plan in one table
3. Calls out the one real strategic difference between them, plainly

## Where the project is right now

- Branch: `main` at HEAD `896fead` (session log commit), code at `9f5c7de`
- Catalog: 60 taxonomy entries (15 per axis), 135 examples, 5 horizontal-slice recipes, 4 diff-pairs
- Infrastructure: `validate.py` with 8 checks (all green), `build-indexes.py`, `compose-instruction` skill, 8 ADRs, 11 authored public docs
- Phase 1 of the strategy roadmap is structurally complete
- Phase 2 of the strategy roadmap is *not yet started* and has not been formally redefined

Source: `AGENTS/session-log/2026-05-14_20-00_claude_phase-1-completion.md`

## The two plans being compared

**Plan A - the original "next" list.** Six candidate work items written at the end of the Phase 1 session log (lines 222-257 of that file). Format: a punch list. No single one was committed to; the list is candidates with rough priority order.

**Plan B - the revised Phase 2 plan.** A structured 8-phase plan I drafted today after our brainstorming. Format: a sequenced plan with one chosen approach (exemplar-driven schema). Two decisions still open (anchor topic 3, branch strategy).

Source for Plan A: `AGENTS/session-log/2026-05-14_20-00_claude_phase-1-completion.md`, lines 222-257
Source for Plan B: `docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md`

## Side-by-side comparison

| Original "next" item | Category | Status in revised plan | Where it lives in revised plan |
|---|---|---|---|
| 1. Phase 2 tooling (SDK / MCP / Composer) | New tooling surfaces | **Deferred, out of scope** | "Out of scope" section |
| 2. Extend no-em-dash check to `docs/` | Hygiene | **Gap, not yet folded in** | (recommendation: fold into Phase 7) |
| 3. Add diff-pair schema + `check_diff_pairs()` | Hygiene | **Included, expanded** | Phase 5 |
| 4. Expand diff-pairs library | Content expansion | **Included, scaled to ~16 with within-axis focus** | Phase 5 |
| 5. Third anchor topic | Content expansion | **Included, with Postgres-vs-DynamoDB recommendation** | Phase 4 |
| 6. Migrate `jsonschema.RefResolver` | Hygiene | **Gap, not yet folded in** | (recommendation: fold into Phase 1) |

And the revised plan adds the following beyond the original list:

| New item in revised plan | Category | Where in revised plan |
|---|---|---|
| Per-entry pedagogical upgrade (tells, anti-patterns, failure modes, mini-glossary, before/after example, cross-ref rationale) | Content depth | Phases 0-2 |
| Catalog doubling (60 to 120 entries) | Content expansion | Phase 3 |
| Schema codification + ADR 0009 | Hygiene + structure | Phase 1 |
| Navigation aids (decision matrix, voice/tone interaction map, style/format compatibility grid) | Structure / meta-layer | Phase 6a |
| Visual taxonomy diagrams (mermaid) | Structure / meta-layer | Phase 6b |
| Richer governance docs | Structure / meta-layer | Phase 6c |
| Per-axis curation rationale | Structure / meta-layer | Phase 6d |
| Release plumbing (CHANGELOG, tag, indexes refresh) | Hygiene | Phase 7 |

## What kind of work is each plan, plainly

Both plans are **content expansion and hygiene work**. Neither is tooling work.

- Plan A is the smaller version: pick a few content/hygiene items off a list of six.
- Plan B is the bigger version of the same kind of work, plus it adds a structure/meta-layer that Plan A didn't envision, plus it raises the depth bar per entry.

The only category in Plan A that *isn't* in Plan B is "new tooling surfaces" (item 1: SDK / MCP / Composer). Plan B explicitly defers that to a later cycle.

## The single real strategic shift

There is one real strategic shift between Plan A and Plan B, and it's not the size or the depth:

**Plan A treats Phase 2 tooling (SDK / MCP / Composer) as the highest-priority next move.** It led the original "next" list with that item.

**Plan B explicitly defers Phase 2 tooling and invests in catalog quality and breadth instead.** This shift was made on your direction during our brainstorming: "I want to further expand / extend the richness of the content base and structure before building an MCP server or composer."

Everything else in Plan B is a scaled-up version of items already in Plan A, or net-new content/structure work that builds on the same foundation. There is no rejection of "content expansion and hygiene as a category." Plan B is more of it, not less.

## What I muddled in earlier messages

In my prior chat response I wrote: *"The original list assumed the existing 60 entries were done and the next move was either tooling, content expansion, or hygiene. The new plan rejects that assumption."* That framing was wrong and is the reason this comparison doc exists. The new plan does not reject content expansion or hygiene; it does *more* of both. The plan only rejects the tooling priority.

I also closed that message by surfacing the MCP item from Plan A as a "be aware you're not doing this" call-out. Reading it back, it came across as "consider doing this instead," which is the opposite of what you'd asked for. Apologies for the confusion that caused.

## Where each artifact lives, for reference

| Artifact | Path |
|---|---|
| Original "next" list | `AGENTS/session-log/2026-05-14_20-00_claude_phase-1-completion.md` (lines 222-257) |
| Revised Phase 2 plan | `docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md` |
| Strategy roadmap (defines Phase 1/2/3 conceptually) | `docs/internal/strategy-approach-roadmap_2026-05-08.md` |
| Overbuilt v1 execution plan (earlier broader plan, deferred) | `docs/internal/overbuilt-v1-execution-plan_2026-05-09.md` |
| Value-delivery approaches (which paths were considered) | `docs/internal/value-delivery-approaches_2026-05-09.md` |
| Phase 1 session log (most recent state record) | `AGENTS/session-log/2026-05-14_20-00_claude_phase-1-completion.md` |

## Recommended next step from a navigation standpoint

If you want to keep moving forward: review the revised plan at `docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md` and decide whether to (a) approve as-is and let me invoke writing-plans, (b) revise specific phases, (c) shrink to a more modest scope, or (d) abandon and pick a smaller item from the original "next" list instead.

If you want to keep thinking before deciding: this comparison doc is now the single place to come back to when you feel lost about which plan you're following.
