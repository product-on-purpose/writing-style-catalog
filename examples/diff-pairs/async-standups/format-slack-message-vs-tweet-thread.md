---
diff_pair_id: format-slack-message-vs-tweet-thread-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: format
entry_a: slack-message
entry_b: tweet-thread
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Format swap - `slack-message` vs `tweet-thread`

**Topic:** Should we adopt async-first standups?
**Axis varied:** format
**A:** `slack-message` - A short, async-first message designed for team channels - direct, scannable, and respectful of the reader's attention in a high-volume feed.
**B:** `tweet-thread` - A sequence of numbered short posts (1/, 2/, 3/...) each under 280 characters, telling one connected story or making one connected argument across the chain.

## What to notice

Both examples address the same topic and (by default) share every axis other than format. 
The only deliberate variable is which format the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The format 
swap is the entire cause of those differences.

---

## A: `slack-message`

**Proposal: try async standups for 30 days starting May 19**

Our 9am standup is hard on the India team and the info disappears after each call. Want to run an experiment:

- Each person posts to #team-standup by 10am local time (3 fields: shipped / in progress / blocked)
- Blocked items @mention the person who can unblock
- On-call reads the channel by 9am PT and responds to blocks within 30 min
- We keep Thursday 3pm as a real working session for anything that needs live discussion

@priya @arjun @deepa - this gets you out of 9:30pm standups. Want to hear your reaction first.

:thread: Drop thoughts in thread by Friday and I will send a final plan Monday.

---

## B: `tweet-thread`

1/ We killed our daily standup six months ago. 11 engineers, 4 timezones. Here is what happened, and what I would tell another EM thinking about it.

2/ The math that broke us: 9am Pacific standup = 9:30pm IST. Our India team attended 3.2 out of 5 days. Our US team showed up 4.6. We were running two different teams pretending to be one.

3/ The 14-minute meeting produced about 4 minutes of signal. The rest was round-robin throat-clearing. And none of it persisted. By Wednesday, nobody remembered what Monday's standup covered.

4/ The replacement: post in #team-standup before 10am local. Three fields. Shipped. In progress. Blocked or at risk. If you are blocked, @mention the person who can unblock. That is the entire ritual.

5/ The sync time did not disappear. We banked it into one 60-minute Thursday working session. Real decisions, real design conversations. If there is no agenda by Wednesday, we cancel.

6/ Week 2 numbers: 47/55 posts on time. Median blocker resolution: 18 minutes. India engineers contributed every weekday for the first time ever. Five person-hours per week recovered, net of the Thursday slot.

7/ The thing nobody warns you about: writing is harder than talking. Engineers who breezed through sync standups struggled with the post. That is a feature, not a bug. The async post forces clarity.

8/ What I got wrong: I underestimated the on-call triage load. Reading 11 posts and routing blockers takes 25 minutes some mornings. We are watching whether to rotate this faster.

9/ If you try this: do not half-async it. A daily call plus an async post is just more work. Pick one. We picked async, with a single weekly synchronous slot held for the things async cannot do.

10/ The hardest part is not the process. It is convincing senior leadership that an engineering team without a daily standup is still a team. Show them the blocker resolution times. The data does the arguing.
