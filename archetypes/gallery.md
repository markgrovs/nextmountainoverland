---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
draft: true
description: ""
cover:
    image: ""
    alt: ""
    caption: ""
---

{{/* Drop images into this folder. They will auto-render as a PhotoSwipe lightbox gallery. */}}
