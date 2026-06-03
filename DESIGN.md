---
project: Henry Wood Skip Hire
aesthetic: editorial-magazine (Family Yard hybrid — heritage above the fold, conversion-machine below)
references_used:
  - ~/.claude/data/design-references/awesome-design-md/design-md/apple/DESIGN.md (alternating full-bleed tile model, ONE accent colour, photography-first)
  - ~/.claude/data/design-references/awesome-design-md/design-md/stripe/DESIGN.md (display-tier discipline, tabular figures for money, pill CTAs)
  - ~/.claude/data/design-references/awesome-design-skills/skills/editorial/DESIGN.md (serif headlines, magazine grid, 8pt baseline)
  - ~/.claude/data/nu-media-design-references.json (trades sector → editorial-magazine; banned fonts/patterns enforced)
version: 1
status: Phase 3 output. Drives Phase 4 mockup.
---

## Brand thesis

Henry Wood Skip Hire's moat is **30 years in Croydon**. The site should feel like a long-standing craft business that happens to take bookings — closer to a heritage British trade brand than a SaaS landing page or a generic skip-hire broker. The booking widget is the lead-gen muscle; the editorial photography and serif headlines are the trust-building wrapper.

Hold these in mind on every decision:
- **Earned, not loud.** No glossy gradients, no AI-default purple, no neon construction-orange. Heritage navy + warm trade orange + cream-paper background.
- **Real, not stock.** Every photograph is the actual Mill Lane yard, actual lorries, actual Henry. Stock skip photography is banned.
- **Transparent prices on every page.** The Waste Group already does this. Henry Wood must too, or we leave money on the table.
- **The booking widget is a designed object, not bolted on.** It is the most important thing on the page after the headline.

## Colour tokens

```
--ink:                  #0F1A2E      /* Heritage navy — deeper, premium */
--ink-soft:             #1A2540
--ink-muted:            #5A6275      /* Secondary text on cream */
--ink-faint:            #8C92A1      /* Tertiary text */

--paper:                #F4EFE6      /* Warm cream — the canvas */
--paper-soft:           #ECE5D7      /* Slightly darker cream for sub-cards */
--canvas:               #FFFFFF      /* Pure white reserved for booking widget + cards */
--hairline:             #DDD5C4      /* Warm hairline that matches the paper */
--hairline-strong:      #C9BFAB

--accent:               #E85D2C      /* Trade orange — warm, not safety-orange */
--accent-deep:          #C44A1F      /* Press / focus state */
--accent-soft:          #F2D1BB      /* Subdued tag fill */

--yard:                 #0A0A0A      /* True black for full-bleed dark photo sections */
--yard-2:               #14140F      /* Sub-step for stacked dark sections */

--on-ink:               #F4EFE6      /* Text on navy — paper, not pure white */
--on-yard:              #F4EFE6      /* Text on yard-black */
--on-accent:            #FFFFFF
```

**Use the accent surgically.** One filled orange button per band. Inline link accents allowed. Background blocks of orange = banned (looks like construction signage).

## Typography

- **Display (headlines):** `Fraunces` — variable serif from Google Fonts. Carries the heritage gravitas a 30-year family business deserves. Used at weights 400 (regular) and 600 (semibold) only. Letter-spacing `-0.02em` on display sizes for editorial tightness.
- **Body / UI:** `Geist` — Vercel's grotesque, open-source via Google Fonts. Modern, neutral, doesn't fight the serif. Banned alternatives (Inter, Roboto, Open Sans, Lato, Arial, Helvetica) are not used anywhere.
- **Numerics (prices, sizes, hours):** `Geist Mono` with `font-feature-settings: "tnum"`. Skip sizes, prices, capacity figures all render in mono so they read as data, not decoration.

### Scale
```
Display XL:   72px / Fraunces 400 / line 1.02 / -0.03em   (hero only)
Display L:    56px / Fraunces 400 / line 1.05 / -0.025em
Display M:    40px / Fraunces 400 / line 1.1  / -0.02em
Display S:    28px / Fraunces 600 / line 1.15 / -0.015em
Heading L:    22px / Geist 600 / line 1.3 / -0.005em
Heading M:    18px / Geist 600 / line 1.4
Heading S:    15px / Geist 600 / line 1.4 / +0.01em
Body L:       18px / Geist 400 / line 1.55
Body:         17px / Geist 400 / line 1.55   (17px not 16px, Apple rule)
Body S:       15px / Geist 400 / line 1.5
Caption:      13px / Geist 400 / line 1.45
Eyebrow:      12px / Geist 600 / line 1.0 / +0.12em / uppercase
Price L:      32px / Geist Mono 500 / line 1 / tnum
Price M:      22px / Geist Mono 500 / line 1 / tnum
Mono S:       13px / Geist Mono 400 / line 1.4 / tnum
```

## Spacing (8pt baseline)
`4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128 · 192`

- Section vertical padding: `96px` desktop, `64px` tablet, `48px` mobile.
- Card padding: `32px` standard, `48px` on booking widget.
- Button padding: `14px 24px` primary, `12px 20px` secondary.

## Shapes
- `radius-none: 0` — full-bleed sections
- `radius-xs: 4px` — input fields, tags
- `radius-sm: 8px` — cards, booking widget panels
- `radius-md: 12px` — feature cards
- `radius-pill: 9999px` — primary CTA + tags

## Elevation
Following Apple's rule: **one shadow in the whole system**, reserved for the booking widget so it "lifts" off the photographic hero.
- Widget shadow: `0 24px 60px -16px rgba(15, 26, 46, 0.35), 0 6px 16px -8px rgba(15, 26, 46, 0.2)`
- Hairline ring on cards: `1px solid var(--hairline)` (no shadow)
- Section divider: surface-colour change (paper → yard-black → paper), NOT a border line.

## Component grammar

### Buttons
- **Primary (filled orange pill):** `bg accent · text on-accent · 14×24 padding · pill radius · 17px weight 500 · active scale(0.97)`
- **Secondary (ghost on paper):** `transparent bg · text ink · 1.5px solid ink · 14×24 padding · pill radius`
- **Tertiary (text link):** `text accent · underline on hover · weight 500`
- **Phone CTA (dark utility):** `bg ink · text paper · radius-xs · 10×16 padding · Geist Mono 13px`

### Booking widget
- Floats over photographic hero, docked right.
- White canvas, radius-sm 8px, single elevation shadow.
- Step 1: postcode (large input) + date picker.
- Step 2: skip size grid (4 cards with size, dimensions, price).
- Step 3: instant total + Book + Pay CTA (orange pill).
- Tabular numerics on every price.

### Pricing cards (Skip Sizes section)
- Cream-paper background, hairline border.
- Skip size in Fraunces 40px, dimensions in Geist Mono, price in Geist Mono 32px.
- Use-case line ("Good for a 3-bed kitchen rip-out") in Geist 15px italic.
- Per-card CTA: ghost secondary "Book this size".

### Review cards
- Designed as Google-review-style cards (not embedded widget).
- Cream paper, hairline, 5-star row in accent orange (use Lucide star SVG, never emoji).
- Name + date in caption, body in 15px Geist.

### Navigation
- Top utility strip: `bg ink · text paper` — phone, hours, login.
- Main nav: `bg paper · text ink` — logo left, menu centre, primary CTA right.

## Photography
- Hero: real Mill Lane yard, dawn light, lorries, generous negative space top-left for headline.
- Heritage strip: archive-style black-and-white of the original yard or Henry Sr.
- Service photos: lorry delivering, skip being loaded — all real, all in cream/sepia tonal range that matches the palette.
- For the mockup, Unsplash industrial-yard photography acts as a stand-in.

## Banned (enforced)
- ❌ Inter, Roboto, Open Sans, Lato, Arial, Helvetica
- ❌ Purple-to-pink, blue-to-cyan, any gradient hero
- ❌ Centered "Welcome to Henry Wood Skip Hire" hero
- ❌ 3-feature-card grid below hero
- ❌ Default shadcn rounded-2xl card grids
- ❌ Stock photo of generic skip, generic lorry, generic high-vis hi-five
- ❌ Generic CTA copy: "Get Started" / "Learn More"
- ❌ Rotating client logo carousel
- ❌ Decorative shadows on cards/buttons/text (shadow is reserved for the booking widget only)

## Motion (Emil Kowalski rules)
- Buttons: `transform: scale(0.97)` on active, `transition: transform 120ms cubic-bezier(0.34, 1.56, 0.64, 1)`
- Booking widget step transitions: 220ms cubic-bezier(0.16, 1, 0.3, 1)
- Reveal on scroll (hero, heritage strip): opacity 0→1 + translateY(16px→0) over 600ms
- Accordion (FAQ): max-height transition 280ms ease-out

## Responsive
- 1440 / 1200 / 1024 / 768 / 480
- Booking widget docks right of hero at ≥1024, stacks below hero <1024
- Pricing grid: 4-col → 2-col @ 768 → 1-col @ 480
- Hero typography: 72 → 56 → 40 → 32

## Tools used (audit trail — preview)
- Brand references: Apple, Stripe (DESIGN.md files in library)
- Aesthetic skill: editorial pack (DESIGN.md)
- Nu Media library: trades sector + banned-list enforcement
- 21st-dev MCP: deferred to Phase 6 (not needed for the HTML mockup itself)
- frontend-design + impeccable + emil-design-eng + high-end-visual-design: principles applied throughout
