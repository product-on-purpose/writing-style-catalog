---
entry_id: changelog-entry
axis: format
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Team Standup Process - Changelog

All notable changes to this team's standup ritual are documented here. Versioning loosely follows SemVer: breaking ritual changes bump the major version.

## [2.0.0] - Async-first trial

Major change to how the 11-person team running across 4 timezones runs standups. This release ends the daily sync standup and replaces it with a written async post plus a single weekly working session. A 30-day trial period begins with this release.

### Added

- Async standup post in `#team-standup`, due by 10am local time, using a fixed three-field template (Shipped / In progress / Blocked or at risk).
- Slack shortcut `/standup` that pre-fills the three-field template.
- Thursday working session, 60 minutes, 8am Pacific / 8:30pm IST. Cancellable by Wednesday 5pm Pacific if there is no agenda.
- On-call engineer is now responsible for triaging `@mention` blockers in `#team-standup` within the workday. New on-call section added to the playbook.
- Trial retro doc at `docs/trial-retro.md` for capturing mid-trial feedback in one place.

### Changed

- On-call engineer's morning responsibility shifts from running the sync standup to scanning the async channel once between 10am and 11am Pacific.
- "Blocked" became "Blocked or at risk." We were under-reporting because nothing felt fully blocked until it was too late.
- Engineering manager's role on Mondays moves from facilitator to async reader. Office hours added Tuesday afternoon for 1:1 follow-ups.

### Deprecated

- "Quick sync after standup" sidebars. If something needs a 1:1, schedule it; do not assume the standup hangover provides one.

### Removed

- Daily 9am Pacific sync standup. The recurring calendar invite has been deleted from all 11 calendars.
- Manual standup notes doc. Async posts in Slack are now the source of truth and are searchable via channel history.
- Round-robin status order. There is no order in async; people post when they start their day.

### Migration notes

- Engineers in IST: you get your evenings back. The 9:30pm slot is yours again.
- Engineers in US Pacific and Eastern: your first 30 minutes of the day are now writing instead of talking.
- If you forget to post by 10am local, the on-call will `@mention` you. Two missed posts in a week triggers a check-in, not a punishment.

## [1.4.2] - Previous release

- Fixed: timezone display in the standup notes doc was showing PST year-round during daylight saving.

## [1.0.0] - Initial sync standup process

- Daily 9am Pacific standup, 15-minute time box, round-robin order, notes captured in a shared doc.
