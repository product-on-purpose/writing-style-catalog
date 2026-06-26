---
entry_id: prd
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Engineer Onboarding: First Two Weeks - Product Requirements

## Problem Statement

New engineers joining a fast-moving backend team that ships to production daily face a repeating set of blockers in their first two weeks: access provisioning is scattered across multiple systems and typically takes one to three days to complete; the codebase has no guided entry path, so new hires spend their first week reading code without context or shipping anything; and there is no explicit conversation about team ownership or on-call responsibilities until the new hire is already expected to carry a pager.

The result is that new engineers become functional - they can run the code and attend the meetings - but they do not feel oriented or trusted with real work until week three or four. That delay extends the period of uncertainty about whether they belong, and belonging is not a soft concern: an engineer who does not feel like a team member by the end of week two is more likely to disengage quietly and less likely to ask the questions that would make them effective faster.

This document sets requirements for the onboarding program for Priya, who started Monday on a backend team with a daily ship cadence and an active on-call rotation. The requirements are intended to be reusable for future engineers in the same role.

## Goals

- Priya ships one real, reviewed, and merged change to production by close of business Friday of week two.
- By end of day Friday of week one, Priya has full working access to every system she needs: source control, the deployment pipeline, secrets management, the ticket tracker, the chat tool, and the on-call runbook.
- By end of week one, Priya can describe the service topology, the team's ownership boundaries, and the release cadence in her own words without prompting.
- By end of week two, Priya knows who to ask for what, and feels comfortable asking without calculating the social cost first.
- By the end-of-week-two retrospective, Priya can say she feels like a member of this team, not a visitor who has been permitted to attend the meetings.

## Non-Goals

The following are explicitly out of scope for weeks one and two:

- **On-call rotation entry.** Familiarity with the runbook is a week-one goal. Being paged is not a week-one or week-two goal. Rotation entry is a week-three or later decision made jointly with Priya, after she has context on at least the services most likely to alert.
- **Comprehensive architecture coverage.** A useful mental model of the services most relevant to her first change is the bar. A full walkthrough of every service the team owns is not. Coverage that is too wide at this stage produces surface familiarity and no depth.
- **Fixing documentation gaps discovered during onboarding.** If gaps surface, they are filed as tech-debt tickets, not resolved in real time at the cost of paired onboarding time.
- **A complex or high-risk first change.** The first change is defined by three criteria: small, real, and merged. A ten-line fix that closes an actual ticket is better than a hundred-line refactor that took two weeks to scope and review.
- **Resolving pre-existing team process issues.** Onboarding reliably surfaces process friction. Addressing that friction is a separate workstream. It should not be loaded onto the onboarding program.

## User Stories / Jobs to Be Done

**Access and tooling (week one)**

- As Priya, I need my local development environment running the full service stack before end of day Tuesday so that I am not blocked from reading and running code while the rest of the team is shipping.
- As Priya, I need a single reference that names who owns what and how to request access so that I do not spend the first week pinging five different people to ask the same question about permissions.
- As Priya, I need a guided walkthrough of the deployment pipeline before I touch it, so that I understand what I am doing when I deploy for the first time and I know who to call if something goes wrong.

**Orientation (week one)**

- As Priya, I want a guided walkthrough of the services my team owns - what they do, how they connect, and what breaks when they fail - so that I can ask informed questions by the time I start pairing on real work.
- As Priya, I want to read through the on-call runbook with someone who can explain the context, so I have a mental model of incident response before I am ever expected to respond to one.
- As Priya, I want to meet each team member for fifteen minutes before the end of week one - not just have names on a team page - so that I know who does what and have a real person behind each chat handle.

**First change (week two)**

- As Priya, I want my first task to be a real ticket - not a synthetic training exercise - so that my work receives the same review bar as everyone else's and I know it matters.
- As Priya, I want to pair with a teammate on my first change so that I learn the team's conventions through doing, not just through reading documentation that may or may not reflect current practice.
- As Priya, I want to own the full lifecycle of my first change - branch, pull request, review, merge, deploy - so that I know I can repeat the process independently, and so I have something concrete to point to at the end of week two.

**Belonging (continuous, both weeks)**

- As Priya, I want to know that asking a basic question will not count against me, so that I do not suppress confusion that a three-minute conversation would resolve.
- As Priya, I want one designated person - not a wiki, not a rotation - who is my first contact for the first two weeks, so that I am not calculating who is safe to interrupt every time I have a question.

## Success Metrics

The following signals are assessed at the end of week two:

- **Shipped change rate**: One merged, production-deployed change by close of business Friday of week two. Binary: either it shipped or it did not.
- **Access completeness**: Zero days in week two where Priya's primary blocker was a missing permission or setup issue rather than the work itself. Any blocked day attributable to provisioning failure is a metric miss.
- **Orientation confidence (self-report)**: In the end-of-week-two retrospective, Priya rates her confidence in explaining the service topology, team ownership model, and release process at 4 out of 5 or higher on a five-point scale she controls.
- **Belonging signal (self-report)**: In the same retrospective, Priya answers "yes" to: "Do you feel like a member of this team?" A "not sure" or "no" is not a failure of the metric; it is a signal requiring immediate follow-up.
- **Paired working time**: At least four hours of active pairing with a named team member during week two, as logged by the designated buddy. Remote or async pairing counts; passive shadowing does not.

## Open Questions

The following assumptions are baked into this plan and have not yet been validated:

1. **Who is Priya's designated buddy?** The plan assumes one named person serves as first contact for two weeks. If no one is available for that commitment, the access, pairing, and belonging goals are all at risk. This decision needs to be made before Priya's first day. It was not made before this document was written.

2. **Is the first-change ticket already identified?** The plan assumes a suitable ticket is waiting in the backlog at the right size and complexity. If the backlog has no appropriate ticket, the team either creates one explicitly or accepts a delay in scoping Priya's first change. The ticket should be reviewed and agreed on by end of week one, not discovered in week two.

3. **Does the deployment pipeline documentation match the current process?** The week-one walkthrough is only as useful as the accuracy of what it covers. If the runbook is stale, the walkthrough may create false confidence. Someone on the team should verify it before Priya's first deploy.

4. **What is Priya's prior experience with service-oriented architectures?** The orientation scope assumes working familiarity with distributed services. If that assumption is wrong, the week-one mental model goal may need to be scoped to two or three core services rather than the full topology, and the timeline for the first change should be adjusted accordingly.

5. **Has the team agreed on what "belonging" looks like in practice?** The belonging goal is the most important goal in this document and the least defined one. A single retrospective question is a minimum signal, not a definition. The team has not yet discussed what behaviors, norms, and interactions produce belonging for a new member on this specific team. That conversation should happen before week two ends, not deferred to a future quarter when the window has already closed.
