---
diff_pair_id: tone-candid-vs-matter-of-fact-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: tone
entry_a: candid
entry_b: matter-of-fact
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Tone swap - `candid` vs `matter-of-fact`

**Topic:** Should we adopt async-first standups?
**Axis varied:** tone
**A:** `candid` - Names the uncomfortable truth directly - not harsh, but unwilling to pretend the hard thing is not there.
**B:** `matter-of-fact` - States what is true without editorial coloring - neither cold nor warm, just accurate.

## What to notice

Both examples address the same topic and (by default) share every axis other than tone. 
The only deliberate variable is which tone the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The tone 
swap is the entire cause of those differences.

---

## A: `candid`

Team,

I want to be direct about something: our daily standup is not delivering what it is supposed to deliver, and we need to change it.

Here is the honest picture. We have three engineers who join at 9:30pm their local time on most days - and when they cannot make it, they miss information that affects their work. We have engineers who post "same as yesterday" most Tuesdays because nothing has actually changed since Monday's standup. We have blockers that get mentioned in the meeting and then disappear because nobody wrote them down. The standup takes 14 minutes on average and the signal-to-noise ratio is not good.

I know this is not news to some of you. I have been aware of it for a while and I should have said something sooner.

Here is what I think we should do: replace the synchronous standup with an async format for 30 days. Three questions, answered in Slack by 10am local time: what shipped, what is in progress today, what is blocked or at risk. Blocked items require a @mention. I read the channel each morning and make sure blocks get resolved the same day.

This does not fix everything. If people do not post consistently, the format breaks. If I do not read the channel attentively, blocked items will pile up. I am asking for your participation and holding myself accountable to the same standard.

The synchronous meeting I want to preserve is Thursday working sessions - real collaboration, not status.

I would rather try this and learn than continue a format that is not working. We will review at 30 days and make a permanent call together.

Any questions, come find me.

---

## B: `matter-of-fact`

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
