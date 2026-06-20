---
id: readme
name: README
axis: format
domain: professional
family: instruction
one_liner: The front-door document for a software project - tells a first-time visitor what it is, why it exists, how to use it, and where to go next.
description: |
  A README is the landing page of a software project. It is read by people who have never seen the
  project before and have roughly thirty seconds of attention to decide whether to keep reading.
  Optimize aggressively for that first thirty seconds.

  The README is distinct from a technical reference. The reference serves the returning reader who
  knows what they want and needs to look it up. The README serves the first-time visitor who does
  not yet know what the project does. The two have opposite information architectures: reference is
  organized for lookup, README is organized for narrative - hook, install, minimal example, links to
  deeper docs.

  On GitHub the README is rendered on the repo's landing page, so the format borrows visual
  conventions from a landing page: a badge row near the top (build status, version, license), a
  short headline, an install command in a fenced code block, a minimal usage example, and a
  table-of-contents or a set of links to deeper documentation. Anything that does not fit the
  thirty-second pitch belongs in a linked doc, not in the README itself.

  Typical length: 100 to 600 words for the in-README prose, plus code blocks and badges.
canonical_template: |
  # Project Name

  [badges: build status, version, license, downloads]

  > One-sentence description of what the project does.

  A short paragraph (2 to 4 sentences) explaining what problem this solves and who it is for.

  ## Install

  ```
  [single install command, e.g. npm install foo or pip install foo]
  ```

  ## Quick start

  ```[language]
  [minimal working example, ideally under 10 lines]
  ```

  ## Documentation

  - [Getting started](docs/getting-started.md)
  - [API reference](docs/reference.md)
  - [Examples](examples/)

  ## Contributing

  See [CONTRIBUTING.md](CONTRIBUTING.md).

  ## License

  [License name] - see [LICENSE](LICENSE).
typical_voices:
  - technical-writer
  - pragmatic-architect
typical_tones:
  - matter-of-fact
  - instructional
digital_or_print: digital
pairs_well_with:
  - technical-writer
  - instructional
  - matter-of-fact
  - frequently-asked-questions
avoid_with:
  - pastoral
  - reverent
confusable_with:
  - technical-reference
when_to_use:
  - The top-level entry point for any open-source or internal software project
  - Library or CLI tool documentation root
  - Onboarding documentation for a new service or repo
  - Sample code repositories and starter templates
when_not_to_use:
  - Deep reference material that a returning user will navigate by lookup
  - A blog post about a project (the README is not the announcement)
  - Internal team status updates or runbooks
llm_instruction_phrasing: |
  Write a README for a software project. Optimize for a first-time visitor with thirty seconds of
  attention. Lead with a single-sentence description of what the project does, followed by a short
  paragraph explaining the problem and the audience. Include a single install command in a fenced
  code block, a minimal usage example also in a fenced code block, and links to deeper docs.
  Resist the urge to put everything in the README - link out to dedicated docs for anything beyond
  the basic pitch. Use matter-of-fact tone. Avoid marketing language; explain what the project
  does, not how revolutionary it is.
tags:
  - documentation
  - open-source
  - software
  - github
  - landing-page
  - digital
review_status: stable
---

## README

A README is the landing page of a software project. It is read by people who have never seen the project before and have roughly thirty seconds of attention to decide whether to keep reading. Optimize aggressively for that first thirty seconds: lead with what the project does, show a minimal example, and link out to deeper docs for everything else.

### Canonical template

```
# Project Name

[badges: build status, version, license, downloads]

> One-sentence description of what the project does.

A short paragraph (2 to 4 sentences) explaining what problem this solves and who it is for.

## Install

```
[single install command]
```

## Quick start

```[language]
[minimal working example, ideally under 10 lines]
```

## Documentation

- [Getting started](docs/getting-started.md)
- [API reference](docs/reference.md)
- [Examples](examples/)

## Contributing

See CONTRIBUTING.md.

## License

[License name]
```

### When to use

Use a README as the top-level entry point for any software project - open-source library, internal service, CLI tool, starter template. The README should be the first file a new reader sees and should answer "what is this and why would I use it" in under thirty seconds.

### When not to use

Do not use the README format for deep reference material that returning users will navigate by lookup - that belongs in a dedicated `technical-reference`. Do not use it as a blog post announcing the project. Do not use it for internal runbooks or status updates.

### Pairs well with

`technical-writer`, `instructional`, `matter-of-fact`, `frequently-asked-questions`

### Often confused with

**technical-reference**: A technical reference is optimized for the returning reader who knows what they want and needs to look it up - it is organized for retrieval. A README is optimized for the first-time visitor who does not yet know what the project does - it is organized for narrative hook and onboarding. A project usually needs both, in separate files.
