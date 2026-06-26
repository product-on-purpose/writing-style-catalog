---
entry_id: adr
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# ADR-0017: Rebuild Checkout as a Parallel System with Incremental Traffic Migration

## Status

Accepted - 2025-02-14
Milestone closure recorded - 2026-06-25

## Context

Cart abandonment had been elevated for three years. Instrumentation pointed to the payment flow as the primary contributor, but the existing checkout system was not safely modifiable: it had grown through five years of emergency patches, carried no meaningful test coverage, and was tightly coupled to the session layer in ways the team did not fully understand. Two previous attempts to refactor it in place had stalled and been abandoned.

Three options were evaluated in early 2025:

1. Continue incremental patching - estimated 18 months to reach a maintainable state, high regression risk throughout, no guarantee of reaching cart-abandonment targets.
2. Big-bang replacement - build a new system and cut over in a single release window. Lower ongoing maintenance burden but no rollback path if the new system failed under real load.
3. Parallel-run replacement - build the new system alongside the existing one, route traffic incrementally by cohort, and keep the old checkout live as a fallback until the new system proved itself under production conditions.

Option 3 was the most expensive to build and operate. It required maintaining two live checkout systems simultaneously, with dual instrumentation, two on-call runbooks, and session compatibility across the boundary. The team would carry that operational overhead for the full duration of the migration.

Engineering lead Priya Nakamura and PM Linh Tran recommended Option 3. Priya's argument: the only way to validate a system built to handle checkout load is to route real checkout load through it. Without a live fallback, the team would have one shot. With a parallel run, they could roll back cohorts without a site incident if something broke.

## Decision

We will rebuild the checkout flow as a separate service, route traffic incrementally by user cohort starting at one percent, and decommission the old system only after the new service has handled at least two peak-load periods without incident.

## Consequences

### Positive

- The new checkout held without degradation under the two highest-traffic periods on record. Cart abandonment dropped in the migrated cohort before full cutover, confirming the hypothesis with live data.
- The rollback capability was exercised in October and December 2025, both times without customer-visible impact. The parallel architecture made those recoveries fast and contained.
- Future changes to the checkout flow now have a tested, instrumented baseline. The codebase no longer depends on undocumented session coupling.

### Negative

- The team maintained two live checkout systems for fourteen months. This was not free: it cost engineering bandwidth, complicated incident response, and required sustained attention from backend engineer Dev Okonkwo and infra lead Marcus Ferreira throughout the run. The full cutover slipped twice as near-miss recoveries and integration work consumed the planned launch windows.
- The parallel-run period produced no visible features. The work was largely invisible to the rest of the organization, which made it difficult to communicate progress or protect the team's capacity.

### Neutral

- ADR-0018 records the decommission schedule for the legacy checkout system.
- Session compatibility shims built for the migration remain in place and will require explicit removal after decommission completes.
