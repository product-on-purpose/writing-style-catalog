---
entry_id: listicle
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# 8 Things We Learned From Two Weeks of Async Standups

We are two weeks into a 30-day trial: no more daily sync standup, just a message posted to a channel before 10am local time. Here is what actually changed, in the order it surprised us.

1. **The timezone math was the real trigger.** Our 9am Pacific standup landed at 9:30pm India Standard Time, and Q1 attendance data made the cost visible: engineers in India averaged 3.2 standups out of 5 per week, against 4.6 for engineers in the US. That gap was never about engagement - it was about asking a third of the team to log in at night, every night.

2. **Most of the old meeting was filler.** The sync standup ran 14 minutes on average, but a review of the past month found only about 4.2 minutes of content that actually changed what someone did next - a blocker raised, a dependency flagged, real context shared. The other 10 minutes was status nobody needed to hear live.

3. **Nothing we said out loud stayed said.** We found three separate incidents last quarter where an engineer burned an hour or more re-solving a problem that had already come up, and been resolved, in an earlier standup. Verbal status has no search function.

4. **Three fields beat an open text box.** The new template is Shipped, In progress, and Blocked or at risk, nothing more. "Nothing today" is an acceptable answer in any field, and skipping one is fine on Fridays - the constraint turned out to be the feature, not a limitation.

5. **A blocker needed a name, not an audience.** Anything at risk gets an @mention of the one person who can unstick it, and the on-call engineer is responsible for making sure that mention gets a response, not for summarizing the channel. Routing beats broadcasting.

6. **We relocated the meeting instead of deleting it.** The old standup slot became a 60-minute Thursday working session for the handful of things that genuinely need real-time back-and-forth. If nothing needs discussing, it gets cancelled by Wednesday at 5pm Pacific instead of held out of habit.

7. **The numbers already beat the meeting they replaced.** On-time posts hit 85.5 percent this week, up from 78 percent in week one, and every India-based engineer posted on every single weekday for the first time in this team's history. Blockers are getting a substantive reply in a median of 18 minutes.

8. **Two seams were already showing.** Some posts are creeping past 200 words, well past the 60-second skim the format is supposed to allow, and the on-call engineer is spending closer to 25 minutes a morning on triage against a 10-minute target. Neither is a surprise for week two, but both are on the list for Thursday's session before they harden into habits.

We have two weeks left before the Day 30 retro decides whether this becomes permanent. If a chunk of your team is logging into a call at night just to say "no update," the math above is why we stopped asking ours to.
