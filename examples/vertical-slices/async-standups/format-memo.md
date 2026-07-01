---
entry_id: memo
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

TO: Platform Engineering Team
FROM: Maya Chen, Engineering Manager, Platform
DATE: Monday, June 23
RE: Adoption of async-first standups as standing practice

This memo confirms that async-first standups are now standing practice for the Platform team. The 30-day trial that began May 19 is concluded, and the synchronous 9am Pacific standup will not return to the calendar.

The trial was a response to three problems recorded in ADR-0014. The 9am Pacific slot fell at 9:30pm for our India-based engineers, who attended at 3.2 of 5 sessions against 4.6 for US-based engineers. The meeting produced roughly four minutes of content that changed anyone's behavior out of a fourteen-minute average. And verbal status left no record, which cost the team real time on three occasions last quarter when someone reworked a problem that had already been solved and discussed out loud. The trial replaced the meeting with a written update in #team-standup - posted by 10am local time, three fields, blockers routed by direct @mention.

The results held. On-time posting climbed from 78 percent in Week 1 to 85.5 percent by Week 2 and stayed near that level for the rest of the trial. Median time from @mention to substantive reply was 18 minutes, well inside the old pattern of blockers waiting until the afternoon for a response. India-based engineers posted every weekday for the first time in this team's history. Two problems flagged mid-trial - posts running long, and on-call triage taking longer than the 10-minute target - were resolved with the three-bullet ceiling introduced at the Thursday working session; splitting the on-call rotation was considered and was not needed. Priya Raman reviewed the trial data ahead of the Day 30 review on June 19, and no objection was raised to making the format permanent.

This memo establishes the async standup format documented in docs/playbook.md as the Platform team's default practice, effective immediately. The Thursday working session continues on its existing schedule. Team members joining after May 19 are expected to read docs/playbook.md as part of onboarding. No further trial review is scheduled; the format will be revisited only if a future retrospective surfaces a specific problem it cannot handle.
