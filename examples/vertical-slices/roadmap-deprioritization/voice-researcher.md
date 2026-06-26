---
entry_id: researcher
axis: voice
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

The decision to defer Insights to Q1 rests on a capacity finding we can state with confidence: the billing-system migration, which was mandatory and could not be descoped, consumed engineering hours across the quarter in a way the original Insights timeline did not account for. That is not an inference. We tracked the allocation against the plan, and the gap is clear.

From that finding, we draw an inference: completing Insights this quarter, given remaining capacity, would produce a partial build. The inference rests on what we know about the feature's requirements - the dashboard components not yet started would ship incomplete or absent. We cannot say with certainty how customers would respond, but we assess the risk as significant: a half-built tool delivered as if finished is likely to undermine confidence in a way that a transparent delay would not.

The conclusion from these two inputs - the capacity finding and the risk inference - is to hold Insights until Q1 and ship a stopgap this quarter instead. We want to be clear about the epistemic status of Q1: it is a target, not a guarantee. The constraint that drove the deferral was a mandatory migration, and we cannot rule out that other mandatory work surfaces before Q1. We will communicate if that picture changes.

The stopgap - a CSV export of the underlying Insights data - is a different kind of commitment. Shipping the export is within current capacity, and we find that estimate reliable. Customers who were expecting a dashboard will need to analyze data in their own tools rather than ours. We acknowledge that this is a materially different experience than what was promised.

We are not in a position to say that the Q1 date carries the same certainty as the original Q3 commitment did when it was set. What we can say is that it is calibrated against a capacity model that now reflects actual migration costs, not projected ones. We will send a status update at the Q4 midpoint so that any emerging constraint surfaces before it becomes a cut.
