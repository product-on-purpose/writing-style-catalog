---
entry_id: urgent
axis: tone
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Urgent on: Choosing between Postgres and DynamoDB

We need a decision at Wednesday 2pm or Priya cannot plan the sprint on Friday.

Ana, Marcus, Priya: read this before the meeting.

The window is closed. There is no Thursday for a follow-up. The next sprint starts Monday and the notifications work is already on the board. If we walk out of Wednesday without a database, three engineers are blocked through the weekend.

Recommendation: ship on Postgres. Confirm in the meeting and move on.

Reasoning, briefly, after the action:

Postgres handles 500K events per day. We have shipped at this scale. The team can start coding Monday morning.

DynamoDB may be better for the 10x scenario, but the partnership has not signed and the timeline is not firm. We do not have time in this sprint to start learning a new ops surface area.

If we trip the 10x volume later, migration is 3 to 6 weeks. That is a recoverable cost. Indecision this week is not.

What needs to happen by end of day Wednesday:

Pick Postgres. Assign schema design to Ana. Assign migration design doc to Marcus as a defensive measure. Send the decision to Priya by 4pm Wednesday so Friday planning has a starting point.

What I am asking each of you to bring to the meeting:

Marcus, bring the strongest specific objection to Postgres at launch volume. Not the general case for DynamoDB. The specific failure mode.

Ana, bring the schema sketch. Not the full design. The shape.

Priya, bring the Friday agenda so we know exactly what we are unblocking.

If anyone reading this thinks the timeline can flex, push back now, today, before Wednesday. Otherwise treat the deadline as fixed and come ready to commit.

- Ana
