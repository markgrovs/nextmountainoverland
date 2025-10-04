# Content Creation Workflow

## Writing from the Road

### Mobile-First Approach

Since you'll be traveling, here's a workflow that works from anywhere:

#### Option 1: Direct GitHub Editing (Simplest)

1. Go to your GitHub repository on mobile
2. Navigate to `content/posts/`
3. Click "Add file" → "Create new file"
4. Name it: `2025-10-04-post-title.md`
5. Write your post in markdown
6. Commit directly to main
7. Netlify auto-deploys in ~2 minutes

**Pros:** Works anywhere with internet, no apps needed
**Cons:** Limited editing features, need internet

#### Option 2: Text Editor + Git (Recommended)

**Apps you'll need:**
- **iA Writer** or **1Writer** (iOS) - Markdown editors with folder sync
- **Working Copy** (iOS) - Git client for iOS

**Workflow:**
1. Write post in iA Writer (syncs to iCloud)
2. Open Working Copy
3. Pull latest changes
4. Copy post from iCloud to repo
5. Commit and push
6. Auto-deploys!

#### Option 3: Obsidian (If you use it)

1. Set up Obsidian vault in your repo's `content/` folder
2. Write posts in Obsidian
3. Use Obsidian Git plugin to sync
4. Auto-deploys on push

### Desktop Workflow

```bash
# Start writing
hugo new posts/my-new-post.md

# Preview locally
hugo server -D

# When ready, publish
# (change draft: false in front matter)

# Commit and push
git add .
git commit -m "New post: My New Post"
git push

# Automatically deploys!
```

## Post Templates

### Travel Log Template

Save this for quick travel posts:

```markdown
---
title: "Day in [Location]"
date: 2025-10-04
draft: false
tags: ["travel-log", "location-name"]
categories: ["Travel"]
description: "Quick summary of the day"
cover:
    image: "/images/2025-10-04-cover.jpg"
    alt: "Description"
---

Quick intro about where we are and what we're doing...

<!--more-->

## Morning

What happened in the morning...

## Afternoon

Afternoon adventures...

## Evening

Evening reflections...

## Photos

{{</* gallery images="/images/photo1.jpg,/images/photo2.jpg,/images/photo3.jpg" */>}}

## Location

- **Where:** Exact location
- **Campsite:** Name/coordinates
- **Weather:** Conditions
- **Mileage:** Miles driven today
```

### 2027 Prep Template

For motorcycle preparation posts:

```markdown
---
title: "2027 Prep: [Topic]"
date: 2025-10-04
draft: false
tags: ["2027-prep", "motorcycles", "specific-topic"]
categories: ["Pan Am Prep"]
description: "Progress update on [topic]"
---

What we're working on this week for the 2027 Pan American journey...

<!--more-->

## Current Status

- ✅ Completed
- 🔄 In Progress
- ⏳ Not Started

## This Week's Progress

Details...

## Lessons Learned

What we discovered...

## Next Steps

What's coming next...
```

### Photo Essay Template

For image-heavy posts:

```markdown
---
title: "Photos: [Location/Event]"
date: 2025-10-04
draft: false
tags: ["photos", "location"]
categories: ["Photo Essay"]
description: "Visual journey through [location]"
cover:
    image: "/images/cover.jpg"
    alt: "Description"
---

Brief intro...

<!--more-->

{{</* gallery images="/images/1.jpg,/images/2.jpg,/images/3.jpg,/images/4.jpg,/images/5.jpg,/images/6.jpg" */>}}

## Caption Section

Individual photos with stories...

{{</* img src="/images/special.jpg" alt="Description" caption="The story behind this photo..." */>}}
```

## Image Management

### Naming Convention

Use this format for easy organization:

```
YYYY-MM-DD-description.jpg

Examples:
2025-10-04-baja-sunset.jpg
2025-10-04-nextmtn-camp.jpg
2025-10-04-beach-view.jpg
```

### Image Optimization

Before uploading, resize images:

**Recommended sizes:**
- Cover images: 1200x630px (social media optimized)
- Gallery images: 1200px wide
- Inline images: 800px wide

**Tools:**
- **macOS:** Preview (Tools → Adjust Size)
- **iOS:** Shortcuts app (create resize workflow)
- **Online:** [Squoosh.app](https://squoosh.app/)

### Folder Structure

```
static/images/
├── 2025/
│   ├── 10/
│   │   ├── 2025-10-04-post1-cover.jpg
│   │   ├── 2025-10-04-post1-1.jpg
│   │   └── 2025-10-04-post1-2.jpg
│   └── 11/
└── covers/
    └── default-cover.jpg
```

## Content Calendar Ideas

### Regular Features

**Weekly:**
- "Week in Review" - Summary of the week's travels
- "Photo Friday" - Best photos from the week

**Monthly:**
- "2027 Prep Update" - Progress on motorcycle journey
- "Lessons Learned" - What we discovered this month
- "Gear Review" - Equipment we're using

**Occasional:**
- Route guides
- Campsite reviews
- Maintenance tips
- Budget updates
- Q&A posts

## SEO Best Practices

### Every Post Should Have:

1. **Descriptive title** (50-60 characters)
2. **Meta description** (150-160 characters)
3. **Alt text** for all images
4. **Internal links** to related posts
5. **Tags** (3-5 relevant tags)
6. **Category** (1 primary category)

### Example Front Matter:

```yaml
---
title: "Exploring Baja's Hidden Beaches: A Week in Paradise"
date: 2025-10-04
draft: false
tags: ["baja-mexico", "beaches", "camping", "nextmtn"]
categories: ["Travel Log"]
description: "Discovering secluded beaches along Baja's Pacific coast in our F-550 RV. Tips for finding free camping spots and avoiding crowds."
cover:
    image: "/images/2025-10-04-baja-beach.jpg"
    alt: "NextMtn RV parked on secluded Baja beach at sunset"
    caption: "Our camp spot for the week"
---
```

## Batch Content Creation

When you have good internet, batch create:

1. **Write multiple posts** in draft mode
2. **Upload all images** at once
3. **Schedule publishing** by setting future dates
4. **Queue commits** for different days

## Emergency "Quick Post" Workflow

When you're short on time:

```markdown
---
title: "Quick Update from [Location]"
date: 2025-10-04
draft: false
tags: ["quick-update"]
---

Just a quick check-in from [location]!

[One paragraph about what you're doing]

[One photo]

More details coming soon!
```

## Collaboration with Valarie

### Shared Workflow

1. **Both can edit** via GitHub web interface
2. **Use branches** for major changes
3. **Draft folder** for works-in-progress
4. **Review before publishing** (optional)

### Attribution

Add to front matter:

```yaml
author: "Mark"
# or
author: "Valarie"
# or
author: "Mark & Valarie"
```

## Backup Your Content

### Automatic (via Git)

- Every commit is backed up to GitHub
- Netlify keeps deploy history
- Clone to multiple machines

### Manual

Periodically export:

```bash
# Create backup
tar -czf nextmtn-backup-$(date +%Y%m%d).tar.gz content/ static/

# Or just copy content folder
cp -r content/ ~/Backups/nextmtn-content-$(date +%Y%m%d)/
```

## Analytics & Feedback

### Track What Works

- Which posts get the most traffic?
- What tags are most popular?
- What time of day do people read?

### Engage with Readers

- Enable comments (Disqus, Utterances, or Giscus)
- Respond to Instagram comments
- Create "Reader Questions" posts

## Content Ideas Generator

When you're stuck for ideas:

**Travel Log:**
- Daily/weekly summaries
- Specific locations
- Challenges faced
- Unexpected discoveries
- Local culture/food
- Wildlife encounters

**2027 Prep:**
- Motorcycle research
- Training progress
- Gear acquisition
- Route planning
- Language learning
- Fitness preparation
- Budget planning

**Practical:**
- RV maintenance
- Solar power setup
- Water management
- Internet solutions
- Cooking on the road
- Laundry tips

**Reflective:**
- Why we retired early
- Second Mountain philosophy
- Relationship on the road
- Fears and excitement
- Lessons learned

## Publishing Checklist

Before hitting publish:

- [ ] Title is descriptive and engaging
- [ ] Description is filled out
- [ ] Tags are relevant (3-5 tags)
- [ ] Category is assigned
- [ ] Cover image is set
- [ ] All images have alt text
- [ ] Links work
- [ ] Spelling/grammar checked
- [ ] `draft: false` is set
- [ ] Preview looks good locally

## Next Steps

1. ✅ Choose your workflow
2. ✅ Set up mobile apps (if using)
3. ✅ Create your first real post
4. 📝 Establish posting rhythm
5. 📝 Build content backlog
6. 📝 Engage with readers

Happy writing! 🏔️✍️
