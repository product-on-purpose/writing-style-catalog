---
entry_id: newsletter
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Subject: Platform Notes #12 - The async standup trial is over, and we are not going back to the meeting

Hey everyone - regulars here know I have been threatening to write this issue since the Week 2 numbers first looked good. As of June 23, it is no longer a trial: the Platform team's daily 9am standup is dead, replaced by an async post in Slack, and I made it official in a memo to the team that day. Here is the fuller story, for everyone who is not sitting in our standup channel already.

---

The Platform team grew from 6 to 11 people over about a year and a half, and somewhere in there we ended up spread across four timezones: US Pacific, US Eastern, UK, and India. Nobody had redesigned the daily standup for that reality. It stayed a 9am Pacific call, which lands at 9:30pm for anyone on IST. Q1 attendance told the story without needing commentary: our India-based engineers were averaging 3.2 out of 5 standups a week, against 4.6 for the US-based half of the team. That gap was never about motivation. It was about asking people to be on a work call at 9:30pm.

The other problem was that none of it stuck. We logged three separate incidents last quarter where someone burned more than an hour reworking a problem that had already been raised and solved out loud in a standup nobody could search afterward. And when we actually timed the meeting, the fourteen minutes it ate broke down to about four minutes of real signal - a blocker, a dependency, something that changed what someone did that day. The other ten minutes was status nobody in the room needed delivered live.

We wrote it up properly as ADR-0014 and ran a 30-day trial starting May 19. The daily call was replaced with a post in `#team-standup`: three fields, Shipped, In progress, Blocked or at risk, due by 10am your own local time, blockers tagged with an @mention. On-call reads the channel every morning and chases anything tagged. The old standup slot became a 60-minute Thursday working session, for discussion that actually needs to happen live.

The Day 30 numbers backed up what Week 2 had already suggested. On-time posting climbed from 78 percent to 85.5 percent and held there. Median time from an @mention to a real reply settled at 18 minutes, against a sync model where a 9am blocker often waited until afternoon for a response. Every India-based engineer posted on every single weekday across the trial's final two weeks, for the first time in this team's history. It was not a clean win along the way: by Day 30, three engineers were still writing 200-plus word posts, on-call triage was running to 25 minutes some mornings against a 10-minute target, and Thursday session attendance had a couple of rough weeks. A few engineers also said in their end-of-trial 1:1s that they missed the small daily social contact the old standup gave them, which the Thursday session has not fully replaced.

Priya Raman pulled the Day 30 numbers together for the review, and the team voted to make the format permanent. The post-length problem got fixed with two exemplar posts pinned to the channel and a hard three-bullet ceiling; we reviewed the on-call triage load too, and splitting the rotation into two roles turned out not to be necessary once the ceiling was in place. The Thursday session kept its existing time. I signed the memo making all of this the Platform team's default practice on June 23, with `docs/playbook.md` as the reference doc going forward. The honest lesson for me was not about the tooling. It was that we had been charging our India teammates an equity tax we could not see until the Q1 numbers made us go looking for it, and an unglamorous Slack template fixed more of that in five weeks than a year of good intentions had.

---

A few things worth a look if any of this sounds familiar for your own team:

- `docs/playbook.md` - The now-official mechanics: what counts as blocked versus in progress, what on-call actually owes the channel each morning, all of it.
- ADR-0014 - The original case for anyone who wants the full argument, including why we passed on just rotating the meeting time or paying for a tool like Geekbot instead of using a Slack template.
- `docs/trial-retro.md` - The finished Day 30 retro, with the parts that did not work included on purpose: the long posts, the on-call triage load, and the uneven Thursday attendance.
- `docs/thursday-agenda.md` - What the 60 minutes is for now that it is not a status meeting. Mostly design reviews and the arguments that never fit cleanly in a thread.

---

Next issue: whether the on-call decision stays closed once a few more people rotate through it. If you are running your own version of this experiment, I would like to hear how it is going - reply here or find me at @maya in Slack.

Talk soon,
Maya

Maya Chen
Engineering Manager, Platform

You are getting Platform Notes because you opted in after an eng all-hands. Manage your subscription or unsubscribe any time by replying to this email.
