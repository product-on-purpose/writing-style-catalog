---
entry_id: pitch-deck
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## Slide 1: The Same Two Failures, Every Time

New engineer joins. Without structure, the same two things happen.

- Week 1: blocked on access and tooling, reluctant to interrupt busy teammates, nothing ships
- Week 2 or 3: first change finally lands - too late for the team's first impression to be reversed, too late for the new hire to feel she belongs

We ship daily. We run a shared on-call rotation. Sustained hand-holding degrades team capacity. Unstructured onboarding does not disappear - it transfers the cost to the new hire.

## Slide 2: The Fix - A Named Protocol, Not a Vague Expectation

A two-week guided pairing protocol: one named buddy, one pre-scoped first change, explicit daily check-ins.

Three constraints that make it work:

- The team picks the first-change task before day one - scope locked to one service, no on-call blast radius
- Access and tooling have a named owner (the buddy) and are not done until the new hire verifies each item
- Notes belong to the new hire; the buddy does not maintain them

## Slide 3: Why Standardize Now

The team is adding headcount. On-call load scales with headcount.

- Every unstructured onboarding produces a slower, more expensive ramp than the last as the codebase grows
- Belonging gaps do not heal on their own - each week without structure widens the cost
- We have a pilot running now with Priya (joined Jun 22) that lets us validate the protocol before committing to it as a standard

This is the lowest-friction moment to adopt: one pilot, one DRI, one set of results to review before the next hire.

## Slide 4: How the Protocol Works

Three domains. Fifteen working days. One clear owner at each stage.

- **Days 1-2 - Access and tooling:** Buddy-owned checklist; each item marked done only after Priya verifies it herself
- **Week 1 - Codebase orientation:** Two 90-minute guided walkthroughs - service topology first, then deployment and on-call tooling; new hire keeps the notes
- **Week 2 - Paired first change:** Pre-scoped task, new hire drives, buddy reviews and pairs on blockers; new hire does the deploy

Goal: Priya's name in the deployment log before the end of week two.

## Slide 5: What Priya's Week One Showed (Jun 22-26)

The pilot ran the first week of the protocol. Results:

- Full access live by Monday afternoon; one setup doc gap found and patched same day
- Priya navigated three services independently by day 3, without prompting
- Week 2 change fully designed by Thursday; Priya caught an edge case the team had missed
- Priya attended a live incident response and knows the escalation path
- Three teammates have async threads going with her outside the formal onboarding plan

One open risk: staging credentials still pending in the infra queue (submitted Jun 23). Shared credential covers her for now; her own access is needed before the Jul 2 on-call alert drill.

## Slide 6: The Real Cost

The protocol is not free. Budget it into sprint planning or it fails silently.

- Week 1: buddy loses roughly 30-40% of capacity
- Week 2: roughly 15-20% as the new hire drives independently

What you buy: an engineer who ships in week two, navigates the codebase on her own, and has real human threads with the team. The unstructured alternative costs the same capacity with no designed outcome and a week-four first ship.

## Slide 7: Three Roles, No Dedicated Function

- **Mei (DRI):** Runs the protocol, owns the check-in schedule, tracks the two-week close
- **Arjun (buddy):** Paired engineer for week two; reviews Priya's first PR; carries the access checklist in week one
- **Team:** Owns the pre-scoped first-change decision before each new hire's start date - the one coordination step that cannot be delegated

No dedicated onboarding function required. The protocol runs on existing team structure.

## Slide 8: The Ask

Adopt the two-week guided pairing protocol as the team standard for all future engineer onboarding.

Three approvals needed:

1. **Engineering manager:** Confirm buddy capacity cost goes into sprint planning at each new hire's start - not treated as an optional buffer
2. **Tech lead:** Own the pre-scoped first-change task decision before each new hire's day one
3. **Next DRI:** Name the onboarding DRI for the next hire before Priya's close-out retro on Jul 3

Two-week retro with Priya on Jul 3 closes the pilot and captures what to carry forward.
