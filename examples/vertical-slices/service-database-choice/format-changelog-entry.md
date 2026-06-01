---
entry_id: changelog-entry
axis: format
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

# CHANGELOG - notification-service

## [0.1.0] - 2026-05-22

First internal release of the Lattice Notify real-time notification service. Datastore selection (Postgres vs DynamoDB) was concluded at the Wednesday 2026-05-13 architecture meeting; the Friday sprint plan is built on this release.

### Added

- Notification storage backed by Postgres (`notifications` schema in the primary cluster) (#142)
- Job queue using `pg_notify` plus a `notification_jobs` table for fanout work (#143)
- Read replica routing for fanout reads to absorb the 500K events/day launch load (#144)
- Datastore decision recorded in ADR-0023 with a 5M events/day revisit threshold (#145)
- Dashboard for `notifications.write_rate`, `notification_jobs.queue_depth`, and replica lag (#146)
- On-call runbook section for notification-service incidents, owned by the 4-person rotation (#147)

### Changed

- Sprint plan for 2026-05-25 week reorganized around the Postgres path; previous DynamoDB spike work archived under `spikes/dynamodb-2026-05/` (#148)
- Capacity-planning doc updated to reflect Postgres-only scaling milestones (#149)

### Deprecated

- DynamoDB spike code in `experiments/notify-ddb/` deprecated; will be removed in 0.3.0 once the Postgres path has 30 days of clean production data. Migration note: no production traffic ever ran on this path, no data migration is required (#150)

### Removed

- The temporary in-memory notification buffer used during the spike phase is removed; all writes now go through the Postgres path (#151)

### Fixed

- Fixed a race condition in the spike-era fanout logic where two replicas could double-deliver the same notification under load (#152)
- Fixed missing index on `notification_jobs.created_at` that caused queue-drain queries to fall back to sequential scan (#153)

### Security

- All notification payloads encrypted at rest via existing Postgres TDE configuration; no additional KMS surface introduced (#154)
- New on-call playbook step requires confirming PII redaction in notification logs before any debug export (#155)
