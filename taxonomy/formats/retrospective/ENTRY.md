---
id: retrospective
name: Retrospective
axis: format
domain: professional
family: appraisal
one_liner: A structured look back at a period of work that surfaces what went well, what did not, and what the team will change.
description: |
  A retrospective is a structured look back at a completed period of work - a sprint, a project,
  or a quarter - to surface what went well, what did not, and what the team will change. Its
  purpose is improvement, not blame, and it runs on a regular cadence regardless of whether
  anything went wrong. The retrospective examines the whole working process and ends in concrete
  action items with named owners.

  Unlike a postmortem, which is triggered by a specific failure or incident and drives to a
  systemic root cause using a time-stamped timeline and a severity rating, a retrospective covers
  the full arc of a working period. No single event needs to have occurred; the format works
  across ordinary sprints, smooth quarters, and difficult ones alike.

  The standard retrospective structure organizes observations into three questions: What Went
  Well (practices to protect or repeat), What Did Not Go Well (friction, blockers, waste), and
  What Will We Change (specific, owned commitments for the next period). Some teams use named
  exercises - Start/Stop/Continue or the 4Ls - that map to the same three questions under
  different labels.

  The retrospective earns its keep not in the meeting itself but in the action items that follow.
  A retrospective that surfaces problems without producing owned commitments is cathartic venting,
  not improvement. The change column is the product.
canonical_template: |
  # Retrospective: [Period] - [Team or Project]

  ## Date

  [Date held]

  ## What Went Well

  - [practice, decision, or behavior worth repeating]

  ## What Did Not Go Well

  - [friction, blocker, or waste that cost the team]

  ## What Will We Change

  - [ ] [Specific change] - Owner: [person] - By: [next retro / date]

  ## Notes

  [Anything that does not fit the three columns but the team needs to remember]
typical_voices:
  - coach
  - operator
typical_tones:
  - candid
  - encouraging
digital_or_print: digital
pairs_well_with:
  - coach
  - operator
  - candid
  - encouraging
  - decision-log
avoid_with:
  - reverent
  - urgent
  - skeptical
confusable_with:
  - postmortem
when_to_use:
  - At the end of every sprint, iteration, or regular working period
  - After a project or milestone, to capture what to carry forward and what to leave behind
  - When recurring friction or slowdowns have no shared name or owner
  - When the team needs a shared record of what it is committing to change
  - When establishing a norm of open process reflection with a new or growing team
when_not_to_use:
  - When a specific incident or failure needs investigation - use a postmortem that drives to root cause and quantifies impact
  - When the goal is to document a decision and its rationale for future readers
  - When the team has not yet completed a working period to reflect on
tells:
  - 'Three-question structure: What Went Well, What Did Not Go Well, What Will We Change'
  - 'Covers a whole working period rather than a single event or incident'
  - 'Runs on a fixed cadence regardless of whether anything went wrong'
  - 'Action items in the change column carry a named owner and a target deadline'
  - 'Participation is collective - observations represent the whole team, not one author'
  - 'Forward-looking frame: the output is a commitment list, not a verdict or audit'
anti_patterns:
  - pattern: 'Naming individuals in What Did Not Go Well instead of the practices or processes that broke'
    why: 'The improvement mandate collapses when people feel they are on trial; the column exists to name systemic and process failures, not personal fault.'
  - pattern: 'Collecting action items without assigning a named owner and a target date'
    why: 'An unowned action item is a wish; without a name and a deadline, it reappears unchanged in the next retrospective.'
  - pattern: 'Running the retrospective format when a specific incident has occurred and needs dedicated investigation'
    why: 'A postmortem is triggered by a specific failure or near-miss and uses a time-stamped timeline to reconstruct the sequence of events, driving to a systemic root cause; a retrospective covers the full working period and cannot substitute for that focused causal analysis.'
  - pattern: 'Skipping What Went Well because the period was difficult'
    why: 'The went-well column identifies practices to protect and repeat; omitting it produces a document that only names problems and gives the team no anchor for what is working.'
failure_modes:
  - mode: 'Psychological-safety norm tips into conflict-avoidance - the blameless stance gets pushed so far that the What Did Not Go Well column fills with trivial inconveniences while real friction goes unspoken'
    mitigation: 'Distinguish blame from candor: blame attributes failure to an individual; candor names the practice, decision, or system that broke. A column full of trivial items signals the format has tipped into false safety.'
  - mode: 'Commitment-to-change tips into an aspirational backlog - the change column accumulates more items than the team can execute, items roll forward indefinitely, and the format loses credibility'
    mitigation: 'Cap the change list to what can realistically ship before the next session; treat a recurring item as an escalation rather than a re-add; close items before opening new ones.'
llm_instruction_phrasing: |
  Write as a team retrospective. Use the three-question structure: What Went Well, What Did Not
  Go Well, and What Will We Change. In What Went Well: name specific practices, decisions, or
  behaviors worth repeating - not vague praise. In What Did Not Go Well: name the process,
  practice, or system that created friction, not individuals. In What Will We Change: every item
  must have a named owner and a target date or next-retro deadline; unowned items do not count.
  Keep the frame improvement-focused, not verdict-focused; the purpose is the change column, and
  everything else exists to fill it well. Do not let the change list grow beyond what the team
  can realistically execute before the next session.
tags:
  - team-process
  - agile
  - improvement
  - cadence
  - accountability
  - sprint
review_status: draft
---

## Retrospective

A retrospective is a structured look back at a completed period of work - a sprint, a project, or a quarter - to surface what went well, what did not, and what the team will change. Its purpose is improvement, not blame, and it runs on a regular cadence regardless of whether anything went wrong. The retrospective examines the whole working process and ends in concrete action items with named owners.

Unlike a postmortem, which is triggered by a specific failure or incident and drives to a systemic root cause using a time-stamped timeline and a severity rating, a retrospective covers the full arc of a working period. No single event needs to have occurred; the format works across ordinary sprints, smooth quarters, and difficult ones alike.

The standard retrospective structure organizes observations into three questions: What Went Well (practices to protect or repeat), What Did Not Go Well (friction, blockers, waste), and What Will We Change (specific, owned commitments for the next period). Some teams use named exercises - Start/Stop/Continue or the 4Ls - that map to the same three questions under different labels.

The retrospective earns its keep not in the meeting itself but in the action items that follow. A retrospective that surfaces problems without producing owned commitments is cathartic venting, not improvement. The change column is the product.

### Canonical template

```
# Retrospective: [Period] - [Team or Project]

## Date
[Date held]

## What Went Well
- [practice, decision, or behavior worth repeating]

## What Did Not Go Well
- [friction, blocker, or waste that cost the team]

## What Will We Change
- [ ] [Specific change] - Owner: [person] - By: [next retro / date]

## Notes
[Anything that does not fit the three columns but the team needs to remember]
```

### When to use

At the end of every sprint, iteration, or regular working period; after a project or milestone to capture what to carry forward and what to leave behind; when recurring friction or slowdowns have no shared name or owner; when the team needs a shared record of what it is committing to change; when establishing a norm of open process reflection with a new or growing team.

### When not to use

When a specific incident or failure needs investigation - use a postmortem that drives to root cause and quantifies impact; when the goal is to document a decision and its rationale for future readers; when the team has not yet completed a working period to reflect on.

### Pairs well with

`coach`, `operator`, `candid`, `encouraging`, `decision-log`

### Often confused with

**postmortem**: A postmortem is a structured account of a failure, near-miss, or significant service degradation - triggered by a specific incident, not by the passage of time. It uses a precise, time-stamped timeline to reconstruct what happened and when, drives the analysis to the systemic root cause rather than stopping at the proximate trigger, and quantifies blast radius with an impact section. A retrospective, by contrast, runs on a regular cadence and examines the whole working period; no incident needs to have occurred. When a specific failure needs dedicated root-cause investigation and owned remediation commitments, a postmortem is the right format.
