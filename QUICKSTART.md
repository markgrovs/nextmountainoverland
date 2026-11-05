# Quick start

With Hugo 0.166.0 installed:

```sh
git submodule update --init --recursive
hugo server --buildDrafts --buildFuture
```

Open http://localhost:1313/. Stop with Ctrl+C. Omit draft/future flags for a production-like view.

Write in Obsidian using [the publishing workflow](WORKFLOW.md). Do not edit generated publisher-owned files in this checkout.

For theme examples isolated from site content:

```sh
hugo server --source themes/travelbook/exampleSite --port 1314 --renderToMemory
```

Run `python3 scripts/check_travelbook.py --hugo hugo` before delivering changes. See [README.md](README.md) for the full verification commands and [DEPLOYMENT.md](DEPLOYMENT.md) for deployment and recovery.
