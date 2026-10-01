# Quick start

Install Hugo 0.166.0, then run from the repository root:

```sh
hugo server
```

Open http://localhost:1313/. Stop with Ctrl+C. Use `--buildDrafts --buildFuture` to see drafts/future posts.

To inspect the theme's labeled examples instead of authored site content:

```sh
hugo server --source themes/travelbook/exampleSite --port 1314 --renderToMemory --disableFastRender
```

Open http://localhost:1314/.

Local Journal bundles: `hugo new content posts/my-entry/index.md`. Local Cairn bundles: `hugo new content cairns/my-guide/index.md`. New pages are drafts. The deployed publisher's folder support differs; read [the publishing contract](docs/publishing-contract.md) before changing the vault workflow.

Run checks with `python3 scripts/check_travelbook.py --hugo hugo` and `node themes/travelbook/tests/appearance.cjs`. See [README.md](README.md) for configuration, publication, and rollback.
