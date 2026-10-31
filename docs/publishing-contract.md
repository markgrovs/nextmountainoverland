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

## Field Notebook theme interface

The 2026-10-30 design revision presents a stable welcome and a compact latest-entry excerpt, with visible header navigation. Up to four Journeys (ordered by Hugo weight/title) and three recent Cairns are derived from content. Journal archive access stays in the header/footer rather than an additional homepage list. Empty sections are omitted. Entry pages and RSS retain full content. Optional `location` (falling back to `place`) and `mileage` supplement the date.

Warm paper, navy serif typography, rust accents, and optional overlapping photographs implement the Field Notebook direction. The opening works without images. `params.home_heading` controls its heading; `params.home_photos` accepts up to two approved delivery assets with source, author-written alt text, and optional caption. `params.home_page` optionally selects a homepage bundle whose body and `home_photos` supply the welcome. Bundle photos are resolved before global assets. The configured `/home-preview` bundle is draft-only, labeled as a demonstration, and supplies AI-generated illustrative photos only in draft builds. Production falls back to the ordinary homepage. Journey and Cairn bundles may provide a `thumbnail` resource; images are decorative alongside descriptive links. A native SVG landscape footer completes the composition. Publisher support for authoring these settings/assets from Obsidian is still separate integration work.

Reader-controlled Light/Dark buttons follow the device preference initially and remember an explicit choice. Without JavaScript, device appearance and core navigation/reading continue to work.

`themes/travelbook/` is the pinned submodule from https://github.com/markgrovs/travelbook. Theme changes are committed and pushed in that repository first, then its updated commit is recorded in this site. See its README and `exampleSite/minimal.hugo.toml` for installation and explicit site settings.

The `ambient-video` shortcode renders explicitly delivered local MP4s as muted, looping, inline video, with a poster, native controls, and direct file link. A small local script adds a pause/play button and reduced-motion handling. This changes the theme's rendering interface only; it does not implement daemon video processing or authorize storing master video files in Git. The checked-in clip is synthetic test media.

Run `python3 scripts/check_travelbook.py --hugo hugo`. Check artifacts and preview output stay in Git-ignored directories under `themes/travelbook/exampleSite/`.

## IndieWeb interface

The theme renders h-entry/h-feed, author h-card, canonical entry URL/identity, publication and update dates, content, and supplied summary/location/categories. Optional `syndication`, `in_reply_to`, `like_of`, and `repost_of` fields are rendered as their corresponding microformat properties. See the theme README for configuration.

Only configured IndieAuth, Webmention, and Micropub endpoint URLs are advertised. No service backend, external delivery, or social verification is created by theme markup. The publisher's scalar parser remains unchanged, so complete frontmatter/list handling in vault publication is still a Phase B task.

## Approval and recovery

Phase B requires sanitized deployed service definitions, deployed revision identity, and Netlify branch/deploy settings. Theme activation was separately authorized on 2026-09-30. Publisher integration and POSSE still require separate authorization. No live publication is a test.

The gallery section and gallery-validation post are excluded from active production and preview builds through Hugo cascades; their source files remain intact. Legacy templates/styles/configuration/archetypes are retained in legacy/papermod/. The prior theme configuration is recorded in legacy/papermod/hugo.toml; record compatible publisher manifest/state before any later publisher integration. Restore theme configuration independently from authored content. Keep POSSE off independently and preserve delivery receipts.

## Journal location metadata

Use these YAML properties for Journal entries and Cairns; Journey introductions can carry the same location context. Coordinates and labels are supplied by the authoring workflow. The theme performs no geocoding or device capture.

```yaml
---
date: 2026-10-31
lat: 34.20
long: -90.57
location: "Clarksdale, MS"
journeys: [fall-motorcycle-trip-florida]
draft: true
---
```

Coordinates in this example and the design fixtures are approximate illustrative values, not captured travel positions. `lat` and `long` are decimal degrees, with negative longitude west of Greenwich. Latitude must be within -90..90 and longitude within -180..180. Supply both together; zero is valid. Empty properties are accepted while composing a draft. Existing content without coordinates remains compatible. `location` is the supplied display label; the theme does not infer it from coordinates. Legacy `place` remains a fallback.

Omit `title` for daily notes: the heading becomes `YYYY-MM-DD location`, consistently on the entry, Journal/Journey lists, browser title, and RSS. With no place label, the fallback is the ISO date. A deliberately supplied title still wins for longer narratives and Cairns, whose date/location metadata remains visible. Stable filenames continue to determine URLs. Entry metadata uses an ISO date followed by the location. Coordinates power a normal OpenStreetMap link and h-geo markup, without embedding a live map or making a lookup request.

`journeys` is a list of stable Journey identifiers; Journal entries and Cairns can belong to the same trip. Lists are generated automatically. The local archetypes provide the properties but do not install an Obsidian template. Capture tools and publisher integration remain separate work; this change defines the data contract expected by the site.
