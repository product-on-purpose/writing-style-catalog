---
id: support-reply
name: Support Reply
axis: format
domain: professional
family: response
one_liner: A written response to one customer's specific question or problem that resolves it and leaves them able to act.
description: |
  A support reply is a written response to one customer's specific question or problem. Its job
  is not just to acknowledge the issue but to close it: the customer should finish reading and
  know exactly what to do next, or know that the problem is already solved. The reply earns its
  place by balancing genuine empathy with efficiency - brief acknowledgment of the customer's
  experience, then an unambiguous resolution.

  The anatomy of an effective support reply is consistent: open by naming the specific issue the
  customer raised (not a generic "thanks for reaching out"), give the resolution or next step in
  the body, and close by confirming the path forward and inviting follow-up. This sequence exists
  because a customer who contacted support is in a state of friction; reducing that friction is
  the primary goal, and every sentence that delays the resolution adds to it.

  Unlike an FAQ, which anticipates many people's questions in advance and answers each once for
  everyone, a support reply is reactive and individual. It answers this person's actual problem,
  right now, in the context of their specific situation. That reactive character is also its
  constraint: a support reply that reads like a generic form letter - naming no specific symptom,
  no specific step - has used the format's shape without doing the format's work.

  Typical length: 100-250 words. Long enough to be complete, short enough to be read in full.
canonical_template: |
  [Greeting and acknowledgment]
  Hi [Customer name],

  [Sentence that names their specific issue.]

  [Resolution or next step - state it directly; use numbered steps if multiple actions are needed.]

  [What to expect next, or confirmation that the issue is resolved.]

  [Close and follow-up invitation.]
  Let me know if this does not resolve the issue or if you have any questions.

  [Agent name]
  [Team / company]
typical_voices:
  - caregiver
  - technical-writer
typical_tones:
  - empathetic
  - diplomatic
digital_or_print: digital
pairs_well_with:
  - caregiver
  - technical-writer
  - empathetic
  - diplomatic
  - problem-solution
avoid_with:
  - confessional
  - reverent
  - playful
confusable_with:
  - faq
when_to_use:
  - A customer has contacted support with a specific question, error, or complaint
  - The issue requires a personalized acknowledgment and a resolution or next step tailored to that customer's situation
  - A customer needs step-by-step direction to get unblocked and proceed on their own
  - Following up on a previous interaction to confirm the issue is resolved or to deliver a promised answer
  - Responding to a complaint where both acknowledgment and a concrete action are required
when_not_to_use:
  - The same question recurs across many customers and a single prepared answer would serve them all - publish a FAQ instead
  - The content is a reference specification, procedure, or policy that belongs in documentation, not a personalized reply
  - The issue requires an escalation, investigation, or action that cannot be completed in writing and needs a phone call or ticket hand-off
tells:
  - 'Opens by naming the specific issue the customer raised, not a generic acknowledgment'
  - 'Uses the customer''s name and refers to their particular situation, not a hypothetical scenario'
  - 'The resolution or next step appears early in the body, not buried after extended explanation'
  - 'Empathy is concentrated at the opening and is brief - one or two sentences, not recurring throughout'
  - 'Closes with a clear invitation for follow-up if the issue persists or a new question arises'
  - 'Passive voice and hedge language are absent - the reply says what will happen, not what might'
  - 'Length is compact, typically 100-250 words - complete but not exhaustive'
anti_patterns:
  - pattern: 'Burying the resolution after several paragraphs of empathy and background'
    why: 'The customer opened the ticket to get an answer; every sentence before the resolution increases friction. Acknowledge briefly, then resolve.'
  - pattern: 'Writing a generalized answer that covers all possible cases rather than the customer''s specific one'
    why: 'A reusable recurring-question answer belongs in a FAQ - it anticipates a predictable question many readers ask and gives one brief, self-contained answer once for everyone. A support reply answers this customer''s actual problem in their specific context. Using the support-reply format to deliver a generic answer wastes the format''s defining strength.'
  - pattern: 'Ending without a clear next step or confirmation that the issue is closed'
    why: 'A support reply that does not leave the customer able to act has not done its job. Every reply must either deliver a resolution or tell the customer exactly what happens next.'
  - pattern: 'Opening with scripted empathy that does not name the actual issue'
    why: 'A line like "I''m sorry you''re having trouble!" without any reference to the specific problem signals that the agent has not read the message, which is the opposite of the personalization this format depends on.'
failure_modes:
  - mode: 'Over-empathizes - the reply tips into extended emotional validation, with multiple passages acknowledging the customer''s frustration, so the customer finishes reading without knowing what to do'
    mitigation: 'Empathy earns its place in the opening sentence or two; after that, move to resolution. A customer who reached out for help needs the resolution, not a sustained reflection of their feelings.'
  - mode: 'Over-specifies - the reply tips into a comprehensive troubleshooting document, covering every possible cause and scenario, so the resolution is buried and the customer cannot identify their single next step'
    mitigation: 'A support reply gives one clear next step for this customer''s situation; if broader depth is needed, link to documentation rather than embedding it in the reply.'
  - mode: 'Over-scopes - the reply tips into addressing the customer''s stated problem plus every adjacent question they might have, until the original answer is buried in unsolicited guidance'
    mitigation: 'Answer the question asked first; then, if related topics are genuinely useful, offer them briefly or as links. Unsolicited breadth in a one-person reply is noise, not service.'
llm_instruction_phrasing: |
  Write as a support reply. This is a direct, personal written response to one specific
  customer's question or problem - not a general explanation, not a policy statement. Open by
  naming the specific issue they raised. Give the resolution or the exact next step early in
  the body, before any extended explanation. Keep empathy brief and concentrated at the opening
  - one or two sentences - then move to the resolution. Use the customer's name and refer to
  their specific situation. Close by confirming what will happen next and inviting follow-up
  if needed. Avoid hedge language and passive constructions - say what will happen, not what
  might. Target 100-250 words: complete enough to resolve the issue, short enough to be read
  in full.
tags:
  - support
  - customer-service
  - professional
  - response
  - one-to-one
review_status: stable
---

## Support Reply

A support reply is a written response to one customer's specific question or problem. Its job is not just to acknowledge the issue but to close it: the customer should finish reading and know exactly what to do next, or know that the problem is already solved. The reply earns its place by balancing genuine empathy with efficiency - brief acknowledgment of the customer's experience, then an unambiguous resolution.

The anatomy of an effective support reply is consistent: open by naming the specific issue the customer raised (not a generic "thanks for reaching out"), give the resolution or next step in the body, and close by confirming the path forward and inviting follow-up. This sequence exists because a customer who contacted support is in a state of friction; reducing that friction is the primary goal, and every sentence that delays the resolution adds to it.

Unlike an FAQ, which anticipates many people's questions in advance and answers each once for everyone, a support reply is reactive and individual. It answers this person's actual problem, right now, in the context of their specific situation. That reactive character is also its constraint: a support reply that reads like a generic form letter - naming no specific symptom, no specific step - has used the format's shape without doing the format's work.

### Canonical template

```
[Greeting and acknowledgment]
Hi [Customer name],

[Sentence that names their specific issue.]

[Resolution or next step - state it directly; use numbered steps if multiple actions are needed.]

[What to expect next, or confirmation that the issue is resolved.]

[Close and follow-up invitation.]
Let me know if this does not resolve the issue or if you have any questions.

[Agent name]
[Team / company]
```

### When to use

- A customer has contacted support with a specific question, error, or complaint
- The issue requires a personalized acknowledgment and a resolution or next step tailored to that customer's situation
- A customer needs step-by-step direction to get unblocked and proceed on their own
- Following up on a previous interaction to confirm the issue is resolved or to deliver a promised answer
- Responding to a complaint where both acknowledgment and a concrete action are required

### When not to use

- The same question recurs across many customers and a single prepared answer would serve them all - publish a FAQ instead
- The content is a reference specification, procedure, or policy that belongs in documentation, not a personalized reply
- The issue requires an escalation, investigation, or action that cannot be completed in writing and needs a phone call or ticket hand-off

### Pairs well with

`caregiver`, `technical-writer`, `empathetic`, `diplomatic`, `problem-solution`

### Often confused with

**faq**: A FAQ is a list of anticipated questions with direct, self-contained answers, ordered by how often they are asked. It is proactive - the author anticipates what many readers will ask and answers each question once, for everyone. A support reply is reactive and individual: it is written to one customer about their specific situation, right now. If the same question is appearing repeatedly across many customers, that is a signal to write a FAQ; if the question belongs to this person and this moment, the right format is a support reply.
