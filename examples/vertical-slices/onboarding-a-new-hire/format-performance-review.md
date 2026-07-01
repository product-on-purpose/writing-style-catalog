---
entry_id: performance-review
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Performance Review: Priya - Two-Week Onboarding Checkpoint

## Period
Jun 22 to Jul 3 (Priya's first two weeks on the team)

## Reviewer
Mei - Onboarding DRI, Backend Services

## Summary
Priya's first two weeks met every goal set in ADR-0023 (the guided pairing protocol): she has full access, she navigates the codebase independently, and she shipped her first change on schedule with the team's confidence, not just its permission. The one area to keep developing is breadth of system knowledge ahead of her on-call rotation start in week five.

## Performance Against Goals

### Access and tooling (days 1-2)
Rating: Met
Full access and a working local environment were in place by Monday afternoon of Day 1. Priya followed the setup doc step-by-step and hit the one gap in it herself - a missing VPN cert step - which let me patch the doc that same day instead of it sitting unnoticed for the next hire.

### Codebase orientation (week one)
Rating: Met
By Day 3, Priya was navigating the three services she owns without hand-holding, including finding the test harness and the team's naming conventions on her own. She completed both guided walkthroughs (service topology; deployment and on-call tooling) and traced a live production request end to end through the system.

### Paired first change (week two)
Rating: Met
Priya co-drove the Thursday design session and caught an edge case the team had missed before any code was written. She opened the PR on schedule and drove the deploy herself; the change merged Jul 3 before end of day, with Arjun pairing as support rather than driving.

### On-call and incident-response orientation (week one and week two)
Rating: Met
Priya observed one live incident response and attended the handoff call; she understands the escalation path. She completed on-call briefing part two (alert routing and escalation) on Jun 29 as scheduled. The hands-on alert drill itself is deferred to Jul 9, pending her own staging credentials - an infrastructure dependency, not a gap in her preparation.

## Strengths
- Follows process precisely enough to catch what it misses: found the setup doc's missing VPN cert step because she worked the doc step-by-step and hit the error, then flagged it immediately instead of quietly self-debugging around it.
- Brings technical judgment to a task before the task is formally hers: caught the edge case in the design session as a co-driver, before a line of the change was written.
- Builds relationships without being asked to: three teammates opened async threads with her outside the formal onboarding plan, and she contributed substantively to the Friday architecture discussion in week one.

## Development Areas
- Her system knowledge is currently deep in the three services she owns changes in, and comparatively thin elsewhere. Both orientation walkthroughs were exposure, not hands-on practice. This matters specifically because on-call rotation eligibility starts in week five, and the rotation will occasionally put her in front of services she has not worked in directly.

## Goals for Next Period
- Get hands-on exposure, not just walkthrough exposure, to at least one service outside the three she currently owns changes in - by Fri Jul 17.
- Complete the hands-on on-call alert drill once her own staging credentials land - by Jul 9, contingent on the infra ticket resolving.
- Keep the working relationship with Arjun going past the formal two-week window - ongoing. ADR-0023 expects this to become an informal mentorship channel, and that is by design, not drift.

## Overall Rating
Exceeds Expectations. This is a two-week onboarding checkpoint, not the annual review cycle, and it carries no compensation weight - but it is the formal written record ahead of Priya's on-call rotation start in week five.

## Additional Notes
Priya remains excluded from the on-call rotation for her first 30 days under team policy; nothing above changes that. Her own staging credentials are still an open infrastructure ticket as of this review. I am continuing to escalate it, through the engineering manager if needed, same as flagged in the week-one status report - the delay is a process gap, not a reflection of Priya's performance.
