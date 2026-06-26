---
entry_id: status-report
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Status Report - Insights Dashboard
**Period:** September 1 - 12, 2026
**Author:** Maya Chen, Product Lead
**Status:** Red

## Headline

Insights is cut from Q3. A mandatory billing-system migration overran its schedule and consumed the engineering capacity allocated to the dashboard; shipping on the original date would mean releasing a product that is half-built. Insights moves to Q1 2027, and a CSV data export ships before September 30 so customers can begin working with their data in the meantime.

## Done this period

- Completed the Q3 billing-system migration: all payment flows are validated in staging and the migration is on track for a production release the week of September 19. This was the workstream that displaced Insights.
- Locked the Q1 2027 scope for Insights with engineering: the full dashboard (six views, filter controls, and date-range selection) is committed for Q1, with a target release of March 13, 2027.
- Scoped and sized the CSV export stopgap: customers will be able to download the underlying event data in CSV format and open it in a spreadsheet or BI tool of their choice. The build is estimated at two weeks.

## Up next

- CSV export: backend endpoint complete by September 19; frontend integration and QA by September 24; release September 26. Owner: Dario Reyes (engineering).
- Customer and sales outreach: written notices go to the four key accounts this week. Individual calls are scheduled for accounts that flagged strong dependency on the Q3 date. Owner: Jordan Park (customer success).
- Insights Q1 kickoff: engineering design document begins October 6, after the billing release stabilizes. Owner: Maya Chen (product).

## Blocked / risks

- No current blockers on the CSV export build.
- Risk (medium): if the billing production release on September 19 surfaces regressions, engineering will triage those before returning to the CSV export, which could push delivery to the week of September 30. The team has a one-week buffer before the quarter closes, so a modest slip is recoverable, but it should be treated as a hard deadline, not a target.
- Risk (low): Q1 capacity is contingent on no further mandatory infrastructure work being introduced. Nothing of that kind is currently scoped, but the pattern from Q3 is worth naming explicitly.

## Asks

- Sales: if any of the four key accounts need a direct call before the written notice goes out, please flag the account name to Jordan Park by Thursday. Individual conversations are better than a written notice landing cold.
- Leadership: confirm that a March 13, 2027 Insights target is acceptable to include in customer-facing communications. We want to set that expectation in writing this week and need sign-off before we do.
