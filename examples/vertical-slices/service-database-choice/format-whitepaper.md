---
entry_id: whitepaper
axis: format
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

# Operational Capacity as a First-Class Constraint in Datastore Selection
## A Framework for Mid-Stage Engineering Organizations, with a Worked Example from Lattice Notify

**Authors:** Ana Rivera (Tech Lead, Lattice Notify), Marcus Chen (Senior Engineer, Lattice Notify), Priya Shah (Product Manager, Lattice Notify)
**Published:** 2026-05-16
**Version:** 1.0

## Executive Summary

Datastore selection at mid-stage engineering organizations (15-60 engineers) is commonly framed as a technical comparison between access-pattern fit, throughput characteristics, and feature coverage. We argue this framing is incomplete. At organizations of this size, the dominant constraint is operational capacity: the network of runbooks, monitoring, alert tuning, and rotation-level muscle memory that an organization has built around its existing datastores. This capacity is expensive to expand and treating it as a fixed cost in the analysis leads teams to adopt technically-superior datastores their operators cannot reliably operate.

We propose a Datastore Selection Matrix that weights operational capacity at 0.25 (the highest single-dimension weight in our rubric) and pairs every recommendation with an explicit revisit threshold. We illustrate the framework with the May 2026 notification service decision at Lattice Notify, a 50-person Series B startup with 8 backend engineers and a 4-person on-call rotation. The decision compared extending an existing Postgres footprint against adopting DynamoDB for a new real-time notification system handling 500K events/day at launch and potentially 5M events/day in 12 months. The framework selected Postgres, with a revisit threshold of 5M events/day sustained.

The recommendation here is not "always pick the boring database." It is: at mid-stage organizations, the technical-fit dimension is necessary but not sufficient. Operational capacity, recovery cost, and the cross-store query landscape need to be weighted explicitly. Doing so will, in most mid-stage situations, favor the incumbent datastore - and this is the correct outcome, not a conservative bias to be corrected for.

## Introduction

The question of which datastore to use for a new service appears regularly at every growing engineering organization. It is treated as a technical decision and is most commonly debated on technical grounds: access pattern, throughput, consistency model, query expressiveness. The literature on the topic is rich, and the major vendors publish well-argued cases for their respective tools.

This whitepaper argues that for mid-stage engineering organizations - those with 15 to 60 engineers - the technical debate, while necessary, has been overweighted. The constraint that most often determines whether a datastore choice succeeds or fails at this scale is operational capacity: the team's accumulated knowledge of how to operate, debug, and scale a specific datastore in production. We will present a framework that elevates operational capacity to a first-class constraint and illustrate it with a worked example.

The audience is engineering leaders, architects, and product managers responsible for service-level technology decisions at mid-stage organizations.

## Background

Datastore selection frameworks in the published literature emphasize fitness criteria oriented around the workload: query patterns (relational, document, key-value, graph), consistency requirements (strong, eventual, causal), throughput shape (read-heavy, write-heavy, mixed), and durability needs. These are necessary inputs and we do not contest their importance.

What is less commonly addressed is the organizational dimension. Brewer's CAP theorem describes a property of distributed systems; it does not describe the property of a team being asked to operate two distributed systems instead of one. Vendor comparison matrices catalog feature coverage; they do not catalog the runbooks the team has not yet written.

The closest published work to our framework is the SRE literature on operational toil and the related work on team topologies by Skelton and Pais. We extend that thinking specifically into the datastore-selection decision.

## The Three Common Failure Modes

In our review of datastore decisions across our own organization and peer organizations at similar stages, three failure modes recur.

**Failure mode 1: Adopting the technically-superior datastore the team cannot operate under load.** The team selects a datastore that fits the workload better than the incumbent. Six months later, the on-call rotation has not built the muscle memory to debug it under stress. A 3am page becomes an outage. The decision is reversed at significant cost.

**Failure mode 2: Sticking with the incumbent datastore past its breaking point.** The opposite failure. The team treats "we already know it" as a permanent answer rather than a current answer. The system reaches a scaling wall that was foreseeable. Recovery requires a hurried migration under pressure, not a planned one.

**Failure mode 3: Adopting both, then operating neither well.** The team avoids the choice by adopting the new datastore for the new service while keeping the incumbent. Operational capacity is now split. Both systems suffer from inadequate attention. This is the most common failure at the 30-50 engineer scale.

The framework we propose is designed to avoid all three by making operational capacity an explicit, weighted input and requiring an explicit revisit threshold with every recommendation.

## The Datastore Selection Matrix

Our framework evaluates each candidate datastore across eight weighted dimensions. The full matrix is presented in our internal technical reference document; the dimensions and weights are summarized here.

| Dimension | Weight |
|-----------|--------|
| Access-pattern fit | 0.15 |
| Throughput at launch volume | 0.10 |
| Throughput at upside-scenario volume | 0.10 |
| Team operational knowledge | 0.25 |
| On-call rotation surface area impact | 0.20 |
| Cross-database query needs | 0.10 |
| Recovery cost if wrong | 0.05 |
| Vendor lock-in / portability | 0.05 |

The recommendation produced by the matrix is not the highest-scoring candidate. It is the highest-scoring candidate whose downside scenarios are recoverable given the team's operational capacity. Every recommendation must be paired with a revisit threshold: a measurable condition under which the decision will be re-evaluated.

## Worked Example: Lattice Notify Notification Service

In May 2026, Lattice Notify (a 50-person Series B startup with 8 backend engineers and a 4-person on-call rotation) faced a datastore decision for a new real-time notification service. The service was expected to handle 500K events/day at launch, with a 10x growth scenario tied to a pending Slack-partnership deal that could materialize within 12 months.

Two candidates were evaluated: extending the existing Postgres cluster with a new schema and a `pg_notify`-backed job queue, or adopting DynamoDB as a second datastore. The architecture meeting was held Wednesday May 13 at 2pm Pacific.

The technical analysis (Access-pattern fit, Throughput) modestly favored DynamoDB. The organizational analysis (Team operational knowledge, On-call surface area, Cross-database query needs) significantly favored Postgres. The weighted scores were Postgres 0.79, DynamoDB 0.68. The recommendation was Postgres, with a revisit threshold of 5M events/day sustained.

The decision was recorded in ADR-0023 and locked at the Friday May 16 11am sync, in time for the 2pm sprint planning.

## Implications and Recommendations

For engineering leaders at mid-stage organizations, we offer four recommendations:

1. **Weight operational capacity explicitly.** Stop treating it as a soft consideration. Quantify it in your selection process. Our matrix uses 0.25 as the single largest weight; your number may differ, but it should be material.
2. **Require a revisit threshold with every datastore recommendation.** A recommendation without a threshold is an open-ended commitment. A recommendation with a measurable threshold is a planned decision point.
3. **Resist the "adopt both" path unless you have explicit operational headroom to absorb the second system.** At 8-30 engineers, this is almost never true.
4. **Recognize that picking the incumbent datastore is not conservatism; it is honest accounting.** A team that picks the boring datastore on purpose, with a documented threshold for revisiting, has done more rigorous work than a team that picks the exciting one on principle.

For product managers, we recommend insisting on the revisit threshold in any decision that crosses your sprint planning. Open-ended technical commitments compound into product risk.

## Conclusion

The dominant constraint on datastore selection at mid-stage engineering organizations is not technical fit. It is operational capacity. Frameworks that fail to weight operational capacity explicitly will systematically select datastores their organizations cannot operate well. The framework presented here, illustrated with the Lattice Notify notification service decision, offers one approach to making operational capacity a first-class constraint.

Open questions remain. The weights in our matrix are calibrated from our own incident data and the experience of peer organizations; they are not derived from a controlled study. The revisit-threshold mechanism has been in place for 18 months and has not yet been stress-tested by a revisit event. We expect the framework to evolve as more data accumulates and we welcome correspondence from organizations applying it.

## References

- Skelton, M., and Pais, M. (2019). *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution Press.
- Beyer, B., Jones, C., Petoff, J., and Murphy, N. R. (Eds.) (2016). *Site Reliability Engineering: How Google Runs Production Systems.* O'Reilly Media.
- Brewer, E. (2012). "CAP twelve years later: How the rules have changed." *IEEE Computer*, 45(2), 23-29.
- Lattice Notify internal documentation: ADR-0023, Datastore Selection Matrix v2.3, ARB Charter.

## Appendix

The full Datastore Selection Matrix specification, including dimension definitions, scoring guidance, and worked counterexamples, is available in the Lattice Notify technical reference at `arb/datastore-selection-matrix.md`. The ADR-0023 record of the notification service decision is at `adr/0023-postgres-notification-service.md`.
