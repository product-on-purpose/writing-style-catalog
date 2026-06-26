---
entry_id: technical-reference
axis: format
topic_slug: thanking-a-mentor
topic_label: Writing to thank a mentor who shaped your career
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Sponsorship Under Uncertainty

A mentorship behavior in which a senior practitioner nominates an under-ready report for a high-visibility assignment, then provides calibrated support without assuming control of the execution.

## Signature

```
sponsor(report: under-ready, assignment: high-stakes) -> ownership, credibility, forward-pattern
```

The sponsoring practitioner absorbs short-term risk to their own reputation and workload in exchange for the report's long-term capability gain.

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| nomination | yes | Public, specific, and unqualified endorsement of the report for a role they have not yet held |
| presence | yes | Sustained availability during execution - visible enough that the report is not isolated, close enough to catch structural failure early |
| non-intervention | yes | Restraint from substituting the sponsor's judgment for the report's own when the report struggles |
| patience reserve | yes | Tolerance for slower progress and repeated questions than the sponsor would accept from an experienced practitioner |
| explicit delegation | yes | Statement to stakeholders that the report has decision authority, not merely execution responsibility |

## Observed Instance

**Assignment:** Nordvik Platform Migration, Q2 of my third year at Calloway Systems. An infrastructure consolidation project with three legacy teams as stakeholders, a fixed deadline, and a budget I had not managed before at that scale.

**Who put me forward:** Dana Reyes, then Director of Platform Engineering. She had managed me for 18 months. I had shipped small projects. I had not led cross-team work.

**What she said to me:** "You are the right person for this. I will be available. You will make the calls."

**What she said to the stakeholders:** The same, without caveats.

**What she did not do during execution:**
- She did not attend the stakeholder syncs unless I invited her.
- She did not correct my communication drafts before I sent them.
- She did not contact the stakeholders directly when one of them escalated to her.
- She answered the escalation by pointing back to me.

**What she did do:**
- Weekly 30-minute syncs, at my request, where I described what I was stuck on and she asked questions rather than giving answers.
- One instance, at week six, when she said: "That decision you are about to make is reversible if you are wrong. Make it." She did not tell me what to decide.

**Duration of support:** Full eight weeks of active execution. No formal handoff - she simply stopped checking in when I stopped needing to be checked in on.

## Returns

**Immediate:** The Nordvik migration shipped on schedule. I led the retrospective. The three stakeholder leads credited the project in their own performance reviews that quarter.

**Lasting:**

| Output | Onset | Still present |
|--------|-------|---------------|
| Comfort operating in ambiguity | Within the project | Yes |
| Credibility with senior stakeholders | End of Q2 | Yes |
| Understanding of what sponsorship looks like from inside | Took several years to name | Yes |
| Ability to replicate the behavior with my own reports | This year | Yes |

The last item is why I am writing this.

## Cost to the Sponsor

This section exists because the behavior carries real costs that are easy to discount from the report's side.

| Cost | Nature | Why it is not trivial |
|------|--------|----------------------|
| Reputation exposure | If the project failed, Dana's judgment was on the record | She had nominated me without caveats |
| Patience overhead | My questions in weeks two and three were questions she could have answered in fifteen seconds by taking over | She did not take over |
| Restraint against escalation | One of the three stakeholders went directly to her when he was unhappy with my pace | She redirected him to me, which cost her a relationship shortcut |
| Opportunity cost | The time she held open for my weekly syncs was time she did not spend on her own deliverables | She held it open every week |

I did not understand most of this cost at the time. I understood it this year, when I put Theo Marchetti forward to lead a comparable project and felt each of these costs from the other side.

## Notes and Constraints

**This is not delegation.** Delegation transfers a task. Sponsorship transfers a role with visibility attached. The distinction matters because the report's credibility is publicly committed before they have earned it.

**The non-intervention constraint is the hardest part.** The instinct when a report is struggling is to fix the thing they are struggling with. Fixing it is faster, cleaner, and less painful to watch. What Dana did instead was ask me what I thought the options were and then stay quiet. The staying quiet is load-bearing. It is also uncomfortable to sustain for eight weeks.

**It does not work without explicit delegation to stakeholders.** If Dana had said privately that I was in charge but let the stakeholders treat her as the real decision point, the project would have trained the wrong thing - that I had execution responsibility but not decision authority. She foreclosed that ambiguity before it formed.

**The support is not open-ended.** The behavior ends when the report has internalized the operating pattern. Continuing past that point converts support into a scaffold the report starts to expect.

## When to Apply

- Report has demonstrated judgment at smaller scale and needs the visible-stakes version to develop credibility
- The assignment has a real failure mode, not a safe practice run - the risk is what makes the development real
- The sponsor has the standing to make the public nomination stick
- The sponsor has available bandwidth to sustain weekly presence without it becoming performative check-ins

## When Not to Apply

- The assignment is genuinely beyond the report's current capacity by a margin that would require the sponsor to silently carry the work
- The sponsor cannot or will not redirect stakeholder escalations back to the report
- The sponsor's restraint is not genuine - if the sponsor will intervene when the discomfort crosses a threshold, the report learns that threshold rather than learning to operate without it

## See Also

- Theo's project (internal, Q1 this year) - I did not tell him what Dana had done. I wanted him to experience it without a name on it, the same way I did.
- This document - the closest I have come to a complete specification of what Dana gave me.
