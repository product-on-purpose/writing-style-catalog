---
entry_id: changelog-entry
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Prism Product Roadmap - Changelog

All notable changes to the Prism delivery plan are documented here. Versions follow the format YYYY-QN-RN: year, quarter, and revision within that quarter.

## [2026-Q3-R2] - 2026-09-12

Scope revision following the mandatory billing-system migration. This entry removes the Insights dashboard from Q3 2026 delivery and replaces it with a CSV export stopgap shipping before the end of September.

### Added
- Analytics data export: customers can now download a full CSV of their account's usage data for analysis in a spreadsheet or BI tool (#412)
- Export covers the same date ranges and dimension filters available on the current reporting screen (#412)

### Changed
- Insights dashboard delivery target moved from Q3 2026 to Q1 2027 (#408)
- Revised Insights scope and updated acceptance criteria will be published at the October roadmap review (#408)

### Removed
- Insights dashboard removed from the Q3 2026 release; a mandatory billing-system migration overran its planned window and consumed the engineering capacity originally allocated to Insights (#408)
- Shipping Insights by the original Q3 date would have required releasing a partial implementation; the team scoped the CSV export as a lower-risk stopgap instead (#408)

## [2026-Q3-R1] - 2026-06-15

- Added: Insights in-app analytics dashboard committed for Q3 2026 delivery (#383)
- Added: CSV data export committed as a Q3 stretch goal (#384)
