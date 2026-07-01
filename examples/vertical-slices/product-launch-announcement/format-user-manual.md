---
entry_id: user-manual
axis: format
topic_slug: product-launch-announcement
topic_label: Announcing a new product to an outside audience
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Tidemark User Manual

## Table of Contents

- [Getting Started](#getting-started)
- [Connecting Feedback Sources](#connecting-feedback-sources)
  - [Connecting a spreadsheet or CSV export](#connecting-a-spreadsheet-or-csv-export)
  - [Connecting a survey export](#connecting-a-survey-export)
  - [Connecting a source by email](#connecting-a-source-by-email)
  - [Connecting a source by webhook](#connecting-a-source-by-webhook)
  - [Viewing and removing connected sources](#viewing-and-removing-connected-sources)
- [Syncing and Ranking Feedback](#syncing-and-ranking-feedback)
  - [Running a sync](#running-a-sync)
  - [Understanding theme scores](#understanding-theme-scores)
  - [Adjusting a source's weight](#adjusting-a-sources-weight)
- [Sharing Your Roadmap](#sharing-your-roadmap)
  - [Generating a share link](#generating-a-share-link)
  - [Upgrading a share link to collaborative access](#upgrading-a-share-link-to-collaborative-access)
  - [Exporting a snapshot](#exporting-a-snapshot)
- [Managing Your Plan](#managing-your-plan)
  - [Free solo plan](#free-solo-plan)
  - [Team plan](#team-plan)
  - [Custom plan](#custom-plan)
  - [Upgrading a plan](#upgrading-a-plan)
- [Troubleshooting](#troubleshooting)
- [Reference](#reference)

## Getting Started

Tidemark connects to your team's existing feedback sources, spreadsheets, chat exports, survey tools, email, or a webhook, and produces one ranked, shareable roadmap. This section covers what to have ready before your first sync.

System requirements:
- Node 18 or later. Run `node --version` to confirm.
- npm access to install a global package.

Install the CLI:

```sh
npm install -g @tidemark/cli
```

Confirm the install:

```sh
tidemark --version
```

A Tidemark account and workspace are created automatically the first time you run `tidemark init`. No separate sign-up step is required.

First-session prerequisite: have at least one feedback source ready to connect, a CSV export, a spreadsheet, an email or chat archive, or a survey export. Tidemark does not require the source to be cleaned or reformatted before connecting.

Continue to Connecting Feedback Sources to run the setup wizard.

## Connecting Feedback Sources

Tidemark reads feedback from five source types: spreadsheet or CSV export, survey export, email, plain text, and webhook. Most teams start with the source they already use to collect customer input and add others later. A sync merges all connected sources into one theme list; see Syncing and Ranking Feedback.

### Connecting a spreadsheet or CSV export

Use this when your feedback lives in a CSV export from a support tool, a sales CRM, or a manually maintained spreadsheet.

Steps:
1. Run `tidemark init`.
2. Choose "Spreadsheet" when the wizard asks for source type.
3. Provide the file path, or drag the file into the terminal window when prompted.
4. Review the item count and preview the wizard reports, then confirm.

A successful connection looks like this:

```
Connected: customer-feedback.csv (148 items detected)
Ready to sync.
```

Options / Parameters:
- File size: 5 MB maximum per file. Larger files should use a webhook source instead.
- Required columns: `date` and `text`. Additional columns are ignored.
- Optional column: `submitter_id`. Providing it enables per-submitter segment scoring; see Understanding theme scores.

Notes:
- Rows missing `date` or `text` are skipped and listed in the upload summary. They do not stop the import.
- Re-running `tidemark init` with the same file path re-imports the current version of the file. It does not append to the previous import.
- If the detected item count is much lower than expected, see Troubleshooting.

### Connecting a survey export

Use this for CSV exports from survey tools, where each row is one response.

Steps:
1. Run `tidemark init`.
2. Choose "Survey export."
3. Provide the file path.

Options / Parameters:
- Multi-question surveys: each question in a response is parsed into a separate feedback item, so one response can produce several items.

Notes:
- If your survey tool exports multiple sheets, connect the response sheet, not a summary sheet.

### Connecting a source by email

Use this when feedback arrives as individual emails: forwarded support requests, or notes from customer calls sent to your own inbox.

Steps:
1. Run `tidemark init` and choose "Email."
2. Tidemark generates a workspace ingest address.
3. Forward relevant emails to that address as they arrive, or forward a backlog to import history.

Notes:
- The subject line and body are parsed together as a single feedback item. A long email thread is parsed as one item per email, not one item per thread.

### Connecting a source by webhook

Use this for automated pipelines, for example posting items from an internal tool whenever a customer submits feedback there.

Steps:
1. Run `tidemark init` and choose "Webhook" to generate your workspace ID.
2. Configure your system to send a POST request to `https://ingest.tidemark.io/v1/workspaces/{workspace_id}/items` with a JSON body containing `source` and `text` at minimum.
3. Optionally include `date`, `submitter_id`, and `tags`.

Options / Parameters:
- `source`: a free-form label identifying the originating channel, for example `"support"` or `"sales-call"`. Labels with a configured weight rule receive that multiplier during scoring; unmatched labels default to a multiplier of 1.0.

Notes:
- The endpoint returns HTTP 202 on receipt, not on processing completion, and delivery is not retried on failure. If an item does not appear after a sync, confirm it was received before assuming it was scored.

### Viewing and removing connected sources

Use this to see which sources feed your roadmap or to disconnect one that is no longer relevant.

Steps:
1. Run `tidemark init` again at any time to add another source; it does not remove existing ones.
2. To remove a source, open your share link, go to workspace settings, and select "Manage sources."

Notes:
- Removing a source does not remove items it already contributed to past syncs. The next sync reflects the removal going forward.

## Syncing and Ranking Feedback

A sync pulls the current contents of every connected source and produces a ranked list of themes. Run a sync any time your sources have new items you want reflected in the roadmap.

### Running a sync

Use this to refresh your ranked roadmap with the latest feedback.

Steps:
1. Run `tidemark sync`.
2. Wait for processing. A first sync against a large source can take a minute or two; later syncs are faster.
3. Read the terminal summary, which lists the number of themes identified and the top theme by score.

A typical summary:

```
Sync complete. 12 themes identified across 148 items.
Top theme: "CSV export is missing recurring items" (23 mentions, most recent: 3 days ago)
Run `tidemark share` to generate a shareable link.
```

Notes:
- Tidemark re-reads every connected source on each sync. It does not carry forward manual edits to theme labels beyond the label text itself; see Understanding theme scores.
- Webhook items delivered after a sync starts are not included in that sync. They appear in the next one.

### Understanding theme scores

Each theme's position in the ranked roadmap comes from its signal weight: a score built from how many distinct customers raised the theme and how recently.

```
signal_weight = sum(item_base_score * source_multiplier * segment_multiplier)
  for each item in the theme
```

Options / Parameters:
- `item_base_score`: fixed at 1.0 per item. Not configurable.
- `source_multiplier`: defaults to 1.0. Set per source label in workspace settings to weight some channels more heavily than others; see Adjusting a source's weight.
- `segment_multiplier`: defaults to 1.0. Set per submitter segment in workspace settings. Requires `submitter_id` on the item; items without it use the default multiplier.

Notes:
- Editing a theme's label after a sync does not trigger recalculation of its signal weight.
- Two themes close in score can swap positions between syncs as new items arrive. This is expected and reflects the recency component of the score; see Troubleshooting.

### Adjusting a source's weight

Use this when one feedback channel should count more heavily than others, for example direct customer calls over an anonymous survey.

Steps:
1. Open your share link and go to workspace settings.
2. Select "Source weights."
3. Set a multiplier for the source label you want to adjust.
4. Run `tidemark sync` to apply the change to the current ranking.

Notes:
- Weight changes apply on the next sync, not retroactively to the last one.

## Sharing Your Roadmap

A share link is a read-only, public-by-link view of your current ranked roadmap. It is the primary way stakeholders outside your Tidemark workspace see the results.

### Generating a share link

Use this to get a URL you can send to anyone, whether or not they have a Tidemark account.

Steps:
1. Run `tidemark share`.
2. Copy the URL Tidemark prints.
3. Send it to your stakeholders.

Notes:
- The view updates automatically each time you run a new sync. You do not need to regenerate the link.
- Anyone with the link can view the roadmap. There is no password protection on share links.

### Upgrading a share link to collaborative access

Use this when stakeholders need to comment or re-rank items, not just read the current state.

Steps:
1. Open your share link and select "Sharing and permissions."
2. Add collaborators by email.
3. Choose a role for each collaborator: comment-only or re-rank.

Notes:
- Read-only remains the default for anyone who receives the link without being added as a named collaborator.

### Exporting a snapshot

Use this to capture the current ranked roadmap as a static file, for a presentation, an email attachment, or an archival record.

Steps:
1. Open your share link.
2. Select "Export."
3. Choose CSV or PDF.

Notes:
- A snapshot captures sort order and item counts at export time. It does not update after export; regenerate it if the roadmap changes.

## Managing Your Plan

Tidemark has three plans. All plans include the full feedback-to-roadmap workflow; plans differ in seats and administrative controls.

### Free solo plan

For an individual who owns a roadmap without a team.

Options / Parameters:
- Price: $0.
- Seats: 1.

Notes:
- The free plan is not a time-limited trial. It does not expire or gate features behind a trial window.

### Team plan

For a team sharing one workspace and one ranked roadmap.

Options / Parameters:
- Price: $29 per month.
- Seats: up to 15.

### Custom plan

For organizations that require SSO and audit logs.

Steps:
1. Email launch@tidemark.io with your organization's requirements.
2. The team follows up with pricing and a provisioning timeline.

Notes:
- SSO and audit logs are not available on the Free solo or Team plans.

### Upgrading a plan

Use this to move from Free solo to Team, or from Team to Custom.

Steps:
1. Open your share link and go to workspace settings.
2. Select "Plan."
3. Choose the new plan and confirm.

Notes:
- Upgrading does not interrupt an in-progress sync or invalidate existing share links.
- Downgrading a workspace that has more members than the target plan allows requires removing members first.

## Troubleshooting

**The setup wizard detects far fewer items than expected.**
Your source file likely uses a column layout Tidemark does not recognize automatically. Create a sample file with a simple header row (one column each for customer name or ID, feedback text, and date), confirm the wizard detects it correctly, then connect the full file the same way.

**The theme list from `tidemark sync` does not look right.**
The most common cause is items that are internal notes or status updates rather than customer feedback. Filter those rows out of the source and sync again. Tidemark re-reads from the source on each sync, so no prior output carries over.

**A share link returns a "not found" error.**
Share links are tied to your Tidemark account. If you ran the CLI on a different machine than the one used during `tidemark init`, run `tidemark init` again on the new machine to reconnect your account, then run `tidemark share`.

**A webhook item is missing from the ranked roadmap after a sync.**
Webhook delivery returns HTTP 202 on receipt, not on processing completion, and is not retried on failure. Confirm the item was received before assuming it was scored. If it was received but still missing after a second sync, check that the payload included both `source` and `text`.

**Two themes swapped positions between syncs and nothing changed on your end.**
This is expected behavior, not an error. Position reflects both frequency and recency, so a theme built from older items can drop below a smaller but more recent one.

## Reference

### CLI command quick reference

| Command | Purpose |
|---|---|
| `tidemark --version` | Confirm the CLI is installed and show the current version. |
| `tidemark init` | Run the setup wizard and connect a new feedback source. |
| `tidemark sync` | Pull and rank feedback from all connected sources. |
| `tidemark share` | Generate or refresh the shareable read-only roadmap URL. |

### Glossary

- **Workspace**: The top-level container for one product's feedback and its active roadmap. One workspace per product.
- **Feedback item**: A single unit of customer input, with a source label and timestamp.
- **Theme**: A labeled cluster of similar feedback items, grouped automatically on sync.
- **Signal weight**: The numeric score that determines a theme's rank, built from item count, source multiplier, and segment multiplier.
- **Ranked roadmap**: The output view: themes sorted by signal weight, each with its supporting item count and share link.

### Plans at a glance

| Plan | Price | Seats | Notes |
|---|---|---|---|
| Free solo | $0 | 1 | No trial gating. |
| Team | $29/month | Up to 15 | |
| Custom | Contact launch@tidemark.io | Organization-defined | Includes SSO and audit logs. |
