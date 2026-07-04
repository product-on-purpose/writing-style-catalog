#!/usr/bin/env python3
"""
Score the stable catalog against a described writing situation, per axis.

Implements Phases 1-2 of docs/internal/release-plans/entry-recommender-implementation-plan.md:
loads every stable/reference-quality candidate per axis (never draft, per AC-6),
then scores the ENTIRE pool in one pass (not just a short list) using each axis's
schema-guaranteed facet field plus when_to_use/tells keyword overlap. Optional
facets fold in as bonus signal only - most stable entries omit them.

This is a deterministic pre-filter, not the recommendation itself. The actual
pick-and-justify judgment (Phase 3) happens in the skill's own reasoning per
SKILL.md, using this script's output as its candidate data.

Usage:
    python recommend.py --situation TEXT [--topic TEXT] [--audience TEXT]
                         [--voice ID] [--tone ID] [--style ID] [--format ID]
                         [--short-list-size N] [--json]
    python recommend.py --fetch AXIS ID [--json]
    python recommend.py --list
"""
import argparse
import importlib.util
import json
import math
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]  # 3 levels up from skills/entry-recommender/scripts/
TAXONOMY_ROOT = REPO_ROOT / "taxonomy"

# build-instruction.py already parses ENTRY.md frontmatter without requiring
# PyYAML - deliberately, per its own comment ("Parse YAML manually... avoid
# requiring pyyaml"), since a shipped skill script cannot assume an end user's
# Claude Code / ZIP-installed Python environment has any package beyond the
# standard library. An earlier version of this script used `yaml.safe_load`
# (matching tools/validate.py's pattern) - but that is repo DEV tooling, run
# under requirements-dev.txt in CI/local dev, a completely different
# execution context from a shipped skill script running in an end user's
# environment. Loading build-instruction.py's own load_entry here reuses its
# proven, dependency-free parser directly (its filename has a hyphen, so a
# normal `import` statement cannot name it - hence importlib) rather than
# vendoring a second parser that could drift from it.
_BUILD_INSTRUCTION_PATH = (
    REPO_ROOT / "skills" / "writing-instruction-builder" / "scripts" / "build-instruction.py"
)
_spec = importlib.util.spec_from_file_location("build_instruction", _BUILD_INSTRUCTION_PATH)
build_instruction = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build_instruction)

AXES = {
    "voice": TAXONOMY_ROOT / "voices",
    "tone": TAXONOMY_ROOT / "tones",
    "style": TAXONOMY_ROOT / "styles",
    "format": TAXONOMY_ROOT / "formats",
}

STABLE_STATUSES = {"stable", "reference-quality"}

# The one field each axis's own schema actually guarantees beyond the universal
# set (id/name/axis/one_liner/description/pairs_well_with/avoid_with/
# confusable_with/when_to_use/when_not_to_use/llm_instruction_phrasing/tags/
# review_status/tells/anti_patterns/failure_modes) - verified directly against
# schemas/{voice,tone,style,format}.schema.json's own "required" list, not
# assumed. See the spec's Requirements section and Revision 5.
AXIS_GUARANTEED_FIELDS = {
    "voice": ["family"],
    "tone": ["markers"],
    "style": ["structural_conventions"],
    "format": ["domain", "family"],
}

# Present on some entries, absent on most today - fold in as bonus signal only.
# Never required; absence must never lower a score or raise an error.
AXIS_OPTIONAL_FACETS = {
    "voice": ["subfamily"],
    "tone": ["spectrum", "spectrum_position", "nn_g_profile"],
    "style": ["frame", "classical_mode", "evidence_types", "reader_contract"],
    "format": [],
}

# Common English function words plus a few domain-generic verbs that appear in
# almost every situation description ("write", "need", "want") and would
# otherwise dilute the overlap score against every candidate equally.
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "from",
    "has", "have", "i", "in", "is", "it", "its", "just", "me", "my", "need",
    "of", "on", "or", "our", "should", "so", "that", "the", "their", "them",
    "then", "there", "they", "this", "to", "want", "was", "we", "were",
    "will", "with", "would", "write", "writing", "you", "your",
}

# Calibrated empirically against the spec's own Behavior/Examples during Phase
# 8's smoke test (docs/internal/release-plans/entry-recommender-implementation-plan.md
# Phase 2 Step 4) - not a value with any external source, by the plan's own
# admission ("the one place... a real number needs picking"). See the module
# docstring in build_idf_table for why this is an IDF-weighted score, not a raw
# token count: a raw count let generic words ("something", a stray token from
# an unstripped possessive) clear the bar as easily as a genuinely distinctive
# word ("houseplant", "migration"), which defeated AC-7 in early testing.
DEFAULT_RELEVANCE_THRESHOLD = 3.0

# A single matching token, however rare, is weaker evidence than several
# independently-informative words overlapping - it is exactly as consistent
# with an incidental match (a generic filler word an IDF weight alone does
# not push low enough, or a genuine polysemy collision - the same word in an
# unrelated sense, like "account" meaning a social-media account in the
# situation but a written incident account in a candidate's one_liner) as
# with a real fit. Requiring at least two distinct tokens, on top of the
# weighted score, rejected exactly this failure mode in testing without
# needing a hand-maintained blocklist of specific words.
MIN_DISTINCT_MATCHES = 2

DEFAULT_SHORT_LIST_SIZE = 6

WHEN_TO_USE_WEIGHT = 3
TELLS_WEIGHT = 2
ONE_LINER_WEIGHT = 1
FACET_WEIGHT = 1

# Length >= 2: drops stray single-character fragments a naive alphanumeric
# split produces from possessives and contractions ("houseplant's" -> "s"),
# which otherwise coincidentally match apostrophe fragments in unrelated
# candidate text and contribute score that is pure noise, not signal.
_TOKEN_RE = re.compile(r"[a-z0-9]{2,}")


def load_stable_ids(axis: str) -> list[str]:
    """Return every id for `axis` whose review_status is stable or
    reference-quality, scanned directly from taxonomy/<axis>s/ - not from the
    root taxonomy.json index.

    An earlier version of this function used taxonomy.json for speed. That
    was a real bug: taxonomy.json is a generated build artifact, and the
    release ZIP packaging scripts (scripts/build-release.sh /
    build-release.ps1) do not stage it - confirmed by reading their MEMBERS
    lists directly - so a user installing via the documented ZIP path (as
    opposed to the Claude Code marketplace path) would have gotten a
    taxonomy.json-less install, and this function would have silently
    returned an empty list for every axis with no error. Reading taxonomy/
    directly has no such gap: it is the actual entry data, confirmed present
    in every install path (both packaging scripts' MEMBERS lists include it,
    and it is what build-instruction.py itself already depends on)."""
    return sorted(
        entry_id
        for entry_id, entry in _iter_all_entries(axis)
        if entry.get("review_status") in STABLE_STATUSES
    )


def _iter_all_entries(axis: str):
    """Yield (entry_id, frontmatter) for every entry in `axis` - draft
    included - reusing build-instruction.py's own list_entries for the id
    scan and load_entry for each read, so a draft entry's presence is only
    ever used to check review_status, never to feed a recommendation."""
    for entry_id in build_instruction.list_entries().get(axis, []):
        entry = build_instruction.load_entry(axis, entry_id)
        if entry is not None:
            yield entry_id, entry


def load_full_entry(axis: str, entry_id: str) -> dict | None:
    """Read one entry's full ENTRY.md frontmatter directly - taxonomy.json is
    a slim index (id/name/axis/one_liner/review_status only) and does not
    carry when_to_use, tells, avoid_with, pairs_well_with, or any axis-specific
    facet, so every field this scorer or a caller needs beyond the slim index
    requires this direct read. Delegates to build-instruction.py's own
    load_entry (see the importlib delegation above) rather than a second
    parser - same axis names, same taxonomy/ layout, same frontmatter shape."""
    return build_instruction.load_entry(axis, entry_id)


def _singularize(token: str) -> str:
    """Normalize the one plural pattern common enough, and safe enough, to
    handle without a real stemmer: "-ies" -> "-y" (eulogies -> eulogy,
    categories -> category). Confirmed necessary in testing: a situation
    describing a "eulogy" scored 0 against the `reverent` tone entry, whose
    own field text says "Eulogies," purely on this inflection mismatch -
    a real, avoidable miss on an otherwise clear match.

    Deliberately NOT extended to bare "-s"/"-es" stripping: too many common,
    non-plural English words end that way ("always", "focus", "status",
    "process", "business") for a blanket rule to be safe - it would trade
    this miss for a new class of false match. Broader normalization (real
    stemming, or an embedding-based match) is the spec's own Open Question 2,
    deliberately deferred, not a gap introduced here."""
    if token.endswith("ies") and len(token) > 4:
        return token[:-3] + "y"
    return token


def tokenize(text) -> set[str]:
    """Lowercase, alphanumeric-only tokens, stopwords removed, then the one
    safe pluralization normalized (see _singularize). Accepts a string, a
    list of strings (joined), or None."""
    if text is None:
        return set()
    if isinstance(text, list):
        text = " ".join(str(t) for t in text)
    tokens = {_singularize(t) for t in _TOKEN_RE.findall(str(text).lower())}
    return tokens - STOPWORDS


def _facet_text(axis: str, entry: dict) -> str:
    """Join every guaranteed and present-optional facet value into one string
    for tokenizing. Absence of an optional facet is silent - never an error,
    never a reason to score lower than the guaranteed field alone would."""
    parts = []
    for field in AXIS_GUARANTEED_FIELDS.get(axis, []):
        value = entry.get(field)
        if value:
            parts.append(str(value) if not isinstance(value, list) else " ".join(str(v) for v in value))
    for field in AXIS_OPTIONAL_FACETS.get(axis, []):
        value = entry.get(field)
        if value:
            parts.append(str(value) if not isinstance(value, list) else " ".join(str(v) for v in value))
    return " ".join(parts)


def load_all_stable_entries() -> dict[str, dict[str, dict]]:
    """Load every stable/reference-quality entry's full frontmatter, across
    all axes, once. Returns {axis: {entry_id: frontmatter}}. Reused both to
    build the corpus-wide IDF table below and to score each axis's pool, so
    each entry (stable or draft) is read exactly once per invocation, not
    twice - a draft entry is opened only long enough to see its
    review_status and is then dropped, never reaching scoring or output."""
    cache = {}
    for axis in AXES:
        cache[axis] = {
            entry_id: entry
            for entry_id, entry in _iter_all_entries(axis)
            if entry.get("review_status") in STABLE_STATUSES
        }
    return cache


def _entry_text(axis: str, entry: dict) -> str:
    """Every field this scorer considers, joined into one string."""
    return " ".join(
        [
            str(entry.get("one_liner", "") or ""),
            " ".join(str(x) for x in (entry.get("when_to_use") or [])),
            " ".join(str(x) for x in (entry.get("tells") or [])),
            _facet_text(axis, entry),
        ]
    )


def build_idf_table(all_entries: dict[str, dict[str, dict]]) -> dict:
    """Corpus-wide inverse document frequency per token, computed once from
    every stable entry's combined text.

    A raw keyword-overlap count treats every matching word as equally
    informative, which does not hold in practice: a token that appears in most
    entries' when_to_use/tells ("reader", "writing"-adjacent words the
    stopword list does not happen to name) contributes score for almost any
    situation, while a token distinctive to only one or two entries
    ("houseplant", "migration", "postmortem") is genuine topical signal. IDF
    weighting (classic information-retrieval technique, pure counting and a
    log - no embeddings, no external call) makes that distinction without a
    hand-maintained blocklist of generic words, which is always incomplete -
    confirmed necessary when an early version of this scorer, using raw counts,
    let "something" clear the relevance bar as easily as a genuinely
    distinctive word.
    """
    doc_count = 0
    df: dict[str, int] = {}
    for axis, entries in all_entries.items():
        for entry in entries.values():
            doc_count += 1
            for token in tokenize(_entry_text(axis, entry)):
                df[token] = df.get(token, 0) + 1
    return {"doc_count": doc_count, "df": df}


def _idf(token: str, idf_table: dict) -> float:
    doc_count = idf_table["doc_count"] or 1
    df = idf_table["df"].get(token, 0)
    return math.log(doc_count / (1 + df))


def _weighted_overlap(situation_tokens: set[str], field_tokens: set[str], weight: float, idf_table: dict) -> float:
    return weight * sum(_idf(t, idf_table) for t in (situation_tokens & field_tokens))


def score_entry(situation_tokens: set[str], axis: str, entry: dict, idf_table: dict) -> dict:
    """IDF-weighted score plus the count of distinct situation tokens matched
    anywhere in the entry (see MIN_DISTINCT_MATCHES). when_to_use counts most
    per token (it is the field AC-3 anchors justifications on); tells next;
    one_liner and facets are lighter signals. Each matching token additionally
    contributes more the rarer it is across the whole stable corpus (see
    build_idf_table). Pure set intersection and arithmetic - no embeddings, no
    external calls, per the spec's Non-Functional Requirements.

    Also returns exactly which situation tokens matched, per field - a score
    with no visibility into which words drove it is not auditable from the
    documented workflow alone (confirmed during Phase 8 testing: a match
    hiding inside a facet field, invisible in this script's own output,
    required reading the raw ENTRY.md directly to explain a low-confidence
    false positive)."""
    when_to_use_tokens = tokenize(entry.get("when_to_use"))
    tells_tokens = tokenize(entry.get("tells"))
    one_liner_tokens = tokenize(entry.get("one_liner"))
    facet_tokens = tokenize(_facet_text(axis, entry))

    score = (
        _weighted_overlap(situation_tokens, when_to_use_tokens, WHEN_TO_USE_WEIGHT, idf_table)
        + _weighted_overlap(situation_tokens, tells_tokens, TELLS_WEIGHT, idf_table)
        + _weighted_overlap(situation_tokens, one_liner_tokens, ONE_LINER_WEIGHT, idf_table)
        + _weighted_overlap(situation_tokens, facet_tokens, FACET_WEIGHT, idf_table)
    )
    matched_tokens = {
        "when_to_use": sorted(situation_tokens & when_to_use_tokens),
        "tells": sorted(situation_tokens & tells_tokens),
        "one_liner": sorted(situation_tokens & one_liner_tokens),
        "facets": sorted(situation_tokens & facet_tokens),
    }
    distinct_matches = len(set().union(*matched_tokens.values()))
    return {"score": round(score, 2), "distinct_matches": distinct_matches, "matched_tokens": matched_tokens}


def build_ranked_list(
    axis: str,
    situation_tokens: set[str],
    all_entries: dict[str, dict[str, dict]],
    idf_table: dict,
    threshold: float = DEFAULT_RELEVANCE_THRESHOLD,
) -> list[dict]:
    """Score every stable candidate for `axis`, sorted highest-score first.
    Ties broken by id for a stable, reproducible order. Returns the FULL pool,
    not a top-N slice - conflict resolution (Phase 5) needs the whole ranked
    list, already scored, to widen into without a second pass. A candidate
    clears `above_threshold` only if BOTH the weighted score clears the bar
    AND at least MIN_DISTINCT_MATCHES distinct situation tokens matched -
    either alone lets a single incidental word masquerade as a genuine fit."""
    results = []
    for entry_id, entry in all_entries.get(axis, {}).items():
        scored = score_entry(situation_tokens, axis, entry, idf_table)
        above = scored["score"] >= threshold and scored["distinct_matches"] >= MIN_DISTINCT_MATCHES
        results.append(
            {
                "id": entry_id,
                "score": scored["score"],
                "distinct_matches": scored["distinct_matches"],
                "above_threshold": above,
                "one_liner": entry.get("one_liner", ""),
                # Which situation words actually matched, per field - lets a
                # caller (or a human) see AT A GLANCE whether a score is
                # driven by a genuine when_to_use/tells match or by a single
                # word hiding in a rarely-read facet field, without having to
                # open the raw ENTRY.md to find out.
                "matched_tokens": scored["matched_tokens"],
            }
        )
    results.sort(key=lambda r: (-r["score"], r["id"]))
    return results


def _select_short_list(ranked: list[dict], short_list_size: int) -> list[dict]:
    """Select the short list from the full ranked pool, putting every
    `above_threshold: True` candidate ahead of every non-qualifying one,
    regardless of raw score.

    Pure top-N-by-score would not guarantee this: a single very rare word
    (high IDF) in a high-weight field can score higher than a genuine
    two-distinct-token match, even though the single-token match fails
    `above_threshold` (MIN_DISTINCT_MATCHES) and the two-token one passes it.
    If short_list_size candidates already score higher by raw number alone,
    the genuinely-qualifying one would be pushed into `full_ranked`, where
    Step 2's low-confidence check would never see it - confirmed as a real
    design gap by an adversarial review, even though no live catalog example
    was found to trigger it with today's entries; the gap is structural, not
    dependent on this specific corpus staying small. Within each group
    (qualifying, then non-qualifying), `ranked`'s existing score order is
    preserved."""
    qualifying = [r for r in ranked if r["above_threshold"]]
    non_qualifying = [r for r in ranked if not r["above_threshold"]]
    return (qualifying + non_qualifying)[:short_list_size]


def _situation_tokens(situation: str | None, topic: str | None, audience: str | None) -> set[str]:
    combined = " ".join(t for t in (situation, topic, audience) if t)
    return tokenize(combined)


def recommend(
    situation: str | None,
    topic: str | None = None,
    audience: str | None = None,
    fixed: dict | None = None,
    short_list_size: int = DEFAULT_SHORT_LIST_SIZE,
    threshold: float = DEFAULT_RELEVANCE_THRESHOLD,
) -> dict:
    """Build the per-axis ranked lists and short lists. `fixed` is a dict of
    axis -> entry_id for any axis the caller already fixed (Phase 4) - a fixed
    axis is validated against the stable pool and never scored."""
    fixed = fixed or {}
    situation_tokens = _situation_tokens(situation, topic, audience)
    all_entries = load_all_stable_entries()
    idf_table = build_idf_table(all_entries)
    axes_out = {}
    errors = []

    for axis in AXES:
        fixed_id = fixed.get(axis)
        if fixed_id:
            stable_ids = list(all_entries.get(axis, {}).keys())
            if fixed_id not in stable_ids:
                errors.append(
                    f"Fixed {axis}={fixed_id!r} is not in the stable/reference-quality catalog."
                )
                axes_out[axis] = {"fixed": fixed_id, "valid": False}
            else:
                axes_out[axis] = {"fixed": fixed_id, "valid": True}
            continue

        ranked = build_ranked_list(axis, situation_tokens, all_entries, idf_table, threshold)
        short_list_entries = _select_short_list(ranked, short_list_size)
        short_list_ids = {r["id"] for r in short_list_entries}
        short_list = []
        for r in short_list_entries:
            entry = load_full_entry(axis, r["id"])
            short_list.append(
                {
                    **r,
                    "when_to_use": (entry or {}).get("when_to_use", []),
                    "tells": (entry or {}).get("tells", []),
                }
            )
        axes_out[axis] = {
            "fixed": None,
            "candidate_count": len(ranked),
            "short_list": short_list,
            # Full ranked list, id+score+matched_tokens (cheap - no full field
            # text) - Phase 5's widened search walks this past the short
            # list's cutoff with no re-scoring. matched_tokens is included so
            # a widened-search candidate's relevance can be sanity-checked
            # before fetching its full fields: a candidate whose only match is
            # a single generic-feeling word is a signal to look closer (or
            # skip it) even before Step 2's read-based check runs on it.
            "full_ranked": [
                {
                    "id": r["id"],
                    "score": r["score"],
                    "above_threshold": r["above_threshold"],
                    "matched_tokens": r["matched_tokens"],
                }
                for r in ranked
                if r["id"] not in short_list_ids
            ],
        }

    return {
        "situation_tokens": sorted(situation_tokens),
        "relevance_threshold": threshold,
        "short_list_size": short_list_size,
        "axes": axes_out,
        "errors": errors,
    }


def fetch_one(axis: str, entry_id: str) -> dict:
    """Full field content for exactly one candidate - used when Phase 5's
    widened search selects a candidate beyond the short list and needs its
    when_to_use/tells for a real Phase 3 Step 2 justification, without paying
    the cost of returning full fields for the whole pool up front.

    Enforces the same stable/reference-quality boundary as scoring and
    listing (AC-6) by checking membership in load_stable_ids(axis) BEFORE any
    filesystem access, not after loading. An earlier version of this
    function checked review_status only after loading - which was itself a
    real gap (a draft entry's fields were returned in full: verified via
    `--fetch format acceptance-speech`) - but checking only a loaded entry's
    own review_status is not enough by itself either: load_full_entry builds
    a path as AXES[axis] / entry_id / "ENTRY.md" with no containment check,
    so a crafted entry_id such as "../voices/pragmatic-architect" escapes
    the intended axis directory entirely and returns a DIFFERENT axis's
    stable entry, mislabeled as belonging to the requested one - confirmed
    live: `--fetch format "../voices/pragmatic-architect"` returned the real
    `pragmatic-architect` voice entry tagged `"axis": "format"`. Checking
    membership first closes this - load_stable_ids only ever contains real
    directory names this process already enumerated itself via
    build_instruction.list_entries, never a caller-supplied string, so a
    path is only ever built from a name already known to be safe."""
    if axis not in AXES:
        return {"found": False, "error": f"unknown axis: {axis}"}
    if entry_id not in load_stable_ids(axis):
        return {
            "found": False,
            "id": entry_id,
            "axis": axis,
            "error": f"{entry_id!r} is not a stable/reference-quality {axis} entry",
        }
    entry = load_full_entry(axis, entry_id)
    if entry is None:
        return {"found": False, "id": entry_id, "axis": axis}
    facets = {
        field: entry[field]
        for field in AXIS_GUARANTEED_FIELDS.get(axis, []) + AXIS_OPTIONAL_FACETS.get(axis, [])
        if entry.get(field)
    }
    return {
        "found": True,
        "id": entry_id,
        "axis": axis,
        "one_liner": entry.get("one_liner", ""),
        "when_to_use": entry.get("when_to_use", []),
        "tells": entry.get("tells", []),
        "avoid_with": entry.get("avoid_with", []),
        "pairs_well_with": entry.get("pairs_well_with", []),
        "review_status": entry.get("review_status", ""),
        # The facet field(s) that feed part of this candidate's score (see
        # AXIS_GUARANTEED_FIELDS / AXIS_OPTIONAL_FACETS) - present here so a
        # caller can see everything that contributed to a score without a raw
        # ENTRY.md read, only the guaranteed/optional fields that actually
        # have a value on this entry.
        "facets": facets,
    }


def list_stable() -> dict[str, list[str]]:
    return {axis: load_stable_ids(axis) for axis in AXES}


def main():
    parser = argparse.ArgumentParser(
        description="Score the stable catalog against a described writing situation, per axis."
    )
    parser.add_argument(
        "--ephemeral-input-file",
        type=Path,
        help=(
            "Same JSON payload as --input-file, but this process deletes the "
            "file itself immediately after reading it (in a finally block, so "
            "cleanup happens even if the JSON is malformed or scoring later "
            "raises) - THE PREFERRED way for an agent to pass real situation "
            "text, which can be sensitive (HR, incident, customer detail). "
            "Cleanup does not depend on a separate agent-followed instruction "
            "step; it is guaranteed by this process's own control flow. Write "
            "the file with a file-write tool (never a shell command) to a "
            "temp/scratchpad location outside the project directory; the "
            "situation text must be properly JSON-string-escaped first "
            "(backslash, quote, newline, etc.) - see SKILL.md Step 1."
        ),
    )
    parser.add_argument(
        "--input-file",
        type=Path,
        help=(
            "Same JSON payload, but this process does NOT delete the file - "
            "for a deliberately-kept test fixture reused across runs, not "
            "day-to-day use with real (possibly sensitive) situation text. "
            "Prefer --ephemeral-input-file for that. --situation below is a "
            "convenience for direct manual/terminal use, where the caller "
            "controls their own shell escaping - a caller assembling this "
            "command from untrusted text (an agent following SKILL.md, for "
            "example) MUST use --ephemeral-input-file instead."
        ),
    )
    parser.add_argument(
        "--stdin",
        action="store_true",
        help=(
            "Read the same JSON payload --input-file takes from stdin instead "
            "of a file. NOT recommended for untrusted situation text piped via "
            "a shell heredoc: a heredoc's closing delimiter is plain text "
            "matched against the body, so situation text containing that exact "
            "line terminates it early and whatever follows is executed as a "
            "new shell command - a real risk if the delimiter is fixed and "
            "predictable (for example, one written into this file's own "
            "history). Safe only when the JSON is supplied by a mechanism with "
            "no delimiter-collision risk, such as another process's stdout "
            "piped directly in. Prefer --input-file for an agent workflow."
        ),
    )
    parser.add_argument("--situation", help="Free-text description of the writing situation (manual/terminal use only - see --input-file)")
    parser.add_argument("--topic", help="Optional topic, folded into the situation tokens")
    parser.add_argument("--audience", help="Optional audience, folded into the situation tokens")
    parser.add_argument("--voice", help="Fixed voice entry id (skip scoring this axis)")
    parser.add_argument("--tone", help="Fixed tone entry id (skip scoring this axis)")
    parser.add_argument("--style", help="Fixed style entry id (skip scoring this axis)")
    parser.add_argument("--format", dest="fmt", help="Fixed format entry id (skip scoring this axis)")
    parser.add_argument("--short-list-size", type=int, default=DEFAULT_SHORT_LIST_SIZE)
    parser.add_argument("--threshold", type=float, default=DEFAULT_RELEVANCE_THRESHOLD)
    parser.add_argument("--fetch", nargs=2, metavar=("AXIS", "ID"), help="Fetch one candidate's full fields")
    parser.add_argument("--list", action="store_true", help="List all stable/reference-quality ids per axis")
    parser.add_argument("--json", dest="output_json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.list:
        result = list_stable()
        if args.output_json:
            print(json.dumps(result, indent=2))
        else:
            for axis, ids in result.items():
                print(f"\n{axis.upper()} ({len(ids)})")
                for i in ids:
                    print(f"  {i}")
        return

    if args.fetch:
        axis, entry_id = args.fetch
        result = fetch_one(axis, entry_id)
        print(json.dumps(result, indent=2) if args.output_json else result)
        return

    if args.stdin or args.input_file or args.ephemeral_input_file:
        if args.ephemeral_input_file:
            # Delete as part of THIS process's own execution, in a finally
            # block, rather than relying on a separate agent-instructed
            # cleanup step - confirmed necessary by an adversarial review:
            # "delete it after" as a SKILL.md instruction is only followed if
            # the agent actually reaches that step, and situation text can be
            # sensitive (HR matters, incident detail). This runs regardless
            # of whether json.loads or recommend() below succeeds or raises.
            try:
                raw = args.ephemeral_input_file.read_text(encoding="utf-8")
            finally:
                args.ephemeral_input_file.unlink(missing_ok=True)
        else:
            raw = sys.stdin.read() if args.stdin else args.input_file.read_text(encoding="utf-8")
        payload = json.loads(raw)
        situation = payload.get("situation")
        topic = payload.get("topic")
        audience = payload.get("audience")
        fixed = {
            axis: payload[axis]
            for axis in ("voice", "tone", "style", "format")
            if payload.get(axis)
        }
        short_list_size = payload.get("short_list_size", DEFAULT_SHORT_LIST_SIZE)
        threshold = payload.get("threshold", DEFAULT_RELEVANCE_THRESHOLD)
    else:
        situation = args.situation
        topic = args.topic
        audience = args.audience
        fixed = {}
        if args.voice:
            fixed["voice"] = args.voice
        if args.tone:
            fixed["tone"] = args.tone
        if args.style:
            fixed["style"] = args.style
        if args.fmt:
            fixed["format"] = args.fmt
        short_list_size = args.short_list_size
        threshold = args.threshold

    if not situation:
        parser.error("situation is required (the \"situation\" key via --ephemeral-input-file, --input-file, or --stdin, or --situation) unless --list or --fetch is used")

    result = recommend(
        situation=situation,
        topic=topic,
        audience=audience,
        fixed=fixed,
        short_list_size=short_list_size,
        threshold=threshold,
    )
    print(json.dumps(result, indent=2))  # structured output is this tool's only real output shape


if __name__ == "__main__":
    main()
