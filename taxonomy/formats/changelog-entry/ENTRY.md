---
id: changelog-entry
name: Changelog Entry
axis: format
one_liner: A structured release entry naming what was added, changed, fixed, or removed in a given version - grouped by impact class under a version heading.
description: |
  A changelog entry is the structured short form of a release announcement. It lives under a version
  heading (commonly "## 2.3.0 - 2026-05-14") and groups items by impact class: Added, Changed,
  Fixed, Deprecated, Removed, Security. Each item is one line, written in the past tense or as a
  short noun phrase, and links to the underlying issue or PR where possible.

  The load-bearing convention is the grouping itself. A reader scanning a changelog is usually
  asking one of two questions: "did anything break for me" (Changed, Deprecated, Removed, Security)
  and "did anything I wanted get fixed" (Added, Fixed). The impact-class structure answers both
  questions in seconds.

  The most widely cited convention is Keep a Changelog (keepachangelog.com), which prescribes the
  six sections above plus a chronological order with the newest version at the top. Many projects
  vary - some add Performance, some merge Security into Fixed - but the structure-by-impact-class
  is universal. If a project's changelog is a flat list of commit messages it has failed to be a
  changelog; it has become a git log.

  Typical length: 5 to 30 lines per version, occasionally longer for major releases.
canonical_template: |
  ## [Version] - YYYY-MM-DD

  ### Added
  - [New feature, described from the user's perspective] (#PR or #issue)

  ### Changed
  - [Behavior change that does not break existing usage] (#PR)

  ### Deprecated
  - [Feature scheduled for removal in a future version, with migration note] (#PR)

  ### Removed
  - [Feature deleted in this version, with migration note] (#PR)

  ### Fixed
  - [Bug fix, described from the user's perspective] (#PR)

  ### Security
  - [Security fix, often with CVE link or advisory link] (#PR)
typical_voices:
  - technical-writer
  - pragmatic-architect
typical_tones:
  - matter-of-fact
digital_or_print: digital
pairs_well_with:
  - technical-writer
  - matter-of-fact
  - decision-log
avoid_with:
  - storyteller
  - narrative-case-study
confusable_with:
  - meeting-notes
when_to_use:
  - Software release announcements in a CHANGELOG.md file
  - Version notes published alongside a tagged release
  - API or SDK version migration docs
  - Library upgrade guides where users need to scan impact quickly
when_not_to_use:
  - Marketing-style release announcements (use long-form blog post instead)
  - Internal team status updates (use status-report)
  - A running development journal (use a git log or session notes)
llm_instruction_phrasing: |
  Write a changelog entry for a software release. Use a version heading in the form
  "## [VERSION] - YYYY-MM-DD". Group items under the six standard subsections: Added, Changed,
  Deprecated, Removed, Fixed, Security. Omit empty subsections. Each item should be one line,
  written from the user's perspective (what changed for them), and linked to the underlying PR or
  issue where possible. Use matter-of-fact tone. Do not editorialize, do not market, do not narrate.
  If an item is a breaking change, say so explicitly and include a migration note.
tags:
  - software
  - release-notes
  - versioning
  - structured
  - digital
  - keep-a-changelog
review_status: stable
---

## Changelog Entry

A changelog entry is the structured short form of a release announcement. It lives under a version heading and groups items by impact class (Added, Changed, Fixed, Deprecated, Removed, Security). The grouping itself is the load-bearing convention: it lets a reader answer "did anything break for me" and "did anything I wanted get fixed" in seconds.

### Canonical template

```
## [Version] - YYYY-MM-DD

### Added
- [New feature, described from the user's perspective] (#PR)

### Changed
- [Behavior change that does not break existing usage] (#PR)

### Deprecated
- [Feature scheduled for removal in a future version, with migration note] (#PR)

### Removed
- [Feature deleted in this version, with migration note] (#PR)

### Fixed
- [Bug fix, described from the user's perspective] (#PR)

### Security
- [Security fix, often with CVE link or advisory link] (#PR)
```

### When to use

Use a changelog entry for software release notes, version migration docs, and library upgrade guides where users need to scan impact quickly. Each version gets one entry; entries accumulate in a single CHANGELOG.md with newest at the top.

### When not to use

Do not use this format for marketing-style release announcements (write a long-form blog post instead). Do not use it for internal team status updates. Do not paste a git log and call it a changelog - the grouping by impact class is the whole point.

### Pairs well with

`technical-writer`, `matter-of-fact`, `decision-log`

### Often confused with

**meeting-notes**: Meeting notes capture discussion that happened in a meeting; they are organized by topic and time. A changelog entry captures what changed in a software release; it is organized by impact class. The two share a "structured short form" feel but serve completely different purposes.
