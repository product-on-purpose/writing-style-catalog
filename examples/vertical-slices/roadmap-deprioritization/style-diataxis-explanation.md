---
entry_id: diataxis-explanation
axis: style
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## Why Insights Moved to Q1

The Insights dashboard is moving from Q3 to Q1. Before we get to what that means for you, it is worth explaining why this kind of shift happens - because the reason is structural, not a symptom of poor planning.

### Why migrations consume roadmaps

A billing-system migration is a different kind of work than building a product feature. Features can be scoped, parallelized, and shipped incrementally. Migrations cannot, because their correctness depends on a single moment: the transition from the old system to the new one. Until that moment, both systems must stay synchronized, which means the migration consumes engineering attention continuously, not just at its scheduled end. When a migration overruns - and billing migrations carry a high rate of unexpected complexity, because billing logic accumulates business rules over years that are only fully visible when you try to change them - the overrun is absorbed by whatever was next in line.

Insights was next in line.

### Why "half-built" is not an option

A dashboard is not a report. A report delivers a fixed set of numbers; a report with half the numbers is half as useful. A dashboard, by contrast, is a system of navigation: it promises that you can explore your data, track what you care about, and trust that what you see is the whole picture. A half-built dashboard breaks that promise not by showing fewer numbers but by making the numbers it does show untrustworthy. Users cannot distinguish which gaps mean "not yet built" from which gaps mean "this data does not exist." The tool becomes a liability because it creates confidence where confidence is not warranted.

This is why the team is shipping a CSV export as a bridge instead of a partial dashboard. The export is honest about what it is: raw data, delivered so you can analyze it in a spreadsheet or BI tool of your choice. It does not pretend to be Insights. It does not make navigational promises it cannot keep.

### What this means for Q1

Insights in Q1 carries the same scope that was committed for Q3. The design has not changed; the timeline moved because the engineering capacity needed to build it properly was consumed by the migration. When the migration completes - which it will, because migrations have a defined end state unlike feature work, which can expand - that capacity returns to the roadmap and Insights becomes the first priority.

The CSV export in September is not a substitute for Insights. It is a carrying mechanism: something that gives you access to the underlying data while the full experience is built on a foundation that is now stable.
