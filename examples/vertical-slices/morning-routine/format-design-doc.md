---
entry_id: design-doc
axis: format
topic_slug: morning-routine
topic_label: Designing a sustainable morning routine
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Morning Routine v3.0 - Design Document

## Status

In Review

## Problem

Two prior attempts at an intentional morning routine (v1.0 and v2.0) failed within a week each. Both failures trace to the same root cause: I removed a behavior (phone scrolling) without substituting a replacement sequence. The vacuum collapsed within days. This document specifies the implementation for v3.0, designed to be specific enough that my accountability partner can evaluate it before I start and that I cannot quietly renegotiate terms once I am tired.

**Constraints shaping the solution space:**

- **Time window:** 6:30am to 7:30am on weekdays. Family obligations begin at 7:30am (breakfast, school dropoff). This is the only reliably discretionary hour.
- **Device dependency:** The phone is the primary failure mechanism. Any design that leaves the phone in the bedroom will reproduce the v1.0 and v2.0 failure mode: I will reach for it before my feet hit the floor.
- **Sequence rigidity:** I cannot make good decisions before 7am. A fixed ordered sequence, not a menu of options, is required. Decision fatigue at 6:31am is a known failure mode in prior versions.
- **Complexity ceiling:** Prior attempts added modules until the morning felt like a second job. The total design must fit inside 60 minutes with buffer remaining for the unplannable parts of a family morning.

## Proposed Design

The routine is a four-module pipeline running in fixed order. Modules do not branch and do not unlock each other; if a module is skipped, the remaining modules still run from where the schedule permits. The sequence is: Water, Light, Movement, Planning.

### Module 1: Water

**Duration:** 5 minutes (absorbed into waking transition)

**Specification:** 500ml water consumed within 5 minutes of waking. A glass is pre-staged on the nightstand the night before as part of the shutdown ritual (see Risks). Coffee does not substitute and follows later.

**Role in pipeline:** Functions as a contextual trigger. Picking up the glass signals to me that the protocol is running. This is the cheapest module and also the one that sets the others in motion.

### Module 2: Light

**Duration:** 10 minutes

**Specification:** Outdoors preferred (back door, front step). Fallback when outdoor exposure is genuinely blocked by weather: stand at the largest available window with curtains fully open. Headphones permitted. Screens do not substitute as a light source.

**Role in pipeline:** Early light exposure is the input that anchors the rest of the sequence. The ordering hypothesis (light before movement) is the implementation decision most worth validating empirically; see Open Questions.

### Module 3: Movement

**Duration:** 15 minutes

**Specification:** Heart rate elevated, not crushed. Acceptable forms: 15-minute walk (default), bodyweight circuit defined in `protocol/movement.md`, or a stretch-only session when recovery is a factor. A gym session does not satisfy this slot - it exceeds the time budget and front-loads decision overhead. The bar is "body is moving," not "workout complete."

**Role in pipeline:** Runs after light to use the early-morning cortisol window without competing with Module 2. Running it before light inverts the sequencing rationale.

### Module 4: Planning

**Duration:** 10 minutes

**Specification:** Paper and pen only. Output: three items I intend to close today, written in a dated notebook entry. The phone is not present for this module. A log row for `log/days.csv` is filled in on the same page at the end of this step and transcribed to the file at week's end.

**Role in pipeline:** Planning is the only cognitively demanding module. Placing it last means 25-30 minutes of lower-demand activity have reduced sleep inertia before I try to set priorities for the day.

### Enforcement mechanism: phone-in-kitchen rule

The phone is plugged in on the kitchen counter, face down, before going to bed each weeknight. It is not retrieved until Module 4 is complete. The phone is not brought to the bedroom.

This is the load-bearing constraint for the entire protocol. Without a hard location rule, the phone becomes accessible at the moment of lowest willpower (waking). Prior versions relied on willpower; this version relies on physical separation.

### Time budget

| Module | Duration | Cumulative |
|--------|----------|------------|
| Water | 5 min | 0:05 |
| Light | 10 min | 0:15 |
| Movement | 15 min | 0:30 |
| Planning | 10 min | 0:40 |
| Buffer | 20 min | 1:00 |

The 20-minute buffer covers getting dressed, making coffee, and whatever the morning actually contains. It is not a module. Do not schedule it.

### Logging schema

Each weekday morning appended to `log/days.csv`:

```
date, wake_time, completed (yes/no/partial), steps_skipped, one_word_mood, notes
```

Completion criterion: all four modules run, in order, on the same morning. "Partial" is not a passing grade for the 30-day success metric. It logs what happened without inflating the completion count.

## Alternatives Considered

**Earlier wake time (5:30am instead of 6:30am).** Rejected. Fixing the content of the existing hour before adding a new one is the correct sequencing. Adding 60 minutes while the current hour is broken is premature optimization. Revisit only after a successful 30-day run at 6:30am.

**Habit-tracking app.** Rejected. Adds a screen to a protocol whose primary leverage is screen removal. The paper log is slower and less convenient; that is intentional. Moving to a digital log would reintroduce the phone into the planning step.

**Variable module menu (pick any three in any order).** Rejected. Prior v2.0 design allowed flexible ordering; Module 3 (movement) was consistently skipped. Choice at 6:31am is the failure mode, not a feature.

**Meditation substituted for planning.** Considered as a Module 4 variant. Rejected for v3.0 because the planning output (three items, written down) is directly testable. If I cannot measure completion, I cannot review the protocol at 30 days. Meditation may be added as an optional extension after the first 30-day review.

**90-day commitment frame.** Rejected based on direct prior evidence: tried at this duration and quit on day 11. A 30-day frame with a formal review point is the minimum viable commitment. Extend only after the first 30-day completion.

## Risks and Open Questions

**Risk: shutdown ritual is an undocumented dependency.** The phone-in-kitchen rule and the pre-staged water glass both require a consistent shutdown ritual the night before. If the shutdown ritual is skipped (late night, travel, family exception), the morning protocol launches without its setup. Mitigation: document the shutdown ritual before day 1 and treat it as part of the protocol. Current bedtime is approximately 11:30pm; the protocol likely requires compressing that to 10:30pm to make 6:30am viable without sleep debt.

**Risk: family friction.** My spouse's morning coffee window runs 6:45 to 7:15am. Modules 2 and 3 overlap with that window and involve leaving and re-entering the house. I have not confirmed that this works for the household. This needs a direct conversation before launch. An assumption of tolerance is not a mitigation.

**Risk: West Coast Slack messages missed.** Colleagues on West Coast time send messages that arrive before 7:30am. Risk is accepted: urgent issues can reach me by phone call. The phone is in the kitchen and can receive calls even during the protocol.

**Open question: weekends.** The protocol is specified for weekdays. Family dynamics on weekends differ (no school dropoff, no fixed 9am start). Running the same protocol on weekends may be correct; a lighter variant may be better. Decision deferred to Week 2 based on what the first weekend actually reveals.

**Open question: travel variant.** Module 2 (light) and Module 3 (movement) degrade in hotel environments. A travel variant needs to be specified before the first travel day in Month 1, not improvised in a hotel room at 6:45am.

**Open question: light-before-movement ordering hypothesis.** The current sequencing (light before movement) is based on reasoning about early-morning cortisol timing. It has not been tested against movement-first. If Month 1 completion is high enough to control the variable, this is the ordering hypothesis most worth testing empirically in Month 2.

## Appendix

### Prior version summary

| Version | Period | Duration | Failure mode |
|---------|--------|----------|-------------|
| v1.0 | 2025-10 | 4 days | Phone removal with no replacement; vacuum collapsed |
| v2.0 | 2025-12 | 6 days | Journaling added but no fixed sequence; movement skipped consistently |

### Accountability partner handoff

This document is the artifact shared with the accountability partner before day 1. Agreed escalation criterion: if 30-day completion falls below 70 percent of weekdays, schedule a session to diagnose before making any changes to the design.
