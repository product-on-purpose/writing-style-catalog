---
id: blog-post-long-form
name: Blog Post (Long Form)
axis: format
domain: public
family: broadcast
one_liner: A substantial web article of 1,500-3,000 words - long enough to go deep, short enough to respect the reader's time.
description: |
  Long-form blog posts occupy a specific territory: they go deeper than a quick take but stop
  before they become a whitepaper or essay. The format works because it has a conversational
  quality that whitepapers lack - the writer is present, the voice is recognizable, and the reader
  feels addressed rather than briefed. The constraint of "post" still applies: this should have a
  specific, focused argument or exploration, not a comprehensive treatment of a domain.

  Structure matters more in long-form than in short-form because the reader needs navigation.
  Headers every 300-500 words, a clear progression from setup to insight to implication, and an
  opening that immediately establishes the specific territory (not the field, the territory) are
  the structural requirements. The title and opening paragraph carry an implicit promise to the
  reader; the rest of the post is the promise kept.

  Long-form posts live or die on the opening and the ending. The opening must establish the
  specific argument or question quickly and make clear why the reader should spend 1,500 more words
  with you. The ending should not summarize - it should land. The reader's last impression of the
  post is the lasting impression.

  Typical length: 1,500-3,000 words.
canonical_template: |
  [Title: specific, not generic]

  [Opening: establishes specific argument and stakes - 2-3 paragraphs]

  [Section 1 header]
  [Content - 300-500 words]

  [Section 2 header]
  [Content - 300-500 words]

  [Section 3 header]
  [Content - 300-500 words]

  [Closing: landing, not summary - 2-3 paragraphs]
typical_voices:
  - columnist
  - friendly-mentor
  - pragmatic-architect
typical_tones:
  - candid
  - warm
  - matter-of-fact
digital_or_print: digital
pairs_well_with:
  - columnist
  - friendly-mentor
  - candid
  - warm
  - diataxis-explanation
  - classical-argument
avoid_with:
  - operator
  - reverent
  - pastoral
confusable_with:
  - whitepaper
when_to_use:
  - Thought leadership
  - Technical explainers
  - Opinion pieces
  - Narrative case studies
  - Educational content
when_not_to_use:
  - Quick updates
  - Operational documentation
  - Formal reports
  - Anything requiring strict citation
tells:
  - 'A specific, non-generic title that names the angle, not the field'
  - 'An opening of 2-3 paragraphs that establishes the specific argument and stakes'
  - 'Section headers roughly every 300-500 words to give the reader navigation'
  - 'A clear progression from setup to insight to implication'
  - 'A closing that lands rather than summarizes - 2-3 paragraphs'
  - 'Substantial length (1,500-3,000 words) with a present, recognizable authorial voice'
anti_patterns:
  - pattern: 'Attempting a comprehensive treatment of an entire domain instead of one focused argument'
    why: 'The "post" constraint still applies; a comprehensive survey drifts toward the confusable whitepaper, which sets position-of-record rather than exploring a specific angle.'
  - pattern: 'Writing in an invisible, institutional voice with rigorous citation as the backbone'
    why: 'That is the whitepaper stance; the long-form post works precisely because the writer is present and the reader feels addressed rather than briefed.'
  - pattern: 'Ending with a recap that restates the section headers'
    why: 'The closing is the lasting impression; a summary wastes it, and the format explicitly asks the ending to land, not to summarize.'
failure_modes:
  - mode: 'Pads with filler - throat-clearing, restatement, and digression stretch the piece to hit the word count rather than to go deeper'
    mitigation: 'Length should come from depth, not volume; if a section does not advance the specific argument, cut it even if the post then runs short of 1,500 words.'
  - mode: 'Over-navigates - so many headers and signposts are added that the prose fragments into a skimmable outline with no continuous thread'
    mitigation: 'Headers exist to aid a reader who is already reading; if removing a header loses no meaning, the section was too thin to deserve one.'
llm_instruction_phrasing: |
  Write as a long-form blog post (1,500-3,000 words). Establish the specific argument or question
  in the opening - not the topic, the specific angle. Use headers every 300-500 words to give the
  reader navigation. The structure should move from setup through insight to implication. The
  opening must earn the reader's next 1,500 words immediately. The closing should land - not
  summarize. Give the reader something to carry away. Conversational but substantial - present in
  voice, deep in content.
tags:
  - blog
  - web
  - long-form
  - thought-leadership
  - educational
  - content-marketing
review_status: stable
---

## Blog Post (Long Form)

Long-form blog posts occupy a specific territory: they go deeper than a quick take but stop before they become a whitepaper or essay. The format works because it has a conversational quality that whitepapers lack - the writer is present, the voice is recognizable, and the reader feels addressed rather than briefed.

Structure matters more in long-form than in short-form because the reader needs navigation. Headers every 300-500 words, a clear progression from setup to insight to implication, and an opening that immediately establishes the specific territory.

### Canonical template

```
[Title: specific, not generic]

[Opening: establishes specific argument and stakes - 2-3 paragraphs]

[Section 1 header]
[Content - 300-500 words]

[Section 2 header]
[Content - 300-500 words]

[Section 3 header]
[Content - 300-500 words]

[Closing: landing, not summary - 2-3 paragraphs]
```

### When to use

Thought leadership, technical explainers, opinion pieces, narrative case studies, educational content.

### When not to use

Quick updates, operational documentation, formal reports, anything requiring strict citation.

### Pairs well with

`columnist`, `friendly-mentor`, `candid`, `warm`, `diataxis-explanation`, `classical-argument`

### Often confused with

**adr**: An ADR is short, structured, and records a specific decision. A long-form blog post is conversational, substantial, and explores a topic for a general audience.

**prd**: A PRD defines product requirements internally. A long-form blog post communicates ideas externally to a broad audience.
