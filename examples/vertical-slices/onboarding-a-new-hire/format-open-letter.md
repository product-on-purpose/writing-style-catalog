---
entry_id: open-letter
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# An Open Letter to Dana Reyes, Director of Engineering

Dear Dana,

Two weeks ago, Priya joined backend services as our newest engineer. This past Friday she shipped her first change end to end, and her onboarding retrospective was the calmest one I have run. I am not writing to report that success. I am writing because what made it possible is not something you have funded, and I have raised that with you before, privately, without an answer. I am putting it in writing this time, and posting it where the rest of engineering leadership can see it, because the private version of this ask has not worked.

You approved ADR-0023 in principle when backend services adopted it: a two-week guided pairing protocol with a named buddy, a printed access checklist, two structured codebase walkthroughs, and a first real change scoped and waiting before the new hire's first day. You have seen the results. Priya had a working local environment by Monday afternoon of week one. She could navigate the three services she needed without help by day three. She opened a pull request in week two instead of week four, which is when new hires on this team used to ship their first change, if they did not quietly give up on asking for help before then. None of that happened by default. It happened because Arjun and I built it as a checklist and then executed it exactly, on top of our regular workload.

Here is the part you will not find in Priya's status reports. Arjun lost real capacity in week one pairing with her on access and tooling, and he is carrying it again this week reviewing her first pull request on top of his own. The ADR says that cost runs 30 to 40 percent of a buddy's time in week one and 15 to 20 percent in week two, and it says plainly that sprint planning has to account for that or the protocol fails silently. Sprint planning has not accounted for it. Arjun absorbed it because he is generous and because Priya's ramp mattered to him. That is not a plan. That is a team getting lucky with who happened to be free.

I keep thinking about a line in the ADR that reads almost like an aside: that whether a new hire believes they belong here gets decided by the silence of their first few weeks, not by anything anyone says to them later. Priya did not get silence. She got a checklist with her name on it, two people who showed up when they said they would, and a real change with her name in the deployment log before the end of week two. I do not want that to keep depending on whether a new hire's team happens to have someone like Arjun to spare, and neither should you.

Every team lead who reads this now knows what I know: the protocol works, it is written down, and it costs a specific, known amount of a senior engineer's time that we are currently treating as free. If it stays a backend-services habit instead of an engineering-wide standard, the next team without a spare senior engineer will skip it, and their new hire will get the version Priya did not: a quiet first week, a first change nobody scoped in advance, and a belonging question nobody thought to ask.

So here is what I am asking you to do, in writing, where the rest of engineering can see the ask next to the answer. Adopt the guided pairing protocol in ADR-0023 as the default onboarding standard for every engineering team, not only backend services. Require sprint planning to carry buddy capacity as a named line item for a new hire's first two weeks, the same way we carry any other planned work, instead of treating it as time a generous engineer finds somewhere. And tell me, before the next new hire's start date on any team, whether that is happening. I would rather have a direct no than another quiet nothing.

Mei
Onboarding DRI, Backend Services
Posted to the internal engineering blog and #eng-leads, because the private ask did not get an answer.
