# Nexara Energy Solutions — Website 2.0

## Two-phase approach

### Phase 1 — Squarespace embed (MVP, target: June 27 2026)
A self-contained HTML file that embeds all home-page sections into the live Squarespace site via a custom code block. No build step, no framework.

**File:** [`squarespace/homepage-embed.html`](squarespace/homepage-embed.html)

**Sections included:**
1. HOW — One partner. One interface. (interactive JS tabs)
2. WHAT — Energy solutions for all environments. (service cards)
3. APPLICATION — Tried and tested in the field. (capability matrix)
4. LIFECYCLE — Full life-cycle support. (interactive timeline)
5. VALUES — Our five pillars of value. (value cards)

Hero section is handled separately by Squarespace.

**Setup — before pasting into Squarespace:**
1. Push this repo to GitHub (public or private)
2. Open `squarespace/homepage-embed.html` and find the `NXR_BASE` constant
3. Replace `YOUR_ORG` with your GitHub username/org
4. Paste the full file contents into a Squarespace → Pages → [Page] → Edit → Code Block

---

### Phase 2 — Full Next.js site (post-MVP)
Full migration off Squarespace. Next.js App Router + Tailwind CSS, hosted on Vercel. The scaffold is already in place (`src/`, `public/`, `package.json`).

**Future additions:** additional pages (Services), headless CMS blog, Spanish toggle (EN/ES).

---

## Tech stack
- Phase 1: Vanilla HTML/CSS/JS (zero dependencies)
- Phase 2: Next.js 15 + Tailwind CSS + TypeScript → Vercel

## Brand
See [`brand-identity/Brand-guidelines.md`](brand-identity/Brand-guidelines.md) for colors, typography, and design system.

## Image hosting
Phase 1 images are served via GitHub raw content URLs from this repo:
```
https://raw.githubusercontent.com/YOUR_ORG/nexara-energy-website/main/images/
```
SVG icons and logos live in `components/icons/` and `components/logos/` respectively.
