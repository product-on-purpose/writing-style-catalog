---
diff_pair_id: format-changelog-entry-vs-meeting-notes-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: format
entry_a: changelog-entry
entry_b: meeting-notes
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Format swap - `changelog-entry` vs `meeting-notes`

**Topic:** Should we adopt async-first standups?
**Axis varied:** format
**A:** `changelog-entry` - A structured release entry naming what was added, changed, fixed, or removed in a given version - grouped by impact class under a version heading.
**B:** `meeting-notes` - A structured capture of what was decided and what was assigned - not a transcript. Organized by outcome so someone who missed the meeting can act without asking follow-up questions.

## What to notice

Both examples address the same topic and (by default) share every axis other than format. 
The only deliberate variable is which format the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The format 
swap is the entire cause of those differences.

---

## A: `changelog-entry`

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

---

## B: `meeting-notes`

# Platform Eng Weekly - Standup Format Review

**Date:** 2026-05-14 (Thursday)
**Time:** 09:00 - 09:45 Pacific
**Location:** Zoom + #eng-platform thread
**Facilitator:** Maya Chen
**Notes:** Priya Raman

## Attendees

Present (9): Maya Chen, Priya Raman, Devon Park, Sara Okafor, Jamie Liu, Tom Bradley, Aditi Sharma, Ravi Krishnan, Nikhil Iyer
Absent (2): Emma Walsh (PTO), Oliver Hughes (on-call handoff)

## Agenda

1. Q1 standup attendance and time-cost data (Maya, 10 min)
2. Proposed async-first format (Maya, 15 min)
3. Trial scope, success metrics, concerns (group, 15 min)
4. Decisions and owners (5 min)

## Decisions

- **D1.** The team will run a 30-day async standup trial starting Monday May 19. The 9am Pacific sync slot is paused for the trial duration.
- **D2.** Daily updates are posted in #team-standup by 10am local time using the three-field template: Shipped / In progress / Blocked or at risk.
- **D3.** The Thursday 9am Pacific slot is repurposed as a 60-minute working session (not status). Agenda required, posted Wednesday EOD.
- **D4.** On-call engineer owns daily channel triage by 9am Pacific and 30-minute blocker response during business hours.
- **D5.** Trial review checkpoints are day 15 (lightweight pulse) and day 30 (go / no-go / extend).

## Discussion summary

Maya presented Q1 data: India attendance 3.2/5 vs US 4.6/5, 14-min average standup with ~4 min driving any action, and three documented duplicate-work incidents that a searchable record would have caught.

Aditi and Nikhil supported the change and noted 9:30pm IST is particularly hard on evenings with family commitments. Devon raised concern that async loses the social moment that makes the team feel like a team. Maya acknowledged this is the strongest argument against and is the reason the Thursday session is being added rather than the time fully reclaimed.

Tom asked what happens if someone consistently misses async posts. Group agreed the on-call engineer pings missing posters at 11am local, and persistent gaps escalate to Maya at day 7. Sara asked about PTO and on-call days - resolved by adding an explicit "out" or "on-call, no update" line, captured in the reference doc.

Jamie raised a tooling question (Geekbot vs Slack pinned template) - group decided to start with the pinned template and revisit at day 30 if friction warrants tooling spend.

## Action items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| A1 | Pin standup template to #team-standup with field definitions | Priya | 2026-05-16 |
| A2 | Send trial kickoff email to eng-platform | Maya | 2026-05-15 |
| A3 | Draft standup format reference doc (PTO, on-call, partial weeks) | Priya | 2026-05-16 |
| A4 | Schedule Thursday working session series, cancel daily 9am Pacific | Maya | 2026-05-15 |
| A5 | Brief on-call rotation on daily triage responsibility | Tom | 2026-05-18 |
| A6 | Set up day-15 pulse survey (3 questions) | Priya | 2026-05-29 |
| A7 | Day-30 review meeting on calendar | Maya | 2026-05-15 |

## Open questions

- **OQ1.** Do we need a separate channel for blockers or does #team-standup with @mentions work? Revisit at day 15 if signal-to-noise is a problem.
- **OQ2.** How do we surface async updates to stakeholders outside the team (PM, design)? Owner: Maya, by day 15.

## Next meeting

Day-15 async pulse review, Friday 2026-05-29, async in thread (no live meeting).
