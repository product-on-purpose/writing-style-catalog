---
entry_id: narrative-case-study
axis: style
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

The Insights dashboard was on the Q3 roadmap as a committed deliverable. In April, the product team locked the scope: a unified view of event counts, funnel conversion steps, and user-level activity logs, built directly into the application so customers would not need to export data at all. Sales had attached Insights to four enterprise contracts signed in May, with feature availability expected by end of September. Two of those customers had agreed to extended contract terms specifically because Insights was on the calendar.

In June, the engineering team started the mandatory billing-system migration, deferred twice already. The migration was regulatory and could not slip a third time. By mid-July, the scope had expanded: the billing system's data model was more tightly coupled to the core application than the initial audit had shown, and resolving it required touching parts of the codebase that Insights also depended on. The team had estimated eight weeks for the migration. It took fourteen. When August arrived, the engineers meant to begin Insights work were still resolving billing edge cases.

The options were two: ship Insights on September 30 with funnel views missing and user-level logs returning placeholder data, or move the full dashboard to Q1 and ship a CSV export of the underlying data by end of Q3 instead. The product and engineering leads reviewed both paths with the head of sales. They chose the second. A half-built dashboard would create support debt, erode trust faster than a delay, and leave customers worse off than they were before Insights existed.

The CSV export shipped September 24. It gave customers access to the same underlying data Insights would surface - event counts, funnel steps, user-level records - in a format they could load into a spreadsheet or BI tool they already used. Not the integrated experience they were promised, but something useful now. Insights remained on the roadmap with a Q1 target.

Two of the four enterprise customers replied to the announcement with questions about the Q1 date rather than complaints about the delay. One said the CSV was enough for the report they had been planning to run in October.

A committed date creates an expectation. Breaking that date is costly. But shipping an incomplete product against a committed date costs more - it trades a one-time expectation gap for an ongoing trust deficit. The lesson this team carried into Q4 planning was not that timelines should be padded or promises softened. It was that when scope change forces a hard choice, the right stopgap is the one that delivers genuine value in the interim, not the one that honors the original date in name only.
