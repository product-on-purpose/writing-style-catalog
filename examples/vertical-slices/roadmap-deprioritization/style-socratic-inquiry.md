---
entry_id: socratic-inquiry
axis: style
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

When a committed feature is cut, what do you need to know first: what happened, or what it means for you?

That question is worth pausing on. If I lead with the outcome, you have the fact without the context to evaluate it. If I lead with the explanation, you have the reasoning without yet knowing your own exposure. So let me offer both in order, and ask you to consider whether it holds.

What happened: a mandatory billing-system migration we could not defer without affecting every customer's invoicing overran its estimate and consumed the engineering capacity assigned to Insights. We could have kept Insights on the Q3 schedule. But it is worth asking honestly: what would that have delivered? The core data pipeline would have been in place. The visualization layer, the summary views, and the alerting system would not. If Insights had shipped in September in that state, would it have served your needs - or would it have introduced a different problem, the kind where customers form a first impression of a feature before the feature is ready to make a good one?

We moved Insights to Q1. Before Q3 closes, we are shipping a CSV export of the same underlying data that Insights would surface. You can pull it into a spreadsheet or BI tool and work with it directly. It is not Insights, and we are not pretending otherwise. But before you decide how much the gap matters, it may be worth asking: what did you need Insights to enable between now and January? Is there a class of those things the CSV gets you to, even partially?

Insights is on the Q1 roadmap - a commitment, not a placeholder. The question we would ask you to hold is not whether you are satisfied with this outcome. You may not be, and that is fair. The question is whether, given what actually happened, the path we are describing looks like the right one.
