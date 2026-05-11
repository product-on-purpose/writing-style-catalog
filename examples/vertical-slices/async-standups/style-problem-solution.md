---
entry_id: problem-solution
axis: style
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## The Problem

The team's daily standup runs at 9am Pacific. Three of the team's eleven engineers are based in India (UTC+5:30), which puts the meeting at 9:30pm their local time. On any given week, at least one of those engineers misses the call because of a conflict with evening life. When they miss it, they do not get the context shared in the meeting - including blockers that affect their work.

The problem is not just timezone fairness. The meeting's information does not persist. When @priya mentions in the standup that the auth service is throwing a 401 on a specific endpoint, that information lives in a 14-minute Zoom recording that nobody will watch. The engineer who hits that same 401 at 2pm does not know Priya already diagnosed it. They spend 45 minutes retracing the same path.

The synchronous standup was designed for co-located teams. It assumes everyone can occupy the same time slot without cost, and that verbal delivery is sufficient for information sharing. Neither assumption holds for this team.

## The Solution

Replace the synchronous standup with a structured async update in #team-standup. Each engineer posts by 10am their local time, answering three questions: what shipped in the last 24 hours, what is in progress today, and what is blocked or at risk. Any blocked item must @mention the specific person who can unblock it.

The channel becomes the single searchable record of daily status. When an engineer hits a 401 at 2pm, they search the channel and find that Priya posted the fix at 8am India time.

Blocked items are resolved faster because the @mention reaches the right person directly, rather than relying on that person happening to attend the meeting and remember.

The synchronous meeting is replaced by a 60-minute working session on Thursdays, reserved for discussion that genuinely requires real-time exchange.

After 30 days: review blocker resolution time, channel engagement rate, and a team survey. Extend or revert based on data.
