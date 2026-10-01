# Next Mountain Overland

Mark and Valarie's travel journal, built with Hugo and the local Travelbook theme.

## Local development

Requires Hugo 0.166.0 (the Netlify pin), Python 3 for checks, and Node.js for appearance tests. After cloning, initialize the pinned themes with `git submodule update --init --recursive`.

```sh
hugo server
```

Open http://localhost:1313/. Add `--buildDrafts --buildFuture` for a preview. Draft source remains in Git and may be exposed by preview builds; keep private originals outside eligible publishing paths.

The self-contained theme is in `themes/travelbook/`. Its labeled demo is outside normal content:

```sh
hugo server --source themes/travelbook/exampleSite --renderToMemory --disableFastRender
```

Demo fixtures and the retained legacy validation samples are excluded from the active site's production and preview output.

## Content

- `content/posts/<stable-name>/index.md`: Journal entries at `/dispatches/<stable-name>/`. Text, photographs, long stories, and video context share one template.
- `content/cairns/<stable-name>/index.md`: Practical guides.
- `journeys: [trip-id]`: Groups Journal entries and Cairns. Optional introduction at `content/journeys/<trip-id>/_index.md`.
- `content/about/_index.md`: Existing supplied About page.

The Obsidian → Workbench publisher → GitHub → Netlify workflow remains in place. The daemon currently publishes posts bundles, draft Markdown, and flat pages; Cairn/journey/media integration still requires separate publisher work. See [the publishing contract](docs/publishing-contract.md).

For local bundle authoring:

```sh
hugo new content posts/my-entry/index.md
hugo new content cairns/my-guide/index.md
```

New content starts as `draft: true`. Journal title is optional; location, mileage, journeys, summary, and IndieWeb relationship fields are optional. [The theme guide](themes/travelbook/README.md) documents authoring and media syntax.

## Verification

```sh
python3 scripts/check_travelbook.py --hugo hugo
node themes/travelbook/tests/appearance.cjs
hugo --gc --minify
```

Checks cover the real site, the theme demo, standalone installation, rendered links, feeds, sample exclusion, draft asset exclusion, media failures, and IndieWeb fields. Generated output and test artifacts are ignored by Git.

## Publishing and rollback

`netlify.toml` pins Hugo 0.166.0. Journal redirects preserve existing `/posts/` links. Production RSS includes published Journal and Cairns entries; structural pages and fixtures are excluded. The contact form remains a Netlify form.

Travelbook is a Git submodule from [markgrovs/travelbook](https://github.com/markgrovs/travelbook). This site pins its theme commit; commit the updated submodule pointer whenever upgrading the theme. The PaperMod submodule remains at `themes/PaperMod/`; previous configuration, layouts, styles, and archetypes are retained under `legacy/papermod/` for rollback. Preview it with:

```sh
git submodule update --init --recursive
hugo server --config legacy/papermod/hugo.toml
```

See [deployment instructions](DEPLOYMENT.md). Committing or pushing this branch does not itself verify a Netlify deployment.

## IndieWeb

Travelbook emits microformats for entries, feeds, authors, publication/update dates, content, location, categories, and canonical URLs. It supports supplied reply/like/repost/syndication fields, `rel="me"` profile links, and optional endpoint discovery. No Webmention, IndieAuth, Micropub, or social delivery service is enabled automatically. [Configuration and supported fields](themes/travelbook/README.md#indieweb).

Content © Mark & Valarie. All rights reserved. The Travelbook theme is MIT licensed.
