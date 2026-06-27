---
entry_id: pitch-deck
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## Slide 1: The Decision We Cannot Delay

Lattice Notify launches in six weeks. Choosing the wrong datastore now means 3-6 weeks of rework later - at the worst possible moment.

- 500K notification events per day at launch
- Two viable options: Postgres (known) and DynamoDB (better access-pattern fit, zero team experience)
- Decision gate: Friday 11am sync with Priya
- Sprint planning Friday 2pm requires a confirmed datastore to proceed

## Slide 2: Recommendation - Postgres

Build the notification service on the existing Postgres cluster with a new `notifications` schema and a `pg_notify`-backed job queue.

- One operational surface for the 4-person on-call rotation
- Cross-database joins (users, accounts, workspaces) stay simple SQL
- Team has operated Postgres at this scale; DynamoDB production experience is zero
- Revisit threshold documented at 5M events/day sustained - migration path exists if growth demands it

## Slide 3: Why This Decision Must Be Made Now

The spike is done. The architecture meeting reached consensus. Every day without a locked decision is a day the sprint team cannot commit work.

- DynamoDB spike (`experiments/notify-ddb/`) complete: access-pattern fit confirmed, operational cost quantified
- Wednesday architecture meeting (Ana, Marcus, Priya, Jordan, Sam) landed on Postgres
- The Slack-partnership deal that triggers the 10x growth scenario has not closed; designing for it now is premature
- Six weeks to first production traffic; the decision window closes Friday

## Slide 4: How the Postgres Path Works

A single cluster carries the full notification lifecycle at launch scale.

- **Write path:** events land in `notifications` schema, picked up by `notification_jobs` worker pool within ~50ms
- **Read path:** read replicas absorb fanout reads; sub-second p95 delivery to end users
- **Queue:** `pg_notify` + `notification_jobs` table with dead-letter, retry, and queue-depth on familiar tooling
- **Threshold:** at 5M events/day sustained the on-call rotation owns the dashboard metric that triggers revisit

## Slide 5: What the Evidence Shows

We did not guess. We ran the spike and put both options through the architecture review.

- DynamoDB spike: access-pattern fit is real; operational overhead is also real (second runbook, second monitoring surface, second debugging skillset on call)
- Postgres at 500K events/day: no new tooling, no new runbooks, on-call rotation load unchanged
- Architecture meeting outcome: after operational cost was quantified, the room aligned on Postgres
- Marcus (DynamoDB advocate) is aligned on the recommendation and the revisit-threshold language

## Slide 6: The Tradeoff We Are Accepting

We are buying operational stability now and accepting access-pattern impurity. This is the right trade at this team size.

- What we gain: ~3 weeks faster to first production traffic; single on-call surface; no new debugging skillset required
- What we give up: DynamoDB's cleaner fit for write-heavy, point-lookup-by-user access patterns
- Rework cost if Postgres is outgrown: 3-6 weeks to migrate, triggered by a clear data signal (5M events/day)
- Rework cost if DynamoDB and cross-database joins are both needed: equivalent rework plus a team that learned the wrong tool for this situation

## Slide 7: The Team That Will Execute

We have experienced operators and a clear ownership structure for every milestone.

- 8 backend engineers with production Postgres experience
- 4-person on-call rotation covering Mon/Wed/Fri/weekend
- **Ana Rivera (tech lead):** owns schema design, Postgres partitioning roadmap, ADR-0023 authorship
- **Sam:** `notifications` schema and `notification_jobs` table spec delivered by May 20
- **Jordan:** queue-depth and write-rate added to on-call dashboard by May 22
- First end-to-end internal traffic on the Postgres path targeted for May 29

## Slide 8: What We Are Asking For

Two approvals this week unblock six weeks of execution.

- **Priya - Friday 11am:** confirm ADR-0023 Accepted and lock the datastore decision
- **Engineering leadership - by Monday:** review ADR-0023 so it can be published to the wider eng team and close the decision loop
- **Sprint planning - Friday 2pm:** first two weeks of build work committed, assuming decision is locked
- **Success signal:** first end-to-end internal traffic on the Postgres path by May 29 - on the six-week ship schedule
