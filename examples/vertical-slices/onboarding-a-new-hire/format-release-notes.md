---
entry_id: release-notes
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Engineer Onboarding Protocol v2.0 - June 22, 2026

## Structured pairing replaces informal absorption

## What's new

- **Named buddy with a printed checklist:** Every new engineer now has a named buddy who owns an access-and-tooling checklist for days 1 and 2. Nothing is marked done until the new hire verifies it herself. You no longer start week one discovering on your own that a provisioning step was missed.

- **Pre-scoped first change, ready on day one:** The team selects a first real task before you arrive - one service, low blast radius, clear test path. You receive it on day one, not after a week of searching for something appropriate to start with.

- **Structured on-call exclusion window:** New engineers are formally excluded from the on-call rotation for the first 30 days. This is now written into the protocol, not left to informal team discretion.

## Improvements

- **Access gaps have a named owner:** Provisioning problems - a missing VPN certificate, wrong secret-manager permissions - previously fell into a silent gap. The buddy checklist assigns ownership and a same-day resolution expectation. When Priya joined, a missing VPN cert step was caught on day one and patched into the setup doc the same afternoon.

- **Codebase orientation is guided, not assumed:** Two 90-minute walkthroughs (one on service topology, one on deployment and on-call tooling) replace the informal "sit beside someone and absorb" approach. Notes belong to the new hire; the buddy does not maintain them.

- **Belonging is designed in, not left to chance:** The Friday week-one check-in and the week-two retrospective are now explicit checkpoints. The week-two retrospective (scheduled Jul 3 for Priya) asks directly whether she feels she belongs, not only whether she is functional.

## Fixes

- **Week one no longer disappears into access churn:** New hires no longer spend days 1 to 3 waiting on provisioning without a clear escalation path. The buddy checklist assigns ownership and a resolution expectation before the new hire's first morning.

- **First contribution no longer slips to week three or four:** Pre-scoping the first change against the team's week-two target (PR open by Jul 1, merge by Jul 3 with Arjun pairing as support) makes the two-week ship a plan, not an aspiration.

## Known issues

- **Staging access provisioning may lag:** The infra queue has no guaranteed SLA for new-hire tickets. Priya's staging access request (submitted Jun 23) was still pending as of Jun 26. Workaround: use the team shared credential for staging until individual access resolves; flag the onboarding DRI (Mei) if the ticket is more than three business days old.

- **Pre-scoping requires advance sprint coordination:** If the first change is not ready on day one, week two's structure collapses and the protocol has no built-in fallback task. This step is most likely to be skipped under sprint pressure. Teams should treat pre-scoping as a sprint-planning artifact, not a pre-arrival nice-to-have.

## Deprecations

- **Unstructured peer absorption:** The informal "sit beside someone and absorb" default is no longer the team's onboarding approach. It is not forbidden, but sprint capacity planning will not account for the undeclared buddy time it consumes.
