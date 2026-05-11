---
entry_id: blog-post-long-form
axis: format
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Your Daily Standup Is Solving the Wrong Problem

Three engineers on your team are joining your 9am standup at 9:30pm their time. They have been doing it for a year. You have noticed they attend less than the US-based engineers. You have probably assumed it is engagement or discipline. It is neither. It is 9:30pm.

The daily standup is one of the most persistent rituals in software development, and one of the most misunderstood. Most teams that run standups believe they are running a coordination meeting. What they are actually running is a presence ritual with some coordination features bolted on. Understanding the difference is what will help you decide whether to change the format - and if you change it, how to do it without breaking what actually matters.

## What a Standup Is Actually Doing

The synchronous standup has two functions that are usually bundled together.

The first is status visibility: who is working on what, what is blocked, what dependencies are about to collide. This is the explicit purpose. A well-run standup surfaces blockers early, catches coordination problems before they become delays, and keeps the team's work visible to everyone on it.

The second is social presence: the daily act of gathering, of being in a shared moment, of saying "I am here and so are you." This function is rarely named, but it is real. Teams that have daily standups feel different from teams that do not - there is a rhythm, a sense of shared forward motion, that does not come from the status itself but from the daily gathering.

The problem with synchronous standups for distributed teams is that they impose a coordination overhead to serve the presence function - and the coordination function can be served more efficiently with a different tool.

## What Async Standups Do Better

An async standup is a structured written update posted to a shared channel. The format that works best is simple: what shipped in the last 24 hours, what is in progress today, what is blocked or at risk. Blocked items include a direct @mention of the person who can help.

Three things happen when you move from synchronous to async that are genuinely better than the meeting.

**The information persists.** When @priya posts at 8am India time that the auth service is throwing a 401 on a specific endpoint, that post is there when @dan starts his day in California three hours later. The engineer who hits the same 401 at 2pm can search the channel and find Priya's diagnosis. In a synchronous standup, the same information evaporates after the meeting unless someone wrote it down. Nobody wrote it down.

**Blockers reach the right person faster.** In a synchronous standup, a blocker reaches the person who can resolve it only if that person attended the meeting and made a note. In an async channel, the @mention sends a direct notification. The blocker routes itself.

**Everyone participates on a schedule that fits their life.** The India-based engineer posts at 8am their time. The west coast engineer posts at 9am their time. Nobody is joining a meeting at 9:30pm. The team's work is visible to everyone, and everyone contributed on a schedule that was reasonable for them.

## What Async Standups Cannot Replace

Here is where most writing about async standups stops being honest: the social presence function does not transfer.

A written update in a channel is not the same as being in a room together, or even a Zoom call together. The daily standup, whatever its coordination failures, created a shared moment - a daily rhythm of gathering that built team fabric over time. Async channels do not do this. You can build warmth and personality into your posts, but the shared-moment feeling does not survive the format change.

This is the real reason some teams switch to async standups and feel more fragmented three months later. The coordination problem is solved. The presence problem is worse.

The teams that get this right do not choose between synchronous and async. They separate the two functions and handle them with different rituals. The async standup handles coordination - status, blockers, visibility. A weekly working session handles presence - a synchronous meeting that exists explicitly for collaboration and connection, not status reporting.

## How to Make the Switch

The structural change is simple. The adoption challenge is getting the team to post consistently and read attentively.

Start with a pinned template in your standup channel. Three fields. Ship it on Monday. Ask for updates by 10am local time. The team lead reads the channel at the start of their day and responds to blocked items within 30 minutes. That commitment to reading and responding is what makes the channel feel alive rather than a place where updates go to be ignored.

The first two weeks will be awkward. Engineers will post and wonder if anyone read it. Some will miss days. Hold the norm firmly and gently: the format only works if everyone participates. At week three, most teams find their rhythm.

The synchronous meeting does not disappear - it transforms. A 60-minute Thursday working session, reserved for discussion that needs real-time exchange. Not a standup. Not status. A session for the work that benefits from being in the room together.

Run it for 30 days before you decide whether it is working. Track blocker resolution time, participation rate, and do a short team survey. If it is not working, you will have data on what to adjust. If it is working, you will know why.

## The Thing That Actually Changes

The shift to async standups is not really about format. It is about what you believe a distributed team owes each other.

The synchronous standup says: we owe each other shared presence, daily, at a fixed time, regardless of what that costs people on the edges of the timezone map. The async standup says: we owe each other visible work and honest blockers, on a schedule that respects the fact that we live in different places.

Both are forms of accountability. The question is which form fits the team you actually have - not the co-located team the standup was designed for, but the distributed team that exists now, on four continents, at four different local times.

The ritual that serves that team is not the one you inherited. It is the one you build.
