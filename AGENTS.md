# Repository guidance

Read [docs/publishing-contract.md](docs/publishing-contract.md) before modifying the theme, content mappings, or publishing workflow.

Travelbook is the active theme, authorized on 2026-09-30. Its example site stays opt-in under themes/travelbook/exampleSite/. Keep publisher code and authored content unchanged without separately authorized integration or authoring. Never put private originals in eligible publishing paths. Preserve unrelated working-tree changes.

Run `python3 scripts/check_travelbook.py --hugo hugo` for prototype verification; verify compatibility with the Hugo version pinned in netlify.toml (currently 0.166.0).

Travelbook is a Git submodule. Commit and push theme changes in its repository before recording its new commit in this site. Initialize submodules after a fresh clone.
