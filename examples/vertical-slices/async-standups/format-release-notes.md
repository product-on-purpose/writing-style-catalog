---
entry_id: release-notes
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# team-standup v2.0

**Async-first standups for a distributed team**

## What's new

- **Async daily updates in #team-standup:** You post to the channel by 10am your local time using the three-field template. No call. No round-robin. No status you have to repeat to people who already knew.

- **/standup Slack shortcut:** Type `/standup` in any Slack message box to load the three-field template pre-filled with the Shipped / In progress / Blocked or at risk fields. The shortcut is also pinned in the channel description.

- **Thursday working session:** A 60-minute real-time session at 8am Pacific / 8:30pm IST replaces the former sync standup slot. Use it for discussions that require live exchange. Agenda lives in `docs/thursday-agenda.md`. If nothing needs real-time discussion, the session cancels by Wednesday 5pm Pacific.

- **On-call triage role:** The on-call engineer reads `#team-standup` between 10am and 11am Pacific each day and makes sure every @mention in a blocked item gets a substantive reply within the workday.

## Improvements

- **IST-compatible schedule:** Engineers in India can participate at 10am IST rather than 9:30pm. The format applies the same participation standard to every timezone.

- **Blockers route directly:** When you flag a blocker with an @mention, the person who can resolve it sees it in their Slack notifications immediately rather than waiting until the next meeting window.

- **Persistent, searchable history:** Status updates live in Slack. Prior blockers, resolved dependencies, and completed work are searchable after the update window closes. The sync standup produced no persistent record.

## Fixes

- **Low-signal meeting time recovered:** The 14-minute daily call averaged roughly 4 minutes of content that changed anyone's behavior. The remaining time was status that required no response. That time is now yours.

## Deprecations and breaking changes

- **Sync standup removed from calendar:** The recurring 9am Pacific meeting is cancelled. Remove it from your calendar. The Thursday working session is the only team-wide synchronous slot going forward.

## Known issues

- **Post length:** The three-field format is meant to be skimmed in under 60 seconds per teammate. If you find yourself writing paragraphs, trim to bullets. Pinned examples in `#team-standup` show the target length.

---

This release runs on a 30-day trial. Drop feedback in `docs/trial-retro.md` at any point. The Day 30 retro will decide whether v2.0 becomes permanent or reverts to the sync format.
