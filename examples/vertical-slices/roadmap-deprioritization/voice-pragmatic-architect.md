---
entry_id: pragmatic-architect
axis: voice
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Insights is moving to Q1. That decision is made. Here is the constraint that drove it and what we are shipping in its place this quarter.

The billing-system migration ran over by six weeks. We burned the engineering capacity allocated for Insights on schema migrations and reconciliation testing that could not be deferred - payment integrity is not a place where partial work ships. By the time the migration closed, we had roughly four weeks of build time left in Q3 against a feature that needs ten to complete correctly.

Shipping Insights in four weeks produces a dashboard that surfaces aggregate counts but cannot drill into per-user behavior, cannot filter by plan tier, and cannot generate the cohort views that are the whole reason customers asked for this feature. I have watched teams ship at 60% completion and spend the following two quarters patching data models while customers file support tickets about missing functionality. We are not doing that here. The failure mode is predictable and the cost is higher than a delayed ship date.

What ships this quarter: a CSV export of the underlying event data, available to all accounts provisioned for Insights. Every metric the dashboard would have surfaced is in that export. Customers can load it into the analysis tool they already use and build the views they need today. This is not what we committed to, and I am not going to describe it as equivalent. It does give you something concrete to deliver rather than a date slip with nothing behind it.

Insights ships in Q1 - target delivery is end of January, with a limited beta for the customers on this list starting early December. The six weeks lost to the migration are already absorbed into that schedule, and the Q1 build starts from a complete, reviewed spec rather than a compressed one. The tradeoff is clear: customers wait longer and receive a feature that works correctly rather than one we spend Q4 patching in production.

If a specific customer needs a harder conversation than "wait until Q1," come to me directly. I will get on the call.
