---
entry_id: problem-solution
axis: style
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

The default is drift.

When Priya arrives on a team that ships every day and runs on-call, the calendar is already full and everyone is already behind. The default is that she gets a wiki link, a ticket queue to browse, and calendar invites to every recurring meeting. By the end of week one she has attended twelve stand-ups and touched nothing real. By the end of week two she can describe the architecture from a diagram but cannot find where the authentication service actually lives in the repository. She has not shipped anything. She does not yet know if she belongs here.

That is the specific failure mode that needs a plan to prevent: not malice, not neglect - just the absence of deliberate structure on a team that has none to spare.

**What a deliberate two weeks looks like.**

Week one is about reducing the blast radius of confusion. On day one, walk her through the full service map live - not a diagram, but the actual repository layout, the deploy pipeline running in a terminal, the on-call rotation schedule on a screen. At the end of day one she should have deployed a hello-world change to a staging environment using her own credentials. Not because that change matters, but because the deploy cycle should stop being abstract before anything else starts.

Days two through four: pair on a known-small, bounded change. A config value. A log statement. A single-line bug fix with a test. Something where the worst case is a fast revert, not an incident. She writes the PR. You review it the way you would review anyone's PR. She merges it. The specificity here matters - "pair on something small" is not the same as "pair on something where the full cycle is visible from change to deploy, and she drives all of it."

Week two: she owns the next change top to bottom, and you are available but not driving. The shift from paired to independent is the explicit goal of the two weeks.

On the human side: pairing sessions are protected time. They do not move for sprint ceremonies or syncs. Priya learns she belongs partly through what the team treats as interruptible, and a dropped pairing session is a signal she will read correctly.

By the end of week two, she has shipped something real. She knows who owns each service because she has touched those boundaries. And she has been treated as a peer - not a project.
