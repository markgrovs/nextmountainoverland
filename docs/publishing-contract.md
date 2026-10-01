# Publishing contract

## Current workflow

Preserve Obsidian → Workbench publisher → GitHub → Netlify. Authors own vault text and originals; the publisher owns generated paths in `.publisher-manifest.json`; maintainers own theme/configuration. Private originals must stay outside eligible publishing paths. Drafts are exposed in preview and Git history.

Current mappings: `posts/<bundle>/` → `content/posts/<bundle>/index.md`; `drafts/*.md` → `content/drafts/*.md`; `pages/*.md` → `content/*.md`. Only posts currently receive bundle processing. Current image processing and Markdown relocation have limitations; proposed media support is not implemented in the daemon.

## Local prototype

See [theme demo instructions](../themes/travelbook/exampleSite/README.md). `themes/travelbook/exampleSite/hugo.toml` selects travelbook and isolated fixture content, layouts, assets, data, and static paths. The example site is opt-in locally; Travelbook is now the active production theme configuration, authorized by the user on 2026-09-30. Authored content remains independent. Do not merge prototype configuration into production or mount fixtures in a deployment.

Journal routes use `/dispatches/:contentbasename/`, preserving bundle identity across title changes. Journeys read oldest first. Root RSS selects Journal and Cairns only and excludes drafts and fixture-marked entries.

Preferred authoring syntax:

```markdown
![Author-written alternative text](images/photo.jpg "Optional visible caption")
```

The render hook accepts current local page resources or proposed media-index entries. It emits dimensions and responsive selections without recompression and fails the build on missing images. Synthetic responsive JPEG fixtures and a PNG diagram demonstrate the proposed interface. Publisher generation, orientation correction, metadata stripping, source validation, and download ownership remain Phase B work.

## Revised high-desert theme interface

The homepage now shows the latest entry in full, with older dispatches beneath it. Optional `location` (falling back to `place`) and `mileage` supplement the date. The presentation uses a single column, inline media, italic captions, system serif headings, and sans-serif prose. A prominent mixed-case serif masthead anchors the page. Reader-controlled Light/Dark buttons default to the device preference and remember an explicit choice in browser local storage; with JavaScript disabled the site follows device appearance.

`themes/travelbook/` is the pinned submodule from https://github.com/markgrovs/travelbook. Theme changes are committed and pushed in that repository first, then its updated commit is recorded in this site. See its README and `exampleSite/minimal.hugo.toml` for installation and explicit site settings.

The `ambient-video` shortcode renders explicitly delivered local MP4s as muted, looping, inline video, with a poster, native controls, and direct file link. A small local script adds a pause/play button and reduced-motion handling. This changes the theme's rendering interface only; it does not implement daemon video processing or authorize storing master video files in Git. The checked-in clip is synthetic test media.

Run `python3 scripts/check_travelbook.py --hugo hugo`. Check artifacts and preview output stay in Git-ignored directories under `themes/travelbook/exampleSite/`.

## IndieWeb interface

The theme renders h-entry/h-feed, author h-card, canonical entry URL/identity, publication and update dates, content, and supplied summary/location/categories. Optional `syndication`, `in_reply_to`, `like_of`, and `repost_of` fields are rendered as their corresponding microformat properties. See the theme README for configuration.

Only configured IndieAuth, Webmention, and Micropub endpoint URLs are advertised. No service backend, external delivery, or social verification is created by theme markup. The publisher's scalar parser remains unchanged, so complete frontmatter/list handling in vault publication is still a Phase B task.

## Approval and recovery

Phase B requires sanitized deployed service definitions, deployed revision identity, and Netlify branch/deploy settings. Theme activation was separately authorized on 2026-09-30. Publisher integration and POSSE still require separate authorization. No live publication is a test.

The gallery section and gallery-validation post are excluded from active production and preview builds through Hugo cascades; their source files remain intact. Legacy templates/styles/configuration/archetypes are retained in legacy/papermod/. The prior theme configuration is recorded in legacy/papermod/hugo.toml; record compatible publisher manifest/state before any later publisher integration. Restore theme configuration independently from authored content. Keep POSSE off independently and preserve delivery receipts.
