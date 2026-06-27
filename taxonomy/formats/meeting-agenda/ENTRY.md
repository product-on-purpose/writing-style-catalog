---
id: meeting-agenda
name: Meeting Agenda
axis: format
domain: professional
family: progress
one_liner: A short pre-meeting document listing what will be discussed, in what order, with time and intended outcomes.
description: |
  A meeting agenda is a short document circulated before a meeting that lists what will be discussed,
  in what order, with how much time each item needs and what outcome it is meant to produce. Its job
  is to make the meeting purposeful and let participants prepare. A meeting without an agenda defaults
  to whoever talks loudest or remembers to raise a topic; a meeting with one has a reason to exist.

  Writing the agenda is itself a forcing function. Naming the intended outcome for each item -
  discussion, decision, or update - reveals whether the item belongs on this call at all. For
  participants, receiving the agenda before the meeting lets them prepare questions, review materials,
  and show up ready rather than reactive.

  Unlike meeting notes, which are written during or after a meeting to record what was decided and
  who owns what, an agenda is forward-looking. It plans the conversation that has not happened yet,
  where notes capture the conversation that already did. An agenda is not a wishlist of topics - it
  is a plan for a bounded piece of time with specific things that need to happen.

  Typical length: 100-300 words.
canonical_template: |
  # [Meeting Title] - [Date]
  Time: [start] - [end] | [Duration]
  Location / Link: [room or video URL]
  Attendees: [Name, Name, Name]

  ## Agenda

  1. [Item name] ([time box, e.g., 5 min]) - [outcome: discuss / decide / update]
     [One sentence of context if needed]

  2. [Item name] ([time box]) - [outcome: discuss / decide / update]
     [One sentence of context if needed]

  3. [Item name] ([time box]) - [outcome: discuss / decide / update]

  ## Pre-reading
  - [Link or document title]

  ## Questions or additions
  Add items before [date or time] to [contact or shared doc].
typical_voices:
  - operator
  - executive
typical_tones:
  - matter-of-fact
  - instructional
digital_or_print: digital
pairs_well_with:
  - operator
  - executive
  - matter-of-fact
  - instructional
  - executive-summary
avoid_with:
  - confessional
  - reverent
  - playful
confusable_with:
  - meeting-notes
when_to_use:
  - Any scheduled meeting where participants need to prepare or align on topics in advance
  - Recurring team meetings where agenda discipline prevents scope creep over time
  - Stakeholder or cross-functional calls where attendees arrive from different contexts
  - Meetings involving a decision or significant discussion where participants need to know their role
  - External calls with clients or partners where setting shared expectations in advance builds credibility
when_not_to_use:
  - Spontaneous conversations or hallway check-ins that have no prior scheduling
  - Emergency or incident response calls where the situation drives the conversation and speed matters more than structure
  - Casual 1:1 check-ins with a trusted peer where a rigid topic list would feel bureaucratic and inhibit candid conversation
tells:
  - 'A header with date, time, location or link, and attendees'
  - 'Each item carries a time box naming how many minutes it will take'
  - 'Each item states an outcome type: discuss, decide, or update'
  - 'Items are listed in the order they will occur in the meeting'
  - 'Time boxes across all items total at or under the meeting duration'
  - 'Circulated before the meeting, not during or after it'
  - 'A one-sentence context note appears under items participants need to prepare for'
anti_patterns:
  - pattern: 'Listing topics with no stated outcome type for each item'
    why: 'Without knowing whether an item is a discussion, a decision, or an update, participants cannot prepare and the facilitator has no shared basis for calling an item done.'
  - pattern: 'Adding a Decisions or Actions section inside the agenda document to capture what happens during the meeting'
    why: 'That converts the agenda into meeting notes, which are organized by outcome from a conversation that already occurred - not a plan for what is still to come. The two documents should stay separate.'
  - pattern: 'Issuing the agenda with so many items that the time boxes total more than the meeting window allows'
    why: 'An agenda that cannot fit in the available time is a topic dump, not a plan. Cut to what can be covered, or split across multiple meetings.'
  - pattern: 'Distributing the agenda during the meeting or after it ends'
    why: 'An agenda serves two jobs - enabling preparation and establishing shared purpose - and both require advance circulation. A same-moment or post-meeting agenda cannot do either.'
failure_modes:
  - mode: 'Over-scripted - each item arrives padded with sub-bullets, talking points, speaker assignments, and transition cues, turning a lightweight plan into a stage-managed script that leaves no room for actual conversation'
    mitigation: 'Keep each item to a label, a time box, and an outcome type. If an item needs preparation material, link to a separate pre-read document rather than embedding it in the agenda.'
  - mode: 'Over-compresses - the agenda reduces every item to a label, time box, and outcome type so aggressively that participants know the order of discussion but not what they need to prepare or decide'
    mitigation: 'Keep the agenda lightweight, but add one sentence of preparation context under any item where participants need background to participate usefully.'
llm_instruction_phrasing: |
  Write as a meeting agenda. List what will be discussed in the order it will occur, with a time box
  and an intended outcome type (discuss, decide, or update) for each item. Include a brief header
  with date, time, location or link, and attendees. Keep each item label short; if an item requires
  preparation context, add one sentence under it - not a paragraph. Total the time boxes to confirm
  they fit within the meeting window before finalizing. This document is meant to be circulated
  before the meeting - an agenda issued during or after the meeting cannot serve its purpose.
tags:
  - meeting
  - planning
  - facilitation
  - professional
  - structured
  - pre-meeting
review_status: stable
---

## Meeting Agenda

A meeting agenda is a short document circulated before a meeting that lists what will be discussed,
in what order, with how much time each item needs and what outcome it is meant to produce. Its job
is to make the meeting purposeful and let participants prepare. A meeting without an agenda defaults
to whoever talks loudest or remembers to raise a topic; a meeting with one has a reason to exist.

Writing the agenda is itself a forcing function. Naming the intended outcome for each item -
discussion, decision, or update - reveals whether the item belongs on this call at all. For
participants, receiving the agenda before the meeting lets them prepare questions, review materials,
and show up ready rather than reactive.

Unlike meeting notes, which are written during or after a meeting to record what was decided and
who owns what, an agenda is forward-looking. It plans the conversation that has not happened yet,
where notes capture the conversation that already did. An agenda is not a wishlist of topics - it
is a plan for a bounded piece of time with specific things that need to happen.

### Canonical template

```
# [Meeting Title] - [Date]
Time: [start] - [end] | [Duration]
Location / Link: [room or video URL]
Attendees: [Name, Name, Name]

## Agenda

1. [Item name] ([time box, e.g., 5 min]) - [outcome: discuss / decide / update]
   [One sentence of context if needed]

2. [Item name] ([time box]) - [outcome: discuss / decide / update]
   [One sentence of context if needed]

3. [Item name] ([time box]) - [outcome: discuss / decide / update]

## Pre-reading
- [Link or document title]

## Questions or additions
Add items before [date or time] to [contact or shared doc].
```

### When to use

Send a meeting agenda for any scheduled call where participants need to prepare or align on topics
in advance. Recurring meetings benefit from agenda discipline - without it, scope creep accumulates
session over session. Stakeholder or cross-functional calls where attendees arrive from different
contexts need a shared map of what is happening and why. Any meeting that involves a decision or
significant discussion should name those items explicitly so participants know what role they are
playing when they arrive.

### When not to use

Skip an agenda for spontaneous conversations and hallway check-ins with no prior scheduling - the
structure implies formality the interaction does not need. Emergency and incident response calls are
driven by the situation, not a pre-set order; adding agenda ceremony slows the response. For casual
1:1 check-ins with a trusted peer, a rigid topic list can feel bureaucratic and inhibit the candid
conversation both parties need.

### Pairs well with

`operator`, `executive`, `matter-of-fact`, `instructional`, `executive-summary`

### Often confused with

**meeting-notes**: Meeting notes are a structured capture of what was decided and who was assigned
what, organized by outcome (decisions, actions, open items) rather than chronology. They are written
during or after a meeting to record what happened. A meeting agenda is written before the meeting to
plan what will happen - the two documents cover the same event from opposite directions in time.
