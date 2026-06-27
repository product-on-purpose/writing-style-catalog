---
entry_id: proposal
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Structured Two-Week Onboarding Protocol for Backend Services Engineers
## Prepared for: Ravi Mehta, Engineering Manager
## Prepared by: Mei, Backend Services Team Lead
## Date: June 16, 2026

## Executive Summary

The backend services team is bringing Priya on board on June 22. Our informal onboarding approach leaves new engineers solving access and tooling problems on their own during their first week, delays the first shipped change to week three or four, and leaves belonging to chance. We are proposing a structured two-week protocol that pairs Priya with a named buddy (Arjun), runs three bounded phases from access through a shipped pull request, and closes with a retrospective on July 3. We are asking for your approval to allocate Arjun at roughly 35% capacity in week one and 20% in week two.

## The Problem

Two failure modes have repeated every time we have onboarded without structure.

First, the new hire spends week one in a silent gap. Access, tooling, and environment setup block progress, but asking for help feels like interrupting a busy team. The new hire waits; the team does not know there is a wait.

Second, the first shipped change lands in week three or four. By then, whether the new engineer feels they belong has already been decided - largely by the silence of the preceding weeks. Shipping earlier does not just accelerate contribution; it changes how the team perceives the new hire and how the new hire perceives herself.

A third constraint: we deploy daily and run a shared on-call rotation. We cannot pause delivery for onboarding, and we cannot ask a buddy to absorb a new hire full-time without a real cost to their own sprint. Any protocol that does not account for that cost will be abandoned under pressure before it finishes.

## Proposed Approach

We will run a structured two-week guided pairing protocol with Arjun as Priya's named buddy, explicit daily check-ins, and a pre-scoped first change ready on day one. The protocol covers three phases:

**Phase 1 - Access and tooling (days 1-2).** Arjun owns a printed checklist. No item is considered complete until Priya has verified it herself. This removes the silent-gap problem by giving blockers a named owner.

**Phase 2 - Codebase orientation (week one).** Two 90-minute guided walkthroughs: one on the service topology, one on deployment and on-call tooling. Notes belong to Priya; Arjun does not maintain them. Priya traces one real production request through the observability platform before the Friday check-in.

**Phase 3 - Paired first change (week two).** The team scopes the task before June 22. Scope constraint: one service, no on-call risk if the change goes wrong. Priya drives the implementation and the deploy; Arjun reviews the pull request and pairs on blockers.

This approach fits our team because the buddy cost is front-loaded and bounded, the first change is de-risked by pre-scoping, and targeting a merged pull request by July 3 gives the protocol a clean close.

## Scope and Deliverables

**Included:**

- Access and tooling checklist completed and verified by end of day June 23
- Two 90-minute codebase walkthroughs in week one
- One pre-scoped first change designed before June 22, opened as a pull request by July 1, merged by July 3
- Week one check-in on Friday June 26 (access confirmed, codebase navigable without hand-holding)
- Two-week retrospective with Priya on July 3 to close the formal onboarding window and surface remaining gaps

**Not included:**

- On-call rotation eligibility (Priya is excluded from on-call for her first 30 days; this protocol operates within that rule, not around it)
- Extended mentorship beyond two weeks (the buddy relationship may continue informally, but the formal protocol closes on July 3)
- Staging environment provisioning (a separate infra request will cover that access; this protocol assumes staging is live for Priya by June 29)

## Timeline

| Milestone | Target Date |
|---|---|
| Approval confirmed, Arjun notified, first change pre-scoped | Fri Jun 19 |
| Priya's first day, checklist starts | Mon Jun 22 |
| Access and tooling verified live | Tue Jun 23 |
| Service topology walkthrough | Jun 23-24 |
| Deployment and on-call tooling walkthrough | Jun 24-25 |
| Week one check-in (Priya navigates codebase unassisted, no open blockers) | Fri Jun 26 |
| First change implementation begins | Mon Jun 29 |
| Pull request opened | Wed Jul 1 |
| Pull request merged; two-week retrospective with Priya | Fri Jul 3 |

## Team and Credentials

**Mei (DRI):** Coordinating access requests, running the June 26 check-in and July 3 retrospective, and serving as the escalation point if the protocol hits a blocker outside Arjun's control.

**Arjun (buddy):** Leads the phase one checklist and phase two walkthroughs, pairs on week two implementation blockers, and reviews the first pull request. Arjun has owned the deployment and on-call tooling for 18 months and is the right person to walk Priya through both.

## Investment

The only cost is internal capacity. There is no external vendor, tooling purchase, or contract.

**Arjun:** approximately 35% in week one (checklist ownership, two walkthroughs, daily check-ins) and approximately 20% in week two (implementation pairing, pull request review). Sprint planning for the June 22 and June 29 sprints should reflect this reduction explicitly; if it is not reflected, the protocol fails silently under sprint pressure.

**Mei:** approximately 15% across both weeks (coordination, check-in facilitation, retrospective).

No budget approval is required. The ask is sprint capacity allocation and your acknowledgment that Arjun's output in those two sprints will be lower than baseline.

## Next Steps

Please reply with your approval by end of day Friday June 19. That window gives Arjun time to be briefed before June 22 and gives the team the weekend to pre-scope the first change so it is ready on Priya's first day.

If the capacity cost is a concern for either sprint, reply with the sprint constraints and we will adjust the buddy schedule. The protocol can absorb some flexibility in week two without moving the July 3 ship target.
