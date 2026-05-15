---
entry_id: direct-communicator
axis: voice
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

I think we should try the async format for 30 days.

Here is why. The 9am Pacific standup is 9:30pm for the three engineers in India. Their Q1 attendance was 3.2 out of 5. The US-based engineers averaged 4.6. That is not a coincidence and it is not their fault. We built a meeting that punishes a third of the team for living where they live.

The meeting also does not earn its time. Fourteen minutes per day, eleven people, and roughly four minutes of that drives any action. The rest is status that could be read. We also lose what gets said. Priya diagnosed a 401 in standup last month. Five hours later, someone else hit the same error and spent 45 minutes re-diagnosing it because the original answer lived in a Zoom call no one could search. A Slack post would have fixed that.

The proposal is simple. Each engineer posts in #team-standup by 10am local time. Three fields: shipped, in progress, blocked or at risk. Blockers @mention the person who can unblock. The old 9am slot becomes a 60-minute Thursday working session - not a status meeting, an actual working session with an agenda.

I want to be straight about the tradeoff. We lose the daily check-in. For some teams that matters, and I do not want to pretend otherwise. The Thursday session is meant to carry the connection load that the daily call was carrying, but it is one session, not five. If after 30 days the team feels disconnected or things are slipping, we go back. The revert is a one-line message in Slack. Nothing about this is permanent.

What I am asking: run it for 30 days starting Monday. At day 30 we look at three things - India attendance and participation, blocker response time, and how people say it is going. Then we decide.

If you have concerns or this is a bad idea for a reason I am missing, tell me before Friday. After that I am going to set it up.
