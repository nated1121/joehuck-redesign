# Fuse Box Replacement: Wix Build Sheet

Build this page by duplicating the **Electrical Panel Upgrade** page (see
`01-electrical-panel-upgrade.md`, last section), then replace the content
strip by strip with the copy below. The layout, sizes and colours don't change.

## Page settings

| Setting | Value |
|---|---|
| Page name | Fuse Box Replacement |
| Show in menu | **No** (people reach it from the Electrician page and the homepage) |
| URL slug (SEO basics) | `fuse-box-replacement`, so the address is `/fuse-box-replacement` |
| Title tag | Fuse Box Replacement in Yardley, PA \| Fuse Box Electrician in Bucks County |
| Meta description | Fuse box replacement and fuse changing in Yardley, PA. Convert an old fuse panel to a modern breaker panel with permits and inspection. Licensed electricians. |
| Let search engines index this page | On |
| Social share image | Leave as the site default |

## Strip 1: Hero

| Element | Copy |
|---|---|
| Breadcrumb | Home / Electrician / Fuse Box Replacement (link "Home" → Home page; "Electrician" → Electrician page; the last part is plain text) |
| Label | ELECTRICIAN |
| H1 | Fuse Box Replacement in Yardley, PA |
| Intro | Fuse boxes did their job for decades, but most can't handle a modern home's electrical load, and many insurers won't cover a house that still has one. We replace fuse boxes with breaker panels across Yardley, and we'll also change a blown fuse safely if that's all you need today. |
| Buttons | Get a free estimate · Call 215-906-4634 |
| Trust line | Licensed & insured · Only electrical, 40+ years · Free written estimates |
| Form | Copied from the homepage (title "Request a Free Estimate" is plain bold text, not a heading) |

## Strip 2: Why us band

Already there from the duplicate. Nothing changes.

## Strip 3: Article

**Photo:** none for this service. Leave the photo out and start the column with the signs box.

**Signs box**

- **H2:** Signs Your Fuse Box Needs Attention
- Bulleted list:

> - Fuses blow regularly, especially in the kitchen or when the AC starts
> - Someone has installed a larger fuse than the circuit's wire can handle
> - There are pennies or foil behind fuses, or the box shows scorch marks
> - Your insurance company or buyer's inspector flagged the fuse box
> - You want to add circuits, and there's no room left

**Section 1**

- **H2:** Changing a Blown Fuse the Right Way
- Paragraph:

> A fuse blows to protect the wire behind it. The most dangerous thing we find in older homes is a 20 or 30 amp fuse screwed into a socket meant for 15 amps, because the wire can overheat long before that fuse blows. When we change fuses, we match each one to its wire size and can install tamper-resistant Type S adapters so the wrong size can't go back in. If fuses keep blowing, that's a sign the circuit is overloaded, and the lasting fix is more circuits or a new panel.


**Section 2**

- **H2:** Replacing a Fuse Box With a Breaker Panel
- Paragraph:

> Most fuse boxes we replace are on 60 amp services, so the job is usually a full panel and service upgrade to 100 or 200 amps. We pull the permit, coordinate the PECO disconnect, install the new panel and service equipment, move each circuit to a properly sized breaker, and book the inspection. Homes with fuse boxes often have old wiring too, and we'll tell you honestly whether any of it needs rewiring.

- Links in this section:
  - Link **"panel and service upgrade"** → Electrical Panel Upgrade page
  - Link **"rewiring"** → Home Rewiring page

**Section 3**

- **H2:** What Affects the Cost
- Paragraph:

> A fuse box swap costs more than a breaker-panel swap because the service equipment usually has to change too. The size of the new service, the condition of the existing wiring and the number of circuits all affect the price. Your written estimate covers everything.


**Section 4**

- **H2:** What to Expect on Replacement Day
- Paragraph:

> Your power will be off for most of the day while we swap the equipment. We'll tell you in advance, so you can plan around refrigerators, medical devices and work from home, and we restore power as soon as the utility reconnects.


**Section 5**

- **H2:** Fuse Boxes Around Yardley
- Paragraph:

> We still find fuse boxes in older homes along Radcliffe Street in Bristol, in Morrisville twins and rowhomes, and in older borough homes in Sellersville and Perkasie.

- Links in this section:
  - Link **"Bristol"** → Bristol page
  - Link **"Morrisville"** → Morrisville page

## Strip 4: Related services

| Element | Copy | Links to |
|---|---|---|
| Label | RELATED | |
| Heading (H2) | Related Services | |
| Card: title (H3) | Electrical Panel Upgrade | |
| Card: text | Replace an outdated or overloaded electrical panel with a modern 200-amp service. We handle the permit, the PECO disconnect and reconnect, the inspection, and label every circuit when we're done. | |
| Card: link | Learn more → | Electrical Panel Upgrade page |
| Card: title (H3) | Home Rewiring | |
| Card: text | Replace knob-and-tube, cloth-insulated or ungrounded wiring in older homes, room by room or all at once. We fish new cable through existing walls wherever we can, so you get new wiring with as little patching as possible. | |
| Card: link | Learn more → | Home Rewiring page |
| Card: title (H3) | Electrical Subpanel Installation | |
| Card: text | Add circuits where you need them with a subpanel for a garage, basement, addition or workshop. We check your service capacity first, size the feeder properly and handle the permit and inspection. | |
| Card: link | Learn more → | Electrical Subpanel Installation page |
| Button | See all 14 electrician services | Electrician page |

## Strip 5: How a job works

Already there from the duplicate. Nothing changes.

## Strip 6: Questions

| Element | Copy |
|---|---|
| Label | QUESTIONS |
| Heading (H2) | Good to Know |
| Intro | Still have a question? Call 215-906-4634. You'll talk to an electrician, not a call center. (link the number to phone `+12159064634`) |

- **H3:** Is it safe to keep my fuse box?

> A fuse box with correctly sized fuses isn't dangerous by itself. The problems are oversized fuses, overloaded circuits and old wiring, which is why we inspect it before recommending anything.

- **H3:** Will my insurance company care about my fuse box?

> Many insurers charge more for homes with fuse boxes or won't write a policy at all. Replacing it usually solves that problem.

- **H3:** Can you just change a blown fuse?

> Yes. We'll replace it with the correct size and check why it blew, so you know whether the circuit needs more work.

## Structured data (SEO)

Page ⋯ → **SEO basics → Advanced SEO → Structured data markup → Add new markup**, and paste this. It tells Google what the service is, where the page sits, and its questions and answers.

```json
{
 "@context": "https://schema.org",
 "@graph": [
  {
   "@type": "Service",
   "name": "Fuse Box Replacement",
   "serviceType": "Fuse Box Replacement",
   "description": "Replace an old fuse box with a modern circuit breaker panel, or get a blown fuse changed safely. We make sure every fuse is the right size for its wire and upgrade the service when it's due.",
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
   "url": "https://www.joehuckelectric.com/fuse-box-replacement"
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
     "name": "Fuse Box Replacement",
     "item": "https://www.joehuckelectric.com/fuse-box-replacement"
    }
   ]
  },
  {
   "@type": "FAQPage",
   "mainEntity": [
    {
     "@type": "Question",
     "name": "Is it safe to keep my fuse box?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "A fuse box with correctly sized fuses isn't dangerous by itself. The problems are oversized fuses, overloaded circuits and old wiring, which is why we inspect it before recommending anything."
     }
    },
    {
     "@type": "Question",
     "name": "Will my insurance company care about my fuse box?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "Many insurers charge more for homes with fuse boxes or won't write a policy at all. Replacing it usually solves that problem."
     }
    },
    {
     "@type": "Question",
     "name": "Can you just change a blown fuse?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "Yes. We'll replace it with the correct size and check why it blew, so you know whether the circuit needs more work."
     }
    }
   ]
  }
 ]
}
```

