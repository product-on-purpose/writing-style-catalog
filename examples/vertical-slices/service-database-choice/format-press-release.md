---
entry_id: press-release
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

**FOR IMMEDIATE RELEASE**

**Lattice Notify Selects PostgreSQL for New Notification Service**

*The service will run on the company's existing Postgres platform instead of a new database.*

DENVER, May 16, 2026 - Lattice Notify today announced that its new real-time notification service, which delivers in-app, email, and Slack notifications for applications built on the Lattice Notify platform, will run on PostgreSQL. The decision follows an architecture review that also considered DynamoDB, and keeps Lattice Notify's infrastructure on a single database platform as usage grows.

The new service is designed to process more than 500,000 notification events per day at launch, using a dedicated schema and job queue built on Lattice Notify's existing PostgreSQL cluster, with a target of sub-second p95 delivery latency across all channels. The engineering team evaluated DynamoDB for its fit with the service's write-heavy access pattern, then chose to extend PostgreSQL after weighing that fit against the cost of operating and monitoring a second production database.

The team has set an internal threshold of 5 million notification events per day at which it will revisit the decision. Additional performance tuning, including table partitioning and job-queue optimization, is already planned well ahead of that threshold.

"We already know how to run Postgres at this scale, and that mattered more to us than picking the theoretically ideal data store for one access pattern," said Ana Rivera, Tech Lead, Lattice Notify. "Every additional database is one more thing our on-call engineers have to understand at two in the morning. We would rather put that time into the product."

The service is expected to begin carrying internal traffic by the end of May 2026, ahead of a broader rollout to Lattice Notify's customers.

**About Lattice Notify**
Lattice Notify builds real-time notification infrastructure that engineering teams use to deliver in-app, email, and chat alerts to their own customers. The platform is built and operated by a small, senior engineering team with a focus on reliability and operational simplicity. Lattice Notify is privately held.

###

**Media Contact:**
Ana Rivera
Tech Lead
ana@latticenotify.com
(303) 555-0148
