# Electrical Subpanel Installation: Wix Build Sheet

Build this page by duplicating the **Electrical Panel Upgrade** page (see
`01-electrical-panel-upgrade.md`, last section), then replace the content
strip by strip with the copy below. The layout, sizes and colours don't change.

## Page settings

| Setting | Value |
|---|---|
| Page name | Electrical Subpanel Installation |
| Show in menu | **No** (people reach it from the Electrician page and the homepage) |
| URL slug (SEO basics) | `electrical-subpanel-installation`, so the address is `/electrical-subpanel-installation` |
| Title tag | Electrical Subpanel Installation in Yardley, PA \| Subpanels in Bucks County |
| Meta description | Subpanel installation in Yardley, PA for garages, basements, additions and workshops. Load calculations, permits and clean installs by licensed electricians. |
| Let search engines index this page | On |
| Social share image | `new-breaker-panel.jpg` |

## Strip 1: Hero

| Element | Copy |
|---|---|
| Breadcrumb | Home / Electrician / Electrical Subpanel Installation (link "Home" → Home page; "Electrician" → Electrician page; the last part is plain text) |
| Label | ELECTRICIAN |
| H1 | Electrical Subpanel Installation in Yardley, PA |
| Intro | A subpanel gives you room for new circuits without replacing your main panel. It's the right fix when your service has enough capacity but the panel is out of space, or when a garage, basement or addition needs its own set of breakers close to where the power is used. |
| Buttons | Get a free estimate · Call 215-906-4634 |
| Trust line | Licensed & insured · Only electrical, 40+ years · Free written estimates |
| Form | Copied from the homepage (title "Request a Free Estimate" is plain bold text, not a heading) |

## Strip 2: Why us band

Already there from the duplicate. Nothing changes.

## Strip 3: Article

**Photo:** `site/assets/img/jobs/new-breaker-panel.jpg`  
**Alt text:** Ryan Huck wiring a new breaker panel in a Bucks County basement

**Signs box**

- **H2:** When a Subpanel Makes Sense
- Bulleted list:

> - Your main panel has no open slots, but your service isn't overloaded
> - You're finishing a basement and need several new circuits
> - A detached garage or workshop needs lights, outlets and tools
> - An addition is a long run from the main panel
> - You want space for a future EV charger or generator hookup

**Section 1**

- **H2:** How We Install a Subpanel
- Paragraph:

> We start with a load calculation. A subpanel adds space, not capacity, so if your service is already close to its limit, the honest answer may be a panel upgrade instead. When a subpanel fits, we choose its location, size the feeder cable and breaker to match what you'll run on it, and install it with separate ground and neutral bars as the code requires.

- Paragraph:

> For a detached building, the feeder runs underground in conduit at the proper depth, and the building gets its own grounding electrode and a disconnect. Inside the house, we route cable through joists and finished spaces as cleanly as we can and patch only what we have to open. Every new circuit is labeled, and the job is permitted and inspected.

- Links in this section:
  - Link **"panel upgrade"** → Electrical Panel Upgrade page

**Section 2**

- **H2:** What Affects the Cost
- Paragraph:

> Cost depends mostly on the distance between the main panel and the subpanel, the size of the feeder, whether trenching is involved, and how many circuits you want installed now. A 60-amp subpanel in a basement next to the main panel is a very different job from a 100-amp feed to a barn across the yard. We price it out in writing before we start.


**Section 3**

- **H2:** Subpanels and Generators
- Paragraph:

> A subpanel can also make a backup generator simpler. Instead of wiring a transfer switch to every circuit in the house, we can move the essentials, like the furnace, refrigerator, sump pump and a few lights and outlets, to a dedicated subpanel that the generator feeds. It's a common setup for homes that lose power in storms.


**Section 4**

- **H2:** Subpanels Around Yardley
- Paragraph:

> We install subpanels for basement finishes in Southampton and Langhorne, and for detached garages and workshops in Warminster and on the larger lots around Washington Crossing. If you're adding a building, our shed and garage wiring page covers the rest of that job.

- Links in this section:
  - Link **"Langhorne"** → Langhorne page
  - Link **"Warminster"** → Warminster page
  - Link **"Washington Crossing"** → Washington Crossing page
  - Link **"shed and garage wiring"** → Shed, Garage & Barn Wiring page

## Strip 4: Related services

| Element | Copy | Links to |
|---|---|---|
| Label | RELATED | |
| Heading (H2) | Related Services | |
| Card: title (H3) | Electrical Panel Upgrade | |
| Card: text | Replace an outdated or overloaded electrical panel with a modern 200-amp service. We handle the permit, the PECO disconnect and reconnect, the inspection, and label every circuit when we're done. | |
| Card: link | Learn more → | Electrical Panel Upgrade page |
| Card: title (H3) | Shed, Garage & Barn Wiring | |
| Card: text | Power for detached garages, sheds and workshops: underground feeders, subpanels, lighting, outlets, 240-volt tool circuits and EV charger circuits, permitted and inspected. | |
| Card: link | Learn more → | Shed, Garage & Barn Wiring page |
| Card: title (H3) | Basement Wiring | |
| Card: text | Complete electrical for finished basements: circuits, outlets, recessed lighting, AFCI and GFCI protection, smoke alarms, sump pump circuits and a subpanel if your main panel is full. | |
| Card: link | Learn more → | Basement Wiring page |
| Button | See all 14 electrician services | Electrician page |

## Strip 5: How a job works

Already there from the duplicate. Nothing changes.

## Strip 6: Questions

| Element | Copy |
|---|---|
| Label | QUESTIONS |
| Heading (H2) | Good to Know |
| Intro | Still have a question? Call 215-906-4634. You'll talk to an electrician, not a call center. (link the number to phone `+12159064634`) |

- **H3:** Will a subpanel give me more power?

> No. It gives you more breaker space. The total power available is still limited by your main service, which is why we run a load calculation before recommending one.

- **H3:** Can a subpanel go in a detached garage?

> Yes. A detached building needs its own grounding and a disconnect, and the feeder runs underground in conduit. We handle all of it, including the permit.

- **H3:** How big should my subpanel be?

> It depends on what you plan to run. A basement might need 60 amps, while a workshop with welders or a garage with an EV charger may need 100 amps or more.

## Structured data (SEO)

Page ⋯ → **SEO basics → Advanced SEO → Structured data markup → Add new markup**, and paste this. It tells Google what the service is, where the page sits, and its questions and answers.

```json
{
 "@context": "https://schema.org",
 "@graph": [
  {
   "@type": "Service",
   "name": "Electrical Subpanel Installation",
   "serviceType": "Electrical Subpanel Installation",
   "description": "Add circuits where you need them with a subpanel for a garage, basement, addition or workshop. We check your service capacity first, size the feeder properly and handle the permit and inspection.",
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
   "url": "https://www.joehuckelectric.com/electrical-subpanel-installation"
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
     "name": "Electrical Subpanel Installation",
     "item": "https://www.joehuckelectric.com/electrical-subpanel-installation"
    }
   ]
  },
  {
   "@type": "FAQPage",
   "mainEntity": [
    {
     "@type": "Question",
     "name": "Will a subpanel give me more power?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "No. It gives you more breaker space. The total power available is still limited by your main service, which is why we run a load calculation before recommending one."
     }
    },
    {
     "@type": "Question",
     "name": "Can a subpanel go in a detached garage?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "Yes. A detached building needs its own grounding and a disconnect, and the feeder runs underground in conduit. We handle all of it, including the permit."
     }
    },
    {
     "@type": "Question",
     "name": "How big should my subpanel be?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "It depends on what you plan to run. A basement might need 60 amps, while a workshop with welders or a garage with an EV charger may need 100 amps or more."
     }
    }
   ]
  }
 ]
}
```

