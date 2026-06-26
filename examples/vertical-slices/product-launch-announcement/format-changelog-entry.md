---
entry_id: changelog-entry
axis: format
topic_slug: product-launch-announcement
topic_label: Announcing a new product to an outside audience
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## [1.0.0] - 2026-07-02

First public release. Tidemark is now available to all teams.

### Added
- Feedback inbox where team members submit or paste customer verbatims collected from any channel (#12)
- CSV import for bulk-loading feedback exported from a ticket tracker or spreadsheet (#18)
- Automated ranking that scores each item by submission volume, recency, and configurable priority weights (#23)
- Ranked roadmap view listing items in descending priority order with vote counts and source tags (#27)
- Read-only shareable roadmap link for distributing the current ranked list to stakeholders outside the workspace (#31)
- Comment threads on each roadmap item for adding team context without switching to another tool (#35)
- Merge tool for consolidating duplicate or near-duplicate feedback items into a single ranked entry (#38)
- Workspace settings panel for managing members, priority weights, and roadmap visibility (#41)

### Changed
- Priority weights are now configurable per workspace; teams must set weights in Settings > Ranking before the first ranked view appears - the fixed beta defaults are no longer in effect (#44)
- Public share link format changed from `/share/<integer>` to `/share/<token>`; beta share links are no longer valid and must be regenerated from the Sharing tab (#47)

### Fixed
- Feedback items submitted within the same minute no longer appear twice in the inbox after a page refresh (#51)
- Ranking score now recalculates immediately when two feedback items are merged, rather than waiting for the next scheduled update (#54)
- CSV import no longer truncates feedback text at 500 characters (#57)

### Security
- Public share links now use a random token instead of a sequential integer ID, preventing enumeration of shared roadmaps (#60)
