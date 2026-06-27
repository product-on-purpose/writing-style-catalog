---
entry_id: postmortem
axis: format
topic_slug: morning-routine
topic_label: Designing a sustainable morning routine
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Postmortem: Week 3 Travel Disruption - Morning Protocol Collapse (Days 20-21)

## Severity

SEV-3 - Two consecutive days of complete protocol failure during a work trip. Scope contained to the travel window, but recovery was incomplete on the return day.

## Summary

On June 2 and June 3, 2026 (days 20 and 21 of the 30-day morning routine experiment), the v3.0 protocol failed completely on both days. A two-day work trip invalidated the protocol's environmental dependencies: no nightstand glass, no kitchen for phone staging, no accessible outdoor light. No travel variant existed. Both of the protocol's phone-deferral failures for the entire 30-day period occurred during this window. Recovery on June 4 was partial.

## Timeline

- 2026-05-26, evening - Work trip booked. No protocol adjustment noted or planned.
- 2026-06-01, 06:15 - Normal protocol completed at home. Day 19 of 30. No preparation for the following morning.
- 2026-06-02, 05:45 - Woke in hotel room. Phone used immediately to check flight and logistics. Water step skipped (no glass prepared the night before). Light step attempted at the window, which faced an interior courtyard. Movement and planning abandoned due to airport departure time pressure.
- 2026-06-02, 07:30 - Departed for airport. Day 20 recorded as failed.
- 2026-06-03, 06:30 - Second morning in hotel. Did not attempt the protocol. Defaulted to pre-experiment behavior: phone in bed, Slack and news before breakfast.
- 2026-06-03, 08:00 - Day 21 recorded as failed.
- 2026-06-04, 06:20 - Returned home. Protocol completed but daily log entry was skipped. Phone-deferral step completed. Classified as a partial recovery.
- 2026-06-04, 20:00 - Backfilled log entry for day 22. Note recorded: "no travel variant is an open gap."

## Root Cause

The protocol succeeded at home because the home environment was re-engineered to remove friction: the glass sits on the nightstand, the phone stays in the kitchen, the front door gives immediate outdoor access for the light step. These are not minor conveniences. They are the mechanism by which the protocol works. Each step that removed a decision point was also a step that depended on a specific physical arrangement.

Travel removed that arrangement without substituting anything. When the nightstand glass was missing, there was no fallback. When the kitchen did not exist, the phone had no staging location and became the default tool for logistics. When the window faced a wall, the light step had no alternative.

The root cause is not a failure of follow-through. It is the absence of a travel branch in the protocol design. The protocol's environmental dependencies were never made explicit, so they were never addressed for conditions other than the home.

## Impact

- Days affected: 2 (June 2-3, days 20-21 of 30)
- Partial recovery: 1 additional day (June 4, day 22 - protocol completed, log skipped)
- Steps completed across the three-day window: 0 of 8 on days 20-21; 3 of 4 on day 22 (light step omitted)
- Phone-deferral failures: Both failures in the 30-day period (2 of 30) occurred during this incident
- Week 3 total: 5 of 7, versus a potential 7 of 7 absent the travel gap

## Contributing Factors

- No travel variant existed at experiment launch; the protocol document had no section covering non-home environments
- Environmental dependencies (glass on nightstand, kitchen for phone, outdoor light access) were implicit and undocumented
- Travel logistics on June 2 required early phone access, removing the deferral rule without any substitute behavior defined
- Sleep schedule shifted: earlier wake time for the airport, less total sleep, elevated logistics load before the first step
- No pre-trip preparation step existed in the protocol to prompt a travel adaptation

## Action Items

- [ ] Write a travel variant covering at minimum: water from hotel coffee station, 10-minute lobby or parking-lot walk for light, planning in travel notebook - Owner: Me - Due: before next booked work trip
- [ ] Enumerate all environmental dependencies for each step and add them to `protocol/movement.md` as explicit assumptions - Owner: Me - Due: 2026-06-21
- [ ] Add "prep nightstand glass" to the evening shutdown checklist and "pack travel notebook" to the packing list - Owner: Me - Due: 2026-06-14
- [ ] Define explicit rules for phone use during travel mornings: distinguish required logistics access from defaulting to the old behavior - Owner: Me - Due: 2026-06-14
- [ ] Before any future multi-day trip, do a one-paragraph written adaptation plan the evening prior - Owner: Me - Due: standing rule beginning 2026-06-14

## Lessons Learned

A protocol that works because the environment has been carefully arranged is not portable by default. The re-engineering that makes the home morning work - removed friction, pre-positioned materials, a predictable sequence - does not travel. Any environmental change (travel, houseguests, illness, a different schedule) can expose the same latent gap.

Designing for the average case while leaving exception cases unaddressed is not a minor oversight. The exception cases are when the protocol is most needed and hardest to execute. A travel variant that requires only a hotel lobby and a pocket notebook is not a lesser version of the protocol. It is what keeps the habit alive when the home environment is unavailable.

The status report for Month 1 attributed three missed wake times to travel across the full 30 days. This incident accounted for two consecutive protocol failures and both phone-deferral failures. Treating travel as an acknowledged gap from the start, rather than a surprise, is the specific change that would have changed those numbers.
