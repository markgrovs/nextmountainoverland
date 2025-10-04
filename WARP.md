# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Development Commands

### Local Development
```bash
# Run development server with drafts enabled
hugo server -D

# Run development server without drafts
hugo server

# Create new post
hugo new posts/YYYY-MM-DD-post-name.md

# Build for production
hugo --gc --minify
```

### Content Management
```bash
# Create new about page
hugo new about/page-name.md

# Create backup of content
tar -czf nextmtn-backup-$(date +%Y%m%d).tar.gz content/ static/

# Validate site build
hugo --gc --minify && cd public && python3 -m http.server 8000
```

## Project Architecture

### Core Components
- **Hugo Static Site Generator** (v0.120.0+)
- **PaperMod Theme** - Main theme, installed as git submodule
- **Netlify** - Build and deployment platform

### Directory Structure
```
nextmountainoverland/
├── content/            # All site content
│   ├── posts/         # Blog posts
│   └── about/         # About pages
├── static/            # Static assets
│   └── images/        # Optimized images by date (YYYY/MM/)
├── layouts/           # Custom layout overrides
│   └── shortcodes/    # Custom shortcodes
├── themes/PaperMod/   # Theme (git submodule)
├── hugo.toml          # Site configuration
└── netlify.toml       # Deployment configuration
```

### Content Organization
- Posts use YYYY-MM-DD-title.md naming convention
- Images follow YYYY-MM-DD-description.jpg pattern
- Categories: Travel, Pan Am Prep, Photo Essay
- Standard image sizes:
  - Cover: 1200x630px
  - Gallery: 1200px wide
  - Inline: 800px wide

### Shortcodes
```
# Single image with caption
{{</* img src="/images/photo.jpg" alt="Description" caption="Caption" */>}}

# Photo gallery
{{</* gallery images="/images/1.jpg,/images/2.jpg,/images/3.jpg" */>}}

# Instagram embed
{{</* instagram "POST_ID" */>}}
```

## Configuration

### Build Environment
- Hugo Extended (v0.120.0+)
- Node.js (for Netlify CLI if used)
- Git with LFS support (for image management)

### Environment Variables
```
HUGO_VERSION=0.120.0
HUGO_ENV=production
HUGO_ENABLEGITINFO=true
```

## Deployment

### Production Build
```bash
# Clean and optimize
hugo --gc --minify

# Deploy via Netlify CLI
netlify deploy --prod
```

### Preview Builds
```bash
# Deploy preview (for PRs)
hugo --gc --minify --buildFuture -b $DEPLOY_PRIME_URL

# Branch deploy
hugo --gc --minify -b $DEPLOY_PRIME_URL
```