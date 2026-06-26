---
entry_id: status-report
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Status Report - Priya Onboarding Workstream
**Period:** Mon Jun 22 - Fri Jun 26
**Author:** Mei (onboarding DRI)
**Status:** Green

## Headline
Priya is on track for a Week 2 ship. All access is live, she has a working read of the codebase, and the first change is designed and ready to code. Belonging indicators are also positive after week one.

## Done this period
- Priya has full access and a working local environment as of Monday afternoon. The setup doc was followed end-to-end; one gap (missing VPN cert step) was patched into the doc same day.
- Priya can navigate the three services she will touch without hand-holding. She located the relevant test harness and the team's naming conventions on her own by Day 3.
- The scoped Week 2 change is fully designed and ready to implement. Priya co-drove the Thursday design session without prompting and caught one edge case the team had missed.
- Priya has observed one live incident response and attended the handoff call. She knows the escalation path and understands the on-call rotation cadence.
- Priya attended the Friday team sync and contributed two points to the architecture discussion. Three teammates have async threads going with her on topics outside the formal onboarding plan.

## Up next
- Priya opens her first pull request (the scoped change) by Wed Jul 1.
- Code review and merge complete by Fri Jul 3, with Arjun pairing as support if needed.
- On-call briefing part two (alert routing and escalation drill) on Mon Jun 29.
- Two-week retrospective with Priya on Fri Jul 3 to close the formal onboarding window and surface any remaining gaps.

## Blocked / risks
- **Staging access pending.** The provisioning request went in Jun 23 and is sitting in the infra queue. Priya is unblocked for now (team shared credential covers her), but she needs her own access before the on-call alert drill scheduled for Jul 2. If not resolved by Mon Jun 29, the drill shifts by at least one week.
- **Risk (low): change velocity.** The team shipped four times this week. Priya kept pace, but Week 2 brings her first solo review alongside her own pull request. A mid-week check-in on Wed Jul 1 is scheduled to catch any load signals early.
- **Risk (watch): belonging vs. function.** One week of positive signals is not enough to conclude she feels she belongs. The Jul 3 retro should ask that question explicitly and not assume the functional progress answers it.

## Asks
- **Infra (by Mon Jun 29):** please confirm or escalate the staging environment ticket submitted Jun 23. If it is stuck, flag me and I will escalate through the engineering manager.
