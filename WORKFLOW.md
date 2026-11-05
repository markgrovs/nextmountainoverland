# Writing and publishing

Author in the synced Obsidian vault. Content flows **Obsidian → sync service → publisher → GitHub → Netlify**. This repository is the delivery destination, not the vault.

## Where to write

| Vault source | Purpose | Generated site file |
| --- | --- | --- |
| `posts/<id>/` | Daily notes, stories, photo/video notes | `content/posts/<id>/index.md` |
| `cairns/<id>/` | Practical guides and lessons | `content/cairns/<id>/index.md` |
| `journeys/<id>/` | Trip introduction | `content/journeys/<id>/_index.md` |
| `home/index.md` | Homepage welcome and photos | `content/home/index.md` |
| `pages/<name>.md` | Standalone page | `content/<name>.md` |

For posts, Cairns, and Journeys, Folder Notes are supported: `<id>/<id>.md` is valid. Hugo’s `index.md` (or `_index.md` for Journeys) takes precedence if present; otherwise the publisher selects the folder-named note or a sole Markdown file. Flat `<id>.md` notes also work. IDs start with a lowercase letter or digit and contain only lowercase letters, digits, hyphens, and underscores. Titles can use normal capitalization and spaces.

Do not create `pages/about.md` without first transitioning the repository-maintained `content/about/_index.md`; both would target `/about/`.

## Properties

```yaml
---
date: 2026-11-05
draft: true
authors: [Mark]
location: Your location
journeys: [fall-2026-southern-usa-shakeout-ride]
---
```

`title` is optional for daily notes; the date and location supply the heading. Use a title for longer stories, guides, and trip introductions. `authors` accepts a name or list, falling back to the site author. Optional coordinates use `lat` and `long`, supplied together. `mileage` and `summary` are optional.

A Journey introduction can omit `journeys`. Posts and Cairns join it through that list. Journeys sort newest date first; daily entries within a Journey read oldest first. No `weight`, `type`, or feature flag is required. `fixture: true` is only for demonstration content and should not be copied into real writing.

## Photographs and video

Place delivery images beside the note, in a subfolder with a relative reference, or in the vault’s shared `attachments/` folder. Reference them explicitly:

```markdown
![Author-written alternative text](images/photo.jpg "Optional visible caption")
```

Obsidian `![[photo.jpg]]` embeds are supported. The publisher copies referenced assets into a bundle’s `media/` directory and rewrites paths. A Journey or Cairn can set `thumbnail: photo.jpg`. Homepage photos use `home_photos` entries with `src`, `alt`, and optional `caption`; `home/index.md` is made headless automatically.

Photo notes are normal Journal entries. The old PhotoSwipe gallery workflow is retired. Travelbook’s basic gallery shortcode is not a complete publisher workflow: wildcard-only references do not cause images to be copied. Use explicit image references for now.

Prepared local MP4s and posters can use the theme’s `ambient-video` shortcode. The publisher copies video without transcoding; the player is muted, looping, and has controls. Keep private originals outside eligible publishing paths.

## Preview and production

1. Finish editing and wait for the vault, including media, to sync.
2. In `PUBLISH.md`, set `action: build-preview`.
3. Read `last_status`, then wait for Netlify and review the [preview site](https://preview--nextmountainoverland.netlify.app/).
4. Set `draft: false` on content ready for production; preview again.
5. Use `action: publish-production` only when ready to promote. This syncs the vault and merges the entire preview branch into main, including site changes.

Preview builds include drafts and future-dated content. Production excludes both. The publisher resets the action to idle and records status; a successful status confirms Git publication, not Netlify deployment.

## Delete or replace content

Delete the note in Obsidian, let the deletion sync, then build preview. The publisher removes its generated note and assets listed in `.publisher-manifest.json`. Removing an image reference also removes the unused delivery copy. Vault originals are untouched; other posts retain their own copies of shared images. Git history still contains earlier versions.

Files never recorded in the manifest are repository-maintained and need deliberate cleanup here. Do not hand-edit or reset the manifest to remove samples. Delete remaining sample notes at their vault sources. Remove stale `journeys` references too: Hugo can generate a trip page from a remaining reference even without an introduction.
