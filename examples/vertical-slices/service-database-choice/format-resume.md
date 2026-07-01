---
entry_id: resume
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Ana Rivera

ana.rivera@example.com | (303) 555-0148 | linkedin.com/in/ana-rivera-dev | Denver, CO

## Experience

Tech Lead, Backend | Lattice Notify | May 2023 - Present
- Directed the datastore evaluation for a new real-time notification service (in-app, email, and Slack push) launching at 500K events/day; selected Postgres over DynamoDB and recorded the decision in ADR-0023.
- Avoided a second production datastore for the 4-person on-call rotation supporting 8 backend engineers, eliminating a duplicate runbook, monitoring surface, and debugging skillset.
- Delivered the Postgres-backed notification path an estimated 3 weeks faster than the competing DynamoDB proposal by extending the team's existing primary cluster instead of onboarding a new one.
- Designed a `pg_notify`-backed job queue and `notifications` schema, achieving sub-second p95 delivery latency across in-app, email, and Slack channels.
- Set a revisit threshold of 5M events/day ahead of a 10x growth scenario tied to a pending partnership deal, keeping the datastore decision reversible without slowing a 6-week ship target.
- Facilitated a cross-functional architecture review with 5 stakeholders across product, backend, and on-call, converging a contested recommendation into one documented decision within a single week.

Backend Engineer | Boxwood Systems | August 2019 - April 2023
- Owned backend services for a subscription billing product, including on-call rotation and incident response.
- Migrated a legacy batch-processing pipeline onto the team's current job-queue pattern, retiring the last dependency on an unsupported internal tool.
- Mentored new backend engineers through onboarding and their first on-call rotations.

## Education

B.S. Computer Science | Alderbrook University | 2019

## Skills

Databases: Postgres, DynamoDB, schema design, read replica architecture, query performance tuning
Systems: event-driven architecture, job queues (pg_notify), distributed systems trade-off analysis
Practices: architecture decision records, incident response, on-call leadership, cross-functional facilitation
Languages: Python, SQL
