---
entry_id: rfc
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# RFC-0012: Structured Two-Week Onboarding Protocol for New Backend Engineers

## Status

Under Review

## Author(s)

Mei (onboarding DRI), June 9

## Problem

The backend services team has no written onboarding protocol. When a new engineer joins, onboarding happens informally: a buddy is assigned the morning the new hire arrives, access requests are filed reactively as gaps surface, and the first meaningful contribution happens when it happens - typically week three or four.

This produces two failure modes we have seen repeat:

**Access and tooling gaps cause invisible blocking.** New hires spend their first week solving environment problems independently. They feel blocked but are reluctant to interrupt teammates who are visibly busy. The buddy does not know what to check because no checklist exists. The silence reads as self-sufficiency; it is usually not.

**The belonging question gets answered by default.** Whether a new hire feels they are actually on the team - not just near it - is mostly decided in the first two weeks. Leaving that window unstructured means it closes on whatever impressions accumulated by chance.

A third factor makes this urgent now: Priya is joining June 22. We have twelve days to put something in place before her first day. The informal approach has worked well enough that we have not felt pressure to change it, but we have also been lucky. Three engineers in the last eighteen months who reported slow starts said the same things: unclear expectations, uncertainty about whether they were blocking anyone by asking questions, and no sense of a structured path through the first two weeks.

## Proposed Approach

Establish a written two-week onboarding protocol with three components:

**1. Access and tooling checklist (Days 1-2).** A named buddy owns a checklist covering source control org membership, VPN and SSO setup, CI/CD pipeline access, observability platform, on-call rotation viewer, secret manager read access for staging, and the relevant chat channels. No item is considered done until the new hire has verified it personally. The buddy files outstanding requests on Day 1 and does not wait for the new hire to notice gaps.

**2. Codebase orientation (Week 1).** Two structured walkthroughs scheduled before the start date: one on service topology and ownership, one on deployment and on-call tooling. The new hire keeps their own notes. A Friday check-in at end of week one confirms whether they can navigate the codebase independently and whether anything is still blocked.

**3. Pre-scoped first change (Week 2).** The team selects the first change before the new hire's start date. Scope constraints: one service, one data model, no on-call risk if the change goes wrong. The new hire drives and does the deploy. The buddy reviews and pairs on blockers. The point is that the new hire's name is in the deployment log before the two-week window closes.

The buddy's load is real: roughly 30-40% capacity in week one, 15-20% in week two. Sprint planning must account for this or the protocol fails before it starts.

## Alternatives Considered

**Unstructured pairing ("sit with someone and absorb").** This is what we do now. It places the entire burden of structure on the relationship between the new hire and whoever is available that day. It also asks the new hire to self-identify what they need, which they cannot do reliably in the first week because they do not yet know what they do not know.

**Fully written runbook with no paired walkthroughs.** A runbook handles access and tooling questions but does not transfer system intuition. The two 90-minute walkthroughs in the proposed approach do something a doc cannot: they show the new hire how an experienced engineer actually moves through the system. That is not written down anywhere, and cannot be.

**Assign onboarding to the tech lead instead of a peer buddy.** This concentrates the load on the highest-leverage person on the team. A peer buddy carries the cost at lower opportunity cost and creates a more lateral relationship. Peer-to-peer onboarding also gives the new hire someone they can ask "is this obvious?" without worrying about signaling weakness to a senior evaluator.

**No pre-scoped first change; let it emerge from sprint planning.** The risk is that week two ends without a ship. Sprint planning under normal pressure tends to route easier work to engineers already calibrated on the codebase. A new hire will be passed over - not because anyone intends it, but because it is faster. Pre-scoping forces that coordination to happen in advance, when there is no sprint pressure on the table.

## Open Questions

1. **Who maintains the checklist between cohorts?** I am proposing the onboarding DRI as the owner, updating it after each new hire completes the protocol. Is that the right home, or should it live with the engineering manager?

2. **How do we handle buddy capacity in sprint estimation?** I have rough figures (30-40% week one, 15-20% week two), but these are not sourced from our team specifically. Should we formalize a reduction factor, or handle it per-sprint at planning? I want Arjun's read on this, since he has seen both sides of the buddy role.

3. **What is the right scope constraint for the first change?** "One service, one data model, no on-call risk" is my first pass, but I am uncertain whether this is too narrow (leaves too little to pick from in the backlog) or too loose (still allows changes that create noise if they go wrong). I want pushback from people who know the current backlog shape.

4. **Does the Friday check-in need a structured format?** A set of specific questions - can you navigate the codebase independently, is anything still blocked, do you know who to ask for what - might surface things a freeform conversation lets slide. But it might also feel like an evaluation at the end of week one. Thoughts on this tradeoff?

## Consequences

**If accepted and followed:**

- New hires have a named owner for access and tooling from Day 1. Gaps do not fall into silence.
- Sprint planning has an explicit capacity model for onboarding weeks. Velocity estimates are honest rather than optimistic.
- Every new engineer ships something before the two-week window closes. That fact changes how the team perceives them and how they perceive themselves.
- The belonging question gets a designed answer rather than a default one.

**Costs and risks:**

- The buddy load is real. If sprint planning does not protect buddy capacity, the buddy absorbs the cost invisibly and resents it. The protocol only works if the team commits to this in advance.
- Pre-scoping the first change requires coordination that can be skipped under pressure. If the task is not ready on Day 1, the week-two structure collapses and we fall back to informal.
- The protocol creates a named onboarding DRI role. Someone has to maintain the checklist, coordinate the buddy assignment, and run the Friday check-in. If that role is not clearly assigned before each new hire arrives, the protocol degrades into a document no one updates.

**Review deadline:** Please comment by June 16. I will synthesize feedback and update the status to Accepted or Withdrawn by June 18, ahead of Priya's June 22 start date.
