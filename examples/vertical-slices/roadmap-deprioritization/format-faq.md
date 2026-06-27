---
entry_id: faq
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## Frequently Asked Questions: Insights Dashboard

### Why is the Insights dashboard not shipping in Q3?

The billing-system migration expanded past its original estimate and consumed the engineering capacity that had been allocated to Insights. The two workstreams could not run in parallel without putting both at risk. Shipping on the original date would have meant releasing the dashboard without saved-view persistence and scheduled-report delivery - the two capabilities the committed accounts specifically asked for.

### When will the Insights dashboard ship?

The dashboard is targeted for Q1 2027, with a planned release date of March 13, 2027. This target is confirmed for Q4 planning but not yet in customer-facing communications; leadership sign-off is needed before that date is shared in writing with accounts.

### What can I use right now?

A CSV export of the same underlying Insights data ships September 26. Access it from Settings > Data and Analytics > Export > Download CSV. The export covers all usage events from your account creation date through the end of the previous calendar day. Open the file in any spreadsheet or BI tool to filter by date range, group by user or feature, and build the views you need.

### What is in the CSV export?

Each row is one event. Columns include: the user who triggered the event, the action recorded, a UTC timestamp in ISO 8601 format, the session ID that groups related events, and the account plan tier at the time. The export does not include saved views, scheduled report delivery, or in-app visualizations - those are part of the Q1 dashboard scope.

### Will the Q1 date actually hold?

The Q1 2027 target is backed by a locked engineering scope and a specific delivery date (March 13, 2027). The one named risk is another mandatory infrastructure workstream appearing before then; nothing of that kind is currently scoped. The team will surface any threat to that date early rather than letting it emerge close to delivery.

### Who do I contact with questions?

For questions about the export format or the Q1 timeline, contact insights@meridian.io. For the four key accounts that were given the original Q3 commitment, direct concerns to Jordan Park (customer success), who is coordinating outreach and individual calls this week.
