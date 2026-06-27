---
entry_id: proposal
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Proposal: Postgres as the Datastore for the Notification Service
## Prepared for: Priya, Engineering Lead
## Prepared by: Ana Rivera, Notification Service Tech Lead
## Date: 2026-05-14

## Executive Summary

Lattice Notify is ready to build the notification service, and the architecture meeting on Wednesday resolved the final open question: the service will run on Postgres, not DynamoDB. This proposal sets out the approach, the scope, the 6-week timeline to first production traffic, and the team capacity required. We are asking you to approve this path in the Friday 11am sync so that sprint planning at 2pm can commit the first two weeks of build work without slippage on the ship target.

## The Problem

You need a datastore decision locked before the team can commit to sprint work. Without it, your team cannot sequence the schema design, the job-queue build, or the dashboard instrumentation that are the critical-path items for the 6-week ship target. The choice has been between two real options:

- **Postgres:** Extend the existing primary cluster with a new `notifications` schema and a `pg_notify`-backed job queue. Familiar to the team, operationally bounded, cross-database queries stay simple. Needs tuning work at the 10x growth scenario.
- **DynamoDB:** A new datastore that fits the write-heavy, point-lookup access pattern for notifications. Scales without operator intervention. Requires the team to learn a new system in production, doubles the on-call runbook surface, and has no rollback plan if it goes wrong.

The architecture meeting on Wednesday concluded that operational capacity is the load-bearing constraint for your team at this stage. Your 4-person on-call rotation cannot absorb a second database with a new debugging skillset at launch time.

## Proposed Approach

Build the notification service on Postgres, using a new `notifications` schema in the existing primary cluster and a job queue backed by `pg_notify` and a `notification_jobs` table. Provision read replicas to absorb fanout reads. Establish a documented revisit threshold of 5M events/day at which the team evaluates the DynamoDB path before scaling the Postgres path further.

This approach fits your team specifically for three reasons:

1. Your 8-person backend team has operated Postgres at this load before. The cost of learning DynamoDB in production, on a new service, under a launch timeline, is the cost of every page that hits a team without the mental model yet.
2. The 500K events/day launch target is well within what Postgres handles without intervention. The 10x scenario depends on the Slack-partnership deal closing; designing for it now means designing for the case that may not arrive.
3. Both choices are recoverable. If Postgres cannot handle the 10x load, the migration cost is 3-6 weeks. If DynamoDB turns out to need cross-database joins for product features, the rework cost is comparable, and the team will have learned the wrong tool.

Marcus's case for DynamoDB's access-pattern fit is correct in isolation. We are accepting a slightly worse fit for the access pattern in exchange for a better fit for the team's operational reality. The revisit threshold is when that trade-off inverts.

## Scope and Deliverables

**Included:**

- `notifications` schema design and migration, owned by Sam
- `notification_jobs` table spec covering queue depth, dead-letter handling, and retry policy, owned by Sam
- Queue depth and write-rate instrumentation on the on-call monitoring dashboard, owned by Jordan
- End-to-end internal traffic on the Postgres path covering in-app, email, and Slack push channels
- ADR-0023 published to the wider engineering team, pending your sign-off
- A 5M events/day revisit threshold documented as a tracked metric owned by the on-call rotation

**Not included:**

- Further DynamoDB spike work - the spike in `experiments/notify-ddb/` is complete and will be archived
- Postgres partitioning for the 10x growth scenario - this is scheduled for Q4 if growth tracks projection; it is on the roadmap, not avoided
- Changes to any existing monolith schema outside the new `notifications` namespace
- Slack-partnership integration work - governed by the partnership timeline, not the service build

## Timeline

| Milestone | Owner | Date |
|---|---|---|
| Datastore decision locked | Priya, Ana | 2026-05-16, Friday 11am sync |
| Sprint planning committed | Full team | 2026-05-16, Friday 2pm |
| `notifications` schema and `notification_jobs` spec delivered | Sam | 2026-05-20 |
| On-call dashboard updated with queue depth and write rate | Jordan | 2026-05-22 |
| First end-to-end internal traffic on Postgres path | Ana | 2026-05-29 |
| Postgres partitioning at 3M events/day mark (if growth tracks) | Ana, TBD | Q4 2026 |

The 6-week ship target holds if the datastore lock happens Friday. A delay past Friday pushes Sam's schema work and puts the 2026-05-29 internal traffic milestone at risk.

## Team and Credentials

Ana Rivera (tech lead) is accountable for the architecture and the sprint plan. Sam owns the schema and queue spec, and has designed two prior migration-backed schemas in the existing cluster. Jordan owns the monitoring instrumentation and is the current on-call lead who built the existing alert surface. Marcus completed the DynamoDB spike and documented the comparison; that work closes and Marcus moves to the build track on Friday.

The full 4-person on-call rotation (Ana, Marcus, Jordan, Sam) will absorb notification-service alerts from the first day of production traffic.

## Investment

Reaching first production traffic requires approximately 6 engineer-weeks of effort:

- Schema, queue spec, and migration: 2 engineer-weeks (Sam)
- Service core and delivery channels: 3 engineer-weeks (Marcus, Ana)
- Monitoring, runbook, and operational readiness: 1 engineer-week (Jordan)

Postgres partitioning work at the 10x growth point is estimated at 2-3 engineer-weeks; it is not in this scope and is planned for Q4. No new infrastructure licenses or third-party services are required. The existing Postgres cluster and read-replica capacity cover the 500K events/day launch target.

## Next Steps

Please confirm approval of this proposal in the Friday 2026-05-16 11am sync. Your approval allows sprint planning at 2pm to commit Sam's schema work and Jordan's dashboard work in the first two-week sprint.

If you have concerns before Friday, please reply by end of day Thursday 2026-05-15 so we can address them before sprint planning. If you want to review ADR-0023 in advance, Marcus and I will send you the current draft today.
