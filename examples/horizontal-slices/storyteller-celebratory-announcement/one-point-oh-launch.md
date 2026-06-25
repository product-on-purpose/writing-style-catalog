---
entry_id: storyteller
axis: voice
topic_slug: one-point-oh-launch
topic_label: Announcing the 1.0 release after two years
voice_id: storyteller
tone_id: celebratory
style_id: narrative-case-study
format_id: blog-post-long-form
author_type: llm
llm_model: claude-sonnet-4-6
review_status: draft
---

# Two Years, One Number

The version number we shipped Thursday is "1.0.0." Three characters. The git tag took four seconds to push.

What it replaced was 847 commits, 23 beta cycles, one full rewrite of the authentication layer, and six weeks in spring 2024 where we did not know if we were going to make it.

## Where We Started

In January 2024, Meridian worked if you already knew how it worked. New-user onboarding completion sat at 19% - the percentage who reached a first successful workflow within 48 hours. We had known this for months. What we had not admitted was that the number was not a bug in our onboarding flow. It was a signal about the product.

The core model required users to understand "sessions" vs. "workspaces" before doing anything useful. Nobody read the tooltips. They clicked around, hit a wall, and left. Active users loved us (NPS: 71). Getting through the door was the problem.

## The Turn

The rewrite came out of a user interview in March 2024. Maya, a freelance consultant, opened the app, looked at the empty session grid, and said out loud to no one: "I don't know what I'm supposed to do next." Then she closed the tab.

Priya, our product lead, watched the recording three times. Then she walked into standup: "We're collapsing sessions and workspaces into one concept. I know what it costs. We're doing it anyway."

It cost four months. In August, two weeks before our target date, we found a race condition that would have silently corrupted data under concurrent edits. We pushed the date. Nobody liked it. We pushed it anyway.

## What Shipped

November 14th, 2:47 PM: Daniel merged the release branch. Eleven-minute deploy. Health checks green. Three people posted the same emoji in Slack within seconds of each other.

Onboarding completion in the first 72 hours: 61%.

Up from 19%. We are not hedging that number. It is 61%.

## The Principle

We didn't ship 1.0 because the calendar said it was time. We shipped it because the product finally does what we always said it would: a new user can sit down and reach their first workflow without asking anyone for help. That sentence took two years. It is the only sentence that matters.
