# Working documents

Plans, call guides, ad and post drafts. Not published: Jekyll skips
folders beginning with an underscore, and `_config.yml` names this one
again in case the folder is ever renamed.

Anything in the repository root is served at soundlineschool.com. These
files were there until 29 October 2026 — `soundlineschool.com/PLAN-35.md`
was readable by anyone who guessed it. Keep working notes here.

## How the pages are built (12 Nov 2026)

The family-facing pages are generated. Do not edit `index.html`, `day.html`, `join.html`, `vision.html`,
`about.html`, `collaborative.html` or `scholarship.html` by hand; the next build overwrites them.

- Copy and layout live in `tools/site/core.py` (header, footer, shared pieces), `tools/site/plain.py` (Home) and `tools/site/pages.py` (every other page).
- `python3 tools/site/make.py` writes the pages, the two redirects (`cost.html` to `join.html#tuition`, `sample-day.html` to `day.html#tuesday`),
  the header and footer on `research.html` and `survey/index.html`, `sitemap.xml` and `robots.txt`.
- `premium.css` holds what inline styles cannot: focus, hover, the phone menu, the phone action bar. `site.css` now serves only the research and survey pages.
- `/cost.html` is printed in the packet and on the tuition card, so that address must keep working.
