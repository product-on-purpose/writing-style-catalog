---
entry_id: faq
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## Frequently Asked Questions - Async Standup

### Is the 9am Pacific standup still happening?

No. The synchronous daily standup is replaced with an async update posted to `#team-standup`. There is no call to join. The old calendar invite has been removed.

### When do I need to post my update?

By 10am your local time, every weekday. That is 10am Pacific, 10am Eastern, 10am UK, or 10am IST depending on where you are. Posting at the start of your morning helps the on-call engineer triage the channel before their midday.

### What do I put in the post?

Use the three-field template pinned in `#team-standup`:

- **Shipped:** what completed in the last 24 hours
- **In progress:** your current focus
- **Blocked or at risk:** anything that needs attention, with an @mention of the person who can resolve it

Keep the whole post to under 60 seconds of reading time. If a field is empty, write "nothing today."

### What if I'm blocked and need help right now?

Add your blocker to the "Blocked or at risk" field and @mention the person who can resolve it directly in your standup post. The on-call engineer scans `#team-standup` once between 10am and 11am Pacific and makes sure every @mention has a response before end of the workday. If the situation is urgent, DM or post in `#team-dev` directly - the async standup does not replace direct communication for critical blocks.

### Why are we switching to this format?

The 9am Pacific standup was 9:30pm for engineers based in India, and Q1 attendance data showed the gap: India-based engineers averaged 3.2 appearances per week versus 4.6 for US-based engineers. Beyond the timezone problem, the 14-minute meeting was producing roughly 4 minutes of information that changed anyone's behavior, and none of it persisted after the call. Three times last quarter an engineer spent an hour on a problem already solved in a previous standup because there was no searchable record. The async format lets everyone participate at a time that fits their day and creates a record that survives the call.

### What happened to the 9am slot on my calendar?

The time that was five standup sessions per week is now one Thursday working session, 60 minutes, at 8am Pacific (8:30pm IST). Agenda lives in `docs/thursday-agenda.md`. The session is reserved for topics that genuinely require real-time conversation. If the agenda is empty by Wednesday at 5pm Pacific, we cancel.

### Who makes sure blocked items don't fall through?

The on-call engineer is responsible for scanning `#team-standup` once between 10am and 11am Pacific each weekday. Their job is to confirm every @mention has a response before end of day - not to summarize the channel for everyone else. This on-call reading responsibility replaces the meeting facilitation duty that was on the same rotation.

### What if I forget to post one day?

Post when you remember. A late post is better than no post. If you miss a day entirely, there is no correction needed - just resume the next morning. Chronic gaps hurt the channel's value for everyone, but a single missed day is not an incident.

### Is this permanent or are we still deciding?

This is a 30-day trial. The retro document is `docs/trial-retro.md`. If you have feedback mid-trial, add it there rather than in DMs or side conversations. The decision to keep, adjust, or revert will be made at the Day 30 retro with input from the full team.
