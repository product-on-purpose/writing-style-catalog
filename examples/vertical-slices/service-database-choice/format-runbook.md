---
entry_id: runbook
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Provision Postgres for the Notification Service (ADR-0023)

## Overview

This runbook provisions the `notifications` schema and `notification_jobs` table in the existing primary Postgres cluster for Lattice Notify; trigger when preparing for first end-to-end traffic or after a full datastore teardown.

## Prerequisites

- [ ] ADR-0023 is in Accepted status - confirm with Ana Rivera before starting
- [ ] Write access to the primary Postgres cluster (`pg-primary.latticenotify.internal`)
- [ ] `psql` available locally with credentials to the `latticenotify` database
- [ ] Migration tool (`make db-migrate`) confirmed working in staging
- [ ] Schema spec (`migrations/0001_notifications_schema.sql`) reviewed and approved by Ana
- [ ] Read replica listed as Available in the cluster admin panel

## Procedure

1. **Verify cluster access**
   Run: `psql -h pg-primary.latticenotify.internal -U notify_admin -d latticenotify -c "SELECT version();"`
   Expected output: A Postgres version string. If the connection is refused, stop here and contact Ana Rivera before continuing.

2. **Apply the notifications schema migration**
   Run: `make db-migrate ENV=production MIGRATION=0001_notifications_schema`
   Expected output: `Migration 0001_notifications_schema applied. 1 schema created (notifications).`

3. **Confirm schema creation**
   Run: `psql -h pg-primary.latticenotify.internal -U notify_admin -d latticenotify -c "\dn notifications"`
   Expected output: A single row listing the `notifications` schema. If no row appears, do not continue - run the rollback and contact Ana.

4. **Apply the notification_jobs table migration**
   Run: `make db-migrate ENV=production MIGRATION=0002_notification_jobs_table`
   Expected output: `Migration 0002_notification_jobs_table applied. 2 tables created (notifications.events, notifications.notification_jobs).`

5. **Enable pg_notify on the notification_jobs table**
   Run: `make db-migrate ENV=production MIGRATION=0003_pg_notify_trigger`
   Expected output: `Migration 0003_pg_notify_trigger applied. 1 trigger created (notify_on_job_insert).`

6. **Confirm the read replica has replicated the schema**
   Run: `psql -h pg-replica.latticenotify.internal -U notify_read -d latticenotify -c "SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'notifications';"`
   Expected output: One row containing `notifications`. If the schema is absent after 60 seconds, stop and contact Jordan - do not proceed to step 7.

7. **Grant service account permissions**
   Run: `make db-grant ENV=production ROLE=notify_service SCHEMA=notifications`
   Expected output: `GRANT executed. Role notify_service has INSERT, SELECT, UPDATE on notifications.*`

8. **Seed the retry policy defaults**
   Run: `make db-seed ENV=production SEED=notification_jobs_defaults`
   Expected output: `Seed applied. 3 rows inserted into notifications.notification_jobs_config.`

## Verification

Confirm end-to-end queue delivery by running the smoke test:

1. Run: `make notify-smoke ENV=production`
2. Expected output: `Smoke test PASSED. 1 event written, 1 event picked up by worker pool, 0 errors.`

Confirm the on-call dashboard is populated:

- Open `https://dashboard.latticenotify.internal/notify-service`
- Confirm the `notification_jobs queue depth` panel shows a numeric value (0 is correct for a fresh install)
- Confirm the `write rate (events/day)` panel is visible - Jordan is the owner if this panel is missing

## Rollback

If any Procedure step fails and you cannot continue:

1. Run: `make db-rollback ENV=production SCHEMA=notifications`
   Expected output: `Rollback complete. Schema notifications dropped.`

2. Post to #notify-service with the step number where the failure occurred and the full error output. Copy Ana Rivera directly.

Do not attempt to drop individual tables manually. The schema-level rollback handles cascades. If the rollback script itself fails, stop all work and escalate immediately.

## Escalation

- **Production incidents:** Page via PagerDuty service `notification-service-prod`
- **Tech lead:** Ana Rivera - direct Slack or #notify-service
- **Schema owner:** Sam - contact if migration files are missing or contain unexpected changes
- **On-call dashboard:** Jordan - contact if the read replica check (step 6) or dashboard verification fails
