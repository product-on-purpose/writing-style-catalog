---
id: email
name: Email
axis: format
one_liner: A business message designed for the inbox scan - subject line doubles as summary, body leads with action, and the reader never needs to re-read to know what is being asked.
description: |
  Business email is not a letter. Letters open with pleasantries and build toward the point.
  Email readers scan - they do not read start to finish, and they especially do not read the
  part before the point. An effective business email leads with the subject line as a compressed
  summary and opens the body with the purpose and required action, not with a greeting that delays
  both. The test is simple: can the reader act on this email without re-reading it?

  The subject line carries more weight than most writers give it. It is the only text many
  recipients will read before deciding whether to open the message. A strong subject line is
  specific enough to act on: "Review and approve Q2 budget draft - needed by Friday" outperforms
  "Q2 Budget" in every measurable way. The subject line is the summary; the body is the detail.

  Email is durable. Unlike a Slack message, email creates a record and travels beyond the
  immediate team. This means the action requested must be explicit (who does what by when),
  the context must be self-contained (assume no conversational history), and the tone must
  be appropriate to the relationship, not just the channel. An email that requires a follow-up
  question to understand has failed at its job.
canonical_template: |
  Subject: [Specific topic - action needed, decision required, or FYI - date or deadline if relevant]

  [One sentence: what this email is about and what action, if any, is needed from the reader]

  [2-4 sentences of context or supporting detail - only what the reader needs to act]

  [Explicit next step: what, who, by when]
  [Optional: secondary next step or offer to discuss]
typical_voices:
  - direct-communicator
  - executive
  - operator
typical_tones:
  - matter-of-fact
  - candid
  - warm
digital_or_print: digital
pairs_well_with:
  - direct-communicator
  - executive
  - candid
  - matter-of-fact
  - warm
avoid_with:
  - pastoral
  - reverent
  - devotional-reflection
confusable_with:
  - slack-message
when_to_use:
  - Communicating with external parties or stakeholders outside the team
  - Requests that require a durable record or audit trail
  - Action items with a specific owner, deadline, or approval needed
  - Announcements to a broad or mixed audience
  - Formal communication where tone and structure reflect organizational relationships
when_not_to_use:
  - Quick back-and-forth that belongs in a chat channel
  - Real-time coordination during incidents or live situations
  - Topics so sensitive or complex they require a conversation first
  - Broadcasting to a large audience where a proper announcement format is warranted
  - Situations where the message will be read in a high-noise async thread rather than an inbox
llm_instruction_phrasing: |
  Write as a business email. The subject line should be specific enough to act on - it doubles
  as the summary of the message. Open the body with the purpose and required action immediately,
  not with pleasantries. Include only the context the reader needs to take the next step. State
  the next step explicitly: who does what, by when. The reader should be able to act on this
  email without re-reading it. Match tone to the relationship - direct but not cold for colleagues,
  slightly more formal for external or senior recipients.
tags:
  - email
  - business
  - async
  - external-comms
  - record
  - digital
  - action-oriented
review_status: stable
---

## Email

Business email is not a letter. Letters open with pleasantries and build toward the point. Email readers scan - they do not read start to finish, and they especially do not read the part before the point. An effective business email leads with the subject line as a compressed summary and opens the body with the purpose and required action, not with a greeting that delays both. The test is simple: can the reader act on this email without re-reading it?

The subject line carries more weight than most writers give it. It is the only text many recipients will read before deciding whether to open the message. A strong subject line is specific enough to act on: "Review and approve Q2 budget draft - needed by Friday" outperforms "Q2 Budget" in every measurable way. The subject line is the summary; the body is the detail.

Email is durable. Unlike a Slack message, email creates a record and travels beyond the immediate team. This means the action requested must be explicit (who does what by when), the context must be self-contained (assume no conversational history), and the tone must be appropriate to the relationship, not just the channel. An email that requires a follow-up question to understand has failed at its job.

### Canonical template

```
Subject: [Specific topic - action needed, decision required, or FYI - date or deadline if relevant]

[One sentence: what this email is about and what action, if any, is needed from the reader]

[2-4 sentences of context or supporting detail - only what the reader needs to act]

[Explicit next step: what, who, by when]
[Optional: secondary next step or offer to discuss]
```

### When to use

Email is the right format when you need a durable record, when you are reaching external parties or stakeholders outside the immediate team, or when a request has a specific owner, deadline, or approval gate. It is also appropriate for formal announcements to a broad or mixed audience where structure and tone reflect organizational relationships.

### When not to use

Email is the wrong format for quick back-and-forth that belongs in a chat channel, for real-time coordination during incidents, or for topics so sensitive they require a conversation before anything is put in writing. If the message will be read inside a high-noise thread rather than a personal inbox, the format advantage is lost.

### Pairs well with

`direct-communicator`, `executive`, `candid`, `matter-of-fact`, `warm`

### Often confused with

**slack-message**: Slack messages are designed for team channels, are ephemeral, and tolerate a conversational opening. Email creates a record, travels outside the team, and must be self-contained - the subject line and body structure carry obligations that a Slack message does not.
