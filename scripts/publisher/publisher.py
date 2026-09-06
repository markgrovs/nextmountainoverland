#!/usr/bin/env python3
"""
Next Mountain Overland - Blog Publisher Daemon
Monitors synced NextMountain-Blog vault, processes drafts and images,
manages Git branches, and resets PUBLISH.md.
"""

import os
import re
import sys
import time
import shutil
import logging
import subprocess
from pathlib import Path
from PIL import Image

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

VAULT_DIR = Path(os.environ.get("VAULT_DIR", "/vault"))
REPO_DIR = Path(os.environ.get("REPO_DIR", "/repo"))
PUBLISH_FILE = VAULT_DIR / "PUBLISH.md"
POLL_INTERVAL = int(os.environ.get("POLL_INTERVAL", "5"))
MAX_IMAGE_WIDTH = int(os.environ.get("MAX_IMAGE_WIDTH", "1800"))
IMAGE_QUALITY = int(os.environ.get("IMAGE_QUALITY", "82"))

FRONTMATTER_PATTERN = re.compile(r"^---\s*
(.*?)
---\s*
(.*)$", re.DOTALL)
WIKILINK_IMG_PATTERN = re.compile(r"!\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
STANDARD_IMG_PATTERN = re.compile(r"!\[(.*?)\]\((.*?)\)")

def parse_frontmatter(text: str):
    m = FRONTMATTER_PATTERN.match(text)
    if not m:
        return {}, text
    raw_yaml, body = m.group(1), m.group(2)
    data = {}
    for line in raw_yaml.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip().strip("'"")
    return data, body

def update_publish_state(action: str, status_msg: str):
    if not PUBLISH_FILE.exists():
        return
    text = PUBLISH_FILE.read_text(encoding="utf-8")
    m = FRONTMATTER_PATTERN.match(text)
    body = m.group(2) if m else text
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    new_content = f'''---
action: {action}
target: current
last_run: {timestamp}
last_status: {status_msg}
---
{body}'''
    PUBLISH_FILE.write_text(new_content, encoding="utf-8")
    logging.info(f"Updated PUBLISH.md: action={action}, status={status_msg}")

def run_git(args, check=True):
    cmd = ["git", "-C", str(REPO_DIR)] + args
    res = subprocess.run(cmd, capture_output=True, text=True)
    if check and res.returncode != 0:
        raise RuntimeError(f"Git failed: {' '.join(cmd)}
Stderr: {res.stderr}
Stdout: {res.stdout}")
    return res

def optimize_image(src_path: Path, dest_path: Path):
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with Image.open(src_path) as img:
            img = img.convert("RGB")
            if img.width > MAX_IMAGE_WIDTH:
                height = int((MAX_IMAGE_WIDTH / img.width) * img.height)
                img = img.resize((MAX_IMAGE_WIDTH, height), Image.Resampling.LANCZOS)
            img.save(dest_path, "JPEG", quality=IMAGE_QUALITY, optimize=True)
            logging.info(f"Optimized image: {src_path.name} -> {dest_path.name}")
    except Exception as e:
        logging.warning(f"Failed to optimize image {src_path.name}: {e}. Copying raw fallback.")
        shutil.copy2(src_path, dest_path)

def process_markdown_and_assets(post_md_file: Path, target_bundle_dir: Path):
    target_bundle_dir.mkdir(parents=True, exist_ok=True)
    images_dest_dir = target_bundle_dir / "images"
    images_dest_dir.mkdir(parents=True, exist_ok=True)
    content = post_md_file.read_text(encoding="utf-8")
    referenced_images = set()
    for match in WIKILINK_IMG_PATTERN.finditer(content):
        referenced_images.add(match.group(1).strip())
    for match in STANDARD_IMG_PATTERN.finditer(content):
        img_url = match.group(2).strip()
        if not img_url.startswith("http") and not img_url.startswith("/"):
            referenced_images.add(Path(img_url).name)
    vault_posts_img_dir = post_md_file.parent / "images"
    vault_attachments_dir = VAULT_DIR / "attachments"
    for img_name in referenced_images:
        found_src = None
        if (vault_posts_img_dir / img_name).exists():
            found_src = vault_posts_img_dir / img_name
        elif (vault_attachments_dir / img_name).exists():
            found_src = vault_attachments_dir / img_name
        elif (post_md_file.parent / img_name).exists():
            found_src = post_md_file.parent / img_name
        if found_src:
            dest_file = images_dest_dir / img_name
            optimize_image(found_src, dest_file)
        else:
            logging.warning(f"Referenced image not found in vault: {img_name}")
    def wikilink_sub(match):
        img_name = match.group(1).strip()
        alt = match.group(2).strip() if match.group(2) else img_name
        return f"![{alt}](images/{img_name})"
    converted_content = WIKILINK_IMG_PATTERN.sub(wikilink_sub, content)
    dest_index = target_bundle_dir / "index.md"
    dest_index.write_text(converted_content, encoding="utf-8")
    logging.info(f"Processed post saved to {dest_index}")

def sync_all_posts():
    vault_posts = VAULT_DIR / "posts"
    if not vault_posts.exists():
        logging.warning("No posts/ directory in vault.")
        return
    content_posts_dir = REPO_DIR / "content" / "posts"
    content_posts_dir.mkdir(parents=True, exist_ok=True)
    for item in vault_posts.iterdir():
        if item.is_dir():
            md_files = list(item.glob("*.md"))
            if md_files:
                target_bundle = content_posts_dir / item.name
                process_markdown_and_assets(md_files[0], target_bundle)
        elif item.is_file() and item.suffix.lower() == ".md":
            slug = item.stem
            target_bundle = content_posts_dir / slug
            process_markdown_and_assets(item, target_bundle)

def handle_publish(target_branch: str):
    logging.info(f"Starting publish cycle targeting branch: {target_branch}")
    time.sleep(2)
    run_git(["fetch", "origin"])
    run_git(["checkout", target_branch])
    run_git(["reset", "--hard", f"origin/{target_branch}"])
    sync_all_posts()
    status_res = run_git(["status", "--porcelain"])
    if not status_res.stdout.strip():
        logging.info("No changes to commit.")
        update_publish_state("idle", f"SUCCESS - No changes (branch: {target_branch})")
        return
    run_git(["add", "content/posts/"])
    commit_msg = f"Automated publish from iPad ({target_branch}): {time.strftime('%Y-%m-%d %H:%M')}"
    run_git(["commit", "-m", commit_msg])
    run_git(["push", "origin", target_branch])
    rev_res = run_git(["rev-parse", "--short", "HEAD"])
    commit_hash = rev_res.stdout.strip()
    logging.info(f"Successfully pushed {commit_hash} to {target_branch}")
    update_publish_state("idle", f"SUCCESS - Pushed to {target_branch} ({commit_hash})")

def main_loop():
    logging.info("Next Mountain Overland Publisher Daemon started.")
    logging.info(f"Monitoring: {PUBLISH_FILE}")
    while True:
        try:
            if PUBLISH_FILE.exists():
                text = PUBLISH_FILE.read_text(encoding="utf-8")
                frontmatter, _ = parse_frontmatter(text)
                action = frontmatter.get("action", "idle").strip().lower()
                if action == "build-preview":
                    logging.info("Detected command: build-preview")
                    update_publish_state("processing", "Building preview branch...")
                    handle_publish("preview")
                elif action == "publish-production":
                    logging.info("Detected command: publish-production")
                    update_publish_state("processing", "Publishing to production...")
                    handle_publish("main")
        except Exception as e:
            logging.error(f"Error during publish cycle: {e}", exc_info=True)
            try:
                update_publish_state("error", f"ERROR: {str(e)[:100]}")
            except Exception:
                pass
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main_loop()
