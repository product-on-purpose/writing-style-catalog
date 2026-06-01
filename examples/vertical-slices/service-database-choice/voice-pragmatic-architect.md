---
entry_id: pragmatic-architect
axis: voice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Pragmatic Architect on: Choosing between Postgres and DynamoDB

We should ship the Lattice Notify notification service on Postgres. The decision turns on three constraints, in this order: operational surface area, team skill, and the cost of being wrong.

500K events per day is not a Postgres scaling problem. It is roughly 6 writes per second sustained, with bursty peaks we can absorb with a partitioned table and a queue. The 10x Slack-partnership scenario gets us to 60 writes per second, which is still well inside what a properly indexed Postgres instance handles before we need to think about read replicas or partitioning by tenant. Ana is right that we have shipped at this scale before. We know the failure modes, we know the recovery playbooks, and the four-person on-call rotation already carries the pager for Postgres.

Marcus's argument for DynamoDB is not wrong on the access pattern - notifications are key-value writes with TTL-based reads, which is exactly what DynamoDB does well. But the cost we would pay is real: a second datastore in production, cross-database query patterns the team will reinvent badly under deadline pressure, and a learning curve that lands in the middle of the partnership push, not before it. If Slack lands, we will want senior engineers on the integration, not on figuring out why our DynamoDB partition keys are hot.

The failure mode of staying on Postgres is known: at some growth multiple beyond 10x, we hit write contention and have to migrate. Priya, that migration is the 3-6 week of rework you flagged, and it is recoverable. The failure mode of going DynamoDB now is unknown: we do not yet know what we do not know about operating it, and we will learn during the partnership window.

My call for Wednesday: Postgres, with a dedicated notifications schema, a partitioned events table, and a Redis-backed queue for delivery. We revisit at 5x current volume. If the Slack deal lands and the curve looks steeper than that, we put DynamoDB on the roadmap as a planned migration, not an emergency one. Friday deadline is achievable.
