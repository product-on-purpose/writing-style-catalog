---
entry_id: postmortem
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Postmortem: Notification Queue Backlog - notification-service-prod (2026-05-29)

## Severity

SEV-3

## Summary

On 2026-05-29, the `notification_jobs` worker queue on the Postgres-backed notification service backed up for approximately 6 hours during the first internal traffic window. Notification delivery for internal users was delayed by up to 4 hours and 12 minutes. The proximate trigger was a bulk account import that spiked event volume above what the 4-worker pool could drain. The underlying condition was an alert threshold left at a placeholder value of `0`, which meant the queue depth was invisible to the on-call rotation until Marcus noticed missing notifications manually.

## Timeline

- 09:00 UTC - First internal traffic enabled on notification-service-prod per the 2026-05-29 go-live plan; baseline write rate approximately 140 events/min
- 11:23 UTC - Sam's bulk account import script runs as part of internal testing; notification volume spikes to approximately 1,100 events/min
- 11:27 UTC - `notification_jobs` worker pool falls behind; queue depth begins growing at roughly 950 jobs/min
- 11:28 UTC - Queue depth alert is expected to fire at 5,000 queued jobs; PagerDuty threshold is set to the placeholder value `0` and does not fire
- 13:45 UTC - Queue depth crosses 140,000 jobs; no alert has fired
- 15:37 UTC - Marcus notices in-app notifications are not arriving during manual smoke testing; queries `notification_jobs` directly and sees the backlog
- 15:42 UTC - Marcus pages Ana; Ana joins the incident channel
- 15:49 UTC - Ana scales the worker pool from 4 to 20 workers
- 16:11 UTC - Queue depth peaks at approximately 191,000 jobs and begins draining
- 17:39 UTC - Queue fully drained; delivery delay for the oldest pending notifications is 4 hours 12 minutes
- 17:52 UTC - Postmortem initiated

## Root Cause

The `notification_jobs` alert threshold was never validated before first traffic. Jordan delivered the queue depth and write rate dashboard on 2026-05-22 as planned, but the PagerDuty alert was left at a placeholder threshold of `0` queued jobs. That value never fires: a healthy worker pool always drains faster than jobs arrive, so the queue depth stays near zero under normal load and the alert condition is never met. No go-live checklist required explicit confirmation that alert thresholds had been set to non-placeholder values before traffic was enabled. When the import spike pushed volume above the worker pool's drain rate, the backlog grew for over 4 hours without triggering any automated notification. The condition was discovered only when a team member noticed missing notifications by hand and queried the table directly.

## Impact

- Users affected: Internal team only (8-person team and internal test accounts); no external users were on the service at the time
- Duration: 11:27 UTC to 17:39 UTC (6 hours 12 minutes total incident window; max delivery delay 4 hours 12 minutes)
- Services affected: notification-service-prod, in-app and email delivery channels; Slack delivery was not yet configured

## Contributing Factors

- The go-live plan had no step requiring alert thresholds to be confirmed against non-placeholder values before traffic was enabled
- The `notification_jobs` table had no dead-letter queue; failed retries consumed worker capacity alongside the growing backlog and slowed drain
- Worker pool size (4 workers) was not tuned against the import-triggered spike scenario; the bulk import was a known internal testing step but its notification volume was not estimated in advance
- The runbook (docs/runbook.md) documented queue depth as an alertable metric but did not specify who was responsible for threshold sign-off before go-live

## Action Items

- [ ] Set the queue depth PagerDuty alert threshold to 10,000 jobs and confirm the alert fires in staging before any future go-live step - Owner: Jordan - Due: 2026-06-05
- [ ] Add a dead-letter queue to `notification_jobs`; implement a max-retry cap of 5 per job before routing to DLQ - Owner: Sam - Due: 2026-06-09
- [ ] Add a pre-traffic readiness section to docs/runbook.md; include alert threshold validation as a required, signed-off item before enabling each traffic tier - Owner: Ana - Due: 2026-06-05
- [ ] Document expected peak notification volume for all planned internal testing scripts; confirm worker pool count against that estimate before each test run - Owner: Sam - Due: 2026-06-09
- [ ] Review the 5M events/day revisit threshold metric with Priya now that baseline write-rate data is available; confirm the metric is landing in the on-call dashboard with a valid alert threshold - Owner: Jordan - Due: 2026-06-12

## Lessons Learned

A placeholder alert threshold is operationally invisible. Delivering the dashboard on schedule is a necessary condition but not a sufficient one: the alert threshold and its validation against a real scenario must be a separate deliverable with its own owner and due date. The go-live plan owned the date; the runbook owned the procedure; neither owned the alert configuration sign-off, so it fell through the gap between them.

One observation worth recording in favor of the Postgres choice: Marcus identified the root cause in under 10 minutes by querying `notification_jobs` directly with a single SQL statement. That access would not have been available under the DynamoDB path considered in ADR-0023. Direct table inspection shortened the response window and gave the team immediate confidence that the backlog was the only problem.
