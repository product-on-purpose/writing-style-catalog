---
entry_id: matter-of-fact
axis: tone
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Insights is not shipping in Q3. The engineering capacity allocated to it was consumed by the billing-system migration, which ran six weeks over schedule due to compliance requirements discovered during integration testing. Shipping Insights by end of Q3 would mean shipping it without the chart layer and the in-app filter interface - two components that are not optional for the product to be usable. The team made the call not to ship a broken version.

The new delivery target is Q1 next year. At that point Insights will ship complete: chart rendering, filter controls, saved views, and the CSV export that was already built as part of the data pipeline.

Before the end of Q3, in September, you will receive access to a CSV export of the underlying analytics data. The export covers all the same data points Insights would have surfaced - sessions, funnel steps, and retention cohorts by account. You can load it into any spreadsheet or BI tool. This is not a replacement for Insights; it is access to the data while Insights is not yet built.

The Q1 timeline is confirmed at the engineering level. If the original Q3 date was a factor in your planning - either for accounts in your pipeline or for your own roadmap - reach out so we can address specifics directly.
