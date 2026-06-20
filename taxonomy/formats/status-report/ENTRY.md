---
id: status-report
name: Status Report
axis: format
domain: professional
family: progress
one_liner: A periodic async update covering progress since the last report, what is next, and what is blocked - the working unit of distributed-team visibility.
description: |
  A status report is a periodic written update, typically weekly or biweekly, that answers three
  questions: what got done since the last report, what is next, and what is blocked. It is written
  async, read async, and exists to give a distributed team or an external stakeholder enough
  visibility to stay aligned without a meeting.

  The format is distinguished from a daily standup by scope and detail: a standup covers yesterday
  and today in a sentence or two; a status report covers a longer window (a week or more) with
  enough detail to be useful to someone who is not in the day-to-day. It is distinguished from
  meeting notes by the absence of a meeting: status reports are written, not transcribed.

  The three-question structure - done, next, blocked - is the load-bearing convention. Variants
  exist (RAG status, traffic-light, GAS - goals/accomplishments/status), but the underlying shape
  is consistent: backward-looking summary, forward-looking commitment, and explicit surfacing of
  what is stuck. The blocked section is the most important section. A status report that does not
  name what is blocked is performing alignment rather than producing it.

  Typical length: 200 to 800 words for a weekly report; longer for monthly reports or
  multi-workstream consulting engagements.
canonical_template: |
  # Status Report - [Project/Workstream Name]
  **Period:** [Date range]
  **Author:** [Name]
  **Status:** [Green | Yellow | Red]

  ## Headline
  [One or two sentences summarizing the state of the work. The reader should be able to stop here.]

  ## Done this period
  - [Outcome, not activity - what changed for the user or the team]
  - [Outcome, with link to artifact where useful]

  ## Up next
  - [Specific deliverable with a target date]
  - [Specific deliverable with a target date]

  ## Blocked / risks
  - [What is stuck, what is needed to unblock, who can help]
  - [Risk, with severity and current mitigation]

  ## Asks
  - [Specific request of the reader, if any]
typical_voices:
  - operator
  - direct-communicator
  - executive
typical_tones:
  - matter-of-fact
  - candid
digital_or_print: digital
pairs_well_with:
  - direct-communicator
  - operator
  - matter-of-fact
  - executive
avoid_with:
  - storyteller
  - pastoral
confusable_with:
  - meeting-notes
  - daily-standup
when_to_use:
  - Weekly or biweekly team updates in a distributed organization
  - Consulting engagement status updates to a client
  - Workstream lead reporting up to a program manager or executive
  - Monthly portfolio reviews where multiple workstreams are summarized in one place
when_not_to_use:
  - Daily standup updates (use daily-standup - smaller scope, less detail)
  - Documentation of a discussion that happened in a meeting (use meeting-notes)
  - One-off announcements (use email or slack-message)
  - Formal project reviews requiring deck format
tells:
  - 'A header with project, period, author, and an overall status (Green/Yellow/Red)'
  - 'A one-or-two-sentence headline the reader can stop at'
  - 'The three-question structure: Done this period, Up next, Blocked'
  - 'Done lines name outcomes, not activity - what changed, not what was worked on'
  - 'Up next items carry specific deliverables with target dates'
  - 'A Blocked section that names what is stuck and what would unblock it, even if "nothing"'
anti_patterns:
  - pattern: 'Covering only yesterday and today in a sentence or two'
    why: 'That is the scope of the confusable daily-standup; a status report spans a week or more with enough detail for someone outside the day-to-day.'
  - pattern: 'Reconstructing a meeting''s discussion organized by topic'
    why: 'That is the confusable meeting-notes; a status report is written async with no meeting, organized by done/next/blocked and reflecting the state of the work itself.'
  - pattern: 'Omitting the Blocked section when nothing happens to be stuck'
    why: 'The Blocked section is the most important; silence reads as either nothing is wrong or nothing was surfaced, so it must say so explicitly.'
failure_modes:
  - mode: 'Over-aggregates parallel workstreams into one rolled-up summary until no owner, risk, or ask is attributable to anyone who could act on it'
    mitigation: 'Aggregate for the outside reader without dissolving accountability; a workstream that carries a risk or an ask needs a named owner, or the report informs without letting anyone respond.'
  - mode: 'Over-reports the period - the update swells with exhaustive detail on every workstream until the headline and the blockers drown in the volume'
    mitigation: 'Give enough detail to stay aligned without a meeting, no more; lead with the stop-here headline and keep the body to outcomes, dates, and what is stuck.'
llm_instruction_phrasing: |
  Write a status report covering a defined period (typically a week). Open with a single-sentence
  headline that lets the reader stop reading if they only have ten seconds. Use the three-section
  structure: Done this period, Up next, Blocked. Write outcomes, not activity - "shipped X to
  users" not "worked on X". Be specific about dates and owners. The Blocked section is the most
  important: if nothing is blocked, say so explicitly. End with an Asks section if there is
  something specific you need from the reader. Use matter-of-fact tone and resist the urge to
  perform progress; the reader needs the truth, not a sales pitch.
tags:
  - async
  - distributed-team
  - reporting
  - stakeholder-communication
  - weekly
  - digital
review_status: stable
---

## Status Report

A status report is a periodic written update, typically weekly or biweekly, that answers three questions: what got done, what is next, and what is blocked. It is written async, read async, and exists to give a distributed team or external stakeholder enough visibility to stay aligned without a meeting. The Blocked section is the most important; a status report that does not name what is stuck is performing alignment rather than producing it.

### Canonical template

```
# Status Report - [Project/Workstream Name]
**Period:** [Date range]
**Author:** [Name]
**Status:** [Green | Yellow | Red]

## Headline
[One or two sentences summarizing the state of the work.]

## Done this period
- [Outcome, not activity]
- [Outcome, with link to artifact where useful]

## Up next
- [Specific deliverable with a target date]

## Blocked / risks
- [What is stuck, what is needed to unblock, who can help]

## Asks
- [Specific request of the reader, if any]
```

### When to use

Use a status report for weekly or biweekly team updates in distributed organizations, consulting engagement updates to a client, or workstream-lead reporting up to a program manager. It is the working unit of async visibility on long-running work.

### When not to use

Do not use this format for a daily standup (smaller scope, less detail - use `daily-standup`). Do not use it to document a discussion that happened in a meeting (use `meeting-notes`). Do not use it for one-off announcements.

### Pairs well with

`direct-communicator`, `operator`, `matter-of-fact`, `executive`

### Often confused with

**meeting-notes**: Meeting notes capture a discussion that happened synchronously; they are organized by topic and reflect what was said. A status report is written async, with no meeting required; it is organized by done/next/blocked and reflects the state of the work itself.

**daily-standup**: A daily standup covers yesterday and today in a sentence or two and is read in seconds. A status report covers a longer window (a week or more) with enough detail to be useful to someone outside the day-to-day. Same shape (done/next/blocked), different scope.
