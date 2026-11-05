# Deployment

Netlify builds this site with Hugo **0.166.0** and the pinned public HTTPS Travelbook submodule. A fresh checkout must initialize it:

```sh
git submodule update --init --recursive
```

## Check and deliver

```sh
python3 scripts/check_travelbook.py --hugo hugo
node themes/travelbook/tests/appearance.cjs
git diff --check
git status --short
```

Commit and push theme changes to Travelbook first, then update the site’s submodule reference. Preserve publisher commits and unrelated working-tree edits. Push site changes to `preview` for review. Promote to `main` only when authorized.

## Netlify contexts

- `main` / production: published content, using `https://nextmountainoverland.com/`.
- `preview`: drafts and future posts, using `$DEPLOY_PRIME_URL`.
- Pull-request deploy previews: the same draft/future settings.
- Other branch deployments: skipped by the fallback command.

`hugo.toml` enables Git information. Explicit `lastmod` takes precedence over the most recent Git commit date for a page. Git timestamps describe repository edits, not the first public deployment.

The live dashboard controls which branch is production and which branches deploy. Checked-in contexts do not establish those dashboard settings. After a deployment, check its status and the homepage, Journal, Journeys, About, Contact markup, feed, and Light/Dark preference. Do not submit a live contact form as an automated test.

Keep `/posts/` redirects to `/dispatches/` and `/rss` to `/index.xml`: these preserve reader links. Raw HTML rendering remains enabled for the Netlify contact form. Preview and Git history are not private storage.

## Publisher boundary

The service is maintained in [publisher-daemon](https://github.com/markgrovs/publisher-daemon), with the Next Mountain entrypoint and adapter. Editing this site does not redeploy that service. The publisher’s manifest is an ownership record, not a cache; preserve it and deployed state during recovery.

## Recovery

Use Git history to identify and revert the site or theme change that caused a regression. Restore a known theme commit independently of authored content. Do not reset an old snapshot over newer published notes or publisher state. The retired PaperMod implementation is available in history, not maintained as a second installation.
