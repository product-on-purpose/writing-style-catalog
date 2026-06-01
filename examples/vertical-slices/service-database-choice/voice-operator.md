---
entry_id: operator
axis: voice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Operator on: Choosing between Postgres and DynamoDB

For Wednesday's meeting. This is the on-call view of the Lattice Notify database decision. Ana asked me to write it. I am one of the four engineers on the rotation.

We already carry one pager for Postgres. We have runbooks for replication lag, connection pool exhaustion, vacuum stalls, and the long-tail of "the disk filled up because someone shipped a query without a LIMIT." Our mean time to recovery on Postgres incidents is under 30 minutes because we have done it 40 times. The Datadog dashboard is wired. The PagerDuty escalation goes Marcus to Ana to me.

If we add DynamoDB, we add a second pager. We will write the runbook the night of the first incident, which is the wrong night. We do not have a dashboard for it. We do not have a mental model for what hot partitions look like at 3am. We do not have a person to escalate to, because nobody on the rotation has shipped DynamoDB to production. The vendor support contract is not in place. Provisioned-capacity tuning is a habit we have not built.

At 500K events per day, the Postgres path is: notifications schema in the existing cluster, a partitioned events table on event_id, a sidecar deliveries table, and SQS or Redis Streams for the worker queue. Index on (user_id, created_at DESC) for the unread query. Retention job nightly. p99 stays under 50ms. I can name the alerts I would set: queue depth over 5000, write latency over 200ms, replication lag over 10 seconds. I know who responds to each.

At the 10x scenario, the same path holds with one partition split and a read replica. I have run that operation. It is a two-hour change with a rehearsed rollback.

For DynamoDB I cannot write that paragraph yet. I do not know what I do not know. That is the answer.

Recommendation for Wednesday: Postgres. Page @oncall-platform if anything changes between now and Friday.
