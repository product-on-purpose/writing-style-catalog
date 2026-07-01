---
id: memo
name: Memo
axis: format
domain: professional
family: messaging
one_liner: A formal internal document that puts a decision or policy on the record for a group, with a TO/FROM/DATE/RE header.
description: |
  A memo is a formal internal document that puts a decision, policy, or position on the record for
  a group within an organization. Its defining hallmark is the structured header - TO, FROM, DATE,
  RE - which signals to the reader that this is not a conversational message but a formal statement
  intended for filing and future reference. A memo is written to be retrieved and re-read weeks or
  months after it was issued, not acted on by a single named recipient before the next meeting.

  The register of a memo is institutional. It addresses the group as a whole, not a specific person
  with a specific task. This makes the memo the right format when a policy needs to be officially
  stated, when a decision needs to sit on the record so that future team members can find it, or
  when an announcement carries enough weight that it should exist as a standalone document outside
  of any email thread or chat channel. A well-written memo does not ask for a reply; it puts
  something in writing so there is no ambiguity about what was decided or communicated.

  Unlike an email - a message optimized for the inbox scan, leading with a specific action request
  to named recipients - a memo is a standalone document that states something for the record and
  addresses the group as a whole. Email can carry action requests, FYIs, broad announcements, and durable records; the memo differs by being a formal standalone internal document with a TO/FROM/DATE/RE header, written to be filed and consulted outside an inbox thread. This distinction matters when choosing
  the format: if the document needs a reply or requires a named person to act, use an email. If the
  document needs to exist as an authoritative record that the organization can point to, use a memo.

  Memos are typically 200 to 600 words. The opening line of the body should state the purpose
  directly below the header - no preamble. Supporting context follows, and a closing statement of
  what the memo establishes or confirms completes the document. Because a memo is read for reference
  rather than for action, its structure should favor clarity and retrievability over urgency cues.
canonical_template: |
  TO: [Recipient group, team, or department]
  FROM: [Author name and title]
  DATE: [Date]
  RE: [Topic - what this memo puts on record]

  [Opening: one to two sentences stating the decision, policy, or position being established]

  [Body: the context, rationale, or supporting detail the reader needs to understand the record]

  [Closing: a statement confirming what this memo establishes or makes official]
typical_voices:
  - executive
  - direct-communicator
typical_tones:
  - matter-of-fact
  - candid
digital_or_print: both
pairs_well_with:
  - executive
  - direct-communicator
  - matter-of-fact
  - candid
  - executive-summary
avoid_with:
  - confessional
  - reverent
  - playful
confusable_with:
  - email
when_to_use:
  - Putting a policy decision on the record for a team or department
  - Announcing an organizational change that needs to exist as a retrievable standalone document
  - Formally communicating a position that future members or stakeholders will need to find
  - Documenting a decision reached in a meeting so it exists outside of anyone's notes
  - Communicating to a group when no reply is expected or required
when_not_to_use:
  - When a reply is expected from a specific person - use email instead
  - When the communication calls for back-and-forth dialogue - use a meeting or a chat channel
  - When the audience is external to the organization - use a letter or a formal announcement
tells:
  - 'A structured header - TO, FROM, DATE, RE - that identifies the document as a formal internal record'
  - 'The RE line names the decision, policy, or position being put on record, not a task or a question'
  - 'The body opens immediately below the header, stating the purpose in the first sentence without preamble'
  - 'Group-addressed: the TO field names a role, team, or department, not a specific individual with a task'
  - 'No call to action or reply requested - the document closes with a statement of record, not an ask'
  - 'A formal institutional register that expects filing and future retrieval, not an inbox response'
  - 'Self-contained: the document assumes no conversational history and no prior thread'
anti_patterns:
  - pattern: 'Writing a memo when the communication needs a specific recipient to act - with a deadline, an approval request, or a named owner'
    why: 'That is better handled as an email: the inbox format can route a named action, owner, approval, or deadline directly to recipients; a memo addresses the group as a whole and puts something on the record, so using it for a targeted ask buries the action request inside a document-style header that signals reference, not response.'
  - pattern: 'Opening the body with background or pleasantries instead of stating the decision or policy in the first sentence'
    why: 'A memo is read for reference: readers return to it to confirm what was decided. If the decision is buried in paragraph three, the memo fails at its one job.'
  - pattern: 'Treating the TO/FROM/DATE/RE header as optional or decorative'
    why: 'The header is what makes a memo a memo; without it, the document is unclassified prose that loses the formal-record signal and cannot be efficiently filed or retrieved.'
failure_modes:
  - mode: 'Bureaucratic inflation - the institutional formality of the memo overdone tips into impenetrable ceremony: every sentence is passive, hedged, and wrapped in official-speak until the actual decision is lost inside the form'
    mitigation: 'State the decision plainly in the first body paragraph; formality lives in the header structure, not in circumlocution throughout the text.'
  - mode: 'Scope creep into treatise - the for-the-record register overdone turns one memo into a comprehensive document that tries to address every related nuance, caveat, and edge case until no one reads it fully'
    mitigation: 'One memo documents one decision or policy; if multiple topics need documenting, write separate memos or restructure the content as a dedicated policy document.'
llm_instruction_phrasing: |
  Write as a memo. Begin with the structured header: TO (recipient group or role), FROM (author
  name and title), DATE, and RE (the topic - what this memo puts on record). Open the body
  immediately below the header with one to two sentences stating the decision, policy, or position
  being established - no preamble. Follow with the context or rationale the reader needs to
  understand the record. Close with a statement of what this memo confirms or establishes. Address
  the group as a whole, not a specific individual with a task. Do not include a call to action or
  request a reply - the memo states something for the record. Maintain a formal institutional
  register; expect the document to be filed and retrieved, not replied to.
tags:
  - internal
  - record
  - policy
  - formal
  - professional
  - announcement
review_status: stable
---

## Memo

A memo is a formal internal document that puts a decision, policy, or position on the record for a group within an organization. Its defining hallmark is the structured header - TO, FROM, DATE, RE - which signals to the reader that this is not a conversational message but a formal statement intended for filing and future reference. A memo is written to be retrieved and re-read weeks or months after it was issued, not acted on by a single named recipient before the next meeting.

The register of a memo is institutional. It addresses the group as a whole, not a specific person with a specific task. This makes the memo the right format when a policy needs to be officially stated, when a decision needs to sit on the record so that future team members can find it, or when an announcement carries enough weight that it should exist as a standalone document outside of any email thread or chat channel. A well-written memo does not ask for a reply; it puts something in writing so there is no ambiguity about what was decided or communicated.

Unlike an email - a message optimized for the inbox scan, leading with a specific action request to named recipients - a memo is a standalone document that states something for the record and addresses the group as a whole. Email can carry action requests, FYIs, broad announcements, and durable records; the memo differs by being a formal standalone internal document with a TO/FROM/DATE/RE header, written to be filed and consulted outside an inbox thread. This distinction matters when choosing the format: if the document needs a reply or requires a named person to act, use an email. If the document needs to exist as an authoritative record that the organization can point to, use a memo.

Memos are typically 200 to 600 words. The opening line of the body should state the purpose directly below the header - no preamble. Supporting context follows, and a closing statement of what the memo establishes or confirms completes the document. Because a memo is read for reference rather than for action, its structure should favor clarity and retrievability over urgency cues.

### Canonical template

```
TO: [Recipient group, team, or department]
FROM: [Author name and title]
DATE: [Date]
RE: [Topic - what this memo puts on record]

[Opening: one to two sentences stating the decision, policy, or position being established]

[Body: the context, rationale, or supporting detail the reader needs to understand the record]

[Closing: a statement confirming what this memo establishes or makes official]
```

### When to use

Putting a policy decision on the record for a team or department, announcing an organizational change that needs to exist as a retrievable standalone document, formally communicating a position that future members or stakeholders will need to find, documenting a decision reached in a meeting so it exists outside of anyone's notes, communicating to a group when no reply is expected or required.

### When not to use

When a reply is expected from a specific person (use email instead), when the communication calls for back-and-forth dialogue (use a meeting or a chat channel), when the audience is external to the organization (use a letter or a formal announcement).

### Pairs well with

`executive`, `direct-communicator`, `matter-of-fact`, `candid`, `executive-summary`

### Often confused with

**email**: Email is a business inbox message whose subject line carries the summary and whose body is optimized for quick scanning, whether the message is an FYI, announcement, durable record, or action request. A memo is designed for the opposite purpose: it addresses the group as a whole, puts a decision or policy on the record for future reference, and does not prompt a reply. When a document needs a named person to act on it before a deadline, use email. When an organization needs an authoritative record to file and retrieve, use a memo.
