# Deployment Guide

## GitHub Setup

### 1. Create GitHub Repository

1. Go to [GitHub](https://github.com/new)
2. Repository name: `nextmountainoverland`
3. Description: "Next Mountain Overland - Travel blog"
4. Choose Public or Private
5. **Don't** initialize with README (we already have one)
6. Click "Create repository"

### 2. Push Your Code

From your project directory:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# First commit
git commit -m "Initial commit - Next Mountain Overland site"

# Add remote (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/nextmountainoverland.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Add Theme as Submodule

```bash
git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
git add .
git commit -m "Add PaperMod theme"
git push
```

## Netlify Deployment

### Option 1: Netlify UI (Recommended for First Time)

1. Go to [Netlify](https://app.netlify.com/)
2. Click "Add new site" → "Import an existing project"
3. Choose "GitHub" and authorize Netlify
4. Select your `nextmountainoverland` repository
5. Configure build settings:
   - **Build command:** `hugo --gc --minify`
   - **Publish directory:** `public`
   - **Branch:** `main`
6. Click "Add environment variable":
   - Key: `HUGO_VERSION`
   - Value: `0.120.0`
7. Click "Deploy site"

### Option 2: Netlify CLI

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login to Netlify
netlify login

# Initialize site
netlify init

# Deploy
netlify deploy --prod
```

### 4. Configure Domain

#### On Netlify:

1. Go to Site settings → Domain management
2. Click "Add custom domain"
3. Enter: `nextmountainoverland.com`
4. Netlify will provide DNS settings

#### On Your Domain Registrar:

Add these DNS records (Netlify will show you the exact values):

```
Type: A
Name: @
Value: 75.2.60.5 (Netlify's IP)

Type: CNAME
Name: www
Value: your-site.netlify.app
```

#### Enable HTTPS:

1. In Netlify: Domain settings → HTTPS
2. Click "Verify DNS configuration"
3. Click "Provision certificate"
4. Wait a few minutes for SSL to activate

## Continuous Deployment

Once set up, every push to GitHub automatically deploys:

```bash
# Make changes
git add .
git commit -m "Add new post about Baja"
git push

# Netlify automatically builds and deploys!
```

## Deploy Previews

Netlify creates preview URLs for:
- Pull requests
- Branch deploys
- Draft posts (if you push with drafts)

## Environment Variables

In Netlify dashboard, add these if needed:

| Variable | Value | Purpose |
|----------|-------|---------|
| `HUGO_VERSION` | `0.120.0` | Hugo version |
| `HUGO_ENV` | `production` | Environment |
| `HUGO_ENABLEGITINFO` | `true` | Git info in posts |

## Build Status Badge

Add to your README.md:

```markdown
[![Netlify Status](https://api.netlify.com/api/v1/badges/YOUR-SITE-ID/deploy-status)](https://app.netlify.com/sites/YOUR-SITE/deploys)
```

## Troubleshooting

### Build Fails

**Check Hugo version:**
- Ensure `HUGO_VERSION` environment variable is set
- Use Hugo Extended version

**Theme not found:**
```bash
git submodule update --init --recursive
git add .
git commit -m "Update theme submodule"
git push
```

### Domain Not Working

1. Verify DNS propagation: `dig nextmountainoverland.com`
2. Wait 24-48 hours for DNS to propagate
3. Check Netlify DNS settings match your registrar

### SSL Certificate Issues

1. Ensure DNS is properly configured
2. Wait for verification (can take up to 24 hours)
3. Try "Renew certificate" in Netlify

## Rollback a Deploy

In Netlify dashboard:
1. Go to Deploys
2. Find the working deploy
3. Click "Publish deploy"

## Local Testing Before Deploy

```bash
# Build exactly as Netlify will
hugo --gc --minify

# Test the built site
cd public
python3 -m http.server 8000
```

Open `http://localhost:8000`

## Post-Deployment Checklist

- [ ] Site loads at your domain
- [ ] HTTPS is working (green padlock)
- [ ] RSS feed works: `https://nextmountainoverland.com/index.xml`
- [ ] Images load correctly
- [ ] Navigation works
- [ ] Mobile responsive
- [ ] Instagram embeds work
- [ ] Search functionality works

## Monitoring

### Netlify Analytics (Optional)

- Go to Site settings → Analytics
- Enable Netlify Analytics ($9/month)
- Privacy-friendly, no cookies needed

### Free Alternatives

- [GoatCounter](https://www.goatcounter.com/) - Open source, privacy-friendly
- [Plausible](https://plausible.io/) - Privacy-focused analytics
- Server logs via Netlify dashboard

## Backup Strategy

Your content is safe because:
1. ✅ Source code in GitHub
2. ✅ Netlify keeps deploy history
3. ✅ Local copy on your machine

**Recommended:** Clone to multiple machines or backup GitHub regularly.

## Next Steps

1. ✅ Deploy to Netlify
2. ✅ Configure domain
3. ✅ Enable HTTPS
4. 📝 Set up analytics (optional)
5. 📝 Create posting workflow
6. 📝 Write your first real post!

---

Need help? Check:
- [Hugo Documentation](https://gohugo.io/documentation/)
- [Netlify Documentation](https://docs.netlify.com/)
- [PaperMod Wiki](https://github.com/adityatelange/hugo-PaperMod/wiki)
