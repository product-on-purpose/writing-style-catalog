---
entry_id: incident-report
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Incident Report: Notification Service - Delayed Delivery (INC-0047)

## Status

Resolved - 2026-06-03, 4:42 PM UTC

## Summary

On June 3, 2026, Lattice Notify's notification service experienced delayed delivery of in-app, email, and Slack push notifications for approximately 2 hours and 20 minutes. Notifications were not lost; they were queued and delivered after service was restored.

## Impact

- Services affected: in-app notifications, email delivery, Slack push notifications
- Customers affected: all active workspaces on the Lattice Notify platform
- Duration: 2:17 PM UTC to 4:37 PM UTC (approximately 2 hours 20 minutes)

## Timeline

- 2:17 PM UTC - Notification delivery latency begins rising; p95 latency exceeds 5 seconds
- 2:24 PM UTC - On-call alert fires; investigation begins
- 2:41 PM UTC - Root cause identified: the notification queue database was accepting more simultaneous operations than it was configured to handle
- 3:05 PM UTC - First mitigation applied; delivery resumes at reduced throughput while a permanent fix is prepared
- 3:45 PM UTC - Configuration update applied; full throughput restored
- 4:37 PM UTC - Queued backlog cleared; all delayed notifications delivered
- 4:42 PM UTC - Incident declared resolved

## Root Cause

The notification service queues and delivers notification events through a shared database. During a period of elevated activity on June 3 - driven by a wave of workspace onboarding events that coincided with higher-than-usual user activity - the number of simultaneous database operations exceeded the configured limit. When that limit was reached, new notifications could not be accepted or dispatched; delivery stalled while events continued to arrive and accumulate in the queue.

The service was designed and sized for a launch volume of 500K notification events per day, and daily volume on June 3 was within that range. The elevated activity arrived in a concentrated hourly burst, temporarily exceeding the rate the service was configured to handle at a single point in time.

## Resolution

We reduced the number of simultaneous delivery workers to relieve immediate pressure on the database, which restored notification delivery at lower throughput. A configuration update raising the database operation limit was applied within the hour, returning the service to full throughput. The accumulated backlog of 14,200 queued notifications was cleared by 4:37 PM UTC. No notifications were lost or duplicated.

## Next Steps

- Raise the database concurrent-operation limit to accommodate 2x the observed peak hourly rate - owner: Jordan, target: 2026-06-10
- Add hourly write-rate monitoring to the on-call dashboard alongside the existing queue-depth alert - owner: Jordan, target: 2026-06-10
- Review launch capacity assumptions against observed onboarding traffic patterns to determine whether the daily event cap or the hourly rate is the more meaningful limit to track - owner: Ana, target: 2026-06-17
- Confirm whether the 5M events/day revisit threshold in ADR-0023 remains the right signal, or whether a concurrent-operation rate threshold should be added alongside it - owner: Ana and Marcus, target: 2026-06-24
