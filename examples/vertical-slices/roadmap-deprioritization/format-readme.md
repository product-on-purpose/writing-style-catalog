---
entry_id: readme
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Insights

![status: CSV export available](https://img.shields.io/badge/status-CSV%20export%20available-blue)
![dashboard: Q1 2026](https://img.shields.io/badge/dashboard-Q1%202026-orange)
![support: insights@meridian.io](https://img.shields.io/badge/support-insights%40meridian.io-lightgrey)

> Insights surfaces your usage data as a downloadable CSV now, with a full in-app analytics dashboard shipping in Q1 2026.

Insights is the analytics layer for the Meridian platform. The in-app dashboard was scheduled for Q3 2025. A mandatory billing-system migration overran its planned timeline and consumed the engineering capacity allocated for the dashboard. Releasing the dashboard on the original date would have meant shipping it in an incomplete state. Instead, the team is releasing a CSV export of the same underlying data before the end of Q3, so you can analyze it in a spreadsheet or BI tool of your choice today. The complete in-app dashboard is scheduled for Q1 2026.

## Get your data

No setup is required. Access the export through the platform settings.

```
Settings > Data and Analytics > Export > Download CSV
```

Exports are generated on demand. Most accounts receive their file within a few seconds. The file covers all usage events from your account creation date through the end of the previous calendar day.

## What is in the export

The CSV contains one row per event.

```
user_id           the user who triggered the event
event_name        the action recorded (for example: page_view, feature_used)
event_timestamp   UTC timestamp in ISO 8601 format
session_id        groups events that belong to the same session
plan_tier         the account plan at the time of the event
```

Open the file in a spreadsheet or BI tool to filter by date range, group by user or feature, or build the retention and engagement views you need.

## What is coming in Q1

The in-app dashboard will present the same underlying data without a manual export step. Planned scope:

- Date-range selectors and trend charts
- Per-feature and per-user breakdowns
- Saved views and scheduled summary emails

See the [Q1 Insights scope document](docs/roadmap-q1.md) for the full feature list and target milestones.

## Why this changed

The billing-system migration was required to support the new plan structure currently in pilot. The work expanded past its original estimate and left no room to complete the dashboard to a shippable standard. Shipping a half-built dashboard would have made subsequent iteration harder, so the team redirected. The CSV export delivers the underlying data now; the dashboard makes that data accessible without a manual step in Q1.

## Resources

- [Export column definitions](docs/export-schema.md)
- [Q1 Insights scope](docs/roadmap-q1.md)
- [Billing migration notes](docs/billing-migration-q3.md)
- [Support portal](https://support.meridian.io)

For questions about the export format or the Q1 timeline, contact [insights@meridian.io](mailto:insights@meridian.io).
