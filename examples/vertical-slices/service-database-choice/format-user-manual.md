---
entry_id: user-manual
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Notification Service User Manual

This manual covers everything you need to send notifications through the Lattice Notify notification service, manage templates, and monitor delivery. It documents the `notify-client` package as it exists today. For why the service runs on Postgres rather than DynamoDB, see ADR-0023.

## Table of Contents

- [Getting Started](#getting-started)
- [Sending Notifications](#sending-notifications)
  - [Send a single notification](#send-a-single-notification)
  - [Send to multiple users](#send-to-multiple-users)
  - [Choose a delivery channel](#choose-a-delivery-channel)
- [Managing Templates](#managing-templates)
  - [Register a template](#register-a-template)
  - [Preview a template](#preview-a-template)
- [Checking Delivery and Retries](#checking-delivery-and-retries)
  - [Check delivery status](#check-delivery-status)
  - [Configure retry behavior](#configure-retry-behavior)
- [Monitoring and Dashboards](#monitoring-and-dashboards)
  - [View the on-call dashboard](#view-the-on-call-dashboard)
- [Troubleshooting](#troubleshooting)
- [Reference](#reference)

## Getting Started

**Requirements:** Python 3.10 or later, network access to Lattice Notify's internal package index, and a `workspace_id` for the service you are sending on behalf of.

**Installation:**

```
pip install notify-client
```

**Get a workspace_id:** post in `#notify-service` with your service name. The on-call engineer provisions a `workspace_id` (format `ws_xxxxxx`) within one business day.

**First session:**

```python
from notify_client import NotifyClient

client = NotifyClient(workspace_id="ws_abc123")
client.ping()
```

`ping()` confirms your `workspace_id` is provisioned and the service is reachable. A successful call returns `True`.

If you are contributing to the notification service itself rather than sending notifications from another service, see the project README and the operational runbook instead of this manual.

## Sending Notifications

### Send a single notification

Delivers one notification to one user through the channel you specify.

Steps:
1. Import `NotifyClient` and instantiate it with your `workspace_id`.
2. Call `client.send()` with `user_id`, `channel`, `template`, and `payload`.
3. Store the returned `notification_id` if you plan to check delivery status later.

```python
result = client.send(
    user_id="usr_xyz789",
    channel="in_app",
    template="comment_mention",
    payload={"actor": "Marcus", "thread_id": "th_42"},
)
```

Options / Parameters:
- `user_id`: the Lattice Notify internal user ID of the recipient. Required.
- `channel`: `in_app`, `email`, or `slack`. Required. See Choose a delivery channel.
- `template`: the registered template name, for example `comment_mention`. Required.
- `payload`: a dict supplying the template's variables. Required keys vary by template; see Register a template.

Notes:
- The event is written to the `notifications` schema and picked up by the `notification_jobs` worker pool within approximately 50ms.
- In-app delivery lands in the user's inbox in under 1 second, matching the documented sub-second p95.
- `send()` raises `TemplateNotFoundError` if `template` is not registered and `WorkspaceNotFoundError` if `workspace_id` has not been provisioned.

### Send to multiple users

Delivers the same template and payload to a list of users in one call.

Steps:
1. Build a list of `user_id` values.
2. Call `client.send_batch()` with `user_ids`, `channel`, `template`, and `payload`.
3. Inspect the returned list of `notification_id` values, one per recipient.

Options / Parameters:
- `user_ids`: list of recipient IDs, limited to 500 per call.
- All other parameters match `send()`.

Notes:
- Batches larger than 500 users must be split by the caller; `send_batch()` does not auto-chunk.
- Each recipient still produces one row in `notification_jobs`; there is no separate batch table.

### Choose a delivery channel

Each channel has different payload requirements and delivery characteristics. Pick based on urgency and where the recipient will see it.

Steps:
1. Decide whether the notification should interrupt the user immediately (`in_app`), land in an inbox for later (`email`), or post to a team channel (`slack`).
2. Add the channel-specific payload fields listed below.
3. Pass the chosen channel as `channel` on `send()` or `send_batch()`.

Options / Parameters:
- `in_app`: fastest path, delivered to the in-app inbox, no extra payload fields required.
- `email`: requires a `subject` key in `payload`; uses the template's HTML layout.
- `slack`: requires a `slack_channel_id` key in `payload`; posts through the workspace's linked Slack app.

Notes:
- A workspace must have a Slack app linked before the `slack` channel accepts sends. Unlinked workspaces get `ChannelNotConfiguredError`.

## Managing Templates

### Register a template

Adds a new reusable message template that `send()` and `send_batch()` can reference by name.

Steps:
1. Add an entry to `templates/` with a lowercase, snake_case `name` (for example `comment_mention`), an `allowed_channels` list, and a `variables` list naming every placeholder the template body uses.
2. Open a pull request against the notification-service repository.
3. Get review from the on-call engineer in `#notify-service` before merging.

Options / Parameters:
- `name`: snake_case identifier, must be unique.
- `allowed_channels`: subset of `in_app`, `email`, `slack`.
- `variables`: list of variable names the template body references, for example `actor`, `thread_id`.

Notes:
- `send()` raises `PayloadMismatchError` if `payload` is missing a variable the template declares.
- Template registration takes effect on the next service deploy, not immediately on merge.

### Preview a template

Renders a template with sample data without sending it, useful for checking formatting before a template goes live.

Steps:
1. Call `client.preview(template=, payload=)` with a template name and a sample payload.
2. Read the rendered output for each channel listed in the template's `allowed_channels`.

Options / Parameters:
- `template`: the template name to preview.
- `payload`: sample values for every declared variable.

Notes:
- `preview()` does not write to `notification_jobs` and does not count against send volume.

## Checking Delivery and Retries

### Check delivery status

Looks up whether a specific notification was delivered, is still queued, or failed.

Steps:
1. Call `client.get_status(notification_id)` using the ID returned by `send()` or `send_batch()`.
2. Read the `status` field on the response.

Options / Parameters:
- `notification_id`: required, returned by a prior `send()` or `send_batch()` call.

Notes:
- `status` is one of `queued`, `delivered`, `failed`, or `retrying`. See Reference for the full table.
- Status reflects the corresponding row in `notification_jobs`; there is no separate status store.

### Configure retry behavior

Overrides the default retry policy for a single call.

Steps:
1. Call `client.send()` with an optional `retry_policy` dict.
2. Set `max_retries` and `retry_backoff_seconds` inside it.

Options / Parameters:
- `max_retries`: default 3.
- `retry_backoff_seconds`: default 30.

Notes:
- Defaults come from `notifications.notification_jobs_config`, seeded during provisioning. Changing the default for all templates requires a schema change owned by Sam, not a per-call override.

## Monitoring and Dashboards

### View the on-call dashboard

Shows live queue depth and write rate for the notification service.

Steps:
1. Open `https://dashboard.latticenotify.internal/notify-service`.
2. Check the `notification_jobs queue depth` panel; 0 is normal for a healthy queue.
3. Check the `write rate (events/day)` panel against the 500K events/day launch baseline.

Options / Parameters:
- None. The dashboard is read-only.

Notes:
- Jordan owns this dashboard. Contact Jordan in `#notify-service` if a panel is missing or reads unexpectedly.
- Sustained write rate approaching 5M events/day is the documented revisit threshold for the Postgres decision (ADR-0023). This manual does not cover that decision, only how to read the number.

## Troubleshooting

**My notification never arrives**: Usually an invalid `template` name, a missing channel-specific payload field, or an unprovisioned `workspace_id`. Call `client.get_status()` with the returned `notification_id` first; if no ID was returned, `send()` raised before queuing and the error message names the cause.

**`client.send()` raises `WorkspaceNotFoundError`**: Your `workspace_id` has not been provisioned yet. Request one in `#notify-service`.

**`client.send()` raises `PayloadMismatchError`**: The `payload` is missing a variable the template declares. Call `client.preview()` with your payload to see which variable is missing.

**Slack notifications are not posting**: The workspace has no linked Slack app, or `payload` is missing `slack_channel_id`. Confirm the link in the workspace admin panel before retrying.

**Delivery is slower than the documented sub-second p95**: Check the on-call dashboard for elevated queue depth. If write rate is climbing toward the 5M events/day threshold, notify Jordan and Ana Rivera; this is a capacity signal, not a client-side bug.

**The service appears fully down, not just one notification failing**: This is an incident, not a usage question. Page via PagerDuty service `notification-service-prod` rather than filing a client-side bug report.

## Reference

### Status values

| Status | Meaning |
|--------|---------|
| `queued` | Written to `notifications`, not yet picked up by a worker |
| `delivered` | Worker confirmed delivery to the channel |
| `retrying` | Delivery attempt failed; waiting on `retry_backoff_seconds` |
| `failed` | Exhausted `max_retries` without a successful delivery |

### Channels

| Channel | Required payload fields | Notes |
|---------|--------------------------|-------|
| `in_app` | none beyond template variables | fastest path |
| `email` | `subject` | uses the template's HTML layout |
| `slack` | `slack_channel_id` | requires a linked Slack app |

### Errors

| Error | Cause |
|-------|-------|
| `WorkspaceNotFoundError` | `workspace_id` not provisioned |
| `TemplateNotFoundError` | `template` name not registered |
| `PayloadMismatchError` | `payload` missing a declared variable |
| `ChannelNotConfiguredError` | channel requires setup the workspace has not completed |

### Glossary

- **workspace_id**: identifier for the internal service sending notifications, provisioned via `#notify-service`.
- **notification_jobs**: the Postgres table backing the delivery queue, seeded with retry defaults during provisioning.
- **revisit threshold**: 5M events/day sustained, the documented trigger to reconsider the datastore decision (ADR-0023).

### Related documents

- ADR-0023: Postgres for the notification service - the datastore decision this manual assumes.
- Operational runbook - provisioning the `notifications` schema and `notification_jobs` table.
- README - installing and contributing to the notification-service repository itself.

Manual reflects `notify-client` v0.1.0 and ADR-0023 (Accepted, 2026-05-16).
