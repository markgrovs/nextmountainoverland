# Next Mountain Overland

Mark and Valarie’s travel journal, built with Hugo and the Travelbook theme.

## Develop locally

Use Hugo **0.166.0**, matching `netlify.toml`. Initialize the theme after cloning:

```sh
git submodule update --init --recursive
hugo server --buildDrafts --buildFuture
```

Open http://localhost:1313/. Omit the two build flags to view production-eligible content. Drafts are public on the preview site and remain in Git history.

Travelbook is the only theme, pinned at `themes/travelbook/`. Its opt-in demo is isolated from this site:

```sh
hugo server --source themes/travelbook/exampleSite --port 1314 --renderToMemory
```

## Write and publish

Write in Obsidian. The separate [publisher-daemon](https://github.com/markgrovs/publisher-daemon) delivers generated content to this repository; Netlify builds it. Do not edit publisher-owned files here: the next publication replaces them.

- [Authoring and publishing workflow](WORKFLOW.md)
- [Content map](docs/content-map.md)
- [Publishing contract and ownership](docs/publishing-contract.md)
- [Deployment and recovery](DEPLOYMENT.md)
- [Theme authoring reference](themes/travelbook/README.md)

The site keeps a few repository-maintained pages: About, Welcome, Contact, and Thank-you. About and Welcome are retained for an author review. Published post routes remain `/dispatches/<stable-id>/`; redirects preserve older `/posts/` links.

## Verify changes

```sh
python3 scripts/check_travelbook.py --hugo hugo
node themes/travelbook/tests/appearance.cjs
git diff --check
```

Python 3.11+ is required for the site checks. Node.js is used for the appearance behavior check. Checks build production and preview in temporary directories, exercise the theme’s isolated fixtures, and verify links, feeds, metadata, media handling, and draft exclusion. They do not submit forms or publish content.

Commit and push theme changes in the theme repository first, then record its new commit here. Site changes go to `preview` for review. A Git push does not confirm a successful Netlify deployment.

Historical design references remain under `output/design-studies/` and in the labeled redesign checklist. The retired PaperMod implementation and samples are recoverable from Git history.

Content © Mark & Valarie. All rights reserved. Travelbook is MIT licensed.
