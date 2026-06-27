---
entry_id: runbook
axis: format
topic_slug: morning-routine
topic_label: Designing a sustainable morning routine
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Runbook: Morning Routine - Weekday First Hour

## Overview

Execute the four-module morning routine (water, light, movement, planning) in the 6:30am-7:30am window on weekdays, triggered each morning when the alarm sounds.

## Prerequisites

- [ ] Glass of water (500ml) placed on the nightstand before going to sleep
- [ ] Phone moved to the kitchen, face down, plugged in, before going to sleep
- [ ] Paper notebook and pen placed at the planning spot (not the bedroom)
- [ ] Wake time is 6:30am or earlier
- [ ] No family emergency requiring immediate attention

## Procedure

1. **Drink the water on the nightstand**
   Reach for the pre-staged glass. Drink all 500ml before standing up.
   Expected output: Glass is empty. You are upright.

2. **Move to the light station**
   Go to the back door or the largest available window. Step outside or open the window to natural light.
   Expected output: You are at natural light. No screen is in your hand.

3. **Complete 10 minutes of light exposure**
   Stand or sit. Do not pick up the phone. No screen of any kind counts as light exposure.
   Expected output: 10 minutes have elapsed. You have not checked Slack or email.

4. **Complete 15 minutes of movement**
   Choose one option: walk around the block, run the bodyweight sequence in `protocol/movement.md`, or do a full stretch session. Heart rate up, not crushing.
   Expected output: 15 minutes have elapsed. Light sweat or elevated breathing. Movement module complete.

5. **Sit down at the planning station with the paper notebook**
   Carry the notebook and pen to a seated spot away from the phone. Do not retrieve the phone from the kitchen first.
   Expected output: Notebook is open. Pen is in hand. No screen is visible.

6. **Write the top three for the day**
   List the three tasks that, if completed today, would make the day count. One sentence each. Do not open any digital tool.
   Expected output: Three items written by hand. Planning module complete.

7. **Retrieve the phone from the kitchen**
   Walk to the kitchen and pick up the phone. Check the clock before checking any app.
   Expected output: Time reads 7:30am or later. All four modules ran before first screen contact.

## Verification

Confirm all four modules ran in the correct order: water before light, light before movement, movement before planning, planning before phone. A completed morning requires all four steps in that sequence with no shortcuts.

Record the result in `log/days.csv` - the "completed" field should read "yes". If any step was skipped, mark "partial" and note which steps ran in the "which_steps_skipped" column.

## Rollback

Rollback is not applicable for time already elapsed. If you wake late and the 7:30am family window is compressed, run the following partial-completion path:

1. Start from the first step not yet completed.
2. Work through remaining steps in order until 7:30am.
3. Mark the day "partial" in `log/days.csv` and note which steps completed.

Do not skip to a later step to compensate for a missed earlier one. Order matters.

If the full 6:30-7:30am window is gone (illness, travel, family emergency), mark "no" in the completed column. Do not attempt a makeup routine at another time of day. Resume on the next scheduled weekday morning.

## Escalation

If completion rate falls below 70 percent of weekdays over any two-week period, contact the accountability partner before modifying the protocol design. Address the root cause of the misses first; do not revise the design as a substitute for diagnosing why it is failing.

If family friction arises - for example, if the spouse's 6:45-7:15am coffee window begins conflicting with the light or movement steps - renegotiate those constraints directly rather than reshaping the routine around them. Log the friction in the weekly retro in `log/retros/` before deciding what to change.

Protocol review date: 2026-06-14 per ADR-001. If two consecutive weeks show below 70 percent completion before that date, escalate to an accountability partner session before Month 2 begins.
