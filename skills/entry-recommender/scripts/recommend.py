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
                         [--short-list-size N] [--response-format concise|detailed]
                         [--pretty] [--debug] [--json]
    python recommend.py --fetch AXIS ID [--json] [--pretty]
    python recommend.py --fetch-many AXIS ID [ID ...] [--json] [--pretty]
    python recommend.py --list [--json] [--pretty]
"""
import argparse
import importlib.util
import json
import math
import re
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]  # 3 levels up from skills/entry-recommender/scripts/
TAXONOMY_ROOT = REPO_ROOT / "taxonomy"

# Required filename suffix for --ephemeral-input-file - see _assert_safe_to_delete.
EPHEMERAL_SUFFIX = ".entry-recommender-input.json"

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
# Interface guard: the two skills version independently (library.json), so a
# refactor of build-instruction.py must fail HERE with a named contract
# violation, not later as an unguided AttributeError mid-recommendation.
for _sym in ("list_entries", "load_entry"):
    if not hasattr(build_instruction, _sym):
        raise ImportError(
            f"build-instruction.py is missing expected symbol {_sym!r}; the two "
            "skills' versions may be out of sync (see library.json components)."
        )

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
    """Select the short list from the full ranked pool.

    ALL `above_threshold: True` candidates are included, however many there
    are - `short_list_size` never truncates the qualifying group. An
    adversarial review found this the hard way: for a real, ordinary
    situation ("telling my engineering team a feature is getting cut..."),
    31 of the 52 stable Format entries cleared `above_threshold` - a
    short_list_size of 6 would have silently hidden 25 of them from Step 2's
    read, in `full_ranked` where they never get their full field text read,
    on a genuinely common case, not a rare edge case. AC-7's low-confidence
    decision and Step 2's actual pick both depend on seeing every candidate
    that genuinely clears the bar, not just the highest-scoring handful of
    them - correctness here matters more than a tidy, fixed-size list.
    `short_list_size` still bounds how many EXTRA non-qualifying candidates
    are shown for context/comparison when there are FEWER qualifying
    candidates than that - it is a floor for a short list, not a ceiling on
    genuine matches. Within each group (qualifying, then non-qualifying),
    `ranked`'s existing score order is preserved."""
    qualifying = [r for r in ranked if r["above_threshold"]]
    non_qualifying = [r for r in ranked if not r["above_threshold"]]
    padding_needed = max(0, short_list_size - len(qualifying))
    return qualifying + non_qualifying[:padding_needed]


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
    response_format: str = "concise",
    debug: bool = False,
) -> dict:
    """Build the per-axis ranked lists and short lists. `fixed` is a dict of
    axis -> entry_id for any axis the caller already fixed (Phase 4) - a fixed
    axis is validated against the stable pool and never scored.

    response_format controls the output contract:
    - "concise" (default): tiered short_list. The first `short_list_size`
      above_threshold rows (read tier) carry full fields
      (when_to_use/tells/when_not_to_use). All other rows are lean
      (id/score/distinct_matches/above_threshold/one_liner/matched_tokens
      plus "fields": "fetch") - this covers BOTH qualifying candidates beyond
      short_list_size (triage tier) AND non-qualifying padding rows. A lean
      row must be fetched via --fetch-many before a pick can be made from it
      (qualifying triage rows); non-qualifying padding rows are not pick
      candidates. full_ranked is omitted unless debug=True.
    - "detailed": legacy behavior - full fields for all short_list entries,
      full_ranked always present. Use when you want everything inline.

    Floor case (0 qualifying candidates): every short_list row is lean; no
    full-field loading occurs. Payload collapses to roughly the K=0 figure.
    Typical case (qualifying <= short_list_size): qualifying rows get full
    fields; non-qualifying padding rows are lean (the B-1 fix).
    High-qualifying case (qualifying > short_list_size): first short_list_size
    qualifying rows are full (read tier); remaining qualifying rows are lean
    (triage tier); no padding rows exist.

    C1 guarantee holds in both modes: every above_threshold candidate appears
    somewhere in short_list (read tier or lean triage). No qualifying candidate
    is ever hidden from the caller.
    """
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
        all_short_list_entries = _select_short_list(ranked, short_list_size)

        if response_format == "detailed":
            # Legacy behavior: full fields for every short_list entry.
            short_list_ids = {r["id"] for r in all_short_list_entries}
            short_list = []
            for r in all_short_list_entries:
                entry = load_full_entry(axis, r["id"])
                short_list.append(
                    {
                        **r,
                        "when_to_use": (entry or {}).get("when_to_use", []),
                        "tells": (entry or {}).get("tells", []),
                        # A required universal field, same as when_to_use - an
                        # adversarial review found it was never surfaced, so a
                        # candidate could score well on positive language while
                        # its own when_not_to_use explicitly disqualifies the
                        # situation, with Step 2's read never seeing the
                        # contradiction because the field was not even in this
                        # payload. Deliberately not folded into the score itself
                        # (a negative-overlap penalty risks the same polysemy
                        # false-positive/negative class already found and fixed
                        # for the positive fields) - this is a Step 2 read-based
                        # check, the same division of labor as everywhere else.
                        "when_not_to_use": (entry or {}).get("when_not_to_use", []),
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
        else:
            # Concise mode (default): tiered short_list.
            # Full fields go ONLY to the first short_list_size qualifying
            # candidates (read tier). Every other row is lean, carrying
            # "fields": "fetch" and physically lacking when_to_use/tells/
            # when_not_to_use. "Every other row" covers two distinct groups:
            #
            # (a) Qualifying candidates beyond short_list_size (triage tier):
            #     above_threshold True, must be fetched before picking.
            # (b) Non-qualifying padding rows: above_threshold False, added
            #     by _select_short_list only when qualifying < short_list_size.
            #     These are near-miss context, not pick candidates; no fetch
            #     is needed unless citing one in an AC-7 justification.
            #
            # Triage and padding are mutually exclusive: padding appears only
            # when qualifying < short_list_size, which means no triage exists.
            #
            # Consequences:
            #   Floor case (0 qualifying): all rows are padding -> all lean ->
            #     payload collapses to roughly the K=0 figure (no full-field
            #     loading at all, regardless of short_list_size).
            #   Typical case (qualifying <= short_list_size): qualifying rows
            #     get full fields; padding rows are lean (B-1 fix).
            #   High-qualifying case (qualifying > short_list_size): first K
            #     qualifying rows are full (read tier); remaining qualifying
            #     rows are lean triage; no padding rows.
            qualifying_sl = [r for r in all_short_list_entries if r["above_threshold"]]
            non_qualifying_sl = [r for r in all_short_list_entries if not r["above_threshold"]]
            read_tier = qualifying_sl[:short_list_size]
            lean_triage = qualifying_sl[short_list_size:]
            lean_padding = non_qualifying_sl

            short_list = []
            for r in read_tier:
                entry = load_full_entry(axis, r["id"])
                short_list.append(
                    {
                        **r,
                        "when_to_use": (entry or {}).get("when_to_use", []),
                        "tells": (entry or {}).get("tells", []),
                        "when_not_to_use": (entry or {}).get("when_not_to_use", []),
                    }
                )
            for r in lean_triage:
                # Lean row (triage): qualifying candidate beyond the read tier.
                # "fields": "fetch" sentinel - must fetch full fields before
                # picking; never pick from a lean row without reading it first.
                short_list.append(
                    {
                        "id": r["id"],
                        "score": r["score"],
                        "distinct_matches": r["distinct_matches"],
                        "above_threshold": r["above_threshold"],
                        "one_liner": r["one_liner"],
                        "matched_tokens": r["matched_tokens"],
                        "fields": "fetch",
                    }
                )
            for r in lean_padding:
                # Lean row (padding): non-qualifying candidate, near-miss context
                # only (not a pick candidate). Cite in an AC-7 justification only
                # after fetching - "fields": "fetch" means its own language is not
                # available inline and quoting it requires a --fetch-many call.
                short_list.append(
                    {
                        "id": r["id"],
                        "score": r["score"],
                        "distinct_matches": r["distinct_matches"],
                        "above_threshold": r["above_threshold"],
                        "one_liner": r["one_liner"],
                        "matched_tokens": r["matched_tokens"],
                        "fields": "fetch",
                    }
                )

            axis_data: dict = {
                "fixed": None,
                "candidate_count": len(ranked),
                "short_list": short_list,
            }
            if debug:
                # full_ranked is only included in debug mode. In normal concise
                # operation it is not needed: every qualifying candidate is already
                # in short_list (read or triage tier), so full_ranked would be
                # exclusively non-qualifying entries with no additional signal for
                # the Step 2 workflow. --debug is for humans diagnosing scores.
                short_list_ids = {r["id"] for r in all_short_list_entries}
                axis_data["full_ranked"] = [
                    {
                        "id": r["id"],
                        "score": r["score"],
                        "above_threshold": r["above_threshold"],
                        "matched_tokens": r["matched_tokens"],
                    }
                    for r in ranked
                    if r["id"] not in short_list_ids
                ]
            axes_out[axis] = axis_data

    return {
        "situation_tokens": sorted(situation_tokens),
        "relevance_threshold": threshold,
        "short_list_size": short_list_size,
        "axes": axes_out,
        "errors": errors,
    }


def fetch_one(axis: str, entry_id: str, _stable_ids=None) -> dict:
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
    path is only ever built from a name already known to be safe.

    `_stable_ids` is an internal-only parameter for callers (i.e. fetch_many)
    that have already hoisted the whitelist computation to avoid an O(N x M)
    re-scan per id. When provided, it is used directly; when None (the default
    for all external callers), load_stable_ids(axis) is called here as normal.
    The gate logic is single-sourced here regardless of which path is taken."""
    if axis not in AXES:
        return {"found": False, "error": f"unknown axis: {axis}"}
    stable_ids = _stable_ids if _stable_ids is not None else load_stable_ids(axis)
    if entry_id not in stable_ids:
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
        "when_not_to_use": entry.get("when_not_to_use", []),
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


def fetch_many(axis: str, ids: list[str]) -> list[dict]:
    """Full field content for multiple candidates in one call, returned as a
    list in the same order as `ids`. Each id passes through the exact same
    stable-membership gate as fetch_one: a list-derived whitelist check that
    the id is a real stable/reference-quality catalog entry, with no path
    construction from caller strings.

    Implemented as a loop over fetch_one (not a reimplementation of its gate)
    to guarantee identical gate behavior per id. The history here is load-
    bearing: two path-traversal bugs were found and fixed in the original
    hardening of fetch_one. This function inherits all of those fixes
    automatically by delegating, rather than by copying and possibly
    drifting from the hardened version.

    The whitelist (load_stable_ids result) is hoisted once and passed into
    each fetch_one call via `_stable_ids` to avoid an O(N x axis-size)
    re-scan. For an unknown axis, `_stable_ids` is None and fetch_one handles
    it via its own axis-not-in-AXES guard, same as a direct fetch_one call.
    The gate logic is single-sourced in fetch_one regardless.

    C6 (security): ids placed into --fetch-many originate only from this
    script's own JSON output (short_list entries carrying "fields": "fetch");
    the ephemeral-input mechanism is untouched. Never pass caller-supplied
    strings from outside the script's own output."""
    stable_ids = load_stable_ids(axis) if axis in AXES else None
    return [fetch_one(axis, entry_id, _stable_ids=stable_ids) for entry_id in ids]


def list_stable() -> dict[str, list[str]]:
    return {axis: load_stable_ids(axis) for axis in AXES}


def _require_ephemeral_path_is_safe(path: Path) -> Path:
    """Raise if `path` is not safe to delete via --ephemeral-input-file;
    otherwise return the resolved path the caller must use for BOTH the read
    and the delete.

    Returning the resolved path (rather than letting the caller re-use the
    original, possibly-symlinked one) closes a real gap an independent
    review found: checking `path.resolve()` here but then reading/deleting
    the original `path` in main() meant a symlink sitting inside the repo,
    pointing at a legitimate temp target, could pass every check here (its
    RESOLVED target is outside the repo and correctly named) while `unlink()`
    in main() removed the symlink object itself, not the file this function
    actually validated. Checking and acting on the same path removes the
    inconsistency entirely.

    Three independent conditions must ALL hold - any one alone is not
    sufficient defense in depth against a caller path mistake, which an
    earlier adversarial review confirmed is a real risk (this flag,
    unguarded, deleted an arbitrary non-JSON file passed to it by mistake).
    Every failure message says outright that nothing was deleted and that
    the caller must clean up manually if the path holds real, possibly
    sensitive text - a second adversarial review found that a caller whose
    scratch location does not happen to satisfy condition 2 would otherwise
    get a raised exception with no indication that the file was left behind:
    1. The resolved path is NOT inside this repository at all - deleting
       anything under REPO_ROOT is never acceptable for this flag,
       regardless of what a temp-directory check below concludes.
    2. The resolved path IS inside the system temp directory
       (tempfile.gettempdir() - covers OS temp roots and session-scoped
       scratchpad directories nested under them, since a scratchpad path is
       itself a subdirectory of the system temp root on this environment).
    3. The filename ends with EPHEMERAL_SUFFIX - a marker that only a file
       actually intended for this mechanism would carry, so even a stray
       file that happens to sit in a temp directory for an unrelated reason
       is not deleted by accident.
    """
    resolved = path.resolve()
    if resolved.is_relative_to(REPO_ROOT.resolve()):
        raise ValueError(
            f"--ephemeral-input-file refuses to touch a path inside the repository: {resolved} "
            f"- nothing was read or deleted; if this file holds real situation text, delete it yourself."
        )
    temp_root = Path(tempfile.gettempdir()).resolve()
    if not resolved.is_relative_to(temp_root):
        raise ValueError(
            f"--ephemeral-input-file requires a path inside the system temp directory "
            f"({temp_root}), got: {resolved} - nothing was read or deleted; if this file "
            f"holds real situation text, delete it yourself now."
        )
    if not resolved.name.endswith(EPHEMERAL_SUFFIX):
        raise ValueError(
            f"--ephemeral-input-file requires a filename ending in {EPHEMERAL_SUFFIX!r}, "
            f"got: {resolved.name!r} - nothing was read or deleted; if this file holds real "
            f"situation text, delete it yourself now."
        )
    return resolved


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
            "step; it is guaranteed by this process's own control flow. This "
            "deletes whatever path you pass, so three conditions are enforced "
            f"first, all required: the path must NOT be inside this repo, MUST "
            f"be inside the system temp directory, and its filename MUST end "
            f"in {EPHEMERAL_SUFFIX!r} - anything else raises instead of "
            f"reading or deleting anything (a caller path mistake must fail "
            f"loudly, not silently destroy the wrong file). Write the file "
            f"with a file-write tool (never a shell command) to a temp/"
            f"scratchpad location outside the project directory, with a "
            f"filename ending in {EPHEMERAL_SUFFIX!r}; the situation text must "
            f"be properly JSON-string-escaped first (backslash, quote, "
            f"newline, etc.) - see SKILL.md Step 1."
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
    parser.add_argument(
        "--short-list-size",
        type=int,
        default=DEFAULT_SHORT_LIST_SIZE,
        help="Floor for how many non-qualifying candidates pad the short list when there are "
        "fewer qualifying ones than this - never a cap on genuinely qualifying candidates. "
        "Must be a non-negative integer.",
    )
    parser.add_argument("--threshold", type=float, default=DEFAULT_RELEVANCE_THRESHOLD)
    parser.add_argument("--fetch", nargs=2, metavar=("AXIS", "ID"), help="Fetch one candidate's full fields")
    parser.add_argument(
        "--fetch-many",
        nargs="+",
        metavar="AXIS_OR_ID",
        help=(
            "Fetch multiple candidates' full fields in one call: "
            "--fetch-many AXIS ID [ID ...]. Each id passes through the same "
            "stable-membership gate as --fetch (list-derived whitelist, no path "
            "construction from caller strings). Returns a JSON array with one "
            "result per id, in the order given. Use for triage-tier lean rows "
            "(those with \"fields\": \"fetch\") when one_liner or matched_tokens "
            "suggest a candidate may be competitive with the read tier."
        ),
    )
    parser.add_argument("--list", action="store_true", help="List all stable/reference-quality ids per axis")
    parser.add_argument(
        "--response-format",
        choices=["concise", "detailed"],
        default="concise",
        help=(
            "Output contract for the recommend path. "
            "\"concise\" (default): tiered short_list - read tier (first "
            "short_list_size above_threshold rows) carries full "
            "when_to_use/tells/when_not_to_use; all other rows are lean "
            "(qualifying triage rows AND non-qualifying padding rows) and carry "
            "\\\"fields\\\": \\\"fetch\\\" marker; full_ranked omitted unless --debug. "
            "\"detailed\": legacy full-fields-for-all-short_list-entries behavior, "
            "full_ranked always emitted."
        ),
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help=(
            "Include full_ranked in the output (omitted by default in concise mode). "
            "full_ranked contains only non-qualifying entries in concise mode, since "
            "every qualifying candidate is already in short_list. Use for diagnosing "
            "scores, not as part of the documented Step 2 workflow."
        ),
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output with indent=2. Default is compact JSON (no whitespace). The model never needed the whitespace; this flag is for human inspection.",
    )
    parser.add_argument("--json", dest="output_json", action="store_true", help="Output as JSON (for --list and --fetch; the recommend path always outputs JSON)")

    args = parser.parse_args()

    if args.short_list_size < 0:
        parser.error("--short-list-size must be a non-negative integer")

    # Fail loudly on mutually exclusive flag combinations rather than silently
    # dropping one of the requested operations (A-6 "fail loudly" principle).
    if args.fetch and args.fetch_many:
        parser.error("--fetch and --fetch-many are mutually exclusive; use one or the other")

    indent = 2 if args.pretty else None

    if args.list:
        result = list_stable()
        if args.output_json:
            print(json.dumps(result, indent=indent))
        else:
            for axis, ids in result.items():
                print(f"\n{axis.upper()} ({len(ids)})")
                for i in ids:
                    print(f"  {i}")
        return

    if args.fetch:
        axis, entry_id = args.fetch
        result = fetch_one(axis, entry_id)
        # Always emit JSON: --fetch output is a structured dict. Previously this
        # required --json; without it, print(result) emitted Python repr (not
        # valid JSON). Made consistent with --fetch-many which always emits JSON.
        print(json.dumps(result, indent=indent))
        return

    if args.fetch_many:
        if len(args.fetch_many) < 2:
            parser.error("--fetch-many requires an axis followed by at least one id: --fetch-many AXIS ID [ID ...]")
        axis = args.fetch_many[0]
        ids = args.fetch_many[1:]
        results = fetch_many(axis, ids)
        print(json.dumps(results, indent=indent))
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
            #
            # _require_ephemeral_path_is_safe is called BEFORE the read/
            # delete, not just before the delete: an earlier version of this
            # deleted whatever path it was given, no questions asked -
            # confirmed live by an adversarial review to delete an arbitrary
            # non-JSON file (a copy of CHANGELOG.md) passed to this flag by
            # mistake. A caller path mistake must fail loudly, not silently
            # destroy the wrong file. The RESOLVED path it returns is what
            # gets read and deleted below, not args.ephemeral_input_file
            # itself - operating on whatever was actually checked, not a
            # possibly-different symlink pointing at it, closes a second gap
            # an adversarial review found (a repo-internal symlink to a safe
            # temp target could pass the check while the original path -
            # the symlink object - was what got deleted).
            safe_path = _require_ephemeral_path_is_safe(args.ephemeral_input_file)
            try:
                raw = safe_path.read_text(encoding="utf-8")
            finally:
                safe_path.unlink(missing_ok=True)
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
        response_format = payload.get("response_format", args.response_format)
        # The CLI path validates these (see the --short-list-size check
        # below); an adversarial review found the JSON-payload path did not,
        # so a malformed payload (a string where an int/float belongs)
        # crashed with an unhandled TypeError deep inside scoring rather than
        # a clear error here. Coerce and bound-check right after loading,
        # matching the CLI's own rule.
        try:
            short_list_size = int(short_list_size)
        except (TypeError, ValueError):
            parser.error(f"payload short_list_size must be an integer, got: {short_list_size!r}")
        if short_list_size < 0:
            parser.error("payload short_list_size must be a non-negative integer")
        try:
            threshold = float(threshold)
        except (TypeError, ValueError):
            parser.error(f"payload threshold must be a number, got: {threshold!r}")
        if response_format not in ("concise", "detailed"):
            parser.error(f"payload response_format must be 'concise' or 'detailed', got: {response_format!r}")
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
        response_format = args.response_format

    if not situation:
        parser.error("situation is required (the \"situation\" key via --ephemeral-input-file, --input-file, or --stdin, or --situation) unless --list or --fetch is used")

    # Fail loudly: --debug is a silent no-op in detailed mode because full_ranked
    # is always included there regardless. Reject the combination rather than
    # silently ignoring the flag.
    if args.debug and response_format == "detailed":
        parser.error(
            "--debug has no effect with --response-format detailed: "
            "full_ranked is always included in detailed mode. "
            "Omit --debug, or switch to --response-format concise where "
            "--debug adds full_ranked to the otherwise-omitted remainder."
        )

    result = recommend(
        situation=situation,
        topic=topic,
        audience=audience,
        fixed=fixed,
        short_list_size=short_list_size,
        threshold=threshold,
        response_format=response_format,
        debug=args.debug,
    )
    print(json.dumps(result, indent=indent))


if __name__ == "__main__":
    main()
