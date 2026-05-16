---
entry_id: confident
axis: tone
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Confident on: Choosing between Postgres and DynamoDB

Recommendation for Wednesday: ship the notification service on Postgres.

Three reasons.

First, 500K events a day is not the scale at which Postgres breaks. It is the scale at which a clean schema, a partitioned events table, and a properly tuned background queue handle the load with headroom. This team has shipped that pattern before. Marcus's load test confirmed it: p99 write latency at 2x projected launch volume came in at 18ms with no tuning beyond defaults.

Second, the operational cost of adding DynamoDB is larger than it looks. Eight engineers, four-person on-call rotation, one production database we operate well today. Adding a second store doubles the runbook surface area, splits cross-database queries that the product will eventually need, and gives us no rollback if the new system surprises us. That is a permanent tax for a hypothetical benefit.

Third, the 10x Slack-partnership scenario is the strongest case for DynamoDB, and it is still a hedge. If the deal closes and we trip 3M events a day, migration takes 3 to 6 weeks of focused work from two engineers. That cost is recoverable. The cost of running two databases for a year while waiting to see if a deal lands is not.

Marcus's DynamoDB case is technically sound on the access pattern. He is right that Dynamo scales more naturally for the read shape we expect. He is not wrong; he is optimizing for a different time horizon. We optimize for launch and the next twelve months. He optimizes for the steady state two years out. Both views are valid; only one fits the situation we are actually in.

Plan for Wednesday: confirm Postgres, agree on the schema review checkpoint at end of sprint, assign Marcus to write the migration design doc so we are not flat-footed if the partnership signs. Priya gets her decision by Friday.

This is the call. Push back in the meeting if I have missed something, but assume we are moving on it unless someone surfaces evidence the load test or the operational analysis missed.

- Ana
