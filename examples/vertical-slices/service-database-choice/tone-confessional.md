---
entry_id: confessional
axis: tone
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Confessional on: Choosing between Postgres and DynamoDB

I owe the team a few things before Wednesday, and I would rather put them in writing than try to slip them into the meeting.

I have been leaning Postgres from the day Priya put this in front of us, and I told myself it was because I had done the load math. That is partly true. But the bigger reason, the one I have not been saying out loud, is that I am the person who would own the operational pain of running a second database, and I am tired. We did the Redis migration eighteen months ago and I underestimated what running two stores would cost the on-call rotation. I did not want to admit that the lesson from that migration was shaping my read of this one, because it felt like I would be arguing from fatigue instead of from architecture.

Marcus, when you pushed back in last Thursday's review and said "you are pattern-matching this to Redis and the patterns are different" - you were right, and I dismissed it too quickly in the moment. The DynamoDB access pattern for notifications is genuinely different from what we hit with Redis. I should have sat with that for a day instead of writing the rebuttal that night.

I also want to own that I have been treating the 10x Slack-partnership scenario as if it were Priya's problem to defend rather than something I should be modeling rigorously. It is a real number from a real deal in motion. If we hit it and we are on Postgres without a migration plan, that failure is mine, not the universe's.

I still think Postgres is the right call for launch. The recommendation has not changed. But I want the room on Wednesday to know that I came to it through a process that was less clean than I made it sound, and that Marcus's case deserved more of my attention earlier than it got.

I will say a version of this in the meeting too. Putting it here first because I needed to write it down before I could mean it.

- Ana
