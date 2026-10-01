# Repository development guide

Read [AGENTS.md](AGENTS.md) and [docs/publishing-contract.md](docs/publishing-contract.md).

The active theme is Travelbook under `themes/travelbook/`, targeting Hugo 0.166.0. Authored content stays under `content/`; labeled theme fixtures are isolated in `themes/travelbook/exampleSite/`. Legacy PaperMod configuration/templates/styles are retained in `legacy/papermod/`.

```sh
hugo server
hugo server --source themes/travelbook/exampleSite --port 1314 --renderToMemory
python3 scripts/check_travelbook.py --hugo hugo
node themes/travelbook/tests/appearance.cjs
hugo --gc --minify
```

Journal bundles use the existing `posts` source section with `/dispatches/` visitor routes. Journeys are taxonomy terms; Cairns are guides; About is a structural page. Theme authoring/interfaces are documented in its README. Publisher integration and live service changes need separate authorization. Private originals must remain outside eligible publishing paths.
