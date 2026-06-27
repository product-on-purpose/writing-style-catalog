---
entry_id: design-doc
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Async Standup System Design Document

## Status

Accepted

## Problem

The engineering team (11 engineers, 4 timezones) runs a synchronous daily standup at 9am Pacific. This format fails on three fronts.

**Timezone asymmetry.** 9am Pacific is 9:30pm IST. The three India-based engineers averaged 3.2 out of 5 standup appearances per week in Q1, against 4.6 for US-based engineers. The gap is not a performance issue; the schedule is structurally unfair.

**No persistence.** Status exchanged verbally disappears when the call ends. We documented three Q1 incidents where an engineer spent over an hour on a problem already surfaced and resolved in a previous standup. The meeting produces no searchable record.

**Low signal-to-noise ratio.** The standup averages 14 minutes. Roughly 4 minutes drives an action - a blocker raised, a dependency flagged, a context shared. The remaining 10 minutes is status nobody needed to respond to.

Constraints shaping the solution:

- Cannot require attendance outside normal working hours for any engineer
- Must preserve the coordination value of the standup: blocker detection and dependency surfacing
- Must produce a persistent, searchable record
- Tooling must stay within Slack; no new paid tools unless value clearly exceeds cost and complexity

## Proposed Design

### Post schema

Each engineer posts one message to `#team-standup` by 10am their local time. The message follows a three-field template:

```
Shipped:
  - <what completed since last post>

In progress:
  - <current focus>

Blocked or at risk:
  - <what is stuck and who or what resolves it, @mentioning the responsible party>
```

Empty fields carry the literal value "nothing today." Fields are not optional - an absent field is ambiguous between "I forgot" and "nothing to report." The 10am local cutoff creates a clear posting window that gives all four timezones time to post before the Pacific-based on-call scan runs.

### Channel architecture

One channel: `#team-standup`. A pinned message carries the template and two exemplar posts (one from a high-load day, one from a quiet day). No bots. No automated summaries. The channel is a log, not an inbox.

The `/standup` Slack message shortcut pre-fills the template into the compose box. It is optional convenience, not the mechanism - typing the three headers manually is equally valid.

### On-call triage role

The on-call engineer scans `#team-standup` once, between 10am and 11am Pacific. Their responsibility is narrow:

1. Confirm every engineer has posted; DM late posters
2. Ensure every `@mention` in a Blocked field has received a substantive reply within 30 minutes of the scan

The on-call is not a summarizer. They do not re-broadcast channel contents. Thread replies are the response surface; a new top-level message is only appropriate for a team-wide blocker affecting multiple people.

This role replaces the meeting facilitation slot already on the on-call rotation.

### Thursday working session

The 60-minute weekly slot at 8am Pacific / 8:30pm IST replaces the five daily sync standup slots. Agenda lives in `docs/thursday-agenda.md`, maintained by the engineering manager. If the doc has no items by Wednesday 5pm Pacific, the session is cancelled for that week.

This is not a standup in async clothing. It is reserved for discussion that requires real-time exchange: design review, cross-team dependency negotiation, or issues that carry nuance the three-field template cannot hold. Status reporting is not a valid agenda item.

### Data flow

```
Engineer post (by 10am local)
  --> #team-standup (persistent, searchable)
      --> On-call scan (10am-11am Pacific)
          --> @mention reply (SLA: 30 min during business hours)
          --> Thursday agenda item (if discussion needed but not urgent)
```

## Alternatives Considered

**Geekbot or equivalent async standup bot.** Rejected. Geekbot solves the scheduling problem and adds structure, but it introduces a paid tool, a data store outside Slack's native search, and vendor dependency for a process the Slack-native approach handles. Cost and complexity are not justified given functional parity.

**Rotating the meeting time.** Rejected. A rotating time makes the schedule equitable on average but does not create information persistence. It also adds coordination overhead and removes engineers' ability to hold a stable recurring block for deep work, since the standup slot is always moving. Solves one of three problems; the other two remain.

**Eliminating the standup entirely.** Rejected. The coordination value - blocker surfacing, dependency flagging, context sharing - is real, even if the signal is buried in noise under the current format. Removing the standup removes the mechanism without replacing the value.

**Moving standup to 12pm Pacific.** Rejected. 12pm Pacific is 12:30am IST the next day, shifting the timezone burden from late evening to late night for India. Worse, not better.

## Risks and Open Questions

**Post quality drift.** If engineers write long-form updates instead of three-bullet summaries, the channel becomes slower to scan and on-call triage load increases. Mitigation: pin two exemplar posts from day one; set an explicit expectation in the process playbook that each field should be readable in under 15 seconds.

**On-call triage load.** The target is 10 minutes per morning for the channel scan. If blockers surface earlier and louder than they did in the sync model, actual time could run higher. If the role consistently exceeds 20 minutes, consider splitting triage responsibility by timezone cluster.

**Participation cliff.** The format's coordination value scales with participation. If one or two engineers consistently miss the cutoff, the channel becomes unreliable as a team signal. Mitigation: on-call DMs late posters; the 30-day trial retro surfaces participation data to catch this early.

**Social cohesion.** The sync standup provided a daily shared moment that the async format does not replicate. The Thursday session is a partial substitute. This is a real trade-off accepted because the equity and persistence gains are larger, but qualitative feedback in the trial retro should track it explicitly.

**Open question: cutoff enforcement.** The 10am local cutoff is a norm, not a hard technical constraint. Whether to add a bot reminder at 9:45am local is deferred until after the 30-day trial produces data on late-posting patterns.

**Open question: holiday handling.** Behavior on local public holidays (UK bank holidays, Indian national holidays, US federal holidays) is not yet specified. Deferred to trial retro.
