---
entry_id: changelog-entry
axis: format
topic_slug: morning-routine
topic_label: How to start a morning routine
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# My Morning Routine - Changelog

A running log of changes to my personal first-hour protocol. Versioning is loose but real: a major bump means the structure changed, a minor bump means a step was tuned, a patch bump means I noticed a small thing.

## [3.0.0] - The four-step protocol

The first protocol I have actually stuck to for more than two weeks. This release reorganizes the entire morning around a fixed sequence and bans the phone from the first 35 minutes after waking.

### Added

- **Water step.** 500ml within 5 minutes of waking. The glass goes on the nightstand the night before, which removed the only excuse I had been using.
- **Light step.** 10 minutes outside, or by an open window when weather refuses. Counts as light only if there is no screen between me and the light source.
- **Planning step.** 10 minutes with paper and pen. Top three for the day, written before any Slack or email exposure.
- **Daily log row in `log/days.csv`.** Single row, six columns. Done as part of the planning step, on the same page.

### Changed

- **Wake time fixed at 6:15.** Previously drifting between 6:00 and 7:00 depending on the night before. The drift was doing more damage than the lost sleep.
- **Movement reduced from 30 minutes to 15.** The longer block was the reason I skipped the routine entirely on tired days. A 15-minute floor turns out to be more sustainable than a 30-minute aspiration.
- **Coffee is now after planning, not before.** Caffeine before water and light made me jittery and unfocused. Now it bookends the protocol instead of replacing it.

### Deprecated

- **The 5:30 wake attempt.** Beautiful in theory, unkind to my actual sleep need. Keeping it documented in `notes/abandoned/` for archaeology.

### Removed

- **Phone in the first 35 minutes.** This was the hardest one and the highest-impact. The phone now lives charging in the kitchen overnight, not on the nightstand.
- **Morning email triage.** Moved to 9:15am as the first work block. Email was masquerading as planning; planning needs paper.
- **Optional steps.** v2.x had a stretch step that was sometimes there, sometimes not. Optional became "skipped." The whole protocol is now mandatory or I have not done it.

### Fixed

- The "I will start tomorrow" loop. Counting partial mornings as completed-with-asterisk fixed the all-or-nothing failure mode.

### Migration notes

- I moved the phone to the kitchen on a Sunday night and could not reach it from bed. That is the migration.
- Family is already used to me being weird in the morning, so no comms needed there.

## [2.4.1] - Patch

- Fixed: 6am cold water on the face was not waking me up faster, it was waking up my sinuses. Removed.

## [2.0.0] - The "wake up earlier" attempt

- Tried 5:30 wake. Lasted 11 days. Got more tired, not less productive. Filed under "lessons."

## [1.0.0] - The original

- Wake, check phone, scroll, get dressed, leave. The default. Documented here only so the changes have a baseline.
