---
entry_id: operator
axis: voice
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

The billing migration that ran through Q2 and into July consumed six more weeks of engineering capacity than the schedule called for. Tomasz Wilder, engineering lead, made the call on August 22nd: finish the migration to a clean state or ship Insights with an incomplete data pipeline. We finished the migration. Insights is not shipping in Q3.

A partial Insights dashboard would have surfaced session counts that did not reconcile with the export data, and retention metrics missing three months of backfill. That is worse for customers than waiting. The half-built version is cut. The complete version ships in Q1.

The target date is February 3rd. Denise Park, product lead, owns that date. If anything changes before then, Denise will update this list directly - not through account reps, not through support channels.

The underlying data Insights was going to surface is available now. Starting September 24, any admin user can go to Settings, then Data Export, and download a CSV with session counts, feature interaction tallies, and per-account retention windows by date range. The column definitions are at docs.internal/insights/export-format. If a customer needs a field not in the standard export, or a date range wider than 90 days, email Marcus Webb at marcus@co.io. He runs manual queries - turnaround is one business day.

If a customer escalates and the CSV does not answer their question, loop in Marcus. Do not commit to a date beyond February 3rd. That is the next hard checkpoint, and it is the date this team is accountable to.
