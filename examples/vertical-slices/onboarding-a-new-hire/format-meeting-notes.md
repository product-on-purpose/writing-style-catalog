---
entry_id: meeting-notes
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Meeting Notes - Priya Onboarding Planning (Weeks 1 and 2)

Date: 2026-06-23
Attendees: Marcus (engineering manager), Keiko (senior engineer / onboarding buddy), Tariq (tech lead), Devi (on-call coordinator)

## Context

Priya joins the team Monday. She has backend experience but is new to our service topology and daily deployment cadence. This meeting set the two-week plan to get her to a shipped change by the end of week two and onto the on-call shadow rotation by week three.

## Decisions

- Keiko is Priya's designated onboarding buddy for weeks 1 and 2, with daily 15-minute check-ins blocked on the calendar.
- The first-change target is the retry-timeout configuration in the auth service - it is isolated, well-tested, and representative of how the team works.
- Priya does not go on-call until week five at the earliest; she shadows the rotation starting week three with Devi as guide.
- Access provisioning follows the standard new-hire checklist; Priya should have baseline permissions by end of day Monday.
- Week one keeps Priya's calendar clear of cross-team meetings; she attends only team rituals (standup, deployment review).
- The team norm during onboarding is that no question is too small - Keiko is the first point of contact, and Priya should not default to async searches when a five-minute conversation would unblock her faster.
- Priya's first pull request will go to Keiko for review, not to the general queue, so feedback stays contextual and timely.

## Actions

- [ ] Send Priya the pre-read packet (architecture overview, deployment runbook, on-call handbook) - owner: Marcus - due: Friday 2026-06-26 (before start date)
- [ ] Complete access provisioning checklist (VPN, code repository, ticket tracker, CI/CD pipeline, logging dashboard, chat tool) - owner: Keiko - due: Monday 2026-06-29 EOD
- [ ] Create and assign the first-change ticket in the tracker with a clear scope and the relevant runbook linked - owner: Tariq - due: Monday 2026-06-29
- [ ] Schedule a 30-minute codebase walkthrough covering service boundaries and the deployment pipeline - owner: Tariq - due: Tuesday 2026-06-30
- [ ] Walk Priya through a full deployment end-to-end (shadow only, not driving) - owner: Tariq - due: Thursday 2026-07-02
- [ ] Introduce Priya to on-call tooling and explain the rotation schedule and escalation path in a low-stakes session - owner: Devi - due: Friday 2026-07-10 (end of week two)
- [ ] Open first pull request for the retry-timeout change and request review from Keiko - owner: Priya - due: Friday 2026-07-10 (end of week two)
- [ ] Review Priya's first pull request with inline notes explaining the "why" behind any requested changes - owner: Keiko - due: Friday 2026-07-10 or same day as PR if time allows
- [ ] Hold end-of-week-one check-in with Marcus to surface blockers, missing context, or tooling gaps - owner: Marcus - due: Friday 2026-07-03

## Open Items / Parking Lot

- Confirm whether Priya's laptop arrives Monday morning or needs a loaner for day one - owner: Keiko - check with ops by Thursday
- Decide which runbooks Priya should annotate as a learning exercise vs. which are stable and should not be touched yet - owner: Tariq - discuss in Tuesday walkthrough
- Clarify who holds the on-call pager during Priya's shadow weeks if Devi is out - owner: Devi - resolve before week three
- Consider a brief team lunch or informal welcome in week one to introduce Priya to members she will not meet in structured sessions - owner: Marcus - optional, gauge team appetite
