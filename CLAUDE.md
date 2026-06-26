# Nexara Energy Solutions — Website 2.0

## Project Overview

This repo is the Next.js + Tailwind CSS replacement for Nexara's Squarespace website, built and hosted via Claude Code / Vercel.

**Two-phase approach:**
- **Phase 1 (MVP — by June 27, 2026):** Build the HOW section (Integrated Delivery Model) as a standalone Next.js component, bundled and embedded as a custom code block in the live Squarespace site.
- **Phase 2 (post-MVP):** Full site migration off Squarespace. Refined aesthetics, additional pages (Services), and a headless CMS blog.

**Tech stack:**
- Framework: Next.js (App Router)
- Styling: Tailwind CSS
- Hosting: Vercel (TBC)
- Future: Headless CMS (TBD) for blog

**Design tokens & brand system:** See `Brand-guidelines.md`.

---

## Client & Enterprise Background

**Company:** Nexara Energy Solutions, LLC
**Address:** 3511 Mallard Pass Ln., Katy, TX 77494
**Website:** nexaraenergy.net (domain on GoDaddy)
**Email:** info@nexaraenergy.net
**Phone:** +1.713.295.1935

**Primary contact:** Juan Pablo Torrealba
**Key stakeholder:** Franco Ciulla (30+ years energy sector; oil engineer → business strategy consultant; O&G, power, renewables, Latin America / North America / Middle East / Europe experience)

**Alivio role:** Andy Luna — Project Manager / Consultant

---

## Brand Identity & Messaging

### Primary taglines
- **"One interface. Clear coordination."**
- **"Reliable onsite power solutions for critical operations."**

### Core value proposition
Nexara removes complexity by unifying specialized power providers under one coordinated interface — end-to-end, door-to-door integrated delivery from procurement through manufacturing, transportation, installation, and ongoing operations coordination.

### Key messaging pillars (the "Five Pillars of Value")
1. **Built to Adapt** — scalable, technology- and fuel-agnostic, modular, purpose-driven
2. **Decisions, Deployed Without Delay** — coordinated sourcing, responsive field deployment, logistics alignment
3. **Field-Earned Experience** — operational familiarity, hands-on execution, specialized technical depth
4. **One Interface. Clear Alignment** — simplified communication, coordinated vendors, reduced execution friction, clear accountability
5. **Reliable Today. Scalable for What's Next** — proven equipment, continuous-duty, modular expansion

### Tone of voice
Technically credible, operationally direct, conversion-oriented. Appeals to both executives (trust, reliability, ROI) and engineers (technical depth, specifications, field experience). Avoid marketing fluff — use precise language and real figures.

### Key buzzwords
reliability · on-site solution · integration · coordinated execution · mission-critical · scalable · field-proven

---

## Solutions Portfolio

Presented in order from near-term / simpler → longer-term / complex:

| # | Solution Family | Near-term? | Scale |
|---|---|---|---|
| 1 | **Onsite Power Generation** | ✓ Priority | 25 kVA → multi-MW |
| 2 | **Power Houses** (containerized, SCADA, MV distribution) | Medium-term | Block-scale |
| 3 | **Microgrids & Hybrid Solutions** (BESS, renewables, load mgmt) | Longer-term | Neighborhood-scale |
| 4 | **Custom Integrated Solutions** (site-specific engineering) | Ongoing | Any scale |

**Short-term focus details (Onsite Power Generation):**
- Natural gas, diesel, LPG, dual-fuel gensets
- Mobile, skid-mounted, containerized configs
- Prime, standby, continuous-duty
- Synchronization, paralleling, telemetry
- Sound-attenuated and weatherproof enclosures
- Capacity: ~25 kVA to 570+ kVA (mobile); ~175 kW to 1.6+ MW (industrial); multi-MW (multi-unit)

---

## Target Audience

| Profile | Who | What they care about |
|---|---|---|
| **Decision-makers** | Executives, ops leaders evaluating providers | Trust, reliability, clear accountability, cost certainty |
| **Technical evaluators** | Engineers validating feasibility & fit | Specs, capacity ranges, field experience, integration depth |

**Primary industries:** Oil & Gas (first priority) → Mining → Industrial Operations → Remote Infrastructure

**Typical applications:** Drilling & production, midstream facilities, mining sites, remote camps, backup & prime power, field development support

---

## Market & Localization

- **Initial market:** Venezuela (do NOT reference explicitly — keep positioning market-agnostic to allow global expansion)
- **Core problem addressed:** Unreliable grid infrastructure, even where electrical infrastructure exists; critical operations need onsite power
- **U.S. proof points:** 2,500+ installed gensets — Permian (2,000+), Eagle Ford (~250), Haynesville (~50), Niobrara (~50), Bakken (~25), Other (~150)
- **Bilingual:** English default; full Spanish toggle (all content) — EN/ES

---

## Home Page Structure (v1)

```
1. Hero            — Positioning + primary taglines + CTA
2. HOW             — Integrated Delivery Model (4 delivery pillars)
3. Solutions       — 4 solution families + capability matrix
4. WHY Nexara      — 5 Pillars of Value
5. Proof Points    — U.S. O&G experience / installed genset stats
6. Contact CTA     — Inquiry prompt → Contact page
```

**Contact page:** Inquiry form + confirmation flow

---

## Design References

- `references/hero-animation.html` — Squarespace hero stack animation. 4 layered PNGs revealed in sequence via `clip-path` with `cubic-bezier(0.77, 0, 0.175, 1)`. Pattern: `revealRTL` (right-to-left wipe) staggered at 0s / 0.49s / 1.46s; `revealCenter` (expand from center) at 0.98s. Reproduce this timing + easing when building the Next.js hero component.

---

## Key Constraints

- No supplier or client logos in v1 (kept generic for flexibility)
- No explicit country/region references (market-agnostic)
- Generic/stock imagery in v1 (no real project photos yet)
- All content must work bilingual (EN/ES)
