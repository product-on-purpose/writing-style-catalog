---
entry_id: classical-argument
axis: style
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Classical Argument on: Choosing between Postgres and DynamoDB

**Claim.** Lattice Notify should build the notification system on Postgres with a queue, not on DynamoDB. The decision the architecture meeting on Wednesday should ratify is the one Ana has been leaning toward: stay on the storage layer the team already operates.

**Grounds.** Three facts about our situation support this claim. First, the team has shipped at the 500K-events-per-day scale on Postgres before. The runbooks exist, the alerting exists, and the four-person on-call rotation can debug Postgres incidents at 3am. Second, the 10x growth scenario is conditional on the Slack-partnership deal landing - a real possibility but not a certainty. Third, our analytics, billing, and product-surface queries all live in Postgres today; introducing DynamoDB introduces a cross-database join problem that becomes application-layer code we have to write, test, and maintain.

**Warrant.** The evidence supports the claim because the cost of a wrong decision is asymmetric. Choosing Postgres and being wrong costs three to six weeks of rework if the Slack deal lands and we have to migrate. Choosing DynamoDB and being wrong costs an entire year of operational drag on an eight-engineer team learning a new system, on a four-person on-call rotation now responsible for two storage engines, and on every analytics query that has to span two stores. The first error is bounded and recoverable on a predictable schedule. The second error is diffuse, ongoing, and very hard to roll back. When error costs are asymmetric, you choose the option whose downside you can actually afford.

**Rebuttal.** One might object, as Marcus does, that DynamoDB matches the notification access pattern - write-heavy, key-lookup, time-ordered - more naturally than Postgres does, and that committing to Postgres now sets us up for a painful sharding project in twelve months if the Slack deal lands. This objection is real and it is the strongest version of the Dynamo case. The response is twofold. First, "natural fit" is a benefit measured at steady state; the cost of getting to steady state on a system the team has never operated is paid every day until then. Second, a twelve-month-out sharding project on Postgres is a problem we will face having spent twelve months at scale on a system we know. A twelve-month-out scaling project on Dynamo would be a problem we face having spent twelve months learning a system that has bitten us in production along the way. We do not avoid pain by switching technologies; we trade known pain for unknown pain.

**Conclusion.** Postgres is the right choice for Lattice Notify's notification system. The claim survives its strongest objection because we are optimizing for the cost of being wrong, not just the elegance of the access pattern. Priya should call the decision by Friday, and the team should plan the next sprint on the Postgres path.
