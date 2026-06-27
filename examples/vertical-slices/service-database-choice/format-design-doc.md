---
entry_id: design-doc
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Notification Service - Database Layer Design

## Status

In Review

## Problem

Lattice Notify is building a real-time notification delivery system. Before implementation begins, the team needs to commit to a database technology and a concrete design for how notification events are stored, queued, and delivered.

**Access pattern.** The write pattern is fanout: one source event generates one notification row per recipient and one delivery job per channel. Writes are insert-only. The dominant read pattern is user-scoped point-lookups: "last 50 notifications for user X." Deletes are rare (30-day TTL via batch job). No analytical queries run against this table.

**Scale envelope.** At launch: 500K notification events per day, roughly 6 events per second sustained with peaks around 30/sec during business hours. A 10x growth scenario (5M events/day) depends on a pending partnership deal that has not closed.

**Team constraint.** 8 backend engineers, 4-person on-call rotation. The team has operated Postgres in production at this scale. The team has no production DynamoDB experience.

**What this design must answer.** Schema layout, write and read data flows, component boundaries between the notification service and upstream callers, worker pool architecture, and the operational surface the on-call rotation inherits.

## Proposed Design

**Technology: Postgres, new `notifications` schema on the existing primary cluster.**

### Schema

```sql
CREATE TABLE notifications.events (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    workspace_id  TEXT        NOT NULL,
    user_id       TEXT        NOT NULL,
    channel       TEXT        NOT NULL,   -- 'in_app' | 'email' | 'slack'
    template      TEXT        NOT NULL,
    payload       JSONB       NOT NULL DEFAULT '{}',
    delivered_at  TIMESTAMPTZ,
    created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX ON notifications.events (user_id, created_at DESC);
CREATE INDEX ON notifications.events (workspace_id, created_at DESC);

CREATE TABLE notifications.jobs (
    id            UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id      UUID        NOT NULL REFERENCES notifications.events(id),
    channel       TEXT        NOT NULL,
    status        TEXT        NOT NULL DEFAULT 'pending',
                  -- 'pending' | 'processing' | 'done' | 'dead'
    attempts      INT         NOT NULL DEFAULT 0,
    next_attempt  TIMESTAMPTZ NOT NULL DEFAULT now(),
    error         TEXT,
    created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX ON notifications.jobs (status, next_attempt)
    WHERE status IN ('pending', 'processing');
```

### Write path

1. Caller writes one row to `notifications.events` and one row per delivery channel to `notifications.jobs` in a single transaction.
2. At commit, the caller issues `pg_notify('notification_ready', event_id::text)`.
3. The worker pool, listening on `notification_ready`, wakes, claims the job via `UPDATE ... RETURNING` with a short lock timeout, and executes delivery.
4. On success: `jobs.status = 'done'`, `events.delivered_at = now()`. After 3 failed attempts: `jobs.status = 'dead'` for dead-letter review.

### Read path

1. User inbox reads go to a read replica: `SELECT * FROM notifications.events WHERE user_id = $1 ORDER BY created_at DESC LIMIT 50`. No joins required for the inbox case.
2. Cross-schema joins (enriching notifications with account display names for digest email) run against the primary and are bounded to under 1 request per second.

### Component boundaries

- `notification-service` owns the `notifications` schema exclusively. No other service writes to it directly.
- Upstream callers use `NotifyClient.send(user_id, channel, template, payload)`. The client opens a connection, writes the two rows, and calls `pg_notify`. It has no knowledge of delivery mechanics.
- The worker pool runs as a separate process in the same deployment unit. It is not called over a network boundary.
- Dead-letter rows (`status = 'dead'`) are drained by a scheduled job on a separate schedule from the worker pool; no automatic retry beyond 3 attempts.

### Read replica provisioning

One read replica at launch. Promote to two if the inbox read rate exceeds 500 req/sec sustained. Jordan owns the dashboard metric that triggers this decision.

## Alternatives Considered

### DynamoDB with a single-table design

A composite key of `(PK = user_id, SK = created_at#event_id)` serves user inbox reads as a single Query with no secondary index. Fan-out writes land in parallel via batch-write. This is the access-pattern-optimal design.

**Why not chosen.** DynamoDB fits the access pattern well. The blocking constraint is operational, not architectural. The team has no production DynamoDB experience. Adding DynamoDB doubles the on-call surface: a second runbook, a second monitoring story, a second class of alerts. At 500K events/day the Postgres design is within the team's demonstrated operating envelope, and the access-pattern advantage of DynamoDB does not outweigh the operational cost at this load. Marcus documented this tradeoff in `experiments/notify-ddb/` after completing the spike. The 5M events/day revisit threshold re-opens DynamoDB consideration at the point where the access-pattern cost becomes dominant.

### DynamoDB + SQS for the delivery queue

Events land in DynamoDB; delivery jobs route through SQS, consumed by Lambda workers.

**Why not chosen.** This adds SQS and Lambda to the operational surface on top of DynamoDB. The team did not evaluate it in detail because DynamoDB was eliminated on operational grounds first. The surface area is strictly larger than the DynamoDB-only option.

### Redis-backed job queue (Sidekiq or BullMQ pattern)

Events stay in Postgres; delivery jobs route through Redis rather than `pg_notify`.

**Why not chosen.** Adds a second datastore with no clear benefit over `pg_notify` at launch scale. `pg_notify` is adequate to roughly 2K messages per second; the design targets 30/sec peak. Revisit only if the team adopts Redis for another service-wide reason.

## Risks and Open Questions

**1. Postgres partitioning at scale (owner: Ana)**

At roughly 3M events/day sustained, the `notifications.events` table accumulates around 1 billion rows in a year. Range partitioning on `created_at` handles this, but the live migration is non-trivial. This is a known roadmap item targeted for Q4 if growth tracks projection. If the Slack partnership deal closes and 10x growth arrives in under 12 months, the team hits this window earlier. Mitigation: Priya monitors deal timing and commits to giving the team 30 days of warning before the 5M events/day threshold is breached.

**2. `pg_notify` message loss on worker restart (owner: Sam)**

`pg_notify` delivers only to active listeners. A worker restart while events are in flight drops those notifications. The worker pool must execute a startup poll - `SELECT * FROM notifications.jobs WHERE status = 'pending' AND next_attempt <= now()` - on startup and on a 30-second fallback schedule to recover missed events. Sam needs to confirm this fallback is in the implementation spec before the schema is finalized on 2026-05-20.

**3. Dead-letter volume baseline (open question)**

No measured delivery failure rate exists yet. Before first production traffic (target: 2026-05-29), the team needs an expected daily volume of `status = 'dead'` rows and an owner for reviewing them. Without this, the dead-letter drain job has no alerting threshold.

**4. Worker pool connection count (owner: Jordan)**

Each worker process holds one persistent `LISTEN` connection to the primary. The pool size at launch is not yet set. Jordan should add worker connection count to the on-call dashboard alongside queue depth and write rate by 2026-05-22, so the team enters launch with visibility into connection pressure.

## Appendix

### Event volume estimates

| Scenario | Events/day | Avg events/sec | Peak events/sec |
|---|---|---|---|
| Launch | 500K | 6 | ~30 |
| Revisit threshold | 5M | 58 | ~290 |

### References

- `experiments/notify-ddb/` - DynamoDB spike and access-pattern analysis (Marcus)
- ADR-0023 (draft) - decision record; to be marked Accepted at the 2026-05-16 11am sync with Priya
- `#notify-arch` - architecture discussion thread
