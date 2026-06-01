---
entry_id: executive
axis: voice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Executive on: Choosing between Postgres and DynamoDB

We are building the Lattice Notify notification service on Postgres. The decision will be ratified at the architecture meeting Wednesday and locked Friday so the team can plan next sprint.

The bet is straightforward. At 500K events per day and across the 10x scenario tied to the Slack partnership, both Postgres and DynamoDB are technically viable. We are optimizing for organizational velocity, not raw scale, and the binding constraint at our stage is engineering focus on the partnership integration itself - not infrastructure capacity. Adding a second datastore to the production surface, with a team that has not operated one, is a tradeoff we are choosing not to make this quarter.

The cost is real and named. If the partnership lands and growth runs hotter than the 10x model, we will be on the migration path Marcus described: roughly 3-6 weeks of rework, with engineering hours we would rather spend elsewhere. We accept that exposure. The alternative cost - on-call burden during a partnership push, learning curve concentrated in the wrong window, cross-database query complexity we have not yet designed for - is harder to contain once incurred.

We do not yet know what the Slack deal timing looks like. Until we do, we instrument the service to detect the signals that would change our call - write contention, queue depth, p99 latency under load - and we scope a DynamoDB readiness spike for Q3. If the deal closes and the curve runs steeper than projected, we will trigger that spike on a planned cadence, not in response to an incident.

Ana owns the implementation call. Marcus leads the readiness spike when we trigger it. Priya, the sprint plan can proceed on this basis Friday morning.

What changes the decision: a signal from the Slack partnership team that closing probability has moved materially above current estimates, or a measured Postgres write rate above 200 per second sustained during pilot. Either triggers a re-open. Otherwise this is settled.

Next decision point: pilot readout in eight weeks.
