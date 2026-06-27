---
entry_id: project-brief
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# New-Engineer Onboarding - Project Brief

## Goal

Get Priya productive as a contributing member of the backend services team, with her first change shipped and on-call eligibility established, by the end of her second week.

## Background

The backend services team deploys to production daily and runs a shared on-call rotation. Every engineer carries pager load proportional to their system knowledge, which means time to productivity is not just a morale question - it is an operational one. Without structure, two failure modes repeat: new hires spend week one solving access and tooling problems alone while feeling blocked, and their first shipped change arrives in week three or four, long after their sense of belonging has been set by the silence that came before it.

Priya joins on Monday June 22. The team has two weeks before the formal onboarding window closes on July 3. A named owner, an explicit protocol, and pre-scoped milestones are the minimum viable structure for this window.

## Scope

### In scope

- Access provisioning across all required systems (source control, VPN and SSO, CI/CD, observability platform, on-call rotation viewer, secret manager staging access, and relevant chat channels)
- Local environment bootstrap and verification
- Codebase orientation covering service topology, deployment process, and on-call tooling
- A first-change task pre-selected by the team before Priya's start date, scoped to one service with no on-call risk
- Buddy pairing protocol for weeks one and two
- Two-week retrospective with Priya at the close of the formal window

### Out of scope

- On-call rotation eligibility (Priya is excluded by policy for her first 30 days; this initiative operates within that constraint)
- Performance review and goal-setting (handled through the standard engineering review cycle)
- Future iterations of the onboarding protocol (addressed separately after the retrospective surfaces gaps)

## Constraints

- The window opens June 22 and closes July 3; no extension is planned
- The buddy cannot exceed 30-40% capacity in week one or 15-20% in week two without a real cost to team output - sprint planning must account for this before Priya starts
- The first-change task must be scoped and ready on day one; there is no baked-in fallback if it is not

## Success Criteria

- All access items provisioned and verified by end of day one (June 22)
- Priya has traced a full production request in the observability platform before the end of week one
- Priya's first pull request is merged and deployed by Friday July 3
- Two-week retrospective completed with Priya to close the formal window and surface any remaining gaps

## Team

- Owner: Mei (onboarding DRI - decides, escalates, runs the retrospective)
- Contributors: Assigned buddy (access checklist, daily check-ins, week-one pairing); Arjun (week-two code review support)
- Informed: Engineering manager, full backend services team
