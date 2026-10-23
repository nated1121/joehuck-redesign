# Electric Car Charger Installation: Wix Build Sheet

Build this page by duplicating the **Electrical Panel Upgrade** page (see
`01-electrical-panel-upgrade.md`, last section), then replace the content
strip by strip with the copy below. The layout, sizes and colours don't change.

## Page settings

| Setting | Value |
|---|---|
| Page name | Electric Car Charger Installation |
| Show in menu | **No** (people reach it from the Electrical Installation Services page and the homepage) |
| URL slug (SEO basics) | `ev-charger-installation`, so the address is `/ev-charger-installation` |
| Title tag | EV Charger Installation in Yardley, PA \| Level 2 Chargers in Bucks County |
| Meta description | Level 2 EV charger installation in Yardley, PA by a Tesla-certified installer. Tesla, Rivian, Kia, Ford and more. Load calculation, permit and testing included. |
| Let search engines index this page | On |
| Social share image | `panel-load-check.jpg` |

## Strip 1: Hero

| Element | Copy |
|---|---|
| Breadcrumb | Home / Electrical Installation Services / Electric Car Charger Installation (link "Home" → Home page; "Electrical Installation Services" → Electrical Installation Services page; the last part is plain text) |
| Label | ELECTRICAL INSTALLATION SERVICES |
| H1 | EV Charger Installation in Yardley, PA |
| Intro | A Level 2 charger adds roughly 25 to 30 miles of range per hour, enough to fill most EVs overnight. We're certified by Tesla to install their Level 2 chargers, and we install chargers for every major brand in garages and driveways around Yardley. |
| Buttons | Get a free estimate · Call 215-906-4634 |
| Trust line | Licensed & insured · Only electrical, 40+ years · Free written estimates |
| Form | Copied from the homepage (title "Request a Free Estimate" is plain bold text, not a heading) |

## Strip 2: Why us band

Already there from the duplicate. Nothing changes.

## Strip 3: Article

**Photo:** `site/assets/img/jobs/panel-load-check.jpg`  
**Alt text:** Measuring load at the electrical panel with a clamp meter

**Signs box**

- **H2:** Is Your Home Ready for a Level 2 Charger?
- Bulleted list:

> - You're charging from a regular 120-volt outlet and it can't keep up
> - You have a 100 amp service, or your panel is nearly full
> - The garage is detached, or the charger needs to go outside
> - You have two EVs, or plan to
> - You want a charger on the same circuit as a future second car

**Section 1**

- **H2:** How We Install Your Charger
- Paragraph:

> Every install starts with a load calculation. A charger is a large, continuous load, and we need to confirm your service can carry it along with your heat, air conditioning, cooking and water heater. Most homes with a 200 amp service can add a charger with no trouble. If yours can't, we'll explain your options, from load-management devices to a panel upgrade.

- Paragraph:

> Then we install a dedicated circuit sized for the charger, typically 40 to 60 amps at 240 volts, and run it to where you park. Wire runs are neat and protected, inside the garage or outdoors in conduit. We mount the charger, configure it for the circuit, and test it with your car. The job is permitted and inspected.

- Links in this section:
  - Link **"panel upgrade"** → Electrical Panel Upgrade page
  - Link **"dedicated circuit"** → Dedicated Circuit Installation page

**Section 2**

- **H2:** Chargers We Install
- Paragraph:

> We're certified by Tesla to install the Tesla Wall Connector, and we install hardwired and plug-in chargers from ChargePoint, Emporia, Grizzl-E, Wallbox and the automakers themselves for Rivian, Ford, Kia, Hyundai, Mercedes, BYD and more. We can install a NEMA 14-50 outlet if you'd rather plug in a mobile charger.


**Section 3**

- **H2:** What Affects the Cost
- Paragraph:

> The distance from the panel to the charger, whether the run is inside or outside, the charger's amperage and your panel's capacity all affect the price. Detached garages may need a trench or a garage subpanel.

- Links in this section:
  - Link **"garage subpanel"** → Shed, Garage & Barn Wiring page

**Section 4**

- **H2:** Choosing Where to Mount the Charger
- Paragraph:

> We'll look at where you park, where the charge port is on your car and whether you might add a second EV later. Mounting the charger where the cable reaches comfortably without crossing a walkway keeps it safe and convenient. Outdoor chargers need a location that's protected from snow piles and plows, and the charger itself must be rated for outdoor use.


**Section 5**

- **H2:** EV Chargers Around Yardley
- Paragraph:

> We install chargers in garages throughout Newtown, Warrington and Richboro, and in driveways on the larger lots around Washington Crossing.

- Links in this section:
  - Link **"Newtown"** → Newtown page
  - Link **"Washington Crossing"** → Washington Crossing page

## Strip 4: Related services

| Element | Copy | Links to |
|---|---|---|
| Label | RELATED | |
| Heading (H2) | Related Services | |
| Card: title (H3) | Electrical Panel Upgrade | |
| Card: text | Replace an outdated or overloaded electrical panel with a modern 200-amp service. We handle the permit, the PECO disconnect and reconnect, the inspection, and label every circuit when we're done. | |
| Card: link | Learn more → | Electrical Panel Upgrade page |
| Card: title (H3) | Dedicated Circuit Installation | |
| Card: text | Give appliances and equipment their own circuit so they stop tripping breakers: microwaves, refrigerators, freezers, sump pumps, space heaters, home offices, gym equipment and 240-volt tools. | |
| Card: link | Learn more → | Dedicated Circuit Installation page |
| Card: title (H3) | Shed, Garage & Barn Wiring | |
| Card: text | Power for detached garages, sheds and workshops: underground feeders, subpanels, lighting, outlets, 240-volt tool circuits and EV charger circuits, permitted and inspected. | |
| Card: link | Learn more → | Shed, Garage & Barn Wiring page |
| Button | See all 23 installation services | Electrical Installation Services page |

## Strip 5: How a job works

Already there from the duplicate. Nothing changes.

## Strip 6: Questions

| Element | Copy |
|---|---|
| Label | QUESTIONS |
| Heading (H2) | Good to Know |
| Intro | Still have a question? Call 215-906-4634. You'll talk to an electrician, not a call center. (link the number to phone `+12159064634`) |

- **H3:** Do I need a permit for an EV charger?

> Yes. A new 240-volt circuit for a charger needs a permit and an inspection, which we handle for you.

- **H3:** Should I hardwire the charger or use an outlet?

> Hardwiring is more reliable and allows higher charging speeds. A NEMA 14-50 outlet is more flexible if you might change chargers.

- **H3:** Can my 100 amp panel handle an EV charger?

> Sometimes, with a lower-amperage charger or a load-management device. The load calculation tells us for sure.

## Structured data (SEO)

Page ⋯ → **SEO basics → Advanced SEO → Structured data markup → Add new markup**, and paste this. It tells Google what the service is, where the page sits, and its questions and answers.

```json
{
 "@context": "https://schema.org",
 "@graph": [
  {
   "@type": "Service",
   "name": "Electric Car Charger Installation",
   "serviceType": "Electric Car Charger Installation",
   "description": "Level 2 home EV charger installation by a Tesla-certified installer. We check your panel's capacity, run the circuit to your garage or driveway, and install and test chargers for Tesla, Rivian, Ford, Kia and other brands.",
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
   "url": "https://www.joehuckelectric.com/ev-charger-installation"
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
     "name": "Electric Car Charger Installation",
     "item": "https://www.joehuckelectric.com/ev-charger-installation"
    }
   ]
  },
  {
   "@type": "FAQPage",
   "mainEntity": [
    {
     "@type": "Question",
     "name": "Do I need a permit for an EV charger?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "Yes. A new 240-volt circuit for a charger needs a permit and an inspection, which we handle for you."
     }
    },
    {
     "@type": "Question",
     "name": "Should I hardwire the charger or use an outlet?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "Hardwiring is more reliable and allows higher charging speeds. A NEMA 14-50 outlet is more flexible if you might change chargers."
     }
    },
    {
     "@type": "Question",
     "name": "Can my 100 amp panel handle an EV charger?",
     "acceptedAnswer": {
      "@type": "Answer",
      "text": "Sometimes, with a lower-amperage charger or a load-management device. The load calculation tells us for sure."
     }
    }
   ]
  }
 ]
}
```

