#!/usr/bin/env python3
"""Generate the 6 utility pages: about, contact, faq, permits, terms, privacy."""
from pathlib import Path
HERE = Path(__file__).parent

# Shared shell — every utility page is built from this
def shell(title, description, active_label, content_html, page_styles=""):
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>{title} | Henry Woods Skip Hire</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="./assets/css/main.css">
<style>
.util-hero{{padding:72px 0 48px;background:linear-gradient(180deg,var(--paper) 0%,var(--paper-warm) 100%)}}
.util-hero__inner{{max-width:880px;margin:0 auto;padding:0 28px}}
.util-hero .breadcrumb{{font-size:13px;color:var(--ink-muted);font-weight:600;margin-bottom:20px;display:flex;align-items:center;gap:8px}}
.util-hero .breadcrumb a{{color:var(--ink-muted)}}.util-hero .breadcrumb a:hover{{color:var(--hw-red)}}
.util-hero .breadcrumb .sep{{color:var(--ink-faint)}}
.util-hero h1{{font-size:clamp(36px,5vw,56px);line-height:1.05;letter-spacing:-0.025em;color:var(--ink);margin:0 0 18px}}
.util-hero h1 em{{font-style:normal;color:var(--hw-red);font-weight:800}}
.util-hero .lead{{font-size:18px;line-height:1.55;color:var(--ink-muted);margin:0;max-width:54ch}}
.prose{{max-width:760px;margin:0 auto;padding:64px 28px}}
.prose h2{{font-family:"Panton","Sora",sans-serif;font-weight:800;font-size:clamp(24px,2.6vw,32px);color:var(--ink);margin:48px 0 16px;letter-spacing:-0.015em;line-height:1.2}}
.prose h2:first-child{{margin-top:0}}
.prose h3{{font-family:"Panton","Sora",sans-serif;font-weight:700;font-size:20px;color:var(--ink);margin:32px 0 12px;letter-spacing:-0.005em}}
.prose p{{font-size:17px;line-height:1.7;color:var(--ink);margin:0 0 18px;max-width:none}}
.prose p strong{{color:var(--hw-red);font-weight:700}}
.prose ul{{padding-left:20px;margin:0 0 24px;display:flex;flex-direction:column;gap:10px}}
.prose li{{font-size:16px;line-height:1.65;color:var(--ink)}}
.prose li strong{{color:var(--ink);font-weight:700}}
{page_styles}
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
    <a href="./mockup.html" class="brand"><img src="./assets/logo.png" alt="Henry Woods Skip Hire" width="260" height="73"></a>
    <div class="nav__menu">
      <a href="./skip-hire.html"{' class="is-active"' if active_label == 'skip-hire' else ''}>Skip hire</a>
      <a href="./skip-hire.html#sizes">Skip sizes</a>
      <a href="./mockup.html#how">How it works</a>
      <a href="./areas/index.html">Areas we cover</a>
      <a href="./contact.html"{' class="is-active"' if active_label == 'contact' else ''}>Contact</a>
    </div>
    <div class="nav__cta">
      <a href="tel:02033699540" class="btn btn--phone">0203 369 9540</a>
      <a href="./book.html" class="btn btn--primary btn--small">Book online</a>
      <button class="nav__burger" id="burger"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>

{content_html}

<section class="cta-strip">
  <div class="container cta-strip__row">
    <h3>Ready when you are. The yard&rsquo;s open.</h3>
    <div class="cta-strip__actions">
      <a href="./book.html" class="btn btn--primary">Book your skip</a>
      <a href="tel:02033699540" class="btn btn--ghost">Call 0203 369 9540</a>
    </div>
  </div>
</section>

<footer>
  <div class="container">
    <div class="footer__grid">
      <div class="footer__brand">
        <img src="./assets/logo.png" alt="Henry Woods Skip Hire" width="220" height="62">
        <p>Henry Woods Waste Management Ltd. Family-run skip hire from Mill Lane, Croydon, since 1996. Environment Agency licensed waste carrier.</p>
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
          <li><a href="./sizes/4-yard.html">4 yard skip</a></li>
          <li><a href="./sizes/6-yard.html">6 yard skip</a></li>
          <li><a href="./sizes/8-yard.html">8 yard skip</a></li>
          <li><a href="./sizes/12-yard.html">12 yard skip</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h5>About</h5>
        <ul>
          <li><a href="./about.html">About us</a></li>
          <li><a href="./permits.html">Council permits</a></li>
          <li><a href="./faq.html">FAQs</a></li>
          <li><a href="./terms.html">Terms</a></li>
          <li><a href="./privacy.html">Privacy</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__legal">
      <span>&copy; 2026 Henry Woods Waste Management Ltd. &nbsp;&middot;&nbsp; Company No. 03244917 &nbsp;&middot;&nbsp; VAT GB 654 8721 03</span>
      <span>Designed by Nu Media Group</span>
    </div>
  </div>
</footer>
<script>
const nav=document.getElementById('nav'),burger=document.getElementById('burger');
burger.addEventListener('click',()=>{{const open=nav.classList.toggle('is-open');burger.setAttribute('aria-expanded',open);}});
nav.querySelectorAll('.nav__menu a').forEach(a=>a.addEventListener('click',()=>nav.classList.remove('is-open')));
document.querySelectorAll('.faq__q').forEach(q=>q.addEventListener('click',()=>q.parentElement.classList.toggle('is-open')));
</script>
</body>
</html>
'''

# ========== ABOUT ==========
about_content = '''
<header class="util-hero">
  <div class="util-hero__inner">
    <nav class="breadcrumb"><a href="./mockup.html">Home</a><span class="sep">/</span><span>About</span></nav>
    <p class="eyebrow">About Henry Woods</p>
    <h1 style="margin-top:18px"><em>Three decades</em> on the same Mill Lane yard.</h1>
    <p class="lead">Henry Woods Waste Management is a family-run skip hire business operating from Croydon since 1996. Same yard. Same number. Same drivers, most weeks.</p>
  </div>
</header>

<article class="prose">
  <h2>The story</h2>
  <p>Henry Woods opened the yard at Mill Lane Trading Estate in 1996 with one second-hand lorry and a phone line. Three decades later we're still on the same site, still run by the family, and now serving every postcode from Croydon out to Wimbledon and Sutton.</p>
  <p>The business has grown — we run <strong>three lorries</strong>, deliver roughly <strong>40 skips a week</strong>, and recycle <strong>95% of what comes back to the yard</strong>. But the operation has stayed deliberately small. We know our drivers, we know our regular customers, and we still answer the yard phone in person.</p>

  <h2>What we do</h2>
  <p>Skip hire is the whole business. We deliver <strong>4, 6, 8 and 12 yard skips</strong> across south London for domestic and trade customers, handle the council permit if the skip's going on the road, and take the waste back to the Mill Lane yard for hand-sorting and recycling.</p>
  <p>We don't subcontract. The lorry that turns up is one of our three. The driver is one of our drivers. The skip on your drive is one we maintain, paint and brand ourselves.</p>

  <h2>Recycling commitment</h2>
  <p>We operate to Environment Agency licence <strong>CBDU172893</strong>. Every load returns to the Mill Lane yard, gets hand-sorted, and is rerouted to the right recycling stream — wood, metals, aggregates, plasterboard, cardboard. Less than 5% of what we collect ends up in landfill.</p>
  <ul>
    <li><strong>Wood</strong> — chipped and reused for biomass and panel manufacturing</li>
    <li><strong>Metals</strong> — separated, baled and sent to UK foundries</li>
    <li><strong>Aggregates &amp; rubble</strong> — crushed and reused as construction sub-base</li>
    <li><strong>Plasterboard</strong> — sent to specialist recyclers for gypsum recovery</li>
    <li><strong>Cardboard &amp; paper</strong> — baled and sold into the paper recycling chain</li>
  </ul>

  <h2>The yard</h2>
  <p>Mill Lane Trading Estate sits just off the A23 in central Croydon, CR0&nbsp;4AA. It's where the lorries are loaded each morning, where the waste comes back for sorting, and where the team have a brew at 7am before the first deliveries go out.</p>
  <p>Visitors are welcome to drop in — phone first so we know to expect you.</p>

  <h2>The accreditations</h2>
  <ul>
    <li><strong>Environment Agency</strong> — Licensed waste carrier CBDU172893</li>
    <li><strong>Information Commissioner's Office</strong> — Data protection registration ZA298415</li>
    <li><strong>SafeContractor</strong> — Accredited contractor for trade and commercial work</li>
  </ul>

  <h2>Contact</h2>
  <p><strong>Phone the yard:</strong> 0203 369 9540 (Mon–Fri 07:00–17:30, Sat 07:30–13:00)<br>
  <strong>Email:</strong> info@henrywoods.co.uk<br>
  <strong>WhatsApp:</strong> 0203 369 9540 — send a photo of your access if you're not sure what'll fit</p>
</article>
'''

# ========== CONTACT ==========
contact_content = '''
<header class="util-hero">
  <div class="util-hero__inner">
    <nav class="breadcrumb"><a href="./mockup.html">Home</a><span class="sep">/</span><span>Contact</span></nav>
    <p class="eyebrow">Contact the yard</p>
    <h1 style="margin-top:18px">Call us, or <em>book online</em>.</h1>
    <p class="lead">The yard phone is answered by a person — not a queue. Online booking is faster if you know what size you need.</p>
  </div>
</header>

<section style="padding:64px 0;background:var(--canvas)">
  <div class="container" style="max-width:1100px">
    <div style="display:grid;grid-template-columns:1.1fr 0.9fr;gap:48px">
      <div style="display:flex;flex-direction:column;gap:24px">
        <div style="padding:28px;background:var(--paper);border-radius:var(--r-md);border:1px solid var(--hairline)">
          <p class="eyebrow" style="margin-bottom:12px">Phone</p>
          <p style="font-family:'Panton','Sora',sans-serif;font-weight:800;font-size:36px;line-height:1;color:var(--hw-red);letter-spacing:-0.02em;margin:0 0 8px"><a href="tel:02033699540" style="color:inherit">0203 369 9540</a></p>
          <p style="font-size:14px;color:var(--ink-muted);margin:0">Mon&ndash;Fri 07:00&ndash;17:30 &middot; Sat 07:30&ndash;13:00</p>
        </div>
        <div style="padding:28px;background:var(--paper);border-radius:var(--r-md);border:1px solid var(--hairline)">
          <p class="eyebrow" style="margin-bottom:12px">Email</p>
          <p style="font-family:'Panton','Sora',sans-serif;font-weight:700;font-size:22px;color:var(--ink);margin:0 0 8px"><a href="mailto:info@henrywoods.co.uk" style="color:inherit">info@henrywoods.co.uk</a></p>
          <p style="font-size:14px;color:var(--ink-muted);margin:0">For account enquiries, trade quotes and non-urgent questions. Replies within a working day.</p>
        </div>
        <div style="padding:28px;background:var(--paper);border-radius:var(--r-md);border:1px solid var(--hairline)">
          <p class="eyebrow" style="margin-bottom:12px">The yard</p>
          <p style="font-family:'Panton','Sora',sans-serif;font-weight:700;font-size:18px;color:var(--ink);margin:0 0 8px;line-height:1.4">Unit 9, Mill Lane Trading Estate,<br>Mill Lane, Croydon CR0&nbsp;4AA</p>
          <p style="font-size:14px;color:var(--ink-muted);margin:0">Just off the A23. Visitors welcome &mdash; phone first so we know to expect you.</p>
        </div>
      </div>
      <div>
        <form style="background:var(--paper);border-radius:var(--r-md);border:1px solid var(--hairline);padding:32px">
          <h3 style="font-family:'Panton','Sora',sans-serif;font-weight:800;font-size:22px;color:var(--ink);margin:0 0 8px;letter-spacing:-0.01em">Send a message</h3>
          <p style="font-size:14px;color:var(--ink-muted);margin:0 0 24px">For booking enquiries it's faster to call the yard.</p>
          <label style="display:block;margin-bottom:16px">
            <span style="display:block;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-muted);margin-bottom:6px">Your name</span>
            <input type="text" style="width:100%;height:48px;padding:0 14px;background:var(--canvas);border:2px solid var(--hairline);border-radius:var(--r-xs);font:inherit;font-size:15px;color:var(--ink)">
          </label>
          <label style="display:block;margin-bottom:16px">
            <span style="display:block;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-muted);margin-bottom:6px">Email</span>
            <input type="email" style="width:100%;height:48px;padding:0 14px;background:var(--canvas);border:2px solid var(--hairline);border-radius:var(--r-xs);font:inherit;font-size:15px;color:var(--ink)">
          </label>
          <label style="display:block;margin-bottom:16px">
            <span style="display:block;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-muted);margin-bottom:6px">Phone (optional)</span>
            <input type="tel" style="width:100%;height:48px;padding:0 14px;background:var(--canvas);border:2px solid var(--hairline);border-radius:var(--r-xs);font:inherit;font-size:15px;color:var(--ink)">
          </label>
          <label style="display:block;margin-bottom:20px">
            <span style="display:block;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-muted);margin-bottom:6px">Your message</span>
            <textarea rows="5" style="width:100%;padding:14px;background:var(--canvas);border:2px solid var(--hairline);border-radius:var(--r-xs);font:inherit;font-size:15px;color:var(--ink);resize:vertical"></textarea>
          </label>
          <button type="submit" class="btn btn--primary" style="width:100%">Send message</button>
          <p style="font-size:12px;color:var(--ink-faint);text-align:center;margin:14px 0 0">Form submissions go to info@henrywoods.co.uk &middot; we reply within a working day.</p>
        </form>
      </div>
    </div>
  </div>
</section>
'''

# ========== FAQ ==========
faq_items = [
    ("Do I need a permit to put a skip on the road?", "If your skip is going on a public road or pavement, yes — the local council issues a permit. We apply for it on your behalf when you book, and include the cost in your total before you pay. On a private drive, no permit is needed."),
    ("What can't I put in the skip?", "Fridges & freezers, TVs & monitors, tyres, asbestos, batteries, paint and chemicals, anything containing fuel. Everything else — including plasterboard, soil and rubble — goes in (tell us in advance for the heavy ones so we bring the right lorry)."),
    ("How long can I keep the skip?", "Standard hire is 14 days. Need longer? Extension is £15 per day. Need it gone sooner? Phone the yard the day before and we'll bring forward the collection at no extra cost."),
    ("Can I get same-day delivery?", "Often yes, depending on lorry availability. Best to ring the yard on 0203 369 9540 before 11am. Online bookings before 14:00 are confirmed for next-day delivery."),
    ("What if the skip won't fit through my access?", "If you're unsure, send us a photo via WhatsApp on 0203 369 9540 before booking. We'd rather check than turn up with the wrong lorry. Tight access? A 4-yard usually clears most domestic driveways."),
    ("Will the skip damage my driveway?", "On concrete, tarmac and block paving, no — we use timber bearers under the feet to spread the weight. On gravel or grass, the marks will be visible while the skip's there. Mention surface in the booking and our driver will plan accordingly."),
    ("Do you do trade accounts?", "Yes — builders, developers and trade customers can open an account with monthly billing, multi-skip discounts and priority booking. Phone the yard or email info@henrywoods.co.uk to set up."),
    ("What happens to my waste?", "Every load comes back to the Mill Lane yard and is hand-sorted. Wood, metals, aggregates and plasterboard are separated into recycling streams. We recycle 95% — only the unsortable residue ends up in landfill."),
    ("How heavy can I load a skip?", "There's a fill line on each skip — load above it and we'll need to remove the excess at the yard, and the driver may refuse collection. Heavy waste (soil, rubble, concrete) is fine in 4/6/8 yard skips but should not be in a 12 yard."),
    ("Do you offer wait-and-load?", "Yes — we drop the skip, you load it while we wait, we take it away the same hour. Useful where road permits aren't possible. Phone for pricing."),
    ("How do I pay?", "Card (Visa/Mastercard), Apple Pay, Google Pay, BACS or trade account. Card payments are processed via Stripe — no surcharges."),
    ("Are you VAT-registered?", "Yes. VAT registration GB 654 8721 03. All prices on the site include VAT. VAT invoices issued for every booking."),
]

faq_content = '''
<header class="util-hero">
  <div class="util-hero__inner">
    <nav class="breadcrumb"><a href="./mockup.html">Home</a><span class="sep">/</span><span>FAQs</span></nav>
    <p class="eyebrow">Frequently asked</p>
    <h1 style="margin-top:18px">Skip hire questions, <em>answered</em>.</h1>
    <p class="lead">If your question isn't here, phone the yard on 0203 369 9540 — answered by a person, not a queue.</p>
  </div>
</header>

<section style="padding:64px 0 0;background:var(--canvas)">
  <div class="container" style="max-width:880px">
    <div class="faq">
'''
for i, (q, a) in enumerate(faq_items):
    open_cls = " is-open" if i == 0 else ""
    faq_content += f'''      <div class="faq__item{open_cls}">
        <button class="faq__q">{q}<span class="faq__plus" aria-hidden="true"></span></button>
        <div class="faq__a"><div>{a}</div></div>
      </div>
'''
faq_content += '''    </div>
  </div>
</section>
<section style="padding:48px 0 64px;background:var(--canvas)">
  <div class="container" style="max-width:880px;text-align:center">
    <p style="font-size:18px;color:var(--ink-muted);margin:0 0 16px">Still got a question?</p>
    <a href="tel:02033699540" class="btn btn--primary">Phone the yard: 0203 369 9540</a>
  </div>
</section>
'''

# ========== PERMITS ==========
permits_content = '''
<header class="util-hero">
  <div class="util-hero__inner">
    <nav class="breadcrumb"><a href="./mockup.html">Home</a><span class="sep">/</span><span>Council permits</span></nav>
    <p class="eyebrow">Council permits</p>
    <h1 style="margin-top:18px">If it's going on the road, <em>we sort the permit</em>.</h1>
    <p class="lead">Forgetting the permit is the #1 way skip hire goes wrong. We handle it on your behalf for every south London council we cover — Croydon, Sutton, Merton, Lambeth, Wandsworth.</p>
  </div>
</header>

<article class="prose">
  <h2>When do you need a permit?</h2>
  <p>Any skip placed on a <strong>public road, pavement, grass verge or other public land</strong> requires a permit issued by the local council. Skips placed on private driveways do not need a permit.</p>
  <p>The Highways Act 1980 (Section 139) is the legal basis. Skips on the public highway without a permit are illegal and can result in immediate removal — at the skip owner's cost.</p>

  <h2>What we do</h2>
  <ul>
    <li><strong>We apply on your behalf</strong> for every booking that needs one. You don't need to phone the council yourself or fill out any forms.</li>
    <li><strong>Cost is included before you pay.</strong> The permit fee is added to your booking total at the review step. Typical permit cost: £40–£75 depending on council.</li>
    <li><strong>Lead time:</strong> most councils issue within 3 working days. If you want the skip down by Friday, order on Monday or Tuesday.</li>
    <li><strong>Reflective markings and night-time lighting</strong> are added by our driver as part of the drop-off — both required under the Act.</li>
    <li><strong>Bay suspensions</strong> (where the parking bay your skip needs to occupy is in use) are arranged by us at council rates.</li>
  </ul>

  <h2>Councils we apply for permits with</h2>
  <ul>
    <li><strong>Croydon Council</strong> — permits handled in-house; typical fee £55, 2 working days</li>
    <li><strong>Sutton Council</strong> — permits handled in-house; typical fee £45, 3 working days</li>
    <li><strong>Merton Council</strong> (covers Wimbledon &amp; Mitcham) — permits handled in-house; typical fee £60, 3 working days</li>
    <li><strong>Lambeth Council</strong> — permits handled in-house; typical fee £75, 3–5 working days</li>
    <li><strong>Wandsworth Council</strong> — permits handled in-house; typical fee £70, 3 working days</li>
    <li><strong>Tandridge District Council</strong> (covers Caterham) — permits handled in-house; typical fee £40, 5 working days</li>
  </ul>
  <p>If you're at the edge of these areas, phone the yard on 0203 369 9540 and we'll confirm whether we can sort the permit for your address.</p>

  <h2>What you need to give us</h2>
  <ul>
    <li><strong>Your full postal address</strong> — including building number and street name (we use this to query the council's permit map)</li>
    <li><strong>Exactly where the skip will sit</strong> — outside which house, on which side of the road. A photo via WhatsApp helps.</li>
    <li><strong>Drop-off and collection dates</strong> — permits are issued for specific date windows</li>
    <li><strong>Skip size</strong> — permit fees can vary slightly by size</li>
  </ul>

  <h2>Common permit gotchas</h2>
  <h3>Controlled parking zones (CPZs)</h3>
  <p>If your road is in a CPZ, the council may require a <strong>bay suspension</strong> as well as a permit. This stops other vehicles from parking in the bay the skip will occupy. We arrange this on your behalf, charged at council rates.</p>
  <h3>Bus routes, tram routes and red routes</h3>
  <p>Skips are not allowed on these. If your address is on one, we'll need to find an alternative drop-off point — usually the nearest side street.</p>
  <h3>Conservation areas</h3>
  <p>Some councils restrict skip placement in conservation areas (Wimbledon Village, parts of Croydon, Sutton's Mulgrave Road CA). These take longer to permit but are not impossible. Phone the yard to discuss.</p>
</article>
'''

# ========== TERMS ==========
terms_content = '''
<header class="util-hero">
  <div class="util-hero__inner">
    <nav class="breadcrumb"><a href="./mockup.html">Home</a><span class="sep">/</span><span>Terms</span></nav>
    <p class="eyebrow">Terms of business</p>
    <h1 style="margin-top:18px">Terms &amp; <em>conditions</em>.</h1>
    <p class="lead">These terms apply to all skip hire bookings made with Henry Woods Waste Management Ltd. Last updated: June 2026.</p>
  </div>
</header>

<article class="prose">
  <p style="background:#FFF6EE;border-left:4px solid var(--hw-orange);padding:18px 22px;border-radius:var(--r-xs);font-size:14px"><strong style="color:var(--hw-orange)">PLACEHOLDER:</strong> This page contains template T&amp;Cs that should be reviewed by a solicitor before going live. Aaron — flag to your legal contact before launch.</p>

  <h2>1. The contract</h2>
  <p>By placing a booking with Henry Woods Waste Management Ltd ("we", "us", "the Company") you enter into a contract under these terms. The contract is formed when we send you a booking confirmation by email.</p>

  <h2>2. Hire period</h2>
  <p>Standard hire is 14 calendar days from drop-off. Extensions are charged at £15 per day. Early collections at no extra cost subject to 24 hours' notice.</p>

  <h2>3. What can go in the skip</h2>
  <p>You agree not to load the skip with: asbestos, fridges or freezers, TVs or monitors, tyres, batteries, paint or chemicals, fuel or any item containing fuel, hazardous waste of any kind. The Company reserves the right to refuse collection of any skip containing prohibited items, or to charge for safe removal.</p>

  <h2>4. Loading and weight limits</h2>
  <p>The skip must not be loaded above the fill line marked on the side. Heavy waste (soil, rubble, concrete) is permitted only in 4, 6 and 8 yard skips, not 12 yard skips.</p>

  <h2>5. Permits and access</h2>
  <p>You are responsible for ensuring safe access to the drop-off location. If the Company arranges a council permit on your behalf, you remain responsible for the skip's compliance with the permit conditions (lighting, reflective markings, location).</p>

  <h2>6. Damage</h2>
  <p>The Company is not liable for damage to private driveways, paving or surfaces arising from the placement of the skip, except where caused by negligence on the part of our drivers.</p>

  <h2>7. Payment</h2>
  <p>Payment in full is required at booking unless you hold a trade account with us. Card payments are processed by Stripe Payments Europe Ltd. Trade accounts are billed monthly with payment due within 30 days.</p>

  <h2>8. Cancellation</h2>
  <p>Cancellations more than 24 hours before scheduled drop-off: full refund. Cancellations within 24 hours: 50% refund. Cancellations after the lorry has been dispatched: no refund.</p>

  <h2>9. Liability</h2>
  <p>Our total liability under any single booking is limited to the amount paid for that booking, except in cases of death, personal injury, or where liability cannot be limited under UK law.</p>

  <h2>10. Governing law</h2>
  <p>These terms are governed by the laws of England and Wales.</p>

  <h2>Contact</h2>
  <p>Henry Woods Waste Management Ltd, Unit 9 Mill Lane Trading Estate, Mill Lane, Croydon CR0&nbsp;4AA. Company number 03244917. VAT GB 654 8721 03. Email: info@henrywoods.co.uk.</p>
</article>
'''

# ========== PRIVACY ==========
privacy_content = '''
<header class="util-hero">
  <div class="util-hero__inner">
    <nav class="breadcrumb"><a href="./mockup.html">Home</a><span class="sep">/</span><span>Privacy</span></nav>
    <p class="eyebrow">Privacy policy</p>
    <h1 style="margin-top:18px">Your data, <em>handled properly</em>.</h1>
    <p class="lead">We collect only what we need to do the job. We don't sell your data, we don't share it with marketers, and we delete it when we no longer need it. Last updated: June 2026.</p>
  </div>
</header>

<article class="prose">
  <p style="background:#FFF6EE;border-left:4px solid var(--hw-orange);padding:18px 22px;border-radius:var(--r-xs);font-size:14px"><strong style="color:var(--hw-orange)">PLACEHOLDER:</strong> This page contains a template GDPR-compliant privacy policy that should be reviewed by a DPO or solicitor before going live.</p>

  <h2>Who we are</h2>
  <p>Henry Woods Waste Management Ltd is the data controller for any personal data collected through this website or through booking with us by phone or email. We are registered with the UK Information Commissioner's Office under registration <strong>ZA298415</strong>.</p>

  <h2>What we collect</h2>
  <ul>
    <li><strong>Booking data</strong> — name, address, phone, email, payment details (processed by Stripe, not stored by us)</li>
    <li><strong>Communications</strong> — emails, phone calls (not recorded), WhatsApp messages</li>
    <li><strong>Website usage</strong> — anonymous analytics via Google Analytics 4 (IP-anonymised)</li>
    <li><strong>Cookies</strong> — only those strictly necessary for the booking flow plus optional analytics cookies (opt-in)</li>
  </ul>

  <h2>Why we collect it</h2>
  <ul>
    <li>To fulfil your skip hire booking (contractual basis)</li>
    <li>To apply for a council permit on your behalf if requested (contractual)</li>
    <li>To issue VAT invoices (legal obligation)</li>
    <li>To improve the website (legitimate interest, anonymous data only)</li>
  </ul>

  <h2>How long we keep it</h2>
  <ul>
    <li><strong>Booking and invoice data</strong> — 7 years (UK tax retention requirement)</li>
    <li><strong>Email and WhatsApp messages</strong> — 2 years after last contact</li>
    <li><strong>Anonymous analytics</strong> — 14 months</li>
  </ul>

  <h2>Who we share it with</h2>
  <p>We never sell your data. We share booking data only with:</p>
  <ul>
    <li><strong>Stripe Payments Europe Ltd</strong> — to process card payments</li>
    <li><strong>The relevant local council</strong> — when applying for a road permit on your behalf</li>
    <li><strong>Our accountant</strong> — for tax and bookkeeping purposes</li>
    <li><strong>HMRC</strong> — for VAT and corporation tax filings, where required by law</li>
  </ul>

  <h2>Your rights</h2>
  <p>Under UK GDPR you have the right to: access your data, correct inaccuracies, request deletion (subject to our legal retention requirements), object to processing, and lodge a complaint with the Information Commissioner's Office (ico.org.uk).</p>
  <p>To exercise any of these rights, email <strong>info@henrywoods.co.uk</strong> or phone the yard on 0203 369 9540.</p>

  <h2>Cookies</h2>
  <p>We use the minimum cookies needed for the website to work. The booking flow uses sessionStorage to remember your selections between steps — this is deleted when you close the browser. Analytics cookies are opt-in via the cookie banner.</p>

  <h2>Contact</h2>
  <p>Data Controller: Henry Woods Waste Management Ltd, Unit 9 Mill Lane Trading Estate, Mill Lane, Croydon CR0&nbsp;4AA. Email: info@henrywoods.co.uk.</p>
</article>
'''

# ========== WRITE ALL FILES ==========
pages = [
    ("about.html", "About — Family-run skip hire from Mill Lane since 1996", "Henry Woods Waste Management Ltd — family-run skip hire from Mill Lane, Croydon since 1996. Three lorries, 95% recycling, Environment Agency licensed.", "about", about_content),
    ("contact.html", "Contact the yard — Phone, email and Mill Lane address", "Phone the Mill Lane yard on 0203 369 9540, email info@henrywoods.co.uk, or visit us at Unit 9 Mill Lane Trading Estate, Croydon CR0 4AA.", "contact", contact_content),
    ("faq.html", "FAQs — Skip hire questions answered", "Common skip hire questions answered — permits, what you can put in, hire periods, same-day delivery, trade accounts and more.", "faq", faq_content),
    ("permits.html", "Council permits for skip hire — we handle them", "If your skip needs to go on the road, we apply for the council permit on your behalf. Croydon, Sutton, Merton, Lambeth, Wandsworth and Tandridge covered.", "permits", permits_content),
    ("terms.html", "Terms & conditions", "Henry Woods Skip Hire terms and conditions of business. Cancellation, payment, what can and can't go in the skip, liability and contact details.", "terms", terms_content),
    ("privacy.html", "Privacy policy", "How Henry Woods handles your data. We collect only what we need, we don't sell it, and we delete it when we no longer need it.", "privacy", privacy_content),
]

for filename, title, desc, active, content in pages:
    out = HERE / filename
    out.write_text(shell(title, desc, active, content))
    print(f"  wrote {filename}")

print(f"\nDone — generated {len(pages)} utility pages.")
