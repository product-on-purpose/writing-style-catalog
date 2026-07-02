---
entry_id: customer-story
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Priya: In the Deployment Log by the End of Week Two

## About Priya

Priya joined the Backend Services team as a backend engineer on Monday, June 22. The team ships to production daily and runs a shared on-call rotation, work Priya would need to be ready for within her first month.

## The Challenge

Before Backend Services adopted a structured onboarding protocol, new engineers ran into one of two outcomes. Either they spent week one solving access and tooling problems on their own, blocked but reluctant to interrupt teammates already carrying a daily deploy cadence, or they didn't ship a first change until week three or four. By then, whether they felt like they belonged on the team had already been decided by the silence of the weeks before it.

Priya was walking into the same daily-deploy, shared-on-call environment that had produced both patterns. The team needed her contributing safely within two weeks, without quietly draining the teammate assigned to bring her up to speed.

## The Solution

Backend Services paired Priya with Arjun under a two-week guided-pairing protocol, with Mei running point as onboarding DRI. The protocol covered three things in a fixed order: access and tooling on days one and two, codebase orientation across week one, and a paired first change in week two, scoped by the team before Priya's start date so nobody had to improvise what her first contribution would be.

Arjun owned a printed access-and-tooling checklist and didn't mark an item done until Priya had verified it herself. Two 90-minute guided walkthroughs, one on service topology and one on deployment and on-call tooling, gave her a working map of the system in her own notes, not Arjun's. For week two, the team had already chosen her task before she arrived: one service, no on-call risk if it went wrong. Priya drove the change; Arjun reviewed and paired on blockers.

## The Results

Priya had full access and a working local environment by Monday afternoon of her first week. By Wednesday, she could navigate the three services she'd been assigned without hand-holding, having already found the test harness and the team's naming conventions on her own. On Thursday, she co-drove the design session for her scoped change without prompting and caught an edge case the team had missed.

Her first pull request went up Wednesday, July 1. It was reviewed and merged by Friday, July 3, with Arjun pairing as support. Her name was in the deployment log before the two-week window closed, which is what the protocol was built to produce rather than leave to chance.

The cost was real, and the team planned for it instead of absorbing it as a surprise: Arjun lost roughly 30-40% of his capacity in week one and 15-20% in week two, accounted for in sprint planning before Priya's first day.

Belonging tracked alongside the technical ramp. Priya observed a live incident response and attended the handoff call before the end of week one. She contributed two points to the Friday architecture discussion, and three teammates had already started async threads with her on topics outside the formal onboarding plan.

"I never had to guess whether it was okay to interrupt someone," Priya said at her two-week retro on July 3. "The checklist had an owner, the walkthroughs were already on my calendar, and I knew from day one which change was mine to ship. Two weeks in, I know who to ask, not just where to look."
