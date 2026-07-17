#!/usr/bin/env python3
"""
Recommender eval corpus runner - tests/eval/run_eval.py

PURPOSE
-------
Run the ten probe situations from tests/eval/situations.jsonl through the
entry-recommender scorer and compare today's qualifying sets against the
recorded baseline.  Reports pass/fail on the token round-trip assertion and
reports drift (changes since the baseline date) as findings.

This runner is a judgment aid, not a gate.  It is kept outside CI because
its output requires human interpretation: a change in qualifying IDs may
be a fix, a regression, or a neutral catalog update.  What it CAN assert
deterministically is that each situation reconstructs to the same token set
as the original probe (the round-trip check), because the scorer consumes
only tokens.

HOW TO RUN
----------
From the repository root:

    python tests/eval/run_eval.py

Optional flags:
    --json          Emit JSON output (useful for scripted diffing)
    --verbose       Print qualifying IDs for every case, not just drifted ones

WHEN TO RUN
-----------
Run this before and after any change to:
  - skills/entry-recommender/scripts/recommend.py  (scorer logic, thresholds,
    stopwords, IDF computation, field weights)
  - Any stable-entry ENTRY.md file (content changes alter IDF table and
    per-entry scoring)

Diff the qualifying sets before/after.  If a case drifts, decide whether the
drift is expected (a fix) or unexpected (a regression).  Update the baseline
date and sets in situations.jsonl when you intentionally change scorer behavior.

NOT IN CI
---------
This runner is deliberately excluded from the CI test suite (pytest, GitHub
Actions).  The qualifying-set comparison is informational, not a pass/fail
gate.  Only the round-trip assertion is truly deterministic; the qualifying
sets are expected to drift when the catalog or scorer evolves.

SITUATION TEXTS ARE RECONSTRUCTIONS
------------------------------------
The original probe inputs from 2026-07-11 were not persisted.  The situation
texts in situations.jsonl are token-faithful RECONSTRUCTIONS: each was written
so that tokenize(situation) produces exactly the set of tokens recorded in the
probe's raw/probe-results.json.  The round-trip check verifies this property
at runtime.  Only the low-signal case ("Write something nice for my coworker.")
survived verbatim from the probe, quoted in
_local/audit/2026-07-10_fable-audit/payload-redesign-proposal.md line 31.

SCHEMA
------
Each line of situations.jsonl is a JSON object with these fields:
  id             - stable name matching the probe case name
  situation      - reconstructed text
  fixed          - dict or null (e.g. {"voice": "pragmatic-architect"})
  tokens         - sorted list of expected tokenizer output (self-checking)
  baseline       - per-axis qualifying IDs as of baseline_date
  baseline_date  - ISO date when the baseline was recorded
  phenomena      - list of probe phenomena codes this case exercises
  notes          - what this case exists to catch and why it matters
  reconstruction - how the text was obtained
"""
import argparse
import importlib.util
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CORPUS_PATH = Path(__file__).parent / "situations.jsonl"
RECOMMEND_PATH = REPO_ROOT / "skills" / "entry-recommender" / "scripts" / "recommend.py"


def _load_recommend():
    spec = importlib.util.spec_from_file_location("recommend", RECOMMEND_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _load_corpus():
    cases = []
    with open(CORPUS_PATH, encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                cases.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"ERROR: situations.jsonl line {lineno} is invalid JSON: {e}", file=sys.stderr)
                sys.exit(1)
    return cases


def _qualifying_ids(axes_result, axis):
    """Extract sorted qualifying IDs from a recommend() axes result."""
    ax = axes_result.get(axis, {})
    if ax.get("fixed"):
        return {"fixed": ax["fixed"]}
    return sorted(
        row["id"] for row in ax.get("short_list", []) if row.get("above_threshold")
    )


def run(verbose=False, json_output=False):
    rec = _load_recommend()
    cases = _load_corpus()

    total = len(cases)
    roundtrip_pass = 0
    roundtrip_fail = 0
    drift_cases = []
    results = []

    for case in cases:
        cid = case["id"]
        situation = case["situation"]
        fixed = case.get("fixed") or {}
        expected_tokens = set(case["tokens"])

        # --- Round-trip assertion (deterministic) ---
        actual_tokens = rec.tokenize(situation)
        rt_ok = actual_tokens == expected_tokens
        if rt_ok:
            roundtrip_pass += 1
        else:
            roundtrip_fail += 1
            missing = sorted(expected_tokens - actual_tokens)
            extra = sorted(actual_tokens - expected_tokens)

        # --- Run scorer ---
        result = rec.recommend(situation, fixed=fixed, response_format="concise")
        axes = result.get("axes", {})

        # --- Compare to baseline ---
        baseline = case.get("baseline", {})
        axis_drift = {}
        for axis in ["voice", "tone", "style", "format"]:
            bl = baseline.get(axis, [])
            if isinstance(bl, dict) and "fixed" in bl:
                # Fixed axis - skip qualifying comparison
                continue
            bl_set = set(bl)
            today_ids = _qualifying_ids(axes, axis)
            if isinstance(today_ids, dict):
                # Fixed axis in scorer output - skip
                continue
            today_set = set(today_ids)
            added = sorted(today_set - bl_set)
            removed = sorted(bl_set - today_set)
            if added or removed:
                axis_drift[axis] = {"added": added, "removed": removed}

        today_qualifying = {
            axis: _qualifying_ids(axes, axis)
            for axis in ["voice", "tone", "style", "format"]
        }

        case_result = {
            "id": cid,
            "roundtrip": "PASS" if rt_ok else "FAIL",
            "phenomena": case.get("phenomena", []),
            "drift": axis_drift,
            "today_qualifying": today_qualifying,
        }
        if not rt_ok:
            case_result["roundtrip_missing"] = missing
            case_result["roundtrip_extra"] = extra

        if axis_drift:
            drift_cases.append(cid)

        results.append(case_result)

    # --- Output ---
    if json_output:
        print(json.dumps({
            "total": total,
            "roundtrip_pass": roundtrip_pass,
            "roundtrip_fail": roundtrip_fail,
            "drift_cases": drift_cases,
            "results": results,
        }, indent=2))
        return roundtrip_fail == 0

    # Plain text report
    print("=" * 70)
    print("ENTRY-RECOMMENDER EVAL CORPUS")
    print("=" * 70)
    print(f"Corpus: {CORPUS_PATH}")
    print(f"Cases:  {total}")
    print()

    print("ROUND-TRIP VERIFICATION (deterministic)")
    print("-" * 40)
    for r in results:
        status = r["roundtrip"]
        line = f"  {status}  {r['id']}"
        print(line)
        if status == "FAIL":
            if r.get("roundtrip_missing"):
                print(f"         missing tokens: {r['roundtrip_missing']}")
            if r.get("roundtrip_extra"):
                print(f"         extra tokens:   {r['roundtrip_extra']}")
    print()

    print("DRIFT vs BASELINE (informational, requires human judgment)")
    print("-" * 40)
    if not drift_cases:
        print("  No drift - all qualifying sets match the recorded baseline.")
    else:
        for r in results:
            if not r["drift"]:
                continue
            print(f"\n  {r['id']} (phenomena: {', '.join(r['phenomena'])})")
            for axis, d in r["drift"].items():
                if d["added"]:
                    print(f"    {axis} ADDED:   {d['added']}")
                if d["removed"]:
                    print(f"    {axis} REMOVED: {d['removed']}")
    print()

    if verbose:
        print("TODAY'S QUALIFYING SETS")
        print("-" * 40)
        for r in results:
            print(f"\n  {r['id']}")
            tq = r["today_qualifying"]
            for axis in ["voice", "tone", "style", "format"]:
                val = tq.get(axis)
                if isinstance(val, dict) and "fixed" in val:
                    print(f"    {axis}: FIXED={val['fixed']}")
                else:
                    print(f"    {axis}: {len(val) if val else 0} qualifying = {val}")
        print()

    print("SUMMARY")
    print("-" * 40)
    rt_status = "ALL PASS" if roundtrip_fail == 0 else f"{roundtrip_fail} FAILED"
    print(f"  Round-trip:  {rt_status} ({roundtrip_pass}/{total})")
    drift_status = f"{len(drift_cases)} cases drifted" if drift_cases else "no drift"
    print(f"  Drift:       {drift_status}")
    if drift_cases:
        print(f"  Drifted:     {drift_cases}")
    print()
    if roundtrip_fail > 0:
        print("ACTION: Round-trip failures mean a situation no longer tokenizes to")
        print("  its recorded token set. This indicates either a tokenizer change")
        print("  (update the situation text) or a corpus error (fix situations.jsonl).")
    if drift_cases:
        print("ACTION: Review each drifted case. If the change is a fix, update")
        print("  baseline in situations.jsonl and set baseline_date to today.")
        print("  If the change is unexpected, investigate before releasing.")

    return roundtrip_fail == 0


def main():
    parser = argparse.ArgumentParser(
        description="Run the recommender eval corpus against the current scorer."
    )
    parser.add_argument(
        "--json", action="store_true", dest="json_output",
        help="Emit JSON output for scripted diffing."
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Print all qualifying IDs, not just drifted cases."
    )
    args = parser.parse_args()

    ok = run(verbose=args.verbose, json_output=args.json_output)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
