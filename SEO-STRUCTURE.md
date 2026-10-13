# Joe Huck Electric — Site Structure & Local SEO Plan

How the site is organized, and why, based on the Local Service SEO playbook
(WWP framework, Steps 1–8) and the Google Business Profile categories and
services checklist.

**Primary keyword:** `electrician yardley`
**Secondary goal:** rank for `electrician near me` across the Yardley map grid,
especially the edges of the heat map.

---

## 1. Architecture

This follows the playbook's diagram: Home → Services hub + Areas we serve →
individual pages. The services hub is split into the three GBP categories.

```
/                                   Homepage — targets "Electrician in Yardley, PA"
├── Services (menu dropdown, no page of its own)
│   ├── /electrician-services/               "Electrician" (primary GBP category) — 8 pages
│   ├── /electrical-installation-services/   "Electrical Installation Services" — 8 pages
│   └── /lighting-contractor-services/       "Lighting Contractor Services" — 6 pages
├── /service-areas/                 Areas hub, grouped by region; 12 town pages
│   ├── Near Yardley (10):  Newtown, Washington Crossing, New Hope, Langhorne, Levittown,
│   │                       Fairless Hills, Morrisville, Bristol, Bensalem, Feasterville
│   └── Central Bucks (2):  Warminster, Doylestown
├── /about/
└── /contact/                       Use as the GBP booking link (Step 3.iv)
```

**41 indexable pages** (the playbook benchmark is 30+). The three category
pages are the playbook's "services hub"; a central Services page above them
would only repeat them, so the menu's Services item is a dropdown instead. Every page is listed,
with its H1, title tag and word count, in [`PAGES.md`](PAGES.md).

### Why 41 pages, not 81

The first version had a page for every one of the 65 GBP services and all 20
GBP towns. Many of those services are rarely searched (doorbells, attic fans,
ballast replacement), and their pages had to be padded to reach 500 words.
Thin, near-duplicate pages can drag down the strong ones, so each low-volume
service is now a short section on the page it belongs with, and the towns
far from Yardley are listed on the Service Areas page without a page of their
own. Every GBP service still maps to a page in `gbp-services.csv`.

### Category names

The three hubs use the GBP category names exactly: **Electrician**, **Electrical
Installation Services** and **Lighting Contractor Services**. "Electrician" is
also the homepage's keyword, so its hub's headline reads "Electrician Services in
Yardley, PA" rather than "Electrician in Yardley, PA". Otherwise the two pages
would compete for the same search.

### Why the homepage is the Yardley page

Yardley is the target city, so the homepage carries the primary keyword in its
title and H1. A separate "Electrician in Yardley" page would compete with the
homepage for the same search, so there isn't one.

---

## 2. Service pages: 22 strong pages, every GBP service covered

Each page covers one main service plus closely related GBP services as their
own sections. The full mapping (folded service → page) is `FOLDED_SERVICES` in
`content/config.py`; old links to folded services resolve to the new page.

| Page | Also covers (GBP services) |
|---|---|
| Electrical Panel Upgrade | Circuit breaker replacement, AFCI breaker installation |
| Home Rewiring | Home electrical upgrades, Ground wire installation & repair |
| Electrical Inspections & Maintenance | Electrical inspections, Electrical code corrections, Smoke detector installation |
| Dedicated Circuit Installation | Appliance wiring, Kitchen electrical upgrade |
| Switch & Outlet Installation | Electrical outlet installation, Switch & outlet relocation, Dimming switch installation, Two-way switching wiring |
| GFCI Outlet Installation | Outdoor outlet installation |
| Ceiling Fan Installation | Attic fan installation, Bathroom fixture wiring |
| Hot Tub Electrical Hookup | Pool electrical wiring |
| Basement Wiring | Electrical wiring installation, New construction electrical |
| Shed, Garage & Barn Wiring | Barn wiring, Garage lighting installation |
| Light Fixture Installation | Ceiling light, Chandelier, Pendant, Wall sconce, Track lighting |
| Under-Cabinet Lighting | LED strip lighting, Accent & cove lighting |
| Security & Flood Lighting | Motion sensor lighting |
| Lighting Repair | Ballast and bulb replacement, Lighting retrofits, LED lighting installation |
| Electrical Installation Services page | Doorbell installation, Smart home wiring, Low voltage wiring |
| Lighting Contractor Services page | Lighting installation, Smart lighting installation |

The other pages (Repair & Troubleshooting, Fuse Box, Subpanel, Surge
Protection, Aluminum Wiring, EV Charger, Recessed, Landscape) cover one service
each.

### What every service page has (WWP steps)

A dark "why us" band sits under every hero: Ryan and Abie's faces ("You'll know who's coming"), free diagnosis and a written quote, and 40+ years plus Nextdoor Favorite. Pages with a matching job photo open the article with it, and every page ends with the four-step "What happens when you call" strip.


| WWP mental step | How the page answers it |
|---|---|
| "They can do the service I need" | H1 = *service + Yardley, PA*; intro that restates the problem |
| Problem-aware, urgent, on mobile | "Signs you need…" checklist near the top; sticky call bar on phones |
| "I trust this company" | Licensed & insured, 40+ years, Nextdoor Favorite, written estimates |
| "I know how to contact them and the trade-off" | Phone in header, hero, sidebar and footer; free-estimate form with the service pre-filled |
| Cost worries | "What affects the cost" section (no made-up prices) |

Each page is 500–700 words (the build checks this) and ends with 2–4 FAQs,
marked up with FAQ schema.

---

## 3. Area pages: the 12 towns that can actually rank

| GBP service area | Page |
|---|---|
| Yardley | Homepage |
| Bucks County | Service Areas hub + schema `areaServed` |
| Newtown, Washington Crossing, New Hope, Langhorne, Levittown, Fairless Hills, Morrisville, Bristol, Bensalem, Feasterville | Near Yardley pages |
| Warminster, Doylestown | Central Bucks pages (large markets worth an organic page) |
| Lower Makefield, Southampton, Richboro, Warrington, Chalfont, Perkasie, Sellersville, Quakertown | Listed on the Service Areas page and the homepage, no page of their own |

Lower Makefield surrounds Yardley, so the homepage already covers it. The
others are far enough from Yardley that a page is unlikely to help in the map
results; they can get pages later if those searches turn out to matter.

Each page has 500–700 words of **unique** local content: the town's real
housing stock, real landmarks and the electrical problems that come with them,
such as the Levitt homes built on slabs. That's Step 6's "referencing real
local landmarks" instead of swapping town names into a template.

### What these pages will and won't do for the heat map

- **The heat-map corners are the lower-Bucks towns:** Newtown, Washington
  Crossing, Langhorne, Levittown, Bristol, Bensalem, Morrisville and Feasterville.
  Pages for these support the map pack where Yardley's proximity already gives
  the profile a chance.
- **Doylestown and Warminster are 15 to 20 miles out.** Google's map results
  lean heavily on distance, so these pages mostly help *organic* results
  ("electrician Doylestown") rather than the map pack.
- **East of Yardley is New Jersey.** The east edge of any Yardley heat map
  falls across the river (Ewing, West Trenton, Titusville). That only matters
  if Joe is licensed in New Jersey.

## 4. Interlinking (Step 7), enforced by the build

- Service pages link to **2–4 area pages** within the text.
- Area pages link to **3–6 service pages** within the text.
- Homepage links to all 3 category hubs, its featured services and all 12 area pages; the hubs link every service.
- Every area page receives at least 2 contextual links from service pages (most get 4–7), spread by what's typical in each town (historic rewiring in Doylestown, aluminum wiring in Bensalem).
- No more than **10 links** in the content of any service or area page; the sidebar skips any service already linked in the body.
- Anchor text is written as a person would say it, and varies from page to page.
- Footer has only NAP, the 3 hubs and company pages. There's no link dump.

`python3 build.py` prints a warning if any page breaks these rules. It currently passes with zero warnings.

---

## 5. On-page basics (Step 5)

| Playbook rule | Homepage | Service, area & hub pages |
|---|---|---|
| **Title:** primary keyword + city \| variation + city | "Electrician in Yardley, PA \| Licensed Electricians in Bucks County" | Same pattern, e.g. "Electrical Panel Upgrade in Yardley, PA \| 200 Amp Upgrades in Bucks County" |
| **H1 = title's main keyword** | "Expert Electrician in Yardley, PA. Not Your Neighborhood Handyman." contains the exact keyword; the wording is the client's | Identical to the title's first half on all 78 pages (the build checks it) |
| **H2s:** prominent services, each with a blurb and a natural-anchor link | "Popular Electrical Services in Yardley": 6 services, each its own H2 with a blurb and varied link text, plus an H2 card for each GBP category | Section H2s per topic (signs, process, cost, local work, FAQ) |
| **Footer:** NAP + embedded map on the homepage | NAP + Google Map embed | NAP on every page |
| **Schema** | `Electrician` LocalBusiness + `WebSite` + `FAQPage` | `Electrician` + `Service`/`OfferCatalog` + `BreadcrumbList` + `FAQPage` |
| **Word count** | ~1,000+ | 500–700 (the build warns outside this) |

Titles run up to ~80 characters so the second half can carry a location
variation. Google displays roughly the first 60, and the keyword and Yardley
always come first.

Also in place: `sitemap.xml`, `robots.txt`, canonical URLs, and 301 redirects
from the old site's URLs (`public/_redirects`).

## 6. GBP deliverable

[`gbp-services.csv`](gbp-services.csv) has one row per checklist service:
the GBP category, the service name, a description under 300 characters, and the
landing page URL. Paste the descriptions into the Business Profile (Step 4.iv).

---

## 7. Before launch

**Confirm with Joe**
- [ ] NAP matches the Business Profile character for character (`content/config.py`)
- [ ] Opening hours (the WWP "they can serve me now" step), plus emergency service if offered. Hours are left blank until confirmed.
- [ ] Every service on the list is one he actually does (Step 4.iii), especially pools, barns, low-voltage/network and commercial work
- [ ] "Master electrician" and "Tesla-certified installer" wording
- [ ] Whether he's licensed in New Jersey
- [ ] Whether the Business Profile shows the street address or is a service-area business. If the address is hidden on GBP, remove the street line and the map pin from the site as well.

**Assets**
- [ ] Official logo file (the site uses a recreated wordmark)
- [x] Real job photos: 16 service pages, the 3 category pages, the Services page and the homepage now show real Joe Huck job photos (`content/photos.py`). Pages with no matching photo don't get a stand-in. Still useful: photos of EV chargers, generators/surge protectors, landscape lighting, ceiling fans, and the van.
- [ ] Map embed code from the Business Profile (Share → Embed), for an exact pin

**Technical**
- [ ] Connect the estimate form to a form handler or CRM (see the TODO in `site/assets/site.js`)
- [ ] Choose a host that supports the `_redirects` file (Netlify or Cloudflare Pages), or recreate the redirects on the chosen host
- [ ] Submit `sitemap.xml` in Google Search Console
- [ ] Run a baseline heat map for "electrician yardley" before launch (Step 1.iii)

**Research**
- [ ] The market research and TPA documents weren't received. Once they arrive, check the keyword choices, area list and competitor-driven services against them.
