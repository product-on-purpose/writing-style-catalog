// tools/agentic/promote.js - RENDER harness (the promotion factory's render stage)
//
// WHAT
//   A Workflow-tool script (NOT a standalone CLI - it runs only through the Claude
//   Code Workflow tool). It renders each FORMAT in `FORMATS` across all 12 anchor
//   topics, writing one worked-sample file per (format, topic) cell, so the formats
//   can then be promoted to stable without failing the Gate 2 sample-count check.
//
// WHY IT MATTERS
//   A stable entry must render on all 12 anchor topics (Gate 2). Drafts are exempt,
//   so you RENDER while still draft (validate stays green), THEN flip with
//   tools/promote.py. This harness is the render step. One isolated agent per cell
//   keeps the 12*N prose blocks out of the orchestrator's context and lets each cell
//   inherit the topic's shared scenario from the existing samples.
//
// HOW IT WORKS
//   For each cell, one sonnet agent: (1) reads taxonomy/formats/<fmt>/ENTRY.md for
//   the format's structure; (2) reads three existing samples on the topic
//   (format-adr/readme/status-report.md) to inherit the SHARED SCENARIO - the named
//   people, situation, and dates every sample on that topic reuses; (3) writes
//   examples/vertical-slices/<topic>/format-<fmt>.md with the required frontmatter.
//   Forced combos (an eng format on a contemplative topic) are expected: apply the
//   format's STRUCTURE to the topic's situation (precedent:
//   daily-rest-practice/format-adr.md renders an ADR for a personal rest decision).
//
// HOW TO RUN
//   1. Set FORMATS to the draft format ids you are about to promote.
//   2. Invoke this file with the Workflow tool: Workflow({ scriptPath: ".../promote.js" }).
//   3. validate.py + a DATE GATE on any dated formats (see tools/agentic/README.md),
//      then tools/promote.py to flip, then counters + manifests + PR.
//
// GOTCHA
//   The 12 TOPICS below mirror tools/anchor_topics.py seed_pool(); keep them in sync
//   if the pool changes. Prose passed into agent prompts must avoid YAML-style ''
//   apostrophe doubling - that is a JS parse error inside a single-quoted string.

export const meta = {
  name: 'agentic-render',
  description: 'Render N formats across all 12 anchor topics (12*N worked samples), reusing each topic shared scenario',
  phases: [{ title: 'Render', detail: 'one agent per (format, topic) cell writes a scenario-consistent sample' }],
}

const ROOT = 'E:/Projects/product-on-purpose/writing-style-catalog'

// EDIT THIS: the draft format ids to render (then promote).
const FORMATS = ['example-format-id']

// The 12 anchor topics (slug, label) - keep in sync with tools/anchor_topics.py.
const TOPICS = [
  ['service-database-choice', 'Choosing Postgres vs DynamoDB for a new service'],
  ['async-standups', 'Whether the team should move to async-first standups'],
  ['roadmap-deprioritization', 'Telling stakeholders a committed feature is being cut this quarter'],
  ['onboarding-a-new-hire', 'Getting a new engineer productive in their first two weeks'],
  ['remote-work-policy', 'Arguing a public position on return-to-office'],
  ['product-launch-announcement', 'Announcing a new product to an outside audience'],
  ['morning-routine', 'Designing a sustainable morning routine'],
  ['thanking-a-mentor', 'Writing to thank a mentor who shaped your career'],
  ['retirement-send-off', "Marking a long-serving colleague's departure"],
  ['team-milestone-celebration', 'Marking the team shipping a hard, long project'],
  ['daily-rest-practice', 'Reflecting on keeping a discipline of rest'],
  ['a-hard-year-in-review', 'A personal year-end reckoning with a difficult year'],
]

function cellPrompt(fmt, slug, label) {
  const file = 'examples/vertical-slices/' + slug + '/format-' + fmt + '.md'
  return [
    'You are rendering ONE worked example for the writing-style-catalog: the FORMAT "' + fmt + '" applied to the anchor topic "' + slug + '" (' + label + '). Working directory: ' + ROOT + ' (use repo-relative paths).',
    '',
    'Step 1: Read taxonomy/formats/' + fmt + '/ENTRY.md - its structure, tells, canonical_template, and llm_instruction_phrasing.',
    '',
    'Step 2: Read these EXISTING samples on this topic to learn the SHARED SCENARIO (the specific situation, named people, concrete details, and dates that every sample on this topic reuses) and the house style:',
    '  examples/vertical-slices/' + slug + '/format-adr.md',
    '  examples/vertical-slices/' + slug + '/format-readme.md',
    '  examples/vertical-slices/' + slug + '/format-status-report.md',
    'Your sample MUST use the SAME scenario - same people, same situation, same specifics and dates - so it is directly comparable to the other samples on this topic. Do NOT invent a different situation.',
    '',
    'Step 3: Write the file ' + file + '. Apply the "' + fmt + '" format faithfully to the shared scenario of this topic, even when the pairing is unusual (an ADR applied to a personal decision still uses Status / Context / Decision / Consequences; render the real structure of the format on whatever situation this topic carries). Frontmatter, exactly these fields:',
    '---',
    'entry_id: ' + fmt,
    'axis: format',
    'topic_slug: ' + slug,
    'topic_label: ' + label,
    'author_type: llm',
    'llm_model: claude-sonnet-4-6',
    'review_status: reviewed',
    '---',
    'Then a blank line and the worked sample body.',
    '',
    'REQUIREMENTS:',
    '- Reuse the people, situation, and specifics from the existing scenario; stay consistent with any dates/weekdays the existing samples use (do not introduce contradictory dates).',
    '- HARD RULE: no em-dashes (U+2014) or en-dashes (U+2013); use " - " (space hyphen space). The write is REJECTED if they appear.',
    '- No fabricated statistics and no real-company / real-person claims; keep details internal and first-person/low-fabrication, matching the existing samples.',
    '- Match the length and density typical of this format (per its ENTRY.md).',
    '- After writing the file, return ONLY "' + fmt + '@' + slug + ' OK". Do not return the file content.',
  ].join('\n')
}

const CELLS = []
for (const fmt of FORMATS) for (const [slug, label] of TOPICS) CELLS.push({ fmt, slug, label })

phase('Render')
const results = await parallel(CELLS.map((c) => () => agent(cellPrompt(c.fmt, c.slug, c.label), { label: c.fmt + '@' + c.slug, phase: 'Render', model: 'sonnet' })))
const wrote = results.filter(Boolean).length
const failed = CELLS.filter((c, i) => !results[i]).map((c) => c.fmt + '@' + c.slug)
log('render: wrote ' + wrote + '/' + CELLS.length + ' samples')
return { wrote, failed, cells: CELLS.length }
