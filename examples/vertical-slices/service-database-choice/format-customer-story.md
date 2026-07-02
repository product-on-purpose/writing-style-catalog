---
entry_id: customer-story
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# The Notification Service Team: 3 Weeks Faster to Production by Staying on Lattice Notify's Existing Postgres Platform

*An internal case study, shared with other Lattice Notify teams weighing a new datastore against the company's existing Postgres platform.*

## About the Notification Service Team

The Notification Service team is one of eight backend groups at Lattice Notify, which delivers in-app, email, and Slack push notifications at sub-second latency. Led by tech lead Ana Rivera, the team spent May building a new real-time notification system and needed a persistent datastore that could carry launch traffic, and whatever came after it, without adding a second thing to operate.

## The Challenge

The new system needed to handle 500,000 notification events a day at launch, with a possible 10x jump within 12 months if a pending partnership deal closed. Two paths were on the table: extend the company's existing Postgres cluster with a new schema and a job queue, or adopt DynamoDB, a datastore built for the write-heavy, point-lookup pattern that notifications actually produce.

Backend engineer Marcus ran a spike against DynamoDB (`experiments/notify-ddb/`) and confirmed the access-pattern fit was real. But the team had never run DynamoDB in production, and taking it on meant a second runbook, a second monitoring surface, and a second skillset added to a four-person on-call rotation that already carried the existing Postgres footprint.

"Marcus's case for DynamoDB wasn't wrong," Ana said. "It just wasn't the constraint that mattered most. The team that has to carry the pager gets a vote too."

## The Solution

The team stayed on Lattice Notify's existing Postgres platform. They built a new `notifications` schema in the primary cluster, added a job queue backed by `pg_notify` and a `notification_jobs` table, and provisioned read replicas to absorb fanout reads at delivery time. Priya, who had drafted the service's PRD, recorded the decision as ADR-0023, with a documented threshold, 5 million events a day sustained, at which the team would revisit DynamoDB before scaling the Postgres path any further.

Nothing about the platform itself had to change to take the new service on. Same cluster, same backup story, same monitoring the on-call rotation already knew how to read, just a new schema and a new queue running alongside everyone else's.

## The Results

The team's own estimate put the Postgres path about 3 weeks faster to first production traffic than the DynamoDB alternative, and the schedule held: first end-to-end internal traffic landed within two weeks of the decision. The four-person on-call rotation still owns exactly one database platform, no second runbook, no second monitoring surface, no second skillset to reach for on a 2am page.

"The fastest way to ship this was to not invent a new way to operate it," Ana said. "We already knew how this database breaks, how to back it up, and who to page. That's worth more at 2am than a marginally better fit for the access pattern."

The service now delivers notifications to a user's in-app inbox in under a second, with the job queue picking up new events in about 50 milliseconds. Cross-database queries against the existing user, account, and workspace tables stayed plain SQL instead of a second query language. Jordan's write-rate and queue-depth additions to the on-call dashboard mean the 5-million-events-a-day threshold for revisiting DynamoDB is now something the team watches trend toward, not a guess made under pressure.

"I ran the spike. DynamoDB would have fit the access pattern better," Marcus said. "But the team that has to run it on a Friday night mattered more than the pattern match. I'd make the same call again."
