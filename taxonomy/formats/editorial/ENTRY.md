---
id: editorial
name: Editorial
axis: format
domain: public
family: position
one_liner: The unsigned opinion of a publication itself, stating the institution's position on an issue.
description: |
  An editorial is the unsigned opinion of a publication itself, written by or for the editorial
  board to state the institution's position on an issue. Unlike a bylined article or an op-ed
  contributed by an outside voice, the editorial speaks as "we" for the masthead, carrying the
  authority and accountability of the whole publication rather than any individual writer. The
  absence of a byline is not an omission - it is the format's defining feature. The institution
  stands behind the position, not a named person.

  The canonical structure opens with the publication's stated position, grounds it in context
  and evidence, and closes with a clear recommendation or conclusion attributed to the institution.
  The reasoning must do the work a personal voice would otherwise do: because there is no named
  author whose expertise or experience lends credibility, the editorial's argument must be
  self-evidently grounded in reported fact, observed pattern, or principled reasoning. A masthead
  that asserts without anchoring invites the charge of decree rather than judgment.

  Editorials earn their place because institutional voice carries weight that individual
  commentary cannot. A named contributor brings their own credibility to an op-ed; an editorial
  carries the credibility of the publication itself, which means it can endorse candidates, demand
  policy changes, or draw red lines in ways that no bylined piece can match. The format is built
  for accountability - the publication's collective judgment, on record.
canonical_template: |
  [Opening: the publication's position stated plainly in one to two sentences. No preamble.]

  [Context: what has happened or what issue is at stake - 1 to 2 paragraphs]

  [Reasoning: the evidence, pattern, or principle that grounds the position - 1 to 2 paragraphs]

  [Recommendation or conclusion: what the publication calls for or concludes.
  Close in the institution's voice.]
typical_voices:
  - columnist
  - journalist
typical_tones:
  - resolute
  - candid
digital_or_print: both
pairs_well_with:
  - columnist
  - journalist
  - resolute
  - candid
  - classical-argument
avoid_with:
  - confessional
  - playful
  - instructional
confusable_with:
  - op-ed
when_to_use:
  - Stating the publication's institutional position on a significant public issue or policy
  - Responding to a major event or decision with the masthead's collective judgment
  - Issuing a recommendation or endorsement in the publication's own voice
  - Providing accountability coverage where the institution itself must take a stand
  - Summarizing the publication's editorial direction on a recurring or contested issue
when_not_to_use:
  - When the piece will carry a named author's personal perspective (use an op-ed instead)
  - When the goal is to explore a topic without committing to a position
  - When the writer represents only themselves and not an institution with editorial accountability
tells:
  - 'Unsigned - no byline; the piece is attributed to the editorial board or the publication itself'
  - 'First-person plural throughout: the text speaks as "we" for the masthead, never as "I"'
  - 'Opens with the publication''s stated position in the first one or two sentences'
  - 'Grounds the position in reported fact, observed pattern, or principled reasoning rather than personal experience'
  - 'Closes with a recommendation or conclusion the reader can attribute to the institution'
  - 'No single author''s expertise or credential is invoked - authority is collective and institutional'
  - 'Shorter and more declarative than a feature or analysis, typically 400 to 700 words'
anti_patterns:
  - pattern: 'Using first-person singular ("I believe," "In my view") anywhere in the piece'
    why: 'An editorial speaks for the publication as a whole; a single "I" collapses the institutional voice into a personal one and undermines the accountability the format exists to carry.'
  - pattern: 'Hedging the position or presenting multiple sides without landing on one'
    why: 'An editorial earns its place by committing to where the institution stands; refusing to land a position turns the piece into an analysis or a summary of the debate.'
  - pattern: 'Treating the editorial as if it were an op-ed by writing a signed piece in which a named contributor argues their personal position in the publication''s pages'
    why: 'An op-ed is a short argued opinion piece - typically 600 to 800 words - written by an individual contributor advancing their own position under a byline; the editorial is unsigned, speaks as "we" for the masthead, and carries the accountability of the whole institution rather than one writer.'
  - pattern: 'Describing events without committing to a view, producing what reads as a news summary or analysis rather than institutional opinion'
    why: 'An editorial is an opinion format; if the piece reports without taking a stand, it has abandoned its defining purpose.'
failure_modes:
  - mode: 'Over-asserts institutional authority - every sentence becomes a proclamation, so the piece reads as a decree rather than a reasoned position'
    mitigation: 'Ground the position in evidence or observed pattern even when stating the institutional view; a masthead that asserts without reasoning sounds authoritarian rather than credible.'
  - mode: 'The collective "we" becomes so careful and inclusive that no actual position emerges - the editorial sounds like an institution but commits to nothing'
    mitigation: 'An editorial must close with a position the reader can name and attribute to the publication; if the closing reads as a hedge or can be taken two ways, redraft it until the stance is unambiguous.'
llm_instruction_phrasing: |
  Write as an editorial - the unsigned institutional voice of a publication's editorial board.
  Speak in first-person plural ("we") throughout; there is no byline, no individual perspective,
  no "I." Open with the publication's position stated plainly; the reader should know where the
  institution stands before the third sentence. Ground the position in reported fact, observed
  pattern, or principled reasoning - do not assert without anchoring the claim in something the
  reader can evaluate. Close with a recommendation or conclusion that the reader can attribute to
  the publication itself. Do not hedge the position into ambiguity, and do not slip into
  first-person singular or offer personal anecdote. The authority is collective and institutional.
tags:
  - opinion
  - journalism
  - public
  - institutional
  - accountability
  - position
review_status: draft
---

## Editorial

An editorial is the unsigned opinion of a publication itself, written by or for the editorial board to state the institution's position on an issue. Unlike a bylined article or an op-ed contributed by an outside voice, the editorial speaks as "we" for the masthead, carrying the authority and accountability of the whole publication rather than any individual writer. The absence of a byline is not an omission - it is the format's defining feature. The institution stands behind the position, not a named person.

The canonical structure opens with the publication's stated position, grounds it in context and evidence, and closes with a clear recommendation or conclusion attributed to the institution. The reasoning must do the work a personal voice would otherwise do: because there is no named author whose expertise or experience lends credibility, the editorial's argument must be self-evidently grounded in reported fact, observed pattern, or principled reasoning. A masthead that asserts without anchoring invites the charge of decree rather than judgment.

### Canonical template

```
[Opening: the publication's position stated plainly in one to two sentences. No preamble.]

[Context: what has happened or what issue is at stake - 1 to 2 paragraphs]

[Reasoning: the evidence, pattern, or principle that grounds the position - 1 to 2 paragraphs]

[Recommendation or conclusion: what the publication calls for or concludes.
Close in the institution's voice.]
```

### When to use

Stating the publication's institutional position on a significant public issue or policy, responding to a major event or decision with the masthead's collective judgment, issuing a recommendation or endorsement in the publication's own voice, providing accountability coverage where the institution itself must take a stand, summarizing the publication's editorial direction on a recurring or contested issue.

### When not to use

When the piece will carry a named author's personal perspective (use an op-ed instead), when the goal is to explore a topic without committing to a position, when the writer represents only themselves and not an institution with editorial accountability.

### Pairs well with

`columnist`, `journalist`, `resolute`, `candid`, `classical-argument`

### Often confused with

**op-ed**: An op-ed is a short argued opinion piece - typically 600 to 800 words - written by an individual contributor advancing their own position under a byline. It speaks in the contributor's voice and is attributed to a named author who may be an outside voice to the publication. An editorial, by contrast, is unsigned and speaks as "we" for the masthead; the authority is institutional rather than personal, and the accountability belongs to the publication as a whole rather than any named writer.
