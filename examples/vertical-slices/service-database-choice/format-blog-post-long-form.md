---
entry_id: blog-post-long-form
axis: format
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

# Why We Picked the Boring Database (Again)

There is a particular meeting that recurs at every growing startup. A new service needs a new datastore. Two engineers, both right in their own way, arrive with opposing recommendations. The PM wants a decision by Friday. The tech lead leans toward the thing the team already knows. The senior engineer leans toward the thing that fits the access pattern. Everyone in the room has read the same blog posts. Nobody has the answer.

We just had that meeting at Lattice Notify. The new thing was our real-time notification system. The two candidates were Postgres (which already runs our monolith) and DynamoDB (which our senior engineer Marcus, with some justification, called "the obvious choice for this access pattern"). The decision was due in three days. I want to write about how we made it, because I think the way we made it is more useful than the answer we landed on.

## The actual question is not the question

The framing on Monday was "Postgres or DynamoDB for the notification service." That is not the actual question. The actual question, once you sit with it for an hour, is something like: which of these two options has a smaller blast radius if we are wrong, given the team we have, the growth we expect, and the time we have to recover?

Marcus is right that DynamoDB fits the access pattern. We are writing 500K notification events per day at launch, with potential for 5M if the Slack-partnership deal lands. The reads are mostly point lookups by user. This is exactly what DynamoDB was designed for. If we were a team of 80 engineers picking from a clean slate, this would be a one-meeting decision.

We are not that team. We are 8 backend engineers with a 4-person on-call rotation, one production database we know how to operate, and a monolith that the new service will need to query. Ana, our tech lead, has been operating Postgres at our scale for three years and has a runbook in her head for every failure mode we have hit. Marcus has read the DynamoDB docs and built one personal project on it. The team is asymmetric on this dimension by a factor of ten.

The actual question is whether the access-pattern fit advantage of DynamoDB is larger than the operational capacity disadvantage of adopting it. And the only honest answer is: probably not, but we have to think about it carefully, because the cost of getting this wrong in the other direction is also real.

## Cost of being wrong, in both directions

Here is a framing that helped us. If we pick Postgres and we are wrong, what does that cost? We hit a scaling wall sometime in the 12-month window if growth accelerates, and we do 3 to 6 weeks of migration work to move the notification system to a different store. We have the data to know when we are approaching the wall. We have the team to do the migration.

If we pick DynamoDB and we are wrong, what does that cost? We discover that cross-database queries against the user data in the monolith are harder than we estimated, we discover that the 4-person on-call rotation cannot reliably debug DynamoDB throttling at 3am, and we have no rollback because we built six weeks of product on top of it. The cost is similar in weeks but worse in confidence: we have a team that has learned a tool that did not serve them.

Both are recoverable. Neither is free. The interesting fact is that the recovery cost of being wrong about Postgres is more predictable than the recovery cost of being wrong about DynamoDB, because we have done one before and not the other. Predictable recovery is itself a form of insurance.

## Why "the team already knows it" is a load-bearing argument

There is a class of engineering decision where "we already know how to operate this" is treated as a soft argument. It is presented as conservative, risk-averse, maybe even a little embarrassing - the implication is that a more sophisticated team would just learn the new thing. I want to push back on this framing.

Operational knowledge is not a static property of a person. It is a network effect across a team. Ana knowing Postgres at our scale is not just Ana's personal expertise; it is the runbooks she has written, the alerts she has tuned, the failure modes the on-call rotation has rehearsed, the monitoring dashboards that already exist, and the muscle memory of every engineer who has paged into a Postgres incident. Replacing that network with DynamoDB is not a 2-week learning curve. It is a year of rebuilding it.

At a 50-person Series B, your operational capacity is one of the scarcest things you have. Spending it to adopt a new database needs to clear a high bar. "Better access-pattern fit" is a real argument, but it is the kind of argument that wins at 80 engineers, not at 8.

## What we actually decided

We picked Postgres. We are building the notification service on a new schema in the existing primary cluster, with a queue backed by `pg_notify` and a jobs table. We have a documented revisit threshold (5M events/day sustained) at which we will pause and ask the question again, with the data we have by then.

Marcus is fine with this. Not because he changed his mind on access-pattern fit, but because he agrees that the operational argument is the load-bearing one given who we are right now. Priya has the decision for sprint planning. We will ship to production in three weeks.

The interesting thing about this decision, in retrospect, is how little of it was about Postgres or DynamoDB. The technical comparison took an hour. The operational comparison took two days. The hard part was getting honest about what kind of team we are, and what kind of mistakes we can afford to recover from.

If you are in a meeting like this next week, that is the question I would put on the whiteboard first. Not "which database fits the access pattern." That one has an answer in a docs page. The harder question is: which of these mistakes can we recover from? Pick the database whose failure mode you already know how to survive.
