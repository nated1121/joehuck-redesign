# Building the Rest of the Site in Wix

How to build every page except the homepage (that's in `WIX-HOMEPAGE.md`).
The coded preview is the visual reference: every page is made of the same
strips, boxes and text as the homepage, so the theme, fonts, colours and
button styles you set up for the homepage carry straight over.

## 1. What to build

| Pages | How many | How to build them in Wix | Wix URL |
|---|---:|---|---|
| Service pages | 22 | **One** dynamic page fed by the `Services` CMS collection | `/services/{slug}` |
| Service-area pages | 12 | **One** dynamic page fed by the `Service Areas` collection | `/service-areas/{slug}` |
| Category pages: Electrician, Electrical Installation Services, Lighting Contractor Services | 3 | Normal pages (build one, duplicate it twice) | `/electrician-services`, `/electrical-installation-services`, `/lighting-contractor-services` |
| Service Areas, About, Contact | 3 | Normal pages | `/service-areas`, `/about`, `/contact` |

So you design **two templates** and **six normal pages**. The other 32
pages fill themselves in from the spreadsheets.

There is **no central Services page**. The three category pages are the
service hubs, and the menu's **Services** item is a dropdown that lists them
(see step 8).

> The coded preview uses `/electrician-services/electrical-panel-upgrade/`
> style addresses. In Wix, one collection gets one address pattern, so the
> service pages live at `/services/electrical-panel-upgrade`. The spreadsheets
> already use the Wix addresses in every link.

## 2. The spreadsheets (in the `wix/` folder)

| File | What it is |
|---|---|
| `wix/services.csv` | 22 rows, one per service page |
| `wix/service-areas.csv` | 12 rows, one per town page |
| `wix/redirects.csv` | 301 redirects from the old site's URLs to the new pages, plus `/services` → homepage |

`build.py` regenerates them from the content files, so if the copy changes,
rebuild and re-import.

### Services collection fields

| Column | Wix field type | Shows on the page as |
|---|---|---|
| `title` | Title (the built-in field) | Service name on cards and in the breadcrumb |
| `slug` | Text | The page address |
| `category`, `categoryPage` | Text, Text | Hero label; the "See all … services" button link |
| `h1` | Text | The page headline (H1) |
| `seoTitle`, `seoDescription` | Text, Text | Title tag and meta description |
| `intro` | Text | Hero paragraph |
| `summary` | Text | Text on cards that link to this page (category pages) |
| `image`, `imageAlt` | **Image**, Text | Job photo above the article (12 pages have one) |
| `signsTitle`, `signsList` | Text, **Rich text** | The grey "Signs you need…" box |
| `body` | **Rich text** | The main article: H2 sections, paragraphs, lists and links |
| `faq` | **Rich text** | Questions (H3) and answers |
| `faqSchema` | Text | FAQ structured data (used by the code in step 4) |
| `gbpServices` | Text | Reference only: the GBP services this page covers |
| `related1Title`…`related3Url` | Text / Text / **URL** | The three Related Services cards |

### Service Areas collection fields

Same idea: `title` (town), `slug`, `region`, `h1`, `seoTitle`,
`seoDescription`, `intro`, `summary`, `body` (Rich text), `faq` (Rich text),
`faqSchema`, and `nearby1Title`…`nearby3Url` for the Nearby Towns cards.

### Importing

1. **CMS → Create Collection**, name it `Services`. Then **More Actions → Import from CSV** and choose `wix/services.csv`.
2. When Wix asks for field types, set `body`, `faq` and `signsList` to **Rich text**, `image` to **Image**, and the `…Url` columns to **URL**. Everything else is Text.
3. **Check one row before going further.** Open any item and confirm `body` shows headings, paragraphs and links rather than raw `<h2>` tags. If you see raw tags, delete the collection and import again with those three fields set to Rich text first.
4. **Photos:** the CSV only names the file (e.g. `older-panel-wiring.jpg`). Upload these 12 from `site/assets/img/jobs/` into each item's Image field, and paste the `imageAlt` text as the image's alt text:

| Service | Photo |
|---|---|
| Electrical Panel Upgrade | `older-panel-wiring.jpg` |
| Electrical Subpanel Installation | `new-breaker-panel.jpg` |
| Electrical Inspections & Maintenance | `panel-connections.jpg` |
| Home Rewiring | `older-panel-wiring-2.jpg` |
| Electrical Repair & Troubleshooting | `outlet-troubleshooting.jpg` |
| Electric Car Charger Installation | `panel-load-check.jpg` |
| Switch & Outlet Installation | `kitchen-outlet-install.jpg` |
| Dedicated Circuit Installation | `kitchen-outlet-range.jpg` |
| GFCI Outlet Installation | `bathroom-outlet-test.jpg` |
| Hot Tub Electrical Hookup | `pool-timer-outdoor-outlet.jpg` |
| Recessed Lighting Installation | `recessed-light-install.jpg` |
| Light Fixture Installation | `chandelier-install.jpg` |

5. Repeat for `Service Areas` with `wix/service-areas.csv` (no photos).

## 3. The service page template

In the CMS, choose **Services → Add a dynamic page → Item page**. Set the
address to `/services/{slug}` (Page settings → SEO → URL, using the `slug` field).

Build these strips top to bottom. "Bind" means: select the element, click
**Connect to CMS**, and pick the field.

| # | Strip | Background | What goes in it |
|---|---|---|---|
| 1 | **Hero** | Paper `#F5F5F3` | 2 columns (55/45). Left: breadcrumb text "Home / Services / {category} / {title}", label bound to `category`, **H1 bound to `h1`**, paragraph bound to `intro`, the two buttons (Get a free estimate → estimate anchor; Call 215-906-4634), and the small line "Licensed & insured · Only electrical, 40+ years · Free written estimates". Right: the same Wix Form as the homepage, in a white box. |
| 2 | **Why us** | Black `#0F0F0F` | 3 columns, each an icon or the two team avatars, a white 19px heading and a silver 15px line: "You'll Know Who's Coming" / "Free Diagnosis & Written Quote" / "40+ Years, Only Electrical". Same on every page. |
| 3 | **Article** | White | One centred column, **760px wide**. Image bound to `image` (4:3, 12px corners). Below it, a paper-coloured box (1px `#DCDBD8` border, 10px corners, 24px padding) holding a 22px heading bound to `signsTitle` and a rich text bound to `signsList`. Below the box, a rich text bound to `body`. |
| 4 | **Related services** | Paper | Centred heading "Related Services" (label "RELATED"). Three white cards in a row, each with a heading bound to `relatedNTitle`, text bound to `relatedNText` and a "Learn more →" link bound to `relatedNUrl`. Under them, an outline button "See all … services" linked to `categoryPage`. |
| 5 | **How a job works** | White | The same 4 numbered boxes as the homepage, heading "What Happens When You Call". |
| 6 | **FAQ** | Paper | Centred heading "Good to Know" (label "QUESTIONS") and the "Still have a question? Call…" line. Below, a 760px rich text bound to `faq`. |
| 7 | CTA + footer | | Already on every page from the homepage build. |

**Page SEO** (Page settings → SEO basics): title tag bound to `seoTitle`,
meta description bound to `seoDescription`. Make sure the hero headline is
the page's only H1; the card titles are H3, and the body's headings are
already H2s inside the rich text.

### 4. A little code for the service page (optional but recommended)

Some services have no photo, and Wix may leave an empty frame where the image
would go. This hides it, and adds the FAQ structured data Google uses for FAQ
results. Turn on **Dev Mode**, give the image the ID `servicePhoto` and the
signs box the ID `signsBox` (Properties panel), and paste this into the page
code:

```js
import wixSeoFrontend from 'wix-seo-frontend';

$w.onReady(() => {
  $w('#dynamicDataset').onReady(() => {
    const item = $w('#dynamicDataset').getCurrentItem();
    if (!item.image) $w('#servicePhoto').collapse();
    if (!item.signsTitle) $w('#signsBox').collapse();
    if (item.faqSchema) {
      wixSeoFrontend.setStructuredData([JSON.parse(item.faqSchema)]);
    }
  });
});
```

If your dataset has a different ID than `dynamicDataset`, use that instead
(it's shown when you click the dataset icon on the page).

## 5. The service-area page template

**Service Areas → Add a dynamic page → Item page**, address `/service-areas/{slug}`.

Same strips as the service page, with these differences:

- **Hero:** label "Serving {title}, PA", breadcrumb "Home / Service Areas / {title}".
- **Article:** no photo and no signs box, just the `body` rich text.
- **Strip 4** is "Nearby Towns We Serve": three cards bound to `nearbyNTitle`, `nearbyNText`, `nearbyNUrl`.
- Use the same code as above, minus the two `collapse()` lines.

## 6. The category pages (3)

Build **Electrician** first, then duplicate it twice and change the text.
Copy the words from the coded preview page for each.

1. **Hero:** same as the service page, with static text. Label "Electrician · Yardley, PA", H1 "Electrician Services in Yardley, PA" (Installation: "Electrical Installation Services in Yardley, PA"; Lighting: "Lighting Contractor Services in Yardley, PA").
2. **Why us** strip.
3. **Overview** (white): 2 columns. Left: the overview text and section(s) from the preview. Right: the category photo (Electrician `panel-connections.jpg`, Installation `kitchen-shirt-back.jpg`, Lighting `ryan-drill.jpg`), 4:5, 12px corners.
4. **Popular jobs** (paper): 2–3 photo cards, like the homepage's Popular Services.
5. **All services** (white): a **repeater** connected to the `Services` collection, with a dataset filter `category` = this page's category name. Each repeater item: H3 bound to `title`, text bound to `summary`, link "Learn more →" bound to the item's dynamic page. This lists every service automatically.
6. How a job works, FAQ (type the 2–3 questions from the preview as static text).

## 7. Service Areas, About, Contact

- **Service Areas:** hero, why us, then one strip per region ("Near Yardley", "Central Bucks", "Upper Bucks"), each with a repeater connected to `Service Areas` filtered by `region`, and a plain text line for the towns without a page ("Also serving Lower Makefield and Southampton. Call to schedule." and so on, as in the preview). Upper Bucks has no pages, so it's just the heading and the text line.
- **About:** hero, then the article text in a 760px column, then the Meet the Local Team strip (copy it from the homepage).
- **Contact:** hero with the form, then 2 columns: business name, address, phone and the "Tell us what's going on…" paragraph | a Google Maps element.

## 8. Before you publish

- [ ] **Redirects:** Marketing & SEO → SEO → URL Redirect Manager → import `wix/redirects.csv` (or add the 9 lines by hand). The last one sends `/services` to the homepage, for anyone who trims a service page's address.
- [ ] Every page has one H1, and the title tag and meta description are set (bound to the collection fields on the two templates).
- [ ] **The menu:** Site Menu → Add Menu Item → **Dropdown title** (Wix may call it a menu folder) named **Services**, with the three category pages dragged under it: Electrician, Electrical Installation Services, Lighting Contractor Services. Then Service Areas, About, Contact. The Services title isn't a page; tapping it just opens the list.
- [ ] Open three service pages and two area pages on a phone and check the strips stack.
- [ ] Submit the sitemap in Google Search Console once the domain is connected.
