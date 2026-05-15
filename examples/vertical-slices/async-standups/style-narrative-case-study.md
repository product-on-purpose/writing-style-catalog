---
entry_id: narrative-case-study
axis: style
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# The standup that ran at 9:30pm

The Platform team at Meridian had a daily standup at 9am Pacific. For eight of the eleven engineers, that was a normal morning meeting. For Priya, Arjun, and Devika in Bengaluru, it was 9:30pm on a Tuesday.

For most of 2025, this was treated as a fact of geography. Priya joined when she could. She missed about two standups a week, usually because her daughter had homework or her in-laws were visiting. Nobody held it against her. The Q1 attendance report eventually showed what everyone already knew: India averaged 3.2 of 5 standups; the US side averaged 4.6.

The turning point came in early March. On a Monday morning, Marcus in Austin pushed a fix for a 401 error on the auth service. He mentioned it in standup. Priya was not on the call.

On Tuesday at 2pm Pacific, Devika hit the same 401. She did not know Marcus had fixed it. She spent the next two hours retracing the diagnosis - reading logs, opening tickets, eventually pinging Marcus on Slack. Marcus replied: "Yeah, I shipped that fix yesterday. Sorry, I should have written it up."

Devika did not say anything in standup the next day. But she sent her manager, Lina, a short message: "If we're going to make me wake up to standups I cannot attend, I would like the standup to also write things down."

Lina read that message twice. Then she opened the Q1 attendance numbers and looked at them with new eyes. She also opened the Zoom recording of Monday's standup. It was 14 minutes long. The auth fix was mentioned at the 11-minute mark, between two unrelated updates. Even if Devika had watched the recording, she would have had to watch eleven minutes of unrelated work first.

Lina proposed a 30-day trial. Replace the sync standup with an async post in `#team-standup`. Three fields - Shipped, In progress, Blocked or at risk - posted by 10am local time. Blockers @mention the person who can unblock. The 9am Pacific slot becomes a 60-minute Thursday working session.

She framed it as reversible. She named the success criteria up front: blocker resolution time, posting consistency, and a team survey at day 30.

The first week was awkward. Two engineers forgot to post. Marcus over-shared and had to be gently told that "Shipped: nothing yet" was acceptable. By week two the rhythm was established.

By day 30, the survey came back with a sentence from Devika that Lina pinned in her notes file: "I no longer feel like I'm chasing the team. The team is on a page I can read." Blocker resolution time during overlap windows had dropped from a median of just over 4 hours to 90 minutes. Nine of eleven engineers were posting at least four times a week.

The team kept the change. The Thursday working session became where the real arguments happened, which is what those meetings were always supposed to be.

Lina's takeaway, written in her own retro notes: the schedule had been treated as fixed and the people as adaptable. The trial reversed the assumption. Once that flipped, the change was small.
