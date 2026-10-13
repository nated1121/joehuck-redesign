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
import photos as PH  # noqa: E402

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
        f'''<li class="hp-team-card">
          <img src="{p.href(t["img"])}" width="900" height="1350" alt="{esc(t["full"])}, {esc(t["role"].lower())} at {C.NAME}" loading="lazy" decoding="async">
          <p><b>{esc(t["full"])}</b><span>{esc(t["role"])}</span></p>
        </li>''' for t in TEAM)
    return f'''
  <section class="hp-sec hp-paper" id="team">
    <div class="wrap">
      <div class="hp-head"><p class="eyebrow">The team</p><h2>Meet the Local Team</h2>
        <p>You deserve a team you know and trust. With us, you always know who you're getting.</p></div>
      <ul class="hp-grid hp-2 hp-team">{cards}</ul>
      <p class="hp-note">Ryan leads every job as head electrician, with Abie at his side. Together they carry on the work Joe Huck started in Bucks County over 40 years ago.</p>
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

    def canonical(self, ref):
        """Follow a folded service to the page that covers it now."""
        tgt = C.FOLDED_SERVICES.get(ref)
        if tgt is None:
            return ref
        return C.CATEGORIES[tgt[4:]]["slug"] if tgt.startswith("hub:") else tgt

    def resolve(self, ref):
        """@slug → site path (None for a town that no longer has its own page)."""
        ref = self.canonical(ref)
        if ref in C.REMOVED_AREAS:
            return None
        if ref in self.services:
            return self.services[ref]["path"]
        if ref in self.areas:
            return self.areas[ref]["path"]
        for cat in C.CATEGORIES.values():
            if ref == cat["slug"]:
                return f"/{ref}/"
        fixed = {"home": "/", "contact": "/contact/", "about": "/about/", "service-areas": AREA_PREFIX}
        if ref in fixed:
            return fixed[ref]
        raise SystemExit(f"Unknown link target @{ref}")

    def kind(self, ref):
        ref = self.canonical(ref)
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
        if path is None or path == self.path:
            return text
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


MAPS_LINK = "https://www.google.com/maps/search/?api=1&query=" + "+".join(f"{C.NAME} {C.STREET} {C.CITY} {C.REGION} {C.POSTAL}".split())


def map_embed(preview, title):
    """Embedded Google Map on the live site. File previews and embedded viewers
    block third-party frames, so previews get an address card instead."""
    if not preview:
        return f'<iframe src="{C.MAP_EMBED}" title="{esc(title)}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
    return f'''<div class="map-card">
        <div><b>{C.NAME}</b><span>{C.STREET}, {C.CITY}, {C.REGION} {C.POSTAL}</span></div>
        <a class="btn btn-bronze" href="{MAPS_LINK}" target="_blank" rel="noopener">Open in Google Maps</a>
      </div>'''


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
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\[([^\]]+)\]\(@[\w-]+\)", r"\1", a).replace("**", "")}}
            for q, a in pairs
        ],
    }


# ----------------------------------------------------------------------------
# Shared page parts
# ----------------------------------------------------------------------------
NAV = [
    ("Services", None, "services"),  # dropdown of the three category pages, no page of its own
    ("Service Areas", AREA_PREFIX, "areas"),
    ("About", "/about/", "about"),
    ("Contact", "/contact/", "contact"),
]


def layout(p, *, title, desc, main, schema, active=None, home=False):
    if len(title) > 80:
        WARNINGS.append(f"{p.path}: title is {len(title)} chars (aim for ≤ 80)")
    if not 70 <= len(desc) <= 160:
        WARNINGS.append(f"{p.path}: meta description is {len(desc)} chars (aim for 70–160)")
    cur = ' aria-current="page"'
    def nav_item(label, url, key):
        if url:
            return f'<li><a href="{p.href(url)}"{cur if key == active else ""}>{label}</a></li>'
        subs = "".join(
            f'<li><a href="{p.href("/" + c["slug"] + "/")}"{cur if p.path.startswith("/" + c["slug"] + "/") and p.path.count("/") == 2 else ""}>{c["name"]}</a></li>'
            for c in C.CATEGORIES.values())
        on = " on" if key == active else ""
        return f'<li class="has-sub"><span class="nav-parent{on}" tabindex="0">{label}</span><ul class="sub">{subs}</ul></li>'
    nav = "".join(nav_item(*item) for item in NAV)
    ld = json.dumps({"@context": "https://schema.org", "@graph": schema}, ensure_ascii=False, indent=1)
    canonical = C.DOMAIN + p.path
    map_band = ""
    if home:
        map_band = f'''<div class="map-band">{map_embed(p.site.preview, f"Map: {C.NAME}, {C.STREET}, {C.CITY}, {C.REGION}")}</div>'''
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
<link rel="icon" href="{p.href('/favicon.ico')}" sizes="32x32">
<link rel="icon" href="{p.href('/assets/favicon/favicon.svg')}" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p.href('/assets/favicon/apple-touch-icon.png')}">
<link rel="manifest" href="{p.href('/assets/favicon/site.webmanifest')}">
<meta name="theme-color" content="#AE9B6C">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,400;0,500;0,600;0,700;0,800;1,500&display=swap">
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


def quote_card(cat=None, service=None):
    if service:
        picker = f'''<input type="hidden" name="service" value="{esc(service)}">
          <p class="about-svc">About: <b>{esc(service)}</b></p>'''
    else:
        opts = "".join(
            f'<option value="{v}"{" selected" if k == cat else ""}>{v}</option>'
            for k, v in [("g", "Repair or upgrade"), ("i", "Installation"), ("l", "Lighting"), ("o", "Something else")]
        )
        picker = f'''<div class="field"><label for="q-svc">What do you need?</label>
            <select id="q-svc" name="service"><option value="">Choose one</option>{opts}</select>
          </div>'''
    return f'''<div class="quote" id="estimate">
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
    crumb_html = " / ".join(
        f'<a href="{p.href(path)}">{esc(name)}</a>' if i < len(crumbs) - 1 else f'<span aria-current="page">{esc(name)}</span>'
        for i, (name, path) in enumerate(crumbs)
    )
    return f'''  <section class="hp-sec hp-paper ip-hero">
    <div class="wrap hp-cols">
      <div>
        <nav class="ip-crumbs" aria-label="Breadcrumb">{crumb_html}</nav>
        <p class="eyebrow">{esc(eyebrow)}</p>
        <h1>{esc(h1)}</h1>
        <p class="lede">{lede}</p>
        <div class="hp-btns">
          <a class="btn btn-bronze" href="#estimate">Get a free estimate</a>
          <a class="btn btn-outline" href="tel:{C.PHONE_E164}">Call {C.PHONE_DISPLAY}</a>
        </div>
        <p class="ip-trust">Licensed &amp; insured · Only electrical, 40+ years · Free written estimates</p>
      </div>
      {quote_card(cat, service)}
    </div>
  </section>'''


def ip_head(label, h2, intro=None):
    return f'''<div class="hp-head">
        <p class="eyebrow">{esc(label)}</p>
        <h2>{esc(h2)}</h2>
        {f"<p>{intro}</p>" if intro else ""}
      </div>'''


def text_cards(p, items, cols=3):
    """Cards with a title, a line of text and a link: a Wix repeater or a row of boxes."""
    cards = "".join(
        f'''<li class="hp-card"><div class="hp-card-body"><h3>{esc(title)}</h3><p>{esc(text)}</p><a class="hp-more" href="{p.href(path)}">{esc(more)} →</a></div></li>'''
        for path, title, text, more in items)
    return f'<ul class="hp-grid hp-{cols}">{cards}</ul>'


def faq_section(p, pairs, heading="Questions"):
    if not pairs:
        return ""
    items = "".join(f"<h3>{esc(q)}</h3><p>{p.inline(a)}</p>" for q, a in pairs)
    intro = f'Still have a question? Call <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a>. You\'ll talk to an electrician, not a call center.'
    return f'''
  <section class="hp-sec faq">
    <div class="wrap">
      {ip_head(heading, "Good to Know", intro)}
      <div class="ip-faq">{items}</div>
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


# ----------------------------------------------------------------------------
# WWP components: real job photos, "why us" band, how-a-job-works strip
# ----------------------------------------------------------------------------
def photo_fig(p, name, cls="job-photo", focus=None, caption=None, eager=False, show_caption=True):
    alt, cap, pos = PH.PHOTOS[name]
    pos = focus or pos
    cap = caption if caption is not None else cap
    base = PH.JOBS + name
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    figcap = f"<figcaption>{esc(cap)}</figcaption>" if (cap and show_caption) else ""
    return (f'<figure class="{cls}"><img src="{p.href(base + ".jpg")}" '
            f'srcset="{p.href(base + "-sm.jpg")} 560w, {p.href(base + ".jpg")} 1000w" '
            f'sizes="(max-width: 960px) 100vw, 700px" width="1000" height="1500" '
            f'alt="{esc(alt)}" style="object-position:{pos}" {load} decoding="async">{figcap}</figure>')


def service_photo(p, slug, **kw):
    entry = PH.SERVICE_PHOTOS.get(slug)
    if not entry:
        return ""
    if isinstance(entry, tuple):
        name, focus, caption = entry
        return photo_fig(p, name, focus=focus, caption=caption, **kw)
    return photo_fig(p, entry, **kw)


def why_band(p):
    avatars = "".join(
        f'<img src="{p.href("/assets/img/avatar-" + t["name"].lower() + ".jpg")}" width="160" height="160" alt="{esc(t["full"])}" loading="lazy">'
        for t in TEAM
    )
    return f'''
  <section class="why-band" aria-label="Why homeowners call Joe Huck Electric">
    <div class="wrap">
      <div class="why-item">
        <div class="why-avatars">{avatars}</div>
        <div><h2>You'll Know Who's Coming</h2><p>Ryan and Abie handle every job themselves. No call center, no strangers at your door.</p></div>
      </div>
      <div class="why-item">
        <span class="why-ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/></svg></span>
        <div><h2>Free Diagnosis &amp; Written Quote</h2><p>We find the problem and price it in writing before any work starts. No surprises on the invoice.</p></div>
      </div>
      <div class="why-item">
        <span class="why-ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.9 6.1 6.7.8-4.9 4.6 1.3 6.6L12 16.9 6 20.1l1.3-6.6L2.4 8.9l6.7-.8z"/></svg></span>
        <div><h2>40+ Years, Only Electrical</h2><p>Licensed and insured. Named a Nextdoor Neighborhood Favorite in 2023 and 2024.</p></div>
      </div>
    </div>
  </section>'''


def steps_strip(p, heading="What Happens When You Call"):
    steps = "".join(
        f'<li class="hp-step"><span class="hp-num">{i}</span><h3>{esc(h)}</h3><p>{esc(t)}</p></li>'
        for i, (h, t) in enumerate(HOME_STEPS, 1))
    return f'''
  <section class="hp-sec">
    <div class="wrap">
      {ip_head("How a job works", heading, "The same four steps on every job, from a single outlet to a full panel upgrade.")}
      <ol class="hp-grid hp-4">{steps}</ol>
    </div>
  </section>'''


def photo_cards(p, site, slugs):
    out = []
    for slug in slugs:
        sv = site.services[slug]
        out.append(f'''<li class="hp-card">{service_photo(p, slug, cls="hp-img", show_caption=False)}<div class="hp-card-body"><h3>{esc(sv["meta"]["name"])}</h3><p>{esc(sv["meta"]["blurb"])}</p><a class="hp-more" href="{p.href(sv["path"])}">Learn more →</a></div></li>''')
    return f'<ul class="hp-grid hp-{min(len(out), 3)}">{"".join(out)}</ul>'


HUB_FEATURED = {
    "g": ["electrical-panel-upgrade", "electrical-repair-troubleshooting", "home-rewiring"],
    "i": ["switch-outlet-installation", "gfci-outlet-installation", "dedicated-circuit-installation"],
    "l": ["recessed-lighting-installation", "light-fixture-installation"],
}


def build_service(site, s):
    m = s["meta"]
    cat = C.CATEGORIES[m["cat"]]
    p = Page(site, s["path"])
    main_md, faqs = split_faq(s["body"])
    intro, _, rest = main_md.partition("\n\n")
    lede = p.inline(intro)
    prose = p.md(rest)
    inline = {r for _, r in p.links}
    rel = []
    for r in (site.canonical(x.strip()) for x in m["related"].split(",")):
        if r in site.services and r != s["slug"] and r not in rel:
            rel.append(r)
    if len(rel) < 3:  # top up from the same category
        rel += [x for x in site.svc_order if site.services[x]["meta"]["cat"] == m["cat"] and x != s["slug"] and x not in rel][:3 - len(rel)]
    n_cat = len(site.cat_services(m["cat"]))
    crumbs = [("Home", "/"), (cat["name"], f"/{cat['slug']}/"), (m["name"], s["path"])]
    faq_html = faq_section(p, faqs)
    rel_cards = text_cards(p, [(site.services[r]["path"], site.services[r]["meta"]["name"], site.services[r]["meta"]["blurb"], "Learn more")
                               for r in rel[:3]])
    for r in rel[:3]:
        p.links.append(("service", r))
    main = page_hero(p, crumbs, cat["name"], m["h1"], lede, service=m["name"]) + why_band(p) + f'''
  <section class="hp-sec">
    <div class="wrap">
      <article class="prose ip-article">
{service_photo(p, s["slug"])}
{prose}
      </article>
    </div>
  </section>
  <section class="hp-sec hp-paper">
    <div class="wrap">
      {ip_head("Related", "Related Services")}
      {rel_cards}
      <p class="hp-center-btn"><a class="btn btn-outline" href="{p.href("/" + cat["slug"] + "/")}">See all {n_cat} {esc(cat["short"].lower())} services</a></p>
    </div>
  </section>
{steps_strip(p)}
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
    near = [n.strip() for n in m["nearby"].split(",")]
    nearby = text_cards(p, [(site.areas[n]["path"], site.areas[n]["meta"]["town"] + ", PA", site.areas[n]["meta"]["blurb"], "Electrician in " + site.areas[n]["meta"]["town"]) for n in near])
    crumbs = [("Home", "/"), ("Service Areas", AREA_PREFIX), (m["town"], a["path"])]
    faq_html = faq_section(p, faqs)
    main = page_hero(p, crumbs, f"Serving {m['town']}, PA", m["h1"], lede, cat=None) + why_band(p) + f'''
  <section class="hp-sec">
    <div class="wrap">
      <article class="prose ip-article">
{prose}
      </article>
    </div>
  </section>
  <section class="hp-sec hp-paper">
    <div class="wrap">
      {ip_head("Nearby", "Nearby Towns We Serve")}
      {nearby}
    </div>
  </section>
{steps_strip(p)}
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
    cards = text_cards(p, [(s["path"], s["meta"]["name"], s["meta"]["blurb"], "Learn more") for s in site.cat_services(key)])
    crumbs = [("Home", "/"), (cat["name"], path)]
    faq_html = faq_section(p, faqs)
    n = len(site.cat_services(key))
    main = page_hero(p, crumbs, f"{cat['name']} · Yardley, PA", m["h1"], lede, cat=key) + why_band(p) + f'''
  <section class="hp-sec">
    <div class="wrap hp-cols ip-top">
      <div class="prose">
        <p class="eyebrow">Overview</p>
        {p.md(rest)}
      </div>
      <img class="hp-photo" src="{p.href(PH.JOBS + PH.CATEGORY_PHOTOS[key] + ".jpg")}" width="1000" height="1500" alt="{esc(PH.PHOTOS[PH.CATEGORY_PHOTOS[key]][0])}" loading="lazy" decoding="async">
    </div>
  </section>
  <section class="hp-sec hp-paper">
    <div class="wrap">
      {ip_head("Most requested", f"Popular {cat['short']} Jobs")}
      {photo_cards(p, site, HUB_FEATURED[key])}
    </div>
  </section>
  <section class="hp-sec">
    <div class="wrap">
      {ip_head(f"{n} services", f"All {cat['name']}", "Every service in this category, each with its own page. Not sure which fits? Call and describe what's going on.")}
      {cards}
    </div>
  </section>
{steps_strip(p)}
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
  <section class="hp-sec">
    <div class="wrap">
      <article class="prose ip-article">
{p.md(rest)}
      </article>
    </div>
  </section>''' if rest else ""
    band = why_band(p) if key == "service-areas" else ""
    main = page_hero(p, crumbs, m["eyebrow"], m["h1"], p.inline(intro), cat=hero_cat) + band + body + extra(p) + faq_section(p, faqs)
    schema = [business_schema(site), breadcrumb_schema(crumbs)]
    out = layout(p, title=m["title"], desc=m["desc"], main=main, schema=schema, active=active)
    REPORT.append((path, m["h1"], m["title"], words(main), len(p.links), "—"))
    return out


REGIONS = [
    ("lower", "Near Yardley", "The towns closest to our Yardley base, along the river and across lower Bucks, where we work every week."),
    ("central", "Central Bucks", "Richboro, Warminster, Warrington, Doylestown and Chalfont. We group appointments here to keep scheduling reliable."),
    ("upper", "Upper Bucks", "Perkasie, Sellersville and Quakertown. Call early, and we'll schedule your job with our other upper Bucks appointments."),
]


def town_list(site):
    """Every service-area town in region order: slugs for towns with a page, names for the rest."""
    out = []
    for key, _, _ in REGIONS:
        out += [sl for sl in site.area_order if site.areas[sl]["meta"]["region"] == key]
        out += [name for name, reg in C.TOWNS_WITHOUT_PAGES if reg == key]
    return out


def areas_index_extra(site):
    def f(p):
        out = []
        for i, (key, title, intro) in enumerate(REGIONS):
            towns = [site.areas[sl] for sl in site.area_order if site.areas[sl]["meta"]["region"] == key]
            also = [name for name, reg in C.TOWNS_WITHOUT_PAGES if reg == key]
            cards = text_cards(p, [(a["path"], a["meta"]["town"] + ", PA", a["meta"]["blurb"], "Electrician in " + a["meta"]["town"]) for a in towns]) if towns else ""
            also_line = f'<p class="ip-also">{"Also serving" if towns else "Serving"} {", ".join(also[:-1]) + " and " + also[-1] if len(also) > 1 else also[0]}. Call to schedule.</p>' if also else ""
            bg = " hp-paper" if i % 2 == 0 else ""
            out.append(f'''
  <section class="hp-sec{bg}" id="{key}">
    <div class="wrap">
      {ip_head(f"{len(towns) + len(also)} towns", title, esc(intro))}
      {cards}
      {also_line}
    </div>
  </section>''')
        return "".join(out)
    return f


def contact_extra(site):
    def f(p):
        return f'''
  <section class="hp-sec">
    <div class="wrap hp-cols">
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
      <div class="contact-map">{map_embed(p.site.preview, f"Map: {C.NAME}")}</div>
    </div>
  </section>'''
    return f


# Homepage copy that isn't in pages.txt. Kept here so the page and the Wix
# build guide (WIX-HOMEPAGE.md) always say the same thing.
HOME_CREDS = [
    ("40+ Years", "Serving Yardley & Bucks County"),
    ("Master Electrician", "Electrician-led, never a handyman"),
    ("Nextdoor Favorite", "Neighborhood Favorite 2023 & 2024"),
    ("Only Electrical", "Licensed & insured"),
]
HOME_STEPS = [
    ("Call or Request", "Tell us what's going on. We'll ask a few questions and set a time that works for you."),
    ("Free Estimate", "We look at the job in person and give you a clear, written price before any work starts."),
    ("Clean Install", "We handle permits, do the work neatly and to code, and clean up before we leave."),
    ("Inspected & Done", "We test every circuit, meet the inspector and walk you through what we did."),
]
HOME_HEADS = {
    "services": ("What we do", "Three Kinds of Electrical Work, One Local Team",
                 None),  # intro comes from pages.txt (services_intro)
    "popular": ("Most requested", "Popular Electrical Services in Yardley",
                "The jobs Yardley and Bucks County homeowners call us for most. Every one starts with a free, written estimate."),
    "team": ("The team", "Meet the Local Team",
             "You deserve a team you know and trust. With us, you always know who you're getting."),
    "process": ("How a job works", "No Surprises, Start to Finish",
                "The same four steps whether you're swapping one fixture or upgrading the whole service."),
    "reviews": ("Reputation", "Recommended by Your Neighbors",
                "Bucks County neighbors named us a Nextdoor Neighborhood Favorite two years running. Read what customers say on the sites below."),
    "faq": ("Questions", "Good to Know",
            "Still have a question? Call 215-906-4634. You'll talk to an electrician, not a call center."),
}
TEAM_NOTE = "Ryan leads every job as head electrician, with Abie at his side. Together they carry on the work Joe Huck started in Bucks County over 40 years ago."


def home_head(key, intro=None, dark=False):
    label, h2, text = HOME_HEADS[key]
    text = intro or text
    return f'''<div class="hp-head">
        <p class="eyebrow">{esc(label)}</p>
        <h2>{esc(h2)}</h2>
        {f"<p>{text}</p>" if text else ""}
      </div>'''


def build_home(site):
    p = Page(site, "/")
    pg = site.pages["home"]
    m = pg["meta"]
    main_md, faqs = split_faq(pg["body"])
    sections = {}
    for chunk in re.split(r"^#### ", main_md, flags=re.M)[1:]:
        k, _, v = chunk.partition("\n")
        sections[k.strip()] = v.strip()

    # Every section below is one full-width strip holding plain columns, cards
    # and text, so it maps one-to-one onto Wix strips, boxes and repeaters.
    # See WIX-HOMEPAGE.md.
    cat_cards = ""
    for key in ("g", "i", "l"):
        cat = C.CATEGORIES[key]
        feat = [x.strip() for x in m[f"featured_{key}"].split(",")]
        links = "".join(f'<li>{p.link(sl, esc(site.services[sl]["meta"]["name"]))}</li>' for sl in feat)
        n = len(site.cat_services(key))
        cat_cards += f'''<li class="hp-card">
          {photo_fig(p, PH.CATEGORY_PHOTOS[key], cls="hp-img", show_caption=False)}
          <div class="hp-card-body">
            <p class="hp-tag">{esc(cat["tag"])}</p>
            <h2>{esc(cat["name"])}</h2>
            <p>{p.inline(sections["cat_" + key])}</p>
            <ul class="hp-links">{links}</ul>
            {p.link(cat["slug"], f"See all {n} services", cls="btn btn-bronze")}
          </div>
        </li>'''

    popular_cards = ""
    for item in m["popular"].split(";"):
        slug, _, anchor = item.strip().partition("=")
        sv = site.services[slug]
        popular_cards += f'''<li class="hp-card">
          {service_photo(p, slug, cls="hp-img", show_caption=False)}
          <div class="hp-card-body">
            <h2>{esc(sv["meta"]["name"])}</h2>
            <p>{esc(sv["meta"]["blurb"])}</p>
            {p.link(slug, esc(anchor) + " →", cls="hp-more")}
          </div>
        </li>'''

    team_cards = "".join(
        f'''<li class="hp-team-card">
          <img src="{p.href(t["img"])}" width="900" height="1350" alt="{esc(t["full"])}, {esc(t["role"].lower())} at {C.NAME}" loading="lazy" decoding="async">
          <p><b>{esc(t["full"])}</b><span>{esc(t["role"])}</span></p>
        </li>''' for t in TEAM)

    creds = "".join(f'<li><b>{esc(a)}</b><span>{esc(b)}</span></li>' for a, b in HOME_CREDS)
    steps = "".join(
        f'<li class="hp-step"><span class="hp-num">{i}</span><h3>{esc(h)}</h3><p>{esc(t)}</p></li>'
        for i, (h, t) in enumerate(HOME_STEPS, 1))
    towns = "".join(f'<li>{p.link(s, esc(site.areas[s]["meta"]["town"]))}</li>' if s in site.areas else f'<li>{esc(s)}</li>'
                    for s in town_list(site))
    badges = "".join(
        f'<a class="btn btn-outline" href="{url}" target="_blank" rel="noopener">{name} ↗</a>'
        for name, url in [("Nextdoor", C.SAME_AS[1]), ("HomeAdvisor", C.SAME_AS[2]), ("Facebook", C.SAME_AS[0])])
    faq_items = "".join(
        f'<details{" open" if i == 0 else ""}><summary>{esc(q)}<span class="pm" aria-hidden="true"></span></summary><p>{p.inline(a)}</p></details>'
        for i, (q, a) in enumerate(faqs))
    about_a, about_b = m["about_h2"].split("|")
    faq_intro = (f'Still have a question? Call <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a>. '
                 "You'll talk to an electrician, not a call center.")

    main = f'''  <section class="hp-hero" id="top" style="--hero-img:url('{p.href(HERO_BG)}')">
    <div class="wrap hp-cols">
      <div class="hp-hero-text">
        <p class="eyebrow">Only electrical, for 40+ years</p>
        <h1>{esc(m["h1"])} <em>Not Your Neighborhood Handyman.</em></h1>
        <p class="lede">{p.inline(sections["lede"])}</p>
        <div class="hp-btns">
          <a class="btn btn-bronze" href="#estimate">Get a free estimate</a>
          <a class="btn btn-outline" href="tel:{C.PHONE_E164}">Call {C.PHONE_DISPLAY}</a>
        </div>
      </div>
      {quote_card()}
    </div>
  </section>

  <section class="hp-creds" aria-label="Credentials">
    <ul class="wrap">{creds}</ul>
  </section>

  <section class="hp-sec" id="services">
    <div class="wrap">
      {home_head("services", p.inline(sections["services_intro"]))}
      <ul class="hp-grid hp-3">{cat_cards}</ul>
    </div>
  </section>

  <section class="hp-sec hp-paper" id="popular">
    <div class="wrap">
      {home_head("popular")}
      <ul class="hp-grid hp-3">{popular_cards}</ul>
    </div>
  </section>

  <section class="hp-sec" id="about">
    <div class="wrap hp-cols">
      <div>
        <p class="eyebrow">About us</p>
        <h2>{esc(about_a)} <em>{esc(about_b)}</em></h2>
        <div class="prose">{p.md(sections["about"])}</div>
        <a class="btn btn-bronze" href="#estimate">Free Diagnosis &amp; Quote</a>
      </div>
      <img class="hp-photo" src="{p.href(ABOUT_PHOTO)}" width="900" height="1350" alt="Ryan Huck, head electrician at Joe Huck Electric, on a job in a Bucks County home" loading="lazy" decoding="async">
    </div>
  </section>

  <section class="hp-sec hp-paper" id="team">
    <div class="wrap">
      {home_head("team")}
      <ul class="hp-grid hp-2 hp-team">{team_cards}</ul>
      <p class="hp-note">{esc(TEAM_NOTE)}</p>
    </div>
  </section>

  <section class="hp-sec" id="process">
    <div class="wrap">
      {home_head("process")}
      <ol class="hp-grid hp-4">{steps}</ol>
    </div>
  </section>

  <section class="hp-sec hp-dark" id="area">
    <div class="wrap hp-cols">
      <div>
        <p class="eyebrow">Service area</p>
        <h2>{esc(m["area_h2"])}</h2>
        <p>{p.inline(sections["area"])}</p>
        {p.link("service-areas", "See all service areas", cls="btn btn-bronze")}
      </div>
      <ul class="hp-towns">
        <li><b>Yardley</b> <span>(home base)</span></li>
        {towns}
      </ul>
    </div>
  </section>

  <section class="hp-sec" id="reviews">
    <div class="wrap">
      {home_head("reviews")}
      <div class="hp-btns hp-center">{badges}</div>
    </div>
  </section>

  <section class="hp-sec hp-paper faq" id="faq">
    <div class="wrap">
      {home_head("faq", faq_intro)}
      <div class="faq-list">{faq_items}</div>
    </div>
  </section>'''
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
# Wix build guide for the homepage (WIX-HOMEPAGE.md), from the same content
# ----------------------------------------------------------------------------
def wix_guide(site):
    m = site.pages["home"]["meta"]
    main_md, faqs = split_faq(site.pages["home"]["body"])
    sec = {}
    for chunk in re.split(r"^#### ", main_md, flags=re.M)[1:]:
        k, _, v = chunk.partition("\n")
        sec[k.strip()] = v.strip()

    def plain(s):
        """Markdown-lite → text a person can paste, with links shown as 'text' → /url/."""
        s = re.sub(r"\[([^\]]+)\]\(@([\w-]+)\)", lambda x: f"{x.group(1)} (link → `{site.resolve(x.group(2))}`)", s)
        return s.replace("**", "")

    def quote(s):
        return "\n".join("> " + line if line else ">" for line in plain(s).split("\n"))

    def head(key, intro=None):
        label, h2, text = HOME_HEADS[key]
        return (f"- **Label:** {label}\n- **Heading (H2):** {h2}\n"
                f"- **Intro:** {plain(intro or text)}\n")

    def svc_link(slug):
        return f"[{site.services[slug]['meta']['name']}] → `{site.services[slug]['path']}`"

    out = [f"""# Rebuilding the Homepage in Wix

Generated by `build.py` from the same content as the coded site, so the copy
here always matches it. Rebuild with `python3 build.py` after editing
`content/pages.txt`.

The homepage is built only from things the Wix Editor has out of the box:
full-width **strips** (sections), **columns**, **boxes**, **text**, **buttons**,
**images**, a **repeater**, **Wix Forms** and the **Wix FAQ** app (or collapsible
text). No custom code is needed for the page itself.

## 1. Site theme (set once: Site Design → Colors / Text)

| Colour | Hex | Used for |
|---|---|---|
| Bronze | `#AE9B6C` | Header bar, CTA strip |
| Brown | `#6E5A32` | Buttons, labels, highlighted heading words, step numbers |
| Light bronze | `#CBB98B` | Labels and figures on black |
| Black | `#0F0F0F` | Credentials strip, service-area strip, footer |
| Paper | `#F5F5F3` | Alternate light strips |
| White | `#FFFFFF` | Page and card backgrounds |
| Ink | `#141414` | Headings |
| Body grey | `#4A4845` | Paragraph text |
| Line grey | `#DCDBD8` | Card borders, dividers |
| Silver | `#C4C6C9` | Body text on black |

Font: **Barlow** everywhere (add it from Wix's font list → Upload/Google fonts if it isn't listed).

| Wix text style | Size desktop / mobile | Weight | Notes |
|---|---|---|---|
| Heading 1 | 50 / 34 px | SemiBold 600 | Hero only. Line height 1.1 |
| Heading 2 | 44 / 30 px | SemiBold 600 | Section headings |
| Heading 3 | 24 / 22 px | SemiBold 600 | Card titles (see the SEO note below) |
| Label | 13 px | SemiBold 600 | ALL CAPS, letter spacing 0.14 em, colour Brown |
| Paragraph 1 | 18 px | Regular 400 | Intros, About copy. Line height 1.6 |
| Paragraph 2 | 16 px | Regular 400 | Card text |

**SEO note:** the card titles in "What we do" and "Popular services" must be real **H2** tags
(the playbook wants each prominent service as its own H2). In Wix, style them with the
Heading 3 look, then set the tag to H2 in the text's SEO settings. Only the hero headline is an H1.

**Buttons** (save both as Wix button presets)
- **Primary:** fill Brown `#6E5A32`, white text, Barlow Bold 16 px, corner radius 6 px, height 48 px. Hover fill `#574625`.
- **Outline:** white fill, 2 px Ink border, Ink text, same size. Hover: Ink fill, white text.

**Layout:** content width 1200 px. Every strip has the same top and bottom padding, 96 px desktop / 56 px mobile.
Cards: white, 1 px Line-grey border, radius 12 px, 24 px inner padding, 24 px gap between cards.

## 2. Header and footer (shared on every page)

- **Top bar** (black strip, 36 px tall): left "Serving Yardley & Bucks County homes and businesses"; right "Licensed & insured · Master electrician · Yardley, PA". Silver 14 px text.
- **Header** (Bronze strip, 72 px, *freeze header* on): logo left; menu in white 16 px SemiBold: a **Services** dropdown title (no page) holding the three category pages, then Service Areas, About, Contact; "CALL OR TEXT / {C.PHONE_DISPLAY}" in white (link `tel:{C.PHONE_E164}`); white button "Free estimate" with Brown text, linked to the form anchor.
- **CTA strip** above the footer (Bronze): H2 "Need an Electrician You Can Trust?" (white) on the left; on the right "CALL OR TEXT" label, the phone number at 56 px white Bold (phone link), and a white button "Or request an estimate online".
- **Footer** (black): a Wix **Google Maps** element across the top on the homepage only (use the Business Profile address). Below it, four columns: logo + "Licensed, insured electricians serving Yardley and the Greater Bucks County area for over 40 years." | Services (the 3 category pages) | Company (About, Service Areas, Contact) | Contact (NAP exactly as on the Business Profile: {C.NAME}, {C.STREET}, {C.CITY}, {C.REGION} {C.POSTAL}, {C.PHONE_DISPLAY}).
- **Mobile:** add Wix's *Quick Action Bar* with Call and an estimate link.

## 3. Homepage, strip by strip

Page SEO (Page → SEO basics):
- **Title tag:** {m["title"]}
- **Meta description:** {m["desc"]}
- **URL:** `/` (homepage)
"""]

    out.append(f"""### Strip 1. Hero (anchor: `top`)

- **Background:** image `assets/img/electrician-panel-yardley-hero.jpg`, focal point right of centre, with a **white colour overlay at 84 % opacity** (Strip background → Settings → Overlay). If your editor has no overlay option, put a full-size white box at 84 % opacity behind the content.
- **Layout:** 2 columns, 55 / 45, vertically centred.
- **Left column**
  - Label: Only electrical, for 40+ years
  - **H1:** {m["h1"]} *Not Your Neighborhood Handyman.* (colour the second sentence Brown)
  - Paragraph 1: {plain(sec["lede"])}
  - Buttons: **Primary** "Get a free estimate" → form anchor; **Outline** "Call {C.PHONE_DISPLAY}" → `tel:{C.PHONE_E164}`
- **Right column:** a white box (radius 12 px, light shadow) holding a **Wix Form** set as the anchor `estimate`:
  - Heading: Request a Free Estimate. Sub-text: Takes about 30 seconds. We reply within one business day.
  - Fields: *What do you need?* (dropdown: Repair or upgrade / Installation / Lighting / Something else), *Name* (required), *Phone* (required), *Town*, *Details (optional)* (long text)
  - Submit button (Primary, full width): Send my request
  - Note under it: Prefer to talk? Call {C.PHONE_DISPLAY}
  - Success message: Thanks! We'll call you within one business day.
  - Send submissions to Joe's email and phone (Wix Forms → Automations).
- **Mobile:** the columns stack: text first, then the form.

### Strip 2. Credentials (black)

4 equal columns, centred text, 28 px top and bottom padding. Mobile: 2 × 2.

| Big line (24 px SemiBold, Light bronze) | Small line (15 px, Silver) |
|---|---|
""")
    out.append("".join(f"| {a} | {b} |\n" for a, b in HOME_CREDS))

    cards = ""
    for key in ("g", "i", "l"):
        cat = C.CATEGORIES[key]
        feat = [x.strip() for x in m[f"featured_{key}"].split(",")]
        n = len(site.cat_services(key))
        cards += (f"\n**Card: {cat['name']}**\n"
                  f"- Image: `assets/img/jobs/{PH.CATEGORY_PHOTOS[key]}.jpg` (4:3 crop)\n"
                  f"- Label: {cat['tag']}\n- **H2:** {cat['name']}\n"
                  f"- Text: {plain(sec['cat_' + key])}\n"
                  f"- Link list (each a text link, 1 px divider between): " + "; ".join(svc_link(s) for s in feat) + "\n"
                  f"- Button (Primary): See all {n} services → `/{cat['slug']}/`\n")
    out.append(f"""
### Strip 3. What we do (white, anchor: `services`)

Centred heading block (max width 760 px):
{head("services", sec["services_intro"])}
Then **3 cards in a row** (mobile: stacked), all the same height:
{cards}""")

    pop = ""
    for item in m["popular"].split(";"):
        slug, _, anchor = item.strip().partition("=")
        sv = site.services[slug]
        entry = PH.SERVICE_PHOTOS.get(slug)
        photo = entry[0] if isinstance(entry, tuple) else entry
        pop += (f"| `{photo}.jpg` | {sv['meta']['name']} | {sv['meta']['blurb']} | {anchor} → | `{sv['path']}` |\n")
    out.append(f"""
### Strip 4. Popular services (paper, anchor: `popular`)

Centred heading block:
{head("popular")}
Then a **repeater** (or 6 boxes), 3 per row on desktop, 2 on tablet, 1 on mobile. Each card: image (4:3) on top, then the
title as an **H2** styled Heading 3, the text in Paragraph 2, and a Brown bold text link at the bottom.

| Image (`assets/img/jobs/`) | Title (H2) | Text | Link text | Links to |
|---|---|---|---|---|
{pop}""")

    about_a, about_b = m["about_h2"].split("|")
    out.append(f"""
### Strip 5. About (white, anchor: `about`)

2 columns, 50 / 50, vertically centred. Mobile: text first, photo below.
- **Left:** Label "About us"; **H2** "{about_a} *{about_b}*" (second part in Brown); then Paragraph 1:

{quote(sec["about"])}

  (Bold the phrase "it's always Abie and I showing up at your door".) Then a Primary button "Free Diagnosis & Quote" → form anchor.
- **Right:** image `assets/img/ryan-huck-electrician-ladder.jpg`, 4:5 crop, radius 12 px.
  Alt text: Ryan Huck, head electrician at Joe Huck Electric, on a job in a Bucks County home

### Strip 6. Meet the Local Team (paper, anchor: `team`)

Centred heading block:
{head("team")}
Then 2 columns (max width 840 px, centred; mobile: stacked). Each: photo (4:5, radius 12 px), then the name centred
(22 px SemiBold) with the role under it in Brown.
""")
    out.append("".join(f"- `{t['img'].lstrip('/')}`: **{t['full']}**, {t['role']}\n" for t in TEAM))
    out.append(f"\nBelow, centred Paragraph 1: {TEAM_NOTE}\n")

    out.append(f"""
### Strip 7. How a job works (white, anchor: `process`)

Centred heading block:
{head("process")}
Then **4 boxes in a row** (tablet 2 × 2, mobile stacked). Each box: a 44 px Brown circle with the white step number, an H3, and Paragraph 2.

| # | Heading (H3) | Text |
|---|---|---|
""")
    out.append("".join(f"| {i} | {h} | {t} |\n" for i, (h, t) in enumerate(HOME_STEPS, 1)))

    towns = "\n".join(f"  - {site.areas[s]['meta']['town']} → `{site.areas[s]['path']}`" if s in site.areas else f"  - {s} (no page, plain text)"
                       for s in town_list(site))
    out.append(f"""
### Strip 8. Service area (black, anchor: `area`)

2 columns, 50 / 50. Mobile: stacked.
- **Left:** Label "Service area" (Light bronze); **H2** "{m["area_h2"]}" (white); paragraph (Silver): {plain(sec["area"])}
  Then a Primary button "See all service areas" → `{AREA_PREFIX}`.
- **Right:** the town links in **3 columns** (mobile 2), white SemiBold 16 px, a faint divider under each.
  First item "Yardley (home base)" (no link, it's this page). Then every service-area page:
{towns}

### Strip 9. Reputation (white, anchor: `reviews`)

Centred heading block:
{head("reviews")}
Then 3 Outline buttons in a centred row, each opening in a new tab:
- Nextdoor ↗ → {C.SAME_AS[1]}
- HomeAdvisor ↗ → {C.SAME_AS[2]}
- Facebook ↗ → {C.SAME_AS[0]}

### Strip 10. FAQ (paper, anchor: `faq`)

Centred heading block:
- **Label:** {HOME_HEADS["faq"][0]}
- **Heading (H2):** {HOME_HEADS["faq"][1]}
- **Intro:** {HOME_HEADS["faq"][2]} (make the number a phone link)

Then the **Wix FAQ** app (or one collapsible text per question), max width 860 px, centred, first question open:
""")
    out.append("".join(f"\n**Q: {q}**\nA: {plain(a)}\n" for q, a in faqs))

    schema = [business_schema(site), {"@type": "WebSite", "name": C.NAME, "url": C.DOMAIN + "/"}, faq_schema(faqs)]
    out.append(f"""
## 4. Things Wix needs set by hand

1. **Structured data:** Page → SEO → Advanced SEO → Structured data markup → add the JSON-LD below. Turn off any
   default Wix markup that duplicates it, or the business ends up described twice.
2. **Redirects:** add each line of `public/_redirects` in Marketing & SEO → SEO → URL Redirect Manager (301).
3. **Images:** set each image's alt text to the one in this guide or in `content/photos.py`.
4. **Heading tags:** check there's exactly one H1 (the hero headline), and that every card title is an H2.
5. **Google Business Profile:** use `{C.DOMAIN}/contact/` (or the homepage) as the booking link, and keep the NAP identical.

```json
{json.dumps({"@context": "https://schema.org", "@graph": schema}, ensure_ascii=False, indent=1)}
```
""")
    return "".join(out)



# ----------------------------------------------------------------------------
# Wix CMS export: one CSV row per service / area page (wix/*.csv)
# ----------------------------------------------------------------------------
def wix_url(site, path):
    """Coded-site path -> the URL the page will have in Wix."""
    for sv in site.services.values():
        if sv["path"] == path:
            return f"/services/{sv['slug']}"
    for a in site.areas.values():
        if a["path"] == path:
            return f"/service-areas/{a['slug']}-pa"
    return path.rstrip("/") or "/"


class WixPage(Page):
    def href(self, target):
        if target.startswith(("http", "#", "tel:", "mailto:")):
            return target
        return wix_url(self.site, target)


def wix_html(p, md_text):
    html = p.md(md_text)
    html = re.sub(r"<li><span>(.*?)</span></li>", r"<li>\1</li>", html)
    return html


def wix_export(site):
    out_dir = ROOT / "wix"
    out_dir.mkdir(exist_ok=True)

    def split_signs(md_text):
        m = re.search(r"(?ms)^:::signs\s*\n## (.+?)\n(.*?)^:::\s*$", md_text)
        if not m:
            return "", [], md_text
        items = [l[2:].strip() for l in m.group(2).splitlines() if l.startswith("- ")]
        return m.group(1).strip(), items, (md_text[:m.start()] + md_text[m.end():]).strip()

    def faq_html(p, faqs):
        return "".join(f"<h3>{esc(q)}</h3><p>{p.inline(a)}</p>" for q, a in faqs)

    def faq_json(p, faqs):
        return json.dumps(faq_schema(faqs), ensure_ascii=False) if faqs else ""

    rows = []
    for slug in site.svc_order:
        sv = site.services[slug]; m = sv["meta"]; cat = C.CATEGORIES[m["cat"]]
        p = WixPage(site, sv["path"])
        main_md, faqs = split_faq(sv["body"])
        intro, _, rest = main_md.partition("\n\n")
        signs_title, signs, body = split_signs(rest)
        rel = []
        for r in (site.canonical(x.strip()) for x in m["related"].split(",")):
            if r in site.services and r != slug and r not in rel:
                rel.append(r)
        rel += [x for x in site.svc_order if site.services[x]["meta"]["cat"] == m["cat"] and x != slug and x not in rel][:max(0, 3 - len(rel))]
        photo = PH.SERVICE_PHOTOS.get(slug)
        photo_name = (photo[0] if isinstance(photo, tuple) else photo) if photo else ""
        row = {
            "title": m["name"], "slug": slug, "category": cat["name"], "categoryPage": "/" + cat["slug"],
            "h1": m["h1"], "seoTitle": m["title"], "seoDescription": m["desc"],
            "intro": re.sub(r"<[^>]+>", "", p.inline(intro)), "summary": m["blurb"],
            "image": f"{photo_name}.jpg" if photo_name else "", "imageAlt": PH.PHOTOS[photo_name][0] if photo_name else "",
            "signsTitle": signs_title, "signsList": "<ul>" + "".join(f"<li>{p.inline(x)}</li>" for x in signs) + "</ul>" if signs else "",
            "body": wix_html(p, body), "faq": faq_html(p, faqs), "faqSchema": faq_json(p, faqs),
            "gbpServices": m.get("gbp", m["name"]),
        }
        for i, r in enumerate(rel[:3], 1):
            rs = site.services[r]
            row[f"related{i}Title"] = rs["meta"]["name"]; row[f"related{i}Text"] = rs["meta"]["blurb"]; row[f"related{i}Url"] = wix_url(site, rs["path"])
        rows.append(row)
    write_csv(out_dir / "services.csv", rows)

    rows = []
    for slug in site.area_order:
        a = site.areas[slug]; m = a["meta"]
        p = WixPage(site, a["path"])
        main_md, faqs = split_faq(a["body"])
        intro, _, rest = main_md.partition("\n\n")
        row = {
            "title": m["town"], "slug": f"{slug}-pa", "region": {"lower": "Near Yardley", "central": "Central Bucks", "upper": "Upper Bucks"}[m["region"]],
            "h1": m["h1"], "seoTitle": m["title"], "seoDescription": m["desc"],
            "intro": re.sub(r"<[^>]+>", "", p.inline(intro)), "summary": m["blurb"],
            "body": wix_html(p, rest), "faq": faq_html(p, faqs), "faqSchema": faq_json(p, faqs),
        }
        for i, n in enumerate([x.strip() for x in m["nearby"].split(",")][:3], 1):
            na = site.areas[n]
            row[f"nearby{i}Title"] = na["meta"]["town"] + ", PA"; row[f"nearby{i}Text"] = na["meta"]["blurb"]; row[f"nearby{i}Url"] = wix_url(site, na["path"])
        rows.append(row)
    write_csv(out_dir / "service-areas.csv", rows)

    # 301s for the Wix URL Redirect Manager: the old site's URLs -> the new Wix pages
    with open(out_dir / "redirects.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["Old URL", "New URL"])
        for old, new in C.REDIRECTS.items():
            w.writerow([old, wix_url(site, new)])


def write_csv(path, rows):
    keys = []
    for r in rows:
        keys += [k for k in r if k not in keys]
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)

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
    shutil.copy(ROOT / "site" / "assets" / "favicon" / "favicon.ico", out_dir / "favicon.ico")

    write(out_dir, "/", build_home(site))
    for key in ("g", "i", "l"):
        write(out_dir, f"/{C.CATEGORIES[key]['slug']}/", build_hub(site, key))
    for slug in site.svc_order:
        write(out_dir, site.services[slug]["path"], build_service(site, site.services[slug]))
    for slug in site.area_order:
        write(out_dir, site.areas[slug]["path"], build_area(site, site.areas[slug]))
    write(out_dir, AREA_PREFIX, build_simple(site, "service-areas", AREA_PREFIX, "areas", areas_index_extra(site)))
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
            for key, names in C.HUB_GBP.items():
                hub = C.CATEGORIES[key]
                for name in names:
                    w.writerow([hub["name"], name, site.pages[hub["slug"]]["body"].partition("\n\n")[0][:299], C.DOMAIN + "/" + hub["slug"] + "/"])
            for slug in site.svc_order:
                s = site.services[slug]
                for name in s["meta"].get("gbp", s["meta"]["name"]).split(";"):
                    w.writerow([C.CATEGORIES[s["meta"]["cat"]]["name"], name.strip(), s["meta"]["blurb"], C.DOMAIN + s["path"]])
                # services listed under a second GBP category point to the same page
                for key in C.GBP_ALSO.get(slug, []):
                    w.writerow([C.CATEGORIES[key]["name"], s["meta"].get("gbp", s["meta"]["name"]).split(";")[0].strip(), s["meta"]["blurb"], C.DOMAIN + s["path"]])

        (ROOT / "WIX-HOMEPAGE.md").write_text(wix_guide(site), encoding="utf-8")
        wix_export(site)

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
