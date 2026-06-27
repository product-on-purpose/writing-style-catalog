---
entry_id: how-to-guide
axis: format
topic_slug: product-launch-announcement
topic_label: Announcing a new product to an outside audience
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# How to turn scattered customer feedback into a ranked, shareable roadmap

## Before you begin

- Node 18 or later is installed on your machine. Run `node --version` to confirm. If you see `v18.x.x` or higher, you are ready.
- You have npm access to install a global package.
- You have at least one feedback source ready: a CSV export from your support tracker, a spreadsheet of customer requests, a chat thread archive, or a survey export. Tidemark does not require that you clean this data before connecting it.
- You have a team that needs to agree on what to build next. If you are the only person who will ever look at the output, a spreadsheet may be faster. Tidemark is built for shared, visible prioritization.

## Overview

This guide walks you through installing Tidemark, connecting your existing feedback sources, running your first sync, and sharing a ranked roadmap view with your team. When you finish, you will have a live link showing what customers are asking for - scored by frequency and recency - that any stakeholder can read without needing their own Tidemark account.

## Step 1: Install the Tidemark CLI

Tidemark's CLI is the primary way to connect sources and run syncs. Installing it globally makes the `tidemark` command available from anywhere in your terminal.

```sh
npm install -g @tidemark/cli
```

Confirm the install worked:

```sh
tidemark --version
```

You should see a version number printed. If you see a "command not found" error instead, check that your npm global bin directory is on your PATH. Running `npm bin -g` shows you where that directory is.

## Step 2: Run the setup wizard

The setup wizard connects your first feedback source. It is interactive and takes about five minutes.

```sh
tidemark init
```

The wizard asks which type of source you are connecting (spreadsheet, ticket tracker, chat export, or survey output) and where to find it. You do not need to reformat the data first; Tidemark reads from your existing structure.

When the wizard finishes, it confirms how many items it detected and shows a brief preview. A successful outcome looks like this:

```
Connected: customer-feedback.csv (148 items detected)
Ready to sync.
```

If the item count is much lower than you expect, your source file may use a non-standard column layout. See Troubleshooting below.

## Step 3: Pull and rank your feedback

Once at least one source is connected, run a sync to pull all items and generate the ranked output.

```sh
tidemark sync
```

Tidemark reads every connected source, identifies recurring themes across items, and scores each theme by how many distinct customers raised it and how recently. The first sync may take a minute or two, depending on how many items your sources contain.

When the sync completes, you will see a summary in the terminal:

```
Sync complete. 12 themes identified across 148 items.
Top theme: "CSV export is missing recurring items" (23 mentions, most recent: 3 days ago)
Run `tidemark share` to generate a shareable link.
```

You do not need to do anything with this output yet. The next step produces the view your team and stakeholders will actually read.

## Step 4: Share the ranked roadmap

Generating a shareable view turns your local sync results into a read-only link you can send to anyone.

```sh
tidemark share
```

After a few seconds, Tidemark prints a URL. That link shows the full ranked theme list, the item count and recency score for each theme, and - if you connected multiple sources - which sources contributed to each theme.

The view is read-only by default. Anyone with the link can read it without signing in. Copy the URL and send it to your stakeholders. The view is designed to be readable without narration, so you do not need to schedule a walkthrough before sharing.

## Troubleshooting

**The wizard detects far fewer items than you expected.**
Your source file may use a layout Tidemark does not recognize automatically. Try copying a sample of 10 to 20 rows into a new CSV with a simple header row (one column for customer name or ID, one for feedback text, one for date), then connect that version. Once you confirm the format is recognized, connect the full file the same way.

**The theme list from `tidemark sync` does not look right.**
The most common cause is items that are internal notes or status updates rather than customer feedback. Filter those rows out of your source and run `tidemark sync` again. Tidemark re-reads from your source on each sync, so no prior output carries over.

**The share URL returns a "not found" error.**
Share links are tied to your Tidemark account. If you ran the CLI on a different machine than the one you used during `tidemark init`, run `tidemark init` again on the new machine to reconnect your account, then run `tidemark share`.

## Next steps

You have connected a feedback source, run your first sync, and produced a shareable ranked roadmap. From here:

- **Add more sources.** Run `tidemark init` again to connect a second source (for example, a support ticket queue alongside your spreadsheet). On the next sync, Tidemark merges all sources and deduplicates themes that appear across them.
- **Give collaborators the ability to comment or re-rank.** See [Sharing and permissions](docs/sharing.md) for how to upgrade a share link from read-only to collaborative.
- **Understand how the ranking score works.** See [How ranking works](docs/scoring.md). The scoring model weights frequency and recency; this page explains the formula and how to interpret edge cases where two themes are close in score.
- **Keep your ranked view current automatically.** If your feedback sources update daily, schedule `tidemark sync` as a cron job so the view stays fresh without a manual run.

If you run into a problem not covered here, visit tidemark.io for additional help resources.
