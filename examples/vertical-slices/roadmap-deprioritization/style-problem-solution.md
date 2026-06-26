---
entry_id: problem-solution
axis: style
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## What Happened to Insights, and What Ships Instead

We committed Insights for Q3. You made plans around that commitment - sales conversations, customer expectations, roadmap conversations with your own stakeholders. We owe you a clear account of why that date is not holding and what we are doing about it.

## The Problem

Partway through August, we were six weeks behind on Insights. The cause was a billing-system migration that ran longer and deeper than the estimate we built the quarter's capacity plan around. The migration is not optional - it closes a compliance gap that would otherwise affect every customer's billing accuracy. But it consumed the engineering time allocated to Insights.

At that point, we had a choice: ship what was done on the original date, or move the full feature and ship something useful in its place.

Shipping the partial build was the wrong call. The version of Insights that was shippable in Q3 was missing date-range filtering, multi-metric overlays, and CSV export - the three capabilities named in nearly every sales conversation and customer discovery call. A dashboard that can display only a single metric for the current period is not the product you committed to. Shipping it would have required a second onboarding when the rest of the features arrived, and it would have anchored your customers' first experience to something we know is incomplete.

## The Path Forward

By the end of September, we are shipping a CSV export of the underlying Insights data. The export includes the same event streams Insights will visualize: session activity, feature-interaction rates, and funnel completion broken down by cohort. You can load it into a spreadsheet or BI tool you already use and run the analysis you have been waiting for.

The full Insights dashboard - with date-range filtering, overlays, and saved views - ships in Q1. We are locking scope now so engineering can start immediately after the billing work wraps, with no planning gap between.

We will send the export field guide and file format on September 15. When the Q1 launch date is confirmed, you hear it before anyone else does.

If there is a specific workflow - a customer-facing report, a board deck, a quarterly review - that the delay creates a concrete problem for, tell us now. We will work out a bridge.
