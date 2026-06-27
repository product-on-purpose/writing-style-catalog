---
entry_id: faq
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## Frequently Asked Questions: Notification Service Datastore (ADR-0023)

### Why did we choose Postgres instead of DynamoDB?

The decision came down to operational capacity. We have a 4-person on-call rotation and adding a second datastore means a second runbook, a second monitoring surface, and a second debugging skillset on every page. The architecture meeting on Wednesday concluded that this cost outweighed DynamoDB's access-pattern advantage at launch scale (500K events/day). ADR-0023 records the full reasoning.

### Doesn't DynamoDB actually fit the notification access pattern better?

Yes - and Marcus's argument holds in isolation. The notification workload is write-heavy with point-lookups by user, which DynamoDB handles natively. We accepted the worse access-pattern fit in exchange for a better fit for the team's operational reality and for the certain launch scenario rather than the uncertain 10x growth scenario that depends on a deal that has not yet closed.

### What does the Postgres setup actually look like?

A new `notifications` schema in the existing primary cluster, a `pg_notify`-backed job queue, and a `notification_jobs` table. Read replicas absorb fanout reads. The service sits entirely within the existing operational footprint - no new cluster, no new backup story, no new monitoring surface for on-call.

### How do cross-database queries work?

They stay as standard SQL joins. Because the `notifications` schema lives in the same primary cluster as the existing monolith data, joining notifications to users, accounts, and workspaces requires no cross-service lookup or API call. This was a secondary argument for Postgres that would not hold with DynamoDB.

### What's the plan when we outgrow Postgres?

ADR-0023 defines a revisit threshold of 5M events/day sustained. When write rate crosses that level, the team evaluates DynamoDB migration before scaling the Postgres path further. Jordan adds queue depth and write rate to the on-call dashboard by 2026-05-22 so the team tracks the approach to that threshold continuously.

### What if the Slack-partnership deal closes and growth arrives ahead of schedule?

This is a known, low-severity risk. Priya tracks deal timing in the partnership review cadence and gives the team 30 days of warning before volume impact arrives. That triggers the 5M events/day revisit early, not as an emergency. Both Postgres and DynamoDB carry an estimated 3-6 week rework window if a migration is needed, so neither choice is a trap.

### Who owns the decision going forward?

Ana owns the Postgres partitioning work scheduled for Q4 if growth tracks projection. Jordan owns the on-call dashboard threshold metric. Priya holds the ADR-0023 record and the sprint planning commitment from Friday. For questions about the decision rationale, see ADR-0023 or reach Ana directly.
