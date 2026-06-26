---
entry_id: technical-writer
axis: voice
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

This document covers the steps to get Priya from day one to her first merged change by Friday of week two.

## Week 1: Access and orientation

**Before day 1**, complete the following:

1. Grant access to the code repository, the deployment pipeline, the ticket tracker, and the chat tool. Verify each credential logs in.
2. Assign a buddy - a teammate who is not Priya's manager - to handle environment setup questions on day one.
3. Select a starter ticket: small, self-contained, and mergeable without elevated permissions.

**Day 1:** Have the buddy walk Priya through environment setup. End the day with a 30-minute team intro: names, roles, and who owns what. Do not cover the codebase yet.

**Days 2-3:** Run two focused sessions.

- Codebase tour (Day 2): Walk through the top-level directory structure, one service entry point, and the path from a merged pull request to production. Cover one service only.
- How we work (Day 3): Cover the pull request process, on-call expectations, and who owns each area of the codebase. Share the runbook link in the chat tool after this session.

## Week 2: First change

Assign the starter ticket on Monday of week two.

Pair with Priya for the first hour. Step back when she is driving. Review her pull request the same day she opens it.

**Note:** If the PR review surfaces a process gap - something she could not have known from the orientation - log it in the onboarding doc and update the doc. Do not treat a missing instruction as Priya's error.

## After the merge

When the change ships, name it in the next team sync: what it does, who shipped it. One or two sentences. This step marks her as a contributor, not an observer in training.
