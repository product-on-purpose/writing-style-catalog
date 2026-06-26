---
entry_id: layered-disclosure
axis: style
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Insights, the in-app analytics dashboard committed for Q3, will not ship this quarter. A mandatory billing-system migration overran its planned scope and consumed the engineering capacity reserved for Insights; shipping in September would mean delivering an incomplete product. Insights moves to Q1. Before the end of September, we will ship a CSV export of the underlying data so you can analyze it in a spreadsheet or BI tool in the meantime.

### What shifted and when

The billing-system migration was a non-negotiable infrastructure upgrade - we could not defer it without risking payment processing. It ran longer than estimated, pulling in the final six weeks of Q3 capacity we had reserved for Insights. The choice came down to two options: ship a half-built dashboard that lacked filter controls, date-range selection, and data drill-down, or hold the feature until the work is actually complete. We chose to hold.

### What you get before the end of Q3

Before September closes, we will send you a CSV export containing the same event and usage records that Insights would have visualized. The file is structured as one row per event, with timestamps, user identifiers, and action types as columns. You can load it into a spreadsheet or BI tool to run filters, pivots, and date-range comparisons using your own setup. No technical configuration is required on your end. We will include a brief field guide with the file to orient you to the column structure.

### What Insights looks like in Q1

The Q1 scope for Insights is unchanged from the original commitment: the full dashboard with date-range controls, filter panels, drill-down views by user segment, and shareable snapshot links. We expect to confirm a specific target date in October, once the migration is closed out and the engineering schedule is set. We will send that date to this same group before September ends. If you have specific use cases you want the dashboard to address, we are collecting that input now.
