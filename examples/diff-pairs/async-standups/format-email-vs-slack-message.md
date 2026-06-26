---
diff_pair_id: format-email-vs-slack-message-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: format
entry_a: email
entry_b: slack-message
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Format swap - `email` vs `slack-message`

**Topic:** Should we adopt async-first standups?
**Axis varied:** format
**A:** `email` - A business message designed for the inbox scan - subject line doubles as summary, body leads with action, and the reader never needs to re-read to know what is being asked.
**B:** `slack-message` - A short, async-first message designed for team channels - direct, scannable, and respectful of the reader's attention in a high-volume feed.

## What to notice

Both examples address the same topic and (by default) share every axis other than format. 
The only deliberate variable is which format the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The format 
swap is the entire cause of those differences.

---

## A: `email`

**From:** Maya Chen <maya.chen@company.com>
**To:** eng-platform@company.com
**Cc:** Priya Raman <priya.raman@company.com>
**Subject:** Starting Monday: 30-day async standup trial - post by 10am local, no more 9am Pacific call

Team,

Starting Monday May 19, we are running a 30-day trial of an async-first standup. The 9am Pacific sync call is paused for the trial. Here is what you need to do and why.

**What changes**

- Post a daily update in #team-standup by 10am your local time. Three fields, pinned template at the top of the channel:
  - Shipped (last 24h)
  - In progress
  - Blocked / at risk - @mention the person who can unblock
- The Thursday 9am Pacific slot becomes a 60-minute working session, not a status meeting. Agenda posted Wednesday EOD.
- On-call engineer reads #team-standup by 9am Pacific each day and responds to blockers within 30 minutes during business hours.

**Why now**

Q1 attendance was 4.6/5 for US, 3.2/5 for India - because 9am Pacific is 9:30pm IST. We average 14 minutes per standup with about 4 minutes that actually changes someone's behavior. And the verbal status doesn't persist - we hit three duplicate-work incidents last quarter that a searchable channel would have caught.

**What I need from you**

1. Post your first async update Monday May 19 by 10am local.
2. If the template doesn't fit your work that day, post anyway and say so. Consistency matters more than format for the trial.
3. Bring friction to the Thursday session or DM me directly. We will review at day 15 and day 30.

If you have concerns before Monday, reply to this thread or grab time on my calendar.

Thanks,
Maya

- - -
Maya Chen
Engineering Manager, Platform
maya.chen@company.com | Slack: @maya

---

## B: `slack-message`

**Proposal: try async standups for 30 days starting May 19**

Our 9am standup is hard on the India team and the info disappears after each call. Want to run an experiment:

- Each person posts to #team-standup by 10am local time (3 fields: shipped / in progress / blocked)
- Blocked items @mention the person who can unblock
- On-call reads the channel by 9am PT and responds to blocks within 30 min
- We keep Thursday 3pm as a real working session for anything that needs live discussion

@priya @arjun @deepa - this gets you out of 9:30pm standups. Want to hear your reaction first.

:thread: Drop thoughts in thread by Friday and I will send a final plan Monday.
