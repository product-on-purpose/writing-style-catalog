---
entry_id: matter-of-fact
axis: tone
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

**Proposal: Transition to Async-First Standup Format**

The team currently holds a daily synchronous standup at 9am Pacific. Attendance has averaged 8 of 11 engineers over the past quarter. The three engineers who miss most frequently are in the UTC+5 timezone, where 9am Pacific is 9:30pm local. The meeting runs an average of 14 minutes.

The proposal is to replace the synchronous standup with a structured async update posted to #team-standup by 10am each engineer's local time. The format uses three fields: what shipped in the last 24 hours, what is in progress today, and what is blocked or at risk. Blocked items must include a @mention of the person who can resolve the block.

The on-call engineer reads the channel by 9am Pacific each day and responds to blocked items within 30 minutes during business hours.

The synchronous meeting would be replaced with a weekly 60-minute working session on Thursdays. That session is not a status meeting - it is reserved for topics that require real-time discussion.

**Expected outcomes:**

- All engineers participate on a schedule that fits their timezone
- Blockers reach the relevant person with a direct mention rather than relying on meeting attendance
- Status information is persistent and searchable rather than spoken and lost

**Risks:**

- Engineers who do not read the channel regularly will miss updates
- The format requires consistent participation to be useful - if three people stop posting, the value drops for everyone

**Next step:** Trial period of 30 days starting the week of May 19. Review at 30 days with a team survey and a look at blocker resolution time before and after.
