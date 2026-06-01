---
entry_id: instructional
axis: tone
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Instructional on: Choosing between Postgres and DynamoDB

How to run the Postgres-vs-DynamoDB decision at the Wednesday 2pm architecture meeting.

Before you start, make sure all attendees (Ana, Marcus, Priya, and the 4-person on-call rotation) have read both option writeups and the load-test results. If any reviewer has not, postpone the meeting; you cannot run this procedure with cold readers.

1. Open with the decision constraint. State that Priya needs an answer by Friday so the next sprint can be planned. This frames the meeting as "make the call" rather than "explore the question."

2. State the two options exactly. Option A: ship on Postgres, add a notifications schema and a queue. Option B: add DynamoDB as a second store for notification events. Write both on the whiteboard. Do not add a third option unless someone proposes one with a concrete writeup; "what about Kafka" is not an option, it is a derailment.

3. Walk through the load model. Confirm the launch number (500K events/day) and the 10x scenario (5M events/day if the Slack partnership lands within 12 months). If anyone disputes the numbers, resolve that before continuing; you cannot evaluate the options against a contested baseline.

4. Have Marcus present the DynamoDB case in 5 minutes, then Ana the Postgres case in 5 minutes. Time each presentation. If a presenter runs over, stop them; the disciplined version of the case is the one the room can evaluate.

5. Ask each on-call engineer the same question, in order: "What does adding a second database do to your week?" Write the answers on the board verbatim. This is the operational input that is usually missing from architecture decisions.

6. Identify the decision thresholds. Specifically: at what event volume does Postgres stop being sufficient? At what point in the partnership timeline does the 10x scenario become real rather than hypothetical? Write both numbers.

7. Take a straw poll. If it is unanimous, confirm the decision. If it is split, run one more round of discussion focused only on the strongest objection to the leading option. Do not run a third round.

8. Name the decision, the owner, and the next-action item. Example: "We are shipping on Postgres. Marcus owns the DynamoDB migration design doc. Ana owns the schema review. We revisit at 3M events/day or partnership signing, whichever comes first."

9. Send the meeting notes to Priya by end of day Wednesday so she has them before the Friday sprint planning.

If the meeting cannot reach a decision in 60 minutes, do not extend it. Schedule a 30-minute follow-up for Thursday morning with only Ana, Marcus, and Priya, and use Wednesday's remaining time to narrow the disagreement to a single resolvable question.
