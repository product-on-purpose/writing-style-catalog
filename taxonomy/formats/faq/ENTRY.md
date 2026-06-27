---
id: faq
name: FAQ
axis: format
domain: professional
family: instruction
one_liner: A list of anticipated questions with direct, self-contained answers, ordered by how often they are asked.
description: |
  A FAQ collects the questions a reader is most likely to ask and answers each one directly,
  ordered by frequency or by the reader journey. It optimizes for a reader who arrives with a
  specific question and wants a fast, self-contained answer, not a narrative. Each entry stands
  alone: a reader should never have to read the whole thing to get their one answer. The format
  earns its place when the questions are predictable, the answers are bounded, and the alternative
  is a wall of prose that buries what the reader actually needs.

  The shape of a FAQ reflects an understanding of the audience: the questions listed are the ones
  the audience has already demonstrated, not the ones the author wishes they would ask. Each answer
  should be the minimum necessary to satisfy the question. A FAQ that balloons answers into
  tutorials has traded away its only advantage. When an answer genuinely requires more depth, it
  should link out rather than expand in place.

  FAQ ordering is not alphabetical and not by author preference. Ordered by frequency, the most
  common question comes first and earns the reader trust immediately. When an audience is on a
  journey - evaluating, onboarding, troubleshooting - the ordering can follow that journey instead.
  Either way, the ordering is a deliberate editorial decision that the format forces.

  Typical length: variable, since the list scales with the number of questions, but each individual
  answer should target one to three short paragraphs.
canonical_template: |
  ## Frequently Asked Questions

  ### [Most frequently asked question, phrased as the reader would ask it?]

  [Answer in 1 to 3 sentences. Self-contained. Do not reference other answers.]

  ### [Second most frequent question?]

  [Answer. If the answer depends on a condition, state the condition first, then the answer for each case.]

  ### [Third question, often one that surfaces a common misconception?]

  [Answer. Correct the misconception directly, then give the right answer.]

  ### [Next question...]

  [Answer...]
typical_voices:
  - technical-writer
  - friendly-mentor
typical_tones:
  - instructional
  - matter-of-fact
digital_or_print: digital
pairs_well_with:
  - technical-writer
  - friendly-mentor
  - instructional
  - matter-of-fact
  - question-and-answer
avoid_with:
  - confessional
  - columnist
  - reverent
confusable_with:
  - technical-reference
when_to_use:
  - A product, service, or process generates a predictable set of recurring questions from users or customers
  - A landing page or onboarding flow needs to pre-empt common questions before the reader reaches a support channel
  - A policy or process document needs a companion that handles reader questions without bloating the main doc
  - Support documentation where readers arrive with a specific question and need a fast, targeted answer
  - After a change such as a product update, policy shift, or launch that will generate a burst of similar questions
when_not_to_use:
  - When the content is a precise technical specification with syntax, parameter definitions, or code examples - use a technical reference instead
  - When no genuine set of recurring questions exists and the format would be used to organize general information that belongs in a guide or reference
  - When the topic is complex enough that each question requires extensive context to answer accurately - a guide or tutorial serves that reader better
tells:
  - 'Questions written in the reader''s own words, often starting with "How do I", "What is", "Can I", or "Why does"'
  - 'Each question-answer pair is a complete, self-contained unit readable without the others'
  - 'Ordered by frequency with the most common question first, or by reader journey stage'
  - 'Answers are brief by design - typically one to three short paragraphs - and link out rather than elaborate inline'
  - 'No transitional prose between pairs; the pairs stand in parallel, not in sequence'
  - 'The question is phrased as the reader would ask it, not as the author would label the topic'
anti_patterns:
  - pattern: 'Phrasing questions the way the author thinks about the topic rather than the way the reader asks'
    why: 'A reader searching for help with a forgotten password will not find a section titled "Account credential management procedures"; the question must match the reader''s own phrasing.'
  - pattern: 'Expanding answers into multi-paragraph tutorials that require the reader to read through to reach the point'
    why: 'Self-containment and brevity are the format''s only advantages over a narrative doc; long answers erase both and signal the content belongs in a guide, not a FAQ.'
  - pattern: 'Using a FAQ to house precise technical specifications - syntax tables, parameter lists, field definitions, code examples - rather than natural-language question-answer pairs'
    why: 'A FAQ collects recurring natural-language questions with self-contained prose answers; a technical-reference is a precise specification of syntax, signatures, parameters, fields, and code. Blurring the two produces a document that does neither job well.'
  - pattern: 'Ordering questions alphabetically or by an author-chosen grouping instead of by reader frequency or journey'
    why: 'FAQ ordering is an editorial decision about the reader, not the author; author-centric ordering buries the most common question where readers stop looking.'
failure_modes:
  - mode: 'Over-atomizes - the format tips into a list of one-sentence stubs where every question gets a non-answer too brief to satisfy anything'
    mitigation: 'Each answer must do actual work; if the answer is shorter than the question, the question is probably out of scope for a FAQ, or needs one more sentence of genuine substance.'
  - mode: 'Over-populates - the format tips into an exhaustive catalogue of every possible question, including rare edge cases, until the common questions are buried in volume'
    mitigation: 'Audit by frequency; remove questions that only a small fraction of readers will ask and move edge-case depth to linked reference material rather than expanding the FAQ itself.'
  - mode: 'Over-isolates - each answer restates so much background context to be self-contained that answers balloon into repeated mini-essays and the document becomes bloated'
    mitigation: 'Self-contained means the reader does not need to read other answers to get their answer, not that each answer must recap the whole product; shared context belongs in a brief preamble, not repeated in every entry.'
llm_instruction_phrasing: |
  Write as a FAQ (Frequently Asked Questions). Structure the content as a series of discrete
  question-answer pairs. Phrase each question the way the reader would actually ask it, not the
  way you would label the topic. Each answer must be self-contained: the reader jumping directly
  to that pair should get a complete, useful response without needing to read other pairs. Order
  pairs by frequency (most common first) or by reader journey stage (orientation before
  troubleshooting). Keep individual answers brief - one to three short paragraphs - and link to
  deeper resources rather than elaborating inline. Do not write transitional prose between pairs.
  If an answer requires extensive length to be accurate, the question probably belongs in a guide,
  not a FAQ.
tags:
  - support
  - documentation
  - onboarding
  - reader-centric
  - question-driven
review_status: draft
---

## FAQ

A FAQ collects the questions a reader is most likely to ask and answers each one directly, ordered by frequency or by the reader journey. It optimizes for a reader who arrives with a specific question and wants a fast, self-contained answer, not a narrative. Each entry stands alone: a reader should never have to read the whole thing to get their one answer.

The shape of a FAQ reflects an understanding of the audience: the questions listed are the ones the audience has already demonstrated, not the ones the author wishes they would ask. Each answer should be the minimum necessary to satisfy the question. FAQ ordering is not alphabetical and not by author preference - it is a deliberate editorial decision about the reader, ordered by how often they ask or by the sequence of their journey.

### Canonical template

```
## Frequently Asked Questions

### [Most frequently asked question, phrased as the reader would ask it?]

[Answer in 1 to 3 sentences. Self-contained. Do not reference other answers.]

### [Second most frequent question?]

[Answer. If the answer depends on a condition, state the condition first, then the answer for each case.]

### [Third question, often one that surfaces a common misconception?]

[Answer. Correct the misconception directly, then give the right answer.]

### [Next question...]

[Answer...]
```

### When to use

A product, service, or process generates a predictable set of recurring questions from users or customers, a landing page or onboarding flow needs to pre-empt common questions before the reader reaches a support channel, a policy or process document needs a companion that handles reader questions without bloating the main doc, support documentation where readers arrive with a specific question and need a fast targeted answer, after a product update, policy shift, or launch that will generate a burst of similar questions.

### When not to use

When the content is a precise technical specification with syntax, parameter definitions, or code examples - use a technical reference instead. When no genuine set of recurring questions exists and the format would organize general information that belongs in a guide or reference. When the topic is complex enough that each question requires extensive context to answer accurately - a guide or tutorial serves that reader better.

### Pairs well with

`technical-writer`, `friendly-mentor`, `instructional`, `matter-of-fact`, `question-and-answer`

### Often confused with

**technical-reference**: Both formats serve a reader who arrives with a specific lookup rather than reading straight through. The difference is content: a FAQ collects recurring natural-language questions with self-contained prose answers, ordered by reader frequency; a technical-reference is a precise specification of syntax, signatures, parameters, fields, and code examples. A FAQ answers "How do I..." or "What happens if..."; a technical-reference documents exactly how something is defined.
