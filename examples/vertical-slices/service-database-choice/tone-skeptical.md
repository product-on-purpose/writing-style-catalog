---
entry_id: skeptical
axis: tone
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Skeptical on: Choosing between Postgres and DynamoDB

Before Wednesday, I want to flag what I think is not yet established in this decision, because we are about to make a commitment based on assumptions that have not been tested.

The 500K events per day launch number. We do not yet have evidence for this. It is a product estimate from Priya's team based on the notifications roadmap, not a measurement against a deployed system. The actual launch number could be 200K. It could be 1.5M. We have not done a sensitivity analysis that tells us at what point the decision would flip. If the real number is 5x our estimate from day one, we are not having the same conversation. What would change my mind: a tighter bound on the launch volume, or a stated commitment that we will treat the number as uncertain and design for a range.

The 10x Slack-partnership scenario. This is being treated as a planning constraint, but the underlying probability is unverified. We have not asked the BD team what their actual close confidence is. We have not asked what the volume profile would look like in the first three months versus the steady state. The 10x number itself is, as far as I can tell, an order-of-magnitude estimate, not a forecast. We are sizing a database decision off it.

The migration cost estimate of 3 to 6 weeks. This has not been verified against a real migration. It is Ana's read based on the Redis migration eighteen months ago, which had different access patterns and a smaller dataset. I would want at least one engineer to write the migration runbook at a sketch level before we treat 3 to 6 weeks as a reliable number.

Marcus's load test on Postgres at 2x launch volume. The 18ms p99 number is real, but it was run against an empty notifications table on dev hardware. We have not tested the cold-cache, partitioned, production-shaped scenario. The number is suggestive at best.

The on-call concern about a second database. This is presented as a hard constraint, but we have not actually polled the rotation. Two of the four on-call engineers have prior DynamoDB experience and may have different views than the rotation lead.

I am not arguing against either option. I am arguing that before we commit on Wednesday, we should be honest about which inputs are measurements and which are estimates dressed as measurements. If we still pick Postgres, we should pick it knowing we are committing on probabilistic grounds, not on settled facts.

- Ana
