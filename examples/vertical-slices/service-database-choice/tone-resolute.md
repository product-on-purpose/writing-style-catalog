---
entry_id: resolute
axis: tone
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Resolute on: Choosing between Postgres and DynamoDB

Team,

Following Wednesday's architecture meeting: we are shipping the notification service on Postgres. The deliberation is closed.

The reasoning has been documented in the meeting notes and the linked decision record; I am not going to relitigate it here. What this message is about is what happens next.

Ana owns the notifications schema and the queue design. First review draft is due by end of day Tuesday next week. Marcus owns the DynamoDB migration design document, scoped to be executable if we cross 3M events per day or if the Slack partnership signs, whichever comes first. That document is due by the end of the sprint after this one. Priya has the decision for Friday's planning, and the notification service goes into the next sprint as a committed deliverable.

On-call rotation stays at the current four people through launch. We are not adding a second data store, so the operational surface area does not change. The runbook updates for the new notifications service will be drafted by Ana and reviewed by the on-call rotation before launch; that review is a hard gate, not a courtesy.

For the team: the question is decided. I am asking everyone to commit fully to the path, including those of you who would have preferred Option B. We are not going to keep the alternative alive in side channels and standup asides. If the load profile changes or the partnership signs, we have a defined trigger and a designed migration ready to execute. Until then, this is the system we are building.

Marcus, I want to name directly: your DynamoDB analysis shaped the schema portability decisions we are making. The work is not wasted; it is built into the architecture going forward, and it is what makes the migration path real instead of theoretical. The decision did not go your way. The work did.

Wednesday 2pm is the kickoff for the notifications sprint. Come ready with story points. We start work next Monday.

- Ana
