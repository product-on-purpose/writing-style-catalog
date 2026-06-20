---
entry_id: friendly-mentor
axis: voice
topic_slug: first-pull-request
topic_label: Your first pull request
voice_id: friendly-mentor
tone_id: encouraging
style_id: procedural
format_id: readme
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# How to open your first pull request

This tutorial walks you through opening your first pull request on this repo. It is written for someone who has used git a little but has never gone through a full PR cycle on a team. If you are a bit nervous, that is normal. Every senior engineer on this team has their own slightly awkward first PR in the history somewhere. The goal here is not to be impressive on your first one. The goal is to ship one small change, end to end, so the second one is easier.

## What you will need

- A local clone of the repo with push access (or fork access if you are external)
- Git installed and configured with your name and email
- The change you want to make - keep it small for the first one, ideally under 20 lines
- About 30 minutes of uninterrupted time

## Steps

### 1. Pull the latest main

Before you branch, make sure your local main is up to date.

```bash
git checkout main
git pull origin main
```

### 2. Create a new branch

Branch names should be short and describe what you are doing.

```bash
git checkout -b your-name/short-description
```

### 3. Make the change

Edit the file or files you came here to edit. Resist the urge to also fix the three other things you noticed - those belong in their own PRs.

### 4. Run the tests locally

This is the step that catches the embarrassing breakages before anyone else sees them.

```bash
npm test
```

### 5. Stage and commit

Write a commit message that explains why the change exists, not just what it does. Future-you will be grateful.

```bash
git add <files-you-changed>
git commit -m "Fix off-by-one in pagination count"
```

### 6. Push the branch

```bash
git push -u origin your-name/short-description
```

### 7. Open the pull request

Follow the URL git prints, or go to the repo and click "Compare and pull request." Fill in the description with what the change does and how to test it. Two or three sentences is plenty.

### 8. Respond to review

This is the part that feels the most exposed, and it is the part where the most learning happens. Reviewers on this team are trying to help you ship a good change, not to grade you. Read every comment, ask if anything is unclear, and push follow-up commits to the same branch. You do not need to defend your choices - just engage with the suggestions.

## How to know it worked

Your PR shows green checks, at least one approving review, and the merge button turns green. When you click it (or a maintainer does), your change is on main. That is it. You shipped.

## If something goes wrong

- **The tests fail on CI but pass locally.** Almost always an environment difference. Check the CI logs for the exact error and ask in the team channel if you cannot reproduce it. This happens to everyone.
- **A reviewer asks for changes and you are not sure how to make them.** Ask. "I'm not sure I understand - could you point me at an example?" is a fine reply. It is not a sign of weakness; it is how the team teaches.
- **You accidentally committed to main instead of your branch.** Recoverable. Tell someone, do not panic-force-push, and we will sort it out.

## What is next

After this one merges, your second PR will feel noticeably less heavy. Aim to open another within the next week, even a tiny one. The cycle is what builds the muscle, not the size of any single change.
