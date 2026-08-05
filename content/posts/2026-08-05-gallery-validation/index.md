---
title: "Gallery Validation Post"
date: 2026-08-05
draft: true
tags: ["test", "gallery"]
categories: ["Validation"]
description: "Validating the in-post gallery shortcode with PhotoSwipe lightbox."
cover:
    image: "images/photo-1.jpg"
    alt: "Validation cover image"
    caption: "Cover shot"
    relative: true
---

This post validates the in-post gallery shortcode. Two photos live in the `images/` subfolder of this page bundle.

<!--more-->

## The Gallery

Drop the shortcode below and it globs all images in the bundle:

```
{{< gallery pattern="images/*" >}}
```

Rendered:

{{< gallery pattern="images/*" >}}

## Notes

- Thumbnails are auto-generated at 600px width, 80% quality.
- Full-size lightbox images are capped at 2048px, 85% quality.
- PhotoSwipe loads only on pages that contain the gallery shortcode.
