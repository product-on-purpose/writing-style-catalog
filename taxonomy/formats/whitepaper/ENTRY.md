---
id: whitepaper
name: Whitepaper
axis: format
domain: public
family: position
one_liner: A long-form authoritative document presenting a position, framework, or analysis - the format for setting position-of-record on a substantive topic.
description: |
  A whitepaper is a long-form document, typically 5 to 30 pages, that presents an authoritative
  position, framework, or analysis on a substantive topic. It is the format used when an
  organization or expert wants to set position-of-record - when the question is important enough
  that a blog post is too casual and a slide deck is too thin.

  The structural conventions are stable: an executive summary at the top (one page, readable on
  its own, often the only thing executives will read); structured body sections with clear
  headings; figures, tables, and citations as needed; and a conclusion section that explicitly
  names implications and recommendations. The executive summary is load-bearing - it must work as
  a standalone artifact for the reader who will not read further.

  Whitepapers serve three audiences simultaneously and have to work for all three: the executive
  who reads only the summary, the analyst who reads the body for evidence, and the skeptic who
  reads the citations to verify the work. The format succeeds when all three come away aligned on
  what the paper claims and what evidence supports it.

  The whitepaper is distinct from a long-form blog post in tone (authoritative rather than
  personal), from a technical reference in purpose (position rather than lookup), and from a
  consulting deliverable in audience (public or semi-public rather than client-specific). It is
  the document an organization publishes when it wants to be cited.

  Typical length: 2,000 to 12,000 words; commonly distributed as a designed PDF.
canonical_template: |
  # [Title - Specific, Substantive, Not Generic]
  ## [Optional subtitle that names the argument or the framework]

  **Authors:** [Names, affiliations]
  **Published:** [Date]
  **Version:** [Version number, if applicable]

  ## Executive Summary
  [One page. Stands alone. Names the problem, the position, the evidence in brief, and the
  implications. A reader who stops here should still come away with the paper's claim.]

  ## Introduction
  [Frame the problem. Why does this matter now. Who is the audience.]

  ## Background
  [What the reader needs to understand to evaluate the argument. Cite prior work.]

  ## [Body Section 1 - the first main movement of the argument]
  [Substance, evidence, figures.]

  ## [Body Section 2]
  [...]

  ## [Body Section 3]
  [...]

  ## Implications and Recommendations
  [What follows from the argument. What should the reader do.]

  ## Conclusion
  [Restate the position. Name the open questions.]

  ## References
  [Citations in a consistent format.]

  ## Appendix (optional)
  [Methodology, data tables, supplementary detail.]
typical_voices:
  - senior-consultant
  - researcher
  - executive
typical_tones:
  - confident
  - matter-of-fact
  - resolute
digital_or_print: both
pairs_well_with:
  - senior-consultant
  - executive
  - executive-summary
  - researcher
avoid_with:
  - playful
  - slack-message
confusable_with:
  - blog-post-long-form
  - technical-reference
when_to_use:
  - Setting an organization's public position on a substantive topic
  - Presenting original research or a new framework to a professional audience
  - Industry analysis intended to be cited by analysts, journalists, or peers
  - Policy proposals or strategic recommendations to senior decision-makers
  - Vendor-published thought leadership intended to anchor a category
when_not_to_use:
  - Internal team communication (use status-report or one-pager)
  - Casual or personal commentary (use blog-post-long-form)
  - Lookup-style documentation (use technical-reference)
  - Anything that will be obsolete in under six months
tells:
  - 'A standalone executive summary at the top that carries the claim on its own'
  - 'Structured body sections with clear, descriptive headings'
  - 'Figures, tables, and rigorous citations supporting the argument'
  - 'An explicit Implications and Recommendations section, not left to inference'
  - 'An authoritative, largely invisible authorial stance - position presented as established'
  - 'Long-form (roughly 2,000-12,000 words), commonly a designed PDF'
anti_patterns:
  - pattern: 'Writing in a personal, exploratory voice with the author present in the prose'
    why: 'That is the confusable blog-post-long-form; a whitepaper is institutional and authoritative, presenting position rather than a writer thinking out loud.'
  - pattern: 'Organizing the content for retrieval with lookup-oriented sections'
    why: 'That is the confusable technical-reference, built for the returning reader; a whitepaper is organized as an argument for the first-time reader who must be convinced.'
  - pattern: 'Omitting the executive summary or making it depend on the body'
    why: 'The summary is load-bearing - many executives read only it - so it must stand alone with the claim, the evidence in brief, and the implications.'
failure_modes:
  - mode: 'Piles on jargon and citations to perform authority - density of references and terminology stands in for an actual argument'
    mitigation: 'Citations exist so the skeptic can verify the work, not to impress; if a reference or a term does not support the claim, cut it and let the argument carry the authority.'
  - mode: 'Over-invests in length and ceremony - sections are padded to look substantial until the position is buried under its own scaffolding'
    mitigation: 'Every section must earn its place; resist padding, and if a reader cannot state the paper''s claim after the summary, the bulk is hiding rather than supporting it.'
llm_instruction_phrasing: |
  Write a whitepaper - a long-form authoritative document setting position-of-record on a
  substantive topic. Open with an executive summary of roughly one page that stands alone: a reader
  who stops there should still know the paper's claim, the evidence in brief, and the implications.
  Use a confident, matter-of-fact voice; do not hedge unnecessarily but do not overclaim. Structure
  the body in clear sections with descriptive headings. Cite sources rigorously - a whitepaper that
  cannot be verified loses its authority. End with explicit Implications and Recommendations; do
  not leave the reader to infer what follows from the argument. Length is typically 2,000 to 12,000
  words. Resist the temptation to pad; every section must earn its place.
tags:
  - long-form
  - authoritative
  - research
  - thought-leadership
  - policy
  - pdf
  - both
review_status: stable
---

## Whitepaper

A whitepaper is a long-form document, typically 5 to 30 pages, that presents an authoritative position, framework, or analysis on a substantive topic. It is the format used when an organization or expert wants to set position-of-record - when the question is important enough that a blog post is too casual and a slide deck is too thin. The executive summary at the top is load-bearing; it must work as a standalone artifact for the reader who will not read further.

### Canonical template

```
# [Title - Specific, Substantive, Not Generic]
## [Optional subtitle that names the argument or framework]

**Authors:** [Names, affiliations]
**Published:** [Date]

## Executive Summary
[One page. Stands alone. Names the problem, the position, the evidence in brief, and the implications.]

## Introduction
[Frame the problem. Why does this matter now. Who is the audience.]

## Background
[What the reader needs to understand to evaluate the argument. Cite prior work.]

## [Body Section 1 - the first main movement of the argument]
[Substance, evidence, figures.]

## [Body Section 2]
[...]

## Implications and Recommendations
[What follows from the argument. What should the reader do.]

## Conclusion
[Restate the position. Name the open questions.]

## References
[Citations in a consistent format.]

## Appendix (optional)
[Methodology, data tables, supplementary detail.]
```

### When to use

Use a whitepaper to set an organization's public position on a substantive topic, to present original research or a new framework, to publish industry analysis intended to be cited, or to deliver policy proposals to senior decision-makers. It is the format you reach for when you want to be cited.

### When not to use

Do not use a whitepaper for internal team communication (use `status-report` or `one-pager`). Do not use it for casual or personal commentary (use `blog-post-long-form`). Do not use it for lookup-style documentation (use `technical-reference`). Do not write one on a topic that will be obsolete in six months; the format invests too much for that payoff.

### Pairs well with

`senior-consultant`, `executive`, `executive-summary`, `researcher`

### Often confused with

**blog-post-long-form**: A long-form blog post is personal and exploratory; the author is present in the prose and the argument unfolds informally. A whitepaper is institutional and authoritative; the author is largely invisible and the argument is presented as established position. Same length range, opposite stance.

**technical-reference**: A technical reference is optimized for the returning reader who needs to look something up; it is organized for retrieval. A whitepaper is optimized for the first-time reader who needs to be convinced of a position; it is organized as an argument. The two have opposite information architectures.
