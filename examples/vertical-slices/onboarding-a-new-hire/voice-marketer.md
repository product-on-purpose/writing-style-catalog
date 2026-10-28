---
entry_id: marketer
axis: voice
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-5-5
review_status: reviewed
---

Your last new hire took three or four weeks to ship a single real change, and by then whether she felt like part of the team had already been decided by the silence of those weeks. You know the shape of it: she solves her own access problems quietly rather than interrupt anyone, and the first commit lands long after the first impression already formed.

Here is what we ran instead, on a team that deploys daily and shares an on-call rotation: a two-week guided pairing protocol with one named buddy, a printed checklist, and a first real change picked before the new hire's first day. Not "sit beside someone and absorb." Not a written runbook she works through alone. Not handing the whole thing to the tech lead and hoping it holds under sprint pressure. We tried versions of all three and dropped them.

Priya's buddy owned the access checklist and caught the one gap, a missing VPN cert step, the same day it surfaced. Two 90-minute walkthroughs covered service topology and deployment tooling in week one. The team scoped her first change before she arrived: one service, no on-call risk if it went wrong. She opened the pull request by the Wednesday that closed week two. It shipped two days later, and her name was in the deployment log before the formal onboarding window ended.

The cost is real and we're not going to hide it from you. Her buddy lost roughly 30 to 40 percent of his capacity in week one and 15 to 20 percent in week two. Put that in sprint planning explicitly or the protocol fails quietly, the same way unstructured onboarding does. And if the first change isn't scoped before day one, week two has no fallback built in. The buddy improvises, and that's variance a checklist can't absorb.

What it buys you: the new hire's access problems have a named owner instead of falling into a gap nobody's watching, and belonging gets decided by what she's done by week two instead of by what nobody said in week one.

Before your next hire's start date, pick the first change they will ship. The buddy, the checklist, and the walkthroughs all organize around that one decision.
