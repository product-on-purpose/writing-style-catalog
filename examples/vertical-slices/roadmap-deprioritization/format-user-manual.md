---
entry_id: user-manual
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Insights User Manual

## Table of Contents

- Getting Started
- Exporting Your Data
  - Downloading a CSV export
- Working with Your Export
  - Column reference
  - Opening the file in a spreadsheet or BI tool
- Dashboard Availability
- Troubleshooting
- Reference
  - Quick reference
  - Glossary
  - Where to get help

## Getting Started

Insights is the analytics layer for the Meridian platform. No separate installation or account setup is required to use it.

- **Access**: through your web browser, from your account's **Settings** page. No additional software is required.
- **Data collection**: Insights records usage events automatically from the date your account is created. There is no opt-in step.
- **Current data access method**: a CSV export of your account's event data, available now. See Exporting Your Data.
- **In-app dashboard**: not yet available. See Dashboard Availability.
- **Permissions**: export access follows your account's existing Settings permissions. Insights does not currently add a separate permission level.

## Exporting Your Data

### Downloading a CSV export

The CSV export gives you your account's underlying Insights event data as a downloadable file, for use in a spreadsheet or BI tool of your choice. Use this to work with your usage data now, while the in-app dashboard is still in development.

Steps:
1. Sign in to your Meridian account.
2. Open **Settings**.
3. Select **Data and Analytics**.
4. Select **Export**.
5. Select **Download CSV**.
6. Save the file when your browser prompts you.

Options / Parameters:
- None currently exposed. Each export returns the full event history for the account; there is no date-range or event-type filter yet.

Notes:
- Exports are generated on demand. Most accounts receive their file within a few seconds; accounts with a long event history may take longer.
- The file covers all usage events from your account's creation date through the end of the previous calendar day. Today's activity will not appear until tomorrow's export.
- There is no scheduled or recurring export yet. Run the export again whenever you want an updated file. Scheduled export delivery is planned as part of the in-app dashboard; see Dashboard Availability.

## Working with Your Export

### Column reference

The export is a single CSV file with one row per event and the following columns:

| Column | Description |
|---|---|
| `user_id` | The user who triggered the event |
| `event_name` | The action recorded (for example, `page_view`, `feature_used`) |
| `event_timestamp` | UTC timestamp of the event, in ISO 8601 format |
| `session_id` | Groups events that belong to the same session |
| `plan_tier` | The account's plan at the time of the event |

Notes:
- `event_timestamp` is always UTC. Convert to your local time zone in your spreadsheet or BI tool.
- `plan_tier` reflects the plan active at the time of each event. An account that has changed plans will show more than one `plan_tier` value across its export history.

### Opening the file in a spreadsheet or BI tool

The export is a standard comma-separated file with a header row. It opens directly in any spreadsheet application or BI tool.

Steps:
1. Open your spreadsheet or BI tool.
2. Open or import the downloaded file directly. Most tools detect `.csv` files automatically.
3. Set `event_timestamp` as a datetime field if your tool does not detect it automatically.

Options / Parameters:
- Delimiter: comma
- Encoding: UTF-8
- Header row: first row

Notes:
- Accounts with a long event history can produce a large file. If your tool struggles to open it, filter by date range after import, or use a BI tool built for large flat files.

## Dashboard Availability

The in-app Insights dashboard is not yet available. It was originally planned for Q3; a mandatory billing-system migration required the engineering capacity that had been allocated to it, and two of the features committed for that release, saved views and scheduled report delivery, were not ready to ship. The dashboard is now targeted for Q1. The CSV export is available now as an interim way to reach the same data.

Notes:
- Until the dashboard ships, use the CSV export (see Exporting Your Data) to work with your Insights data.
- Planned dashboard scope: date-range selectors and trend charts, per-feature and per-user breakdowns, saved views, and scheduled report delivery.
- This manual will be updated with dashboard documentation when the feature becomes available.

## Troubleshooting

**I don't see a dashboard in the product, only an export option.**
The in-app dashboard has not shipped yet; it is targeted for Q1. Use the CSV export in the meantime. See Exporting Your Data.

**My export file is empty.**
Your account has not recorded any usage events in the export window (account creation date through the end of the previous calendar day). Confirm the account has been active, then export again.

**My export does not include today's activity.**
Exports cover events only through the end of the previous calendar day. Today's activity will appear in tomorrow's export.

**The Export option is missing from Settings.**
Confirm you are signed in to the correct account and that you have access to the Settings page. If the option is still missing, contact insights@meridian.io.

**The `event_timestamp` values do not match my local time.**
`event_timestamp` is recorded in UTC by design. Convert to your local time zone in your spreadsheet or BI tool. See Column reference.

## Reference

### Quick reference

| Task | Where |
|---|---|
| Download a CSV export | Settings > Data and Analytics > Export > Download CSV |
| Full in-app dashboard | Not yet available. Targeted for Q1. |

### Glossary

- **Event**: a single tracked action in the product, such as a page view or a feature use. Each event is one row in the export.
- **Session**: a period of continuous product use by one user, grouped by `session_id`.
- **Plan tier**: the subscription plan tied to an account at a given point in time.

### Where to get help

- Support portal: https://support.meridian.io
- Email: insights@meridian.io
