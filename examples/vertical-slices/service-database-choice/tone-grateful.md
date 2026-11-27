---
entry_id: grateful
axis: tone
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-5-5
review_status: reviewed
---

## Grateful on: Choosing between Postgres and DynamoDB

Marcus,

Before ADR-0023 goes to Priya for the Friday lock, I want to write down what you did to make this decision a good one, because the ADR will record the decision and not the work behind it.

You built the DynamoDB spike in `experiments/notify-ddb/` when nobody had asked you to prove the option you were arguing for. You did it knowing that the honest result might hurt your own case. It did not hurt it. The spike showed that DynamoDB fits the notification access pattern, and that finding is the reason the ADR says so in plain words. Without your spike, the Postgres choice would have rested on my instinct about operational load, and the team would have been right to doubt it.

Then you made the strongest case against my position in the Wednesday 2pm meeting, in front of Priya, Jordan, and Sam. I came into that room certain, and I left it with a better reason than the one I walked in with. The concern about our 4-person on-call rotation survived because you pushed on it until it held. That cost you an afternoon and the discomfort of arguing for the option that lost.

You also stayed with me overnight on the recommendation and the 5M events/day revisit threshold. The threshold language in the ADR is mostly yours. It is the reason the Postgres decision is a choice we can reverse and not a bet we have to defend, and it is the reason Sam can build the `notifications` schema without anyone feeling that the DynamoDB option was thrown away.

I did not thank you on Wednesday, and I should have. Thank you for the spike, for the argument, and for the threshold.

Ana
