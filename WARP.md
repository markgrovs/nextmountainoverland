# Repository development guide

Read [AGENTS.md](AGENTS.md) and [docs/publishing-contract.md](docs/publishing-contract.md).

Travelbook is the only active theme, pinned under `themes/travelbook/`. Hugo 0.166.0 matches the Netlify build. Theme fixtures remain opt-in under `themes/travelbook/exampleSite/`; do not mount them into site content.

```sh
hugo server --buildDrafts --buildFuture
python3 scripts/check_travelbook.py --hugo hugo
node themes/travelbook/tests/appearance.cjs
```

Read [WORKFLOW.md](WORKFLOW.md) for Obsidian authoring and [DEPLOYMENT.md](DEPLOYMENT.md) for delivery. The publisher is maintained separately; do not deploy or change that service as part of theme maintenance. Private originals stay outside eligible publishing paths.
