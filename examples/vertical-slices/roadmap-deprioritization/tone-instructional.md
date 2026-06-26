---
entry_id: instructional
axis: tone
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Here is what you need to know about the Insights delivery, and what steps follow from it.

Insights - the in-app analytics dashboard scheduled for Q3 - is moving to Q1 of next year. The reason is a mandatory billing-system migration (a required infrastructure upgrade to meet updated payment-processing compliance requirements) that ran significantly over its allocated duration and consumed the engineering capacity set aside for Insights. Shipping in Q3 would have meant delivering the data pipeline without the dashboard interface - the part you would use. We chose not to do that.

Before you update your own plans, it helps to understand what happened to the timeline. The billing migration's integration surface turned out to be substantially larger than the pre-migration audit indicated. We did not surface that risk to stakeholders early enough; that gap is being addressed in how we scope and track migration work going forward. If you need to explain the slip to your own teams or customers, the accurate framing is: a mandatory infrastructure requirement expanded unexpectedly and consumed the capacity reserved for Insights. Scope creep on a compliance dependency is the cause, not a reprioritization of Insights itself.

Before the end of September, you will receive a CSV export of the underlying analytics data - the same data set that the Insights dashboard will surface in Q1. To begin using it, download the file from the link in the delivery email, open it in your preferred analysis tool (a spreadsheet, a BI platform, or anything that reads CSV), and note that the first row is a header row and the default date range covers the current quarter.

Insights ships Q1. A confirmed date follows as soon as Q4 planning closes.
