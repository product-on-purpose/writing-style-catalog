#!/usr/bin/env python3
"""
Validation script for the writing-style-library taxonomy.

Runs all CI checks locally and exits with code 0 if no errors,
code 1 if any errors are found (warnings do not affect exit code).

Requirements:
    pip install jsonschema

Usage:
    python tools/validate.py
"""

import json
import re
import sys
from pathlib import Path

try:
    import jsonschema
    from jsonschema import validate as jschema_validate, ValidationError
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012
except ImportError:
    print("[ERROR] jsonschema and referencing are required. Run: pip install jsonschema referencing")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parents[1]
TAXONOMY_ROOT = REPO_ROOT / "taxonomy"
SCHEMAS_DIR = REPO_ROOT / "schemas"
EXAMPLES_DIR = REPO_ROOT / "examples"
DOCS_DIR = REPO_ROOT / "docs"

AXES = {
    "voice": TAXONOMY_ROOT / "voices",
    "tone": TAXONOMY_ROOT / "tones",
    "style": TAXONOMY_ROOT / "styles",
    "format": TAXONOMY_ROOT / "formats",
}

AXIS_SCHEMAS = {
    "voice": SCHEMAS_DIR / "voice.schema.json",
    "tone": SCHEMAS_DIR / "tone.schema.json",
    "style": SCHEMAS_DIR / "style.schema.json",
    "format": SCHEMAS_DIR / "format.schema.json",
}

SLUG_PATTERN = re.compile(r"^[a-z][a-z0-9-]*[a-z0-9]$")

EM_DASH = "—"
EN_DASH = "–"


# ---------------------------------------------------------------------------
# YAML frontmatter parser (adapted from skills/writing-instruction-builder/
# scripts/build-instruction.py)
# ---------------------------------------------------------------------------

def _parse_simple_yaml(text: str) -> dict:
    """Parse simple YAML frontmatter sufficient for taxonomy entry files.

    Handles: scalar key-value, multi-line lists (  - item), and YAML
    block scalars (> folded and | literal) for multi-line string fields.
    """
    result = {}
    current_key = None
    current_list = None
    block_key = None
    block_lines = []
    block_style = None  # ">" or "|"

    def flush_block():
        nonlocal block_key, block_lines, block_style
        if block_key is None:
            return
        if block_style == "|":
            result[block_key] = "\n".join(block_lines).strip()
        else:  # ">" folded: join with space, collapse newlines
            result[block_key] = " ".join(line for line in block_lines if line).strip()
        block_key = None
        block_lines = []
        block_style = None

    def flush_list():
        nonlocal current_key, current_list
        if current_list is not None and current_key is not None:
            result[current_key] = current_list
        current_key = None
        current_list = None

    for line in text.split("\n"):
        # Inside a block scalar: collect indented lines
        if block_key is not None:
            if line.startswith("  ") or (line.strip() == "" and block_lines):
                block_lines.append(line.strip())
                continue
            else:
                # Block ended
                flush_block()
                # Fall through to process this line normally

        # Inside a list: collect list items
        if current_list is not None and line.startswith("  - "):
            current_list.append(line[4:].strip())
            continue

        # Blank line: flush pending state
        if not line.strip():
            if current_list is not None:
                flush_list()
            continue

        # Top-level key
        if ":" in line and not line.startswith(" "):
            flush_list()
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()

            if value in (">", "|"):
                block_key = key
                block_style = value
                block_lines = []
            elif value == "":
                current_key = key
                current_list = []
            elif value.startswith("["):
                items = value.strip("[]").split(",")
                result[key] = [i.strip().strip('"').strip("'") for i in items if i.strip()]
            else:
                str_val = value.strip('"').strip("'")
                # Coerce to numeric types if applicable
                if str_val.lstrip('-').isdigit():
                    result[key] = int(str_val)
                elif str_val.replace('.', '', 1).lstrip('-').isdigit() and str_val.count('.') == 1:
                    result[key] = float(str_val)
                else:
                    result[key] = str_val

    # Flush any pending state at end
    flush_block()
    flush_list()

    return result


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _extract_frontmatter(entry_md_path: Path) -> dict | None:
    """Read ENTRY.md and return parsed frontmatter dict, or None on failure."""
    content = entry_md_path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return None
    # Split on "---" only when it appears alone on a line (YAML delimiter).
    # Plain str.split("---") would match "---" inside table separators like
    # "|------|" inside canonical_template block scalars.
    parts = re.split(r"(?m)^---[ \t]*$", content, maxsplit=2)
    if len(parts) < 3:
        return None
    frontmatter_text = parts[1].strip()
    return _parse_simple_yaml(frontmatter_text)


def _load_schema(schema_path: Path) -> dict:
    """Load a JSON schema file."""
    return json.loads(schema_path.read_text(encoding="utf-8"))


def _build_schema_registry() -> Registry:
    """Build a referencing.Registry containing every local schema file.

    Each schema's $id is the canonical https://... URI used in $ref references.
    The registry maps that URI to the schema content, so Draft202012Validator
    can resolve cross-schema refs without network calls.
    """
    registry = Registry()
    for f in SCHEMAS_DIR.glob("*.schema.json"):
        schema_dict = json.loads(f.read_text(encoding="utf-8"))
        uri = f"https://raw.githubusercontent.com/product-on-purpose/writing-style-library/main/schemas/{f.name}"
        resource = Resource(contents=schema_dict, specification=DRAFT202012)
        registry = registry.with_resource(uri=uri, resource=resource)
    return registry


def _iter_entries():
    """Yield (axis, entry_dir) tuples for every entry directory."""
    for axis, axis_path in AXES.items():
        if not axis_path.exists():
            continue
        for entry_dir in sorted(axis_path.iterdir()):
            if entry_dir.is_dir():
                yield axis, entry_dir


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_slug_format() -> list[str]:
    """Every entry directory name must match ^[a-z][a-z0-9-]*[a-z0-9]$."""
    print("[CHECK] Slug format...")
    errors = []
    for axis, entry_dir in _iter_entries():
        slug = entry_dir.name
        if not SLUG_PATTERN.match(slug):
            errors.append(
                f"[ERROR] taxonomy/{axis}s/{slug}: slug does not match "
                f"^[a-z][a-z0-9-]*[a-z0-9]$ (got '{slug}')"
            )
    count = len(errors)
    if count == 0:
        print(f"[PASS] Slug format: 0 errors")
    for e in errors:
        print(e)
    return errors


def check_entry_md_exists() -> list[str]:
    """Every directory under each axis must contain ENTRY.md."""
    print("[CHECK] ENTRY.md presence...")
    errors = []
    for axis, entry_dir in _iter_entries():
        entry_md = entry_dir / "ENTRY.md"
        if not entry_md.exists():
            rel = entry_md.relative_to(REPO_ROOT)
            errors.append(f"[ERROR] {rel}: ENTRY.md missing")
    count = len(errors)
    if count == 0:
        print(f"[PASS] ENTRY.md presence: 0 errors")
    for e in errors:
        print(e)
    return errors


def check_frontmatter_parseable() -> tuple[list[str], dict[str, tuple[str, dict]]]:
    """
    Parse all ENTRY.md frontmatter. Returns (errors, id_map).
    id_map maps entry ID -> (axis, frontmatter_dict).
    """
    print("[CHECK] Frontmatter parsing...")
    errors = []
    id_map: dict[str, tuple[str, dict]] = {}

    for axis, entry_dir in _iter_entries():
        entry_md = entry_dir / "ENTRY.md"
        if not entry_md.exists():
            continue  # already reported by check_entry_md_exists
        rel = entry_md.relative_to(REPO_ROOT)
        try:
            fm = _extract_frontmatter(entry_md)
        except Exception as exc:
            errors.append(f"[ERROR] {rel}: frontmatter parse error: {exc}")
            continue
        if fm is None:
            errors.append(f"[ERROR] {rel}: could not parse frontmatter (missing --- delimiters?)")
            continue
        entry_id = fm.get("id", entry_dir.name)
        id_map[entry_id] = (axis, fm)

    count = len(errors)
    if count == 0:
        print(f"[PASS] Frontmatter parsing: 0 errors")
    for e in errors:
        print(e)
    return errors, id_map


def check_schema_validation(id_map: dict[str, tuple[str, dict]]) -> list[str]:
    """Validate each entry's frontmatter against its axis-specific JSON schema."""
    print("[CHECK] JSON Schema validation...")
    errors = []

    registry = _build_schema_registry()

    for entry_id, (axis, fm) in id_map.items():
        schema_path = AXIS_SCHEMAS.get(axis)
        if schema_path is None or not schema_path.exists():
            errors.append(f"[ERROR] schemas/{axis}.schema.json: schema file not found")
            continue

        schema = _load_schema(schema_path)
        validator = Draft202012Validator(schema=schema, registry=registry)

        rel = f"taxonomy/{axis}s/{entry_id}/ENTRY.md"
        try:
            validator.validate(fm)
        except ValidationError as exc:
            errors.append(f"[ERROR] {rel}: schema validation failed: {exc.message}")

    count = len(errors)
    if count == 0:
        print(f"[PASS] JSON Schema validation: 0 errors")
    for e in errors:
        print(e)
    return errors


def check_cross_references(id_map: dict[str, tuple[str, dict]]) -> list[str]:
    """Every ID in pairs_well_with, avoid_with, confusable_with must resolve to an existing entry."""
    print("[CHECK] Cross-reference validation...")
    errors = []
    cross_ref_fields = ["pairs_well_with", "avoid_with", "confusable_with"]
    known_ids = set(id_map.keys())

    for entry_id, (axis, fm) in id_map.items():
        rel = f"taxonomy/{axis}s/{entry_id}/ENTRY.md"
        for field in cross_ref_fields:
            refs = fm.get(field, [])
            if not isinstance(refs, list):
                continue
            for ref_id in refs:
                if ref_id and ref_id not in known_ids:
                    errors.append(
                        f"[ERROR] {rel}: {field} references unknown entry ID '{ref_id}'"
                    )

    count = len(errors)
    if count == 0:
        print(f"[PASS] Cross-reference validation: 0 errors")
    for e in errors:
        print(e)
    return errors


def check_no_em_dashes() -> list[str]:
    """Scan .md and .html files in taxonomy/, examples/, and docs/ for em/en-dashes."""
    print("[CHECK] No em-dash / en-dash linting...")
    errors = []
    # (search_root, file_glob_patterns)
    search_targets = [
        (TAXONOMY_ROOT, ("*.md",)),
        (EXAMPLES_DIR, ("*.md",)),
        (DOCS_DIR, ("*.md", "*.html")),
    ]

    for root, patterns in search_targets:
        if not root.exists():
            continue
        files = []
        for pattern in patterns:
            files.extend(root.rglob(pattern))
        for src_file in sorted(set(files)):
            rel = src_file.relative_to(REPO_ROOT)
            try:
                lines = src_file.read_text(encoding="utf-8").splitlines()
            except Exception as exc:
                errors.append(f"[ERROR] {rel}: could not read file: {exc}")
                continue
            for lineno, line in enumerate(lines, start=1):
                if EM_DASH in line:
                    errors.append(
                        f"[ERROR] {rel}:{lineno}: em-dash (U+2014) found"
                    )
                if EN_DASH in line:
                    errors.append(
                        f"[ERROR] {rel}:{lineno}: en-dash (U+2013) found"
                    )

    count = len(errors)
    if count == 0:
        print(f"[PASS] No em-dash / en-dash: 0 errors")
    for e in errors:
        print(e)
    return errors


def check_examples(id_map: dict[str, tuple[str, dict]]) -> list[str]:
    """Validate example files: frontmatter parses, matches example schema,
    and entry_id resolves to a known entry in the catalog."""
    print("[CHECK] Example file validation...")
    errors = []

    example_schema_path = SCHEMAS_DIR / "example.schema.json"
    if not example_schema_path.exists():
        errors.append("[ERROR] schemas/example.schema.json: schema file not found")
        return errors

    example_schema = _load_schema(example_schema_path)
    known_ids = set(id_map.keys())

    if not EXAMPLES_DIR.exists():
        print("[PASS] Example file validation: 0 errors (no examples directory)")
        return errors

    example_count = 0
    for md_file in sorted(EXAMPLES_DIR.rglob("*.md")):
        # Recipe definition files live alongside horizontal-slice examples but
        # are documentation, not examples. Skip them here.
        if md_file.name == "README.md":
            continue
        # Diff-pair files have their own frontmatter shape (entry_a / entry_b,
        # not entry_id) and are validated separately if at all.
        if "diff-pairs" in md_file.parts:
            continue
        rel = md_file.relative_to(REPO_ROOT)
        try:
            fm = _extract_frontmatter(md_file)
        except Exception as exc:
            errors.append(f"[ERROR] {rel}: frontmatter parse error: {exc}")
            continue
        if fm is None:
            errors.append(f"[ERROR] {rel}: missing or unparseable frontmatter")
            continue

        example_count += 1

        try:
            jsonschema.validate(instance=fm, schema=example_schema)
        except ValidationError as exc:
            errors.append(f"[ERROR] {rel}: example schema validation failed: {exc.message}")
            continue

        entry_id = fm.get("entry_id")
        if entry_id and entry_id not in known_ids:
            errors.append(
                f"[ERROR] {rel}: entry_id '{entry_id}' does not match any entry in the catalog"
            )

        fm_axis = fm.get("axis")
        if entry_id in known_ids:
            actual_axis, _ = id_map[entry_id]
            if fm_axis and fm_axis != actual_axis:
                errors.append(
                    f"[ERROR] {rel}: axis '{fm_axis}' does not match entry's actual axis '{actual_axis}'"
                )

    count = len(errors)
    if count == 0:
        print(f"[PASS] Example file validation: 0 errors ({example_count} examples checked)")
    for e in errors:
        print(e)
    return errors


def check_diff_pairs(id_map: dict[str, tuple[str, dict]]) -> list[str]:
    """Validate diff-pair files: frontmatter parses, matches diff-pair schema,
    entry_a and entry_b resolve to known entries, both are on the declared axis,
    and the two entries differ."""
    print("[CHECK] Diff-pair file validation...")
    errors = []

    diff_pair_schema_path = SCHEMAS_DIR / "diff-pair.schema.json"
    if not diff_pair_schema_path.exists():
        errors.append("[ERROR] schemas/diff-pair.schema.json: schema file not found")
        return errors

    diff_pair_schema = _load_schema(diff_pair_schema_path)
    known_ids = set(id_map.keys())

    diff_pairs_dir = EXAMPLES_DIR / "diff-pairs"
    if not diff_pairs_dir.exists():
        print("[PASS] Diff-pair file validation: 0 errors (no diff-pairs directory)")
        return errors

    diff_pair_count = 0
    for md_file in sorted(diff_pairs_dir.rglob("*.md")):
        if md_file.name == "README.md":
            continue
        rel = md_file.relative_to(REPO_ROOT)
        try:
            fm = _extract_frontmatter(md_file)
        except Exception as exc:
            errors.append(f"[ERROR] {rel}: frontmatter parse error: {exc}")
            continue
        if fm is None:
            errors.append(f"[ERROR] {rel}: missing or unparseable frontmatter")
            continue

        diff_pair_count += 1

        try:
            jsonschema.validate(instance=fm, schema=diff_pair_schema)
        except ValidationError as exc:
            errors.append(f"[ERROR] {rel}: diff-pair schema validation failed: {exc.message}")
            continue

        entry_a = fm.get("entry_a")
        entry_b = fm.get("entry_b")
        axis_varied = fm.get("axis_varied")

        if entry_a and entry_a not in known_ids:
            errors.append(
                f"[ERROR] {rel}: entry_a '{entry_a}' does not match any entry in the catalog"
            )
        if entry_b and entry_b not in known_ids:
            errors.append(
                f"[ERROR] {rel}: entry_b '{entry_b}' does not match any entry in the catalog"
            )

        if entry_a and entry_b and entry_a == entry_b:
            errors.append(
                f"[ERROR] {rel}: entry_a and entry_b are identical ('{entry_a}'); a diff-pair must contrast two distinct entries"
            )

        if entry_a in known_ids and axis_varied:
            actual_axis_a, _ = id_map[entry_a]
            if actual_axis_a != axis_varied:
                errors.append(
                    f"[ERROR] {rel}: entry_a '{entry_a}' is on axis '{actual_axis_a}' but axis_varied is '{axis_varied}'"
                )
        if entry_b in known_ids and axis_varied:
            actual_axis_b, _ = id_map[entry_b]
            if actual_axis_b != axis_varied:
                errors.append(
                    f"[ERROR] {rel}: entry_b '{entry_b}' is on axis '{actual_axis_b}' but axis_varied is '{axis_varied}'"
                )

    count = len(errors)
    if count == 0:
        print(f"[PASS] Diff-pair file validation: 0 errors ({diff_pair_count} diff-pairs checked)")
    for e in errors:
        print(e)
    return errors


def check_review_status(id_map: dict[str, tuple[str, dict]]) -> list[str]:
    """Entries with review_status 'draft' produce a warning (not an error)."""
    print("[CHECK] Review status warnings...")
    warnings = []
    for entry_id, (axis, fm) in id_map.items():
        status = fm.get("review_status", "")
        if status == "draft":
            rel = f"taxonomy/{axis}s/{entry_id}/ENTRY.md"
            warnings.append(f"[WARN] {rel}: review_status is 'draft'")

    if not warnings:
        print("[PASS] Review status: 0 draft entries")
    for w in warnings:
        print(w)
    return []  # warnings do not contribute to error count


# ---------------------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------------------

def run_all_checks() -> list[str]:
    """Run all checks and return the combined error list."""
    all_errors = []

    all_errors += check_slug_format()
    all_errors += check_entry_md_exists()

    parse_errors, id_map = check_frontmatter_parseable()
    all_errors += parse_errors

    if id_map:
        all_errors += check_schema_validation(id_map)
        all_errors += check_cross_references(id_map)
    else:
        print("[INFO] No entries found - skipping schema and cross-reference checks")

    all_errors += check_no_em_dashes()

    if id_map:
        all_errors += check_examples(id_map)
        all_errors += check_diff_pairs(id_map)
    else:
        print("[INFO] No entries found - skipping example and diff-pair validation")

    check_review_status(id_map)

    print()
    if all_errors:
        print(f"Validation complete: {len(all_errors)} error(s) found.")
    else:
        print("Validation complete: all checks passed.")

    return all_errors


if __name__ == "__main__":
    errors = run_all_checks()
    sys.exit(1 if errors else 0)
