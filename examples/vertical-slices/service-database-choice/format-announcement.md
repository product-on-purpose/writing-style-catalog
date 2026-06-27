---
entry_id: announcement
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

**Subject: Notification Service datastore decision locked - Postgres (ADR-0023 accepted)**

The notification service will run on Postgres. We locked the decision in the 11am Friday sync with Priya; ADR-0023 is now accepted.

For the team building and operating this service, here is what that means: the new `notifications` schema lands in the existing primary cluster, backed by a `pg_notify` job queue and a `notification_jobs` table. The 4-person on-call rotation stays on a single stack. No new runbooks, no new monitoring surface, no new debugging skillset on call.

The 5M events/day mark is the revisit threshold per ADR-0023. When we hit it, we evaluate a DynamoDB migration before scaling the Postgres path further. Until then, Jordan will have queue depth and write rate on the on-call dashboard by 2026-05-22 so we can track it.

The immediate next steps:

- Sam delivers the `notifications` schema and `notification_jobs` table spec by 2026-05-20.
- Jordan adds queue depth and write rate to the on-call dashboard by 2026-05-22.
- Target for first end-to-end internal traffic on the Postgres path: 2026-05-29.

Sprint planning starts today at 2pm. Read ADR-0023 before you arrive: `docs/adr/0023-postgres-notification-service.md`. Questions go to #notify-arch.
