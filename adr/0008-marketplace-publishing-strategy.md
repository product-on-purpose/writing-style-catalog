---
adr_id: "0008"
title: Publish as Experimental on agentskills.io from Phase 0
date: 2026-05-10
status: Accepted
---

# 0008 - Publish as Experimental on agentskills.io from Phase 0

## Status

Accepted

## Context

The plugin can be published to the agentskills.io marketplace at any point after the Phase 0 walking skeleton is complete. Three timing options were considered:

1. Publish immediately as `experimental` from Phase 0.
2. Hold until Phase 1 ships (Composer + 15 entries per axis) and publish as `beta`.
3. Register the plugin as `unlisted` in Phase 0, making it installable by direct link but not discoverable in marketplace search.

The core tension is between discoverability value and first-impression risk. An `experimental` plugin with 5 entries per axis that ships early starts the discoverability flywheel in an ecosystem where early listings accumulate reviews and install counts before the ecosystem saturates. A plugin that holds until Phase 1 ships better but joins a potentially more crowded marketplace.

The Claude Code ecosystem as of May 2026 is dominated by early adopters who are sophisticated about evaluating experimental software. They read status flags, they install experimental tools with appropriate expectations, and they leave feedback that is actionable rather than dismissive. This is the cohort most likely to give useful Phase 0 feedback before the catalog grows.

The `unlisted` option was evaluated and rejected. An unlisted plugin is effectively invisible except to users who receive a direct link. The discoverability cost of hiding a published plugin in this ecosystem outweighs the marginal first-impression improvement over using the `experimental` status correctly.

## Decision

Publish to the agentskills.io marketplace with `status: experimental` from Phase 0.

The `marketplace.json` file sets `"status": "experimental"` and will be updated to `"status": "stable"` when Phase 1 ships (Composer + 15 entries per axis). The README prominently displays the current phase and phase roadmap so users who install the plugin know what to expect and when to expect improvements.

No `unlisted` period. The discoverability cost of an unlisted plugin in the current ecosystem is higher than the first-impression cost of an explicitly `experimental` plugin.

The Phase 0 -> Phase 1 upgrade path is handled by the standard plugin update mechanism. Breaking changes to the SDK API (if any) will be documented in the changelog and signaled by a semver minor bump.

## Consequences

### Positive
- Early feedback from real users who self-select into the `experimental` cohort provides signal before the catalog is fully built.
- The discoverability flywheel starts earlier. Install counts, reviews, and word-of-mouth start accumulating from Phase 0 rather than Phase 1.
- Contributing to the agentskills.io catalog immediately, rather than waiting, demonstrates commitment to the ecosystem and increases the likelihood of being featured in curator roundups.

### Negative
- Any bugs or schema changes in Phase 0 are visible to anyone who installs the plugin. Phase 0 is explicitly a walking skeleton, and some rough edges are expected.
- Phase 0 has only 5 entries per axis. Some users who expect a production-ready style catalog may be disappointed by the thin initial coverage, even with the `experimental` status set.
- Schema changes between Phase 0 and Phase 1 may require migration guidance for users who have built automation on the Phase 0 SDK interface.

### Neutral
- The `experimental` status sets correct expectations for the target cohort. Users who require stable, production-ready plugins will skip experimental listings by convention.
- The plugin update process handles the Phase 0 -> Phase 1 upgrade path without requiring users to reinstall. The status flag update from `experimental` to `stable` triggers a marketplace re-index.
