---
entry_id: executive-summary
axis: style
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Executive Summary on: Choosing between Postgres and DynamoDB

**Recommendation: ship the Lattice Notify notification system on Postgres with a queue. Pre-commit to a DynamoDB migration trigger if real volume crosses 2M events/day on a 30-day rolling average.** This is the decision the architecture meeting should ratify on Wednesday 2pm Pacific, with the team executing against it from sprint planning on Friday.

**Why Postgres now.** Three of the five evaluation criteria favor Postgres at launch volume of 500K events/day: the eight-backend-engineer team has shipped at this scale on Postgres before; the four-person on-call rotation can debug Postgres incidents without ramp-up; cross-database queries to the existing billing, analytics, and product reads stay native SQL. Operating two storage systems doubles the on-call cognitive load on a rotation that does not have slack to absorb it. The cost of being wrong is bounded: 3-6 weeks of rework if a migration is forced, on a schedule the team can plan rather than an incident the team has to survive.

**Why the trigger condition.** The 10x growth scenario depends on the Slack-partnership deal closing. CRO estimate is 60% confidence. At that probability, the expected operational cost of running on DynamoDB from day one (a year of two-database operations on an untrained team) exceeds the expected cost of a deferred migration. The 2M events/day threshold is roughly the point at which Postgres sharding work becomes urgent rather than discretionary; defining the trigger now converts a future emergency into a scheduled engineering project.

**Risks accepted.** If the Slack deal closes and volume ramps faster than expected, the team will face a migration project they could have avoided. Marcus's prototype Dynamo schema is preserved in the design-docs repo to shorten that path if it becomes necessary. If volume stays flat, the team gains a year of stability on familiar infrastructure with no architectural debt.

**What this decision rejects.** It rejects DynamoDB-from-day-one as too operationally expensive for the current team size. It rejects an unconditional Postgres commitment as insufficiently planned for the high-volume scenario. It rejects deferring the decision past Friday, which would block next sprint's planning.

**Owners and dates.** Ana owns the Postgres schema and queue integration; target in production by 2026-06-15. Marcus owns the preserved Dynamo design and will be lead engineer if the trigger fires. Priya owns the quarterly volume review against the 2M events/day threshold, starting 2026-Q3. The on-call rotation stays at four people on one storage system.
