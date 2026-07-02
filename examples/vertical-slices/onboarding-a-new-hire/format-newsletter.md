---
entry_id: newsletter
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Subject: Ramp Notes #12 - Backend Services runs the protocol on a real hire

Hi everyone,

If you read the last issue, you know I've spent the past few months pushing every team lead I talk to toward writing their onboarding process down instead of trusting it to whoever has free time that week. Backend Services is the first team to run their new version start to finish, on an actual new hire, so this issue is the live version instead of the theory. Her name is Priya, she started a week ago today, and week one just wrapped.

---

Backend Services ships to production daily and shares a single on-call rotation, so a new engineer's system knowledge isn't abstract - it's pager load, carried unevenly until they catch up. The team kept seeing the same two failure modes: a new hire spends week one solving access problems alone rather than interrupting busy teammates, or nothing ships until week three or four, by which point whether they feel like they belong has quietly been decided by the silence before it.

So they wrote the protocol down. ADR-0023 (structured guided pairing) sets out a two-week cycle with a named buddy, daily check-ins, and a first real change chosen and scoped before the new hire's first day, not after. Three domains: access and tooling in the first two days, codebase orientation across week one (two ninety-minute walkthroughs, one traced production request, three one-on-ones with the engineers who own the services she'll touch, a deploy watched start to finish), and a paired first change in week two that Priya drives and her buddy reviews.

Week one, on paper, held. Priya had full access and a working local environment by Monday afternoon - one gap in the setup doc got patched the same day instead of waiting for the next hire to trip over it. By Wednesday she was navigating the three services she'll touch without help. Thursday she co-drove the design session for her first change and caught an edge case the team had missed. Friday she spoke up in the team sync and already has async threads going with three teammates on things that have nothing to do with the formal plan.

None of that is free. The team's own estimate is that the buddy loses 30-40% of their output in week one, tapering to 15-20% in week two. Sprint planning accounted for that before Priya's first day, not after someone noticed they were underwater. That's the part most teams skip, and it's the part that makes the rest of the protocol survive contact with a real sprint.

This week: Priya's first pull request lands Wednesday, Arjun's pairing on the review if she needs it, and Friday closes with a retro that's supposed to ask the belonging question directly instead of assuming two good weeks of output already answered it. I'll tell you next issue whether it did.

---

A few things worth pulling from this if you're building your own version:

- [ADR-0023: Structured Guided Pairing](../backend-services/adr-0023-guided-pairing.md) - three domains, one named buddy, one task chosen before the new hire's first day instead of after. Steal the structure, not the specifics.
- [Backend Services onboarding guide](../backend-services/README.md) - written for two readers at once, the new hire and the buddy. Notice how much of it is instructions for the buddy, not just the new hire.
- [Issue 9: the two failure modes](archive/ramp-notes-09.md) - the piece this whole protocol is designed against. Worth a re-read if you're still deciding whether structure is worth the buddy's lost capacity.
- [How Backend Services scopes a first task](../backend-services/README.md#week-two) - one service, one data model, a test that fits in an hour, nothing that needs on-call context. Small enough to be real, small enough that nobody's pager depends on it going right.

---

Back after Friday's retro with whatever didn't survive contact with the sprint - there's always at least one thing. Talk soon.

Mei

You're getting this because you lead a team or buddy a new hire somewhere in the org. Manage preferences or unsubscribe: intranet.example.internal/newsletters/ramp-notes
