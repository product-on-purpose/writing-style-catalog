---
entry_id: definitional
axis: style
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

A quarterly scope change is a scheduled commitment removed from a specific quarter's delivery plan because engineering capacity is unavailable, with a new target quarter assigned and the commitment otherwise intact. That is what happened to Insights.

The billing-system migration overran its planned capacity this quarter. The engineering hours remaining after the migration were not enough to ship Insights completely - and shipping it incompletely would mean delivering a product that does not meet the specification we committed to. So Insights is removed from Q3 and rescheduled to Q1.

## What this is, by its facets

A quarterly scope change has three components that together define it:

- A specific timeline shift: Insights moves from Q3 (this quarter) to Q1 next year.
- An unchanged product definition: Insights ships with its full original scope in Q1, not a reduced version.
- An interim accommodation: a CSV export of the underlying data ships in September so you can analyze it in a spreadsheet or BI tool while the full dashboard is in development.

Each of those three components must be present for this to count as a quarterly scope change rather than something else.

## What this is not

Not every removal from a quarter's plan is the same thing, and the distinctions matter for how you plan.

A cancellation would mean Insights is removed from the roadmap with no replacement date and no continued commitment. That did not happen. Insights has a new target quarter and the same scope.

A value deprioritization would mean the team concluded Insights is less important than previously believed - that competing work is simply worth more. That also did not happen. This is a capacity decision, not a reassessment of what Insights is worth.

An indefinite hold would mean Insights moves out with no committed landing date. It has a date: Q1.

One adjacent case worth naming precisely: the September CSV export is not a partial Insights delivery. It shares underlying data with Insights but does not meet the definition of the dashboard - there is no in-app interface, no team-level segmentation, no saved views. It is a data accommodation that bridges the gap; it is not a shipping milestone for Insights. If you ask "does this count as Insights?" the answer is no.

## The definition applied

Insights is a quarterly scope change: same feature, same scope, new quarter, with an interim data bridge. The billing migration consumed the capacity it needed in Q3. The new target is Q1. What ships in September is a CSV export of the data - a stopgap, not the dashboard. What ships in Q1 is the original Insights.
