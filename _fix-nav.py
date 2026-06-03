#!/usr/bin/env python3
"""Fix nav menus on every HTML page to link to real inner pages, not homepage anchors."""
import re
from pathlib import Path

ROOT = Path(__file__).parent

def nav_for(prefix, active_key):
    """Build the nav block. prefix is './' for root pages, '../' for subdirectory pages.
    active_key is one of: home, skip-hire, sizes, areas, about, contact, faq, permits."""
    items = [
        ("skip-hire", "Skip hire", f"{prefix}skip-hire.html"),
        ("sizes",     "Skip sizes", f"{prefix}skip-hire.html#sizes"),
        ("areas",     "Areas we cover", f"{prefix}areas/index.html"),
        ("about",     "About", f"{prefix}about.html"),
        ("contact",   "Contact", f"{prefix}contact.html"),
    ]
    lines = ['    <div class="nav__menu">']
    for key, label, href in items:
        cls = ' class="is-active"' if key == active_key else ''
        lines.append(f'      <a href="{href}"{cls}>{label}</a>')
    lines.append('    </div>')
    return "\n".join(lines)

# Regex matches the whole <div class="nav__menu"> ... </div> block
NAV_RE = re.compile(r'    <div class="nav__menu">.*?    </div>', re.DOTALL)

# Map every HTML file to its (prefix, active_key)
files = {
    "mockup.html":             (".",  "home"),
    "skip-hire.html":          (".",  "skip-hire"),
    "about.html":              (".",  "about"),
    "contact.html":            (".",  "contact"),
    "faq.html":                (".",  "faq"),
    "permits.html":            (".",  ""),       # Permits doesn't appear in main nav; nothing active
    "terms.html":              (".",  ""),
    "privacy.html":            (".",  ""),
    "index.html":              (".",  "home"),   # alias of homepage
    "sizes/4-yard.html":       ("..", "sizes"),
    "sizes/6-yard.html":       ("..", "sizes"),
    "sizes/8-yard.html":       ("..", "sizes"),
    "sizes/12-yard.html":      ("..", "sizes"),
    "areas/index.html":        ("..", "areas"),
    "areas/croydon.html":      ("..", "areas"),
    "areas/sutton.html":       ("..", "areas"),
    "areas/wimbledon.html":    ("..", "areas"),
    "areas/mitcham.html":      ("..", "areas"),
    "areas/caterham.html":     ("..", "areas"),
}

fixed = 0
for rel, (prefix_dot, active) in files.items():
    path = ROOT / rel
    if not path.exists():
        print(f"  SKIP (missing): {rel}")
        continue
    html = path.read_text()
    # Prefix: "./" or "../"
    p = "./" if prefix_dot == "." else "../"
    new_nav = nav_for(p, active)
    new_html, n = NAV_RE.subn(new_nav, html)
    if n > 0:
        path.write_text(new_html)
        print(f"  fixed nav in {rel} ({n} block)")
        fixed += 1
    else:
        print(f"  NO MATCH: {rel}")

print(f"\nDone — fixed nav in {fixed} files.")
