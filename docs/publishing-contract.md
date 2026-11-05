# Publishing contract

## Ownership and workflow

Preserve **Obsidian → sync service → publisher → GitHub → Netlify**. Authors own vault text and originals; the publisher owns the generated files in `.publisher-manifest.json`; maintainers own theme and configuration. Private originals stay outside eligible publishing paths. Drafts are public in preview and remain in Git history.

The current Next Mountain adapter lives in the separate [publisher-daemon repository](https://github.com/markgrovs/publisher-daemon), under `publisher/nextmountain.py`, with `scripts/nextmountain_entrypoint.py`. The mappings below were checked against that source and the site's generated manifest; this document does not certify the deployed service revision.

| Vault source | Site destination |
| --- | --- |
| `posts/<id>/` or `posts/<id>.md` | `content/posts/<id>/index.md` |
| `cairns/<id>/` or `cairns/<id>.md` | `content/cairns/<id>/index.md` |
| `journeys/<id>/` or `journeys/<id>.md` | `content/journeys/<id>/_index.md` |
| `home/index.md` | `content/home/index.md` (headless) |
| `pages/*.md` | `content/*.md` |
| `drafts/*.md` | `content/drafts/*.md` (legacy flat mapping) |

For post, Cairn, and Journey bundles, selection order is the Hugo index filename, a folder-named Markdown note, then a sole Markdown file. IDs match `[a-z0-9][a-z0-9_-]*`. The title is independent of the ID. The current adapter parses YAML lists and nested settings, handles referenced local media, and validates coordinates and paths. Flat pages/drafts receive validation and text copying, not bundle media processing.

The publisher stages and validates its output before applying changes. On a successful sync, files previously recorded in the manifest but absent from the new output are removed. Unmanaged files remain untouched. Do not edit or reset the manifest to retire samples: delete notes at their vault sources. Removing generated files alone allows the next publication to restore them. Git history retains previous versions.

`build-preview` mirrors eligible content, including drafts, to preview. `publish-production` syncs preview and merges it into main, including site changes. Hugo controls draft/future visibility. Publisher success confirms a Git update; check Netlify separately. No live publication or form submission is a test. Service deployment and social delivery require separate authorization.

## Theme and routes

Travelbook is the active theme, authorized on 2026-09-30, and the only maintained theme submodule. Commit and push theme changes in its repository before recording the new commit here. Initialize submodules after cloning. Preserve unrelated working-tree changes.

The isolated theme demo is opt-in under `themes/travelbook/exampleSite/`. Never mount fixtures into the live site's content. Old PaperMod templates, gallery samples, location banner, and hero assets have been retired; Git history provides recovery. Historical design references are retained, not operational instructions.

Journal entries use `/dispatches/:contentbasename/`, preserving identity across title changes. Keep the `/posts/` redirects for existing links. Journeys list newest authored date first regardless of weight, including introductions without linked entries. Daily Journal entries within each Journey read oldest first. The homepage shows all Journeys and up to three recent Cairns. RSS includes published Journal and Cairn entries and excludes drafts and fixture-marked content.

The homepage welcome comes from `params.home_page = "/home"`. Its body and `home_photos` provide the opening; `params.home_heading` provides the heading. The theme supports up to two welcome photographs with `src`, author-written `alt`, and optional `caption`. No demonstration fallback is configured. Journey/Cairn thumbnails are optional page resources. Empty content sections are omitted.

## Media

Preferred syntax:

```markdown
![Author-written alternative text](images/photo.jpg "Optional visible caption")
```

Obsidian image embeds are also supported. The publisher resolves explicitly referenced local assets beside the note or in vault `attachments/`, generates delivery files in `media/`, and rewrites references. JPEG, PNG, and WebP images are orientation-corrected, resized as needed, and re-encoded without original metadata. Downloads and prepared MP4 files are copied; video is not transcoded. Only referenced eligible files are published.

The theme renders local images with dimensions, alt text, and optional captions, without recompressing them. Its optional media-index interface supports supplied responsive variants; the adapter does not generate those variants. Missing required images fail the build. The basic gallery shortcode does not provide a complete wildcard-based publishing workflow or the retired PhotoSwipe grid/lightbox. Photo notes remain Journal entries.

The `ambient-video` shortcode uses muted, looping, inline video with a poster, native controls, and a direct file link. An enhancement supplies pause/play and reduced-motion handling. Explicitly approve delivery clips; do not store master videos in Git.

## Metadata

```yaml
---
date: 2026-11-05
draft: true
authors: [Mark]
location: Your location
journeys: [your-trip-id]
---
```

Omit `title` for daily notes: the heading becomes the ISO date plus location, falling back to the date alone. Supplied titles win. `location` falls back to legacy `place`; no geocoding or device capture is performed. Optional `lat` and `long` are decimal degrees, supplied together and in range. Empty coordinates are accepted. Optional `mileage` supplements the location.

`journeys` is a list of stable trip identifiers used by Journal and Cairn entries. The introduction itself need not reference its own Journey. Remaining references can generate a Journey term after its introduction is deleted.

Journal, Cairn, and Journey headers share a byline and readable calendar date under the title, a quieter update date, and optional location/map/mileage details. `authors` falls back to the site author. Explicit `lastmod` takes priority over the last Git change; dates use the configured timezone. Git timestamps describe repository revisions, not the first public deployment. Light/Dark controls follow the device initially and remember a reader's selection.

The theme emits IndieWeb microformats and configured endpoint discovery. It does not supply Webmention, IndieAuth, Micropub, or syndication services. Never infer social publication from metadata alone.

## Verification and recovery

Run `python3 scripts/check_travelbook.py --hugo hugo` with Hugo 0.166.0, matching `netlify.toml`. The check builds both the theme fixtures and the actual site into temporary ignored directories. Run `node themes/travelbook/tests/appearance.cjs` for preference behavior. See [deployment instructions](../DEPLOYMENT.md) for branch contexts and recovery.

Recover theme/configuration independently from authored content and publisher state. Do not replace current content or ownership records with an old repository snapshot. Preserve delivery receipts and keep social delivery off unless separately authorized.
