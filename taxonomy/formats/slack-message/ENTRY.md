---
id: slack-message
name: Slack Message
axis: format
domain: professional
family: messaging
one_liner: A short, async-first message designed for team channels - direct, scannable, and respectful of the reader's attention in a high-volume feed.
description: |
  A Slack message in a professional context competes with dozens of others in the same channel.
  The reader skims. The effective Slack message acknowledges this and works with it rather than
  against it: the most important information appears in the first line, the message is short enough
  to read without scrolling, and any required action is explicit.

  The Slack message is the format most vulnerable to voice/tone mismatch. A pastoral voice in a
  standup channel reads as incongruous; a cold, corporate tone in a team's social channel creates
  distance. The format itself is neutral - the voice and tone carry almost all the social weight.

  Slack messages exist on a spectrum from a 3-word reply to a multi-paragraph status update. The
  format constraint that holds across the full range is: be scannable, be direct, be appropriately
  brief. The "appropriately" qualifier matters: a complex incident update should be as long as it
  needs to be, but it should use bullet points and headers to make it scannable at the required
  length.

  Typical length: 1 line to 200 words.
canonical_template: |
  [One-line summary - the message should be understandable from this alone]

  [Optional: 2-4 bullet points for supporting detail]

  [Optional: @mention for required action]
  [Optional: thread invitation for discussion]
typical_voices:
  - operator
  - friendly-mentor
typical_tones:
  - matter-of-fact
  - warm
  - candid
digital_or_print: digital
pairs_well_with:
  - operator
  - friendly-mentor
  - matter-of-fact
  - candid
  - warm
avoid_with:
  - pastoral
  - reverent
  - columnist
confusable_with:
  - email
when_to_use:
  - Team status updates
  - Quick questions
  - Sharing a link with context
  - Incident notifications
  - Async decisions
when_not_to_use:
  - Formal communication requiring a paper trail
  - Communication with external parties
  - Emotionally complex topics that deserve more space
  - Announcements requiring broad visibility
tells:
  - 'The most important information lands in the first line'
  - 'Short enough to read without scrolling'
  - 'Any required action is explicit, often with an @mention and a deadline'
  - 'Scannable - bullet points and headers used when the message must run longer'
  - 'Voice and tone matched to the channel, since the format itself is neutral'
  - 'Spans a wide range, from a 3-word reply to a multi-paragraph update'
anti_patterns:
  - pattern: 'Writing it as a self-contained durable record with a formal subject and full context'
    why: 'That is the confusable email; a Slack message is ephemeral team-channel communication that can lean on the channel and the conversation, where email must travel and stand alone.'
  - pattern: 'Burying the point under a conversational warm-up before getting to it'
    why: 'The reader skims a high-volume feed; if the first line does not carry the message, it is missed in the scroll.'
  - pattern: 'Closing a request with "let me know what you think" instead of a specific ask'
    why: 'A vague ask in a busy channel goes unanswered; the format works only when the required action names who does what by when.'
failure_modes:
  - mode: 'Compresses into cryptic shorthand - brevity is pushed until the message is acronyms and clipped fragments that the reader cannot decode without asking'
    mitigation: 'Be brief enough to scan, not so terse it needs a follow-up; if a teammate would have to ask "what do you mean," add the few words that make it clear.'
  - mode: 'Over-trims a genuinely complex update - an incident or decision is forced into one cramped line when it needed scannable structure'
    mitigation: 'Appropriately brief means as long as it needs to be; let a complex message run, but make it scannable with bullets and headers rather than crushing it.'
llm_instruction_phrasing: |
  Write as a Slack message for a professional team channel. Lead with the most important
  information in the first line - the message should be understandable from the first line alone.
  Keep it short enough to read without scrolling. If the message is complex, use bullet points to
  make it scannable. Make any required action explicit and specific: "@alex can you confirm by
  EOD?" not "let me know what you think." Match the channel's tone - standup channels are more
  formal, social channels are warmer. Respect the reader's attention in a high-volume feed.
tags:
  - async
  - team-communication
  - short-form
  - slack
  - internal
  - digital
review_status: stable
---

## Slack Message

A Slack message in a professional context competes with dozens of others in the same channel. The reader skims. The effective Slack message acknowledges this and works with it rather than against it: the most important information appears in the first line, the message is short enough to read without scrolling, and any required action is explicit.

### Canonical template

```
[One-line summary - the message should be understandable from this alone]

[Optional: 2-4 bullet points for supporting detail]

[Optional: @mention for required action]
[Optional: thread invitation for discussion]
```

### When to use

Team status updates, quick questions, sharing a link with context, incident notifications, async decisions.

### When not to use

Formal communication requiring a paper trail, communication with external parties, emotionally complex topics that deserve more space.

### Pairs well with

`operator`, `friendly-mentor`, `matter-of-fact`, `candid`, `warm`

### Often confused with

**prd**: A PRD is a structured multi-section document defining product requirements. A Slack message is a short async communication in a team feed - the two should not be confused in practice, but "format" as a category occasionally causes library navigation confusion.

**adr**: An ADR is a permanent record of an architectural decision. A Slack message is ephemeral async communication - it may contain a decision, but it is not a record of one.
