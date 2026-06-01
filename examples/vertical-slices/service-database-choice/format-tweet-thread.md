---
entry_id: tweet-thread
axis: format
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

# Tweet Thread - Picking a database, 8 tweets

1/ We just made a database decision at our 50-person startup that I would have made differently 5 years ago. Postgres or DynamoDB for a new real-time notification service. We picked the boring one. Here is why, and why you probably should too.

2/ Setup: Lattice Notify, 8 backend engineers, 4-person on-call rotation, monolith on Postgres. New service needs to handle 500K events/day at launch, possibly 5M in 12 months. Two engineers, two opposing recommendations, three days to decide.

3/ Marcus (senior eng) made a strong case for DynamoDB. He was right on the technical merits. The access pattern (write-heavy, point lookups by user) is exactly what DynamoDB was built for. If this were the only dimension, the meeting would have lasted 10 minutes.

4/ Ana (tech lead) made the operational case for Postgres. We already run it. The on-call rotation has 3 years of muscle memory with it. There is a runbook for every failure mode we have hit. Adopting DynamoDB doubles the operational surface on a 4-person rotation.

5/ The interesting thing is that this was not a "boring vs exciting" argument. It was a "what can we recover from" argument. Both options are recoverable in 3-6 weeks if we are wrong. The difference is which mistake is more predictable to recover from.

6/ The turn: at 8 backend engineers, your operational capacity is one of your scarcest resources. Spending it to adopt a new database needs to clear a high bar. "Better access-pattern fit" is real, but it is the argument that wins at 80 engineers, not 8.

7/ We picked Postgres. Added a documented revisit threshold (5M events/day sustained) so we are honest about when to ask the question again. Ships to production in 3 weeks. Marcus is fine with it because he agrees the operational argument is load-bearing right now.

8/ The takeaway I want you to carry: when you have a database decision in front of you, do not ask "which one fits the access pattern." That answer is in a docs page. Ask "which one's failure mode do we already know how to survive." Pick the boring database, on purpose.
