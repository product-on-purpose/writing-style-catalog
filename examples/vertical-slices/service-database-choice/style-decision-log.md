---
entry_id: decision-log
axis: style
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Decision Log on: Choosing between Postgres and DynamoDB

# Decision: Notification System Primary Storage

**Status:** Decided
**Date:** 2026-05-15
**Owner:** Ana Velasquez (Tech Lead, Notifications)
**Stakeholders:** Marcus Chen (Senior Eng, prototype owner); Priya Singh (PM); 4-person on-call rotation
**Forum:** Architecture meeting, Wednesday 2026-05-13 2pm Pacific

## Context

Lattice Notify is a 50-person Series B with 8 backend engineers. The product currently runs as a monolith on Postgres. We are building a real-time notification system that needs new persistent storage. Launch volume is projected at 500K events/day. The CRO assigned 60% confidence on Friday 2026-05-08 to a Slack-partnership deal closing in Q3 2026; if it lands, volume reaches roughly 5M events/day in twelve months.

Priya set a Friday 2026-05-15 deadline so the team can plan the next sprint. The on-call rotation is four engineers, none of whom have operated DynamoDB in production. Ana has scaled Postgres to this range before in a prior role; Marcus has prototyped on DynamoDB but not operated it.

The cost of being wrong: roughly 3-6 weeks of rework if a migration is forced later. The cost of being right: roughly a year of stability on the chosen storage path.

## Options Considered

### Option A: Postgres with a queue

Reuse the existing Postgres cluster, add a notifications schema, put a queue (likely SQS) in front to absorb write spikes. Known operational profile. Sharding required in the 10x scenario, but reversible.

### Option B: DynamoDB

Stand up a new DynamoDB table for notifications. Natural fit for the write-heavy, key-lookup, time-ordered access pattern. Scales transparently in the 10x scenario. Adds a second storage system the team has never operated. Cross-database queries to existing Postgres tables move into application code.

### Option C: Postgres now, plan a Dynamo migration if and when the Slack deal closes

Hybrid. Defers the new-system learning curve until the volume actually arrives. Accepts a 3-6 week migration project in the future as an explicit, scheduled cost.

## Criteria

In priority order:

1. **Operational safety for the on-call rotation.** A four-person rotation cannot be on-call for two storage systems they cannot debug.
2. **Cost of being wrong.** Recoverable errors are preferred over diffuse, hard-to-roll-back errors.
3. **Fit to the launch-day access pattern at 500K events/day.**
4. **Fit to the 10x scenario, weighted by the probability of that scenario.**
5. **Cross-system query cost** with billing, analytics, and product reads that live in Postgres.

## Decision

**Adopt Option C: ship on Postgres with a queue. Pre-commit to a Dynamo migration project if and when the Slack deal closes.**

Specifics:

- Notifications schema lands in the existing Postgres cluster behind an SQS queue. Marcus owns the schema design and queue integration. Target: in production by 2026-06-15.
- A trigger condition is defined now, not later: if Slack-partnership volume puts us above 2M events/day on a 30-day rolling average, the Dynamo migration project begins the following sprint. Owner: Ana.
- The Dynamo design Marcus prototyped this week is preserved in the design-docs repo with a status of "deferred design, ready to revive."
- The 4-person on-call rotation does not take on a second storage system at launch.

## Reasoning

Option C scores best on criteria 1, 2, and 3. It scores worst on criterion 4 if the Slack deal lands, but the pre-committed trigger condition converts that worst case into a scheduled project rather than an emergency. Option B scores best on criterion 4 but worst on criterion 1, and the team agreed that operational safety for the on-call rotation was the right load-bearing constraint. Option A and Option C are structurally similar; the addition of the explicit trigger condition is what makes Option C honest rather than wishful.

The deciding factor was the recognition (Ana, in the Wednesday meeting) that the decision was really about how much we believe the Slack deal will close. At 60% confidence, the expected operational cost of running on Dynamo from day one is higher than the expected migration cost of moving to Dynamo later.

## Open Questions

- Exact trigger threshold for the Dynamo migration: 2M events/day on a 30-day rolling average is the starting number; revisit at the 2026-Q3 architecture review with real volume data.
- Should the SQS queue be replaced with the existing internal event bus? Defer to Marcus's schema design review.
- Who owns the Dynamo runbook drafting if the trigger fires? Owner unassigned; revisit when the Slack deal closes.
