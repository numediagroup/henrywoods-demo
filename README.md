# Henry Woods Skip Hire — Website Demo

A clickable HTML demo of the upgraded Henry Woods Skip Hire website.
Built by Nu Media Group from the real brand assets extracted from
[henrywoodsskiphire.co.uk](https://www.henrywoodsskiphire.co.uk/).

## What's here

19 static HTML pages + a 7-step interactive booking flow:

| Page | Path | Purpose |
|---|---|---|
| Homepage | `index.html` / `mockup.html` | Hero + booking strip + all sections |
| Skip Hire (main) | `skip-hire.html` | Long-form service page, the SEO meat |
| Booking flow | `book.html` | 7-step interactive demo |
| Skip sizes | `sizes/{4,6,8,12}-yard.html` | One page per size |
| Areas covered | `areas/index.html` + 5 area children | Local SEO per postcode |
| About | `about.html` | 30-year heritage story |
| Contact | `contact.html` | Phone, email, address + form |
| FAQ | `faq.html` | 12 questions answered |
| Permits | `permits.html` | Council permit explainer |
| Terms | `terms.html` | Legal placeholder |
| Privacy | `privacy.html` | GDPR template |

## Brand system

Extracted live from henrywoodsskiphire.co.uk on 21 May 2026.

- **Primary**: `#9F1E00` Henry Woods burgundy red
- **Accent**: `#F77C39` Henry Woods orange (cartoon skip + secondary)
- **Ink**: `#2C2C2C` body text
- **Paper**: `#F7F7F7` header / off-white surface
- **Font**: `Panton` (Aaron's WordPress) with `Sora` (Google Fonts) as the
  open-source fallback for the local mockup

All real brand assets (`logo.png`, `hero-skip.png`, `hero-bg.jpg`, the
4 service icons, the 3 lorry illustrations) are in `assets/`.

Full design system in `DESIGN.md`.

## How to view locally

```bash
cd <this-folder>
python3 -m http.server 8741
# Then open http://localhost:8741/
```

Or drag the folder onto **netlify.com/drop** for an instant public URL.

## How to take this into Lovable

1. Open Lovable
2. Connect this GitHub repo
3. The 19 HTML pages + `assets/` give Lovable everything it needs to
   reconstruct the design system as React components
4. The booking flow at `book.html` is the state-machine reference for
   the Stripe-integrated version
5. The 4 generator scripts (`_fix-nav.py`, `_utility-generate.py`,
   `sizes/_generate.py`, `areas/_generate.py`) document the content model

## Generator scripts

Some pages were generated from templates to keep them visually 1:1:
- `sizes/_generate.py` produces the 4 skip-size pages from `sizes/_template.html`
- `areas/_generate.py` produces 5 area pages + parent from `areas/_template.html`
- `_utility-generate.py` produces about/contact/faq/permits/terms/privacy
- `_fix-nav.py` standardises the nav menu across every HTML file

To regenerate any of these: edit the template OR the data dict in the
generator, run `python3 _generate.py`.

---

Designed by Nu Media Group, June 2026.
