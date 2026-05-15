---
entry_id: technical-reference
axis: format
topic_slug: morning-routine
topic_label: How to start a morning routine
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Morning Routine: Module Reference

A reference for the four composable modules of the standard weekday morning routine. Each module has defined inputs, outputs, timing, and failure modes. Modules execute sequentially in the order listed unless otherwise noted.

## 1. Overview

The routine is decomposed into four modules executed between wake time (T+0) and end-of-window (T+60 minutes). Total elapsed time is approximately 45 minutes; the remaining 15 minutes is buffer for transitions and interruptions.

### 1.1 Module summary

| # | Module | Duration | Window | Required |
|---|---|---|---|---|
| 1 | Water | 1 min | T+0 to T+5 | Yes |
| 2 | Light | 10 min | T+5 to T+20 | Yes |
| 3 | Movement | 15 min | T+20 to T+40 | Yes |
| 4 | Planning | 10 min | T+40 to T+55 | Yes |

## 2. Module: Water

### 2.1 Purpose

Establish the first physical action of the day as a chosen one. Secondary benefit: rehydration after 7-8 hours without intake.

### 2.2 Inputs

| Input | Specification |
|---|---|
| Volume | 8 oz (240 ml) |
| Temperature | Room temperature |
| Location | Bedside or kitchen, prepared the night before |
| Preconditions | Eyes open, feet on floor |

### 2.3 Outputs

- One glass consumed
- Transition signal to module 2

### 2.4 Failure modes

- **No water prepared:** Default to tap water in kitchen. Do not skip.
- **Forgot until after phone-check:** Routine has already failed at module 0 (phone discipline). Reset tomorrow.

## 3. Module: Light

### 3.1 Purpose

Provide bright-light exposure within 30 minutes of waking to support circadian alignment and morning alertness.

### 3.2 Inputs

| Input | Specification |
|---|---|
| Duration | 10 minutes |
| Light source | Outdoor daylight preferred; large window acceptable |
| Posture | Standing or seated; eyes open |
| Concurrent activity | Optional: water sips, slow breathing |

### 3.3 Outputs

- 10 minutes of light exposure completed
- Transition signal to module 3

### 3.4 Fallback variants

| Condition | Fallback |
|---|---|
| Rain or cold | Largest window in house, blinds fully open |
| Pre-dawn (winter) | Bright indoor lighting + 10,000 lux lamp if available |
| Travel | Hotel window or hallway window |

## 4. Module: Movement

### 4.1 Purpose

Raise core body temperature, mobilize joints after sleep, and generate a modest cardiovascular signal to wake the system.

### 4.2 Inputs

| Input | Specification |
|---|---|
| Duration | 15 minutes |
| Intensity | Low to moderate (talk pace) |
| Modality | Walk, stretching sequence, or bodyweight |
| Equipment | None required |

### 4.3 Outputs

- 15 minutes of movement logged (mental note, not tracked)
- Transition signal to module 4

### 4.4 Failure modes

- **Injury or illness:** Substitute with 10 minutes of stretching or gentle mobility only.
- **Time pressure (running late):** Compress to 5 minutes; do not skip entirely.

## 5. Module: Planning

### 5.1 Purpose

Convert vague morning intentions into a concrete written shortlist before any digital tool is opened.

### 5.2 Inputs

| Input | Specification |
|---|---|
| Duration | 10 minutes (hard cap) |
| Tool | Paper notebook, pen |
| Location | Desk, kitchen table, or stationary surface |
| Prerequisites | Modules 1-3 completed |

### 5.3 Outputs

| Output | Format |
|---|---|
| Today's top three priorities | Three bullet lines |
| Today's protection list | What to defend time against |
| Today's drop list | What to explicitly not do |

### 5.4 Constraints

- No phone, laptop, or tablet during this module
- Do not extend past 10 minutes; route weekly planning to Sunday evening block
- Do not use this module to process email or messages

## 6. Sequencing rules

- Modules execute in numerical order (1 -> 2 -> 3 -> 4).
- Modules 2 and 3 MAY be combined (walking outside satisfies both light and movement). When combined, allocate the maximum of the two durations.
- An interrupted module resumes at the next module after the interruption ends; the interrupted module is not retried.

## 7. End state

At T+60, the routine is complete. Phone re-enters the workflow. Daily shortlist is in hand. Work day begins at T+150 (9:00am).

## 8. Variants

| Variant | Modules | Total time | Use case |
|---|---|---|---|
| Standard | 1, 2, 3, 4 | 45 min | Weekday at home |
| Compressed | 1, 4 | 6 min | Travel days |
| Recovery | 1, 2, 4 | 21 min | Illness or injury |
| Weekend (TBD) | Not yet specified | - | Future spec |
