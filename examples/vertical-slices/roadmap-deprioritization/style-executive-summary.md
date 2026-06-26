---
entry_id: executive-summary
axis: style
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Insights will not ship in Q3. The billing-system migration that began in July ran significantly longer than projected and consumed the engineering capacity reserved for Insights. Shipping this quarter would mean shipping a dashboard with core reporting features incomplete, which would fail to deliver the value we committed to. We are moving Insights to Q1 next year and shipping a CSV export of the underlying data before the end of September so customers can begin their analysis in the interim.

The migration could not be deferred. Billing is a compliance-critical system, and the underlying schema issues discovered mid-migration required a complete resolution before the quarter closed. When the choice was between delaying billing stabilization and delaying Insights, the engineering team had no acceptable alternative to completing the migration. Engineering capacity did not recover in time to begin meaningful Insights development.

A half-shipped Insights dashboard is worse than no Insights dashboard. The features stakeholders were promised - comparative period views, funnel breakdowns, and exportable cohort data - require the full data pipeline to be useful. Shipping a partial build would have given customers a product that looked complete but answered none of the questions that justified the commitment in the first place.

The CSV export is not a substitute for Insights, but it enables meaningful customer analysis before Q1. The same underlying data that will power Insights is available in tabular form. Customers who want to begin trend analysis or build their own views can do so in a spreadsheet or BI tool starting in September. The export format will be documented, so any work done now will be transferable when the full dashboard ships.

Insights enters Q1 planning as the top-priority feature with full engineering allocation starting the first sprint. We expect to share a Q1 delivery date and a preview of the beta program with sales and key customers by mid-October.
