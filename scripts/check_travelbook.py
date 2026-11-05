#!/usr/bin/env python3
"""Verify the theme and current site without requiring demonstration content."""
import argparse
import csv
import io
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import tomllib
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
THEME = ROOT / 'themes/travelbook'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hugo', default='hugo')
    args = parser.parse_args()
    subprocess.run([sys.executable, str(THEME/'tests/check_theme.py'), '--hugo', args.hugo], check=True)
    helpers = runpy.run_path(str(THEME/'tests/check_theme.py'))
    run, require, audit_links = (helpers[name] for name in ('run', 'require', 'audit_links'))
    # Hugo understands the site's frontmatter and routes; don't duplicate its YAML parser.
    inventory = subprocess.check_output(
        [args.hugo, 'list', 'all', '--source', str(ROOT), '--noBuildLock'], text=True)
    pages = list(csv.DictReader(io.StringIO(inventory)))
    eligible_feed = {p['permalink'] for p in pages
                     if p['section'] in {'posts', 'cairns'} and p['draft'] == 'false'}
    scratch = THEME/'exampleSite/.checks'
    scratch.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='site-check-', dir=scratch) as temporary:
        work = Path(temporary)
        site_config = tomllib.loads((ROOT/'hugo.toml').read_text())
        require(site_config['theme'] == 'travelbook', 'Travelbook is not active')
        require(site_config.get('enableGitInfo'), 'Git update dates disabled')
        require('home_preview_page' not in site_config['params'], 'Retired homepage fallback configured')
        for name, flags in (('production', ()), ('preview', ('--buildDrafts', '--buildFuture'))):
            actual = work/name
            run(args.hugo, ROOT, ROOT/'hugo.toml', actual,
                ('--minify', '--gc', '--environment', name, *flags))
            audit_links(actual)
            for route in ('about', 'contact', 'thank-you'):
                require((actual/route/'index.html').is_file(), f'{route} page missing')
            contact = helpers['Page']((actual/'contact/index.html').read_text())
            forms = [attrs for tag, attrs in contact.elements if tag == 'form']
            require(any(f.get('data-netlify') == 'true' and f.get('action') == '/thank-you/'
                        and f.get('netlify-honeypot') == 'bot-field' for f in forms),
                    'Netlify contact form or success route missing')
            for retired in ('gallery', 'dispatches/2026-08-05-gallery-validation', 'home-preview'):
                require(not (actual/retired).exists(), f'Retired content leaked: {retired}')
            require(not (actual/'dispatches/latest').exists(), 'Theme fixture leaked')
            if name == 'production':
                for page in pages:
                    if page['draft'] == 'true':
                        route = unquote(urlsplit(page['permalink']).path).strip('/')
                        require(not (actual/route/'index.html').exists(), f'Draft leaked: {route}')
                require(not any('sample-' in str(p.relative_to(actual)) for p in actual.rglob('*')),
                        'Sample content or assets leaked into production')
            real_home = (actual/'index.html').read_text()
            require('h-card' in real_home, 'Site author microformat missing')
            require('Local design prototype' not in real_home, 'Theme demo label leaked')
            require('unpkg.com' not in real_home and 'identity.netlify' not in real_home,
                    'Retired external scripts leaked')
            if name == 'preview':
                require(any(tag == 'meta' and attrs.get('name') == 'robots'
                            and 'noindex' in attrs.get('content', '')
                            for tag, attrs in helpers['Page'](real_home).elements),
                        'Preview indexing protection missing')
            feed = ET.parse(actual/'index.xml').findall('./channel/item')
            links = [item.findtext('link') for item in feed]
            require(len(links) == len(set(links)), 'Duplicate RSS entries')
            require(set(links) <= eligible_feed, 'RSS contains drafts or non-Journal/Cairn pages')
            for item in feed:
                route = unquote(urlsplit(item.findtext('link')).path).strip('/')
                require((actual/route/'index.html').is_file(), f'RSS links to missing page: {route}')
                require(bool(item.findtext('description')), f'RSS entry has no content: {route}')
            # Preserve the existing Welcome entry while allowing its title/body to be rewritten.
            welcome = next((p for p in pages if p['path'] == 'content/posts/welcome.md'), None)
            if welcome and welcome['draft'] == 'false' and (actual/'dispatches/welcome/index.html').exists():
                require(welcome['permalink'] in links, 'Published Welcome entry missing from RSS')
        netlify = tomllib.loads((ROOT/'netlify.toml').read_text())
        require(netlify['build']['environment']['HUGO_VERSION'] == '0.166.0', 'Netlify Hugo pin changed')
        require(any(row['from'] == '/posts/*' and row['to'] == '/dispatches/:splat'
                    and row['status'] == 301 for row in netlify['redirects']), 'Post redirects missing')
        require('themes/PaperMod' not in (ROOT/'.gitmodules').read_text(), 'Retired theme still registered')
        print('PASS: current production/preview content, links, Contact form, RSS, redirects, draft exclusion, and theme isolation.')


if __name__ == '__main__':
    main()
