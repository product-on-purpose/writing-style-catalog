// Load a tools/agentic/*.js Workflow template the way the Workflow runtime must.
//
// A Workflow script is NOT an importable ES module: it carries a top-level
// `return` statement (illegal in a module) alongside `export const meta`. The
// runtime therefore strips the exports and wraps the body in an async function
// before running it. This helper does the same transform, so a test can run a
// harness with stubbed runtime globals and capture the prompts it emits.
//
// It is deliberately a faithful stand-in and not a parser: if a harness stops
// loading here, that is a signal its shape drifted from what the runtime
// accepts, which is worth a test failure.

import { readFileSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'

const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor

const NODE_IMPORT = /^\s*import\s+\{[^}]*\}\s+from\s+'node:[a-z/]+'\s*$/

/**
 * Run a harness file and return everything the test needs.
 *
 * @param {string} file absolute path to the harness
 * @param {object} [opts]
 * @param {any} [opts.args] the value the Workflow `args` global should carry
 * @param {string} [opts.agentReturn] what the stubbed agent() resolves to
 * @returns {Promise<{prompts: string[], calls: object[], result: any, meta: object, source: string}>}
 */
export async function runHarness(file, opts = {}) {
  const source = readFileSync(file, 'utf8')

  const body = source
    .split(/\r?\n/)
    .filter((line) => !NODE_IMPORT.test(line))
    .join('\n')
    .replace(/^export (const|function|class|let)\b/gm, '$1')
    .replace(/^export \{[^}]*\}\s*$/gm, '')
    .replace(/import\.meta\.url/g, '__METAURL__')
    // The body ends in a top-level `return`, so the meta capture has to be
    // injected right after the meta literal rather than appended. The literal
    // closes with a brace in column 0, which is also what the runtime's
    // pure-literal rule implies.
    .replace(/^(const meta = \{[\s\S]*?\n\})$/m, '$1\n__capture.meta = meta')
    .concat('\n')

  const calls = []
  const phases = []
  const logs = []

  const agent = async (prompt, agentOpts = {}) => {
    calls.push({ prompt, opts: agentOpts })
    return opts.agentReturn === undefined ? 'OK' : opts.agentReturn
  }
  const parallel = async (thunks) => Promise.all(thunks.map((t) => t()))
  const phase = (title) => phases.push(title)
  const log = (message) => logs.push(message)

  const fn = new AsyncFunction(
    'phase', 'parallel', 'agent', 'log', 'args',
    'fileURLToPath', 'dirname', 'resolve', '__METAURL__', '__capture',
    body,
  )

  const capture = {}
  const result = await fn(
    phase, parallel, agent, log, opts.args,
    fileURLToPath, dirname, resolve, pathToFileURL(file).href, capture,
  )

  return { prompts: calls.map((c) => c.prompt), calls, result, meta: capture.meta, phases, logs, source }
}

/** The repo root, from this helper's own location. */
export const REPO_ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..', '..')

/**
 * Replace the absolute repo root with a placeholder, so a golden prompt file
 * is identical on every machine and in every worktree.
 */
export function normalizeRoot(text, root = REPO_ROOT) {
  // On Windows the harness builds the root with backslashes while a caller may
  // pass it with forward slashes, so both spellings are replaced.
  const posix = root.replaceAll('\\', '/')
  const win = posix.replaceAll('/', '\\')
  return text.replaceAll(posix, '__ROOT__').replaceAll(win, '__ROOT__')
}
