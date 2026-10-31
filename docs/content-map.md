# Field Notebook content map

```mermaid
flowchart TD
    Home[Home: welcome and latest entry] --> Journal[Journal: all travel entries]
    Home --> Journeys[Journeys: trips]
    Home --> Cairns[Cairns: reviews and learnings]
    Journal --> Short[Short daily note]
    Journal --> Photo[Photo or video note]
    Journal --> Story[Long travel story]
    Journeys --> Trip[One trip: introduction and chronological entries]
    Trip --> Short
    Trip --> Photo
    Trip --> Story
    Trip --> Cairns
```

| Content | Where readers find it | Site destination |
| --- | --- | --- |
| Short daily update | Journal, latest-entry area, associated Journey | `content/posts/<id>/index.md` → `/dispatches/<id>/` |
| Photo/video note | Same as any Journal entry; no separate gallery required | Same post bundle, with delivery media |
| Long travel narrative | Journal and associated Journey | Same post bundle |
| Practical review or learning | Cairns, homepage notes, related Journey | `content/cairns/<id>/index.md` |
| Trip introduction | Journeys and its trip page; entries collected automatically | `content/journeys/<trip-id>/_index.md` |
| About | Header/footer navigation | Existing About page |

A Journey is a collection, not a post type. A long story stays in the Journal; a reusable review or guide belongs in Cairns. `journeys: [trip-id]` connects either kind to a trip. Entry lists require no duplicate writing.

## Draft review examples

The `sample-*` bundles are authorized design examples, labeled as samples, `draft: true`, and `fixture: true`. They contain explanatory sample text and synthetic media, not invented first-person travel accounts. Normal production builds exclude their pages and resources. Draft previews include them; RSS excludes them. They are public-safe Git content, not private drafts.

Run `hugo server --buildDrafts` to see the populated homepage, Journal, Journey, and Cairn views. The newest example is intentionally a short text-only daily update. Remove or replace the sample bundles when real content is ready.

## Authoring boundary

All types are intended to be authored in Obsidian. The existing publisher mapping supports post bundles; complete routing for Cairns, Journey introductions, and homepage media/settings remains integration work. These review examples are hand-maintained fixtures outside publisher ownership, not a new daily authoring workflow. Do not use this document as evidence that new publisher routing has been implemented.

## Visual review

The draft-only `content/home-preview/index.md` bundle supplies the demonstration welcome and two AI-generated illustrative photos. `params.home_page` selects it when draft builds include it; production falls back to the normal homepage and never emits these draft photos. This is a stable welcome, not a Journal entry.

Desktop placement: welcome and latest Journal note on the left; overlapping opening photos on the right. Below, the left column shows four Journeys (first featured with a thumbnail); the right shows three recent Cairns with optional thumbnails. The landscape footer holds navigation, following links, and appearance controls. On phones these sections stack in that order. Daily entries remain in the Journal archive and associated Journey; there is no extra homepage archive list.

The preview uses two illustrative images repeatedly to demonstrate optional thumbnails. They are not photographs of the travelers or evidence of real trips. Homepage body/photo and thumbnail interfaces are ready in the theme; authoring and routing them through the publisher still needs integration. The existing video shortcode autoplays muted; the original no-autoplay preference still needs resolution separately.

## Daily-note heading

The daily-note, photo-note, video-note, and small trip examples intentionally omit `title`. The latest daily note displays `2026-10-31 Clarksdale, MS`, derived from `date` and `location`. All sample entry and Journey bundles supply illustrative `lat`, `long`, and `location` properties. The longer story and Cairns keep descriptive titles. The draft homepage introduction has empty location properties because it does not represent a dated stop. See the publishing contract for the complete metadata schema.
