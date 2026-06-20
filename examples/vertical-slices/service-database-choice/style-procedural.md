---
entry_id: procedural
axis: style
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## How-To Tutorial on: Choosing between Postgres and DynamoDB

This tutorial walks you through making a defensible storage choice between Postgres and DynamoDB for a new service, using the Lattice Notify notification system as the worked example. By the end, you will have produced a written recommendation ready to present at the Wednesday 2pm architecture meeting and committed to the team by Friday.

### Prerequisites

Before you start, make sure you have:

- A clear definition of the new service and its expected access pattern (Lattice Notify: write-heavy, key-lookup by user_id, time-ordered).
- Launch volume estimate and a 12-month growth scenario, with a probability for that scenario (500K events/day at launch; 5M at 10x; 60% probability per the CRO).
- The current on-call rotation size and current familiarity with each candidate (4-person rotation; familiar with Postgres, unfamiliar with DynamoDB).
- Knowledge of which other systems will need to read or join against this service's data (billing, analytics, product UI - all on Postgres).
- Empty document at `docs/decisions/2026-05-15-notification-storage.md`.

### Steps

#### 1. Write the access pattern in one sentence.

Open the decision doc. Type the actual access pattern, not a category. For Lattice Notify: "Write a notification record per event, read recent notifications for a given user_id ordered by timestamp."

#### 2. List every other system that will read or join against this data.

Bullet list. For Lattice Notify: billing (joins user, plan, notification volume), analytics dashboards (joins workspace, user, event), product UI (reads notifications by user_id). All currently on Postgres.

#### 3. Look up your current on-call rotation and their database familiarity.

Find the rotation roster. Confirm how many engineers are on it and which databases they have operated in production. For Lattice Notify: 4 engineers, all fluent in Postgres, none have run DynamoDB in production.

#### 4. Write the launch volume and 10x scenario with the probability of the 10x case.

One line each. "Launch: 500K events/day. 10x scenario: 5M events/day in 12 months. Probability: 60%."

Warning: do not skip the probability. A growth scenario without a probability is a guess. Get the number from your PM, your CRO, or your sales lead, not from your own estimate.

#### 5. Score each option against five criteria.

Use this table format. Score each option on access-pattern fit, team familiarity, operational surface area, cross-system query cost, and 10x growth behavior. Use simple labels: excellent, good, adequate, poor.

| Criterion | Postgres | DynamoDB |
|---|---|---|
| Access-pattern fit | Adequate | Excellent |
| Team familiarity | Excellent | Poor |
| Operational surface area | No change | Doubled |
| Cross-system query cost | Native SQL | Application code |
| 10x growth behavior | Sharding project required | Native |

#### 6. Calculate the expected operational cost of each option using the probability.

For each option, estimate the cost if the 10x scenario hits and the cost if it does not. Multiply by the probability and sum. Round to weeks of engineering work. For Lattice Notify: DynamoDB-from-day-one costs roughly 40-50 engineer-weeks of operational drag over twelve months in either scenario. Postgres-with-deferred-trigger costs roughly 0 in the no-Slack-deal case and roughly 3-6 weeks of migration if the deal lands.

#### 7. Name the load-bearing constraint.

Pick the one criterion that, if violated, makes the option unsafe regardless of other scores. For Lattice Notify: on-call rotation operational safety. This converts the decision from "which is better" to "which is acceptable."

#### 8. Write the recommendation in one paragraph.

Lead with the choice and the trigger condition, if any. For Lattice Notify: "Ship on Postgres with a queue. Pre-commit to a DynamoDB migration if real volume crosses 2M events/day on a 30-day rolling average."

#### 9. Schedule the architecture meeting and circulate the doc 24 hours in advance.

Calendar invite, doc link in description. For Lattice Notify: Wednesday 2pm Pacific. Send the doc Tuesday by 2pm. Notify Ana, Marcus, Priya, and the four-person on-call rotation.

#### 10. Run the meeting. Capture objections in the doc.

Take live notes inline. If the recommendation survives the meeting, mark the decision committed and assign owners. If a load-bearing assumption is challenged, defer the decision by 24 hours and re-run the math.

#### 11. Commit the decision to the team channel by Friday morning.

Single message in the engineering channel. Include the recommendation, the trigger condition, the owner, and a link to the decision doc. Sprint planning runs Friday 2pm against this decision.

### How to know it worked

You have succeeded if, at sprint planning Friday afternoon:

- The team can name the choice without checking the doc.
- The trigger condition (if any) is recorded with a defined threshold and owner.
- Sprint planning produces concrete tasks against the chosen storage path.
- No engineer can identify a load-bearing criterion that was not considered.

If any of these fail, the decision is not yet shippable. Reopen the doc and re-run from step 5.
