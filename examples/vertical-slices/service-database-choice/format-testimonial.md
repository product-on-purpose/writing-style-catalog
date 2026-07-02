---
entry_id: testimonial
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Testimonial - Notification Service Datastore Decision

*An internal testimonial, collected by Priya for Lattice Notify's "Decisions We'd Make Again" wiki page, alongside ADR-0023.*

"I built the case for DynamoDB myself: better fit for our write-heavy, point-lookup traffic at 500K events a day. Then Ana asked the question I hadn't: who debugs a brand-new database at 2am, on a four-person rotation that already carries one. We went with Postgres instead: one new schema, a pg_notify queue, read replicas for the fanout reads. First production traffic landed in under two weeks, and the rotation is still one platform deep. If your spike proves the new datastore is the better technical fit, run it anyway, then ask who's on call for it. That question mattered more than mine did."
- Marcus, Backend Engineer, Notification Service team, Lattice Notify
