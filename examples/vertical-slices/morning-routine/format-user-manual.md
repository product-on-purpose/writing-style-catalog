---
entry_id: user-manual
axis: format
topic_slug: morning-routine
topic_label: Designing a sustainable morning routine
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Morning Protocol v3.0 User Manual

Reference for the four-module weekday morning sequence (water, light, movement, planning), the phone lockout rule, the logging system, and the current travel and weekend variants.

## Table of Contents

- [Getting Started](#getting-started)
- [Water Module](#water-module)
- [Light Module](#light-module)
- [Movement Module](#movement-module)
- [Planning Module](#planning-module)
- [Phone Lockout](#phone-lockout)
- [Logging Your Mornings](#logging-your-mornings)
- [Weekend and Travel Variants](#weekend-and-travel-variants)
- [Troubleshooting](#troubleshooting)
- [Reference](#reference)

## Getting Started

System requirements:

- A wake time that leaves a real gap before your first fixed obligation (family breakfast, school dropoff, or work start). The current target is 6:15am, with family obligations starting at 7:30am.
- A second location for the phone overnight, away from the bedroom (see Phone Lockout).
- A paper notebook and pen, staged separately from any device.
- Someone outside the routine (your spouse, an accountability partner, or both) who knows the commitment window.

First-session setup (do this once, the night before day one):

1. Fill a glass with 500ml of water and place it on the nightstand.
2. Move the phone to its overnight location, plugged in.
3. Set the paper notebook and pen at the planning spot.
4. Tell your accountability partner the start date and the commitment window.
5. If you share a household, confirm any schedule overlap and agree on a boundary before day one, not after friction has already built up.

After first-session setup, the protocol runs the same way every weekday morning. Jump to whichever module you need.

## Water Module

Rehydrates after several hours without intake and makes the day's first action a chosen one instead of a reach for the phone. Reach for this module first, immediately on waking.

Steps:

1. Reach for the glass staged on the nightstand the night before.
2. Drink the full glass before standing up.
3. Proceed to the Light module.

Options / Parameters:

- Volume: 500ml, room temperature.
- Staging location: nightstand is standard. A kitchen counter works if it can be reached without passing the phone's overnight location.

Notes:

- No glass staged: default to tap water in the kitchen rather than skipping the module.
- No minimum duration. Completion matters, pace does not.

## Light Module

Provides early light exposure to support alertness. Reach for this module second, right after Water.

Steps:

1. Move to an outdoor space or the largest window in the house.
2. Face the light source, standing or seated.
3. Hold the full duration with no screen in hand.
4. Proceed to the Movement module.

Options / Parameters:

- Duration: 10 minutes.
- Light source: outdoors preferred, a large window is an acceptable substitute.
- Low-light fallback: blinds fully open at the largest available window, plus a supplemental lamp if one is available.

Notes:

- A screen does not count as light exposure at any brightness setting.
- Any remaining water can be finished during this module.

## Movement Module

Raises heart rate and mobilizes the body after a night of stillness. Reach for this module third, after Light.

Steps:

1. Choose a walk, a stretch sequence, or the bodyweight routine.
2. For the bodyweight routine, follow the sequence in `protocol/movement.md`.
3. Sustain the activity at a light-to-moderate pace for the full duration.
4. Proceed to the Planning module.

Options / Parameters:

- Duration: 15 minutes.
- Intensity: talk-pace. This module is a wake-up signal, not a workout.
- Modality: walk, stretch, or bodyweight, interchangeable day to day.

Notes:

- No equipment required for any modality.
- Short on time: compress the duration rather than skip the module. See Troubleshooting.

## Planning Module

Converts the day's intentions into a written shortlist before any digital tool opens. Reach for this module last, immediately before the Phone Lockout ends.

Steps:

1. Carry the notebook and pen to a seated spot away from the phone's overnight location.
2. Write the top three tasks for the day, one line each.
3. Optionally note what to protect time against or what to explicitly skip today.
4. Add the day's log row (see Logging Your Mornings) on the same page.
5. Retrieve the phone. The lockout ends here.

Options / Parameters:

- Duration: 10 minutes, hard cap.
- Tool: paper and pen only.
- Location: any seated, stationary surface out of reach of the phone's overnight location.

Notes:

- Do not process email or messages in this module once the phone is back in hand. Planning ends before the phone begins.
- Route weekly or longer-horizon planning to a separate evening session instead of extending this module past ten minutes.

## Phone Lockout

Governs all four modules: the phone stays out of reach until Planning is logged. Set up the night before; applies automatically through the rest of the sequence.

Steps:

1. The night before, move the phone to its overnight location: kitchen, plugged in, face down.
2. Leave it there through Water, Light, and Movement.
3. Retrieve it only after Planning is logged.

Options / Parameters:

- Overnight location: kitchen is standard. Any room outside the bedroom and outside the planning spot works, provided reaching it takes a deliberate walk.
- Alarm handling: if the phone is also the alarm, use a separate alarm device or set the alarm before relocating the phone.

Notes:

- A location rule, not a willpower rule. The module works because the device is out of reach.
- Reaching for the phone before Planning is logged means the overnight location is not far enough away, not that more resolve is needed. See Troubleshooting.

## Logging Your Mornings

Turns four modules into data you can review at the end of the week. Runs inside Planning, not as a separate task.

Steps:

1. During Planning, add one row to `log/days.csv` on the same paper page.
2. Record date, wake time, completed status, which modules were skipped, one-word mood, and optional notes.
3. At the end of the week, transcribe the week's rows into the file.
4. Write a short retro in `log/retros/` summarizing the week.

Options / Parameters:

- Completed status: `yes` (all four modules, in order, no shortcuts), `partial` (a module skipped or reordered), or `no` (no modules ran).
- Mood field: one word, free choice. Used for pattern-spotting, not scored.

Notes:

- Logging inside Planning, rather than as a separate task, is what keeps it from becoming its own thing to skip.
- Log partial and missed days as accurately as completed ones. The 30-day review depends on it.

## Weekend and Travel Variants

Covers the two conditions the standard sequence does not assume: an unfamiliar environment, or a non-workday.

### Travel

Use when away from your regular environment.

Steps:

1. Run Water and Planning. Treat Light and Movement as optional.
2. Substitute a hotel window or hallway window for Light if attempted.
3. Log the day `partial` if fewer than four modules ran, `no` if none ran.

Options / Parameters:

- Scope: Water and Planning are the two modules judged essential enough to preserve away from home.

Notes:

- Exists because the standard sequence assumes a familiar environment. Do not improvise Movement in an unfamiliar space without a plan already in place.

### Weekend

Use on Saturdays and Sundays.

Steps:

1. Run the standard sequence unchanged. No dedicated weekend variant exists yet.

Notes:

- An open question, not a settled rule. The current default is the standard sequence. See Troubleshooting.

## Troubleshooting

**You reach for the phone before Planning is logged.** The overnight location is not far enough from reach. Move it to a different room, not just a different surface in the same room.

**You complete three of four modules and call it done.** Log the day `partial` and note which module dropped. Do not redefine `completed` before the 30-day review; a pattern in the notes will show where the friction actually is.

**Travel breaks the sequence.** Expected. Use the travel variant (Water and Planning only) instead of attempting the full sequence away from home, and log the day `partial`.

**One weekday is consistently the hardest.** Check the mood and skipped-module fields in `log/days.csv` for a pattern by day of week. A cluster on one day often traces back to the day before.

**Weekend practice feels unresolved.** Known open item, not a bug. The current default is the standard sequence; revisit at the next scheduled review instead of deciding ad hoc on a given Saturday.

**Completion rate is trending down.** If weekday completion falls below 70 percent over two consecutive weeks, raise it with your accountability partner before changing the protocol design.

## Reference

### Module summary

| Module | Duration | Tool | Phone status |
|---|---|---|---|
| Water | Under 1 minute | Glass, staged the night before | Locked out |
| Light | 10 minutes | Outdoors or window | Locked out |
| Movement | 15 minutes | None required | Locked out |
| Planning | 10 minutes, hard cap | Paper notebook, pen | Locked out until logged |

### Glossary

- **Completed:** all four modules ran, in order, with no shortcuts.
- **Partial:** at least one module skipped or run out of order, noted in the log.
- **Lockout:** the phone's overnight location and the rule that it stays there until Planning is logged.
- **Review:** the scheduled checkpoint where the log is examined before any redesign.

### Files and directories

- `protocol/MANUAL.md` - this document
- `protocol/movement.md` - the bodyweight sequence referenced in the Movement module
- `log/days.csv` - one row per morning
- `log/retros/` - weekly retro notes
- `notes/` - source material that shaped the protocol

### Review checkpoints

- 30-day review: end of the current commitment window.
- Escalation threshold: below 70 percent weekday completion across two consecutive weeks.
