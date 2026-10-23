# Electrical Repair & Troubleshooting: Wix Build Sheet

Build this page by duplicating the **Electrical Panel Upgrade** page (see
`01-electrical-panel-upgrade.md`, last section), then replace the content
strip by strip with the copy below. The layout, sizes and colours don't change.

## Page settings

| Setting | Value |
|---|---|
| Page name | Electrical Repair & Troubleshooting |
| Show in menu | **No** (people reach it from the Electrician page and the homepage) |
| URL slug (SEO basics) | `electrical-repair-troubleshooting`, so the address is `/electrical-repair-troubleshooting` |
| Title tag | Electrical Repair & Troubleshooting in Yardley, PA \| Bucks County Electrician |
| Meta description | Electrical repair and troubleshooting in Yardley, PA. Dead outlets, tripping breakers, flickering lights and buzzing switches found and fixed. |
| Let search engines index this page | On |
| Social share image | `outlet-troubleshooting.jpg` |

## Strip 1: Hero

| Element | Copy |
|---|---|
| Breadcrumb | Home / Electrician / Electrical Repair & Troubleshooting (link "Home" → Home page; "Electrician" → Electrician page; the last part is plain text) |
| Label | ELECTRICIAN |
| H1 | Electrical Repair & Troubleshooting in Yardley, PA |
| Intro | When part of your house loses power, a breaker won't stay on, or the lights flicker for no clear reason, you need someone who finds the cause, not someone who starts replacing parts. We troubleshoot and repair electrical problems in Yardley-area homes and small businesses every day. |
| Buttons | Get a free estimate · Call 215-906-4634 |
| Trust line | Licensed & insured · Only electrical, 40+ years · Free written estimates |
| Form | Copied from the homepage (title "Request a Free Estimate" is plain bold text, not a heading) |

## Strip 2: Why us band

Already there from the duplicate. Nothing changes.

## Strip 3: Article

**Photo:** `site/assets/img/jobs/outlet-troubleshooting.jpg`  
**Alt text:** Testing a kitchen outlet with a voltage tester to find a fault

**Signs box**

- **H2:** Problems We Fix Every Week
- Bulleted list:

> - Outlets or a whole room that suddenly stopped working
> - Breakers or GFCIs that trip and won't reset
> - Lights that flicker, dim or buzz
> - Switches or outlets that are warm, loose or crackle when used
> - A burning smell, scorch marks or a shock from a switch or appliance
> - Power that works on some outlets on a circuit but not others

**Section 1**

- **H2:** How We Troubleshoot
- Paragraph:

> Electrical problems follow the wiring, so we start at the panel and work outward. We test voltage and continuity, check each device on the affected circuit, and look for the usual suspects: a loose connection at a push-in "backstab" outlet, a tripped GFCI in another room that feeds the circuit, a failed splice in a junction box, or a nail through a cable. Once we find the fault, we explain it, give you the price to fix it and make the repair.

- Paragraph:

> If the problem is a worn breaker, see circuit breaker replacement. If it's worn or damaged devices, we replace switches and outlets. Flickering fixtures often have their own causes, covered on our lighting repair page.

- Links in this section:
  - Link **"circuit breaker replacement"** → Electrical Panel Upgrade page
  - Link **"replace switches and outlets"** → Switch & Outlet Installation page
  - Link **"lighting repair"** → Lighting Repair page

**Section 2**

- **H2:** When It Can't Wait
- Paragraph:

> Turn off the circuit at the panel and call right away if you see sparks or smoke, smell burning plastic, feel heat at a switch or outlet, or get a shock. Don't reset a breaker that trips immediately. Call 215-906-4634 and we'll tell you how to make things safe until we get there.

- Links in this section:
  - Link **"215-906-4634"** → Contact page

**Section 3**

- **H2:** What Affects the Cost
- Paragraph:

> Most repairs are straightforward once the problem is found. The time it takes to locate a fault, the parts involved and access to the wiring drive the price. We tell you what we found and what it costs before we fix it.


**Section 4**

- **H2:** Problems That Come Back
- Paragraph:

> If you've had the same breaker trip or the same outlet fail more than once, the earlier fix probably treated a symptom. We look for the root cause, such as a shared neutral, an overloaded circuit or a failing splice, so you don't have to call again.


**Section 5**

- **H2:** Repairs Around Yardley
- Paragraph:

> We handle repair calls across Morrisville, Bristol and Warminster, and for small businesses along the Route 1 and Street Road corridors.

- Links in this section:
  - Link **"Morrisville"** → Morrisville page
  - Link **"Bristol"** → Bristol page
  - Link **"Warminster"** → Warminster page

## Strip 4: Related services

| Element | Copy | Links to |
|---|---|---|
| Label | RELATED | |
| Heading (H2) | Related Services | |
| Card: title (H3) | Electrical Panel Upgrade | |
| Card: text | Replace an outdated or overloaded electrical panel with a modern 200-amp service. We handle the permit, the PECO disconnect and reconnect, the inspection, and label every circuit when we're done. | |
| Card: link | Learn more → | Electrical Panel Upgrade page |
| Card: title (H3) | Lighting Repair | |
| Card: text | Fix lights that flicker, buzz or won't turn on, replace failed ballasts and drivers, change bulbs in hard-to-reach fixtures, and repair outdoor and landscape lighting. | |
| Card: link | Learn more → | Lighting Repair page |
| Card: title (H3) | Switch & Outlet Installation | |
| Card: text | Add outlets where you need them and replace worn, loose, cracked or warm switches and outlets. We install USB and tamper-resistant outlets and fix the loose connections behind flickering switches. | |
| Card: link | Learn more → | Switch & Outlet Installation page |
| Button | See all 14 electrician services | Electrician page |

## Strip 5: How a job works

Already there from the duplicate. Nothing changes.

## Strip 6: Questions

| Element | Copy |
|---|---|
| Label | QUESTIONS |
| Heading (H2) | Good to Know |
| Intro | Still have a question? Call 215-906-4634. You'll talk to an electrician, not a call center. (link the number to phone `+12159064634`) |

- **H3:** Why did half the outlets in my room stop working?

> Often a tripped GFCI elsewhere on the circuit, or a loose connection at the last working outlet. We trace it and fix the connection.

- **H3:** Is a flickering light dangerous?

> A bulb or dimmer issue isn't, but flicker across several rooms can mean a loose connection at the panel or service. That needs a look soon.

- **H3:** Do you charge to diagnose the problem?

> No. Diagnosis and the quote are free. We find the problem, explain it and give you a written price before we fix anything.

## Structured data (SEO)

Page ⋯ → **SEO basics → Advanced SEO → Structured data markup → Add new markup**, and paste this. It tells Google what the service is, where the page sits, and its questions and answers.

```json
{
 "@context": "https://schema.org",
 "@graph": [
  {
   "@type": "Service",
   "name": "Electrical Repair & Troubleshooting",
   "serviceType": "Electrical Repair & Troubleshooting",
   "description": "Dead outlets, tripping breakers, flickering lights, buzzing switches and half-working circuits, tracked down methodically and fixed properly. We find the cause instead of guessing, and explain what we found.",
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
   "url": "https://www.joehuckelectric.com/electrical-repair-troubleshooting"
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
     "name": "Electrical Repair & Troubleshooting",
     "item": "https://www.joehuckelectric.com/electrical-repair-troubleshooting"
    }
   ]
  },
  {
   "@type": "FAQPage",
   "mainEntity": [
    {
     "@type": "Question",
     "name": "Why did half the outlets in my room stop working?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "Often a tripped GFCI elsewhere on the circuit, or a loose connection at the last working outlet. We trace it and fix the connection."
     }
    },
    {
     "@type": "Question",
     "name": "Is a flickering light dangerous?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "A bulb or dimmer issue isn't, but flicker across several rooms can mean a loose connection at the panel or service. That needs a look soon."
     }
    },
    {
     "@type": "Question",
     "name": "Do you charge to diagnose the problem?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "No. Diagnosis and the quote are free. We find the problem, explain it and give you a written price before we fix anything."
     }
    }
   ]
  }
 ]
}
```

