---
entry_id: postmortem
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Postmortem: Staging Environment Provisioning Delay - Priya Onboarding

## Severity

SEV-4

## Summary

A staging environment provisioning request submitted on Jun 23 remained unresolved through Jul 2, shifting Priya's on-call readiness drill by one week to Jul 9. The delay stemmed from the infra queue's lack of an SLA for new-hire provisioning and the onboarding checklist's failure to distinguish "submitted" from "confirmed." No production systems were affected; the impact was confined to Priya's onboarding timeline and the scheduled on-call drill.

## Timeline

- Tue Jun 23 - Staging environment access provisioning ticket submitted (Priya's Day 2)
- Fri Jun 26 - Week one status report flags staging access as pending risk; team shared credential covering Priya in the interim
- Mon Jun 29 - Access still unprovisioned; Mei queries ticket status; no response on record from infra queue
- Tue Jun 30 - Mei escalates via engineering manager; infra team acknowledges and estimates 2-3 business days for resolution
- Thu Jul 2 - On-call alert drill cannot proceed; Priya lacks her own staging credentials; drill rescheduled to Thu Jul 9
- Fri Jul 3 - Staging access provisioned; Priya's account confirmed working in staging environment
- Thu Jul 9 - On-call alert drill completed; Priya used her own credentials for the full exercise

## Root Cause

The infra team's provisioning queue has no published SLA for new-hire access requests, and the onboarding protocol has no built-in escalation trigger when access is not confirmed within a set window. The request sat in the queue for six business days before anyone escalated. The systemic condition is the absence of a feedback loop between onboarding milestones and infra provisioning status: neither the onboarding DRI nor the infra team had a mechanism to surface a stuck ticket before it blocked a scheduled deliverable.

## Impact

- Engineers affected: 1 (Priya)
- Duration: Jun 23 (request submitted) to Jul 3 (access confirmed) - 8 business days
- Scheduled events slipped: on-call readiness drill shifted 7 days, from Jul 2 to Jul 9
- Production impact: None

## Contributing Factors

- No SLA defined for new-hire provisioning in the infra queue
- Onboarding access checklist tracks items as "submitted" with no column for "confirmed"; no follow-up loop built in
- The Jun 26 status report flagged the risk but named no escalation trigger; escalation happened on Jun 30, four days after the flag and one day after the Mon Jun 29 stated deadline passed
- Shared team credential masked the daily impact of the gap through week one, making it easy to defer action until the drill date made the absence concrete

## Action Items

- [ ] Update the access checklist to require a "confirmed by: [name], [date]" entry for each item, not just "submitted" - Owner: Mei - Due: Jul 17
- [ ] Add a Day 5 (end of week one) checkpoint to the onboarding DRI calendar: verify all access items confirmed, not just submitted; if any are still pending, escalate to infra that day - Owner: Mei - Due: Jul 17
- [ ] Define and publish a 48-hour SLA for standard new-hire provisioning requests in the infra team runbook - Owner: Infra team lead - Due: Jul 31
- [ ] Add Arjun to the onboarding access verification step so a second person holds the escalation path if Mei is unavailable - Owner: Mei - Due: Jul 17

## Lessons Learned

Submitting a ticket is not the same as owning the outcome. The onboarding checklist treated access as done once requested; this incident showed it should be treated as done only when the person who needed it has confirmed it themselves. The shared team credential kept Priya functional but removed urgency from the unresolved gap. The escalation that eventually unblocked her happened four days after the status report identified the risk and one day after the stated deadline passed - there was no automatic trigger, only the looming drill date. Building a Day 5 confirmation checkpoint into the DRI calendar converts the current "wait and see" pattern into "surface and resolve before it blocks a milestone."
