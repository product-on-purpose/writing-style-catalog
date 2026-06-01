---
entry_id: problem-solution
axis: style
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Problem-Solution on: Choosing between Postgres and DynamoDB

### The problem

Lattice Notify needs to commit to a storage choice for the new notification system by Friday so the team can plan next sprint, and the team is stuck. Ana (tech lead) wants Postgres because the eight-engineer backend team has shipped at the 500K-events-per-day launch volume on Postgres before and the four-person on-call rotation can debug it cold at 3am. Marcus (senior engineer) wants DynamoDB because the access pattern is write-heavy, key-lookup, and time-ordered, and because the 10x growth scenario tied to the Slack-partnership deal would force a Postgres sharding project the team has never done.

The standoff is not a personality conflict; it is a real structural disagreement about what the decision is optimizing for. The current state is that the architecture meeting Wednesday 2pm Pacific has been on the calendar for ten days, two thoughtful engineers have produced credible analyses in opposite directions, Priya has reset the deadline twice already, and the team is now four days from sprint planning with no committable answer. Getting this wrong costs 3-6 weeks of rework if a migration is forced. Getting it right gives the notifications team a year of stability on a foundation that will not need to be replaced. The cost of further indecision is concrete: every day past Friday delays the notification launch by a day.

### The solution

Ship the notification system on Postgres with a queue, and pre-commit to a binding trigger condition that fires a planned migration to DynamoDB if real volume crosses 2M events/day on a 30-day rolling average. This addresses the specific problem named because it resolves the actual disagreement: Ana's concern about operational safety for the four-person rotation is honored at launch, and Marcus's concern about the 10x scenario is converted from a projection-driven argument into a measurable trigger that fires on real data.

The execution: Ana owns the Postgres schema and the queue integration for a 2026-06-15 production target. Marcus's prototype Dynamo schema is preserved in the design-docs repo with the status "deferred design, ready to revive," not deleted, not productionized. Priya owns the quarterly volume review against the 2M events/day threshold starting 2026-Q3. The on-call rotation stays at four engineers on one storage system at launch; if the trigger fires, the rotation is revisited before the second storage system goes live.

The decision survives the load-bearing critique from each side. From Ana's side: the team is not committing now to operating DynamoDB; the commitment is only to revisit when volume demands it. From Marcus's side: the team is not pretending the 10x scenario will not happen; the trigger is binding and tied to real data rather than to hope. The 60% Slack-deal probability from the CRO is what makes this trade rational rather than evasive: at 60%, the expected cost of running two storage systems for a year is higher than the expected cost of a scheduled migration if the high-volume scenario materializes.

### Before and after

Before: two engineers in disagreement, a PM resetting deadlines, a four-day countdown to sprint planning with no decision, and a meeting on Wednesday with no path to convergence. After: a recommendation circulated 24 hours before the meeting, the meeting ratifying the path, the decision committed to the engineering channel Friday morning, sprint planning running Friday afternoon against concrete tasks, and a trigger condition that converts the unresolved future into a managed contingency.

This is the path. Run it.
