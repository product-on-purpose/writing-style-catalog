---
entry_id: prd
axis: format
topic_slug: morning-routine
topic_label: How to start a morning routine
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# PRD: Morning Routine v1

- Author: Me
- Status: Draft
- Last updated: 2026-05-14
- Target launch: 2026-05-19 (Monday)

## 1. Problem Statement

The current morning experience (6:30am - 7:30am) is unstructured and reactive. The first action upon waking is phone-checking, which consumes 40-50 minutes and produces measurable downstream effects: elevated baseline stress, slower work start, and a recurring sense of having begun the day in a deficit. Three prior unstructured attempts to "use the phone less in the morning" have failed within a week, indicating the problem is not motivational but architectural.

## 2. Goals

- G1: Establish a repeatable, low-friction routine for the 6:30am - 7:30am window on weekdays.
- G2: Eliminate phone use during this window.
- G3: Arrive at the 9am work start with a written daily plan already in hand.
- G4: Be sustainable for at least 30 consecutive weekdays without willpower spikes.

## 3. Non-Goals

- NG1: Not optimizing weekends in v1. Weekends have different constraints (children, social schedule) and warrant a separate spec.
- NG2: Not solving sleep. Bedtime drift is an upstream issue; will be addressed in a future cycle.
- NG3: Not adopting a meditation practice in v1. Out of scope to avoid scope creep on a fragile habit.
- NG4: Not tracking metrics in an app. Paper-only by design.

## 4. Success Metrics

| Metric | Target | Measurement |
|---|---|---|
| Weekday adherence | >= 80% (4 of 5 weekdays per week) | Paper checklist, weekly review |
| Phone-touch before 7:30am | 0 times per weekday | Self-report, honesty system |
| Daily plan completion before 9am | 100% of weekdays | Notebook timestamp |
| Self-rated morning calm (1-5) | >= 3.5 weekly average | One-line journal entry |

## 5. Requirements

### 5.1 Functional

- R1: Routine MUST execute in this order: water, light, movement, planning.
- R2: Routine MUST complete within 60 minutes of waking.
- R3: Phone MUST remain in the kitchen, plugged in, face down, until 7:30am.
- R4: Planning step MUST produce a written daily shortlist in a designated paper notebook.

### 5.2 Non-functional

- R5: Routine MUST be executable in under 30 seconds of decision-making (no daily re-planning of the routine itself).
- R6: Routine MUST tolerate one missed module per day without invalidating the rest.
- R7: Routine MUST function in winter (light module has a window fallback for cold or dark mornings).

## 6. User Story

> As a working adult who currently begins the day in a reactive state, I want a predefined sequence of four small actions in my first hour so that I arrive at the work day having already chosen how I show up.

## 7. Open Questions

- OQ1: What happens when a child wakes early and interrupts the routine? Default behavior: resume at the next module after the interruption ends. Needs trial.
- OQ2: Should travel days use a compressed version (e.g., water + planning only) or be exempt? Lean toward compressed.
- OQ3: Is 10 minutes of planning enough on heavy-meeting days? Possibly extend to 15 on Mondays.

## 8. Out of Scope (for future versions)

- Evening routine design (v2)
- Weekend variant (v2)
- Family-coordinated morning (v3)

## 9. Approval

Self-approved. Re-review in 30 days.
