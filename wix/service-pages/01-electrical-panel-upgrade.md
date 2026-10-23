# Electrical Panel Upgrade: Wix Build Sheet

This sheet has everything for building this page by hand in Wix: the
settings, the layout of each strip with sizes and colours, and every word of
copy in the order it appears. Build this page first. Every other service page
has the same layout, so you'll duplicate this one for the other 21 (see the
last section).

Open the coded preview of this page alongside: it's the visual reference.

**Before you start:** the homepage should already exist, because you'll copy
three things from it: the estimate form, the "How a job works" strip and the
button styles. Put the bronze **"Need an Electrician You Can Trust?"** band in
the **site footer** (above the black footer) if it isn't there already; then
it appears on every page automatically and you never build it again.

## Page settings

Pages panel → **+ Add Page** → Blank. Then ⋯ → **Settings** for each tab below.

| Setting | Value |
|---|---|
| Page name | Electrical Panel Upgrade |
| Show in menu | **No** (people reach it from the Electrician page and the homepage) |
| URL slug (SEO basics) | `electrical-panel-upgrade`, so the address is `/electrical-panel-upgrade` |
| Title tag | Electrical Panel Upgrade in Yardley, PA \| 200 Amp Upgrades in Bucks County |
| Meta description | Electrical panel and service upgrades in Yardley, PA. 100A to 200A upgrades, PECO coordination, permits and inspection by licensed electricians. Free estimates. |
| Let search engines index this page | On |
| Social share image | `older-panel-wiring.jpg` |

## Strip 1: Hero

**Layout:** section background paper `#F5F5F3`, 72px space above and below.
Two columns: text on the left (about 640px wide), the estimate form on the right
(about 520px wide), with 72px between them, vertically centred.

**Build it:**
1. Add a blank section. Set its background to `#F5F5F3`.
2. **Breadcrumb:** a text box, 14px Barlow Regular, `#4A4845`, with the links below in brown `#6E5A32`.
3. **Label:** 13px Barlow SemiBold, all caps, letter spacing 0.14em, `#6E5A32`, 14px below the breadcrumb.
4. **H1:** your Heading 1 style, 48px Barlow SemiBold, `#141414`, 14px below the label. Make sure its HTML tag is **H1**: this is the page's only H1.
5. **Intro:** 20px Barlow Regular, `#4A4845`, about 18px below the H1.
6. **Buttons**, 26px below the intro: Primary "Get a free estimate" linked to the form's anchor (step 8), then Outline "Call 215-906-4634" linked to phone `+12159064634`.
7. **Trust line**, 22px below the buttons: 14px Barlow Regular, `#4A4845`.
8. **Form:** copy the estimate form box from the homepage hero and paste it in the right column. Add an anchor just above it (Add → Menu & Anchor → Anchor) named `estimate`.

| Element | Copy |
|---|---|
| Breadcrumb | Home / Electrician / Electrical Panel Upgrade (link "Home" → Home page; "Electrician" → Electrician page; the last part is plain text) |
| Label | ELECTRICIAN |
| H1 | Electrical Panel Upgrade in Yardley, PA |
| Intro | If your breakers trip when two things run at once, or you're planning an EV charger, a heat pump or a finished basement, your panel may be the bottleneck. We upgrade panels and electrical services for Yardley homes every week, from the permit to the final inspection. |
| Buttons | Get a free estimate · Call 215-906-4634 |
| Trust line | Licensed & insured · Only electrical, 40+ years · Free written estimates |
| Form | Copied from the homepage (title "Request a Free Estimate" is plain bold text, not a heading) |

## Strip 2: Why us band

Copy the black "why us" section from any page where you've built it (or build it once using the directions you have for it) and paste it directly under the hero. Nothing on it changes from page to page.

## Strip 3: Article

**Layout:** white section, 96px space above and below. Everything sits in **one
centred column 760px wide** (x = 220 inside the 1,200px content area). Use one
text box per section below, so each is easy to space and to replace later.

**Build it:**
1. **Photo** (if the page has one): Add → Image, **760 × 570** (4:3), corners 12px, alt text as below.
2. **Signs box**, 30px below the photo: a Container Box 760 wide, fill `#F5F5F3`, 1px border `#DCDBD8`, corners 10px. Inside it, 24px padding:
   - the box title: Heading style 22px SemiBold, HTML tag **H2**;
   - a bulleted list, 18px Regular, `#4A4845`, 10px between items.
3. **Sections**, 26px below the box: one text box per section, 760 wide. In each box, the first line uses your **Heading 2** style (32px SemiBold, tag **H2**) and the paragraphs use Paragraph 1 (18px Regular, `#4A4845`, line height 1.6). Leave 48px above each section's heading.
4. **Links:** highlight the words shown under each section and use the link button to link them to the page named. Links are brown `#6E5A32`, SemiBold, underlined.

**Photo:** `site/assets/img/jobs/older-panel-wiring.jpg`  
**Alt text:** Ryan Huck working in a full residential electrical panel

**Signs box**

- **H2:** Signs You Need a Panel Upgrade
- Bulleted list:

> - Breakers trip when the microwave and toaster run together
> - You have a 60 or 100 amp service and want to add major appliances
> - The panel is warm, buzzing, rusty or smells like burning plastic
> - There are no open slots, or the panel is full of tandem breakers
> - It's a Federal Pacific Stab-Lok or Zinsco panel
> - Your home insurer or home inspector flagged the panel

**Section 1**

- **H2:** What a Panel Upgrade Involves
- Paragraph:

> Most upgrades in older Yardley homes go from 100 amps to 200 amps. That usually means a new panel, new service entrance cable, a new meter base when the utility requires it, and updated grounding and bonding. We pull the permit with your township, schedule the disconnect and reconnect with PECO, and book the inspection.

- Paragraph:

> On the day of the swap, your power is off for part of the day. We move every circuit to the new panel, replace any breakers that are damaged or wrong for the wire size, and add the protection current code requires. Before we leave, every breaker gets a clear, typed label, so you know what each one controls.

- Paragraph:

> Sometimes a full upgrade isn't needed. If your service is big enough but the panel is out of space, a subpanel may solve the problem for less. If you still have fuses, see our page on fuse box replacement. We'll tell you which option actually fits your house.

- Links in this section:
  - Link **"subpanel"** → Electrical Subpanel Installation page
  - Link **"fuse box replacement"** → Fuse Box Replacement page

**Section 2**

- **H2:** What Affects the Cost
- Paragraph:

> The price depends on the size of the new service, whether the meter base and service cable need replacing, where the panel sits in the house, and how many circuits need new breakers or repairs. Moving the panel to a new location costs more than a same-spot swap. Your written estimate spells out all of it before any work starts, so there are no surprises on the invoice.


**Section 3**

- **H2:** Breaker Replacement
- Paragraph:

> A breaker that trips for no reason, feels hot or won't reset is telling you something. We find out why it failed first, whether that's a loose connection, an overloaded circuit or a breaker that's simply worn out, then replace it with the breaker your panel is listed for, not just one that fits. Mismatched breakers are one of the most common problems we find in older Bucks County panels.


**Section 4**

- **H2:** AFCI Breakers
- Paragraph:

> Arc-fault (AFCI) breakers detect the kind of sparking that starts fires inside walls. Current code requires them on most living-space circuits, so we add them during panel upgrades and remodels. If an AFCI keeps tripping, there's usually a real cause, like a damaged cable or a loose connection, and we track it down instead of swapping in a standard breaker.


**Section 5**

- **H2:** Panel Upgrades Around Yardley
- Paragraph:

> A lot of our panel work is in the 1950s and 1960s homes of Levittown and Feasterville, where the original services were never sized for today's appliances. We also upgrade panels in the historic homes of Doylestown, and coordinate with the borough utility on upgrades in Quakertown.

- Links in this section:
  - Link **"Levittown"** → Levittown page
  - Link **"Feasterville"** → Feasterville page
  - Link **"Doylestown"** → Doylestown page

## Strip 4: Related services

**Layout:** paper `#F5F5F3` section, 96px space above and below.
Centred heading block (max 760px wide), 48px gap, then **3 white cards in a row**,
each **384px wide** with 24px gaps (x = 0, 408, 816): fill white, 1px border
`#DCDBD8`, corners 12px, 24px padding. Inside each card: title (Heading 3 look,
22px SemiBold, tag **H3**), text (16px Regular, `#4A4845`), then a text link
"Learn more →" (16px Bold, `#6E5A32`). Make all three cards the same height.
Below the cards, 32px down, a centred **Outline** button.

| Element | Copy | Links to |
|---|---|---|
| Label | RELATED | |
| Heading (H2) | Related Services | |
| Card: title (H3) | Electrical Subpanel Installation | |
| Card: text | Add circuits where you need them with a subpanel for a garage, basement, addition or workshop. We check your service capacity first, size the feeder properly and handle the permit and inspection. | |
| Card: link | Learn more → | Electrical Subpanel Installation page |
| Card: title (H3) | Fuse Box Replacement | |
| Card: text | Replace an old fuse box with a modern circuit breaker panel, or get a blown fuse changed safely. We make sure every fuse is the right size for its wire and upgrade the service when it's due. | |
| Card: link | Learn more → | Fuse Box Replacement page |
| Card: title (H3) | Whole House Surge Protection | |
| Card: text | A surge protector installed at your electrical panel protects everything in the house, from the furnace and fridge to TVs and computers, against surges from lightning, the utility and your own large appliances. | |
| Card: link | Learn more → | Whole House Surge Protection page |
| Button | See all 14 electrician services | Electrician page |

## Strip 5: How a job works

Copy the **"How a job works"** section from the homepage and paste it here. Change only the heading and the intro line:

| Element | Copy |
|---|---|
| Label | HOW A JOB WORKS |
| Heading (H2) | What Happens When You Call |
| Intro | The same four steps on every job, from a single outlet to a full panel upgrade. |
| 4 boxes | Unchanged from the homepage (titles are H3) |

## Strip 6: Questions

**Layout:** paper `#F5F5F3` section, 96px space above and below. Centred heading block,
48px gap, then **one text box 760 wide, centred**. In it, each question uses a
**Heading 3** style (20px SemiBold, tag **H3**) with its answer below in Paragraph 1
(18px Regular, `#4A4845`). Leave 28px above each question.

| Element | Copy |
|---|---|
| Label | QUESTIONS |
| Heading (H2) | Good to Know |
| Intro | Still have a question? Call 215-906-4634. You'll talk to an electrician, not a call center. (link the number to phone `+12159064634`) |

- **H3:** How long does a panel upgrade take?

> The work itself is usually done in one day, with the power off for part of it. Scheduling the PECO reconnect and the inspection can add a few days on either side.

- **H3:** Do I need a permit to replace my electrical panel?

> Yes. A panel or service upgrade always needs a permit and an inspection in Pennsylvania. We pull the permit and meet the inspector for you.

- **H3:** Is a 200 amp service enough for an EV charger?

> In most homes, yes. We run a load calculation first to confirm there's room for the charger along with your heating, cooking and other large loads.

## Structured data (SEO)

Page ⋯ → **SEO basics → Advanced SEO → Structured data markup → Add new markup**, and paste this. It tells Google what the service is, where the page sits, and its questions and answers.

```json
{
 "@context": "https://schema.org",
 "@graph": [
  {
   "@type": "Service",
   "name": "Electrical Panel Upgrade",
   "serviceType": "Electrical Panel Upgrade",
   "description": "Replace an outdated or overloaded electrical panel with a modern 200-amp service. We handle the permit, the PECO disconnect and reconnect, the inspection, and label every circuit when we're done.",
   "provider": {
    "@id": "https://www.joehuckelectric.com/#business"
   },
   "areaServed": [
    {
     "@type": "City",
     "name": "Yardley, PA"
    },
    {
     "@type": "City",
     "name": "Newtown, PA"
    },
    {
     "@type": "City",
     "name": "Washington Crossing, PA"
    },
    {
     "@type": "City",
     "name": "New Hope, PA"
    },
    {
     "@type": "City",
     "name": "Langhorne, PA"
    },
    {
     "@type": "City",
     "name": "Levittown, PA"
    },
    {
     "@type": "City",
     "name": "Fairless Hills, PA"
    },
    {
     "@type": "City",
     "name": "Morrisville, PA"
    },
    {
     "@type": "City",
     "name": "Bristol, PA"
    },
    {
     "@type": "City",
     "name": "Bensalem, PA"
    },
    {
     "@type": "City",
     "name": "Feasterville, PA"
    },
    {
     "@type": "City",
     "name": "Warminster, PA"
    },
    {
     "@type": "City",
     "name": "Doylestown, PA"
    },
    {
     "@type": "AdministrativeArea",
     "name": "Bucks County, PA"
    }
   ],
   "url": "https://www.joehuckelectric.com/electrical-panel-upgrade"
  },
  {
   "@type": "BreadcrumbList",
   "itemListElement": [
    {
     "@type": "ListItem",
     "position": 1,
     "name": "Home",
     "item": "https://www.joehuckelectric.com/"
    },
    {
     "@type": "ListItem",
     "position": 2,
     "name": "Electrician",
     "item": "https://www.joehuckelectric.com/electrician-services"
    },
    {
     "@type": "ListItem",
     "position": 3,
     "name": "Electrical Panel Upgrade",
     "item": "https://www.joehuckelectric.com/electrical-panel-upgrade"
    }
   ]
  },
  {
   "@type": "FAQPage",
   "mainEntity": [
    {
     "@type": "Question",
     "name": "How long does a panel upgrade take?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "The work itself is usually done in one day, with the power off for part of it. Scheduling the PECO reconnect and the inspection can add a few days on either side."
     }
    },
    {
     "@type": "Question",
     "name": "Do I need a permit to replace my electrical panel?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "Yes. A panel or service upgrade always needs a permit and an inspection in Pennsylvania. We pull the permit and meet the inspector for you."
     }
    },
    {
     "@type": "Question",
     "name": "Is a 200 amp service enough for an EV charger?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "In most homes, yes. We run a load calculation first to confirm there's room for the charger along with your heating, cooking and other large loads."
     }
    }
   ]
  }
 ]
}
```

## Mobile

Switch to the mobile editor and check each strip:
- **Hero:** text first, then the form, both full width.
- **Article:** photo, box and text boxes full width with 16px side margins.
- **Related cards and step boxes:** stacked one per row, 16px apart.
- Text sizes: H1 about 32px, H2 about 26px, paragraphs 17px.

## Building the other 21 service pages

1. In the Pages panel, hover over this page → ⋯ → **Duplicate**.
2. Open that service's sheet in `wix/service-pages/` and work down it:
   - **Page settings:** rename the page, change the URL slug, title tag, meta description and social image.
   - **Hero:** breadcrumb, label, H1 and intro.
   - **Article:** swap the photo (or delete it if the sheet says there's none), the signs box, and each section's text. Add or delete section text boxes so the count matches the sheet, and redo the links.
   - **Related services:** the three cards and the button.
   - **Questions:** replace the questions and answers.
   - **Structured data:** delete the old markup and paste the new one.
3. Preview it, check it on mobile, and move to the next one.

Each duplicate takes roughly 20–30 minutes once you're used to it. If that
sounds like too much, the CMS route in `WIX-PAGES.md` builds all 22 from one
template and a spreadsheet import instead; the content is identical.
