---
id: op-ed
name: Op-Ed
axis: format
domain: public
family: position
one_liner: A short argued opinion piece for a publication that advances one clear position on a timely issue.
description: |
  An op-ed is a short argued opinion piece - typically 600 to 800 words - written for a
  publication's readership to advance one clear position on a timely issue. The writer enters
  already holding a conviction; the work is to state it sharply, marshal a few well-chosen
  supporting points, and end on a call or implication. The form disciplines the writer: no
  meandering, no hedging, no comprehensive survey. One claim, argued concisely, for a readership
  that did not choose the writer.

  The canonical structure is three moves: the lede (a claim or provocation that names the position
  and why this piece exists now), the body (two to four supporting paragraphs, each a distinct point
  drawn from evidence, experience, or reasoning), and the close (a call to action, a reframing, or
  an implication the reader can carry away). The hard word limit makes every transition load-bearing;
  an op-ed cannot hide a weak seam behind volume.

  The format earns its place because a third-party outlet carries credibility that the writer's own
  channel does not. A byline in a publication speaks to a readership that did not opt in, which means
  the writer must earn attention in the first two sentences, sustain it through the constrained word
  count, and make the position land before the reader moves on.

  Typical length: 600-800 words.
canonical_template: |
  [Lede: the claim or provocation in one to two sentences. Name the issue and the position immediately.]

  [Context: why this issue matters now - 1 paragraph]

  [Point 1: first supporting argument or piece of evidence - 1 paragraph]

  [Point 2: second supporting argument or evidence - 1 paragraph]

  [Point 3 (optional): third supporting argument - 1 paragraph]

  [Close: call to action, reframing, or implication. Land the piece in one to two sentences.]
typical_voices:
  - columnist
  - journalist
typical_tones:
  - candid
  - resolute
digital_or_print: both
pairs_well_with:
  - columnist
  - journalist
  - candid
  - resolute
  - classical-argument
avoid_with:
  - instructional
  - reverent
  - pastoral
confusable_with:
  - blog-post-long-form
when_to_use:
  - Arguing a clear position on a timely public issue in a named outlet
  - Building external credibility through a third-party publication
  - Responding to a recent event, report, or policy decision with a focused opinion
  - Establishing a point of view for a bylined author on a contested question
  - Contributing to a public debate where the writer's stance is distinct and defensible
when_not_to_use:
  - When the topic requires nuanced exploration rather than a pre-held conclusion
  - When the goal is to inform or instruct rather than argue a position
  - When the writer wants to publish at their own length in their own venue without editorial constraints
tells:
  - 'Leads with the claim or provocation in the first one or two sentences - no preamble or buildup'
  - 'A single arguable position held throughout - no hedging or both-sides framing'
  - 'Two to four body paragraphs, each a distinct point, not a wandering exploration'
  - 'Hard word limit observed: 600-800 words, with no digressions'
  - 'Written for a named publication''s readership, not the writer''s own audience'
  - 'Ends on a call, implication, or reframing - not a restatement of the argument'
anti_patterns:
  - pattern: 'Opening with background or context before stating the position'
    why: 'Op-ed readers are strangers; the first sentence must earn the next. Delaying the claim wastes the lede and gives an editor reason to reject.'
  - pattern: 'Hedging the position throughout to capture both sides or add nuance'
    why: 'An op-ed argues one position; hedging collapses it into a summary of the debate and abandons the stance the format exists to carry.'
  - pattern: 'Writing a substantial, multi-section exploration of 1,500-plus words in a conversational voice - which is how a long-form blog post works, as a substantial web exploration with a present authorial voice - and then cutting it down to 800 words'
    why: 'A long-form blog post is a substantial web article (1,500-3,000 words) with a present, recognizable authorial voice; the op-ed is written for a third-party outlet, holds one pre-held position from the start, and is conceived at 600-800 words. Trimming a blog post does not produce an op-ed; the op-ed must be structured as argument from the first draft.'
  - pattern: 'Adding a supporting evidence paragraph for every sub-claim until the piece exceeds the word limit'
    why: 'The word constraint is structural; one well-chosen anchor per point is the discipline. A piece that needs exhaustive evidence for every claim has become a brief or policy paper.'
failure_modes:
  - mode: 'Hammers the same claim in every paragraph rather than building a cumulative argument, turning the piece into a one-note polemic'
    mitigation: 'Each body paragraph must advance a distinct point; if two paragraphs say the same thing with different words, collapse them and use the freed space to add a second supporting line of reasoning.'
  - mode: 'Over-compresses for the word limit and tips into pure assertion - the claim is stated but never supported enough to distinguish the piece from a tweet thread'
    mitigation: 'Even at 600-800 words there is room for two to three concrete anchors (an example, a figure, an observed pattern); if a draft has none, it is asserting rather than arguing and will not survive an editorial read.'
llm_instruction_phrasing: |
  Write as an op-ed (600-800 words). Lead with the position in the first one or two sentences - do
  not open with context, history, or a rhetorical question. The claim must be arguable, timely, and
  clear before the third sentence. Structure the body as two to four distinct supporting points, one
  per paragraph, each grounded in a concrete example, figure, or observation. Do not hedge the
  position or present multiple sides - this is an opinion piece, not a survey. End with a call to
  action, a reframing, or an implication the reader can carry forward. Stay within 800 words.
tags:
  - opinion
  - public
  - journalism
  - persuasion
  - argument
review_status: draft
---

## Op-Ed

An op-ed is a short argued opinion piece - typically 600 to 800 words - written for a publication's readership to advance one clear position on a timely issue. The writer enters already holding a conviction; the work is to state it sharply, marshal a few well-chosen supporting points, and end on a call or implication. The form disciplines the writer: no meandering, no hedging, no comprehensive survey. One claim, argued concisely, for a readership that did not choose the writer.

The canonical structure is three moves: the lede (a claim or provocation that names the position and why this piece exists now), the body (two to four supporting paragraphs, each a distinct point drawn from evidence, experience, or reasoning), and the close (a call to action, a reframing, or an implication the reader can carry away). The hard word limit makes every transition load-bearing; an op-ed cannot hide a weak seam behind volume.

### Canonical template

```
[Lede: the claim or provocation in one to two sentences. Name the issue and the position immediately.]

[Context: why this issue matters now - 1 paragraph]

[Point 1: first supporting argument or piece of evidence - 1 paragraph]

[Point 2: second supporting argument or evidence - 1 paragraph]

[Point 3 (optional): third supporting argument - 1 paragraph]

[Close: call to action, reframing, or implication. Land the piece in one to two sentences.]
```

### When to use

Arguing a clear position on a timely public issue in a named outlet, building external credibility through a third-party publication, responding to a recent event or policy decision with a focused opinion, establishing a point of view for a bylined author on a contested question.

### When not to use

When the topic requires nuanced exploration rather than a pre-held conclusion, when the goal is to inform or instruct rather than argue a position, when the writer wants to publish at their own length in their own venue without editorial constraints.

### Pairs well with

`columnist`, `journalist`, `candid`, `resolute`, `classical-argument`

### Often confused with

**blog-post-long-form**: A long-form blog post is a substantial web article of 1,500-3,000 words with a present and recognizable authorial voice; it can pursue a focused argument or a deeper exploration of a topic at its own pace. An op-ed is written for a third-party publication, holds to 600-800 words, and argues a single pre-held position from the first sentence. The blog post's length lets the writer develop ideas gradually; the op-ed's hard word limit and external outlet demand that the position be declared and defended without detour.
