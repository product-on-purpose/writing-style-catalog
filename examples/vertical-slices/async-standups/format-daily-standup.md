---
entry_id: daily-standup
axis: format
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

**#team-standup - Devon Park - Tue May 27, 9:42am PT (day 9 of trial)**

**Shipped**
- Rate-limiter rollout to staging; 0 errors over 18h soak
- PR #4412 merged (auth token rotation runbook)

**In progress**
- Production rollout of rate-limiter, gated behind `rl_v2` flag, 5% traffic by EOD
- Pairing with Aditi 10am PT on the IST-hour metrics dashboard

**Blocked / at risk**
- Waiting on @sara for sign-off on the rotation runbook before I close the parent ticket (not urgent, EOW is fine)
- (meta) Async format participation was 9/11 yesterday - @oliver and @emma did not post. Oliver was on-call handoff, fine. Emma I will DM. Flagging so @maya has visibility before the day-15 pulse.
