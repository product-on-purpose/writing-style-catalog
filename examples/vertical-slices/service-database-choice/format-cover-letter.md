---
entry_id: cover-letter
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Ana Rivera
ana.rivera@example.com | (303) 555-0148 | linkedin.com/in/ana-rivera-dev | Denver, CO
June 15, 2026

Corvid Labs
Engineering Manager, Backend Platform

Dear Hiring Team,

I'm applying for the Engineering Manager, Backend Platform role. For the last three years I've led the backend team at Lattice Notify, and most recently I did exactly what your posting names as core to this role: picked the datastore for a new service, owned the call in writing, and kept the team aligned behind one answer instead of two.

This spring I directed the datastore decision for a new real-time notification service: Postgres against DynamoDB, with 500K events a day at launch and a possible 10x growth spike riding on a partnership deal that had not yet closed. I chose Postgres, designed the `pg_notify`-backed job queue and schema that carry the traffic today, and wrote the full reasoning into our decision record as ADR-0023, with a documented threshold, 5M events a day, for when we'd revisit the call instead of guessing now. We shipped an estimated 3 weeks faster than the DynamoDB path would have taken, hit sub-second p95 delivery latency, and never added a second production datastore to a 4-person on-call rotation.

That recommendation was not unanimous going in. One of my engineers had a strong, correct case for DynamoDB's fit to our access pattern, and I needed the team behind one answer, not two competing ones. I ran the review that brought 5 stakeholders across product, backend, and on-call to a single documented decision inside a week, and made sure the losing argument's real strength stayed in the record instead of getting argued away. That is the call your posting says this role owns, and it is the one I already know how to make.

I'd welcome the chance to talk with you about this role - do you have time for a call next week?

Sincerely,
Ana Rivera
