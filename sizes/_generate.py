#!/usr/bin/env python3
"""Generate /sizes/{4,6,8,12}-yard.html from _template.html"""
from pathlib import Path

HERE = Path(__file__).parent
TPL = (HERE / "_template.html").read_text()

# Reusable cartoon skip SVG — simple flat illustration, scales by size
def skip_svg(scale=1.0, height_ratio=1.0):
    h_top = 30
    h_bottom = 140 * height_ratio
    w_top = 280
    w_bottom = 240
    return f'''<svg viewBox="0 0 320 {h_top + h_bottom + 20}" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <ellipse cx="160" cy="{h_top + h_bottom + 14}" rx="130" ry="4" fill="#2C2C2C" opacity="0.16"/>
  <polygon points="20,{h_top} 300,{h_top} 275,{h_top + h_bottom} 45,{h_top + h_bottom}" fill="#F77C39" stroke="#9F1E00" stroke-width="3" stroke-linejoin="round"/>
  <polygon points="20,{h_top} 45,{h_top + h_bottom} 50,{h_top + h_bottom} 25,{h_top}" fill="#C44A1F"/>
  <path d="M 20 {h_top} L 300 {h_top} L 295 {h_top + 12} L 25 {h_top + 12} Z" fill="#FA8B4A" opacity="0.55"/>
  <line x1="100" y1="{h_top + 5}" x2="103" y2="{h_top + h_bottom - 5}" stroke="#9F1E00" stroke-width="2" opacity="0.5"/>
  <line x1="160" y1="{h_top + 5}" x2="160" y2="{h_top + h_bottom - 5}" stroke="#9F1E00" stroke-width="2" opacity="0.5"/>
  <line x1="220" y1="{h_top + 5}" x2="217" y2="{h_top + h_bottom - 5}" stroke="#9F1E00" stroke-width="2" opacity="0.5"/>
  <rect x="130" y="{h_top + 35}" width="60" height="28" fill="#FFFFFF" stroke="#9F1E00" stroke-width="2" rx="2"/>
  <text x="160" y="{h_top + 48}" text-anchor="middle" font-family="'Sora',sans-serif" font-size="8" font-weight="800" fill="#2C2C2C">HENRY WOODS</text>
  <text x="160" y="{h_top + 58}" text-anchor="middle" font-family="'Sora',sans-serif" font-size="5" font-weight="700" fill="#9F1E00" letter-spacing="1">SKIP HIRE</text>
</svg>'''

SIZES = [
    {
        "code": "4",
        "name": "4 yard",
        "price": "240",
        "bags": "30&ndash;40",
        "dims_m": "1.83 &middot; 1.28 &middot; 1.07&thinsp;m",
        "tag": "The compact &middot; 4 yard skips",
        "lead": "Our smallest skip — perfect for tight driveways, narrow side returns and Croydon's terraced streets. Suitable for heavy waste like soil and rubble.",
        "svg": skip_svg(0.85, 0.75),
        "heavy": "Yes",
        "access": "2.4&thinsp;m",
        "fits_headline": "Good for the smaller jobs that still need a proper skip.",
        "heavy_note": "Heavy waste fine (soil, rubble, concrete) up to the fill line",
        "fits_best": [
            "<strong>Bathroom rip-out</strong> — sanitaryware, tiles, plasterboard",
            "<strong>Garage clearance</strong> — old furniture, garden tools, packaging",
            "<strong>Garden tidy</strong> — soil, paving slabs, timber",
            "<strong>Small kitchen refit</strong> — old units and worktops",
        ],
    },
    {
        "code": "6",
        "name": "6 yard",
        "price": "288",
        "bags": "50&ndash;60",
        "dims_m": "2.59 &middot; 1.52 &middot; 1.22&thinsp;m",
        "tag": "Most popular &middot; 6 yard skips",
        "lead": "The Croydon all-rounder. Holds the contents of most kitchen rip-outs and modest renovations, and still fits on most driveways. Suitable for heavy waste.",
        "svg": skip_svg(1.0, 0.9),
        "heavy": "Yes",
        "access": "2.5&thinsp;m",
        "fits_headline": "The skip that handles most domestic renovations.",
        "heavy_note": "Heavy waste fine (soil, rubble, concrete) up to the fill line",
        "fits_best": [
            "<strong>Kitchen rip-out</strong> — units, worktops, tiles, appliances",
            "<strong>Modest renovation</strong> — small extension strip-out, partition removal",
            "<strong>Heavy garden clear</strong> — soil, paving, brick rubble",
            "<strong>Mid-size house clearance</strong> — bulky furniture and household goods",
        ],
    },
    {
        "code": "8",
        "name": "8 yard",
        "price": "318",
        "bags": "70&ndash;80",
        "dims_m": "3.66 &middot; 1.68 &middot; 1.22&thinsp;m",
        "tag": "Trade favourite &middot; 8 yard skips",
        "lead": "The everyday workhorse — the one most builders book by default. Suitable for heavy waste, and the most-booked size at the Mill Lane yard.",
        "svg": skip_svg(1.0, 1.0),
        "heavy": "Yes",
        "access": "2.6&thinsp;m",
        "fits_headline": "The builder's default. Mid-size renovations and bigger garden jobs.",
        "heavy_note": "Heavy waste fine (soil, rubble, concrete) up to the fill line",
        "fits_best": [
            "<strong>Two- and three-bed renovations</strong> — strip-out and refit",
            "<strong>Larger garden clearances</strong> — patios, decking, hedge removal",
            "<strong>Mid-size commercial</strong> — shop fit-outs, office refurbs",
            "<strong>Trade accounts</strong> — most builders' default size",
        ],
    },
    {
        "code": "12",
        "name": "12 yard",
        "price": "396",
        "bags": "100&ndash;120",
        "dims_m": "3.66 &middot; 1.68 &middot; 1.83&thinsp;m",
        "tag": "Big jobs only &middot; 12 yard skips",
        "lead": "Our largest open-top skip. Designed for bulky light waste — full property clearances, loft conversions, big commercial refurbs. Not for heavy waste.",
        "svg": skip_svg(1.0, 1.15),
        "heavy": "Light only",
        "access": "3.0&thinsp;m",
        "fits_headline": "When the small ones won't cut it.",
        "heavy_note": "<strong>Light bulky waste only</strong> &mdash; no heavy soil or rubble",
        "fits_best": [
            "<strong>Full property clearance</strong> — house contents to landfill / charity sort",
            "<strong>Loft conversion strip-out</strong> — joists, plasterboard, insulation",
            "<strong>Large commercial refurb</strong> — office or retail stripped to shell",
            "<strong>Multi-room renovations</strong> — strip-out across whole house",
        ],
    },
]

for s in SIZES:
    html = TPL
    html = html.replace("{{SIZE_NAME}}", s["name"])
    html = html.replace("{{SIZE_CODE}}", s["code"])
    html = html.replace("{{PRICE}}", s["price"])
    html = html.replace("{{BAGS}}", s["bags"])
    html = html.replace("{{DIMS_M}}", s["dims_m"])
    html = html.replace("{{TAG}}", s["tag"])
    html = html.replace("{{LEAD}}", s["lead"])
    html = html.replace("{{SVG}}", s["svg"])
    html = html.replace("{{HEAVY}}", s["heavy"])
    html = html.replace("{{ACCESS}}", s["access"])
    html = html.replace("{{FITS_HEADLINE}}", s["fits_headline"])
    html = html.replace("{{HEAVY_NOTE}}", s["heavy_note"])
    html = html.replace("{{FITS_BEST}}", "\n          ".join(f"<li><svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><polyline points=\"20 6 9 17 4 12\"/></svg> {fit}</li>" for fit in s["fits_best"]))
    # Compare row — mark current size as is-current
    for code in ["4", "6", "8", "12"]:
        html = html.replace(f"{{{{CMP_{code}}}}}", "is-current" if code == s["code"] else "")
    out_file = HERE / f"{s['code']}-yard.html"
    out_file.write_text(html)
    print(f"  wrote {out_file.relative_to(HERE.parent)}")

print(f"\nDone — generated {len(SIZES)} size pages.")
