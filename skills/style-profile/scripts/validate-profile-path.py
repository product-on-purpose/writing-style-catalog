#!/usr/bin/env python3
"""
Validate a proposed profile write target before any file is created or overwritten.

This script enforces the path-safety invariant that SKILL.md previously
described only in prose (Step 6, items 1 and 5 in style-profile/SKILL.md).
Nothing is written or deleted here; this script only checks.

Guards applied:

1. task_key must match ^[a-z0-9][a-z0-9-]{0,63}$. This eliminates the widest
   attack classes with one rule: path separators (/ \\) that enable directory
   traversal, dots (.) that enable .. traversal or extension injection, null
   bytes, drive letters (C:), UNC prefixes (\\\\server), Unicode homoglyphs,
   uppercase lookalikes, and empty strings.

2. Both the profiles directory and the candidate path are resolved (symlinks
   followed to their real targets) before comparison. The resolved path is what
   is printed to stdout and what the caller must use for the actual write. This
   closes the gap found in entry-recommender: _require_ephemeral_path_is_safe
   originally validated path.resolve() but then let the caller act on the
   original, possibly-different symlink path.

3. The resolved candidate path must be inside the resolved profiles directory
   (is_relative_to check on both resolved paths). This is the containment
   backstop: if Guard 1 is ever weakened in a future edit, Guard 3 is the
   last line of defense against a write outside profiles/.

4. The resolved filename must end with .local.md. Normally guaranteed by the
   fixed suffix in path construction, but checked explicitly as a safety net
   for path-construction bugs.

WHY A SCRIPT INSTEAD OF SKILL.MD PROSE (OWASP LLM01):
entry-recommender shipped with THREE separate path/deletion bugs found during
hardening: two path-traversal bugs and one destructive-deletion bug. All three
were fixed by moving the invariant from prose into Python code. style-profile
was the last place in the plugin where a path-safety invariant was still
enforced only as an LLM instruction. This script closes that gap.

WHY CONTAINMENT + FORMAT INSTEAD OF WHITELIST:
entry-recommender's fetch_one uses a whitelist because the valid entry-id space
is enumerable from the catalog (real directory names already scanned by
list_entries). task_key is user-supplied and unbounded - default, work,
client-foo, and any other valid slug are all legitimate - so a whitelist is not
possible. A strict key format (regex) closes the widest attack classes;
containment is the backstop for future changes that might weaken the regex.
The two together are the honest equivalent of a whitelist for an unbounded key
space.

Exits 0 and prints the RESOLVED profile path to stdout on success.
Exits 1 and prints an error to stderr on failure. Nothing is written.

Usage:
    python validate-profile-path.py --profiles-dir DIR --task-key KEY
"""
import argparse
import re
import sys
from pathlib import Path

# The task_key format is the first and primary guard.
# Mirrors the contract stated in SKILL.md Step 6 and profile-schema.md.
# Allows: ASCII lowercase letters (a-z), digits (0-9), hyphen (-).
# The first character must be a letter or digit (no leading hyphen).
# Length: 1 to 64 characters total (one mandatory char + 0 to 63 more).
# Disallowed (exhaustive, not illustrative):
#   /  -> Unix path separator (directory traversal)
#   \  -> Windows path separator (directory traversal)
#   .  -> dot (enables .. traversal; extension injection; . and .. filenames)
#   :  -> drive letter separator on Windows (C:), invalid on most filesystems
#  \0  -> null byte (filesystem injection)
#  A-Z -> uppercase (case confusion, Unicode homoglyph attacks)
# Unicode -> homoglyph attacks (Cyrillic 'a' U+0430 looks like Latin 'a')
# (empty string) -> fails the mandatory first character class
TASK_KEY_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")


def validate_profile_path(profiles_dir: Path, task_key: str) -> Path:
    """Validate task_key and the candidate profile path.

    Returns the RESOLVED profile path on success.
    Raises ValueError with a message that includes 'No file was written'
    on any failure - the caller and any human reading the error know the
    filesystem is unchanged.

    WHY THIS RETURNS THE RESOLVED PATH:
    An earlier gap found during entry-recommender hardening: the safety
    check used path.resolve() internally but returned (or let the caller
    act on) the original, possibly-symlinked path. A symlink inside the
    expected directory that pointed outside it could pass the resolve()-
    based check while the subsequent file operation followed the symlink
    to an unintended target. Returning the resolved path removes the
    inconsistency: every guard runs on the resolved path, and the caller
    writes to EXACTLY the path this function verified.
    """
    # Guard 1 - task_key format.
    # This is the first check (cheapest, most specific) and covers the
    # widest attack surface. See TASK_KEY_RE comment above for the full
    # exclusion list. An empty string does not match because the first
    # character class [a-z0-9] requires exactly one char.
    if not TASK_KEY_RE.match(task_key):
        raise ValueError(
            f"task_key {task_key!r} does not match the required format "
            f"'^[a-z0-9][a-z0-9-]{{0,63}}$' (lowercase ASCII letters and "
            f"digits, hyphens, 1-64 chars, must start with a letter or "
            f"digit). No file was written."
        )

    # Guard 2 - resolve profiles_dir and build the candidate path.
    # resolve() makes the path absolute and follows symlinks. A relative
    # profiles_dir (the typical case: '.claude/writing-style-catalog/profiles'
    # from the project root) becomes absolute here. A symlinked profiles_dir
    # is followed to its real target, so the containment check in Guard 3
    # compares real filesystem locations, not link objects.
    # After Guard 1, task_key contains no separators or dots, so joining it
    # to profiles_dir cannot escape the directory. resolve() is applied
    # to candidate anyway to catch symlinks in profiles_dir itself and as
    # defense-in-depth against any future weakening of Guard 1.
    resolved_profiles_dir = profiles_dir.resolve()
    candidate = resolved_profiles_dir / f"{task_key}.local.md"
    resolved_candidate = candidate.resolve()

    # Guard 3 - containment.
    # is_relative_to() uses OS path semantics (case-insensitive on Windows),
    # which is correct here. A raw string prefix check fails on Windows case
    # differences and on symlinks - both confirmed real failure modes in prior
    # bugs on this codebase. This guard is the backstop: if Guard 1 is ever
    # weakened, Guard 3 is the last line of defense.
    if not resolved_candidate.is_relative_to(resolved_profiles_dir):
        raise ValueError(
            f"Resolved profile path {str(resolved_candidate)!r} is not "
            f"inside the profiles directory {str(resolved_profiles_dir)!r}. "
            f"Refusing to write outside the profiles directory. "
            f"No file was written."
        )

    # Guard 4 - suffix.
    # The fixed '.local.md' suffix in the path construction above makes
    # this always true as long as resolve() does not change the filename.
    # It is here as a safety net: if path-construction logic ever changes
    # and produces a non-.local.md path, this catches it before a write.
    if not resolved_candidate.name.endswith(".local.md"):
        raise ValueError(
            f"Resolved profile filename {resolved_candidate.name!r} does "
            f"not end with '.local.md'. This is a path-construction error. "
            f"No file was written."
        )

    return resolved_candidate


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Validate a proposed style-profile write target. "
            "Prints the resolved path to stdout on success (exit 0). "
            "Prints an error to stderr and exits 1 on failure. "
            "Nothing is written or deleted by this script."
        )
    )
    parser.add_argument(
        "--profiles-dir",
        required=True,
        type=Path,
        help=(
            "The profiles directory "
            "(e.g. .claude/writing-style-catalog/profiles). "
            "May be relative or absolute."
        ),
    )
    parser.add_argument(
        "--task-key",
        required=True,
        help=(
            "The proposed task_key "
            "(e.g. 'default', 'work', 'client-foo'). "
            "Must match ^[a-z0-9][a-z0-9-]{0,63}$."
        ),
    )
    args = parser.parse_args()

    try:
        resolved = validate_profile_path(args.profiles_dir, args.task_key)
        print(str(resolved))
        sys.exit(0)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
