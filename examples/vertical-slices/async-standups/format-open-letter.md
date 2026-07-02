---
entry_id: open-letter
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# An Open Letter to Priya Raman, Director of Engineering
*On making async-first standups the default for every team at Fernbridge Software, not just mine.*

Dear Priya,

Two weeks ago, on June 23, the memo went out confirming that async-first standups are now the Platform team's permanent practice, not a thirty-day experiment anymore. I am one of the three of us in Bangalore that memo was actually about, and before I ask you for anything, I want you to know it worked. I have not set a 9:30pm alarm for a standup since the trial started, and that is the first time I have been able to say that since before this team grew from six people to eleven.

I am posting this to our internal engineering blog instead of sending it to you directly, because you already know it worked. You reviewed our numbers yourself ahead of the Day 30 review, and you raised no objection to making the change permanent. What you have not said yet, at least not anywhere the rest of the company can hear it, is what happens next. That is what I am writing to ask about.

You have seen the shape of these numbers already, but most people reading this have not, so here they are in full. Before the trial, the three of us in India averaged 3.2 standups out of 5 each week, against 4.6 for everyone on a US clock. That was never a motivation problem. It was a 9:30pm problem, built around a 9am Pacific slot that made sense for whoever sat closest to the Seattle office and nobody else. The meeting itself ran fourteen minutes and, by the team's own count, produced about four minutes that changed what anyone did that day; the rest was status nobody needed to hear out loud, and none of it was written down anywhere searchable, which is how we ended up with three separate cases last quarter of someone burning an hour rediscovering a bug a teammate had already solved and mentioned once, out loud, in a meeting nobody could search afterward. Thirty days of a written update by 10am local time, posted to #team-standup, with blockers routed by @mention instead of by whoever happened to still be listening, fixed all three problems at once. On-time posting climbed from 78 percent in the first week to 85.5 percent by the second. Median time from a flagged blocker to a real reply settled at 18 minutes. And for the first time in this team's history, all three of us in India posted on every single weekday of the trial's back half. None of that was luck, Priya. It was a Slack channel, a pinned template, and someone willing to read it every morning.

Here is the part I cannot put a number on, so I will just say it plainly: I do not believe this team is the only one at Fernbridge Software with people on the wrong end of a 9am Pacific meeting. You have peer EMs, which means you have peer teams, and a company that grew this one from six people to eleven in eighteen months has almost certainly grown others the same way, into the same timezone spread, with the same standup nobody ever redesigned to match. I do not have their numbers. I only have ours, and the fact that nobody outside this team has yet stood up and said, in public, that ours are the numbers every distributed team here should be measured against.

Here is what is true as of today: the fix is written down. docs/playbook.md has the template, the on-call expectations, and the Thursday working session design, built by our EM to be copied, not just used once. You know this, because you reviewed it before the Day 30 review. What the rest of the company now knows, because I am telling them here, is that a distributed team can close a timezone-equity gap in thirty days, with no new tools and no new budget. If that playbook sits inside one team's repo for another eighteen months while engineers on other teams keep losing their evenings to a 9am Pacific meeting, it will not be because the fix was hard to find. It will be because you were the person with the standing to say "use this" in front of the whole engineering org, and you had not said it yet.

So here is what I am asking, in public, where the other ten engineers on this team and everyone else who reads this can see the answer too. First, point every EM running a distributed team to docs/playbook.md this quarter, not as a link buried in a wiki, but as something you say out loud at the next leadership sync. Second, ask, by name, which teams still have engineers sitting through a standup built for a clock that is not theirs, and tell them they are allowed to run their own thirty days without asking twice. We already did the part that took nerve. Someone just has to say the rest of the company is allowed to copy it.

Nine in the morning and wide awake,

Devika Nair
Platform team, Bangalore
One of the three engineers ADR-0014 was written about

cc: the Platform team, peer EMs, and anyone else still setting a 9:30pm alarm for a meeting that was never built for their clock
