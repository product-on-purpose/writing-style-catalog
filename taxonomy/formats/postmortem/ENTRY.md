---
id: postmortem
name: Postmortem
axis: format
domain: professional
family: appraisal
one_liner: 'A blameless retrospective of an incident: what happened, why, the impact, and the changes that keep it from happening again.'
description: |
  A postmortem is a structured account of a failure, near-miss, or significant service degradation.
  It traces what happened, when, and why - not to assign blame but to surface the systemic conditions
  that allowed the event to occur. Done well, a postmortem converts a painful episode into
  institutional knowledge that makes the system safer and the team more resilient.

  The canonical postmortem separates timeline from analysis. A precise, time-stamped timeline lets
  reviewers reconstruct the sequence of events without relying on disputed memory; the analysis
  sections then ask why each link in the chain failed, following the chain until it reaches a
  systemic root cause rather than a human one. The blameless posture is not a courtesy - it is
  epistemically necessary: when individuals fear blame, the candid detail that reveals the real
  cause goes unspoken.

  Postmortems earn their place when they end with concrete, owned, time-bound action items. A
  postmortem that catalogues what went wrong without committing to change is archaeology, not
  learning. The action items are the contract the team makes with itself to close the gap between
  the world as it was and the world as it should be.

  Typical length: 500-1500 words, scaling with incident severity.
canonical_template: |
  # Postmortem: [Incident Title]

  ## Severity
  [SEV-1 | SEV-2 | SEV-3 | SEV-4]

  ## Summary
  [2-3 sentences: what broke, when, and the blast radius.]

  ## Timeline
  - HH:MM UTC - [event]
  - HH:MM UTC - [event]

  ## Root Cause
  [The systemic condition that allowed the incident to occur. Follow the chain past the proximate trigger.]

  ## Impact
  - Users affected: [count or percentage]
  - Duration: [start] to [end]
  - Services affected: [list]

  ## Contributing Factors
  - [factor]

  ## Action Items
  - [ ] [Specific change] - Owner: [person/team] - Due: [date]

  ## Lessons Learned
  [What the team now knows that it did not know before.]
typical_voices:
  - operator
  - pragmatic-architect
typical_tones:
  - candid
  - matter-of-fact
digital_or_print: digital
pairs_well_with:
  - operator
  - pragmatic-architect
  - candid
  - matter-of-fact
  - decision-log
  - problem-solution
avoid_with:
  - playful
  - celebratory
  - pastoral
  - reverent
confusable_with:
  - adr
  - status-report
when_to_use:
  - After a production incident, service outage, or significant near-miss
  - When a team needs to convert a failure into shared institutional knowledge
  - To produce concrete, owned remediation commitments after an incident
  - When building a safety culture that treats incidents as systemic signals rather than individual failures
  - Communicating transparently with stakeholders about what went wrong and what changes are coming
when_not_to_use:
  - Routine project retrospectives that have no specific incident to investigate
  - Celebrating successful launches or milestones
  - Documenting forward-looking design or architectural decisions
tells:
  - 'A blameless framing that names systemic root causes rather than individual errors'
  - 'A precise, time-stamped event timeline that reconstructs the sequence of the incident'
  - 'A root cause statement that follows the chain past the proximate trigger to a systemic condition'
  - 'An impact section that quantifies blast radius: users affected, duration, services degraded'
  - 'Action items with named owners and due dates, not vague process aspirations'
  - 'A lessons-learned section that states what the team now knows that it did not before'
anti_patterns:
  - pattern: 'Assigning blame to an individual instead of tracing the systemic conditions that made the failure possible'
    why: 'Blameless postmortems surface the real cause; blame-forward ones stop at the nearest human and leave the systemic gap intact.'
  - pattern: 'Writing action items as vague process aspirations such as "improve monitoring" without named owners or due dates'
    why: 'Unowned, undated action items are wishes, not commitments; they evaporate and the gap the incident exposed stays open.'
  - pattern: 'Skipping the timeline and jumping straight to root cause and action items'
    why: 'The timeline is where contested memories get reconciled and hidden contributing factors surface; omitting it loses the evidence the analysis rests on.'
  - pattern: 'Writing the document as a status update covering ongoing project health instead of a specific incident investigation'
    why: 'That slides into the confusable status-report format; a postmortem is always anchored to a specific, bounded incident, not ongoing project state.'
failure_modes:
  - mode: 'Forensic over-reach - the root-cause chain is drilled so deep that the document becomes a months-long audit that no one reads and no action items ship'
    mitigation: 'Stop the chain when you reach a systemic condition you can actually fix; flag the next layer as a separate lower-priority item and ship the action items you have.'
  - mode: 'Blamelessness tips into false neutrality - every contributing factor is so softened that the document avoids naming what specifically broke and the action items have no teeth'
    mitigation: 'Blameless means no named individuals bear fault, not that the document avoids naming the specific system, process, or decision that failed; be precise about what broke, even when it is uncomfortable.'
llm_instruction_phrasing: |
  Write as a blameless postmortem. Use the canonical structure: Severity, Summary, Timeline,
  Root Cause, Impact, Contributing Factors, Action Items, Lessons Learned. In the Timeline:
  list events in chronological order with timestamps; be precise about what was observed, not
  what was assumed. In Root Cause: follow the causal chain past the proximate trigger to the
  systemic condition that allowed the incident to occur - name systems, processes, and decisions,
  not people. In Action Items: every item must have a named owner and a due date; vague
  aspirations do not count. Do not soften findings to the point that the document avoids naming
  what broke. Blameless means no individual fault - it does not mean imprecise.
tags:
  - incident-response
  - retrospective
  - reliability
  - engineering
  - accountability
review_status: draft
---

## Postmortem

A postmortem is a structured account of a failure, near-miss, or significant service degradation. It traces what happened, when, and why - not to assign blame but to surface the systemic conditions that allowed the event to occur. Done well, a postmortem converts a painful episode into institutional knowledge that makes the system safer and the team more resilient.

The canonical postmortem separates timeline from analysis. A precise, time-stamped timeline lets reviewers reconstruct the sequence of events without relying on disputed memory; the analysis sections then ask why each link in the chain failed, following the chain until it reaches a systemic root cause rather than a human one. The blameless posture is not a courtesy - it is epistemically necessary: when individuals fear blame, the candid detail that reveals the real cause goes unspoken.

Postmortems earn their place when they end with concrete, owned, time-bound action items. A postmortem that catalogues what went wrong without committing to change is archaeology, not learning. The action items are the contract the team makes with itself to close the gap between the world as it was and the world as it should be.

### Canonical template

```
# Postmortem: [Incident Title]

## Severity
[SEV-1 | SEV-2 | SEV-3 | SEV-4]

## Summary
[2-3 sentences: what broke, when, and the blast radius.]

## Timeline
- HH:MM UTC - [event]
- HH:MM UTC - [event]

## Root Cause
[The systemic condition that allowed the incident to occur. Follow the chain past the proximate trigger.]

## Impact
- Users affected: [count or percentage]
- Duration: [start] to [end]
- Services affected: [list]

## Contributing Factors
- [factor]

## Action Items
- [ ] [Specific change] - Owner: [person/team] - Due: [date]

## Lessons Learned
[What the team now knows that it did not know before.]
```

### When to use

After a production incident, service outage, or significant near-miss; when a team needs to convert a failure into shared institutional knowledge; to produce concrete, owned remediation commitments after an incident; when building a safety culture that treats incidents as systemic signals rather than individual failures; communicating transparently with stakeholders about what went wrong and what changes are coming.

### When not to use

Routine project retrospectives that have no specific incident to investigate; celebrating successful launches or milestones; documenting forward-looking design or architectural decisions.

### Pairs well with

`operator`, `pragmatic-architect`, `candid`, `matter-of-fact`, `decision-log`, `problem-solution`

### Often confused with

**adr**: An ADR captures a significant decision and the reasoning behind it, typically at or near the time the decision is made. A postmortem investigates a failure that has already occurred; its output is root-cause analysis and action items, not a decision rationale. The adr looks forward from a decision point; the postmortem looks backward from a failure.

**status-report**: A status report gives a periodic snapshot of project health - what is done, what is at risk, and what comes next. A postmortem is bounded to a specific incident: it investigates what broke, why, and what changes will prevent a recurrence. Status reports are recurring and open-ended; postmortems are closed when their action items ship.
