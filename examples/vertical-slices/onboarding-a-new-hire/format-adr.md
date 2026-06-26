---
entry_id: adr
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# [ADR-0023] Structured Guided Pairing for New-Engineer Onboarding

## Status

Accepted

## Context

We ship to production every day. Our on-call rotation means every engineer on the team carries pager load proportional to their system knowledge. When a new engineer joins, they need credentials, repository access, tooling configuration, and enough codebase familiarity to contribute safely - and they need it within two weeks, because the team's capacity to absorb sustained hand-holding degrades fast.

Two failure modes repeat when we skip structure:

**First:** The new hire spends week one solving access and tooling problems independently, feeling blocked but reluctant to interrupt busy teammates.

**Second:** The new hire ships their first change in week three or four. By then, whether they feel they belong has been decided largely by the silence of the preceding weeks.

A third constraint: the delivery cadence does not pause for onboarding. A buddy cannot spend the full day with a new hire without a real cost to their own output. Any protocol must account for this, not pretend it away.

Alternatives considered: unstructured "sit beside someone and absorb"; fully written runbook with no paired work; assigning onboarding to the tech lead rather than a peer buddy.

## Decision

We will run a structured two-week guided pairing protocol with a named buddy, explicit daily check-ins, and a pre-scoped "first real change" task handed off on day one. The protocol covers three domains:

1. **Access and tooling (days 1-2):** The buddy owns a printed checklist. No item is considered done until Priya has verified it herself.

2. **Codebase orientation (week one):** Two 90-minute guided walkthroughs - one on the service topology, one on the deployment and on-call tooling. Notes belong to Priya; the buddy does not maintain them.

3. **Paired first change (week two):** The team picks the task before Priya's first day. Scope constraint: one service, no on-call risk if the change goes wrong. Priya drives; the buddy reviews and pairs on blockers.

We will not wait for the new hire to self-identify her first contribution. The team owns that decision in advance.

## Consequences

### Positive

- Priya's name appears in the deployment log before the end of week two. The team's perception of her, and her perception of herself, shifts accordingly.
- The buddy checklist means access and tooling problems have a named owner. They stop falling into a silent gap.
- Belonging is given structure rather than being left to chance - the protocol designs for it rather than hoping it emerges.

### Negative

- The buddy loses roughly 30-40% of their capacity in week one and 15-20% in week two. This is a real cost. Sprint planning must account for it explicitly, or the protocol fails silently.
- Pre-scoping the first change before Priya arrives requires coordination the team may skip under sprint pressure. If the task is not ready on day one, the protocol's week two collapses.
- If the pre-scoped task blocks unexpectedly (service churn, shifting dependencies), there is no baked-in fallback. The buddy improvises, which introduces variance the checklist cannot cover.

### Neutral

- The buddy relationship created here does not automatically end at two weeks. It tends to become an informal mentorship channel. The team should expect this and treat it as a feature, not drift.
- Priya is explicitly excluded from the on-call rotation for her first 30 days. This protocol does not change that rule; it operates within it.
