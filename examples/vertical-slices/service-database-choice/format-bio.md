---
entry_id: bio
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Team Profile - Lattice Notify Engineering Wiki

**wiki.latticenotify.com/team/ana-rivera**

Ana Rivera is the tech lead for Lattice Notify's notification service, and one of eight engineers on the company's backend team. She has spent three years operating Lattice Notify's primary Postgres cluster in production, the experience behind most of the runbooks the 4-person on-call rotation still reaches for today. Most recently, she led the team through the decision to build the new real-time notification service on Postgres rather than DynamoDB, a call written up in ADR-0023 that traded a better-fitting access pattern for the operational familiarity an 8-person team could actually carry. The decision came with a documented threshold, 5 million events a day, for revisiting the call once the team has real growth data instead of a guess. Ana writes occasionally for the Lattice Notify engineering blog about calls like this one, where the boring choice turns out to be the correct one.
