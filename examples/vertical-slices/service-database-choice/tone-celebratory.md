---
entry_id: celebratory
axis: tone
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Celebratory on: Choosing between Postgres and DynamoDB

Team,

Before we walk into Wednesday's architecture meeting and pick a database, I want to stop for a minute and name what just happened over the last two weeks.

Ana and Marcus, you took a question that could have turned into a months-long architecture debate and you ran it down in twelve days. You ran a real load test against both options. You wrote up the access patterns for the notification service in enough detail that Priya could read the doc cold and understand what we are deciding. You disagreed sharply on the recommendation, and you did it in writing, in public, without either of you flinching or making it personal. That is hard. I have watched smaller decisions than this one fracture teams.

What I want to mark is not the answer we are about to choose. The answer matters less than people think. What I want to mark is that Lattice Notify, at fifty people, has a backend team that can argue about Postgres versus DynamoDB on the technical merits, surface the tradeoffs honestly, and arrive at a decision with the PM in the room. That is not a thing every Series B has. We earned it.

Marcus, your DynamoDB writeup made me genuinely reconsider a position I held for three years. Ana, the cost model for the two-database operational surface area is the cleanest piece of analysis I have seen come out of this team. Priya, you held the timeline without rushing the substance, and you asked the right question on Monday about the 10x scenario instead of the one we were all already arguing about.

On Wednesday we will pick a database. Then we will plan the sprint, and on-call will rotate, and the work will get hard in the ordinary ways. But this part - the part where we proved we can think clearly together about something that matters - that part is already done. I wanted to say so before the next thing started.

Thank you for the work.

- Ana
