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
├── /services/                      Services hub (all 53 service pages, grouped)
│   ├── /electrician-services/               "Electrician" (primary GBP category) — 16 pages
│   ├── /electrical-installation-services/   "Electrical Installation Services" — 21 pages
│   └── /lighting-contractor-services/       "Lighting Contractor Services" — 16 pages
│                                            (also the page for "Lighting installation")
├── /service-areas/                 Areas hub, grouped by region
│   ├── Near Yardley (12):  Lower Makefield, Newtown, Washington Crossing, New Hope,
│   │                       Langhorne, Levittown, Fairless Hills, Morrisville, Bristol,
│   │                       Bensalem, Feasterville-Trevose, Southampton
│   ├── Central Bucks (5):  Richboro, Warminster, Warrington, Doylestown, Chalfont
│   └── Upper Bucks (3):    Perkasie, Sellersville, Quakertown
├── /about/
└── /contact/                       Use as the GBP booking link (Step 3.iv)
```

**81 indexable pages** (the playbook benchmark is 30+). Every page is listed,
with its H1, title tag and word count, in [`PAGES.md`](PAGES.md).

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

## 2. Service pages: one per GBP service, without duplicates

Every service on the checklist has a landing page. Where two checklist names
describe the same job, one page covers both, and both names appear on it.
That follows Step 4 ("one clear version of each service, no duplicates"). It
also avoids near-identical pages competing with each other, and avoids the thin,
AI-sounding pages you wanted to stay away from.

| One page | Covers these checklist services | Why combined |
|---|---|---|
| Fuse Box Replacement | Fuse box replacement, Electrical fuse changing | Same equipment and customer |
| Electrical Repair & Troubleshooting | General electrical repair, Electrical troubleshooting | Same job: find it, fix it |
| Switch & Outlet Installation | Switch & Outlet installation, Electrical switch replacement | Install and replace are one visit |
| LED Lighting Installation & Retrofits | LED lighting installation, Lighting retrofits | A retrofit *is* an LED conversion |
| Landscape & Low-Voltage Lighting | Landscape lighting installation (listed twice), Low voltage lighting installation | Duplicate on the checklist; low-voltage lighting is mostly landscape |
| Security & Flood Light Installation | Security lighting installation, Flood light installation | Floodlights are the security light |
| Accent & Cove Lighting | Accent lighting installation, Cove lighting installation | Cove is a type of accent lighting |
| Lighting Repair | Lighting repair, Ballast and bulb replacement | Same service call |
| Lighting Contractor Services hub | Lighting installation | It's the category's umbrella term |

**Moved:** "Ground wire installation & Repair" was listed under Lighting. It sits
under Electrician, where it belongs. Consider moving it in GBP too.

Any combined page can be split later by adding a block to the content file.

### What every service page has (WWP steps)

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

## 3. Area pages: one per GBP service area

There's an area page for every town in the Business Profile's service area
list, except Yardley (that's the homepage) and Bucks County (the whole region).
Lower Makefield and Fairless Hills also have pages. They aren't in the GBP list,
but they sit right next to Yardley, and GBP only allows 20 service areas.

| GBP service area | Page |
|---|---|
| Yardley | Homepage |
| Bucks County | Service Areas hub + schema `areaServed` |
| Langhorne, Levittown, Bristol, Newtown, New Hope, Morrisville, Washington Crossing, Bensalem, Southampton (Upper Southampton), Feasterville (Feasterville-Trevose) | Near Yardley pages |
| Richboro, Warminster Township, Warrington, Doylestown, Chalfont | Central Bucks pages |
| Perkasie, Sellersville, Quakertown | Upper Bucks pages |

Each page has 500–700 words of **unique** local content: the town's real
housing stock, real landmarks and the electrical problems that come with them.
One example is the Levitt homes built on slabs. Another is Perkasie and
Quakertown running their own electric utilities, which changes how service
upgrades get scheduled. That's Step 6's "referencing real local landmarks"
instead of swapping town names into a template.

### What these pages will and won't do for the heat map

- **The heat-map corners are the lower-Bucks towns:** Newtown, Washington
  Crossing, Langhorne, Levittown, Bristol, Bensalem, Morrisville and Feasterville.
  Pages for these support the map pack where Yardley's proximity already gives
  the profile a chance.
- **The central and upper Bucks towns are 15 to 35 miles out.** Google's map
  results lean heavily on distance, so these pages mostly help *organic* results
  ("electrician Doylestown", "electrician Quakertown") rather than the map
  pack. They're still worth having, since those searches convert.
- **East of Yardley is New Jersey.** The east edge of any Yardley heat map
  falls across the river (Ewing, West Trenton, Titusville). That only matters
  if Joe is licensed in New Jersey.

## 4. Interlinking (Step 7), enforced by the build

- Service pages link to **2–4 area pages** within the text.
- Area pages link to **3–6 service pages** within the text.
- Homepage links to all 3 category hubs, 12 featured services and all 20 area pages; the hubs link every service.
- Every area page receives at least 4 contextual links from service pages, spread by what's typical in each town (historic rewiring in Doylestown, aluminum wiring in Bensalem, barns up north).
- No more than **10 links** in the content of any service or area page; the sidebar skips any service already linked in the body.
- Anchor text is written as a person would say it, and varies from page to page.
- Footer has only NAP, the 3 hubs and company pages. There's no link dump.

`python3 build.py` prints a warning if any page breaks these rules. It currently passes with zero warnings.

---

## 5. On-page basics (Step 5)

- **Title tags:** *Service + Yardley, PA | keyword variation* (≤ 70 characters). Homepage: "Electrician in Yardley, PA | Licensed Electricians in Bucks County".
- **H1:** one per page, containing the primary keyword + city.
- **NAP:** in the footer of every page, and on the contact page. Must match GBP exactly.
- **Map:** embedded in the homepage footer and on the contact page.
- **Schema (every page):** `Electrician` LocalBusiness with address, phone, areaServed and sameAs. Service pages add `Service`, `BreadcrumbList` and `FAQPage`; hubs add `OfferCatalog`.
- **Word counts:** homepage ~1,000; service and area pages 500–700.
- **Technical:** `sitemap.xml`, `robots.txt`, canonical URLs, and 301 redirects from the old site's URLs (`public/_redirects`).

---

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
- [ ] Real job photos for each category, plus the van and crew. The WWP step "images align with the service" is the biggest gap right now. (One photo is in: the panel photo in the homepage estimate card, also used for og:image and schema.)
- [ ] Map embed code from the Business Profile (Share → Embed), for an exact pin

**Technical**
- [ ] Connect the estimate form to a form handler or CRM (see the TODO in `site/assets/site.js`)
- [ ] Choose a host that supports the `_redirects` file (Netlify or Cloudflare Pages), or recreate the redirects on the chosen host
- [ ] Submit `sitemap.xml` in Google Search Console
- [ ] Run a baseline heat map for "electrician yardley" before launch (Step 1.iii)

**Research**
- [ ] The market research and TPA documents weren't received. Once they arrive, check the keyword choices, area list and competitor-driven services against them.
