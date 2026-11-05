# Site cleanup audit — 2026-11-05

Scope: tracked site files, active Hugo/Netlify configuration, content ownership, obsolete theme dependencies, authoring/deployment documentation, and site/theme verification. No deployed publisher configuration or private vault was changed. This is a repository audit, not confirmation of live service configuration.

## Cleanup prepared

| Area | Change and reason |
| --- | --- |
| Retired theme | Removed the clean PaperMod submodule and `legacy/papermod/` templates, styles, archetypes, and configuration. Travelbook is the sole maintained theme; old versions remain in Git history. |
| Gallery | Removed the old gallery section and sample album. The gallery-validation post was already gone. Removed the two Hugo cascades that existed only to suppress those retired sources. |
| Unused assets | Removed the old homepage hero, placeholder, location data/banner instructions, and unmanaged sample Cairn thumbnails/download. These were not referenced by the active theme or current published notes. |
| Hugo configuration | Removed the nonexistent `/home-preview` fallback and unused site-description parameter. Retained active author, homepage, timezone, Git metadata, taxonomy, permalink, output, and Markdown settings. |
| Page metadata | Removed unused PaperMod flags from Contact and Thank-you; preserved their prose, form, styles, and success route. |
| Netlify | Removed duplicate Git-information configuration (already enabled in Hugo) and the long-lived `/images/*` cache rule for the retired static-image directory. Preserved deployment contexts, security headers, and reader redirects. |
| Documentation | Replaced obsolete direct-Git/mobile publishing guidance with the current Obsidian workflow. Updated mappings, Folder Notes, media handling, ownership/deletion behavior, date ordering, and recovery guidance. |
| Design references | Preserved the original design mockups and checklist as requested; labeled the old checklist historical. Corrected stale theme documentation about Journey limits and homepage rendering. |
| Verification | Removed requirements for retired samples, demonstration homepage photos, a PaperMod rollback installation, and fixed Welcome title/body text. Checks now inspect current Hugo content and RSS routes, draft exclusion, preview indexing protection, contact-form integration, and theme isolation. |

## Preserved and author-managed follow-up

- **About and Welcome:** preserved for the author to rewrite, as requested. Both still contain the old claim that the travelers do not own motorcycles. The Welcome post remains published and in RSS until deliberately changed.
- **Old publisher copy:** removed `scripts/publisher/publisher.py` and its Dockerfile with explicit author approval. The publisher is maintained in the separate `publisher-daemon` repository; no deployed service was changed.
- **Publisher-owned samples:** the author will clean these up in Obsidian. The current manifest still contains `cairns/sample-overnight-notes`, `cairns/sample-packing-review`, `cairns/sample-route-notes`, and `pages/sample-about.md` outputs. Remove the notes in Obsidian and run `build-preview`; deleting generated files here alone is not durable. Sample Journey references in those Cairns can also recreate taxonomy pages.
- **Homepage:** the delivered source contains real photos but still has `title: Homepage design preview`, `fixture: true`, and `draft: true`. Update these in Obsidian. Remove `fixture` for real writing; choose draft visibility deliberately. The cleanup does not change the author's publication status.
- **Working-tree edits:** three sample photo/video file deletions existed before this audit. They are included in the cleanup commit under the author’s subsequent instruction to push all changes.
- **Contact:** preserved Netlify form and `unsafe = true` Markdown rendering because that form uses raw HTML. Its existing CSS aliases remain supported by Travelbook.
- **Reader routes:** retained `/posts/` → `/dispatches/` and `/rss` → `/index.xml` redirects.
- **Theme demo:** retained under `themes/travelbook/exampleSite/`, isolated from the site's content and useful for rendering tests.

## Validation

- `python3 scripts/check_travelbook.py --hugo hugo` passes on Hugo 0.166.0, including isolated theme tests and the actual site's production and preview builds.
- Appearance preference tests pass using the installed Node 22 runtime. The default Node executable on this machine has a missing shared-library dependency; no machine-wide runtime repair was attempted.
- Site and theme `git diff --check` pass.
- Publication and a live contact-form submission are not used as tests. Delivery targets are Travelbook `main` for theme documentation, followed by site `preview` for the cleanup; production promotion is separate.
