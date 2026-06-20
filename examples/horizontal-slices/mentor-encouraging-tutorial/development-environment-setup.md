---
entry_id: friendly-mentor
axis: voice
topic_slug: development-environment-setup
topic_label: Setting up your development environment
voice_id: friendly-mentor
tone_id: encouraging
style_id: procedural
format_id: readme
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Setting up your development environment

This tutorial gets the project running on your machine for the first time. Honest warning up front: environment setup is the worst part of joining most projects. Things break for reasons nobody documented, paths fight each other, and version mismatches surface as cryptic errors. If you have already lost an afternoon to this somewhere else, you are not bad at this - the work itself is genuinely fiddly. We have tried to flatten the bumps below, and once you are through, you do not have to do it again.

## What you will need

- A laptop you have admin rights on
- A terminal you are comfortable using
- Roughly an hour, possibly two on the first attempt
- The team Slack open so you can ping someone if you get stuck

## Steps

### 1. Install the required tools

You will need three things: Node.js (version pinned in `.nvmrc`), Docker Desktop, and the `pnpm` package manager. We pin Node because the build scripts assume a specific version, and version drift here is the single most common source of "works on my machine" bugs.

```bash
# Mac
brew install node docker pnpm

# Linux - use your package manager or the official installers
```

### 2. Clone the repo

```bash
git clone git@github.com:your-org/your-repo.git
cd your-repo
```

### 3. Install dependencies

```bash
pnpm install
```

This downloads the project's libraries. It can take a few minutes on a fresh clone. Expected output ends with `Done`.

### 4. Copy the example environment file

```bash
cp .env.example .env
```

Open the new `.env` file and read through it. Most values are fine as-is for local development. The ones you will need to fill in are documented inline with comments.

### 5. Start the database container

```bash
docker compose up -d db
```

This runs Postgres in the background. The first time, Docker will download the image, which takes a minute.

### 6. Run the database migrations

```bash
pnpm db:migrate
```

Expected output: a list of migrations applied, ending with `Database is up to date.`

### 7. Run the test suite

```bash
pnpm test
```

This is the verification step. If the tests pass, your environment is correctly configured. If they fail, that is information - move to the troubleshooting section before doing anything else.

### 8. Start the app locally

```bash
pnpm dev
```

Open `http://localhost:3000` in your browser. You should see the app's home page.

## How to know it worked

The test suite passes, `pnpm dev` starts without errors, and the app loads at `localhost:3000`. That trio is the contract. If all three are green, you are done.

## If something goes wrong

- **`pnpm install` fails with a Node version error.** Your installed Node does not match `.nvmrc`. Install `nvm` and run `nvm use` from the repo root. This is the most common first-day problem.
- **Docker says it cannot connect to the daemon.** Docker Desktop is not running. Open the app, wait for the whale icon to stop animating, then retry. This trips up everyone, including people who have used Docker for years.
- **Tests pass but the app fails to start.** Almost always a missing `.env` value. Re-read the comments in `.env.example` and check that every required variable is filled in.

If you have been stuck on any single step for more than 30 minutes, stop and ping the team channel. We mean this. Setup problems are not character tests, and someone has almost certainly seen your specific error before.

## What is next

Once your environment is running, the next thing is making a small change and watching the hot-reload pick it up. Edit something visible on the home page, save, and watch it update in the browser. That moment is when the project starts to feel like yours.
