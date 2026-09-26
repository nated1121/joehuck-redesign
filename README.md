# Joe Huck Electric — Website

A static site for Joe Huck Electric (Yardley, PA), built for local SEO.
It has 81 pages: homepage, 3 category hubs, 53 service pages, 20 service-area
pages, plus Services, Service Areas, About and Contact.

- **Plan and reasoning:** [`SEO-STRUCTURE.md`](SEO-STRUCTURE.md)
- **Every page, with its title, H1 and word count:** [`PAGES.md`](PAGES.md)
- **Google Business Profile service descriptions:** [`gbp-services.csv`](gbp-services.csv)

## Build

Requires Python 3 only (no packages).

```sh
python3 build.py                  # builds the site into public/
python3 -m http.server -d public  # view it at http://localhost:8000
```

`build.py` also checks each page against the SEO playbook: word counts, link
counts, title and description lengths, and broken links. It prints a warning
for anything out of range.

## Editing content

| What | Where |
|---|---|
| Name, address, phone, hours, map, redirects | `content/config.py` |
| Service pages | `content/services-general.txt`, `services-installation.txt`, `services-lighting.txt` |
| Area pages | `content/areas.txt` |
| Homepage, hubs, About, Contact | `content/pages.txt` |
| Styles and scripts | `site/assets/` |

The content files are plain text. Each page starts with `=== slug`, followed by
a few `key: value` lines, then `---` and the body. In the body:

- `## Heading` starts a section.
- `- item` makes a bullet list.
- `[text](@slug)` links to another page.
- `## FAQ` followed by `Q:` / `A:` lines adds FAQs, with schema.

## Output

`public/` is the deployable site. It includes `sitemap.xml`, `robots.txt` and
`_redirects` (301s from the old site's URLs; Netlify and Cloudflare Pages format).
