---
id: incident-report
name: Incident Report
axis: format
domain: public
family: accountability
one_liner: 'A customer-facing account of a service incident: what happened, the impact, and what is being done.'
description: |
  An incident report is the external, customer-facing record of a service disruption. It is written
  for the people who were affected: customers, partners, and the public. Its defining job is not
  forensic - it is relational. The format exists to acknowledge what happened, take organizational
  accountability, and communicate what is being done, all in language accessible to someone who is
  not an engineer and who cares primarily about whether their service is reliable and trustworthy
  again.

  An incident report is not always a post-incident document. It may be issued during an active
  outage as a live status update - with a Status field of Investigating or Identified - and then
  revised or finalized after service is restored with a complete account of the timeline, root
  cause, and remediation. The same structure serves both moments: an initial report early in an
  incident builds trust by showing the team is aware and working; the final report closes the loop
  with customers who deserve to know what actually happened and what has changed.

  An incident report is not a postmortem. A postmortem is an internal, blameless learning document
  written for the engineering team: it asks why the system failed and what processes can improve.
  An incident report is written for customers: it states what they experienced, what caused it at
  an accessible level of detail, and what the organization is committing to. The distinction matters
  because the two audiences need fundamentally different things, and conflating the formats either
  exposes internal detail that customers do not need or strips the learning depth that engineers do.

  Typical length: 300 to 600 words for a final report. An initial report issued while the incident
  is still active may be shorter, with additional sections appended as the situation develops and
  resolves.
canonical_template: |
  # Incident Report: [Incident Name or ID]

  ## Status

  [Investigating | Identified | Monitoring | Resolved] - [date and time, timezone]

  ## Summary

  [One to two sentences: what service was affected, what customers experienced, and when.]

  ## Impact

  - Services affected: [list]
  - Customers affected: [scope or percentage, if known]
  - Duration: [start time] to [end time] ([total duration])

  ## Timeline

  - [time] - [event]
  - [time] - [event]
  - [time] - Incident declared resolved

  ## Root Cause

  [Plain-language explanation of what caused the failure. Accessible to a non-engineer.
  Avoid internal jargon, team names, and speculative detail.]

  ## Resolution

  [What was done to restore service.]

  ## Next Steps

  - [Specific, committed remediation action]
  - [Expected completion or owner, if known]
typical_voices:
  - executive
  - direct-communicator
typical_tones:
  - candid
  - diplomatic
digital_or_print: both
pairs_well_with:
  - executive
  - direct-communicator
  - candid
  - diplomatic
  - problem-solution
  - executive-summary
avoid_with:
  - playful
  - confessional
  - reverent
confusable_with:
  - postmortem
  - public-statement
when_to_use:
  - Communicating a service disruption to affected customers during or after an incident
  - Publishing a final account after service is restored with root cause and remediation
  - Meeting contractual, SLA, or compliance obligations to report downtime or data events
  - Building or restoring customer trust through transparent, accountable communication
  - Responding to public or stakeholder inquiries about what happened and what has changed
when_not_to_use:
  - Internal engineering retrospectives on what went wrong (use a postmortem instead)
  - Routine maintenance notices or scheduled updates with no unplanned service impact
  - Internal team communication during the incident response itself
tells:
  - 'A Status field at the top showing investigation stage: Investigating, Identified, Monitoring, or Resolved'
  - 'An Impact section that names affected services and customer populations in plain language'
  - 'A chronological Timeline of key events leading to and through the incident'
  - 'A Root Cause section written for a non-engineer: category of failure, not internal system detail'
  - 'A Next Steps or Remediation section with specific, committed actions rather than vague assurances'
  - 'Organizational accountability taken without naming individuals or exposing internal team structure'
  - 'Tone that is direct and factual with a single, clear acknowledgment of customer impact'
anti_patterns:
  - pattern: 'Using internal jargon, system names, or engineering architecture detail in the root cause section'
    why: 'Customer-facing reports must be accessible to affected users; unexplained technical language shifts the burden of interpretation onto the reader and signals the writer has not translated the incident for its actual audience.'
  - pattern: 'Omitting the customer impact and leading with the technical timeline'
    why: 'Customers need to understand what they experienced before they can care about the internal sequence of events; opening with a timeline without stating the impact treats the incident as an engineering puzzle rather than a customer harm.'
  - pattern: 'Writing the incident report as though it were a postmortem by including blameless retrospective framing, team names, or internal process detail'
    why: 'The postmortem is the internal learning document; the incident report is for customers. Exposing internal process language in a customer-facing report conflates two distinct audiences with incompatible needs and over-discloses engineering detail.'
  - pattern: 'Publishing a final incident report with vague commitments like we will look into this when the incident is already resolved'
    why: 'By the time a final report is issued, affected customers expect concrete remediation steps; vague language signals the organization has not yet understood its own failure and erodes the trust the format exists to rebuild.'
failure_modes:
  - mode: 'Over-apologizes - the accountability register tips into a string of regret statements that crowd out the factual content customers actually need, turning the report into a performance of remorse rather than a record of the incident'
    mitigation: 'One clear acknowledgment of customer impact is enough; the remaining sections should be factual, specific, and forward-facing - customers need to know what happened and what will change, not how sorry the team is.'
  - mode: 'Over-discloses in the name of transparency - the accessible explanation tips into sharing internal system names, draft hypotheses, team attribution, or speculative root cause detail that creates new confusion or liability without serving the reader'
    mitigation: 'Bound the root cause to the category and mechanism of failure in accessible terms; reserve incomplete or sensitive technical analysis for the internal postmortem.'
llm_instruction_phrasing: |
  Write as a customer-facing Incident Report. Use the canonical structure: Status, Summary, Impact,
  Timeline, Root Cause, Resolution, Next Steps. In Status: name the current investigation stage
  (Investigating, Identified, Monitoring, or Resolved) and the date and time. In Summary: state in
  one to two sentences what service was affected and what customers experienced. In Impact: name
  the affected services and the customer population in plain language. In Timeline: give a
  chronological list of key events. In Root Cause: explain what caused the failure in terms a
  non-engineer can understand - name the category of failure without internal jargon, team names,
  or speculative detail. In Resolution: state what was done to restore service. In Next Steps: list
  specific, committed remediation actions. Take organizational accountability clearly but do not
  name individuals or expose internal team structure. Keep the tone direct and factual. One
  acknowledgment of customer harm is sufficient; the rest of the document should be specific and
  forward-facing. Do not write this as a postmortem - that is an internal document; this is for
  the people who were affected.
tags:
  - service-communication
  - customer-facing
  - accountability
  - incident-management
  - trust
review_status: draft
---

## Incident Report

An incident report is the external, customer-facing record of a service disruption. It is written for the people who were affected: customers, partners, and the public. Its defining job is not forensic - it is relational. The format exists to acknowledge what happened, take organizational accountability, and communicate what is being done, all in language accessible to someone who is not an engineer and who cares primarily about whether their service is reliable and trustworthy again.

An incident report is not always a post-incident document. It may be issued during an active outage as a live status update - with a Status field of Investigating or Identified - and then revised or finalized after service is restored with a complete account of the timeline, root cause, and remediation. The same structure serves both moments: an initial report early in an incident builds trust by showing the team is aware and working; the final report closes the loop with customers who deserve to know what actually happened and what has changed.

An incident report is not a postmortem. A postmortem is an internal, blameless learning document written for the engineering team: it asks why the system failed and what processes can improve. An incident report is written for customers: it states what they experienced, what caused it at an accessible level of detail, and what the organization is committing to. The distinction matters because the two audiences need fundamentally different things, and conflating the formats either exposes internal detail that customers do not need or strips the learning depth that engineers do.

Typical length: 300 to 600 words for a final report. An initial report issued while the incident is still active may be shorter, with additional sections appended as the situation develops and resolves.

### Canonical template

```
# Incident Report: [Incident Name or ID]

## Status

[Investigating | Identified | Monitoring | Resolved] - [date and time, timezone]

## Summary

[One to two sentences: what service was affected, what customers experienced, and when.]

## Impact

- Services affected: [list]
- Customers affected: [scope or percentage, if known]
- Duration: [start time] to [end time] ([total duration])

## Timeline

- [time] - [event]
- [time] - [event]
- [time] - Incident declared resolved

## Root Cause

[Plain-language explanation of what caused the failure. Accessible to a non-engineer.
Avoid internal jargon, team names, and speculative detail.]

## Resolution

[What was done to restore service.]

## Next Steps

- [Specific, committed remediation action]
- [Expected completion or owner, if known]
```

### When to use

Communicating a service disruption to affected customers during or after an incident, publishing a final account after service is restored with root cause and remediation, meeting contractual or compliance obligations to report downtime or data events, building or restoring customer trust through transparent accountable communication, responding to public or stakeholder inquiries about what happened and what has changed.

### When not to use

Internal engineering retrospectives on what went wrong, routine maintenance notices or scheduled updates with no unplanned service impact, internal team communication during the incident response itself.

### Pairs well with

`executive`, `direct-communicator`, `candid`, `diplomatic`, `problem-solution`, `executive-summary`

### Often confused with

**postmortem**: A postmortem is an internal, blameless engineering retrospective - it asks why the system failed and how to improve team processes, and is written for the engineering team. An incident report is written for customers and the public: it takes organizational accountability, explains impact in accessible terms, and commits to remediation without exposing the forensic depth that belongs in the postmortem.

**public-statement**: An incident-report covers a technical service disruption with a reconstructable timeline and root cause (Status, Timeline, Root Cause, Resolution) and is addressed to affected users who need to know what failed and what changed. A public-statement covers a controversy or decision under scrutiny that has no incident timeline; it is carried as institutional prose with a named signatory and addresses a watching public rather than a population of technically affected customers.
