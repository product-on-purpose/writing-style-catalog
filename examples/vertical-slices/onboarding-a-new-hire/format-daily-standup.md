---
entry_id: daily-standup
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

*(Async standups posted by the onboarding lead in the team's daily channel. Priya started Monday. Four updates across two weeks.)*

---

**Mon, Week 1**

**Done**
- Priya local setup complete - repo access, dev environment confirmed
- Service topology orientation done - she knows the four core services and integration points

**Next**
- Assign first read-only task: trace a recent deploy through the pipeline, one question per step
- Walk her through the on-call rotation doc before EOD

**Blockers**
- VPN cert not provisioned - Priya cannot reach staging from home; need IT to issue by tomorrow EOD

---

**Wed, Week 1**

**Done**
- VPN cert issued by IT Tuesday afternoon - Priya hit staging on her own this morning
- Priya shadowed on-call handoff; found a runbook gap (alert threshold reference is missing)
- First real ticket assigned: add structured log field to the notification service

**Next**
- Pair on her first PR today - she drives
- File the runbook gap as a ticket

**Blockers**
- None

---

**Mon, Week 2**

**Done**
- Priya's first PR open since Friday - tests passing, one review comment resolved
- Ownership map review done - she knows the four domain leads and what each owns

**Next**
- Second review on Priya's PR needed today from Keiko or Marcus (deploy window closes Wednesday)
- After merge, she picks her own second ticket from the backlog

**Blockers**
- PR review from Keiko or Marcus needed by EOD today to hit the Wednesday deploy window

---

**Thu, Week 2**

**Done**
- Priya's change merged Tuesday; she ran the deploy solo
- Two-week retro done - two doc gaps filed as tickets, one tooling friction item logged
- Priya joined this morning's on-call handoff as secondary; knows her rotation schedule through month end

**Next**
- Close onboarding checklist and hand to team lead for sign-off
- Priya moves to self-directed tickets next sprint

**Blockers**
- None
