// tools/agentic/remediate.js - FIX-APPLIER harness (precise, one agent per file)
//
// WHAT
//   A Workflow-tool script that applies a list of precise, pre-specified corrections,
//   one agent per file. General-purpose: use it for de-dup remediation (the fixes
//   from dedup.js), for date-consistency corrections (the fixes from a date gate), or
//   for any batch of surgical edits where you already know the exact change per file.
//
// WHY IT MATTERS
//   Gates produce precise fix-lists; applying them by hand across a dozen files is
//   slow and leaks prose into the orchestrator's context. This harness applies each
//   correction in an isolated agent that reads only its own file, so the orchestrator
//   stays lean and the edits stay surgical. Always re-validate after (validate.py),
//   and re-gate anything that was a genuine quality finding.
//
// HOW IT WORKS
//   For each fix, one sonnet agent reads the target file, applies ONLY the described
//   correction, preserves everything else, and respects the no-dash rule. Reciprocal
//   pairs (edits to two files that must stay consistent, e.g. a confusable link added
//   both ways) are handled by a single fix entry that names both files, so both sides
//   are written by the same agent.
//
// HOW TO RUN
//   1. Set FIXES: one entry per file (or per reciprocal pair). Each `instruction` is
//      the exact correction - quote the offending text and state the replacement, so
//      the agent cannot drift. Use backtick template literals for instructions (they
//      contain apostrophes and quotes).
//   2. Invoke with the Workflow tool.
//   3. validate.py + build (+ re-gate genuine findings) + PR.

export const meta = {
  name: 'agentic-remediate',
  description: 'Apply a list of precise per-file corrections, one agent per file',
  phases: [{ title: 'Remediate', detail: 'one agent per fix applies a precise edit' }],
}

const ROOT = 'E:/Projects/product-on-purpose/writing-style-catalog'

// EDIT THIS: one entry per file (or per reciprocal pair). `instruction` should quote
// the exact text to change and state the exact replacement.
const FIXES = [
  {
    id: 'example-fix',
    instruction: `In taxonomy/formats/example-id/ENTRY.md, change the exact text "old wording" to "new wording" because <reason>. Change nothing else.`,
  },
]

function fixPrompt(f) {
  return [
    'You are applying ONE precise correction to a file in the writing-style-catalog. Working directory: ' + ROOT + '. Read the file, apply ONLY the change described, preserve everything else.',
    '',
    f.instruction,
    '',
    'REQUIREMENTS:',
    '- Apply exactly the change described and nothing more.',
    '- Keep valid YAML frontmatter. Escape an apostrophe inside a single-quoted YAML scalar by doubling it. Body prose uses normal apostrophes.',
    '- HARD RULE: no em-dashes (U+2014) or en-dashes (U+2013); use " - ". Writes containing them are rejected.',
    '- When done, return ONLY: "fixed ' + f.id + '".',
  ].join('\n')
}

phase('Remediate')
const results = await parallel(FIXES.map((f) => () => agent(fixPrompt(f), { label: 'fix:' + f.id, phase: 'Remediate', model: 'sonnet' })))
const done = FIXES.filter((f, i) => results[i]).map((f) => f.id)
const failed = FIXES.filter((f, i) => !results[i]).map((f) => f.id)
log('remediate: ' + done.length + '/' + FIXES.length + ' applied')
return { done, failed }
