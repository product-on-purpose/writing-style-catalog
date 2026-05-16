---
entry_id: reverent
axis: tone
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

## Reverent on: Choosing between Postgres and DynamoDB

Before the meeting on Wednesday, I want to take a moment to set down what we are actually doing, because I do not think it is what the calendar invite suggests.

We are not picking a database. We are choosing the shape of the system that will carry every notification Lattice Notify sends for the next several years. Every alert that wakes a customer at the right moment, every message that arrives too late and is no longer useful, every silent failure that nobody sees, every paged engineer at 3am who has to walk back through a schema they did not write - all of that lives downstream of the decision we make in this room at 2pm on Wednesday.

The choice deserves to be approached with the seriousness it earns rather than the seriousness we usually grant it. Five hundred thousand events a day, at launch, is not an abstraction. It is five hundred thousand separate moments of someone, somewhere, being told something that matters to them. Within a year, if the partnership we are not allowed to name yet comes to pass, it may be five million. The systems we build now are the substrate of attention for people we will never meet.

Ana, who has carried the operational weight of our existing systems through outages most of us have already forgotten, brings to this decision the memory of what it costs to run something at 3am. Marcus, who has spent two weeks in the access patterns of a system that does not yet exist, brings the discipline of imagining a load we have not yet felt. Priya, who carries the timeline, holds the deadline so that the rest of us are free to think. These are not roles. They are forms of care, distributed across the team, and the decision we are about to make rests on all three.

Whatever we choose on Wednesday, I would ask the room to choose it with attention to what it will mean two years from now, to the engineer on call who inherited it, and to the customer who will not know our names but whose trust we are quietly accepting.

Friday we will tell Priya. Wednesday we will choose. Let us choose carefully.

- Ana
