# Quick Start Guide

## First Time Setup

### 1. Install Hugo

**macOS (using Homebrew):**
```bash
brew install hugo
```

**Verify installation:**
```bash
hugo version
```

You should see version 0.120.0 or later.

### 2. Install the Theme

From the project root directory:

```bash
git init
git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
git submodule update --init --recursive
```

### 3. Run Locally

```bash
hugo server -D
```

Open your browser to: `http://localhost:1313`

The `-D` flag shows draft posts. Remove it to see only published content.

## Creating Your First Post

### Using Hugo Command

```bash
hugo new posts/my-first-post.md
```

This creates: `content/posts/my-first-post.md`

### Manual Creation

Create a file in `content/posts/` with this front matter:

```markdown
---
title: "My First Post"
date: 2025-10-04
draft: false
tags: ["travel", "baja"]
categories: ["Travel Log"]
description: "A brief description of the post"
---

Your content here...

<!--more-->

More content after the break...
```

## Adding Photos

### Single Image

1. Add image to `static/images/`
2. In your post:

```markdown
![Description](/images/photo.jpg)
```

Or use the custom shortcode for more control:

```markdown
{{</* img src="/images/photo.jpg" alt="Description" caption="Sunset in Baja" */>}}
```

### Photo Gallery

```markdown
{{</* gallery images="/images/photo1.jpg,/images/photo2.jpg,/images/photo3.jpg" */>}}
```

### Cover Image

Add to post front matter:

```yaml
cover:
    image: "/images/cover.jpg"
    alt: "Cover image description"
    caption: "Photo caption"
    relative: false
```

## Publishing a Post

Change `draft: true` to `draft: false` in the front matter, or remove the draft line entirely.

## Common Tasks

### Preview Without Drafts
```bash
hugo server
```

### Build for Production
```bash
hugo --gc --minify
```

### Create New About Page
```bash
hugo new about/page-name.md
```

## Tips for Writing on the Road

### Mobile Workflow

1. **Use a text editor app** (iA Writer, 1Writer, etc.)
2. **Write in Markdown** - it's just text
3. **Sync via iCloud/Dropbox** to your content folder
4. **Commit and push** when you have internet

### Quick Post Template

Save this as a template in your notes app:

```markdown
---
title: ""
date: 2025-10-04
draft: false
tags: []
---

Quick thoughts...

<!--more-->

Full story...
```

## Troubleshooting

### Theme Not Found
```bash
git submodule update --init --recursive
```

### Port Already in Use
```bash
hugo server -D -p 1314
```

### Clear Cache
```bash
hugo --gc
```

## Next Steps

1. ✅ Get site running locally
2. ✅ Create your first post
3. ✅ Add some photos
4. 📝 Set up GitHub repository
5. 📝 Deploy to Netlify
6. 📝 Point domain to Netlify

See `DEPLOYMENT.md` for deployment instructions.
