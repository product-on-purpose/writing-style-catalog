---
entry_id: encouraging
axis: tone
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Encouraging on: Choosing between Postgres and DynamoDB

Team,

Wednesday's meeting is going to feel bigger than it is, and I want to say a few things in advance.

This is a hard call. There is no version of it that does not have real tradeoffs, and either path carries risk we will have to manage. I am not going to pretend otherwise. But I want you to know that this team is well positioned to make this decision and execute on it, and I have specific reasons for believing that.

You have already done the hard part. Marcus, you ran a real load test instead of arguing from intuition. Ana, you mapped the operational cost in concrete terms instead of waving at "ops complexity." Priya, you held the timeline without compressing the substance. The decision in front of us is hard, but it is hard on top of work that has already been done well. You are further along than this feels.

On the technical question itself: we have shipped at the 500K-events-per-day scale before. We know how to design schemas and partition tables and tune queues at that level. If we pick Postgres, the path is one this team has walked. If we pick DynamoDB, Marcus has done enough discovery work that the learning curve is shorter than it would be for a team starting cold. Either way, we are not stepping off a cliff.

And on the 10x scenario: even if the Slack partnership lands and we have to migrate, that migration is 3 to 6 weeks. That is recoverable. We are not making a decision that will end the company if we get it wrong. We are making a decision that will cost some rework if we miss, and that is a category of cost this team can pay.

What I want you walking into Wednesday with: this is the kind of decision this team is built to make. You have the data, you have the operational instincts, and you have a PM who is going to back the call rather than relitigate it on Friday. Bring the analysis. Disagree where you disagree. Then commit to whatever the room decides and ship it. You can do this part. The hardest part is already behind you.

See you at 2pm Wednesday.

- Ana
