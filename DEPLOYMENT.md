# Deployment

Travelbook is the active theme. Netlify builds with Hugo 0.166.0 using the checked-in `netlify.toml`; Travelbook is pinned as a public HTTPS Git submodule. A fresh checkout must initialize submodules; Netlify must fetch them during checkout.

For a fresh local checkout, run `git submodule update --init --recursive`.

## Before committing

```sh
python3 scripts/check_travelbook.py --hugo hugo
node themes/travelbook/tests/appearance.cjs
git diff --check
git status --short
```

Review authored content and the final diff, then commit and push the desired branch using your normal Git workflow. The theme demo stays under `themes/travelbook/exampleSite/`; output/resources/cache/check directories are ignored. Python bytecode is also ignored. The previously deleted tracked Python cache is not restored.

## Netlify configuration

- Production: `hugo --gc --minify --baseURL https://nextmountainoverland.com/`.
- Named `preview` branch context: builds drafts and future posts using the deploy URL.
- Other branch deploys: the checked-in fallback skips builds.
- Legacy Journal routes redirect from `/posts/` to `/dispatches/`.
- Gallery and validation sample content stays in the repository but is excluded by Hugo build cascades.

Verify production-branch and branch-deploy settings in the actual Netlify dashboard; checked-in contexts do not establish the live dashboard configuration. A successful local build or Git push is not deployment verification. This change does not alter the Workbench publisher service.

After an intended deployment, verify the production homepage, Journal, About, Contact form, feed, post redirects, and Light/Dark preference. Do not use a live form submission or live publisher action as an automated check.

## Rollback

PaperMod remains available as the original submodule. Previous templates, styles, archetypes, and compatible configuration are in `legacy/papermod/`.

```sh
git submodule update --init --recursive
hugo server --config legacy/papermod/hugo.toml
```

For an intentional rollback, restore the legacy configuration with its explicit layout/asset/archetype paths. Review `/dispatches/` compatibility and Netlify redirects at that time. Do not reset older repository content over newer authored material. Publisher code, ownership state, and social-delivery state are separate from theme rollback.
