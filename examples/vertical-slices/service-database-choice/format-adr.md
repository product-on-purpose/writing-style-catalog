---
entry_id: adr
axis: format
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

# ADR-0023: Use Postgres for the Notification Service

## Status

Accepted

## Context

Lattice Notify is launching a real-time notification system that needs a new persistent data store. The system will handle 500K notification events per day at launch, with a 10x growth scenario in 12 months if the pending Slack-partnership deal closes. The decision sits between two candidates:

- **Option A: Postgres.** Extend the existing Postgres footprint with a new schema, add a job queue, and absorb the resulting scaling work. The team has operated Postgres at this scale before. Cross-database queries against the existing monolith data stay simple.
- **Option B: DynamoDB.** Adopt a new datastore that fits the notification access pattern (write-heavy, point-lookups by user) and scales without operator intervention. The team has no production DynamoDB experience. Ops surface area doubles. There is no rollback plan if it goes wrong.

Three forces pushed this decision:

**Team operational capacity.** We have 8 backend engineers and a 4-person on-call rotation. Adding a second database adds a second runbook, a second monitoring surface, a second backup story, and a second debugging skillset on every page. We have measured this cost before in a separate workstream and it is non-trivial.

**Growth uncertainty.** The 10x growth scenario depends on a deal that has not closed. Designing the system for the larger scenario, when the smaller one is the certain one, optimizes for the case that may not arrive.

**Reversibility cost.** If we choose Postgres and outgrow it, we incur 3-6 weeks of rework to migrate. If we choose DynamoDB and find we need cross-database joins for product features, we incur similar rework plus a team that has learned the wrong tool. The asymmetry is small; both choices are recoverable.

Marcus made a strong case for DynamoDB's access-pattern fit. Ana raised the operational capacity concern. The architecture meeting on Wednesday confirmed that the operational concern is the load-bearing one.

## Decision

Build the notification service on Postgres, using a new schema (`notifications`) in the existing primary cluster and a job queue backed by `pg_notify` plus a `notification_jobs` table. Provision read replicas to absorb fanout reads. Add a documented threshold (5M events/day sustained) at which we revisit DynamoDB before scaling the Postgres path further.

Priya has the decision recorded for the Friday sprint planning.

## Consequences

### Positive

- Single operational surface for the 4-person on-call rotation. No new runbooks, no new monitoring, no new debugging skillset on call.
- Cross-database queries (joining notifications to users, accounts, workspaces) remain simple SQL.
- The team ships the launch scope on familiar ground. Estimated 3 weeks faster to first production traffic than the DynamoDB path.
- The decision is reversible: if we cross the 5M events/day threshold, we have the data and the operational margin to plan a migration.

### Negative

- We will likely need to do non-trivial Postgres tuning at the 10x growth point: partitioning the notifications table, tuning the job queue, possibly sharding. This work is real and is on the roadmap, not avoided.
- Marcus's argument about access-pattern fit is correct in isolation; we are accepting a worse fit for the access pattern in exchange for a better fit for the team's operational reality.
- If the Slack deal closes and growth arrives faster than 12 months, we hit the rework window earlier than planned.

### Neutral

- The `notification_jobs` table becomes a new operational concern: queue depth, dead-letter handling, retry policy. These are familiar problems on a familiar platform.
- The 5M events/day revisit threshold becomes a tracked metric. The on-call rotation owns the dashboard.
