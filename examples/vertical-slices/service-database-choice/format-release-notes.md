---
entry_id: release-notes
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# notification-service v0.1.0 - May 16, 2026

## Initial launch: notification delivery for Lattice Notify

## What's new

- **Multi-channel delivery**: You can now send in-app, email, and Slack push notifications through a single `NotifyClient` call. Specify the channel, template, and payload; the service handles delivery and writes the event to the `notifications` schema. Notifications reach users in under one second at p95.

- **Template-based dispatch**: Notification copy is managed centrally. Your service sends a template name (for example, `comment_mention`) and a structured payload; you do not own the notification text. This keeps copy changes out of your deployment cycle.

- **Built-in job queue**: All delivery is queued through `notification_jobs` using `pg_notify`, so your call returns as soon as the event is written. No fire-and-forget HTTP requests and no manual retry logic on your side.

## Known issues

- **Capacity ceiling at launch**: The service is sized for 500K notification events per day. Integrations expected to send above that rate should coordinate with Ana before going live. A formal revisit threshold is defined at 5M events/day in ADR-0023 and is tracked on the on-call dashboard.

- **No batching for bulk fan-out**: High-volume workspace broadcasts are queued as individual jobs. Rate-shape bulk dispatches on the caller side; see the operational runbook for recommended patterns.

## Deprecations and breaking changes

None. This is the initial release.
