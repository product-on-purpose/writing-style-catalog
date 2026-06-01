---
entry_id: meeting-notes
axis: format
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

# Meeting Notes - Notification Service Datastore Decision

**Date:** 2026-05-13
**Time:** 2:00pm - 3:15pm Pacific
**Attendees:** Ana Rivera (tech lead), Marcus Chen (senior eng), Priya Shah (PM), Jordan Patel (on-call lead), Sam Okafor (backend eng)
**Absent:** Two backend engineers off-cycle this week (notes shared via #notify-arch)

## Decisions

- Lattice Notify will build the new notification service on Postgres, extending the existing primary cluster with a `notifications` schema and a `pg_notify`-backed job queue. DynamoDB option declined for this release.
- A revisit threshold of 5M events/day sustained is set; crossing it triggers a new decision review, not an automatic migration.
- Ana owns drafting ADR-0023 to record the decision and rationale; Marcus has explicit sign-off on the revisit threshold language.
- Decision will be locked at the Ana-Priya 11am sync on Friday 2026-05-16 so sprint planning at 2pm Friday can proceed on the Postgres assumption.
- DynamoDB spike work moves to `experiments/notify-ddb/` and is deprecated; no production code depends on it.

## Actions

- [ ] Draft ADR-0023 (Postgres for notification service) - owner: Ana - due: 2026-05-15 EOD
- [ ] Review and approve ADR-0023 revisit threshold language - owner: Marcus - due: 2026-05-15 EOD
- [ ] Lock decision in 11am sync, confirm sprint plan - owner: Priya - due: 2026-05-16
- [ ] Spec out `notifications` schema and `notification_jobs` table - owner: Sam - due: 2026-05-20
- [ ] Add `notifications.write_rate` and queue depth to the on-call dashboard - owner: Jordan - due: 2026-05-22
- [ ] Announce decision in Friday all-hands engineering update - owner: Ana - due: 2026-05-16
- [ ] Archive DynamoDB spike to `experiments/notify-ddb/` with README explaining context - owner: Marcus - due: 2026-05-19

## Open Items / Parking Lot

- Whether to provision dedicated read replicas now or after first production traffic - owner: Ana, to be resolved in sprint planning
- Long-term partitioning strategy for the `notifications` table at the 3M events/day mark - owner: Ana, parked until growth data is available
- Whether to revisit the decision if the Slack deal closes faster than expected - owner: Priya, will track in the partnership review cadence

## Context

The team evaluated Postgres vs DynamoDB for a new real-time notification service expected to handle 500K events/day at launch with a potential 10x growth scenario in 12 months tied to a pending Slack-partnership deal. The decision turned primarily on operational capacity (8 backend engineers, 4-person on-call rotation, deep Postgres operational knowledge, no production DynamoDB experience) rather than on access-pattern fit. The team has 3-6 weeks of rework as the recovery cost if Postgres becomes the wrong choice, which the room considered acceptable given the predictability of that recovery.
