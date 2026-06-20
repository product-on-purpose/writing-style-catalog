---
id: meeting-notes
name: Meeting Notes
axis: format
domain: professional
family: progress
one_liner: A structured capture of what was decided and what was assigned - not a transcript. Organized by outcome so someone who missed the meeting can act without asking follow-up questions.
description: |
  Meeting notes are not a transcript and not a summary. A transcript records everything that
  was said; a summary compresses it. Meeting notes record the outcomes: what was decided, what
  was assigned, and what questions remain open. The reader who missed the meeting should be
  able to act from the notes without sending a follow-up message to someone who was there.

  The organizing principle is outcome, not chronology. Organizing by "who said what, in order"
  produces a document that is accurate but nearly useless - it requires the reader to reconstruct
  the conclusions from the raw material. Organizing by decisions, actions, and open items produces
  a document that is immediately actionable. A decision section states what was decided, not how
  long the group debated it. An action section states who owns what by when, not the discussion
  that led to the assignment.

  Meeting notes serve a secondary function as institutional memory. They are the difference between
  a team that relitigates the same discussion every month and one that can point to when a decision
  was made and why. For this reason, notes should be filed where they are findable, dated, and
  include enough context that someone reading six months later can reconstruct the situation without
  needing anyone to explain it.
canonical_template: |
  # Meeting Notes - [Topic or Meeting Name]
  Date: [YYYY-MM-DD]
  Attendees: [Name, Name, Name]

  ## Decisions
  - [Decision stated as a fact, not as a discussion topic]
  - [Decision stated as a fact]

  ## Actions
  - [ ] [Specific task] - owner: [Name] - due: [date or "next meeting"]
  - [ ] [Specific task] - owner: [Name] - due: [date or "next meeting"]

  ## Open Items / Parking Lot
  - [Question or item that needs resolution, with owner if known]

  ## Context (optional)
  [1-3 sentences of background for anyone reading later who lacks context]
typical_voices:
  - operator
  - direct-communicator
typical_tones:
  - matter-of-fact
  - candid
digital_or_print: both
pairs_well_with:
  - operator
  - direct-communicator
  - matter-of-fact
  - candid
avoid_with:
  - columnist
  - pastoral
  - playful
  - warm
confusable_with:
  - adr
  - daily-standup
when_to_use:
  - Capturing outcomes from any synchronous meeting where decisions were made or tasks were assigned
  - Team syncs, planning sessions, retrospectives, stakeholder meetings, or design reviews
  - Any situation where people who were not present need to stay informed or take action
  - Recurring meetings that benefit from a record of evolving decisions over time
when_not_to_use:
  - Casual hallway conversations or informal 1:1 check-ins with no action items
  - Real-time incident response where speed matters more than documentation format
  - Meetings where decisions will be formally documented in an ADR or PRD immediately after
  - Informational-only presentations with no decisions or assignments
llm_instruction_phrasing: |
  Write as meeting notes. Organize by outcome: decisions first, then action items, then open
  questions. Do not organize chronologically or by who said what. State each decision as a
  concluded fact, not as a topic discussed. State each action item with a specific owner and
  due date. The person who missed this meeting should be able to read these notes and act
  without sending a follow-up question. Use plain, direct language - meeting notes are not
  prose, they are a structured record.
tags:
  - meeting
  - async
  - decisions
  - actions
  - internal
  - record
  - structured
review_status: stable
---

## Meeting Notes

Meeting notes are not a transcript and not a summary. A transcript records everything that was said; a summary compresses it. Meeting notes record the outcomes: what was decided, what was assigned, and what questions remain open. The reader who missed the meeting should be able to act from the notes without sending a follow-up message to someone who was there.

The organizing principle is outcome, not chronology. Organizing by "who said what, in order" produces a document that is accurate but nearly useless - it requires the reader to reconstruct the conclusions from the raw material. Organizing by decisions, actions, and open items produces a document that is immediately actionable. A decision section states what was decided, not how long the group debated it. An action section states who owns what by when, not the discussion that led to the assignment.

Meeting notes serve a secondary function as institutional memory. They are the difference between a team that relitigates the same discussion every month and one that can point to when a decision was made and why. For this reason, notes should be filed where they are findable, dated, and include enough context that someone reading six months later can reconstruct the situation without needing anyone to explain it.

### Canonical template

```
# Meeting Notes - [Topic or Meeting Name]
Date: [YYYY-MM-DD]
Attendees: [Name, Name, Name]

## Decisions
- [Decision stated as a fact, not as a discussion topic]
- [Decision stated as a fact]

## Actions
- [ ] [Specific task] - owner: [Name] - due: [date or "next meeting"]
- [ ] [Specific task] - owner: [Name] - due: [date or "next meeting"]

## Open Items / Parking Lot
- [Question or item that needs resolution, with owner if known]

## Context (optional)
[1-3 sentences of background for anyone reading later who lacks context]
```

### When to use

Use meeting notes any time a synchronous meeting produces decisions or assignments - team syncs, planning sessions, retrospectives, stakeholder meetings, design reviews. If people who were not present need to stay informed or take action, notes are required. Recurring meetings especially benefit from a consistent notes format that accumulates as institutional memory over time.

### When not to use

Skip formal notes for casual conversations and informal 1:1 check-ins with no action items. During real-time incident response, speed matters more than format. If a meeting's decisions will be immediately captured in an ADR or PRD, redundant notes add noise. Informational-only presentations with no decisions or assignments do not need a decisions/actions structure.

### Pairs well with

`operator`, `direct-communicator`, `matter-of-fact`, `candid`

### Often confused with

**adr**: An ADR is a permanent, structured record of a specific architectural decision designed to explain the reasoning to future engineers. Meeting notes capture everything decided in a meeting, including non-architectural matters, and are organized for immediate action by attendees and absentees alike.

**daily-standup**: A daily standup is a recurring short-form status communication with a fixed three-part structure. Meeting notes cover a specific meeting's full set of outcomes, including decisions and assigned work, across any topic or time range.
