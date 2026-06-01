---
entry_id: candid
axis: tone
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Candid on: Choosing between Postgres and DynamoDB

Ana, Marcus, Priya,

I want to be direct about where I have landed before Wednesday's meeting, because I think we have been talking around the real question.

Here is the honest picture. We are not actually choosing between Postgres and DynamoDB. We are choosing between "the system the 8 of us know how to operate" and "a second system that solves a problem we have not yet had." 500K events a day is not a scale problem for Postgres. It is a schema and queue design problem. The 10x Slack-partnership scenario is real, but it is also speculative, and it is 12 months out. We have 8 engineers and a 4-person on-call rotation. Adding a second database doubles the operational surface area for a team that already has a full backlog.

I know this is not what Marcus wanted to hear, and I do not want to dismiss his case. DynamoDB is genuinely better for the steady-state access pattern. If the partnership lands and we are at 5M events a day next spring, we will probably wish we had built on it. That is a real risk and I am not pretending it is not.

But here is the thing I have been avoiding saying: if we pick DynamoDB and the partnership does not land, we have taken on permanent ops complexity to hedge against a scenario that did not happen. And the 3 to 6 weeks of rework if we have to migrate from Postgres later is cheaper than 12 months of paying the two-database tax for a 10x that never came.

What I think we should do: ship on Postgres with a clean enough schema and event model that a future migration to DynamoDB is mechanical, not a rewrite. Revisit at 3M events a day or when the partnership signs, whichever comes first. Marcus owns the migration design doc so we are not flat-footed if we trip the threshold.

Priya, you will have the decision by Friday. I wanted you to know where my head is before Wednesday so the meeting is a conversation, not a surprise.

- Ana
