# Resources

This directory is deliberately empty (a `.gitkeep` placeholder only).

An earlier design had `tools/build-indexes.py` generating a `resources/taxonomy.json` index here for faster lookups. That index was never wired in: the skill reads `taxonomy/` ENTRY.md files directly and requires no build artifact. The directory is kept for potential future bundled resources.
