---
entry_id: email
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

**To:** Volta team; Engineering org; Product leadership; Customer Experience; Finance
**From:** Renata Coyle, VP Engineering
**Subject:** Checkout rebuild shipped - fourteen months of dual-track work, two near-misses, and a clean launch [FYI, no action needed]

The Volta team shipped the new checkout platform to 100% of traffic on May 9. The legacy flow is retired. This message is a record of what it took.

The project ran fourteen months. For every one of those months, the team was building a replacement system while the original remained live, processing real orders, with real consequences if either path broke. There was no clean room. Every release the team shipped had to coexist with the system it was meant to replace, which meant the complexity of maintaining two live flows was a constant overhead on top of the actual build.

We missed two launch dates.

The first slip came last August. Priya Mehta surfaced a data consistency gap between the two systems three days before the then-planned go-live. She raised it at a moment when everyone was ready to ship and the pressure to move was high. She was right to raise it. The team held, spent two weeks resolving the issue, and carried on. The second slip came in February, after Tomasz Wielecki and the platform side caught a race condition that would have triggered under concurrent session load - the kind of load a major sale event produces. Fixing it took eight days. Both delays were the correct call.

The final rollout ran over six hours on May 9. We saw our highest single-day order volume since the company started tracking that number. The system held. Anika Soren ran incident command for the full window. Darian Osei had been running load models against this exact scenario for six weeks before the launch date. The rollout held because they built a ceiling they knew would not move.

Cart abandonment in the new flow is tracking below baseline at fourteen days out. We will report formally at thirty days.

No action needed from anyone on this message. I am sending it because work this hard, done this quietly, deserves to be named before the team moves to whatever is next. The Volta team spent fourteen months on a problem that will not look like much from the outside. That is the nature of infrastructure work done well. The people who know what it took are the ones who did it.

Thank you, Volta.

Renata Coyle
VP Engineering
