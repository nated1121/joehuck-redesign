"""Business details used on every page.

NAP (name, address, phone) must match the Google Business Profile exactly,
character for character. Check it against the profile before launch.
"""

DOMAIN = "https://www.joehuckelectric.com"

NAME = "Joe Huck Electric"
LEGAL_NAME = "Joe Huck Electric LLC"
PHONE_DISPLAY = "215-906-4634"
PHONE_E164 = "+12159064634"
STREET = "42 Bedford Pl"
CITY = "Yardley"
REGION = "PA"
POSTAL = "19067"

# Opening hours shown on the site and in schema, e.g.
# HOURS = [("Mo-Fr", "07:00", "17:00", "Monday–Friday, 7:00am–5:00pm")]
# Left empty until confirmed with Joe: the WWP framework wants hours visible,
# but wrong hours are worse than none.
HOURS = []

# Google Maps embed. Replace with the embed code from the Business Profile
# (Maps → Share → Embed a map) so the pin is the listing itself.
MAP_EMBED = "https://www.google.com/maps?q=Joe+Huck+Electric,+42+Bedford+Pl,+Yardley,+PA+19067&output=embed"

SAME_AS = [
    "https://www.facebook.com/JoeHuckElectric/",
    "https://nextdoor.com/pages/joe-huck-electric-yardley-pa/",
    "https://www.homeadvisor.com/rated.JoeHuckElectric.29631615.html",
]

CATEGORIES = {
    "g": {
        "slug": "electrician-services",
        "name": "Electrician",
        "short": "Electrician",
        "chip": "Electrician services",
        "tag": "Repairs · Upgrades",
    },
    "i": {
        "slug": "electrical-installation-services",
        "name": "Electrical Installation Services",
        "short": "Installation",
        "chip": "Electrical installation",
        "tag": "New circuits · Wiring",
    },
    "l": {
        "slug": "lighting-contractor-services",
        "name": "Lighting Contractor Services",
        "short": "Lighting",
        "chip": "Lighting",
        "tag": "Recessed · Fixtures",
    },
}

# Old URLs on the current site → new pages (301 redirects).
REDIRECTS = {
    "/bucks-county-electrician": "/electrician-services/",
    "/bucks-county-electrical-installation-service": "/electrical-installation-services/",
    "/bucks-county-lighting-contractor": "/lighting-contractor-services/",
    "/bucks-county-electric-vehicle-charging-station-contractor": "/electrical-installation-services/ev-charger-installation/",
    "/level-2-ev-charger-installation": "/electrical-installation-services/ev-charger-installation/",
    "/copy-of-electrical-fixture-installation-1": "/electrical-installation-services/ev-charger-installation/",
    "/copy-of-commercial-electrical-contrac": "/electrician-services/electrical-repair-troubleshooting/",
    "/residential-electricial-services-yardley-pennsylvania/service-upgrades-panel-replacements": "/electrician-services/electrical-panel-upgrade/",
    # no central Services page: the menu's Services dropdown lists the three category pages
    "/services": "/",
}

# Services the Business Profile lists under more than one category. The page
# lives under its "cat"; these extra categories get a row in gbp-services.csv.
GBP_ALSO = {"ev-charger-installation": ["g"]}

# Services that no longer have their own page, and the page that covers them now.
# "hub:i" / "hub:l" means a section on that category page. Old links and
# redirects to these slugs resolve to the new page.
FOLDED_SERVICES = {
    "circuit-breaker-replacement": "electrical-panel-upgrade",
    "afci-breaker-installation": "electrical-panel-upgrade",
    "home-electrical-upgrades": "home-rewiring",
    "ground-wire-installation-repair": "home-rewiring",
    "electrical-code-corrections": "electrical-maintenance",
    "smoke-detector-installation": "electrical-maintenance",
    "kitchen-electrical-upgrade": "dedicated-circuit-installation",
    "appliance-wiring": "dedicated-circuit-installation",
    "new-construction-electrical": "basement-wiring",
    "electrical-wiring-installation": "basement-wiring",
    "switch-outlet-relocation": "switch-outlet-installation",
    "dimmer-switch-installation": "switch-outlet-installation",
    "three-way-switch-wiring": "switch-outlet-installation",
    "outdoor-outlet-installation": "gfci-outlet-installation",
    "attic-fan-installation": "ceiling-fan-installation",
    "bathroom-fixture-wiring": "ceiling-fan-installation",
    "pool-electrical-wiring": "hot-tub-electrical-hookup",
    "barn-wiring": "shed-garage-wiring",
    "garage-lighting-installation": "shed-garage-wiring",
    "smart-home-wiring": "hub:i",
    "doorbell-installation": "hub:i",
    "low-voltage-wiring": "hub:i",
    "chandelier-installation": "light-fixture-installation",
    "pendant-lighting-installation": "light-fixture-installation",
    "wall-sconce-installation": "light-fixture-installation",
    "track-lighting-installation": "light-fixture-installation",
    "ceiling-light-installation": "light-fixture-installation",
    "led-strip-lighting-installation": "under-cabinet-lighting-installation",
    "accent-cove-lighting": "under-cabinet-lighting-installation",
    "motion-sensor-lighting": "security-flood-lighting",
    "led-lighting-retrofits": "lighting-repair",
    "smart-lighting-installation": "hub:l",
}

# GBP services covered by a section on a category page rather than a service page
HUB_GBP = {"i": ["Smart home wiring", "Doorbell installation", "Low voltage wiring"], "l": ["Smart lighting installation"]}

# Service-area towns listed on the site without a page of their own (region shown on the Service Areas page)
TOWNS_WITHOUT_PAGES = [
    ("Lower Makefield", "lower"), ("Southampton", "lower"), ("Richboro", "central"), ("Warrington", "central"),
    ("Chalfont", "central"), ("Perkasie", "upper"), ("Sellersville", "upper"), ("Quakertown", "upper"),
]
REMOVED_AREAS = ["lower-makefield", "southampton", "richboro", "warrington", "chalfont", "perkasie", "sellersville", "quakertown"]
