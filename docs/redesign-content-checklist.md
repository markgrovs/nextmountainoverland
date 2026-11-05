# Redesign handoff and content checklist

Reviewed 2026-11-05 against site preview `eb5e41f` and Travelbook `e6fb17e`.

## Branch handoff

- Travelbook: `main` now contains the redesign at `e6fb17e`.
- Site: `preview` already contains the redesign and pins that same theme commit. Its newer publisher commits are preserved.
- Site `main` is not part of this handoff. Production promotion remains a separate step.
- Verification: `python3 scripts/check_travelbook.py --hugo hugo` passes with Hugo 0.166.0, matching `netlify.toml`.

## What you need to write

Paths below are destinations in this Hugo repository, not verified vault source paths. Author publisher-owned files in their vault sources. The current manifest demonstrates homepage, Journey, Cairn, and post delivery, although the older publisher documentation still describes narrower routing. This review does not establish the deployed publisher's source-folder rules or change its code.

| Page or content | Markdown destination | Action |
| --- | --- | --- |
| Homepage welcome | `content/home/index.md` | Replace the current publisher-owned demonstration with your welcome. This is the configured homepage source. |
| About | `content/about/_index.md` | Review/update the existing biography. It already supplies `/about/`; you do not need a second About page. |
| Trip introduction | `content/journeys/<trip-id>/_index.md` | Create one per trip that needs a named introduction. Use the same ID in entry `journeys` lists. |
| Journal entry | `content/posts/<stable-id>/index.md` | Create one per daily note, photo/video note, or longer story. The newest entry fills the homepage excerpt automatically. |
| Cairn | `content/cairns/<stable-id>/index.md` | Create one per review, practical guide, or lesson. The latest three fill the homepage notes area. |
| Contact | `content/contact.md` | Already exists. Retain its form markup and redirect when editing the prose. |
| Thank-you | `content/thank-you.md` | Already exists as the contact-form completion page. Retain it if keeping the form. |

A useful initial content set is a welcome, the updated existing About page, one trip introduction, and one Journal entry assigned to that trip. Add Cairns when you have something to publish; their section is optional. Photos are optional too.

## Pages Hugo generates for you

- `/`: the theme composes the welcome, latest Journal excerpt, up to four Journeys ordered by weight/title, and up to three recent Cairns.
- `/dispatches/`: the Journal archive and pagination, generated from `content/posts/`.
- `/journeys/`: the trip index, generated from the `journeys` taxonomy. Give each trip at least one entry with the matching `journeys` value so it appears in the index/navigation.
- Each trip page: introduction plus matching Journal entries oldest first and related Cairns. Do not copy entries into the trip folder.
- `/cairns/`: the archive of practical notes.
- `/index.xml`: RSS for published Journal entries and Cairns, excluding drafts and fixtures.

You do not need to create `content/_index.md`, `content/posts/_index.md`, `content/cairns/_index.md`, or `content/journeys/_index.md` to obtain this layout. Section `_index.md` files can supply optional introductions. With `params.home_page = "/home"`, use the home bundle for the welcome rather than creating a competing root introduction.

Header navigation is generated for Journal, Journeys, Cairns, and About when those sections qualify. Contact is not currently a header item; creating a Markdown page alone does not add a new navigation item.

## Starting frontmatter

These are templates for your authoring source, not new authored pages added by this handoff. Replace placeholders and dates. Keep `draft: true` while reviewing; change to `false` when ready for production. Remove `fixture: true`, sample notices, and `authors: [Design preview]` from real content. Preview builds show drafts and future-dated content; production does not.

### Homepage: `content/home/index.md`

```yaml
---
title: Home
headless: true
draft: true
---
Your welcome text.
```

`headless: true` makes this a content source for `/`, not a separate reading page. The visible main heading comes from `params.home_heading` in `hugo.toml`, currently defaulting to “A journal of our travels”; the bundle title does not change that heading.

Optional frontmatter for up to two delivered photos:

```yaml
home_photos:
  - src: media/welcome.jpg
    alt: Your description of the photograph
    caption: Optional caption
```

Use the actual publisher-produced resource path. Do not copy hashed sample filenames into real content. Only approved delivery images belong here, never private originals. Omit `home_photos` for a text-only welcome.

### About: existing `content/about/_index.md`

Retain its existing frontmatter and replace the biography as needed. Do not also create `content/about.md` or `content/about/index.md` while this page exists: they compete for the same route. `content/sample-about.md` is a separate demonstration at `/sample-about/`, not the About page used in navigation. Publishing a flat vault `pages/about.md` needs a deliberate transition from the existing About path.

### Journey: `content/journeys/<trip-id>/_index.md`

```yaml
---
title: Your trip name
draft: true
weight: 1
---
Your trip introduction.
```

Use `_index.md` for Journey introductions, unlike the `index.md` leaf bundles used for posts and Cairns. Optional `thumbnail` references a delivered image in the trip bundle. Lower weights appear first; only the first featured homepage Journey displays its thumbnail.

### Journal: `content/posts/<stable-id>/index.md`

```yaml
---
date: 2026-11-05
draft: true
location: Your location
journeys: [your-trip-id]
---
Your daily note or story.
```

Add `title` for a named story; omit it for a heading generated from date and location. The folder ID determines `/dispatches/<stable-id>/`, so keep it stable. Optional fields include `summary`, `mileage`, and paired numeric `lat`/`long`. Omit coordinates when unknown. The latest entry is selected by publication date, not modification date.

### Cairn: `content/cairns/<stable-id>/index.md`

```yaml
---
title: Your guide or review title
date: 2026-11-05
draft: true
journeys: [your-trip-id]
---
Your practical note.
```

Omit `journeys` for a standalone guide. Optional `thumbnail` references a delivered bundle image. Ordinary inline images use `![Your alt text](media/photo.jpg "Optional caption")`; missing referenced images fail the build.

## Samples for you to remove or replace

No sample content was deleted by this handoff. Remove whole sample bundles with their sample media when ready, after checking that any retained content has no references to them.

**Publisher-owned in the current manifest:** remove/replace at the vault source and let the publisher reconcile its outputs. Deleting only generated GitHub files can allow them to return on the next publication.

- Replace `content/home/` with your real welcome and delivery photos.
- Remove `content/sample-about.md`; edit the actual About page separately.
- Journal bundles under `content/posts/`: `sample-backroads`, `sample-daily-note`, `sample-long-story`, `sample-mountains`, `sample-parks`, `sample-photo-note`, `sample-video-note`.
- Journey bundles under `content/journeys/`: `sample-backroads`, `sample-florida-trip`, `sample-mountains`, `sample-parks`.
- Cairn bundles under `content/cairns/`: `sample-overnight-notes`, `sample-packing-review`, `sample-route-notes`.

**Repository-maintained demonstrations outside the current manifest:**

- `content/home-preview/`: draft-only fallback welcome and illustrative photos. When a real `/home` bundle is available it wins; removing only `/home` would reveal this fallback in draft builds. Remove this bundle when retiring the demonstration, and then remove the unused `params.home_preview_page` setting.
- `content/gallery/` (including `sample-album`) and `content/posts/2026-08-05-gallery-validation/`: legacy examples already excluded by configuration from both production and preview. They are not needed for the new layout.
- `themes/travelbook/exampleSite/`: isolated theme fixtures, not deployed site content. Keep these for theme checks; they do not compete with your content.

Do not assume every existing page is disposable: `content/posts/welcome.md`, the real About page, Contact, and Thank-you are existing non-sample content. Review them yourself before deciding whether to retain them. After removing samples, replace any remaining `journeys: [sample-...]` references with your real trip IDs.

## Before a later production promotion

Review preview with your replacement content, confirm intended entries are no longer drafts or fixtures, and run the repository check command again. Draft previews and Git history are public-safe publishing destinations, not storage for private originals. Production promotion of site `preview` into `main` is separate from this handoff.
