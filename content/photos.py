"""Job photos and where they appear.

Only pages whose service the photo actually shows get one (WWP: "images should
align with the service they offer"). Pages without a matching photo show the
team card instead. Files live in site/assets/img/jobs/ (NAME.jpg + NAME-sm.jpg).

Each entry: (file, alt text, caption, CSS object-position for the crop).
"""

JOBS = "/assets/img/jobs/"

PHOTOS = {
    "new-breaker-panel": ("Ryan Huck wiring a new breaker panel in a Bucks County basement",
                          "A new breaker panel going in, with every circuit labeled.", "55% 45%"),
    "breaker-terminal": ("Electrician tightening a breaker terminal in a residential panel",
                         "Checking the connection on a breaker before replacing it.", "50% 50%"),
    "panel-connections": ("Tightening connections inside an electrical panel during an inspection",
                          "Tightening panel connections during a safety check.", "50% 50%"),
    "breaker-work": ("Working on breakers in a full residential electrical panel",
                     "Swapping breakers in a panel that's been added onto over the years.", "50% 45%"),
    "panel-load-check": ("Measuring load at the electrical panel with a clamp meter",
                         "Measuring the panel's load before adding a charger circuit.", "55% 50%"),
    "older-panel-wiring": ("Ryan Huck working in a full residential electrical panel",
                           "Working through a crowded panel before an upgrade.", "50% 40%"),
    "outlet-troubleshooting": ("Testing a kitchen outlet with a voltage tester to find a fault",
                               "Testing an outlet to track down where a circuit fails.", "50% 40%"),
    "outlet-inspection-test": ("Testing a kitchen outlet with a receptacle tester",
                               "Testing outlets for wiring faults and missing protection.", "45% 45%"),
    "kitchen-outlet-install": ("Installing a new outlet on a kitchen backsplash",
                               "Setting a new backsplash outlet in a remodeled kitchen.", "50% 45%"),
    "kitchen-outlet-range": ("Replacing a kitchen outlet beside the range",
                             "Replacing a countertop outlet beside the range.", "50% 50%"),
    "bathroom-outlet-test": ("Testing a bathroom outlet with a receptacle tester",
                             "Testing a bathroom outlet's wiring and protection.", "45% 45%"),
    "recessed-light-install": ("Ryan Huck installing a slim LED recessed light in a finished ceiling",
                               "Installing a slim LED recessed light in a finished ceiling.", "50% 25%"),
    "chandelier-install": ("Hanging a crystal chandelier from a stepladder",
                           "Hanging a crystal chandelier over a dining area.", "50% 30%"),
    "pool-timer-outdoor-outlet": ("Testing a pool pump timer and weatherproof outdoor outlet on a post",
                                  "Testing a pool pump timer and its weatherproof outlet.", "40% 55%"),
    "ryan-drill": ("Ryan Huck of Joe Huck Electric on a job in a Bucks County home",
                   "Ryan Huck, head electrician, on the job.", "50% 30%"),
    "panel-shirt-back": ("Joe Huck Electric electrician working at a basement electrical panel",
                         "At the panel in a Bucks County basement.", "50% 35%"),
    "kitchen-shirt-back": ("Joe Huck Electric electrician wiring a kitchen backsplash",
                           "Wiring a kitchen during a remodel.", "50% 40%"),
    "tool-belt": ("Joe Huck Electric electrician's tool belt", "", "50% 50%"),
    "abie-ladder": ("Abie, assistant electrician at Joe Huck Electric, with a stepladder",
                    "Abie, assistant electrician.", "50% 30%"),
}

# service slug -> photo name (only where the photo shows that service)
SERVICE_PHOTOS = {
    "electrical-panel-upgrade": "older-panel-wiring",
    "electrical-subpanel-installation": ("new-breaker-panel", "62% 40%", "A new breaker panel going in, with every circuit labeled."),
    "circuit-breaker-replacement": "breaker-terminal",
    "electrical-maintenance": "panel-connections",
    "afci-breaker-installation": "breaker-work",
    "ev-charger-installation": "panel-load-check",
    "home-rewiring": "older-panel-wiring-2",
    "home-electrical-upgrades": "panel-shirt-back",
    "electrical-repair-troubleshooting": "outlet-troubleshooting",
    "electrical-code-corrections": "outlet-inspection-test",
    "switch-outlet-installation": "kitchen-outlet-install",
    "kitchen-electrical-upgrade": "kitchen-outlet-range",
    "gfci-outlet-installation": "bathroom-outlet-test",
    "recessed-lighting-installation": "recessed-light-install",
    "chandelier-installation": "chandelier-install",
    "pool-electrical-wiring": "pool-timer-outdoor-outlet",
    "outdoor-outlet-installation": ("pool-timer-outdoor-outlet", "45% 85%",
                                    "A weatherproof outdoor outlet with an in-use cover."),
}

PHOTOS["older-panel-wiring-2"] = ("Ryan Huck updating an older home's electrical panel",
                                  "Updating an older home's panel and circuits.", "50% 40%")

# category hubs and the /services/ page
CATEGORY_PHOTOS = {"g": "panel-connections", "i": "kitchen-shirt-back", "l": "ryan-drill"}
