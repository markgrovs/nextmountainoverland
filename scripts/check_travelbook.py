#!/usr/bin/env python3
"""Check the pinned Travelbook theme and this site's production/preview contract."""
import argparse
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import tomllib
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
    scratch = THEME/'exampleSite/.checks'
    scratch.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='site-check-', dir=scratch) as temporary:
        work = Path(temporary)
        # Verify the activated site, not only the theme fixtures.
        site_config = tomllib.loads((ROOT/'hugo.toml').read_text())
        require(site_config['theme'] == 'travelbook', 'Travelbook is not active')
        for name, flags in (('real-production', ()), ('real-preview', ('--buildDrafts','--buildFuture'))):
            actual = work/name
            run(args.hugo, ROOT, ROOT/'hugo.toml', actual, ('--minify','--gc', *flags))
            audit_links(actual)
            require((actual/'dispatches/welcome/index.html').is_file(), 'Existing entry missing')
            require((actual/'about/index.html').is_file(), 'About page missing')
            require((actual/'thank-you/index.html').is_file(), 'Contact success page missing')
            contact = (actual/'contact/index.html').read_text()
            require('data-netlify=true' in contact or 'data-netlify="true"' in contact, 'Netlify form missing')
            require(not (actual/'gallery').exists(), 'Legacy sample gallery or assets leaked')
            require(not (actual/'dispatches/2026-08-05-gallery-validation').exists(), 'Validation bundle leaked')
            require(not (actual/'dispatches/latest').exists(), 'Theme fixture leaked')
            real_home = (actual/'index.html').read_text()
            require('h-entry' in real_home and 'e-content' in real_home and 'h-card' in real_home, 'Site IndieWeb markup missing')
            require('Local design prototype' not in real_home, 'Demo label leaked')
            require('unpkg.com' not in real_home and 'identity.netlify' not in real_home, 'Legacy external scripts leaked')
            feed = ET.parse(actual/'index.xml').findall('./channel/item')
            require([item.findtext('title') for item in feed] == ['Welcome to Next Mountain Overland'], 'Site RSS membership wrong')
            require('The 2027 Challenge' in feed[0].findtext('description'), 'RSS does not contain full content')
        netlify = tomllib.loads((ROOT/'netlify.toml').read_text())
        require(netlify['build']['environment']['HUGO_VERSION'] == '0.166.0', 'Netlify Hugo pin changed')
        require(any(row['from'] == '/posts/*' and row['to'] == '/dispatches/:splat' and row['status'] == 301 for row in netlify['redirects']), 'Legacy post redirects missing')
        require((ROOT/'legacy/papermod/hugo.toml').is_file(), 'Rollback configuration missing')
        print('PASS: activated production/preview site, existing authored pages, Contact form, full RSS, redirects, and fixture/sample exclusion.')

if __name__ == '__main__': main()
