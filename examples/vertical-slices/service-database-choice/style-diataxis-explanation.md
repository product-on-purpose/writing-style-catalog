---
entry_id: diataxis-explanation
axis: style
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Diataxis Explanation on: Choosing between Postgres and DynamoDB

This piece is not a how-to. It does not walk through configuring either database, nor does it tell you which one to pick for the Lattice Notify notification system on Wednesday. The goal is conceptual: by the end, you will understand why the choice between Postgres and DynamoDB is harder than it looks, and why that difficulty is structural rather than accidental.

### Why these two databases represent two different theories of storage

Postgres is a relational database. Its design intent is to model rich relationships between entities and to answer arbitrary questions about those relationships through SQL. The schema is rigid up front; the queries are flexible later. DynamoDB is a key-value (and document) store. Its design intent is to serve one well-defined access pattern at predictable latency and unlimited scale. The schema is loose; the queries must be designed up front. These are not two products competing on the same axis. They are products from different worldviews about what a database is for.

This matters because the Lattice Notify notification system has, at launch, exactly one access pattern: "give me the recent notifications for user X, ordered by time." That is the kind of access pattern DynamoDB was built to serve. But Lattice Notify also has analytics, billing, and product-surface queries that span the user, the notification, the workspace, and the integration. Those are the kinds of queries Postgres was built to serve. Neither database is bad at the wrong job; both are designed for the right one.

### Why familiarity is a real engineering quantity, not a feeling

There is a temptation to treat "the team knows Postgres" as a soft consideration that should be weighted lightly because real engineers can learn anything. This is a misunderstanding of what familiarity is. Familiarity is the property that the alerts trigger on the right thresholds, that the runbooks reflect the actual failure modes, that the on-call engineer has seen this exact stack trace before and knows what query to run. Familiarity is, in effect, a body of cached knowledge that was paid for in past incidents. Discarding it has the same cost as paying for it again.

This is why the four-person on-call rotation at Lattice Notify is a load-bearing consideration in the choice. The rotation is the body that holds the familiarity. Adding a second database does not add a small new system; it bifurcates the body that holds the operational knowledge.

### Why "scale" is the wrong word for what is being decided

The Postgres-versus-Dynamo conversation often gets framed as a scale question: Postgres handles small workloads, Dynamo handles big ones. This framing is wrong because Postgres handles very large workloads in production at companies much bigger than Lattice Notify. The real distinction is not scale but the shape of growth.

Postgres scales by deliberate engineering interventions: read replicas, partitioning, sharding. Each intervention requires a team to plan it, execute it, and operate it. DynamoDB scales by configuration: you increase the throughput setting and the system grows. The difference is not how much volume each can handle but how much engineering work is required per unit of growth. For a team facing 500K events/day at launch and a possible 5M events/day in twelve months, the question is whether the team has the engineering bandwidth for the deliberate interventions Postgres would require, or whether they need the property that the database scales without their attention.

### Why the decision is bound to a probability, not a number

A common mistake in storage decisions is treating projected volume as if it were known volume. Lattice Notify's "10x growth in twelve months" is conditional on the Slack-partnership deal closing. That deal has a probability, not a certainty. A correctly framed decision uses the probability: the expected operational cost of each option is the sum of the costs in each scenario, weighted by the probability of that scenario.

This is why Priya's request to the CRO for a probability estimate is not a procurement step. It is the input that converts the architectural choice into a decision under uncertainty rather than a guess about the future. Without the probability, the team is choosing between databases. With the probability, the team is choosing between theories of how to absorb risk.

Understanding this is the point. Whether you choose Postgres or Dynamo on Wednesday is downstream of whether you have grasped what the choice is actually about.
