#!/usr/bin/env python3
"""Build the Joe Huck Electric website.

    python3 build.py                  # production build into public/
    python3 build.py --preview DIR    # file-browsable build (relative links)

Content lives in content/*.txt; business details in content/config.py.
The build also checks every page against the local SEO playbook
(word counts, link counts, title/description length, broken links) and
writes PAGES.md and gbp-services.csv.
"""
import csv
import html
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "content"))
import config as C  # noqa: E402

AREA_PREFIX = "/service-areas/"
HERO_PHOTO = "/assets/img/electrician-panel-yardley.jpg"  # 2:1 crop, used for og:image and schema
HERO_BG = "/assets/img/electrician-panel-yardley-hero.jpg"
ABOUT_PHOTO = "/assets/img/ryan-huck-electrician-ladder.jpg"
TEAM = [
    {"name": "Ryan", "full": "Ryan Huck", "role": "Head Electrician", "img": "/assets/img/ryan-huck-head-electrician.jpg"},
    {"name": "Abie", "full": "Abie", "role": "Assistant Electrician", "img": "/assets/img/abie-assistant-electrician.jpg"},
]


def team_section(p, bg=""):
    cards = "".join(
        f'''<li class="team-card">
          <img src="{p.href(t["img"])}" width="900" height="1350" alt="{esc(t["full"])}, {esc(t["role"].lower())} at {C.NAME}" loading="lazy" decoding="async">
          <span class="team-tag">{esc(t["name"])} | {esc(t["role"])}</span>
        </li>'''
        for t in TEAM
    )
    return f'''
  <section class="block team{bg}" id="team">
    <div class="wrap">
      <div class="team-head">
        <h2>Meet the <em>Local Team</em></h2>
        <p>You deserve a team you know and trust. With us, you always know who you're getting.</p>
      </div>
      <ul class="team-grid">{cards}</ul>
      <p class="team-note">Ryan leads every job as head electrician, with Abie at his side. Together they carry on the work Joe Huck started in Bucks County over 40 years ago.</p>
    </div>
  </section>'''

WARNINGS = []


# ----------------------------------------------------------------------------
# Content parsing
# ----------------------------------------------------------------------------
def parse_blocks(path):
    """Split a content file into {slug: {"meta": {...}, "body": str}}."""
    out, order = {}, []
    text = path.read_text(encoding="utf-8")
    for chunk in re.split(r"^=== ", text, flags=re.M)[1:]:
        head, _, rest = chunk.partition("\n")
        slug = head.strip()
        meta_txt, sep, body = rest.partition("\n---\n")
        if not sep:
            raise SystemExit(f"{path.name}: block '{slug}' is missing the --- separator")
        meta = {}
        for line in meta_txt.strip().splitlines():
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()
        out[slug] = {"slug": slug, "meta": meta, "body": body.strip()}
        order.append(slug)
    return out, order


def split_faq(body):
    main, sep, faq = body.partition("\n## FAQ\n")
    pairs = []
    if sep:
        q = None
        for line in faq.strip().splitlines():
            line = line.strip()
            if line.startswith("Q:"):
                q = line[2:].strip()
            elif line.startswith("A:") and q:
                pairs.append((q, line[2:].strip()))
                q = None
    return main.strip(), pairs


# ----------------------------------------------------------------------------
# Site registry
# ----------------------------------------------------------------------------
class Site:
    def __init__(self, preview=False):
        self.preview = preview
        self.services, svc_order = {}, []
        for f in ("services-general.txt", "services-installation.txt", "services-lighting.txt"):
            blocks, order = parse_blocks(ROOT / "content" / f)
            self.services.update(blocks)
            svc_order += order
        self.svc_order = svc_order
        self.areas, self.area_order = parse_blocks(ROOT / "content" / "areas.txt")
        self.pages, _ = parse_blocks(ROOT / "content" / "pages.txt")
        for s in self.services.values():
            cat = C.CATEGORIES[s["meta"]["cat"]]
            s["path"] = f"/{cat['slug']}/{s['slug']}/"
        for a in self.areas.values():
            a["path"] = f"{AREA_PREFIX}{a['slug']}-pa/"

    def resolve(self, ref):
        """@slug → site path."""
        if ref in self.services:
            return self.services[ref]["path"]
        if ref in self.areas:
            return self.areas[ref]["path"]
        for cat in C.CATEGORIES.values():
            if ref == cat["slug"]:
                return f"/{ref}/"
        fixed = {"home": "/", "contact": "/contact/", "about": "/about/", "service-areas": AREA_PREFIX, "services": "/services/"}
        if ref in fixed:
            return fixed[ref]
        raise SystemExit(f"Unknown link target @{ref}")

    def kind(self, ref):
        if ref in self.services:
            return "service"
        if ref in self.areas:
            return "area"
        return "page"

    def cat_services(self, key):
        return [self.services[s] for s in self.svc_order if self.services[s]["meta"]["cat"] == key]


# ----------------------------------------------------------------------------
# Rendering helpers
# ----------------------------------------------------------------------------
esc = html.escape


class Page:
    def __init__(self, site, path):
        self.site, self.path = site, path
        self.links = []  # in-content links: (kind, ref)

    def href(self, target):
        """Link from this page to a site path (or #anchor / absolute URL)."""
        if target.startswith(("http", "#", "tel:", "mailto:")):
            return target
        if not self.site.preview:
            return target
        depth = self.path.strip("/").count("/") + (1 if self.path.strip("/") else 0)
        rel = "../" * depth + target.lstrip("/")
        if rel == "" or rel.endswith("/"):
            rel += "index.html"
        return rel

    def link(self, ref, text, track=True, cls=None):
        path = self.site.resolve(ref)
        if track:
            self.links.append((self.site.kind(ref), ref))
        c = f' class="{cls}"' if cls else ""
        return f'<a{c} href="{self.href(path)}">{text}</a>'

    def inline(self, s):
        s = esc(s, quote=False)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"\[([^\]]+)\]\(@([a-z0-9-]+)\)", lambda m: self.link(m.group(2), m.group(1)), s)
        s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
        return s

    def md(self, text):
        out = []
        # fenced ":::signs" boxes
        parts = re.split(r"^:::(\w*)\s*$", text, flags=re.M)
        box = None
        for i, part in enumerate(parts):
            if i % 2 == 1:
                box = part or None
                if box:
                    out.append(f'<div class="{box}">')
                else:
                    out.append("</div>")
                continue
            for block in re.split(r"\n\s*\n", part.strip()):
                block = block.strip()
                if not block:
                    continue
                lines = block.splitlines()
                if block.startswith("### "):
                    out.append(f"<h3>{self.inline(block[4:])}</h3>")
                elif block.startswith("## "):
                    out.append(f"<h2>{self.inline(lines[0][3:])}</h2>")
                    rest = "\n".join(lines[1:]).strip()
                    if rest:
                        out.append(self.md(rest))
                elif all(l.startswith("- ") for l in lines):
                    out.append("<ul>" + "".join(f"<li><span>{self.inline(l[2:])}</span></li>" for l in lines) + "</ul>")
                else:
                    out.append(f"<p>{self.inline(' '.join(l.strip() for l in lines))}</p>")
        return "\n".join(out)


def words(html_text):
    return len(re.findall(r"[A-Za-z0-9’'&-]+", re.sub(r"<[^>]+>", " ", html_text)))


ICON_CALL = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 2h3l1.5 4-2 1.3a10 10 0 0 0 5.2 5.2l1.3-2 4 1.5v3a2 2 0 0 1-2 2A15 15 0 0 1 3 4a2 2 0 0 1 2-2z"/></svg>'
ICON_ARROW = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 10h12M11 5l5 5-5 5"/></svg>'
LOGO = '<svg class="logo-mark" viewBox="0 0 34 40" fill="currentColor" aria-hidden="true"><path d="M2 38c0-7 3-9 7-9h4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><rect x="12" y="20" width="16" height="16" rx="3"/><rect x="28" y="23" width="6" height="3" rx="1"/><rect x="28" y="30" width="6" height="3" rx="1"/></svg><span class="logo-type"><strong>Joe Huck</strong><span>Electric</span></span>'


def hours_line():
    return "; ".join(h[3] for h in C.HOURS) if C.HOURS else "Call or text to schedule"


# ----------------------------------------------------------------------------
# Schema
# ----------------------------------------------------------------------------
def business_schema(site):
    b = {
        "@type": "Electrician",
        "@id": C.DOMAIN + "/#business",
        "name": C.NAME,
        "legalName": C.LEGAL_NAME,
        "url": C.DOMAIN + "/",
        "telephone": "+1-215-906-4634",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": C.STREET,
            "addressLocality": C.CITY,
            "addressRegion": C.REGION,
            "postalCode": C.POSTAL,
            "addressCountry": "US",
        },
        "areaServed": [{"@type": "City", "name": "Yardley, PA"}]
        + [{"@type": "City", "name": a["meta"]["town"] + ", PA"} for a in site.areas.values()]
        + [{"@type": "AdministrativeArea", "name": "Bucks County, PA"}],
        "sameAs": C.SAME_AS,
        "image": C.DOMAIN + HERO_PHOTO,
        "founder": {"@type": "Person", "name": "Joe Huck"},
        "employee": [{"@type": "Person", "name": t["full"], "jobTitle": t["role"], "image": C.DOMAIN + t["img"]} for t in TEAM],
    }
    if C.HOURS:
        days = {"Mo": "Monday", "Tu": "Tuesday", "We": "Wednesday", "Th": "Thursday", "Fr": "Friday", "Sa": "Saturday", "Su": "Sunday"}
        specs = []
        for rng, opens, closes, _ in C.HOURS:
            a, _, z = rng.partition("-")
            keys = list(days)
            sel = keys[keys.index(a): keys.index(z or a) + 1]
            specs.append({"@type": "OpeningHoursSpecification", "dayOfWeek": [days[k] for k in sel], "opens": opens, "closes": closes})
        b["openingHoursSpecification"] = specs
    return b


def breadcrumb_schema(crumbs):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": C.DOMAIN + path}
            for i, (name, path) in enumerate(crumbs)
        ],
    }


def faq_schema(pairs):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs
        ],
    }


# ----------------------------------------------------------------------------
# Shared page parts
# ----------------------------------------------------------------------------
NAV = [
    ("Services", "/services/", "services"),
    ("Service Areas", AREA_PREFIX, "areas"),
    ("About", "/about/", "about"),
    ("Contact", "/contact/", "contact"),
]


def layout(p, *, title, desc, main, schema, active=None, home=False):
    if len(title) > 70:
        WARNINGS.append(f"{p.path}: title is {len(title)} chars (aim for ≤ 70)")
    if not 70 <= len(desc) <= 160:
        WARNINGS.append(f"{p.path}: meta description is {len(desc)} chars (aim for 70–160)")
    cur = ' aria-current="page"'
    nav = "".join(
        f'<li><a href="{p.href(url)}"{cur if key == active else ""}>{label}</a></li>'
        for label, url, key in NAV
    )
    ld = json.dumps({"@context": "https://schema.org", "@graph": schema}, ensure_ascii=False, indent=1)
    canonical = C.DOMAIN + p.path
    map_band = ""
    if home:
        map_band = f'''<div class="map-band"><iframe src="{C.MAP_EMBED}" title="Map: {C.NAME}, {C.STREET}, {C.CITY}, {C.REGION}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>'''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{C.NAME}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{C.DOMAIN + HERO_PHOTO}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,400;0,500;0,600;0,700;0,800;1,500&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{p.href('/assets/site.css')}">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<div class="topbar">
  <div class="wrap">
    <span><span class="dot" aria-hidden="true"></span>Serving Yardley &amp; Bucks County homes and businesses</span>
    <span class="hide-sm">Licensed &amp; insured · <b>Master electrician</b> · Yardley, PA</span>
  </div>
</div>

<header class="site">
  <div class="wrap">
    <a class="logo" href="{p.href('/')}" aria-label="{C.NAME} home">
      <!-- Recreated wordmark. Swap in the official logo file when available. -->
      {LOGO}
    </a>
    <nav class="primary" id="nav" aria-label="Main"><ul>{nav}</ul></nav>
    <a class="header-call" href="tel:{C.PHONE_E164}"><small>Call or text</small><span>{C.PHONE_DISPLAY}</span></a>
    <a class="btn btn-bronze hide-md" href="#estimate" style="min-height:44px;white-space:nowrap">Free estimate</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" aria-label="Open menu">
      <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 5h16M2 10h16M2 15h16"/></svg>
    </button>
  </div>
</header>

<main id="main">
{main}
  <section class="cta">
    <div class="wrap">
      <h2>Need an Electrician You Can Trust?</h2>
      <div>
        <small>Call or text</small>
        <a class="phone-big" href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a>
        <a class="btn" href="#estimate">Or request an estimate online</a>
      </div>
    </div>
  </section>
</main>

<footer>
  {map_band}
  <div class="wrap">
    <div>
      <a class="logo" href="{p.href('/')}" aria-label="{C.NAME} home">{LOGO}</a>
      <p class="about">Licensed, insured electricians serving Yardley and the Greater Bucks County area for over 40 years.</p>
    </div>
    <div>
      <h4>Services</h4>
      <ul>
        <li><a href="{p.href('/' + C.CATEGORIES['g']['slug'] + '/')}">{C.CATEGORIES['g']['name']}</a></li>
        <li><a href="{p.href('/' + C.CATEGORIES['i']['slug'] + '/')}">{C.CATEGORIES['i']['name']}</a></li>
        <li><a href="{p.href('/' + C.CATEGORIES['l']['slug'] + '/')}">{C.CATEGORIES['l']['name']}</a></li>
      </ul>
    </div>
    <div>
      <h4>Company</h4>
      <ul>
        <li><a href="{p.href('/about/')}">About</a></li>
        <li><a href="{p.href(AREA_PREFIX)}">Service Areas</a></li>
        <li><a href="{p.href('/contact/')}">Contact</a></li>
      </ul>
    </div>
    <div>
      <h4>Contact</h4>
      <address class="nap-foot" style="font-style:normal">
        <b style="color:var(--white);font-weight:600">{C.NAME}</b><br>
        {C.STREET}<br>{C.CITY}, {C.REGION} {C.POSTAL}<br>
        <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a><br>
        <span>{hours_line()}</span>
      </address>
    </div>
  </div>
  <div class="wrap legal">
    <span>© <span id="yr">2026</span> {C.LEGAL_NAME} · {C.CITY}, {C.REGION}</span>
    <span>Licensed &amp; insured electrical contractor</span>
  </div>
</footer>

<div class="mbar" aria-label="Quick actions">
  <a class="btn btn-ghost" href="tel:{C.PHONE_E164}">{ICON_CALL}Call now</a>
  <a class="btn btn-bronze" href="#estimate">Free estimate</a>
</div>

<datalist id="townlist"></datalist>
<script src="{p.href('/assets/site.js')}" defer></script>
</body>
</html>
'''


def quote_card(cat=None, service=None, photo=False):
    if service:
        picker = f'''<input type="hidden" name="service" value="{esc(service)}">
          <p class="about-svc">About: <b>{esc(service)}</b></p>'''
    else:
        chips = "".join(
            f'<label class="chip"><input type="checkbox" name="svc" value="{v}"{" checked" if k == cat else ""}><span>{lbl}</span></label>'
            for k, v, lbl in [
                ("g", "Electrician services", "Repair / upgrade"),
                ("i", "Electrical installation", "Installation"),
                ("l", "Lighting", "Lighting"),
                ("o", "Other", "Something else"),
            ]
        )
        picker = f'''<fieldset class="field">
            <legend>What do you need?</legend>
            <div class="chips" id="svcChips">{chips}</div>
          </fieldset>'''
    fig = ""
    if photo:
        fig = f'''<figure class="quote-photo">
          <img src="{photo}" width="960" height="480" alt="Ryan Huck of Joe Huck Electric working on a home electrical panel" fetchpriority="high" decoding="async">
        </figure>'''
    return f'''<div class="quote{" has-photo" if photo else ""}" id="estimate">
        {fig}
        <form id="quoteForm" novalidate>
          <h2>Request a Free Estimate</h2>
          <p class="sub">Takes about 30 seconds. We reply within one business day.</p>
          {picker}
          <div class="row2">
            <div class="field"><label for="q-name">Name</label><input id="q-name" name="name" autocomplete="name" required></div>
            <div class="field"><label for="q-phone">Phone</label><input id="q-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
          </div>
          <div class="field"><label for="q-town">Town</label>
            <input id="q-town" name="town" list="townlist" autocomplete="address-level2" placeholder="e.g. Yardley">
          </div>
          <div class="field"><label for="q-note">Details (optional)</label><textarea id="q-note" name="note" placeholder="Tell us what's going on"></textarea></div>
          <p class="err" id="q-err" hidden></p>
          <button class="btn btn-bronze" type="submit">Send my request</button>
          <p class="fine">Prefer to talk? Call <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a></p>
        </form>
        <div class="done" id="quoteDone" hidden aria-live="polite">
          <div class="check"><svg width="26" height="26" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 10.5l4 4 8-9"/></svg></div>
          <h3>Request Sent</h3>
          <p id="doneMsg">We'll call you within one business day.</p>
          <button class="btn btn-ghost" type="button" id="quoteReset" style="color:var(--ink);border-color:var(--line)">Send another request</button>
        </div>
      </div>'''


def page_hero(p, crumbs, eyebrow, h1, lede, cat=None, service=None):
    crumb_html = "".join(
        f'<li><a href="{p.href(path)}">{esc(name)}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{esc(name)}</li>'
        for i, (name, path) in enumerate(crumbs)
    )
    return f'''  <section class="hero page-hero">
    <div class="wrap">
      <div>
        <ol class="crumbs" aria-label="Breadcrumb">{crumb_html}</ol>
        <p class="eyebrow">{esc(eyebrow)}</p>
        <h1>{esc(h1)}</h1>
        <p class="lede">{lede}</p>
        <div class="hero-ctas">
          <a class="btn btn-bronze" href="#estimate">Get a free estimate {ICON_ARROW}</a>
          <a class="btn btn-ghost" href="tel:{C.PHONE_E164}">{ICON_CALL}{C.PHONE_DISPLAY}</a>
        </div>
        <ul class="trust"><li>Licensed &amp; insured</li><li>Only electrical, 40+ years</li><li>Free written estimates</li></ul>
      </div>
      {quote_card(cat, service)}
    </div>
  </section>'''


def faq_section(p, pairs, heading="Questions"):
    if not pairs:
        return ""
    items = "".join(
        f'<details{" open" if i == 0 else ""}><summary>{esc(q)}<span class="pm" aria-hidden="true"></span></summary><p>{p.inline(a)}</p></details>'
        for i, (q, a) in enumerate(pairs)
    )
    return f'''  <section class="block faq">
    <div class="wrap">
      <div class="sec-head"><div><p class="eyebrow">{heading}</p><h2>Good to Know.</h2></div>
        <p>Still have a question? Call <a href="tel:{C.PHONE_E164}" style="color:var(--bronze-deep);font-weight:700">{C.PHONE_DISPLAY}</a>. You'll talk to an electrician, not a call center.</p></div>
      <div class="faq-list">{items}</div>
    </div>
  </section>'''


def call_card(p):
    return f'''<div class="side-card dark">
          <h2>Talk to an Electrician</h2>
          <p>{hours_line()}. Estimates are free and in writing.</p>
          <a class="phone" href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a>
          <a class="btn btn-bronze" href="#estimate">Request an estimate</a>
        </div>'''


def list_card(title, items):
    lis = "".join(f"<li>{a}</li>" for a in items)
    return f'<div class="side-card"><h2>{title}</h2><ul>{lis}</ul></div>'


# ----------------------------------------------------------------------------
# Page builders
# ----------------------------------------------------------------------------
REPORT = []


def check_len(path, wc, lo, hi, label):
    if wc < lo:
        WARNINGS.append(f"{path}: {label} has {wc} words (playbook: {lo}–{hi})")


def build_service(site, s):
    m = s["meta"]
    cat = C.CATEGORIES[m["cat"]]
    p = Page(site, s["path"])
    main_md, faqs = split_faq(s["body"])
    intro, _, rest = main_md.partition("\n\n")
    lede = p.inline(intro)
    prose = p.md(rest)
    inline = {r for _, r in p.links}
    related = [p.link(r, esc(site.services[r]["meta"]["name"]))
               for r in (x.strip() for x in m["related"].split(",")) if r not in inline]
    if not related:  # keep the sidebar useful even when the body already links everything
        extra = [x for x in site.svc_order if site.services[x]["meta"]["cat"] == m["cat"] and x not in inline and x != s["slug"]]
        related += [p.link(x, esc(site.services[x]["meta"]["name"])) for x in extra[:1]]
    hub = p.link(cat["slug"], f"All {cat['name'].lower()}")
    crumbs = [("Home", "/"), ("Services", "/services/"), (cat["name"], f"/{cat['slug']}/"), (m["name"], s["path"])]
    faq_html = faq_section(p, faqs)
    main = page_hero(p, crumbs, cat["name"], m["h1"], lede, service=m["name"]) + f'''
  <section class="article">
    <div class="wrap">
      <article class="prose">
{prose}
      </article>
      <aside class="side">
        {call_card(p)}
        {list_card("Related Services", related + [hub])}
      </aside>
    </div>
  </section>
{faq_html}'''
    schema = [
        business_schema(site),
        {
            "@type": "Service",
            "name": m["name"],
            "serviceType": m["name"],
            "description": m["blurb"],
            "provider": {"@id": C.DOMAIN + "/#business"},
            "areaServed": business_schema(site)["areaServed"],
            "url": C.DOMAIN + s["path"],
        },
        breadcrumb_schema(crumbs),
    ]
    if faqs:
        schema.append(faq_schema(faqs))
    out = layout(p, title=m["title"], desc=m["desc"], main=main, schema=schema, active="services")
    wc = words(lede + prose + faq_html)
    area_links = {r for k, r in p.links if k == "area"}
    if not 2 <= len(area_links) <= 4:
        WARNINGS.append(f"{s['path']}: links to {len(area_links)} area pages (playbook: 2–4)")
    if len(p.links) > 10:
        WARNINGS.append(f"{s['path']}: {len(p.links)} in-content links (playbook: ≤ 10)")
    if len(m["blurb"]) > 300:
        WARNINGS.append(f"{s['path']}: GBP description is {len(m['blurb'])} chars (limit 300)")
    check_len(s["path"], wc, 500, 700, "service page")
    REPORT.append((s["path"], m["h1"], m["title"], wc, len(p.links), m.get("gbp", m["name"])))
    return out


def build_area(site, a):
    m = a["meta"]
    p = Page(site, a["path"])
    main_md, faqs = split_faq(a["body"])
    intro, _, rest = main_md.partition("\n\n")
    lede = p.inline(intro)
    prose = p.md(rest)
    nearby = [p.link(n.strip(), esc(site.areas[n.strip()]["meta"]["town"])) for n in m["nearby"].split(",")]
    crumbs = [("Home", "/"), ("Service Areas", AREA_PREFIX), (m["town"], a["path"])]
    faq_html = faq_section(p, faqs)
    main = page_hero(p, crumbs, f"Serving {m['town']}, PA", m["h1"], lede, cat=None) + f'''
  <section class="article">
    <div class="wrap">
      <article class="prose">
{prose}
      </article>
      <aside class="side">
        {call_card(p)}
        {list_card("Nearby Towns We Serve", nearby)}
      </aside>
    </div>
  </section>
{faq_html}'''
    schema = [business_schema(site), breadcrumb_schema(crumbs)]
    if faqs:
        schema.append(faq_schema(faqs))
    out = layout(p, title=m["title"], desc=m["desc"], main=main, schema=schema, active="areas")
    wc = words(lede + prose + faq_html)
    svc_links = {r for k, r in p.links if k == "service"}
    if not 3 <= len(svc_links) <= 6:
        WARNINGS.append(f"{a['path']}: links to {len(svc_links)} service pages (playbook: 3–6)")
    if len(p.links) > 10:
        WARNINGS.append(f"{a['path']}: {len(p.links)} in-content links (playbook: ≤ 10)")
    check_len(a["path"], wc, 500, 700, "area page")
    REPORT.append((a["path"], m["h1"], m["title"], wc, len(p.links), "—"))
    return out


def build_hub(site, key):
    cat = C.CATEGORIES[key]
    pg = site.pages[cat["slug"]]
    m = pg["meta"]
    path = f"/{cat['slug']}/"
    p = Page(site, path)
    main_md, faqs = split_faq(pg["body"])
    intro, _, rest = main_md.partition("\n\n")
    lede = p.inline(intro)
    cards = "".join(
        f'<li><a href="{p.href(s["path"])}"><b>{esc(s["meta"]["name"])}</b><span>{esc(s["meta"]["blurb"])}</span><em>Learn more →</em></a></li>'
        for s in site.cat_services(key)
    )
    crumbs = [("Home", "/"), ("Services", "/services/"), (cat["name"], path)]
    faq_html = faq_section(p, faqs)
    main = page_hero(p, crumbs, f"{cat['name']} · Yardley, PA", m["h1"], lede, cat=key) + f'''
  <section class="block services">
    <div class="wrap">
      <div class="hub-intro">{p.md(rest)}</div>
      <h2 class="sr" style="position:absolute;left:-9999px">All {esc(cat["name"])}</h2>
      <ul class="svc-grid">{cards}</ul>
    </div>
  </section>
{faq_html}'''
    schema = [business_schema(site), breadcrumb_schema(crumbs), {
        "@type": "OfferCatalog", "name": cat["name"],
        "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["meta"]["name"], "url": C.DOMAIN + s["path"]}} for s in site.cat_services(key)],
    }]
    if faqs:
        schema.append(faq_schema(faqs))
    out = layout(p, title=m["title"], desc=m["desc"], main=main, schema=schema, active="services")
    REPORT.append((path, m["h1"], m["title"], words(lede + main + faq_html), len(site.cat_services(key)), "(category hub)"))
    return out


def build_simple(site, key, path, active=None, extra="", hero_cat=None):
    pg = site.pages[key]
    m = pg["meta"]
    p = Page(site, path)
    main_md, faqs = split_faq(pg["body"])
    intro, _, rest = main_md.partition("\n\n")
    crumbs = [("Home", "/"), (m["crumb"], path)]
    body = f'''
  <section class="article">
    <div class="wrap">
      <article class="prose">
{p.md(rest)}
      </article>
      <aside class="side">{call_card(p)}</aside>
    </div>
  </section>''' if rest else ""
    main = page_hero(p, crumbs, m["eyebrow"], m["h1"], p.inline(intro), cat=hero_cat) + body + extra(p) + faq_section(p, faqs)
    schema = [business_schema(site), breadcrumb_schema(crumbs)]
    out = layout(p, title=m["title"], desc=m["desc"], main=main, schema=schema, active=active)
    REPORT.append((path, m["h1"], m["title"], words(main), len(p.links), "—"))
    return out


REGIONS = [
    ("lower", "Near Yardley", "The towns closest to our Yardley base, along the river and across lower Bucks, where we work every week."),
    ("central", "Central Bucks", "Richboro, Warminster, Warrington, Doylestown and Chalfont. We group appointments here to keep scheduling reliable."),
    ("upper", "Upper Bucks", "Perkasie, Sellersville and Quakertown. Call early, and we'll schedule your job with our other upper Bucks appointments."),
]


def areas_index_extra(site):
    def f(p):
        total = len(site.areas)
        jumps = " · ".join(
            f'<a href="#{key}">{esc(title)} ({sum(1 for a in site.areas.values() if a["meta"]["region"] == key)})</a>'
            for key, title, _ in REGIONS
        )
        all_towns = ", ".join(esc(site.areas[s]["meta"]["town"]) for s in site.area_order)
        out = [f'''
  <section class="block" style="padding-block:40px">
    <div class="wrap">
      <p class="eyebrow">{total} towns + Yardley, in 3 regions</p>
      <p class="region-jumps">{jumps}</p>
      <p style="color:var(--ink-2);max-width:80ch;margin:0">{all_towns}.</p>
    </div>
  </section>''']
        for i, (key, title, intro) in enumerate(REGIONS):
            towns = [site.areas[s] for s in site.area_order if site.areas[s]["meta"]["region"] == key]
            cards = "".join(
                f'<li><a href="{p.href(a["path"])}"><b>{esc(a["meta"]["town"])}, PA</b><span>{esc(a["meta"]["blurb"])}</span><em>Electrician in {esc(a["meta"]["town"])} →</em></a></li>'
                for a in towns
            )
            bg = " services" if i % 2 == 0 else ""
            out.append(f'''
  <section class="block{bg}" id="{key}">
    <div class="wrap">
      <div class="sec-head"><div><p class="eyebrow">{len(towns)} of {total} towns</p><h2>{esc(title)}</h2></div>
        <p>{esc(intro)}</p></div>
      <ul class="svc-grid">{cards}</ul>
    </div>
  </section>''')
        return "".join(out)
    return f


def services_index_extra(site):
    def f(p):
        out = []
        for key in ("g", "i", "l"):
            cat = C.CATEGORIES[key]
            hub = site.pages[cat["slug"]]
            intro = split_faq(hub["body"])[0].partition("\n\n")[0]
            cards = "".join(
                f'<li><a href="{p.href(s["path"])}"><b>{esc(s["meta"]["name"])}</b><span>{esc(s["meta"]["blurb"])}</span><em>Learn more →</em></a></li>'
                for s in site.cat_services(key)
            )
            bg = " services" if key != "i" else ""
            out.append(f'''
  <section class="block{bg}" id="{cat["slug"]}">
    <div class="wrap">
      <div class="sec-head"><div><p class="eyebrow">{len(site.cat_services(key))} services</p><h2>{esc(cat["name"])}</h2></div>
        <p>{p.inline(intro)} <a href="{p.href("/" + cat["slug"] + "/")}" style="color:var(--bronze-deep);font-weight:700">{esc(cat["name"])} overview →</a></p></div>
      <ul class="svc-grid">{cards}</ul>
    </div>
  </section>''')
        return "".join(out)
    return f


def contact_extra(site):
    def f(p):
        return f'''
  <section class="block">
    <div class="wrap contact-grid">
      <div>
        <p class="eyebrow">Contact details</p>
        <address class="nap" style="margin-top:14px">
          <b>{C.NAME}</b>
          {C.STREET}<br>{C.CITY}, {C.REGION} {C.POSTAL}<br>
          <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a> (call or text)<br>
          {hours_line()}
        </address>
        <p style="color:var(--ink-2);max-width:52ch;margin-top:20px">Tell us what's going on and where you are. We'll call back within one business day to set up a free, written estimate. For anything that's sparking, smoking or smells like burning, turn off the circuit at the panel and call us right away.</p>
      </div>
      <div class="contact-map"><iframe src="{C.MAP_EMBED}" title="Map: {C.NAME}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
    </div>
  </section>'''
    return f


def build_home(site):
    p = Page(site, "/")
    pg = site.pages["home"]
    m = pg["meta"]
    main_md, faqs = split_faq(pg["body"])
    # home.txt sections are separated by "## " headings with ids in the meta
    sections = {}
    for chunk in re.split(r"^#### ", main_md, flags=re.M)[1:]:
        k, _, v = chunk.partition("\n")
        sections[k.strip()] = v.strip()

    # Breaker panel: one tab per category, server-rendered for crawlers.
    tabs, panels = [], []
    for i, key in enumerate(["g", "i", "l"]):
        cat = C.CATEGORIES[key]
        feat = [x.strip() for x in m[f"featured_{key}"].split(",")]
        links = "".join(f'<li>{p.link(sl, esc(site.services[sl]["meta"]["name"]))}</li>' for sl in feat)
        n = len(site.cat_services(key))
        tabs.append(
            f'<button type="button" class="brk" role="tab" id="brk-{key}" data-id="{key}" aria-controls="panel-{key}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}"><span class="toggle" aria-hidden="true"></span><span class="brk-txt"><b>{cat["name"]}</b><small>{cat["tag"]}</small></span></button>'
        )
        panels.append(f'''<div class="detail" role="tabpanel" id="panel-{key}" aria-labelledby="brk-{key}"{"" if i == 0 else " hidden"}>
          <span class="num">Circuit 0{i + 1} · {cat["tag"]}</span>
          <h2>{cat["name"]} in Yardley</h2>
          <p>{p.inline(sections["cat_" + key])}</p>
          <ul class="links">{links}</ul>
          <div class="actions">{p.link(cat["slug"], f"See all {n} {cat['short'].lower()} services", cls="btn btn-bronze")}
            <a class="btn btn-ghost" href="tel:{C.PHONE_E164}">Call {C.PHONE_DISPLAY}</a></div>
        </div>''')

    towns = "".join(
        f'<li>{p.link(s, esc(site.areas[s]["meta"]["town"]))}</li>' for s in site.area_order
    )
    area_links = {site.areas[s]["meta"]["town"]: p.href(site.areas[s]["path"]) for s in site.area_order}
    area_links["Upper Makefield"] = area_links.get("Washington Crossing")
    area_links["Falls Township"] = area_links.get("Fairless Hills")
    area_links["Middletown"] = area_links.get("Langhorne")
    aliases = {"Trevose": "Feasterville", "Feasterville-Trevose": "Feasterville", "Lower Southampton": "Feasterville",
               "Upper Southampton": "Southampton", "Holland": "Richboro", "Churchville": "Richboro", "Northampton": "Richboro",
               "Ivyland": "Warminster", "New Britain": "Chalfont", "Croydon": "Bristol", "Solebury": "New Hope",
               "Penndel": "Langhorne", "Langhorne Manor": "Langhorne", "Tullytown": "Levittown"}
    for k, v in aliases.items():
        area_links[k] = area_links.get(v)

    faq_html = faq_section(p, faqs)
    main = f'''  <section class="hero hero-photo" id="top">
    <div class="hero-bg">
      <img src="{p.href(HERO_BG)}" width="1200" height="1800" alt="Ryan Huck of Joe Huck Electric working on a home electrical panel" fetchpriority="high" decoding="async">
    </div>
    <div class="wrap">
      <div>
        <p class="eyebrow">Only electrical, for 40+ years</p>
        <h1>{esc(m["h1"])} <em>Not Your Neighborhood Handyman.</em></h1>
        <p class="lede">{p.inline(sections["lede"])}</p>
        <div class="hero-ctas">
          <a class="btn btn-bronze" href="#estimate">Get a free estimate {ICON_ARROW}</a>
          <a class="btn btn-ghost" href="tel:{C.PHONE_E164}">{ICON_CALL}{C.PHONE_DISPLAY}</a>
        </div>
        <div class="proof">
          <span><svg viewBox="0 0 20 20" fill="currentColor"><path d="M10 1l2.6 5.6 6.1.7-4.5 4.2 1.2 6L10 14.5 4.6 17.5l1.2-6L1.3 7.3l6.1-.7z"/></svg>Nextdoor Neighborhood Favorite 2023 &amp; 2024</span>
          <span><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 2l7 3v5c0 4-3 7-7 8-4-1-7-4-7-8V5z"/><path d="M7 10l2 2 4-4"/></svg>Licensed &amp; insured</span>
        </div>
      </div>
      {quote_card()}
    </div>
  </section>

  <section class="creds" aria-label="Credentials">
    <div class="wrap">
      <ul>
        <li><span class="big">40<sup>yrs</sup></span><span class="sm">Serving Yardley &amp; Bucks County</span></li>
        <li><span class="big">Master</span><span class="sm">Electrician-led, never a handyman</span></li>
        <li><span class="big">’23 + ’24</span><span class="sm">Nextdoor Neighborhood Favorite</span></li>
        <li><span class="big">Only Electric</span><span class="sm">Licensed &amp; insured. Never a jack-of-all-trades.</span></li>
      </ul>
    </div>
  </section>

  <section class="block services" id="services">
    <div class="wrap">
      <div class="sec-head">
        <div><p class="eyebrow">What we do</p><h2>Every Circuit in the House.</h2></div>
        <p>{p.inline(sections["services_intro"])}</p>
      </div>
      <div class="panel">
        <div class="box">
          <div class="box-top"><span class="screw" aria-hidden="true"></span><span class="main">● Main · 200A</span><span class="screw" aria-hidden="true"></span></div>
          <div class="breakers breakers-3" role="tablist" aria-label="Service categories">{"".join(tabs)}</div>
          <p class="box-foot">CIRCUIT DIRECTORY — JOE HUCK ELECTRIC · YARDLEY, PA</p>
        </div>
        {"".join(panels)}
      </div>
    </div>
  </section>

  <section class="block about-home" id="about">
    <div class="wrap">
      <div>
        <p class="eyebrow">About us</p>
        <h2>{esc(m["about_h2"].split("|")[0])} <em>{esc(m["about_h2"].split("|")[1])}</em></h2>
        <div class="prose">{p.md(sections["about"])}</div>
        <a class="btn btn-bronze" href="#estimate" style="margin-top:8px">Free Diagnosis &amp; Quote {ICON_ARROW}</a>
      </div>
      <figure class="about-photo">
        <img src="{p.href(ABOUT_PHOTO)}" width="900" height="1350" alt="Ryan Huck, head electrician at Joe Huck Electric, on a job in a Bucks County home" loading="lazy" decoding="async">
      </figure>
    </div>
  </section>
{team_section(p, " services")}

  <section class="block" id="process">
    <div class="wrap">
      <div class="sec-head">
        <div><p class="eyebrow">How a job works</p><h2>No Surprises, Start to Finish.</h2></div>
        <p>These are the same four steps whether you're swapping one fixture or upgrading the whole service.</p>
      </div>
      <ol class="steps">
        <li><h3>Call or Request</h3><p>Tell us what's going on. We'll ask a few questions and set a time that works for you.</p></li>
        <li><h3>Free Estimate</h3><p>We look at the job in person and give you a clear, written price before any work starts.</p></li>
        <li><h3>Clean Install</h3><p>We handle permits, do the work neatly and to code, and clean up before we leave.</p></li>
        <li><h3>Inspected &amp; Done</h3><p>We test every circuit, meet the inspector and walk you through what we did.</p></li>
      </ol>
    </div>
  </section>

  <section class="block area" id="area">
    <div class="wrap">
      <div>
        <p class="eyebrow">Service area</p>
        <h2>{esc(m["area_h2"])}</h2>
        <p>{p.inline(sections["area"])}</p>
        <form class="checker" id="areaForm" role="search" data-links='{esc(json.dumps(area_links), quote=True)}'>
          <label for="a-town" style="position:absolute;left:-9999px">Your town</label>
          <input id="a-town" list="townlist" placeholder="Your town, e.g. Langhorne" autocomplete="address-level2">
          <button class="btn" type="submit">Check</button>
        </form>
        <p class="result" id="areaResult" aria-live="polite"></p>
      </div>
      <ul class="towns">
        <li class="hi">Yardley <small>Home base</small></li>
        {towns}
        <li class="all">{p.link("service-areas", "…and the rest of Bucks County")}</li>
      </ul>
    </div>
  </section>

  <section class="block rep" id="reviews">
    <div class="wrap">
      <div>
        <p class="eyebrow">Reputation</p>
        <blockquote style="margin-top:16px">Two years running, <span>Bucks County neighbors</span> named us a Nextdoor Neighborhood Favorite.</blockquote>
        <p class="who">Neighborhood Favorite, 2023 &amp; 2024. Read what customers say about us on the sites below.</p>
      </div>
      <div class="badges">
        <a class="badge" href="{C.SAME_AS[1]}" target="_blank" rel="noopener"><span class="ic"><svg viewBox="0 0 20 20" fill="currentColor"><path d="M10 1l2.6 5.6 6.1.7-4.5 4.2 1.2 6L10 14.5 4.6 17.5l1.2-6L1.3 7.3l6.1-.7z"/></svg></span><span><b>Nextdoor</b><small>Neighborhood Favorite ’23 &amp; ’24</small></span><span class="arr">↗</span></a>
        <a class="badge" href="{C.SAME_AS[2]}" target="_blank" rel="noopener"><span class="ic"><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l7-6 7 6v8H3z"/><path d="M8 17v-5h4v5"/></svg></span><span><b>HomeAdvisor</b><small>Verified customer reviews</small></span><span class="arr">↗</span></a>
        <a class="badge" href="{C.SAME_AS[0]}" target="_blank" rel="noopener"><span class="ic"><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2"><circle cx="10" cy="10" r="8"/><path d="M11 17v-6h2.5M11 11V8.5A1.5 1.5 0 0 1 12.5 7H14M8.5 11H11"/></svg></span><span><b>Facebook</b><small>Recent jobs &amp; updates</small></span><span class="arr">↗</span></a>
      </div>
    </div>
  </section>
{faq_html}'''
    schema = [business_schema(site), {"@type": "WebSite", "name": C.NAME, "url": C.DOMAIN + "/"}]
    if faqs:
        schema.append(faq_schema(faqs))
    out = layout(p, title=m["title"], desc=m["desc"], main=main, schema=schema, home=True)
    visible = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", main, flags=re.S)
    wc = words(visible)
    if wc < 1000:
        WARNINGS.append(f"/: homepage has {wc} words (playbook: ~1,000)")
    REPORT.insert(0, ("/", m["h1"], m["title"], wc, len(p.links), "(homepage)"))
    return out


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def write(out_dir, path, text):
    f = out_dir / path.lstrip("/") / "index.html"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")


def main():
    preview = "--preview" in sys.argv
    out_dir = Path(sys.argv[sys.argv.index("--preview") + 1]) if preview else ROOT / "public"
    site = Site(preview=preview)
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    shutil.copytree(ROOT / "site" / "assets", out_dir / "assets")

    write(out_dir, "/", build_home(site))
    for key in ("g", "i", "l"):
        write(out_dir, f"/{C.CATEGORIES[key]['slug']}/", build_hub(site, key))
    for slug in site.svc_order:
        write(out_dir, site.services[slug]["path"], build_service(site, site.services[slug]))
    for slug in site.area_order:
        write(out_dir, site.areas[slug]["path"], build_area(site, site.areas[slug]))
    write(out_dir, AREA_PREFIX, build_simple(site, "service-areas", AREA_PREFIX, "areas", areas_index_extra(site)))
    write(out_dir, "/services/", build_simple(site, "services", "/services/", "services", services_index_extra(site)))
    write(out_dir, "/about/", build_simple(site, "about", "/about/", "about", lambda p: team_section(p, " services")))
    write(out_dir, "/contact/", build_simple(site, "contact", "/contact/", "contact", contact_extra(site)))

    paths = [r[0] for r in REPORT]
    if not preview:
        (out_dir / "sitemap.xml").write_text(
            '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "".join(f"  <url><loc>{C.DOMAIN}{u}</loc></url>\n" for u in paths)
            + "</urlset>\n", encoding="utf-8")
        (out_dir / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {C.DOMAIN}/sitemap.xml\n", encoding="utf-8")
        (out_dir / "_redirects").write_text("".join(f"{a} {b} 301\n{a}/ {b} 301\n" for a, b in C.REDIRECTS.items()), encoding="utf-8")

        # GBP services sheet: one row per checklist service, with its page and a <300-char description.
        with open(ROOT / "gbp-services.csv", "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["GBP category", "GBP service name", "Description (<300 chars)", "Landing page"])
            lc = C.CATEGORIES["l"]
            w.writerow([lc["name"], "Lighting installation", site.pages[lc["slug"]]["body"].partition("\n\n")[0][:299], C.DOMAIN + "/" + lc["slug"] + "/"])
            for slug in site.svc_order:
                s = site.services[slug]
                for name in s["meta"].get("gbp", s["meta"]["name"]).split(";"):
                    w.writerow([C.CATEGORIES[s["meta"]["cat"]]["name"], name.strip(), s["meta"]["blurb"], C.DOMAIN + s["path"]])

        with open(ROOT / "PAGES.md", "w", encoding="utf-8") as fh:
            fh.write("# Page Inventory\n\nGenerated by `build.py`. One row per page.\n\n")
            fh.write("| URL | H1 | Title tag | Words | Links | GBP services covered |\n|---|---|---|---:|---:|---|\n")
            for path, h1, title, wc, nl, gbp in REPORT:
                fh.write(f"| `{path}` | {h1} | {title} | {wc} | {nl} | {gbp.replace(';', ', ')} |\n")

    print(f"Built {len(paths)} pages into {out_dir}")
    if WARNINGS:
        print(f"\n{len(WARNINGS)} warning(s):")
        for wmsg in WARNINGS:
            print("  -", wmsg)


if __name__ == "__main__":
    main()
