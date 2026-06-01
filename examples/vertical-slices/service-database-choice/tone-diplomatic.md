---
entry_id: diplomatic
axis: tone
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Diplomatic on: Choosing between Postgres and DynamoDB

Marcus,

Thank you for the thorough DynamoDB writeup you circulated Monday. The depth of the access-pattern analysis and the load projections under the 10x Slack-partnership scenario have meaningfully sharpened how the team is thinking about this decision, and several points in the document have already changed my own reading of the tradeoffs.

While the case for DynamoDB on the steady-state access pattern is well constructed, there are considerations worth weighing alongside it as we approach Wednesday's meeting. Concerns have been raised, both in the engineering channel and in the operations review last Friday, about the cumulative load on a four-person on-call rotation that would now be responsible for two production data stores rather than one. The team has shipped at the 500K-events-per-day scale on Postgres before, and the institutional knowledge in that area is substantial. The 10x scenario, while real and worth planning for, remains contingent on a partnership decision outside our control, and the timeline for that decision is not yet firm.

We may want to explore a path that preserves the option you are advocating for without committing to it ahead of the evidence. One framing worth surfacing in the meeting: ship the launch on Postgres with a schema and event model designed for portability, while you maintain ownership of a DynamoDB migration design document that we could execute on if and when we cross a defined threshold (perhaps 3M events per day, or partnership signing, whichever arrives first). This preserves the optionality your analysis identified as valuable, while allowing us to defer the operational complexity until it is clearly justified by load.

I would welcome the opportunity to discuss this framing with you ahead of Wednesday, so that whatever recommendation we bring to Priya reflects the strongest version of both positions rather than a compromise neither of us fully endorses. I am available before noon Pacific tomorrow if a thirty-minute conversation would be useful.

Either way, the work you have put into this analysis has improved the decision, and I want that acknowledged regardless of where we land.

Best,
Ana
