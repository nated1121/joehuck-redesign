# Shed, Garage & Barn Wiring: Wix Build Sheet

Build this page by duplicating the **Electrical Panel Upgrade** page (see
`01-electrical-panel-upgrade.md`, last section), then replace the content
strip by strip with the copy below. The layout, sizes and colours don't change.

## Page settings

| Setting | Value |
|---|---|
| Page name | Shed, Garage & Barn Wiring |
| Show in menu | **No** (people reach it from the Electrical Installation Services page and the homepage) |
| URL slug (SEO basics) | `shed-garage-wiring`, so the address is `/shed-garage-wiring` |
| Title tag | Shed & Garage Wiring in Yardley, PA \| Garage Power in Bucks County |
| Meta description | Shed and garage wiring in Yardley, PA. Power to detached garages and sheds, underground feeders, subpanels, lighting, outlets and EV chargers. Licensed. |
| Let search engines index this page | On |
| Social share image | Leave as the site default |

## Strip 1: Hero

| Element | Copy |
|---|---|
| Breadcrumb | Home / Electrical Installation Services / Shed, Garage & Barn Wiring (link "Home" → Home page; "Electrical Installation Services" → Electrical Installation Services page; the last part is plain text) |
| Label | ELECTRICAL INSTALLATION SERVICES |
| H1 | Shed & Garage Wiring in Yardley, PA |
| Intro | A shed or detached garage without power is just storage. With lights and outlets it's a workshop, a gym or a place to charge the car. We run power to detached garages, sheds and workshops around Yardley, from a single circuit to a full subpanel. |
| Buttons | Get a free estimate · Call 215-906-4634 |
| Trust line | Licensed & insured · Only electrical, 40+ years · Free written estimates |
| Form | Copied from the homepage (title "Request a Free Estimate" is plain bold text, not a heading) |

## Strip 2: Why us band

Already there from the duplicate. Nothing changes.

## Strip 3: Article

**Photo:** none for this service. Leave the photo out and start the column with the signs box.

**Signs box**

- **H2:** What Your Garage or Shed Might Need
- Bulleted list:

> - Lights and a few outlets for tools and a fridge
> - 240-volt circuits for a compressor, welder or table saw
> - An EV charger in a detached garage
> - A subpanel for a workshop or finished space
> - Replacing an old extension-cord or overhead-wire setup

**Section 1**

- **H2:** Getting Power to the Building
- Paragraph:

> Most detached buildings are fed underground. We trench from the house to the building and run the feeder in conduit at the required depth, sized for the load and the distance. For a shed that only needs light and a couple of outlets, a single circuit may be enough. For a garage or workshop, we install a subpanel with its own grounding electrode and a disconnect, which the code requires for a separate building.

- Links in this section:
  - Link **"subpanel"** → Electrical Subpanel Installation page

**Section 2**

- **H2:** Inside the Building
- Paragraph:

> We install lighting, outlets and the circuits you need, with GFCI protection on garage and shed outlets. Bright LED fixtures make a big difference; see garage lighting installation. For car charging in a detached garage, we size the feeder to include it; see EV charger installation. We use wiring methods suited to unfinished spaces and damp locations.

- Links in this section:
  - Link **"garage lighting installation"** → Shed, Garage & Barn Wiring page
  - Link **"EV charger installation"** → Electric Car Charger Installation page

**Section 3**

- **H2:** Attached Garages
- Paragraph:

> Attached garages often need more outlets, better lighting and a dedicated circuit or two. The work is simpler because the panel is usually close.


**Section 4**

- **H2:** What Affects the Cost
- Paragraph:

> The distance and route for the trench, the size of the feeder, and what you want inside the building are the main factors. We'll tell you if anything like a driveway or patio is in the way.


**Section 5**

- **H2:** Garage Lighting
- Paragraph:

> Most garages start with one bare bulb. We replace it with bright, even LED shop lighting on a switch by the door, and add outlets and circuits for tools, freezers and workbenches.


**Section 6**

- **H2:** Barn Wiring
- Paragraph:

> Horse barns and pole buildings need more than a garage: a properly sized feeder and subpanel, damp- and dust-rated lighting, GFCI-protected outlets, and circuits for water heaters, fans and heated waterers. We also replace old barn wiring that's been added onto for decades.


**Section 7**

- **H2:** Garage and Shed Wiring Around Yardley
- Paragraph:

> We run power to detached garages and workshops on larger lots in Washington Crossing and Quakertown, and to backyard sheds in Levittown.

- Links in this section:
  - Link **"Washington Crossing"** → Washington Crossing page
  - Link **"Levittown"** → Levittown page

## Strip 4: Related services

| Element | Copy | Links to |
|---|---|---|
| Label | RELATED | |
| Heading (H2) | Related Services | |
| Card: title (H3) | Electrical Subpanel Installation | |
| Card: text | Add circuits where you need them with a subpanel for a garage, basement, addition or workshop. We check your service capacity first, size the feeder properly and handle the permit and inspection. | |
| Card: link | Learn more → | Electrical Subpanel Installation page |
| Card: title (H3) | Electric Car Charger Installation | |
| Card: text | Level 2 home EV charger installation by a Tesla-certified installer. We check your panel's capacity, run the circuit to your garage or driveway, and install and test chargers for Tesla, Rivian, Ford, Kia and other brands. | |
| Card: link | Learn more → | Electric Car Charger Installation page |
| Card: title (H3) | Dedicated Circuit Installation | |
| Card: text | Give appliances and equipment their own circuit so they stop tripping breakers: microwaves, refrigerators, freezers, sump pumps, space heaters, home offices, gym equipment and 240-volt tools. | |
| Card: link | Learn more → | Dedicated Circuit Installation page |
| Button | See all 23 installation services | Electrical Installation Services page |

## Strip 5: How a job works

Already there from the duplicate. Nothing changes.

## Strip 6: Questions

| Element | Copy |
|---|---|
| Label | QUESTIONS |
| Heading (H2) | Good to Know |
| Intro | Still have a question? Call 215-906-4634. You'll talk to an electrician, not a call center. (link the number to phone `+12159064634`) |

- **H3:** How deep does wiring to a shed need to be buried?

> It depends on the wiring method and conduit. We follow the code depth for the method we use and call to have utilities marked first.

- **H3:** Does a detached garage need its own panel?

> Not always. A small shed can run on one circuit; a garage or workshop usually benefits from a subpanel.

- **H3:** Do I need a permit?

> Yes. Running power to a detached building needs a permit and an inspection.

## Structured data (SEO)

Page ⋯ → **SEO basics → Advanced SEO → Structured data markup → Add new markup**, and paste this. It tells Google what the service is, where the page sits, and its questions and answers.

```json
{
 "@context": "https://schema.org",
 "@graph": [
  {
   "@type": "Service",
   "name": "Shed, Garage & Barn Wiring",
   "serviceType": "Shed, Garage & Barn Wiring",
   "description": "Power for detached garages, sheds and workshops: underground feeders, subpanels, lighting, outlets, 240-volt tool circuits and EV charger circuits, permitted and inspected.",
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
   "url": "https://www.joehuckelectric.com/shed-garage-wiring"
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
     "name": "Electrical Installation Services",
     "item": "https://www.joehuckelectric.com/electrical-installation-services"
    },
    {
     "@type": "ListItem",
     "position": 3,
     "name": "Shed, Garage & Barn Wiring",
     "item": "https://www.joehuckelectric.com/shed-garage-wiring"
    }
   ]
  },
  {
   "@type": "FAQPage",
   "mainEntity": [
    {
     "@type": "Question",
     "name": "How deep does wiring to a shed need to be buried?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "It depends on the wiring method and conduit. We follow the code depth for the method we use and call to have utilities marked first."
     }
    },
    {
     "@type": "Question",
     "name": "Does a detached garage need its own panel?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "Not always. A small shed can run on one circuit; a garage or workshop usually benefits from a subpanel."
     }
    },
    {
     "@type": "Question",
     "name": "Do I need a permit?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "Yes. Running power to a detached building needs a permit and an inspection."
     }
    }
   ]
  }
 ]
}
```

