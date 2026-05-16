---
entry_id: empathetic
axis: tone
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Empathetic on: Choosing between Postgres and DynamoDB

Marcus,

I want to write to you before Wednesday, because I think the meeting is going to feel a particular way for you and I do not want that to happen without acknowledgment.

You have spent the last two weeks building a serious case for DynamoDB. You ran the access patterns end to end, you modeled the 10x partnership scenario in real detail, and you wrote a document that is, technically, the strongest piece of architecture writing this team has produced this quarter. You did that knowing the team's center of gravity was already leaning Postgres, and knowing the tech lead was already leaning Postgres, and you did it anyway. That is not nothing. It takes a particular kind of nerve to do thorough work on a position you suspect is going to lose.

And on Wednesday, the most likely outcome is that we choose Postgres. I think you probably already know that. Priya has a Friday deadline, the on-call rotation cannot absorb two databases right now, and the launch volume of 500K events a day does not force the change. The decision is not going to turn on the quality of your analysis. It is going to turn on operational reality that your analysis does not control. That is a hard thing to walk into a room knowing.

I want you to hear from me, before the meeting, that the case you made is going to shape how we build this even if Postgres is the database we ship on. The portability decisions in the schema, the choice to keep the event model clean, the migration threshold we are going to commit to - all of that exists because you forced the team to take the alternative seriously instead of defaulting. That is the value your work created, and I want to name it before the room moves to the decision and we never come back to it.

If you want to talk before Wednesday, I have time tomorrow afternoon. If you would rather just walk into the meeting and have it out, that is also fine. Either way, you should know I see what this week has cost you.

- Ana
