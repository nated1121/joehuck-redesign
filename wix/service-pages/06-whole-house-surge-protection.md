# Whole House Surge Protection: Wix Build Sheet

Build this page by duplicating the **Electrical Panel Upgrade** page (see
`01-electrical-panel-upgrade.md`, last section), then replace the content
strip by strip with the copy below. The layout, sizes and colours don't change.

## Page settings

| Setting | Value |
|---|---|
| Page name | Whole House Surge Protection |
| Show in menu | **No** (people reach it from the Electrician page and the homepage) |
| URL slug (SEO basics) | `whole-house-surge-protection`, so the address is `/whole-house-surge-protection` |
| Title tag | Whole House Surge Protection in Yardley, PA \| Surge Protectors, Bucks County |
| Meta description | Whole house surge protector installation in Yardley, PA. Protect appliances, HVAC and electronics at the panel. Licensed electricians, free estimates. |
| Let search engines index this page | On |
| Social share image | Leave as the site default |

## Strip 1: Hero

| Element | Copy |
|---|---|
| Breadcrumb | Home / Electrician / Whole House Surge Protection (link "Home" → Home page; "Electrician" → Electrician page; the last part is plain text) |
| Label | ELECTRICIAN |
| H1 | Whole House Surge Protection in Yardley, PA |
| Intro | Plug-in power strips only protect what's plugged into them. A whole-house surge protector mounts at your electrical panel and protects every circuit, including the furnace, air conditioner, refrigerator, washer and all the electronics built into modern appliances. |
| Buttons | Get a free estimate · Call 215-906-4634 |
| Trust line | Licensed & insured · Only electrical, 40+ years · Free written estimates |
| Form | Copied from the homepage (title "Request a Free Estimate" is plain bold text, not a heading) |

## Strip 2: Why us band

Already there from the duplicate. Nothing changes.

## Strip 3: Article

**Photo:** none for this service. Leave the photo out and start the column with the signs box.

**Signs box**

- **H2:** Good Reasons to Add Surge Protection
- Bulleted list:

> - You've lost a TV, router, garage door opener or appliance board after a storm
> - Your home has expensive HVAC, a generator, solar or an EV charger
> - Lights briefly brighten or flicker when large appliances cycle
> - You're upgrading or replacing your panel
> - You work from home and rely on your computer and network

**Section 1**

- **H2:** Where Surges Come From
- Paragraph:

> Lightning gets the attention, but most surges start closer to home: utility switching, tree limbs on lines, and large motors in your own house turning on and off. Each surge wears on electronic circuit boards a little, which is why appliances sometimes die early for no clear reason. A panel-mounted protector diverts that excess voltage to ground before it reaches your circuits.


**Section 2**

- **H2:** How We Install It
- Paragraph:

> We install a surge protective device in or beside your panel on a dedicated breaker, keeping the leads as short as possible so it reacts fast. We check your grounding and bonding while we're there, because a surge protector is only as good as the ground it dumps energy into. If your grounding needs work, see our page on ground wire installation and repair.

- Paragraph:

> Newer editions of the electrical code require surge protection whenever a service is upgraded or replaced, so we include it in every panel upgrade. For the most protection, we recommend pairing the whole-house device with quality plug-in protectors for computers and home theaters.

- Links in this section:
  - Link **"ground wire installation and repair"** → Home Rewiring page
  - Link **"panel upgrade"** → Electrical Panel Upgrade page

**Section 3**

- **H2:** What Affects the Cost
- Paragraph:

> The protector's rating, your panel type and whether a breaker space is available all affect the price. Most installs take about an hour.


**Section 4**

- **H2:** Signs Your Home Has Been Hit by Surges
- Paragraph:

> Surge damage isn't always dramatic. Watch for electronics that fail after storms, garage door openers and furnace control boards that need replacing more often than they should, and LED bulbs that burn out early. Those are common signs of repeated small surges. A whole-house protector won't repair damage that's already happened, but it can prevent the next round.


**Section 5**

- **H2:** Surge Protection Around Yardley
- Paragraph:

> Homes near the river in New Hope and Washington Crossing, and anywhere with overhead lines through the trees, see more than their share of storm surges. We also add protection during panel upgrades in Chalfont.

- Links in this section:
  - Link **"New Hope"** → New Hope page
  - Link **"Washington Crossing"** → Washington Crossing page

## Strip 4: Related services

| Element | Copy | Links to |
|---|---|---|
| Label | RELATED | |
| Heading (H2) | Related Services | |
| Card: title (H3) | Electrical Panel Upgrade | |
| Card: text | Replace an outdated or overloaded electrical panel with a modern 200-amp service. We handle the permit, the PECO disconnect and reconnect, the inspection, and label every circuit when we're done. | |
| Card: link | Learn more → | Electrical Panel Upgrade page |
| Card: title (H3) | Electrical Subpanel Installation | |
| Card: text | Add circuits where you need them with a subpanel for a garage, basement, addition or workshop. We check your service capacity first, size the feeder properly and handle the permit and inspection. | |
| Card: link | Learn more → | Electrical Subpanel Installation page |
| Card: title (H3) | Fuse Box Replacement | |
| Card: text | Replace an old fuse box with a modern circuit breaker panel, or get a blown fuse changed safely. We make sure every fuse is the right size for its wire and upgrade the service when it's due. | |
| Card: link | Learn more → | Fuse Box Replacement page |
| Button | See all 14 electrician services | Electrician page |

## Strip 5: How a job works

Already there from the duplicate. Nothing changes.

## Strip 6: Questions

| Element | Copy |
|---|---|
| Label | QUESTIONS |
| Heading (H2) | Good to Know |
| Intro | Still have a question? Call 215-906-4634. You'll talk to an electrician, not a call center. (link the number to phone `+12159064634`) |

- **H3:** Does a whole-house surge protector stop lightning?

> Nothing stops a direct lightning strike. A surge protector handles the far more common surges from nearby strikes, the utility and your own appliances.

- **H3:** How long does a surge protector last?

> Most last many years, but they wear with each surge they absorb. Many models have an indicator light that shows when they need replacing.

- **H3:** Do I still need power strips?

> For computers and home theaters, a good plug-in protector adds a second layer. The whole-house unit protects everything else.

## Structured data (SEO)

Page ⋯ → **SEO basics → Advanced SEO → Structured data markup → Add new markup**, and paste this. It tells Google what the service is, where the page sits, and its questions and answers.

```json
{
 "@context": "https://schema.org",
 "@graph": [
  {
   "@type": "Service",
   "name": "Whole House Surge Protection",
   "serviceType": "Whole House Surge Protection",
   "description": "A surge protector installed at your electrical panel protects everything in the house, from the furnace and fridge to TVs and computers, against surges from lightning, the utility and your own large appliances.",
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
   "url": "https://www.joehuckelectric.com/whole-house-surge-protection"
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
     "name": "Whole House Surge Protection",
     "item": "https://www.joehuckelectric.com/whole-house-surge-protection"
    }
   ]
  },
  {
   "@type": "FAQPage",
   "mainEntity": [
    {
     "@type": "Question",
     "name": "Does a whole-house surge protector stop lightning?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "Nothing stops a direct lightning strike. A surge protector handles the far more common surges from nearby strikes, the utility and your own appliances."
     }
    },
    {
     "@type": "Question",
     "name": "How long does a surge protector last?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "Most last many years, but they wear with each surge they absorb. Many models have an indicator light that shows when they need replacing."
     }
    },
    {
     "@type": "Question",
     "name": "Do I still need power strips?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "For computers and home theaters, a good plug-in protector adds a second layer. The whole-house unit protects everything else."
     }
    }
   ]
  }
 ]
}
```

