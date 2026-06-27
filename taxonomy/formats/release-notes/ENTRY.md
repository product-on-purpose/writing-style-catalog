---
id: release-notes
name: Release Notes
axis: format
domain: public
family: broadcast
one_liner: A user-facing summary of what changed in a release and why it matters to the reader.
description: |
  Release notes are the user-facing companion to every software release. Where a changelog records
  every commit, ticket, and patch for developers, release notes are written for the people who use
  the product - they ask "what does this mean for me?" before they ask "what changed?" A release
  note leads with the benefit, groups changes by theme or workflow area, and translates technical
  fixes into plain language. "Fixed a null reference in the auth service" becomes "you will no
  longer be logged out unexpectedly while editing." The translation is the work.

  The format earns its place by bridging the gap between the team that builds and the audience that
  uses. Most teams ship more changes than users can absorb; curation is therefore a core
  responsibility. Release notes decide what rises to the surface - what is worth the reader's
  attention - and what stays in the commit log. A well-curated set of release notes respects the
  reader's time and builds confidence that the product is improving in ways that matter to them.

  Release notes have a recognizable structure: a version identifier, an optional short headline
  capturing the theme of the release, grouped sections for new features and fixes (and optionally
  deprecations or breaking changes), and brief plain-language descriptions of each item. The
  groupings are reader-oriented, not code-oriented. "Improved performance on large datasets" is a
  single note; it does not become three notes just because it required three pull requests.

  Typical length: 150 to 500 words, varying with release size.
canonical_template: |
  # [Product Name] [Version] - [Release Date]

  ## [Optional headline capturing the theme of this release]

  ## What's new

  - [Feature name]: [Plain-language description of the feature and what it enables for the user.]

  ## Improvements

  - [Area or workflow]: [What improved and how the user notices the difference.]

  ## Fixes

  - [Symptom or affected workflow]: [What was happening and that it no longer happens.]

  ## Known issues

  - [Issue]: [Workaround if available.]

  ## Deprecations and breaking changes (if any)

  - [What is changing]: [What the user must do, and by when.]
typical_voices:
  - product-thinker
  - technical-writer
typical_tones:
  - encouraging
  - matter-of-fact
digital_or_print: both
pairs_well_with:
  - product-thinker
  - technical-writer
  - friendly-mentor
  - encouraging
  - matter-of-fact
  - layered-disclosure
avoid_with:
  - confessional
  - skeptical
  - reverent
confusable_with:
  - changelog-entry
  - blog-post-long-form
  - announcement
when_to_use:
  - Announcing a versioned software release to end users or customers.
  - Publishing updates to a SaaS product, mobile app, developer tool, or library where the audience will update or encounter the new version.
  - Communicating what changed in a public API or SDK to the developers who build on it.
  - Accompanying a plugin, extension, or package release to its marketplace or registry.
  - Notifying users of a breaking change or deprecation that requires action on their part.
when_not_to_use:
  - Documenting internal engineering decisions or architecture changes (use an ADR).
  - Recording every commit and merged pull request as a developer audit trail (use a changelog entry).
  - Promoting a new product or major version in narrative form to prospective customers (use a blog post or launch announcement).
tells:
  - 'Opens with a version identifier and optional release date, not a prose introduction'
  - 'Groups changes by what users notice (New, Improved, Fixed) rather than by engineering area or ticket'
  - 'Each item leads with the user benefit or observable symptom, not with an internal ticket or PR number'
  - 'Plain-language translation of technical fixes into user-facing behavior'
  - 'Curates rather than enumerates - fewer items, higher signal per item'
  - 'Second-person framing addresses the reader directly: You can now, or Exporting a report no longer'
  - 'Breaking changes or deprecations isolated in a dedicated, visually distinct section'
anti_patterns:
  - pattern: 'Bullet-pointing every commit or ticket rather than curating the changes that matter to users'
    why: 'Readers cannot determine what is worth their attention when everything is listed; curation is the core responsibility of this format.'
  - pattern: 'Writing in technical jargon without translating into user-facing language'
    why: 'Resolved NullPointerException in TokenRefreshService is a changelog line; You will no longer be signed out while refreshing a shared link is a release note.'
  - pattern: 'Burying breaking changes inside a routine fix list without a migration path'
    why: 'Breaking changes require action from the user; making them hard to spot leaves users stranded at upgrade time.'
  - pattern: 'Framing the notes as a narrative story about why features were built rather than what changed and what it means'
    why: 'That is the confusable blog-post-long-form format; release notes are scannable reference documents, not product storytelling.'
failure_modes:
  - mode: 'Benefit-framing tips into promotional hyperbole - every fix becomes a "major improvement" and every feature is "game-changing," so the notes read as marketing copy rather than honest change documentation'
    mitigation: 'Check that each item describes a specific, observable change in behavior. Reports now load in under 2 seconds on datasets over 50,000 rows is a release note; Experience blazing-fast performance is marketing copy.'
  - mode: 'Curation tips into omission - only the most dramatic changes appear, routine fixes vanish entirely, and users who encountered the omitted bugs feel unacknowledged and distrust the notes'
    mitigation: 'Include all user-visible fixes, even minor ones. A short, undramatic note signals attentiveness. Reserve omission for changes that are genuinely invisible to users.'
  - mode: 'Plain-language translation strips out specificity until nothing is actionable - Various performance improvements and Bug fixes appear as entries that cover everything but inform nothing'
    mitigation: 'Every item should name a specific workflow, area, or symptom. If a note cannot be more specific than Bug fixes, the change was not user-visible and belongs in the changelog, not here.'
llm_instruction_phrasing: |
  Write as release notes for a user-facing software release. Lead every item with the user benefit
  or observable change, not the internal implementation detail. Group changes by what users notice -
  new capabilities, improvements, fixes - not by engineering area, file, or ticket number. Translate
  technical language into plain user-facing descriptions: resolved NullPointerException in
  TokenRefreshService becomes you will no longer be signed out while refreshing a shared link.
  Curate: include only changes that are visible or meaningful to the reader; leave exhaustive
  enumeration to the changelog. For breaking changes or deprecations, call them out in a visually
  distinct section and name the required user action. Keep the format scannable - version identifier,
  grouped bullets, plain language. Do not write prose paragraphs in place of bullets. Do not use
  marketing superlatives. Each item should describe a specific, observable change in user behavior
  or capability.
tags:
  - release-management
  - user-communication
  - product
  - documentation
  - software
review_status: stable
---

## Release Notes

Release notes are the user-facing companion to every software release. Where a changelog records every commit, ticket, and patch for developers, release notes are written for the people who use the product - they ask "what does this mean for me?" before they ask "what changed?" A release note leads with the benefit, groups changes by theme or workflow area, and translates technical fixes into plain language. "Fixed a null reference in the auth service" becomes "you will no longer be logged out unexpectedly while editing." The translation is the work.

The format earns its place by bridging the gap between the team that builds and the audience that uses. Most teams ship more changes than users can absorb; curation is therefore a core responsibility. Release notes decide what rises to the surface - what is worth the reader's attention - and what stays in the commit log. A well-curated set of release notes respects the reader's time and builds confidence that the product is improving in ways that matter to them.

### Canonical template

```
# [Product Name] [Version] - [Release Date]

## [Optional headline capturing the theme of this release]

## What's new
- [Feature name]: [Plain-language description of the feature and what it enables for the user.]

## Improvements
- [Area or workflow]: [What improved and how the user notices the difference.]

## Fixes
- [Symptom or affected workflow]: [What was happening and that it no longer happens.]

## Known issues
- [Issue]: [Workaround if available.]

## Deprecations and breaking changes (if any)
- [What is changing]: [What the user must do, and by when.]
```

### When to use

Announcing a versioned software release to end users or customers, publishing updates to a SaaS product, mobile app, developer tool, or library, communicating what changed in a public API or SDK, accompanying a plugin or package release to a marketplace or registry, notifying users of a breaking change or deprecation that requires action.

### When not to use

Documenting internal engineering decisions or architecture changes (use an ADR), recording every commit and merged pull request as a developer audit trail (use a changelog entry), promoting a new product or major version in narrative form to prospective customers (use a blog post or launch announcement).

### Pairs well with

`product-thinker`, `technical-writer`, `friendly-mentor`, `encouraging`, `matter-of-fact`, `layered-disclosure`

### Often confused with

**changelog-entry**: A changelog is a chronological, exhaustive record of every change merged into a codebase, authored for developers rather than users. Release notes curate from the changelog: they select the changes worth communicating, translate them into user language, and lead with benefit rather than implementation detail.

**blog-post-long-form**: A long-form blog post tells a narrative story about why something was built, what problems it solves, and where the product is going. Release notes are not storytelling - they are scannable reference documents. Where a blog post invites reading, release notes invite scanning.

**announcement**: Release notes are version-anchored, multi-item, and curated from a changelog into scannable grouped sections (New, Improved, Fixed) under a version identifier. An announcement is a single-subject news message in the organization's own voice with no version identifier and no grouped change sections. Use release notes when a versioned release has multiple changes to communicate; use an announcement when a single piece of news warrants its own direct message to the audience.
