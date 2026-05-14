---
adr_id: "0002"
title: Use Atomic-Folder Pattern for Taxonomy Entries
date: 2026-05-10
status: Accepted
---

# 0002 - Use Atomic-Folder Pattern for Taxonomy Entries

## Status

Accepted

## Context

Three structural options existed for organizing taxonomy entries:

1. Flat files: each entry is a single file at `taxonomy/<axis>/<entry-id>.md`. Simple, easy to browse. Cannot co-locate examples or anti-examples without naming collisions or separate mirrored directories.

2. YAML monolith: all entries for an axis live in one file (e.g., `voices.yaml`). Easy to read the full axis in one shot. Scales poorly as the catalog grows - merge conflicts are common on a single large file, individual entry review is difficult because changes are buried in a large diff, and there is no natural home for per-entry example files.

3. Atomic-folder pattern: each entry lives in its own directory at `taxonomy/<axis>/<entry-id>/ENTRY.md`, with subdirectories for examples and anti-examples.

The atomic-folder pattern is established practice in design system repositories (GOV.UK Design System, Atlassian Design System) and matches the agentskills.io plugin resource convention. It is also the natural fit for an entry set that will accumulate per-entry examples over time: Phase 0 has 5 entries per axis with 1 example each, Phase 1 targets 15 entries per axis with 3 examples each, and Phase 2 targets 50+ entries per axis with reference-quality multi-topic examples.

The per-entry directory also provides a clean unit of contribution. A pull request adding one voice entry touches exactly one directory plus the generated index artifact, making review scoped and fast.

## Decision

Each taxonomy entry lives at `taxonomy/<axis>/<entry-id>/ENTRY.md`.

Entry directories follow this structure:

```
taxonomy/voices/pragmatic-architect/
  ENTRY.md
  examples/
    async-standups-rfc.md
  anti-examples/
    too-hedging.md
```

Entry IDs are slugs conforming to the pattern `^[a-z][a-z0-9-]*[a-z0-9]$`. The entry directory name must exactly equal the `id` field in the entry's frontmatter. A validation script enforces this invariant at build time.

The four catalog directories are:

- `taxonomy/voices/` - Voice entries (Axis 1, persistent dimension)
- `taxonomy/tones/` - Tone entries (Axis 1, situational dimension)
- `taxonomy/styles/` - Style entries (Axis 2)
- `taxonomy/formats/` - Format entries (Axis 3)

## Consequences

### Positive
- Each entry is a self-contained unit. It can be reviewed, added, deprecated, or extended without touching any other entry's files.
- No merge conflicts on shared files. Two contributors adding different entries simultaneously produce non-overlapping diffs.
- Natural home for per-entry examples, anti-examples, and any future entry-specific assets (prompt files, renderings, test cases).
- Matches the contribution model of established design system repositories, reducing friction for contributors familiar with that pattern.

### Negative
- More directories than the flat-file approach. A catalog of 300 entries across four axes produces 300 entry directories plus example subdirectories.
- Build tools must traverse directory trees and aggregate ENTRY.md files rather than reading a single file. This is a modest but non-zero complexity cost.

### Neutral
- Build scripts in `tools/build-indexes.py` aggregate all entries into a single `taxonomy.json` artifact at build time. Downstream consumers (the SDK, the Composer) read the aggregated index rather than traversing the directory tree at runtime.
- The `.gitkeep` convention is used in empty `examples/` and `anti-examples/` subdirectories so Git tracks the directory structure before content is added.
