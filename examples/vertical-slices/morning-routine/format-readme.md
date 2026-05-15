---
entry_id: readme
axis: format
topic_slug: morning-routine
topic_label: How to start a morning routine
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# morning-experiment

A personal repo where I track my attempt at an intentional first hour of the day. Public because accountability works better when someone might look.

## Why this exists

I wake around 6:30. I check my phone before my feet hit the floor. I am reactive by 7am, depleted by 2pm, and asleep on the couch by 9. I have a family, a 9am-start job, and finite energy. I want to find out what happens if the first hour belongs to me, not to whatever Slack thinks is urgent.

## The protocol

For 30 days, the first hour after waking follows the same four-step sequence. No phone until step 4.

1. **Water.** 500ml within 5 minutes of waking. Glass sits on the nightstand the night before.
2. **Light.** 10 minutes outside or by an open window. No screen counts as light.
3. **Movement.** 15 minutes. Walk, stretch, or follow the bodyweight routine in `protocol/movement.md`. Heart rate up, not crushing.
4. **Planning.** 10 minutes with paper and pen. Top three for the day. Then, and only then, phone.

The other 20 minutes are buffer for getting dressed, making coffee, and whatever the morning actually contains.

## How to track

Each morning gets one row in `log/days.csv`. Columns:

- date
- wake_time
- completed (yes / no / partial)
- which_steps_skipped
- one_word_mood
- notes

I do the log entry as part of step 4, on the same paper page, then transcribe at the end of the week.

## Results so far

| Period | Completed mornings | Average wake | One-line takeaway |
|--------|-------------------|--------------|-------------------|
| Week 1 | 4 of 7 | 6:42 | Phone is the hardest one to skip. |
| Week 2 | 6 of 7 | 6:28 | Light before movement matters more than I expected. |
| Week 3 | 5 of 7 | 6:31 | Travel killed Tuesday and Wednesday. |

Full weekly retros live in `log/retros/`.

## What you can steal

- The four-step sequence (water, light, movement, planning).
- The single-row daily log.
- The rule that the phone waits until step 4.

What you should probably not steal:

- The 6:30 wake time. Try your own. Mine was already a compromise.
- The 30-day frame. I tried 90 first and quit on day 11.

## Repo layout

- `protocol/` - the routine itself, including the movement file
- `log/` - daily entries, weekly retros, monthly status
- `notes/` - things I read or watched that shaped the protocol

## License

Do whatever you want with this. If you fork the repo and run your own experiment, open a discussion and tell me what changed.
