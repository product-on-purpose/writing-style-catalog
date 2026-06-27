---
entry_id: design-doc
axis: format
topic_slug: thanking-a-mentor
topic_label: Writing to thank a mentor who shaped your career
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Mentorship-by-Sponsorship Design Document

*Written to Dana, who implemented this in 2016, and to Priya, who is currently running inside it.*

## Status

Accepted - implemented March 2016; actively replicated as of February 2026.

## Problem

In early 2016 my organization needed a lead for the Alderton platform migration: six months, cross-functional, visible to senior stakeholders. The organization expected someone who had already run a project at that scope. I had not.

Dana had a junior contributor - me, in my second year - who had demonstrated aptitude in smaller work but had no track record at the scale the role required. The conventional move was to name an established mid-level person. The opportunity cost of that move was that I would not develop.

The constraints shaping the solution space:

**Real accountability cannot be delegated in halves.** If the lead carries decisions made by someone more senior, the project delivers but the person does not develop. The accountability has to land somewhere and stay there.

**Simulated stakes do not transfer.** Practice projects and pre-assignment coaching produce a kind of readiness that does not survive first contact with a real deadline and a stakeholder expecting answers. The capacity for judgment under pressure can only be built under actual pressure.

**The sponsor holds an unrecoverable position.** If the project failed, the organization would remember Dana's judgment, not my inexperience. The asymmetry between candidate exposure and sponsor exposure is not incidental - it is the central structural fact of this design.

**Co-lead arrangements teach nothing at the relevant margin.** When a decision becomes difficult, the senior person absorbs it. The junior person watches. That is observation, not development.

## Proposed Design

Dana's implementation can be characterized as three sequential phases with a governing constraint that operates across all three.

**Phase 1 - Nomination**

Nominate the candidate before they feel ready. Do not wait for the candidate to ask. Self-nomination would allow them to frame the appointment as something they earned through confidence. Confidence is not a prerequisite. Submit the name to the relevant stakeholder without flagging the appointment as developmental stretch. The candidate is the lead, not a developmental candidate.

*Interface:* Sponsor names the candidate to the decision-maker unilaterally. Candidate learns they have been nominated, not asked.

**Phase 2 - Close shadowing (months 1 through 3)**

Stay visible and available. Attend key stakeholder meetings for the first two months and say little. When the candidate asks a question, answer it - then ask a sharper one back, the kind that surfaces what they are not yet seeing. When the candidate gets something wrong in a meeting, correct it privately afterward, not during.

*Critical negative constraint:* Do not accept the work back. If the candidate offers to return accountability in a moment of panic, decline without softening the boundary. Accepting the work back ends the intervention.

*State transition signal:* The candidate runs a stakeholder meeting without referencing the sponsor for validation. At that point, advance to Phase 3.

**Phase 3 - Withdrawal (months 3 through 6)**

Reduce visibility. Stop attending standing meetings. Remain available by request but do not initiate contact. The work is the candidate's.

*Exit condition:* The project delivers with the candidate as the named accountable party. The sponsor does not appear in the post-mortem as a contributor.

**Governing constraint (all phases):** The sponsor must hold back intervention even when the candidate is working more slowly or less cleanly than the sponsor would. This is not a feature of the design - it is the design. Every accelerated intervention shifts attribution of the outcome away from the candidate. The candidate will register this transfer even if neither party names it.

## Alternatives Considered

**Assign an established mid-level lead.** Delivers the project. Does not develop the junior contributor at the relevant scope. The safer call and the costlier one over time.

**Co-lead arrangement.** Grants the candidate title and nominal shared accountability. When a call becomes difficult, the senior person absorbs it. The junior person observes. The candidate learns that accountability is shared when it is easy and transferred when it is hard. That is the wrong lesson.

**Intensive pre-assignment coaching.** Better than no preparation. Does not transfer. The stakes remain simulated and the candidate knows it. Coaching produces confidence without the evidence base that makes confidence durable.

**Wait for a fuller track record at smaller scope.** Each deferred cycle is another period the candidate spends at a scope that is not building the capacity you need them to have. Deferral compounds in cost. At sufficient lag, the candidate is developed by someone else or stops waiting.

## Risks and Open Questions

**Sponsor reputational exposure is real and unhedged.** Dana held a vulnerable position for the full duration of the Alderton project. There is no mitigation that preserves the intervention's value while removing this exposure. A sponsor who cannot hold this position should not use this design.

**The nomination decision is the critical gate.** The intervention has no clean early-exit mechanism. If the sponsor has misread the candidate's baseline, taking back accountability midway through invalidates the development value and leaves the project in a worse position than if it had been led by the established mid-level person from the start.

**The patience cost is not visible on delivery plans.** The time Dana spent absorbing my uncertainty across six months - check-ins, redirects, holding space while I worked through decisions she could have made in an afternoon - does not appear in any project management view. Organizations will not have priced this overhead when the intervention is running. Sponsors should expect to carry it without recognition during the project.

**Replication fidelity degrades without a written record.** When I nominated Priya Osei for the Cassava data-pipeline rebuild in February 2026, I was working from memory. I had one pattern to replicate and I had experienced it from the inside. Someone who had not experienced this approach would have no implementation to work from. That is the reason this document exists.

## Appendix

**From the 2016 record (Alderton platform migration):**

- March 2016: Dana submits nomination for Sable Marchetti as project lead
- Months 1 through 2: Dana attends primary stakeholder review meetings; intervenes rarely
- Week 11: Sable offers to hand the project back; Dana declines
- Month 4: Dana stops attending standing meetings; available on request
- April 2017: Project closes; Dana not named in the post-mortem

**From the 2026 record (Cassava data-pipeline rebuild):**

- February 2026: Priya Osei nominated for project lead; she said she was not ready
- Week three, March 2026: Priya stuck on handoff logic; Sable sits on her hands
- June 2026: Priya is four weeks ahead of original schedule

**Note on this document:** The 2016 intervention was not documented at the time. This record was written in June 2026, ten years after implementation, by the person who was developed by it. The system Dana built in 2016 is currently running in my team. I did not have a name for what she did until I found myself doing it. The debt is acknowledged. The design is worth preserving.
