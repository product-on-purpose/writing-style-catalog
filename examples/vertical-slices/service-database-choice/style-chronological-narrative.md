---
entry_id: chronological-narrative
axis: style
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Chronological Narrative on: Choosing between Postgres and DynamoDB

On Monday morning, May 11, Priya pinged the architecture channel and said the notification system needed a storage decision by Friday. The Slack-partnership conversation had moved to a term sheet stage over the weekend, and if it landed, Lattice Notify would be staring down ten times the daily volume by next spring. The team needed to commit to a path before sprint planning.

That same afternoon, Ana opened a draft doc and laid out the Postgres case. She had shipped the monolith at 500K events per day before, on Postgres, with a queue in front. She knew the runbooks. The on-call rotation knew the runbooks. The work was unglamorous but mapped.

Tuesday morning, Marcus pushed back in the doc comments. He said the access pattern for notifications, write-heavy, key-lookup, time-ordered, was exactly what DynamoDB was built for. He noted that the 10x growth scenario would force a Postgres sharding project in twelve months that nobody on the team had done before. He attached a benchmark he had run on a personal account over the weekend.

Tuesday afternoon, Ana read the benchmark, then read it again, then walked over to Marcus's desk. They spent ninety minutes whiteboarding. By the end of the session, Ana had granted that DynamoDB matched the access pattern. Marcus had granted that adding a second database meant the four-person on-call rotation now needed to be on-call for two systems instead of one, and that cross-database joins for the analytics dashboards would become application-layer code.

Wednesday at 2pm Pacific, the architecture meeting opened with Priya restating the deadline. Ana presented the Postgres-with-queue option. Marcus presented the DynamoDB option. Then, instead of the debate Priya had been bracing for, Ana said something the room had not expected: "If the Slack deal closes, we should be on Dynamo. If it does not, we should stay on Postgres. The decision we are actually making is how much we believe in the Slack deal."

The room got quiet. Priya said she could get a probability estimate from the CRO by end of day Thursday. Marcus said he could prototype the Dynamo schema in parallel so that either decision Friday morning would have a real artifact behind it. The meeting ended without a verdict.

Thursday afternoon, the CRO came back with sixty percent confidence on the Slack deal closing in Q3. Priya routed that number to the channel. Ana posted a single sentence: "At sixty percent, I think we should go with Dynamo and accept the operational cost."

Friday at 10am, the decision shipped to the team. Sprint planning ran at 2pm.
