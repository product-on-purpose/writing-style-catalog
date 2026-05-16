---
entry_id: comparison-contrast
axis: style
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Comparison-Contrast on: Choosing between Postgres and DynamoDB

This document compares two storage options for the Lattice Notify notification system on five dimensions that matter for our situation: access-pattern fit, team familiarity, operational surface area, cross-system query cost, and behavior under the 10x Slack-deal growth scenario. The alternating structure below moves dimension by dimension so the points of contrast stay in focus.

### Access-pattern fit

The notification system is write-heavy, key-lookup by user_id, and time-ordered. **Postgres** handles this pattern at 500K events/day without trouble, but the design has to anticipate sharding work in the 10x scenario. **DynamoDB** is purpose-built for this pattern; partition keys on user_id and sort keys on timestamp do the work natively, and scaling is effectively transparent up to and beyond the 10x scenario. Edge: DynamoDB.

### Team familiarity

**Postgres** is the database all eight backend engineers use daily. Ana has scaled it before. The four-person on-call rotation can debug Postgres incidents from muscle memory. **DynamoDB** is new to the team. Marcus has built a side project on it; nobody else has touched it. The on-call rotation would need ramp-up time and would, in the meantime, be on-call for a system they cannot debug confidently. Edge: Postgres.

### Operational surface area

**Postgres** adds zero new systems; the notification service uses the existing cluster (with a new schema and a queue). **DynamoDB** adds a second database, second alerting setup, second backup and restore process, second IAM model, and second mental model on every incident. Edge: Postgres.

### Cross-system query cost

Analytics, billing, and the product UI all read from Postgres today. **Postgres** keeps cross-table joins in SQL, where they are cheap and where we already have tooling. **DynamoDB** moves those joins into application code or into a downstream warehouse pipeline we would need to build. Edge: Postgres.

### Behavior under the 10x growth scenario

If the Slack deal lands and volume hits 5M events/day in twelve months, **Postgres** requires a sharding or read-replica project. The team has not done this on Postgres but the path is well-documented and reversible. **DynamoDB** absorbs the growth with no engineering work beyond capacity tuning. Edge: DynamoDB, by a clear margin only if the Slack deal actually lands.

### Summary

| Dimension | Postgres | DynamoDB |
|---|---|---|
| Access-pattern fit | Adequate | Excellent |
| Team familiarity | Excellent | Poor |
| Operational surface area | No change | Doubled |
| Cross-system query cost | Native SQL | Application code or pipeline |
| 10x growth behavior | Sharding project required | Native |

**Verdict.** On four of five dimensions, Postgres wins for Lattice Notify today. DynamoDB wins decisively only on the 10x growth dimension, and that dimension is conditional on the Slack-partnership deal. The right question for the Wednesday meeting is not "which database is better" but "how confident are we in the Slack deal?" If confidence is above roughly 70%, the operational cost of DynamoDB becomes the right insurance to pay. Below that, Postgres is the better fit for our situation. Priya should drive that probability estimate by Thursday so the Friday decision rests on the load-bearing question.
