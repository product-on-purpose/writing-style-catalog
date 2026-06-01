---
entry_id: one-pager
axis: format
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

# Notification Service Datastore: Recommend Postgres, Decision Needed by Friday

## Situation / Background

Lattice Notify is building a real-time notification system that needs a new persistent datastore. Launch volume is 500K events/day; the upside scenario is 10x growth in 12 months if the Slack-partnership deal closes. We evaluated two candidates in the Wednesday 2pm architecture meeting: extend our existing Postgres footprint, or adopt DynamoDB as a second datastore.

## The Point

- **Recommend Postgres**, extended with a new schema and a `pg_notify`-backed job queue.
- The decision turns on operational capacity, not access-pattern fit. We have 8 backend engineers and a 4-person on-call rotation with deep Postgres knowledge and zero production DynamoDB experience.
- DynamoDB is the better technical fit for the access pattern; Marcus made that case correctly. We are accepting a worse pattern fit in exchange for a smaller operational risk surface at our current team size.
- A documented revisit threshold (5M events/day sustained) triggers a new decision review before we scale further on Postgres.

## Why It Matters / Implications

- **Time to launch:** Postgres path ships ~3 weeks faster to first production traffic than the DynamoDB path. Sprint planning Friday assumes this.
- **Recovery cost if wrong:** Both options are recoverable in 3-6 weeks. Postgres recovery is more predictable because we have done a Postgres migration before; DynamoDB recovery would also require unwinding a partially-learned tool. The asymmetry is small but real.
- **On-call burden:** Adopting DynamoDB doubles our operational surface (second runbook, second monitoring story, second debugging skillset on every page). At 8 engineers, this is the load-bearing concern.

## Ask / Recommendation / Next Steps

- **Priya:** lock the decision at our 11am Friday sync so I can mark ADR-0023 Accepted before sprint planning at 2pm.
- **Marcus:** sign off on the 5M events/day revisit threshold language in ADR-0023 by EOD Thursday.
- **Ana (me):** post the decision to the Friday all-hands engineering update and brief the on-call rotation.

Full reasoning: ADR-0023 (draft, link in #notify-arch). Contact: Ana Rivera, ana@latticenotify.com.
