---
entry_id: incident-report
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Incident Report: Staging Environment Provisioning Delay - Engineer Onboarding

## Status

Monitoring - Jun 26, end of day

## Summary

Priya's individual staging environment access, required for the on-call orientation drill scheduled Jul 2, was requested Jun 23 and has not been provisioned. The delay is currently covered by a shared team credential but will block a Week 2 onboarding milestone if not resolved before Jun 29.

## Impact

- Services affected: Staging environment provisioning; on-call onboarding program
- Team members affected: Priya (incoming engineer, end of Week 1) and the Week 2 onboarding program
- Delay period: Jun 23 (request submitted) through Jun 26 (current); hard resolution deadline Jun 29

## Timeline

- Tue Jun 23 - Staging access request submitted through the IT provisioning portal on day two of onboarding
- Wed Jun 24 to Fri Jun 26 - Request remained in queue with no provisioning action
- Fri Jun 26 - Onboarding DRI confirmed Priya is unblocked for all Week 1 activities under a shared team credential; Jul 2 on-call drill identified as the first milestone requiring her individual access

## Root Cause

The provisioning request entered the standard IT queue without a flag indicating time sensitivity. Onboarding access requests currently have no mechanism to signal that they are tied to a program deadline, so the request sat alongside routine items rather than being routed or prioritized for same-week completion. The gap is in how onboarding requests are submitted and tagged, not in the provisioning system itself.

## Resolution

Not yet complete. Priya's Week 1 activities are covered by the shared credential workaround. Full resolution requires her individual staging access to be provisioned before Jun 29.

## Next Steps

- IT provisioning: confirm or complete Priya's staging environment access by end of day Mon Jun 29
- If not confirmed by Jun 29, onboarding DRI escalates to the engineering manager to expedite the open ticket
- On-call orientation drill (scheduled Jul 2) proceeds only if individual access is confirmed live; if not resolved in time, the drill moves to the week of Jul 7
- Onboarding setup documentation: add a note that staging access provisioning can take three to five business days and must be requested on day one, not day two, to avoid blocking Week 2 milestones
