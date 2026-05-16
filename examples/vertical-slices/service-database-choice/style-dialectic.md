---
entry_id: dialectic
axis: style
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Dialectic on: Choosing between Postgres and DynamoDB

### Thesis: Lattice Notify should stay on Postgres.

The Postgres position, in its strongest form, is not "use what you know." It is this: the cost of a wrong storage decision is not symmetric with the cost of a right one. A team of eight backend engineers running a four-person on-call rotation has a finite operational budget. Every system that rotation has to be on-call for consumes a share of that budget that compounds: more runbooks, more alerts, more 2am decisions made under pressure. Adding a second database is not a one-time cost; it is a recurring tax on every incident, every hire, every quarter for as long as the second database exists. Postgres at 500K events/day is a known cost; the team has shipped at this scale before. Sharding work in twelve months is also a known cost; the path is documented and the team can practice on staging. Choosing Postgres is choosing the option whose costs we can see.

### Antithesis: Lattice Notify should adopt DynamoDB.

The Dynamo position, in its strongest form, is not "Dynamo is better at this." It is this: the access pattern of a notification system, write-heavy, key-lookup, time-ordered, is the pattern DynamoDB was built for. Choosing Postgres is choosing to spend the next year writing code that compensates for an impedance mismatch the original engineers of Postgres would acknowledge if asked. Queues to absorb the write spikes, indexes carefully tuned for the time-ordered access, eventual sharding work that will pull two engineers off feature delivery for six weeks - all of this is operational cost that does not exist in the Dynamo option because the technology already handles it. The Postgres position treats "familiar" as if it were free, but familiar is just the form unfamiliar costs take when you have already paid them. If the Slack deal lands, the team will eventually need to operate Dynamo or something like it at scale; the question is whether they learn on a system at 500K events/day where errors are recoverable, or on a system at 5M events/day where errors are expensive. The right time to learn an unfamiliar system is when the cost of error is lowest, which is now.

### Synthesis

Both positions are correct about what they emphasize, and both are incomplete in the same way.

The Postgres position is right that operational capacity is a binding constraint, that the four-person rotation cannot absorb a second storage system without cost, and that the cost of being wrong should be measured in the dimension of "can we recover" rather than only "is the access pattern optimal." The Dynamo position is right that familiarity is not the same as zero cost, that the access pattern fit is not a luxury but a structural property that compounds, and that the right time to learn a system is before the workload demands it.

What becomes visible when both are held at once is that the decision is not actually between Postgres and Dynamo at the storage layer. It is between two theories of risk. The Postgres position is the theory that uncertainty should be absorbed by familiar systems. The Dynamo position is the theory that uncertainty should be absorbed by systems matched to the workload. Neither theory is true in all cases. Both are true in some cases.

For Lattice Notify, at this moment, with a 60% Slack-deal probability and a four-person rotation, the synthesis points to a third path that neither original position contained: ship on Postgres now to absorb the launch uncertainty with familiar tooling, and pre-commit to a Dynamo migration trigger tied to actual volume rather than projected volume. This is not a compromise. It is what becomes visible only by holding both positions seriously. Ana and Marcus were both right, and the architecture they need is the one their disagreement built.
