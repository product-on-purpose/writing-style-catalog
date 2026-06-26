---
entry_id: adr
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# ADR-0027: Defer Insights Dashboard to Q1; Ship CSV Export as Q3 Stopgap

## Status

Accepted

## Context

The team entered Q3 with a firm commitment to ship the Insights analytics dashboard before the end of the quarter. Sales had positioned Insights as a closing point for several enterprise accounts, and three key customers had been given a delivery date.

In early Q3, the mandatory billing-system migration surfaced scope that was not visible during planning. The migration is non-optional - regulatory and contract dependencies require it to complete before year-end. The engineering work required to meet migration requirements consumed the capacity originally allocated to Insights. The two projects cannot share capacity without risking both.

Two options were on the table:

1. Ship Insights on the original Q3 date against the current state of the build.
2. Cut Insights from Q3, complete the billing migration cleanly, and move Insights to Q1.

Option 1 was evaluated and ruled out. The current Insights build is missing the saved-view persistence layer and the scheduled-report delivery feature. These are the two capabilities the committed customers specifically asked for. Shipping without them would deliver a product that fails at the exact use cases for which it was promised. Rework after a disappointing early release carries more cost than an honest delay.

A partial stopgap is available. The underlying data that Insights will eventually surface is already queryable from the data layer. A CSV export of that data can ship before the end of Q3 without material engineering risk and with a few days of integration work.

## Decision

We defer the Insights dashboard to Q1 next year. Before the end of Q3 (target: September), we ship a CSV export of the Insights data layer so that customers can analyze their data in a spreadsheet or BI tool of their choosing while the full dashboard is under development.

Sales and the affected customers will be notified directly and given the CSV export date and the Q1 commitment. The Insights scope for Q1 will be confirmed in the Q4 planning cycle.

## Consequences

### Positive

- No half-built feature ships. The Q3 commitment was for Insights with saved views and scheduled reports; releasing without those would not deliver the value that was sold.
- The billing migration completes without schedule pressure from a competing workstream, reducing defect risk from context switching.
- The CSV export gives customers immediate access to their data with no install or onboarding requirement. Some customers may find it sufficient for their current workflow.
- Q1 gives the team time to build Insights to the committed spec without scope shortcuts.

### Negative

- The Q3 commitment to sales and key customers is broken. Trust repair is required and will take direct communication, not just a status update.
- The CSV export is a weaker experience than the dashboard. Customers must supply their own tooling to filter, visualize, and schedule reports against the exported data.
- The Q1 target is a directional commitment. It is not backed by a closed capacity plan until Q4 planning completes. Stakeholders should be told this clearly.

### Neutral

- The Insights feature scope is frozen at the Q3 spec for now. Requests for scope changes during the deferral period are queued for Q1 planning; none will be folded in silently.
- Customer-facing messaging about the change is owned by Sales and customer success. Engineering provides the technical facts; messaging decisions are theirs.
