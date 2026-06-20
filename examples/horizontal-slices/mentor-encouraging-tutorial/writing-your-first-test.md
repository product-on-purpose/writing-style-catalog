---
entry_id: friendly-mentor
axis: voice
topic_slug: writing-your-first-test
topic_label: Writing your first test
voice_id: friendly-mentor
tone_id: encouraging
style_id: procedural
format_id: readme
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Writing your first test

This tutorial walks you through writing your first automated test. It is for engineers who have shipped working code but have never written a test for it. Honest framing up front: the first test you write will feel awkward, and that feeling is normal. Tests are a learning tool as much as a verification tool - writing them teaches you what your function actually does, not just what you think it does. Untested code is not failing code. It is just code with no documented contract. You are about to write one.

## What you will need

- A working development environment - if you do not have one yet, see the setup tutorial first
- A function in the codebase you wrote, or one you are about to change
- About 20 minutes

## Steps

### 1. Pick a small pure function

For your first test, pick a function that takes input, returns output, and does not touch the network, the database, or the filesystem. Pure functions are the easiest to test, and your first test should be easy. If you are not sure which to pick, ask your reviewer - they will know.

### 2. Create the test file

By convention in this repo, the test for `src/utils/format-name.ts` lives at `src/utils/format-name.test.ts`. Create the file next to the function.

```bash
touch src/utils/format-name.test.ts
```

### 3. Import the function and the test framework

```typescript
import { describe, it, expect } from 'vitest';
import { formatName } from './format-name';
```

### 4. Write a failing test

Start with a test that you expect to pass, but write the assertion wrong on purpose so you see it fail first. This proves the test is actually running.

```typescript
describe('formatName', () => {
  it('returns first and last name joined by a space', () => {
    expect(formatName('Ada', 'Lovelace')).toBe('WRONG');
  });
});
```

Run the test:

```bash
pnpm test format-name
```

You should see a failure with a clear diff. Good. That confirms the test is wired up.

### 5. Make the test pass

Now fix the assertion to match what the function actually returns.

```typescript
expect(formatName('Ada', 'Lovelace')).toBe('Ada Lovelace');
```

Run it again. Green. You wrote a passing test.

### 6. Add an edge case

One green test is a start, not a finish. Think about what could go wrong with this function: empty strings, missing arguments, unusually long names, names with unexpected characters. Pick one of those cases and add it.

```typescript
it('handles an empty last name', () => {
  expect(formatName('Ada', '')).toBe('Ada');
});
```

If that test fails, you have just learned something useful about your function - it does not handle the case you assumed it did. That is the test doing exactly what tests are for.

## How to know it worked

The test file exists, `pnpm test` runs it, and at least one assertion passes. The second signal that it worked is harder to measure: you should now have a slightly clearer mental model of what that function does. If thinking about edge cases made you spot a behavior you had not noticed before, that is the real value showing up.

## If something goes wrong

- **The test runner cannot find your test file.** Check the filename matches the convention - it must end in `.test.ts`. The runner discovers tests by filename pattern.
- **You write an assertion you are sure should pass and it fails.** Read the diff carefully. Nine times out of ten, the function behaves slightly differently than you remember. This is the test being useful, not the test being wrong.
- **You feel like you are testing something obvious.** That is fine for the first one. Obvious tests still document behavior, and they catch regressions when someone refactors the function later. The exercise is the point.

## What is next

The second test is the one where the muscle starts to form. Pick another small function this week and repeat the loop: failing test, passing test, edge case. After three or four, writing a test feels like a natural part of writing code, not a chore tacked on at the end.
