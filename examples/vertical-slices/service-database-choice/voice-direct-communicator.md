---
entry_id: direct-communicator
axis: voice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Direct Communicator on: Choosing between Postgres and DynamoDB

Postgres for the notifications service. Wednesday meeting can confirm; Friday lock works.

Why: 500K events/day fits comfortably on the existing cluster with a partitioned table and a queue. The team operates Postgres now. Adding DynamoDB adds an on-call surface no one on the four-person rotation has shipped to production. The 10x Slack-partnership scenario is real but conditional; the operational cost of DynamoDB is unconditional and immediate.

Tradeoff: if growth runs past 10x, we eat 3-6 weeks of migration rework. Accepted. The alternative is paying that complexity now, every day, against an outcome that may not materialize.

What I need from each of you:

- Ana: own the implementation plan. First draft by Tuesday EOD.
- Marcus: scope the DynamoDB readiness spike for Q3 so we can pull it off the shelf if the Slack deal closes. One-pager by next Friday.
- Priya: sprint plan Friday morning on this basis.

Three signals that would change the call:
1. Slack deal closing probability moves materially above current read before pilot ends.
2. Sustained Postgres write rate above 200/sec during pilot.
3. Ana's Postgres operational confidence at 10x drops below where it is today.

If any of those land, we reopen. Otherwise this is decided.

Reply if you disagree before Wednesday 12pm Pacific. Silence = ratification at the 2pm meeting.
