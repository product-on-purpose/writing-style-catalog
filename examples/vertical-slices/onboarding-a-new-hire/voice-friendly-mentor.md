---
entry_id: friendly-mentor
axis: voice
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Getting Priya from "where's the bathroom" to "I shipped a real change" in two weeks is achievable. You just need to resist one temptation: front-loading everything you know.

Think of it like teaching someone to drive. You do not start with traction physics. You start with: ignition, mirrors, gear, go. Priya needs a working mental model first - the complete picture comes after she has one to build on.

**Week one: ground, then orient**

Start with access and tooling on day one. Not the full tour - just access. She needs to read the codebase, run the service locally, and get into the chat tool and ticket tracker. Spend the first morning on those three things and you've already avoided the most common new-hire stall: two days blocked on a missing permission.

Once she can see the system running, walk her through one request out loud - from the point it enters the service to the point a response goes back. Do it in a call, not a document. Why a call? Because you'll see the moment a concept lands, and that's your cue to move on.

The part that usually trips people up on a service-oriented backend is not the code itself - it's why the services are split the way they are. Name that gap directly: "The boundaries feel arbitrary at first. They'll make sense once you've seen a few on-call incidents."

**Week two: pair on something real**

Now that she has a mental map of the system, pick a small issue together. Something with a narrow blast radius - a label fix, a missing validation, a config adjustment. Walk through it with her, but let her drive. Your job is to name the landmines, not clear them for her.

When she pushes that first change, make a small moment of it. Shipping is how engineers start to feel real on a team. Belonging is not something you can tell someone to feel; it happens when they do something that matters.
