---
entry_id: definitional
axis: style
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Definitional on: Choosing between Postgres and DynamoDB

**A "service database choice" is the decision a team makes about which persistent storage technology will own the primary data for a new service, evaluated against the specific access pattern of that service, the operational capacity of the team that will run it, and the probability-weighted scenarios for how the workload will evolve.** That definition is doing the work in this piece. Every section below tests it.

### The facets of the definition

The definition has four load-bearing parts. **First, it is about a new service**, not an existing one - the cost of changing storage in flight is so different from choosing storage at greenfield time that the two decisions are not the same decision. The Lattice Notify notification system qualifies because it is greenfield; modifying the existing Postgres monolith would not. **Second, it concerns the primary data store** - not caches, not read replicas, not search indexes, not warehouses. The candidate that owns the source of truth is what we are choosing. **Third, the access pattern of the service is a constituent of the choice**, not a downstream concern. The notification system's pattern (write-heavy, key-lookup, time-ordered) is part of the question, not a check at the end. **Fourth, the team's operational capacity is also constituent.** A storage technology the four-person on-call rotation cannot debug is not actually a candidate, even if the access-pattern math says it should be.

### What this decision is not

It is not a benchmark comparison. A document that ranks Postgres and DynamoDB by write throughput on a synthetic workload is performing a benchmark; it is not making a service database choice. Marcus's weekend prototype produced useful numbers, but the numbers alone could not decide the question.

It is not a technology preference. A team that says "we like Postgres" or "we believe in Dynamo" is expressing affinity, not making a service database choice. Ana leans Postgres and Marcus leans Dynamo; the definition requires them to engage the access pattern and the operational capacity, not just their priors.

It is not a vendor evaluation. Comparing AWS pricing pages or AWS support tiers is a procurement activity. A service database choice may use procurement inputs but cannot be reduced to them.

It is not the same decision as the long-term storage architecture. The Wednesday 2pm meeting at Lattice Notify is choosing storage for one service at one moment. The probability-weighted scenarios (Slack deal closes, Slack deal does not close) are part of the choice, but a permanent architectural commitment is not. A service database choice that pre-commits to a trigger for revisiting is still a service database choice, not an architecture mandate.

### Boundary case: the deferred migration

Suppose Lattice Notify ships on Postgres but pre-commits to a Dynamo migration if volume crosses a defined threshold. Does that decision count as a service database choice? It does. The definition requires the team to choose the primary store for the new service; choosing Postgres today and naming the trigger condition for change is still a choice about which technology owns the data at launch. The trigger does not dissolve the choice; it conditions it.

### The definition, refined

A service database choice is therefore the launch-time selection of the primary persistent store for a new service, made against the access pattern, the operational capacity, and probability-weighted growth scenarios, with optional pre-committed trigger conditions for revisiting. A reader given Lattice Notify's situation can now decide whether what happens on Friday counts. It does.
