---
diff_pair_id: format-adr-vs-whitepaper-service-database-choice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
axis_varied: format
entry_a: adr
entry_b: whitepaper
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Format swap - `adr` vs `whitepaper`

**Topic:** How to choose between Postgres and DynamoDB for a new service
**Axis varied:** format
**A:** `adr` - A short structured document that captures a significant architectural decision, its context, and its consequences.
**B:** `whitepaper` - A long-form authoritative document presenting a position, framework, or analysis - the format for setting position-of-record on a substantive topic.

## What to notice

This is the wide pair on this topic, and the clean one: both sides recommend Postgres with a
5M events/day revisit threshold, so the content is genuinely held constant and the container
is the only variable. The difference is **who the writing is accountable to.**

**A is accountable to this team, later.** `adr` is a record with a status field, and
"Accepted" is doing real work: it marks the decision as closed and the document as the thing
you will be pointed at in six months when someone asks why. Its sections exist to serve that
future reader, not to persuade a present one: Context names the two options and the three
forces, Decision states what to build in implementable terms (`notifications` schema,
`pg_notify` plus a `notification_jobs` table, read replicas), and Consequences is split
Positive / Negative / Neutral. That three-way split is the format's integrity mechanism: the
Negative section obliges the author to write down the cost in their own document, which is
why A concedes "Marcus's argument about access-pattern fit is correct in isolation." An ADR
that has nothing in Negative is not finished. Scope is exactly one decision, and named
people appear because accountability is local: "Priya has the decision recorded."

**B is accountable to strangers, generally.** `whitepaper` has to earn a reader who has no
stake in Lattice Notify, so it inverts the relationship between claim and case: the argument
is the product, and the decision becomes a *worked example* inside it. Note where the
Lattice Notify decision actually appears - one section, roughly a fifth of the way from the
end, under the heading "Worked Example." Everything before it builds a general apparatus:
a titled thesis (operational capacity as a first-class constraint), a bounded audience
(15-60 engineers), a positioned literature review (Team Topologies, the SRE book, CAP), a
named failure-mode taxonomy, and an eight-dimension weighted matrix. It carries the trappings
of publication: authors, version, date, references, appendix. It also does something an ADR
never does - it argues against itself in a Conclusion that concedes the weights "are not
derived from a controlled study" and that the revisit mechanism "has not yet been
stress-tested."

**The sharpest single tell.** Look at what each does with the number 0.25. A does not have
it; the ADR just asserts that operational capacity was "the load-bearing one" and moves on,
because a record does not need to justify its weighting to anyone outside the room. B builds
a whole matrix to make that weight explicit and defensible, because a stranger will not
accept "load-bearing" on this team's authority.

**If you are choosing between them:** pick `adr` when the decision is made and the audience
is the people who will maintain it. Pick `whitepaper` when the decision is the evidence and
the audience is people who do not work here. The same facts fit both; the reader you owe is
what changes.

---

## A: `adr`

# ADR-0023: Use Postgres for the Notification Service

## Status

Accepted

## Context

Lattice Notify is launching a real-time notification system that needs a new persistent data store. The system will handle 500K notification events per day at launch, with a 10x growth scenario in 12 months if the pending Slack-partnership deal closes. The decision sits between two candidates:

- **Option A: Postgres.** Extend the existing Postgres footprint with a new schema, add a job queue, and absorb the resulting scaling work. The team has operated Postgres at this scale before. Cross-database queries against the existing monolith data stay simple.
- **Option B: DynamoDB.** Adopt a new datastore that fits the notification access pattern (write-heavy, point-lookups by user) and scales without operator intervention. The team has no production DynamoDB experience. Ops surface area doubles. There is no rollback plan if it goes wrong.

Three forces pushed this decision:

**Team operational capacity.** We have 8 backend engineers and a 4-person on-call rotation. Adding a second database adds a second runbook, a second monitoring surface, a second backup story, and a second debugging skillset on every page. We have measured this cost before in a separate workstream and it is non-trivial.

**Growth uncertainty.** The 10x growth scenario depends on a deal that has not closed. Designing the system for the larger scenario, when the smaller one is the certain one, optimizes for the case that may not arrive.

**Reversibility cost.** If we choose Postgres and outgrow it, we incur 3-6 weeks of rework to migrate. If we choose DynamoDB and find we need cross-database joins for product features, we incur similar rework plus a team that has learned the wrong tool. The asymmetry is small; both choices are recoverable.

Marcus made a strong case for DynamoDB's access-pattern fit. Ana raised the operational capacity concern. The architecture meeting on Wednesday confirmed that the operational concern is the load-bearing one.

## Decision

Build the notification service on Postgres, using a new schema (`notifications`) in the existing primary cluster and a job queue backed by `pg_notify` plus a `notification_jobs` table. Provision read replicas to absorb fanout reads. Add a documented threshold (5M events/day sustained) at which we revisit DynamoDB before scaling the Postgres path further.

Priya has the decision recorded for the Friday sprint planning.

## Consequences

### Positive

- Single operational surface for the 4-person on-call rotation. No new runbooks, no new monitoring, no new debugging skillset on call.
- Cross-database queries (joining notifications to users, accounts, workspaces) remain simple SQL.
- The team ships the launch scope on familiar ground. Estimated 3 weeks faster to first production traffic than the DynamoDB path.
- The decision is reversible: if we cross the 5M events/day threshold, we have the data and the operational margin to plan a migration.

### Negative

- We will likely need to do non-trivial Postgres tuning at the 10x growth point: partitioning the notifications table, tuning the job queue, possibly sharding. This work is real and is on the roadmap, not avoided.
- Marcus's argument about access-pattern fit is correct in isolation; we are accepting a worse fit for the access pattern in exchange for a better fit for the team's operational reality.
- If the Slack deal closes and growth arrives faster than 12 months, we hit the rework window earlier than planned.

### Neutral

- The `notification_jobs` table becomes a new operational concern: queue depth, dead-letter handling, retry policy. These are familiar problems on a familiar platform.
- The 5M events/day revisit threshold becomes a tracked metric. The on-call rotation owns the dashboard.

---

## B: `whitepaper`

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
