---
entry_id: release-notes
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Meridian Platform - September 26, 2026

## Q3 update: data export ships; Insights dashboard moves to Q1 2027

## What's new

- **Insights CSV export**: You can now download your full account usage data directly from the platform. Go to Settings > Data and Analytics > Export > Download CSV. The export covers all events from your account creation date through the previous calendar day, one row per event, with columns for user, action, timestamp, session, and plan tier. Use it in any spreadsheet or BI tool to filter by date range, group by user or feature, or build the engagement views your team needs.

## Improvements

- **Billing and plan management**: The billing-system migration running through Q3 is complete. You can now update your plan, switch billing intervals, and manage invoices from a single location in account settings. Accounts in the new plan pilot will see their tier reflected correctly starting today.

## Changes to announced roadmap

- **Insights dashboard deferred to Q1 2027**: The in-app analytics dashboard was committed for Q3 2026 and is not in this release. A mandatory billing-system migration expanded past its original scope and consumed the engineering capacity allocated to the dashboard. Releasing in the current build would have meant shipping without saved views and scheduled report delivery - the two capabilities most often requested by customers who were given the Q3 commitment date. Shipping that build would not have delivered the value that was promised.

  The Insights dashboard is scheduled for Q1 2027, with a target of March 2027. Planned scope includes date-range selectors, per-feature and per-user breakdowns, saved views, and scheduled summary emails. The CSV export above delivers the same underlying data in the meantime.

  If your team was depending on the Q3 delivery date, contact your customer success representative or email insights@meridian.io.
