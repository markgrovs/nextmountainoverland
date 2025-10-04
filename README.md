# Next Mountain Overland

Hugo-based travel blog for Mark and Valarie's overland adventures.

## About

This site documents our journey from RV adventures in NextMtn to preparing for our 2027 Pan American Highway motorcycle expedition from Colorado to Argentina.

## Quick Start

### Prerequisites

- [Hugo Extended](https://gohugo.io/installation/) (v0.120.0 or later)
- Git

### Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR-USERNAME/nextmountainoverland.git
cd nextmountainoverland
```

2. Install the PaperMod theme:
```bash
git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
git submodule update --init --recursive
```

3. Run the development server:
```bash
hugo server -D
```

4. Open your browser to `http://localhost:1313`

## Creating Content

### New Post

```bash
hugo new posts/my-new-post.md
```

This creates a new post with the proper front matter template.

### Adding Images

1. Place images in `static/images/`
2. Reference in posts: `![Alt text](/images/photo.jpg)`
3. Or use the custom shortcode: `{{</* img src="/images/photo.jpg" alt="Description" caption="Photo caption" */>}}`

### Photo Gallery

Use the gallery shortcode:
```
{{</* gallery images="/images/photo1.jpg,/images/photo2.jpg,/images/photo3.jpg" */>}}
```

### Instagram Embeds

```
{{</* instagram "POST_ID" */>}}
```

## Project Structure

```
nextmountainoverland/
├── archetypes/          # Content templates
├── content/
│   ├── posts/          # Blog posts
│   └── about/          # About pages
├── layouts/
│   └── shortcodes/     # Custom shortcodes
├── static/
│   └── images/         # Images and media
├── themes/
│   └── PaperMod/       # Theme (git submodule)
└── hugo.toml           # Site configuration
```

## Deployment

### Netlify

1. Push to GitHub
2. Connect repository to Netlify
3. Build settings:
   - Build command: `hugo --gc --minify`
   - Publish directory: `public`
   - Environment variables: `HUGO_VERSION = 0.120.0`

### Manual Build

```bash
hugo --gc --minify
```

Output will be in the `public/` directory.

## Configuration

Main configuration is in `hugo.toml`. Key settings:

- `baseURL`: Update to your domain
- `title`: Site title
- `params`: Theme-specific settings
- `menu`: Navigation menu items

## Writing Tips

### Front Matter

Every post should have:
```yaml
---
title: "Post Title"
date: 2025-10-04
draft: false
tags: ["tag1", "tag2"]
categories: ["Category"]
description: "Brief description for SEO"
cover:
    image: "/images/cover.jpg"
    alt: "Cover image description"
    caption: "Photo caption"
---
```

### Content Organization

- Use `<!--more-->` to create post excerpts
- Add tags organically (they auto-generate tag pages)
- Use descriptive filenames (becomes the URL slug)

## Open Web Features

- Full-content RSS feed at `/index.xml`
- Semantic HTML markup
- No tracking by default
- Privacy-respecting embeds

## Customization

### Colors and Styling

PaperMod supports custom CSS. Create `assets/css/extended/custom.css` for overrides.

### Adding New Sections

1. Create directory in `content/`
2. Add `_index.md` for section page
3. Update menu in `hugo.toml`

## Support

- [Hugo Documentation](https://gohugo.io/documentation/)
- [PaperMod Wiki](https://github.com/adityatelange/hugo-PaperMod/wiki)

## License

Content © Mark & Valarie. All rights reserved.

---

Built with ❤️ and [Hugo](https://gohugo.io/)
