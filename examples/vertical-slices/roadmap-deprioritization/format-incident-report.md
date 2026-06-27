---
entry_id: incident-report
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Incident Report: Insights Dashboard - Q3 Delivery Commitment

## Status

Resolved - September 12, 2026

## Summary

The Insights analytics dashboard, committed for delivery to customers before the end of Q3 2026, will not ship on schedule. A mandatory billing-system migration earlier in the quarter expanded beyond its original scope and consumed the engineering capacity allocated to the dashboard. Customers with a firm Q3 commitment will receive a CSV data export before September 30 and the full dashboard in Q1 2027.

## Impact

- Services affected: Insights analytics dashboard (Q3 2026 release)
- Customers affected: Four enterprise accounts that received a direct Q3 delivery commitment from the sales team
- Duration: Delivery gap identified early September 2026; decision finalized September 12, 2026

## Timeline

- Q3 2026 start - Insights dashboard enters the quarter as a committed delivery; four accounts have been given a Q3 date by the sales team
- Early September 2026 - Billing-system migration, required to support the new plan structure in pilot, is confirmed to have expanded past its original scope estimate
- September 8, 2026 - Confirmed that the migration and the Insights dashboard cannot both be completed in the time remaining without risking both deliveries
- September 12, 2026 - Decision made to defer Insights to Q1 2027 and ship a CSV export of the Insights data layer before September 30 as an immediate stopgap
- September 26, 2026 (scheduled) - CSV export available to all Meridian accounts
- March 13, 2027 (target) - Full Insights dashboard release

## Root Cause

A mandatory infrastructure migration required to support the new plan structure expanded past its original estimate. The scope increase was not visible during Q3 planning. Once the full scope became clear, the engineering capacity available for the quarter could not cover both the migration and the Insights dashboard. Delivering a partially built dashboard - one missing the saved-view persistence and scheduled-report delivery that committed customers specifically requested - was evaluated and ruled out. Shipping an incomplete version would not meet the use cases for which it was promised and would make subsequent iteration harder than an honest delay.

## Resolution

The Insights dashboard is deferred to Q1 2027, with a target release of March 13, 2027. A CSV export of the underlying data ships before September 30, giving customers immediate access to their data in a spreadsheet or BI tool of their choice while the full dashboard is under development. The four affected enterprise accounts will be contacted directly before September 15, with individual calls offered to accounts that have a strong dependency on the Q3 date.

## Next Steps

- September 26, 2026: CSV export available to all Meridian accounts with no action required; access through Settings > Data and Analytics > Export
- Week of September 15: Direct written notice to all four affected enterprise accounts; individual calls available on request for accounts that need them
- October 6, 2026: Engineering design work on the full Q1 Insights scope begins after the billing migration stabilizes in production
- Q4 2026: Q1 scope and the March 13, 2027 target confirmed through quarterly planning and communicated in writing to affected accounts
