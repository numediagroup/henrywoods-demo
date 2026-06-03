#!/usr/bin/env python3
"""Generate /areas/{croydon,sutton,wimbledon,mitcham,caterham}.html from _template.html"""
from pathlib import Path
HERE = Path(__file__).parent
TPL = (HERE / "_template.html").read_text()

AREAS = [
    {
        "slug": "croydon",
        "area": "Croydon",
        "headline_tail": "Two miles from the yard.",
        "lead": "Mill Lane is in Croydon — every CR postcode is on our doorstep. Same-day delivery available most weekdays, ring the yard before 11am.",
        "postcodes": ["CR0", "CR2", "CR3", "CR4", "CR5", "CR6", "CR7", "CR8", "CR9"],
        "miles": "0–4",
        "drops_pa": "2,400",
        "local_headline": "We've been delivering into Croydon longer than most builders have been trading.",
        "local_body": [
            "<p>The Mill Lane yard sits in <strong>CR0</strong>, which means every part of Croydon — Selsdon, Purley, Thornton Heath, South Croydon, Coulsdon, Sanderstead — is on our daily routes.</p>",
            "<p>We know the <strong>tight terraced streets</strong> of South Croydon, the <strong>permit-parking zones</strong> around the town centre, and which roads need a permit application started early. Bookings before 11am can usually be delivered same-day.</p>",
            "<p>Croydon Council permits handled in-house. Bay suspensions arranged where the kerb you need is in a controlled parking zone.</p>",
        ],
        "review_quote": "Booked at 11am, skip arrived next morning at 7:45am sharp. Driver reversed it onto an awkward Selsdon driveway like it was nothing.",
        "review_name": "Sarah Henderson",
        "review_meta": " &middot; Selsdon, Croydon",
    },
    {
        "slug": "sutton",
        "area": "Sutton",
        "headline_tail": "Family yard, four miles up the road.",
        "lead": "Skip hire across every SM postcode. We know the Sutton parking-zone rules and we apply for the Sutton Council permit on your behalf.",
        "postcodes": ["SM1", "SM2", "SM3", "SM4", "SM5", "SM6"],
        "miles": "3–6",
        "drops_pa": "1,200",
        "local_headline": "Cheam, Carshalton, Wallington — covered by the same yard, the same drivers.",
        "local_body": [
            "<p>From Mill Lane it's a 15-minute run to Sutton High Street. We're at Cheam Village and Carshalton Beeches inside an hour of dispatch.</p>",
            "<p>Sutton has more <strong>permit-parking zones</strong> than most south London boroughs, so the council permit step matters here. We apply on your behalf and have the paperwork in place before the driver sets off.</p>",
            "<p>Lots of <strong>1930s semi driveways</strong> in Sutton — usually fine for a 6 or 8 yard skip, but tight access for a 12. Send a photo via WhatsApp if you're not sure.</p>",
        ],
        "review_quote": "Sutton parking-zone permit sorted before I'd even hung up the phone. Driver was bang on time the next morning.",
        "review_name": "James Patterson",
        "review_meta": " &middot; Cheam, Sutton",
    },
    {
        "slug": "wimbledon",
        "area": "Wimbledon",
        "headline_tail": "SW19 and surrounding, daily.",
        "lead": "Skip hire across SW16, SW17, SW19 and SW20. Wimbledon, Tooting, Streatham and Raynes Park all on our weekday routes from the Croydon yard.",
        "postcodes": ["SW16", "SW17", "SW19", "SW20"],
        "miles": "5–8",
        "drops_pa": "900",
        "local_headline": "Wimbledon's older properties, Edwardian conversions and tight side returns — we know them.",
        "local_body": [
            "<p>The 10-mile run from Mill Lane to Wimbledon takes about 25 minutes outside rush hour. We're at SW19 first thing on weekday routes.</p>",
            "<p>Wimbledon has plenty of <strong>conservation-area restrictions</strong> and tight Victorian/Edwardian side returns. A 6 yard skip is usually the largest that'll fit a typical Wimbledon driveway — anything bigger and we recommend road placement with a Merton Council permit.</p>",
            "<p>Merton Council permit applications handled in-house. Allow 3 working days for the permit if the skip's going on the road.</p>",
        ],
        "review_quote": "Tight conservation-area side return and Henry Woods made it look easy. Permit sorted, skip dropped, gone again 14 days later.",
        "review_name": "Priya Tandon",
        "review_meta": " &middot; Wimbledon, SW19",
    },
    {
        "slug": "mitcham",
        "area": "Mitcham",
        "headline_tail": "CR4 and SW17 covered.",
        "lead": "Mitcham, Mitcham Common, Pollards Hill — covered daily from the Mill Lane yard. CR4 and the SW17 fringe.",
        "postcodes": ["CR4", "SW17"],
        "miles": "3–5",
        "drops_pa": "600",
        "local_headline": "Mid-density Mitcham streets. Some need a permit, some don't — we tell you which.",
        "local_body": [
            "<p>Mitcham sits between Croydon and Wimbledon — easy run from the yard, usually under 20 minutes.</p>",
            "<p>Most of <strong>CR4</strong> is residential driveway delivery — no permit. The <strong>SW17 fringe</strong> (Tooting border) sometimes needs a Merton Council permit. We'll tell you which applies when you give us the postcode.</p>",
            "<p>Trade accounts welcome — Mitcham has plenty of builders and we keep regular jobs on the schedule.</p>",
        ],
        "review_quote": "Got a 6 yard for the back garden refit. No fuss, no surprise charges. Just turned up and did the job.",
        "review_name": "Mike Kowalski",
        "review_meta": " &middot; Builder, Mitcham CR4",
    },
    {
        "slug": "caterham",
        "area": "Caterham",
        "headline_tail": "Surrey side of the M25, easy run.",
        "lead": "Caterham, Whyteleafe, Warlingham, Old Coulsdon — covered from Mill Lane, daily. CR3 and CR6 postcodes.",
        "postcodes": ["CR3", "CR6"],
        "miles": "5–8",
        "drops_pa": "450",
        "local_headline": "The Surrey hills don't put us off — most Caterham streets have proper drives, no permit needed.",
        "local_body": [
            "<p>Caterham is a 20-minute run from Mill Lane, mostly down the A22. We're at CR3 by 8am on most weekday routes.</p>",
            "<p>Compared to Croydon and Sutton, Caterham properties tend to have <strong>bigger drives and easier access</strong>, so we rarely need road permits here. That means lower total cost and a faster booking flow.</p>",
            "<p>Tandridge District Council handles permits in this area if needed — we apply on your behalf.</p>",
        ],
        "review_quote": "Big driveway in Old Coulsdon, ordered a 12 yard. Driver positioned it perfectly so we could load from both sides.",
        "review_name": "David & Helen Reid",
        "review_meta": " &middot; Old Coulsdon, CR5",
    },
]

for a in AREAS:
    html = TPL
    html = html.replace("{{AREA}}", a["area"])
    html = html.replace("{{HEADLINE_TAIL}}", a["headline_tail"])
    html = html.replace("{{LEAD}}", a["lead"])
    html = html.replace("{{POSTCODES_SHORT}}", ", ".join(a["postcodes"]))
    html = html.replace("{{POSTCODES_PILLS}}", "".join(f'<span class="pcode">{p}</span>' for p in a["postcodes"]))
    html = html.replace("{{MILES}}", a["miles"])
    html = html.replace("{{DROPS_PA}}", a["drops_pa"])
    html = html.replace("{{LOCAL_HEADLINE}}", a["local_headline"])
    html = html.replace("{{LOCAL_BODY}}", "\n        ".join(a["local_body"]))
    html = html.replace("{{REVIEW_QUOTE}}", a["review_quote"])
    html = html.replace("{{REVIEW_NAME}}", a["review_name"])
    html = html.replace("{{REVIEW_META}}", a["review_meta"])
    out = HERE / f"{a['slug']}.html"
    out.write_text(html)
    print(f"  wrote areas/{a['slug']}.html")

# Also generate the index/parent areas page
INDEX = '''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Areas We Cover — Skip Hire across south London | Henry Woods</title>
<meta name="description" content="Skip hire across Croydon, Sutton, Wimbledon, Mitcham and Caterham. 19 south London postcodes covered from the Mill Lane yard. Same-day or next-day delivery.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/main.css">
<style>
.area-index{padding:80px 0 64px;background:linear-gradient(180deg,var(--paper) 0%,var(--paper-warm) 100%)}
.area-index .breadcrumb{font-size:13px;color:var(--ink-muted);font-weight:600;margin-bottom:20px;display:flex;align-items:center;gap:8px}
.area-index .breadcrumb a{color:var(--ink-muted)}
.area-index h1{font-size:clamp(36px,5vw,58px);line-height:1.05;letter-spacing:-0.025em;color:var(--ink);margin:0 0 18px;max-width:18ch}
.area-index h1 em{font-style:normal;color:var(--hw-red);font-weight:800}
.area-index .lead{font-size:18px;line-height:1.55;color:var(--ink-muted);margin:0;max-width:54ch}

.area-cards{padding:80px 0;background:var(--canvas)}
.area-cards__grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
@media(max-width:960px){.area-cards__grid{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.area-cards__grid{grid-template-columns:1fr}}
.area-card{display:flex;flex-direction:column;gap:14px;padding:32px;background:var(--paper);border:2px solid var(--hairline);border-radius:var(--r-md);transition:all 240ms var(--ease-out);text-decoration:none;color:inherit}
.area-card:hover{border-color:var(--hw-red);transform:translateY(-3px);box-shadow:var(--shadow-card)}
.area-card__name{font-family:"Panton","Sora",sans-serif;font-weight:800;font-size:28px;color:var(--ink);margin:0;letter-spacing:-0.015em;display:flex;align-items:center;justify-content:space-between}
.area-card__name span{font-size:18px;color:var(--hw-red)}
.area-card__pcodes{display:flex;flex-wrap:wrap;gap:6px;margin:0}
.area-card__pcodes span{padding:4px 10px;background:var(--canvas);border:1px solid var(--hairline);border-radius:var(--r-pill);font-family:"Geist Mono",monospace;font-size:11px;font-weight:600;color:var(--ink-muted)}
.area-card__meta{font-size:14px;color:var(--ink-muted);line-height:1.5;margin:0}
.area-card__cta{display:inline-flex;align-items:center;gap:6px;font-size:14px;font-weight:700;color:var(--hw-red);margin-top:auto;padding-top:8px}
</style>
</head>
<body>

<div class="util">
  <div class="container util__row">
    <div class="util__left">
      <span class="util__item"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg> <a href="tel:02033699540"><strong style="color:var(--ink)">0203 369 9540</strong></a></span>
    </div>
    <div class="util__right">
      <span class="hide-mob">Mon&ndash;Fri 07:00&ndash;17:30 &nbsp;&middot;&nbsp; Sat 07:30&ndash;13:00</span>
    </div>
  </div>
</div>

<nav class="nav" id="nav">
  <div class="container nav__row">
    <a href="../mockup.html" class="brand"><img src="../assets/logo.png" alt="Henry Woods Skip Hire" width="260" height="73"></a>
    <div class="nav__menu">
      <a href="../skip-hire.html">Skip hire</a>
      <a href="../skip-hire.html#sizes">Skip sizes</a>
      <a href="../mockup.html#how">How it works</a>
      <a href="./index.html" class="is-active">Areas we cover</a>
      <a href="../mockup.html#contact">Contact</a>
    </div>
    <div class="nav__cta">
      <a href="tel:02033699540" class="btn btn--phone">0203 369 9540</a>
      <a href="../book.html" class="btn btn--primary btn--small">Book online</a>
      <button class="nav__burger" id="burger"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>

<header class="area-index">
  <div class="container">
    <nav class="breadcrumb"><a href="../mockup.html">Home</a><span class="sep">/</span><span>Areas we cover</span></nav>
    <p class="eyebrow">Areas we cover</p>
    <h1 style="margin-top:18px">Skip hire across <em>south London</em>.</h1>
    <p class="lead">From the Mill Lane yard we cover 19 postcodes across five core areas. Same-day or next-day delivery to all of them. Pick your area below to see local notes, the postcodes we serve and a review from a recent customer.</p>
  </div>
</header>

<section class="area-cards">
  <div class="container">
    <div class="area-cards__grid">
'''

for a in AREAS:
    INDEX += f'''      <a href="./{a['slug']}.html" class="area-card">
        <h3 class="area-card__name">{a['area']} <span>{a['miles']} mi</span></h3>
        <div class="area-card__pcodes">{"".join(f"<span>{p}</span>" for p in a["postcodes"])}</div>
        <p class="area-card__meta">{a['drops_pa']}+ skips delivered in {a['area']} last year. Same yard, same family, same number.</p>
        <span class="area-card__cta">Skip hire in {a['area']} &rarr;</span>
      </a>
'''

INDEX += '''    </div>
  </div>
</section>

<section class="cta-strip">
  <div class="container cta-strip__row">
    <h3>Outside these areas? Phone the yard.</h3>
    <div class="cta-strip__actions">
      <a href="../book.html" class="btn btn--primary">Book a skip</a>
      <a href="tel:02033699540" class="btn btn--ghost">Call 0203 369 9540</a>
    </div>
  </div>
</section>

<footer id="contact">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__brand">
        <img src="../assets/logo.png" alt="Henry Woods Skip Hire" width="220" height="62">
        <p>Henry Woods Waste Management Ltd. Family-run skip hire from Mill Lane, Croydon, since 1996. EA licensed waste carrier.</p>
        <div class="accreds"><span>EA · CBDU172893</span><span>ICO · ZA298415</span><span>SafeContractor</span></div>
      </div>
      <div class="footer__col">
        <h5>Contact the yard</h5>
        <ul>
          <li class="mono">0203 369 9540</li>
          <li><a href="mailto:info@henrywoods.co.uk">info@henrywoods.co.uk</a></li>
          <li>Unit 9, Mill Lane Trading Estate, Mill Lane, Croydon CR0 4AA</li>
        </ul>
      </div>
      <div class="footer__col">
        <h5>Sizes</h5>
        <ul>
          <li><a href="../sizes/4-yard.html">4 yard skip</a></li>
          <li><a href="../sizes/6-yard.html">6 yard skip</a></li>
          <li><a href="../sizes/8-yard.html">8 yard skip</a></li>
          <li><a href="../sizes/12-yard.html">12 yard skip</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h5>Areas</h5>
        <ul>
'''
for a in AREAS:
    INDEX += f'          <li><a href="./{a["slug"]}.html">{a["area"]}</a></li>\n'
INDEX += '''        </ul>
      </div>
    </div>
    <div class="footer__legal">
      <span>&copy; 2026 Henry Woods Waste Management Ltd. &nbsp;&middot;&nbsp; Company No. 03244917</span>
      <span>Designed by Nu Media Group</span>
    </div>
  </div>
</footer>
<script>
const nav=document.getElementById('nav'),burger=document.getElementById('burger');
burger.addEventListener('click',()=>{const open=nav.classList.toggle('is-open');burger.setAttribute('aria-expanded',open);});
nav.querySelectorAll('.nav__menu a').forEach(a=>a.addEventListener('click',()=>nav.classList.remove('is-open')));
</script>
</body>
</html>
'''

(HERE / "index.html").write_text(INDEX)
print(f"  wrote areas/index.html")
print(f"\nDone — generated {len(AREAS)} area pages + parent index.")
