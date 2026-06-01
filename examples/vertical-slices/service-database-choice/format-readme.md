---
entry_id: readme
axis: format
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

# notification-service

![build](https://ci.latticenotify.com/notification-service/badge.svg) ![version](https://img.shields.io/badge/version-0.1.0-blue) ![license](https://img.shields.io/badge/license-internal-lightgrey)

> Real-time notification delivery for Lattice Notify, backed by Postgres.

The notification service delivers in-app, email, and Slack push notifications for Lattice Notify at sub-second p95 latency. It runs on the existing primary Postgres cluster with a `pg_notify`-backed job queue, and is operated by the 4-person on-call rotation. It is sized for 500K events/day at launch with a documented 5M events/day revisit threshold per ADR-0023.

## Install

```
git clone git@github.com:latticenotify/notification-service.git
cd notification-service && make setup
```

## Quick start

```python
from notify_client import NotifyClient

client = NotifyClient(workspace_id="ws_abc123")
client.send(
    user_id="usr_xyz789",
    channel="in_app",
    template="comment_mention",
    payload={"actor": "Marcus", "thread_id": "th_42"},
)
```

The event is written to the `notifications` schema, picked up by the `notification_jobs` worker pool within ~50ms, and delivered to the user's in-app inbox in under 1 second.

## Documentation

- [Getting started](docs/getting-started.md) - local setup, environment, smoke tests
- [Architecture overview](docs/architecture.md) - schema, queue, fanout, replication
- [API reference](docs/reference.md) - `NotifyClient` methods, payload schemas, error codes
- [Operational runbook](docs/runbook.md) - alerts, common failure modes, on-call procedures
- [ADR-0023: Postgres for notification service](docs/adr/0023-postgres-notification-service.md) - why we chose Postgres over DynamoDB
- [Examples](examples/) - common notification patterns

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Internal contributors: pair with Ana, Marcus, or Sam on a first PR. All schema changes need a migration plan reviewed by Ana before merge.

## License

Internal Lattice Notify project - see [LICENSE](LICENSE). Not for external distribution.

## Support

Slack: #notify-service. On-call: rotates Mon/Wed/Fri/weekend across the 4-person rotation. For production incidents, page via PagerDuty service `notification-service-prod`.
