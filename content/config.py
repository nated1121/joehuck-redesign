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
    "/bucks-county-electric-vehicle-charging-station-contractor": "/electrician-services/ev-charger-installation/",
    "/level-2-ev-charger-installation": "/electrician-services/ev-charger-installation/",
    "/copy-of-electrical-fixture-installation-1": "/electrician-services/ev-charger-installation/",
    "/copy-of-commercial-electrical-contrac": "/electrician-services/electrical-repair-troubleshooting/",
    "/residential-electricial-services-yardley-pennsylvania/service-upgrades-panel-replacements": "/electrician-services/electrical-panel-upgrade/",
}
