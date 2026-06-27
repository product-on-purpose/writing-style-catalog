---
entry_id: rfc
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# RFC-0041: Datastore Selection for the Lattice Notify Notification Service

## Status

Under Review

## Author(s)

Ana Rivera, 2026-05-12

## Problem

Lattice Notify is building a notification service from scratch and needs a persistent datastore before we can begin the build sprint. The service will handle an estimated 500K notification events per day at launch - a write-heavy workload with point-lookups by user_id for delivery and fanout reads for inbox hydration. Two candidates are on the table: extend the existing Postgres cluster into a new `notifications` schema, or adopt DynamoDB for a closer access-pattern fit.

Both options have real advocates on the team. Marcus ran a DynamoDB spike this week (`experiments/notify-ddb/`) that confirmed it handles the access pattern well. The operational question is less settled. We need to align before Wednesday's architecture meeting so sprint planning on Friday starts from a locked decision, not an open one.

The question is not which database is better in the abstract. It is which database fits the team's operational reality, given that the growth scenario that most favors DynamoDB has not materialized yet.

## Proposed Approach

Build the notification service on Postgres, using a new `notifications` schema in the existing primary cluster with a `pg_notify` + `notification_jobs` table job queue. Provision read replicas to absorb fanout reads. Document a revisit threshold at 5M events/day sustained, at which the team evaluates a DynamoDB migration before scaling the Postgres path further.

Rationale:

**Operational familiarity is load-bearing.** The 4-person on-call rotation has existing runbooks, monitoring, and debugging experience on Postgres. Adding a second datastore adds a second runbook, a second monitoring surface, and a second set of debugging skills needed on-call. We have measured this cost in a prior workstream and it is not small.

**The growth scenario driving the DynamoDB argument is uncertain.** The 10x projection at 12 months depends on the Slack-partnership deal closing. Designing for a scenario that has not arrived, at the cost of operational complexity that lands immediately, seems like the wrong trade.

**The asymmetry of reversibility is smaller than it looks.** If we choose Postgres and outgrow it, the rework is 3-6 weeks. If we choose DynamoDB and find we need cross-database joins for product features, the rework is similar in size, plus we have built operational muscle on a platform we may not keep. Neither choice is a trap; both are recoverable.

**Cross-database queries stay simple.** Joining notifications to users, accounts, and workspaces is a real product requirement. On Postgres, that is SQL. On DynamoDB, it moves to the application layer.

## Alternatives Considered

**DynamoDB.** The access-pattern argument is real. Marcus's spike confirmed DynamoDB handles write-heavy, point-lookup-by-user workloads well, which is exactly our pattern. My counterargument is not that DynamoDB is wrong in principle - it is that the team has no production DynamoDB experience, no existing runbook, and the on-call rotation absorbs a new surface at launch. I would weight the access-pattern argument more heavily if the growth projection were certain. It is not.

**Postgres on a dedicated cluster.** Rather than sharing the monolith cluster, we could provision a separate Postgres instance to avoid coupling. I do not recommend this now. It adds the same operational complexity as a new datastore (a cluster to provision, monitor, and operate) without the access-pattern benefit. Worth revisiting at the 5M events/day threshold if we decide to isolate the service.

**In-process queue with no persistent store.** Rejected early in the spike. The notification service needs durability and a replay path for delivery failures. An in-process queue has no recovery story if the service restarts.

## Open Questions

1. **Revisit threshold definition.** I have proposed 5M events/day as the migration trigger. Is that the right signal, or should the threshold be tied to a latency metric like p99 write latency or queue drain time? Marcus, your spike gave you the closest read on where DynamoDB starts outperforming Postgres for this workload - would a throughput threshold miss early warning signs?

2. **Cross-database join requirements in H2.** My assumption is that joining notifications to users and workspaces will be a product requirement within 6 months. If that assumption is wrong, the access-pattern argument for DynamoDB gets stronger and I want to revisit this proposal. Priya, can you confirm whether the notification-to-workspace join is in the H2 product roadmap?

3. **Read replica lag tolerance.** The fanout read path will hit read replicas. Is replica lag acceptable for the notification inbox - that is, can a user see their notifications a few seconds after generation - or does the product behavior require immediate consistency? This affects whether read replicas are sufficient or whether we need a different read architecture on the Postgres path.

4. **On-call cost quantification.** I have described the second-datastore operational cost as non-trivial but have not expressed it in concrete terms. Jordan, is there a way to frame this in the decision record - hours per incident, runbook pages, something that gives the argument more weight than my prior experience?

## Consequences

**If this proposal is accepted:**

- The notification service ships on familiar operational ground. Based on the team's past migration work, the Postgres path is estimated to be 3 weeks faster to first production traffic than the DynamoDB path.
- Single operational surface for the on-call rotation. Existing monitoring and runbooks apply. No new debugging context needed at 2am.
- Cross-database queries stay SQL. No application-layer join logic introduced at launch.
- Known future work lands on the roadmap, not in a drawer: Postgres partitioning and job queue tuning at the 3-5M events/day range. Ana owns this; it is currently projected for Q4 if growth tracks.
- The decision is recoverable. If the Slack-partnership deal closes and growth accelerates faster than the 12-month projection, the 5M events/day threshold gives the team a planned migration window with 30-day notice from Priya.

**If this proposal is rejected in favor of DynamoDB:**

- Access-pattern fit improves at the cost of operational unfamiliarity. The first 6 months on-call will have a steeper learning curve.
- A rollback plan is needed before the service reaches production. There is not one yet.
- Cross-database join logic moves to the application layer. This will surface as product complexity when the notification-to-workspace requirement lands.
