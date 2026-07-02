---
entry_id: op-ed
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# In Defense of the Boring Database

*By Ana Rivera*

This month my team spent two days close to adopting a second production database, for reasons that sounded airtight in the room and mostly evaporated the moment we asked who would carry the pager for it. We did not adopt it. I think that near miss says more about how engineering teams should choose data stores than the decision itself does.

Every growth-stage team eventually sits in this meeting. A new feature needs a new place to put its data, someone runs the access-pattern numbers, and the numbers point toward a database the team has never operated in production. At Lattice Notify the feature was a real-time notification system: about 500,000 events a day at launch, with a scenario for ten times that within twelve months if a partnership deal we are negotiating with Slack closes. The candidate that fit the access pattern on paper was DynamoDB, built for exactly this kind of write-heavy, point-lookup traffic. The candidate we already knew how to run under production pressure was Postgres. We picked Postgres, and I want to argue the reasoning generalizes well past our one decision.

Start with the question access-pattern analysis never asks: who operates this at two in the morning? My team runs a four-person on-call rotation across eight backend engineers. Every additional production datastore is not a line item, it is a second runbook, a second alerting surface, a second set of failure modes someone has to hold in their head while half awake. Marcus, one of our senior engineers, made a genuinely strong technical case for DynamoDB's fit with our access pattern, and he was not wrong about the fit. He was answering a narrower question than the one that mattered. The database that suits your access pattern on a whiteboard and the database your team can actually operate under production pressure are two different evaluations, and treating them as one is how teams end up debugging an unfamiliar system during an incident instead of during a training exercise.

Second, be suspicious of any architecture decision that is really being made on behalf of a future you do not have yet. Our case for the DynamoDB-shaped future rested on a partnership deal that had not closed. Ten times the load is a real scenario worth planning for, but it is a scenario, not a commitment, and a scenario should not get an equal vote against the traffic we already know we are building for. We wrote the decision down with a number attached instead of a forecast: 5 million events a day, and when we cross it, we revisit the choice with real data. That threshold does more work than another round of debate about whose growth model is more credible, because it turns an argument about the future into a metric we can simply watch.

Third, weigh reversibility honestly, in both directions. If we outgrow Postgres, we lose 3 to 6 weeks to a migration we can plan for, on a system we understand well enough to know exactly when the wall is coming. If we had adopted DynamoDB and it turned out wrong, the more expensive loss would never have shown up on a project plan at all: a team that spent its scarce learning capacity on a second database instead of on the product. Operational knowledge is not one engineer's skill, it is a team's accumulated runbooks, tuned alerts, and rehearsed failure modes, and rebuilding that for a new datastore costs closer to a year than a sprint. That asymmetry, not the access-pattern comparison, is what should decide most of these meetings.

The next time your team is choosing a database, ask the access-pattern question last, not first. Ask who carries the pager, ask what you actually know today instead of what you are forecasting for a deal that has not signed, and pick the tool that turns your team's existing competence into an advantage. The boring answer is usually the disciplined one.

*Ana Rivera is the tech lead for the notification service at Lattice Notify.*
