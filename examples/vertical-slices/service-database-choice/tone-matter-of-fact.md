---
entry_id: matter-of-fact
axis: tone
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Matter of Fact on: Choosing between Postgres and DynamoDB

Decision brief for Wednesday 2pm architecture meeting. Decision required by Friday.

Context. Lattice Notify is adding a real-time notification system. Launch volume is 500K events per day. A pending Slack partnership, if signed within 12 months, would push volume to approximately 5M events per day. The backend team is 8 engineers. The on-call rotation is 4 people. The existing core product runs on Postgres.

Option A. Stay on Postgres. Requires a new notifications schema, a partitioned events table, and a background queue for delivery. Operational surface area unchanged. Team has shipped at the 500K/day scale on Postgres before. Load test at 2x launch volume returned p99 write latency of 18ms. Migration path to DynamoDB later, if required, is 3 to 6 weeks of work for 2 engineers.

Option B. Add DynamoDB as a second store for notification events. Access pattern fits Dynamo well. Scales naturally through the 10x scenario without intervention. Team does not currently operate DynamoDB in production. Adds one production data store to the on-call rotation. Cross-database queries between notifications and the existing product data become application-layer joins. No rollback plan if the new system fails to meet operational targets.

Cost of getting it wrong. Choosing Postgres and tripping the 10x scenario costs 3 to 6 weeks of migration work. Choosing DynamoDB and not tripping the 10x scenario costs ongoing operational load on a 4-person rotation for the duration the second database is in production.

Positions. Ana leans Option A on operational and team-capability grounds. Marcus leans Option B on access-pattern and scaling grounds. Priya has no preference and needs a decision.

Recommendation. Ship on Option A. Design the schema for portability. Marcus to own a DynamoDB migration design doc with a defined trigger threshold of 3M events per day or partnership signing.

Outstanding items for the meeting. Confirm the 3M threshold. Confirm who covers the migration doc within the next sprint. Confirm Priya gets the decision by end of day Wednesday so Friday planning is unblocked.

- Ana
