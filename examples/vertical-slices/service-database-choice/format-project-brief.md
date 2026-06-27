---
entry_id: project-brief
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Notification Service Datastore Selection - Project Brief

## Goal

Select and document the persistent datastore for the Lattice Notify notification service before sprint planning begins on May 16.

## Background

Lattice Notify is launching a real-time notification system that needs a new persistent store. Two candidates are in contention: extending the existing Postgres footprint with a new schema, or adopting DynamoDB for its write-heavy access-pattern fit. The team needs a documented decision with clear tradeoffs before committing build work in sprint planning. A choice made without a shared rationale risks mid-sprint reversal, which would jeopardize the 6-week ship target.

## Scope

### In scope

- Evaluate Postgres and DynamoDB against the notification service access pattern (500K events/day at launch, potential 10x growth in 12 months)
- Assess the operational cost of each option against the 4-person on-call rotation and the team's existing Postgres expertise
- Produce a written recommendation and a draft ADR (ADR-0023) capturing the decision and its consequences
- Define a growth threshold at which the chosen approach should be revisited

### Out of scope

- Schema design and migration plan (follows from the decision; Sam owns this in sprint 1)
- Evaluation of datastores other than Postgres and DynamoDB
- Infrastructure provisioning or cost modeling
- Notification service feature requirements

## Constraints

- Decision must be final before 2pm sprint planning on Friday, May 16
- The team has no production DynamoDB experience; adding a new datastore doubles the on-call surface area
- The 10x growth scenario depends on a deal that has not closed; the certain scenario is 500K events/day at launch
- The 6-week ship target is fixed

## Success Criteria

- A written ADR-0023 with status Accepted, reviewed and signed off by Priya
- Marcus and Ana aligned on the recommendation before it goes to Priya
- A documented growth threshold specifying when the team revisits the chosen approach
- Sprint planning proceeds on May 16 with no datastore open question remaining

## Team

- Owner: Priya (decision authority)
- Contributors: Ana Rivera (tech lead, recommendation author), Marcus (DynamoDB spike lead), Sam (schema spec), Jordan (on-call dashboard)
- Informed: Engineering leadership, #notify-arch channel
