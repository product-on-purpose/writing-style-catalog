---
entry_id: memo
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

TO: Lattice Notify Engineering
FROM: Ana Rivera, Tech Lead, Notification Service
DATE: 2026-05-16
RE: Notification Service datastore - Postgres selected over DynamoDB (ADR-0023 accepted)

The Notification Service will run on Postgres, not DynamoDB. The 11am sync with Priya today locked the decision that came out of Wednesday's architecture meeting, and ADR-0023 is now accepted. This memo puts that decision on record for the engineering org.

The service launches at 500K notification events per day, with a possible 10x growth scenario in 12 months if the pending Slack-partnership deal closes. Two options were evaluated: extend the existing Postgres footprint with a new schema and job queue, or adopt DynamoDB for its native fit to a write-heavy, point-lookup access pattern. Marcus's case for DynamoDB on access-pattern grounds was sound and is recorded in full in ADR-0023. The deciding factor was operational capacity, not access-pattern fit: an 8-person backend team on a 4-person on-call rotation absorbs a second production database as a second runbook, a second monitoring surface, a second backup story, and a second debugging skillset on every page, regardless of which system fits the workload better. The 10x growth case is not yet certain, since it depends on a deal that has not closed, so the launch architecture is sized for the load we know rather than the load we are hoping for.

Both paths were reversible at roughly similar cost, so reversibility did not decide this; operational load did. The Postgres tuning that arrives at the 10x mark - partitioning the notifications table, tuning the job queue, possibly sharding - is real work, and it is on the roadmap rather than avoided by this choice.

The build is already underway under this decision. The `notifications` schema and `notification_jobs` table sit in the existing primary Postgres cluster, with `pg_notify` driving the job queue and read replicas absorbing fanout reads. Sam's schema and table spec are due 2026-05-20; Jordan's queue-depth and write-rate additions to the on-call dashboard are due 2026-05-22; first end-to-end internal traffic on the Postgres path is targeted for 2026-05-29. Sprint planning this afternoon commits the first two weeks against this plan.

This memo establishes Postgres, under the schema and job-queue design above, as the system of record for the Notification Service datastore. ADR-0023 carries the full context, the alternatives considered, and the consequences accepted; this memo is the standing engineering-wide notice that the decision is closed. The datastore choice will be revisited only if sustained volume crosses the documented 5M events/day threshold. Until then, it stands.
