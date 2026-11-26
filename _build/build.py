#!/usr/bin/env python3
"""One-off generator for the static Lodges of Round Table site.
Writes plain HTML into ../site. The output needs no build step on GitHub Pages."""
import os, pathlib, textwrap

OUT = pathlib.Path(__file__).resolve().parent.parent
YEAR = 2026

NAV = [
    ("/", "Home", "home"),
    ("/lodges/", "The Lodges", "lodges"),
    ("/history/", "History", "history"),
    ("/cardiff-2026/", "Cardiff 2026", "cardiff-2026"),
    ("/contact-us/", "Contact", "contact"),
]

def page(path, title, body, active="", description="", hero=None):
    nav = "\n".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if key == active else ""}>{label}</a></li>'
        for href, label, key in NAV
    )
    hero_html = ""
    if hero:
        img, kicker, heading, sub = hero[:4]
        emblem = len(hero) > 4 and hero[4]
        style = f' style="--hero:url(\'/images/{img}\')"' if img else ""
        hero_html = f"""
<header class="hero"{style}>
  <div class="wrap hero-inner{' has-emblem' if emblem else ''}">
    {'<img class="hero-emblem" src="/images/emblem-light.png" alt="Lodges of Round Table emblem" width="181" height="204">' if emblem else ''}
    {f'<p class="kicker">{kicker}</p>' if kicker else ''}
    <h1>{heading}</h1>
    {f'<p class="lede">{sub}</p>' if sub else ''}
  </div>
</header>"""
    else:
        hero_html = f"""
<header class="page-head">
  <div class="wrap"><h1>{title}</h1></div>
</header>"""
    full_title = "Lodges of Round Table" if path == "" else f"{title} | Lodges of Round Table"
    html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description or 'Lodges of Round Table: Masonic lodges founded by members of the Round Table movement.'}">
<meta property="og:title" content="{full_title}">
<meta property="og:image" content="https://www.lodgesofroundtable.uk/images/logo.png">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#13233f">
<link rel="stylesheet" href="/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
<div class="topbar">
  <div class="wrap topbar-inner">
    <a class="brand" href="/"><img src="/images/emblem-light.png" alt="" width="50" height="56"><span>Lodges of Round Table</span></a>
    <nav aria-label="Main"><ul>{nav}</ul></nav>
  </div>
</div>
{hero_html}
<main id="main">
{textwrap.dedent(body).strip()}
</main>
<footer class="site-foot">
  <div class="wrap foot-inner">
    <div>
      <strong>Lodges of Round Table</strong><br>
      <a href="mailto:lodgesofroundtable@gmail.com">lodgesofroundtable@gmail.com</a>
    </div>
    <ul class="social">
      <li><a href="https://www.facebook.com/SouthWalesMason">Facebook</a></li>
      <li><a href="https://www.instagram.com/southwales_craft_ra/">Instagram</a></li>
      <li><a href="https://x.com/southwalesmason">X</a></li>
    </ul>
    <p class="copy">&copy; {YEAR} Lodges of Round Table</p>
  </div>
</footer>
</body>
</html>
"""
    target = OUT / path / "index.html" if path else OUT / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")

def redirect(old, new):
    target = OUT / old / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(f"""<!DOCTYPE html>
<html lang="en-GB"><head><meta charset="utf-8">
<title>Moved</title>
<link rel="canonical" href="{new}">
<meta http-equiv="refresh" content="0; url={new}">
<meta name="robots" content="noindex">
</head><body><p>This page has moved to <a href="{new}">{new}</a>.</p></body></html>
""", encoding="utf-8")

def figure(img, alt):
    return f'<figure class="photo"><img src="/images/{img}" alt="{alt}" loading="lazy"></figure>'

def split(text_html, img, alt, flip=False):
    return f"""
<section class="split{' flip' if flip else ''}">
  <div class="wrap split-inner">
    <div class="prose">{text_html}</div>
    {figure(img, alt)}
  </div>
</section>"""

FINISHED = """
<div class="notice">
  <div class="wrap"><p><strong>This Reunion has taken place.</strong> The Cardiff Biennial Reunion ran from 15 to 17 May 2026. Thank you to everyone who joined us. These pages are kept as a record of the weekend; bookings are closed.</p></div>
</div>"""

SUBNAV = """
<nav class="subnav" aria-label="Cardiff 2026">
  <div class="wrap"><ul>
    <li><a href="/cardiff-2026/">Overview</a></li>
    <li><a href="/cardiff-2026/itinerary/">Itinerary</a></li>
    <li><a href="/cardiff-2026/accommodation/">Accommodation</a></li>
    <li><a href="/cardiff-2026/cardiff/">About Cardiff</a></li>
  </ul></div>
</nav>"""

# ---------------------------------------------------------------- Home
page("", "Home", """
<section class="section">
  <div class="wrap narrow prose">
    <h2>Fellowship that began at the Round Table</h2>
    <p>The Lodges of Round Table are a network of Masonic lodges, mostly in England and Wales with some overseas, founded by members of the Round Table movement. Each lodge is independent, but we share a common origin and come together every two years for a Biennial Reunion hosted by one of the lodges.</p>
    <p>These pages will grow into a directory of the lodges around the country. If your lodge belongs on the list, please <a href="/contact-us/">get in touch</a>.</p>
  </div>
</section>

<section class="section alt">
  <div class="wrap cards">
    <a class="card" href="/lodges/">
      <div class="card-img" style="--img:url('/images/cardiff-by-air.jpg')"></div>
      <div class="card-body"><h3>Find a lodge</h3><p>A growing list of the Lodges of Round Table across the country and overseas.</p><span class="more">View the lodges &rarr;</span></div>
    </a>
    <a class="card" href="/cardiff-2026/">
      <div class="card-img" style="--img:url('/images/cardiff-castle.jpg')"></div>
      <div class="card-body"><h3>Cardiff 2026 Reunion</h3><p>Hosted by the Lodge of Round Table No. 9549, 15 to 17 May 2026. A look back at the weekend.</p><span class="more">See the programme &rarr;</span></div>
    </a>
    <a class="card" href="/contact-us/">
      <div class="card-img" style="--img:url('/images/cardiff-bay-sunset.jpg')"></div>
      <div class="card-body"><h3>Get in touch</h3><p>Questions about the lodges, the next Reunion, or adding your lodge to the directory.</p><span class="more">Contact us &rarr;</span></div>
    </a>
  </div>
</section>
""", active="home", hero=("cardiff-bay-sunset.jpg", None, "Friendship, tradition and the spirit of Round Table", None, True))

# ---------------------------------------------------------------- Lodges list
page("lodges", "The Lodges", """
<section class="section">
  <div class="wrap narrow prose">
    <p>There are almost fifty Round Table lodges in England and Wales, with a few overseas. This directory is a work in progress. If your lodge is missing or the details are wrong, please <a href="/contact-us/">let us know</a>.</p>
  </div>
  <div class="wrap">
    <label class="filter">Search the list <input type="search" id="lodge-filter" placeholder="Name, number or area"></label>
    <div class="table-wrap">
    <table class="lodges" id="lodges">
      <thead><tr><th scope="col">Lodge</th><th scope="col">No.</th><th scope="col">Meets in</th><th scope="col">Province</th><th scope="col">Website</th></tr></thead>
      <tbody>
        <!-- To add a lodge, copy one <tr> block below and change the details. -->
        <tr><td>Lodge of Round Table</td><td>9549</td><td>Cardiff</td><td>South Wales</td><td><a href="/cardiff-2026/">This site</a></td></tr>
        <tr><td>Astolat Lodge <span class="muted small">(founded 1942 with members drawn from Round Table)</span></td><td>5848</td><td>Weybourne House, Guildford</td><td>Surrey</td><td><a href="https://astolat.org/history/">Website</a></td></tr>
        <tr><td>Lodge of Harmony <span class="muted small">(founded 1951 at the request of Bristol&rsquo;s Round Tables)</span></td><td>7127</td><td>Freemasons&rsquo; Hall, Park Street, Bristol</td><td>Bristol</td><td><a href="https://www.bristolmasons.co.uk/lodges/#:~:text=The%20Lodge%20of%20Harmony">Province page</a></td></tr>
        <tr><td>Round Table Lodge <span class="check" title="Found in historical records only; please confirm it still meets">&dagger;</span></td><td>7619</td><td>London</td><td>Metropolitan</td><td>&ndash;</td></tr>
        <tr><td>Lodge of the Round Table</td><td>7762</td><td>Leicester</td><td>Leicestershire &amp; Rutland</td><td><a href="https://www.roundtable7762.org.uk/">Website</a></td></tr>
        <tr><td>Lodge of the Round Table <span class="check" title="Found in historical records only; please confirm it still meets">&dagger;</span></td><td>7961</td><td>Worcestershire</td><td>Worcestershire</td><td>&ndash;</td></tr>
        <tr><td>Round Table Lodge of Sussex <span class="check" title="Found in historical records only; please confirm it still meets">&dagger;</span></td><td>7965</td><td>Brighton</td><td>Sussex</td><td>&ndash;</td></tr>
        <tr><td>Round Table Lodge <span class="check" title="Found in historical records only; please confirm it still meets">&dagger;</span></td><td>8111</td><td>Cleveleys, Blackpool</td><td>West Lancashire</td><td>&ndash;</td></tr>
        <tr><td>Round Table Lodge of Essex</td><td>8217</td><td>Hutton</td><td>Essex</td><td><a href="https://essexfreemasons.org.uk/calendar/l8217-round-table-lodge-of-essex-4-1713139200">Province calendar</a></td></tr>
        <tr><td>Round Table Lodge of Lincolnshire</td><td>8240</td><td>Horncastle</td><td>Lincolnshire</td><td><a href="https://www.lincolnshirefreemasons.org/masonic-centres/">Province page</a></td></tr>
        <tr><td>Round Table Lodge <span class="check" title="Found in historical records only; please confirm it still meets">&dagger;</span></td><td>8273</td><td>Wednesbury</td><td>Staffordshire</td><td>&ndash;</td></tr>
        <tr><td>Round Table Lodge of Middlesex</td><td>8301</td><td>Twickenham</td><td>Middlesex</td><td><a href="http://www.roundtablelodgeofmiddlesex.org.uk">Website</a></td></tr>
        <tr><td>North Staffordshire Round Table Lodge</td><td>8355</td><td>Stoke-on-Trent</td><td>Staffordshire</td><td><a href="https://www.nsrtl8355.co.uk/">Website</a></td></tr>
        <tr><td>Lodge of Round Table</td><td>8424</td><td>Warwickshire</td><td>Warwickshire</td><td><a href="https://warwickshirefreemasons.org.uk/useful-links/">Province links</a></td></tr>
        <tr><td>Round Table Lodge of Norfolk <span class="check" title="Found in historical records only; please confirm it still meets">&dagger;</span></td><td>8600</td><td>Norwich</td><td>Norfolk</td><td>&ndash;</td></tr>
        <tr><td>Round Table Lodge of Nottinghamshire</td><td>8604</td><td>Nottingham</td><td>Nottinghamshire</td><td><a href="https://www.nottinghamshiremasons.co.uk/event-details/round-table-lodge-2024-04-01-17-30">Province calendar</a></td></tr>
        <tr><td>Kentish Round Table Lodge</td><td>8685</td><td>Sevenoaks</td><td>West Kent</td><td><a href="https://kentishroundtablelodge.weebly.com/">Website</a></td></tr>
        <tr><td>Round Table Lodge of Derbyshire</td><td>8725</td><td>Dore, Sheffield</td><td>Derbyshire</td><td><a href="https://www.derbyshiremason.org/lodges/round-table-lodge-of-derbyshire-8725/">Province page</a></td></tr>
        <tr><td>Round Table Lodge of South Cheshire <span class="check" title="Found in historical records only; please confirm it still meets">&dagger;</span></td><td>8787</td><td>Sandbach</td><td>Cheshire</td><td>&ndash;</td></tr>
        <tr><td>Table Fellowship Lodge</td><td>8989</td><td>Surbiton</td><td>Surrey</td><td><a href="https://tablefellowshiplodge.org.uk/">Website</a></td></tr>
        <tr><td>Gloucestershire Round Table Lodge</td><td>9017</td><td>Wotton-under-Edge</td><td>Gloucestershire</td><td><a href="https://www.glosmasons.org.uk/lodges/gloucestershire-round-table-lodge-no-9017/">Province page</a></td></tr>
        <tr><td>Round Table Lodge of South Derbyshire</td><td>9074</td><td>Burton upon Trent</td><td>Derbyshire</td><td><a href="https://www.derbyshiremason.org/lodges/round-table-lodge-of-south-derbyshire-9074/">Province page</a></td></tr>
        <tr><td>Somerset Tablers Lodge</td><td>9075</td><td>Ilminster</td><td>Somerset</td><td><a href="https://www.somersetfreemasons.org/category/zlodges/9075/">Province page</a></td></tr>
        <tr><td>The Shropshire Round Table Lodge</td><td>9104</td><td>Shropshire</td><td>Shropshire</td><td><a href="https://www.shropshiremasons.org.uk/craft-lodges/the-shropshire-round-table-lodge">Province page</a></td></tr>
        <tr><td>Round Table Lodge of Hertfordshire</td><td>9221</td><td>St Albans</td><td>Hertfordshire</td><td><a href="https://pglherts.org/province/lodges/round-table-lodge-of-hertfordshire/">Province page</a></td></tr>
        <tr><td>Round Table Lodge of Suffolk <span class="check" title="Found in historical records only; please confirm it still meets">&dagger;</span></td><td>9276</td><td>Ipswich</td><td>Suffolk</td><td>&ndash;</td></tr>
        <tr><td>West Essex Round Table Lodge <span class="check" title="Found in historical records only; please confirm it still meets">&dagger;</span></td><td>9310</td><td>Chingford</td><td>Essex</td><td>&ndash;</td></tr>
        <tr><td>Lodge of King Arthur</td><td>9311</td><td><em>To confirm</em> (members in West Yorkshire)</td><td><em>To confirm</em></td><td>&ndash;</td></tr>
        <tr><td>Round Table Lodge of Oxfordshire</td><td>9509</td><td>Oxfordshire</td><td>Oxfordshire</td><td><a href="https://roundtablelodgeoxon.com/">Website</a></td></tr>
        <tr><td>Louis Marchesi Lodge <span class="muted small">(named after Round Table&rsquo;s founder)</span></td><td>9558</td><td>Uffculme</td><td>Devonshire</td><td>&ndash;</td></tr>
        <tr><td>North Essex Round Table Lodge <span class="check" title="Found in historical records only; please confirm it still meets">&dagger;</span></td><td>9578</td><td>Clacton-on-Sea</td><td>Essex</td><td>&ndash;</td></tr>
        <tr><td>Ridings Tablers Lodge</td><td>9586</td><td>Beverley</td><td>Yorkshire North &amp; East Ridings</td><td><a href="https://justbeverley.co.uk/articles/ridings-tablers-lodge">Profile</a></td></tr>
        <tr><td>Round Table Thames Valley Lodge</td><td>9697</td><td>Henley-on-Thames</td><td>Oxfordshire</td><td><a href="https://henleyfreemasons.uk/round-table-thames-valley-lodge-no-9697/">Website</a></td></tr>
        <tr><td>Round Table Lodge <span class="check" title="Found in historical records only; please confirm it still meets">&dagger;</span></td><td>9711</td><td>Nairobi, Kenya</td><td>District of East Africa</td><td>&ndash;</td></tr>
      </tbody>
    </table>
    </div>
    <p id="no-match" class="muted" hidden>No lodges match that search.</p>
    <p class="muted small">&dagger; Found only in historical lodge records, so it may have closed or moved. Last checked November 2026.</p>
  </div>
</section>
<script>
(function(){
  var input=document.getElementById('lodge-filter'),rows=document.querySelectorAll('#lodges tbody tr'),none=document.getElementById('no-match');
  input.addEventListener('input',function(){
    var q=input.value.trim().toLowerCase(),shown=0;
    rows.forEach(function(r){var hit=r.textContent.toLowerCase().indexOf(q)>-1;r.hidden=!hit;if(hit)shown++;});
    none.hidden=shown>0;
  });
})();
</script>
""", active="lodges", description="A directory of the Lodges of Round Table.")

# ---------------------------------------------------------------- History
def ev(year, title, text, lodges="", confirm=False, kind="lodge"):
    tag = ' <span class="tbc">to confirm</span>' if confirm else ''
    import re as _re
    y = _re.search(r"\d{4}", year); y = y.group(0) if y else "2026"
    eid = "y" + y + "-" + _re.sub(r"[^a-z]+", "-", _re.sub(r"&[a-z]+;", "", title.lower())).strip("-")[:30]
    label = {"lodge": "Lodges", "reunion": "Reunion", "rt": "Round Table"}[kind]
    return f"""
      <li class="ev ev-{kind}" id="{eid}" data-kind="{kind}" data-year="{y}" data-title="{_re.sub(r'<[^>]+>', '', title)}">
        <div class="ev-year">{year}</div>
        <div class="ev-body"><span class="ev-kind">{label}</span><h3>{title}{tag}</h3><p>{text}</p>{f'<p class="ev-lodges">{lodges}</p>' if lodges else ''}</div>
      </li>"""

def era(name, intro, events):
    return f"""
  <section class="era">
    <div class="wrap narrow">
      <h2>{name}</h2>
      {f'<p class="era-intro">{intro}</p>' if intro else ''}
      <ol class="timeline">{''.join(events)}
      </ol>
    </div>
  </section>"""

history_body = """
<section class="section">
  <div class="wrap narrow prose">
    <p class="lede-dark">Round Table was built for young men, and it has always had an upper age limit. As Tablers reached it, many looked for a way to keep the friendships and the spirit of service going. Some joined 41 Club; others, who were also Freemasons, started lodges of their own. Over eighty years those lodges have grown into a network across England and Wales and beyond, meeting every two years at the Biennial Reunion.</p>
    <p class="muted small">This page is a first draft put together from lodge and provincial websites, published lodge records and Reunion papers. Dates are given where a source states them. If you can correct or add to it, please <a href="/contact-us/">get in touch</a>.</p>
  </div>
</section>
<section class="explorer" aria-label="Timeline explorer">
  <div class="wrap narrow">
    <div class="filters" role="group" aria-label="Show">
      <button type="button" class="chip is-on" data-filter="all" aria-pressed="true">Everything</button>
      <button type="button" class="chip" data-filter="lodge" aria-pressed="false"><i class="dot dot-lodge"></i>Lodges founded</button>
      <button type="button" class="chip" data-filter="reunion" aria-pressed="false"><i class="dot dot-reunion"></i>Reunions</button>
      <button type="button" class="chip" data-filter="rt" aria-pressed="false"><i class="dot dot-rt"></i>Round Table</button>
    </div>
    <div class="track" id="track" hidden>
      <div class="track-line"></div>
      <div class="track-ticks" id="track-ticks"></div>
      <div class="track-dots" id="track-dots"></div>
      <div class="track-tip" id="track-tip" role="status" aria-live="polite"></div>
    </div>
    <p class="muted small track-hint">Tap a dot to jump to that moment.</p>
  </div>
</section>
""" + era("Beginnings", "", [
    ev("1927", "Round Table is founded in Norwich",
       "Louis Marchesi starts the first Round Table in Norwich as a club where young business and professional men can meet, make friends and serve their community. The movement spreads quickly across Britain and abroad.", kind="rt"),
    ev("1942", "Astolat Lodge, Guildford",
       "In the middle of the Second World War, a group of Guildford Freemasons plan a new lodge and decide that its first members should come, as far as possible, from past and present Round Tablers. It takes its name from Astolat, the Arthurian name for Guildford. Warranted in April and consecrated in May 1942, it is the earliest lodge with Round Table roots that we know of.",
       "Astolat Lodge No. 5848 &middot; Surrey"),
    ev("1951&ndash;52", "Lodge of Harmony, Bristol",
       "Bristol&rsquo;s Round Tables ask for a lodge of their own. Lodge of Harmony is established in 1951 and consecrated in January 1952, still meeting today at Freemasons&rsquo; Hall in Park Street.",
       "Lodge of Harmony No. 7127 &middot; Bristol"),
    ev("1958", "The Round Table name arrives",
       "Round Table Lodge in London is warranted, the earliest lodge we have found that carries the Round Table name itself. In the years that follow, lodges of the Round Table are formed in Leicester, Worcestershire and Sussex.",
       "Round Table Lodge No. 7619 &middot; Lodge of the Round Table No. 7762 &middot; Lodge of the Round Table No. 7961 &middot; Round Table Lodge of Sussex No. 7965"),
]) + era("Growth", "From the mid-1960s, new lodges appear across the country, usually founded by members of the local Round Tables and often taking the name of their county.", [
    ev("1966&ndash;69", "Lancashire, Essex, Lincolnshire, Staffordshire and Middlesex",
       "Round Table Lodge at Cleveleys is warranted in 1966. In 1968 the Round Table Lodges of Essex (Hutton) and Lincolnshire (Horncastle) follow, the latter founded by former Tablers wanting to combine Round Table camaraderie with Freemasonry. Lodges at Wednesbury and in Middlesex follow in 1969.",
       "Nos. 8111, 8217, 8240, 8273 &middot; Round Table Lodge of Middlesex No. 8301"),
    ev("1971", "North Staffordshire",
       "North Staffordshire Round Table Lodge is founded in Stoke-on-Trent; it marked its fiftieth anniversary in 2021.",
       "North Staffordshire Round Table Lodge No. 8355"),
    ev("1970s", "Warwickshire, Norfolk, Nottinghamshire, Kent, Derbyshire and Cheshire",
       "The Lodge of Round Table in Warwickshire is followed by the Round Table Lodges of Norfolk and Nottinghamshire (both 1974). In 1976 Kentish Round Table Lodge is formed by members of Round Tables in West Kent, and the Round Table Lodge of Derbyshire by ex-Tablers looking to carry on their purpose. The Round Table Lodge of South Cheshire follows in 1977.",
       "Nos. 8424, 8600, 8604, 8685, 8725, 8787"),
]) + era("The 1980s", "", [
    ev("1981&ndash;83", "Surrey, Gloucestershire, South Derbyshire and Somerset",
       "Table Fellowship Lodge is consecrated in November 1981 by Surrey Freemasons and Round Tablers. Gloucestershire Round Table Lodge is consecrated in January 1982. In 1983 Burton-upon-Trent Tablers found the Round Table Lodge of South Derbyshire, and Somerset Tablers Lodge is founded by members of Round Table Area 37, which then covered the whole county.",
       "Nos. 8989, 9017, 9074, 9075"),
    ev("1984&ndash;88", "Shropshire, Hertfordshire, Suffolk, Essex and Yorkshire",
       "Shropshire Round Table Lodge is followed by the Round Table Lodge of Hertfordshire, consecrated in St Albans in April 1987, and in 1988 by the Round Table Lodge of Suffolk and West Essex Round Table Lodge. The Lodge of King Arthur, whose members come from the Yorkshire and Lancashire Tables, also dates from this period.",
       "Nos. 9104, 9221, 9276, 9310, 9311"),
]) + era("The 1990s", "", [
    ev("1993", "Oxfordshire",
       "The Round Table Lodge of Oxfordshire is warranted.",
       "Round Table Lodge of Oxfordshire No. 9509"),
    ev("1994", "Cardiff and North Essex",
       "The Lodge of Round Table is founded in Cardiff, bringing the network to Wales. Louis Marchesi Lodge in Devon, named after the founder of Round Table, follows around the same time, and in December North Essex Round Table Lodge is warranted at Clacton-on-Sea.",
       "Lodge of Round Table No. 9549 &middot; Louis Marchesi Lodge No. 9558 &middot; North Essex Round Table Lodge No. 9578"),
    ev("1990s", "Ridings Tablers, Beverley",
       "Ridings Tablers Lodge brings the network to East Yorkshire.",
       "Ridings Tablers Lodge No. 9586"),
    ev("1999", "Thames Valley and Nairobi",
       "Round Table Thames Valley Lodge is established at Henley-on-Thames as a home for Tablers, ex-Tablers and those who &lsquo;should have been Tablers&rsquo;. The same year a Round Table Lodge is warranted in Nairobi, Kenya.",
       "Round Table Thames Valley Lodge No. 9697 &middot; Round Table Lodge No. 9711"),
]) + era("The 2000s", "", [
    ev("2004", "Biennial Reunion hosted by Middlesex",
       "The Round Table Lodge of Middlesex hosts the Biennial Reunion.",
       "Hosted by No. 8301", kind="reunion"),
    ev("2006", "Biennial Reunion in Cardiff",
       "The Lodge of Round Table hosts the Reunion in Cardiff for the first time, twelve years after the lodge was founded.",
       "Hosted by No. 9549", kind="reunion"),
]) + era("Today", "", [
    ev("Now", "Almost fifty lodges",
       "There are now almost fifty Round Table lodges in England and Wales. Many no longer recruit only from Round Table, but they keep its traditions: fun and fellowship alongside service to the community, and a warm welcome for visitors. Every two years the lodges come together for the Biennial Reunion, a tradition that goes back many years, hosted in turn by one of the lodges.",
       '<a href="/lodges/">See the directory of lodges</a>', kind="rt"),
    ev("2022", "Biennial Reunion at Crewe Hall",
       "North Staffordshire Round Table Lodge hosts the Round Table Lodges Biennial weekend at Crewe Hall, 10&ndash;12 June 2022.",
       "Hosted by No. 8355", kind="reunion"),
    ev("2024", "Biennial Reunion in Torquay",
       "Louis Marchesi Lodge takes the Reunion to the seaside at the Anchorage Hotel in Babbacombe, 10&ndash;12 May 2024: a pre-tour for early arrivals, a Lodge meeting at St Marychurch Masonic Hall, a ladies&rsquo; dinner hosted by former members of Ladies Circle, beach games and a fish and chip lunch at Paignton, and a gala dinner to finish.",
       "Hosted by No. 9558", kind="reunion"),
    ev("2026", "Biennial Reunion in Cardiff",
       "Twenty years after it last hosted, the Lodge of Round Table welcomes the Reunion back to Cardiff, 15&ndash;17 May 2026: a Lodge Installation Meeting at Cardiff Masonic Hall, a private tour of Cardiff Castle and a black-tie gala dinner at Cornerstone.",
       '<a href="/cardiff-2026/">Cardiff 2026</a> &middot; Hosted by No. 9549', kind="reunion"),
]) + """
<section class="section alt">
  <div class="wrap narrow prose small-prose">
    <h2>Sources</h2>
    <ul>
      <li><a href="https://astolat.org/history/">Astolat Lodge No. 5848: History</a></li>
      <li><a href="https://www.bristolmasons.co.uk/lodges/#:~:text=The%20Lodge%20of%20Harmony">Province of Bristol: The Lodge of Harmony</a></li>
      <li><a href="https://www.dhi.ac.uk/lane/">Lane&rsquo;s Masonic Records</a> (warrant dates)</li>
      <li><a href="https://www.lincolnshirefreemasons.org/masonic-centres/">Lincolnshire Freemasons: Round Table Lodge No. 8240</a></li>
      <li><a href="https://www.nsrtl8355.co.uk/">North Staffordshire Round Table Lodge No. 8355</a></li>
      <li><a href="https://kentishroundtablelodge.weebly.com/">Kentish Round Table Lodge</a></li>
      <li><a href="https://www.derbyshiremason.org/lodges/round-table-lodge-of-derbyshire-8725/">Derbyshire: Round Table Lodge No. 8725</a> and <a href="https://www.derbyshiremason.org/lodges/round-table-lodge-of-south-derbyshire-9074/">No. 9074</a></li>
      <li><a href="https://tablefellowshiplodge.org.uk/our-lodge-history/">Table Fellowship Lodge No. 8989: History</a></li>
      <li><a href="https://www.glosmasons.org.uk/lodges/gloucestershire-round-table-lodge-no-9017/">Gloucestershire Round Table Lodge No. 9017</a></li>
      <li><a href="https://www.somersetfreemasons.org/?p=1728">Somerset Tablers Lodge No. 9075</a></li>
      <li><a href="https://pglherts.org/province/lodges/round-table-lodge-of-hertfordshire/">Round Table Lodge of Hertfordshire No. 9221</a></li>
      <li><a href="https://henleyfreemasons.uk/round-table-thames-valley-lodge-no-9697/">Round Table Thames Valley Lodge No. 9697</a></li>
      <li>Louis Marchesi Lodge No. 9558: Reunion flyer and booking details, 2024</li>
    </ul>
  </div>
</section>
<script>
(function(){
  var evs=[].slice.call(document.querySelectorAll('.ev'));
  var track=document.getElementById('track'),dotsBox=document.getElementById('track-dots'),ticks=document.getElementById('track-ticks'),tip=document.getElementById('track-tip');
  var START=1920,END=2030,pct=function(y){return (y-START)/(END-START)*100;};
  track.hidden=false;
  for(var d=START;d<=END;d+=10){var t=document.createElement('span');t.style.left=pct(d)+'%';t.textContent=d;ticks.appendChild(t);}
  // stack dots that share a year-ish slot
  var used={};
  evs.forEach(function(ev){
    var y=+ev.dataset.year,slot=Math.round(pct(y)),row=used[slot]=(used[slot]||0)+1;
    var b=document.createElement('button');b.type='button';b.className='tdot tdot-'+ev.dataset.kind;
    b.style.left=pct(y)+'%';b.style.bottom=(14+(row-1)*14)+'px';
    b.setAttribute('aria-label',ev.querySelector('.ev-year').textContent+': '+ev.dataset.title);
    b.dataset.target=ev.id;b.dataset.kind=ev.dataset.kind;
    var show=function(){tip.textContent=ev.querySelector('.ev-year').textContent+' \u00b7 '+ev.dataset.title;tip.style.left=Math.min(Math.max(pct(y),12),88)+'%';tip.classList.add('on');};
    b.addEventListener('mouseenter',show);b.addEventListener('focus',show);
    b.addEventListener('mouseleave',function(){tip.classList.remove('on');});
    b.addEventListener('click',function(){
      ev.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'center'});
      ev.classList.remove('flash');void ev.offsetWidth;ev.classList.add('flash');
    });
    dotsBox.appendChild(b);
  });
  // filters
  var chips=[].slice.call(document.querySelectorAll('.chip'));
  chips.forEach(function(c){c.addEventListener('click',function(){
    var f=c.dataset.filter;
    chips.forEach(function(x){var on=x===c;x.classList.toggle('is-on',on);x.setAttribute('aria-pressed',on);});
    evs.forEach(function(ev){ev.hidden=!(f==='all'||ev.dataset.kind===f);});
    [].forEach.call(dotsBox.children,function(b){b.classList.toggle('dim',!(f==='all'||b.dataset.kind===f));});
    [].forEach.call(document.querySelectorAll('.era'),function(era){era.hidden=!era.querySelector('.ev:not([hidden])');});
  });});
  // reveal on scroll + highlight active dot
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){
      if(e.isIntersecting){e.target.classList.add('seen');
        [].forEach.call(dotsBox.children,function(b){b.classList.toggle('active',b.dataset.target===e.target.id);});}
    });},{rootMargin:'-40% 0px -40% 0px'});
    evs.forEach(function(ev){ev.classList.add('reveal');io.observe(ev);});
    var io2=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)e.target.classList.add('seen');});},{rootMargin:'0px 0px -10% 0px'});
    evs.forEach(function(ev){io2.observe(ev);});
  }
})();
</script>
"""
page("history", "History", history_body, active="history",
     description="A history of the Lodges of Round Table, from Astolat Lodge in 1942 to the Biennial Reunions of today.",
     hero=("cardiff-castle.jpg", "Since 1942", "Our history", "How Round Tablers built a network of Masonic lodges"))

# ---------------------------------------------------------------- Cardiff 2026 overview
page("cardiff-2026", "Cardiff 2026", FINISHED + SUBNAV + """
<section class="section">
  <div class="wrap narrow prose">
    <h2>Welcome to Cardiff 2026</h2>
    <p>The Lodge of Round Table No. 9549 was delighted to host the <strong>Lodges of Round Table Biennial Reunion</strong> from Friday 15th to Sunday 17th May 2026 in the heart of Cardiff.</p>
    <p>The Reunion brought together members, partners, and friends from Lodges of Round Table across the country and beyond: a special occasion to rekindle friendships, celebrate our shared values, and enjoy a weekend of fellowship in one of the UK’s most vibrant cities.</p>
    <p>Our base for the weekend was the Holiday Inn Cardiff City Centre, opposite Cardiff Castle and just a short walk from the Principality Stadium and Cardiff Bay.</p>
    <h3>The programme</h3>
    <ul>
      <li><strong>Friday evening:</strong> A Lodge Installation Meeting and dinner at Cardiff Masonic Hall for brethren, and a private ladies’ dinner at the hotel with after-dinner entertainment from the man with the ‘<em>Rolls-Royce Voice</em>’, West End &amp; Opera Sensation Anthony Stuart Lloyd.</li>
      <li><strong>Saturday:</strong> A private tour of Cardiff Castle with lunch in the hospitality suite, free time to explore the city or take a boat trip around the Bay, followed by a black-tie gala dinner at Cornerstone Cardiff with headline entertainment from Wales’ Premiere Showman and Entertainer, <em>The Man, The Hat, The Voice</em>, Deano Martini, and a different programme from Anthony Stuart Lloyd.</li>
      <li><strong>Sunday:</strong> A fond farewell after breakfast and time together with friends old and new.</li>
    </ul>
    <p><a class="btn" href="/cardiff-2026/itinerary/">Full itinerary &rarr;</a></p>
  </div>
</section>
<section class="section alt">
  <div class="wrap cards">
    <a class="card" href="/cardiff-2026/cardiff/"><div class="card-img" style="--img:url('/images/cardiff-bay-sunset.jpg')"></div><div class="card-body"><h3>Discover Cardiff</h3><p>From its historic castle to the waterfront at Cardiff Bay.</p></div></a>
    <a class="card" href="/cardiff-2026/itinerary/"><div class="card-img" style="--img:url('/images/cardiff-castle.jpg')"></div><div class="card-body"><h3>The weekend</h3><p>Friday’s Lodge meeting and ladies’ dinner to Saturday’s castle tour and gala.</p></div></a>
    <a class="card" href="/cardiff-2026/accommodation/"><div class="card-img" style="--img:url('/images/principality-stadium.jpg')"></div><div class="card-body"><h3>Where we stayed</h3><p>The Holiday Inn Cardiff City Centre, steps from Cardiff Castle.</p></div></a>
  </div>
</section>
""", active="cardiff-2026", description="The Lodges of Round Table Biennial Reunion, Cardiff, 15–17 May 2026.",
     hero=("cardiff-by-air.jpg", "Biennial Reunion &middot; 15&ndash;17 May 2026", "Cardiff 2026", "Hosted by the Lodge of Round Table No. 9549"))

# ---------------------------------------------------------------- Itinerary
itin = FINISHED + SUBNAV + """
<section class="day-head"><div class="wrap"><h2>Friday 15th May 2026</h2><p>Afternoon / Evening</p></div></section>
""" + split("""
<h3>Lodge Installation Meeting &amp; Dinner</h3>
<p>Brethren will assemble at the historic Cardiff Masonic Hall for a formal Lodge Installation Meeting, held in the magnificent Duke of Kent Temple. This impressive setting provides a fitting backdrop for the ceremony, which will be conducted in accordance with the traditions and dignity of the Craft.</p>
<p>Following the meeting, brethren will gather for drinks in the Members’ Bar, offering a relaxed opportunity to renew acquaintances and welcome visitors from across the country and beyond.</p>
<p>The evening will then continue with dinner in the elegant Duke of Kent Suite, where guests will enjoy fine dining in convivial surroundings. This combination of ceremony, hospitality, and fellowship creates a truly memorable opening to the Reunion weekend.</p>
<p>This traditional first evening sets the tone for the days ahead — celebrating friendship, shared values, and the enduring spirit of the Lodges of Round Table.</p>
""", "cardiff-masonic-hall.jpg", "Cardiff Masonic Hall") + split("""
<h3>Ladies’ Dinner</h3>
<p>Partners and guests are warmly invited to enjoy a delightful evening at the Junction Restaurant within the Holiday Inn Cardiff City Centre, offering a stylish and welcoming setting for the start of the Reunion weekend.</p>
<p>The evening will begin with drinks, providing an opportunity to relax and socialise in comfortable surroundings before taking seats for dinner. Guests will then enjoy a carefully prepared meal, followed by exceptional after-dinner entertainment.</p>
<p>We are delighted that the evening’s entertainment will be provided by the man with the “<em>Rolls-Royce Voice</em>”, West End and opera sensation — Anthony Stuart Lloyd, whose performance promises to bring elegance, warmth, and a touch of theatrical brilliance to the occasion.</p>
<p>This special gathering offers the perfect opportunity to reconnect with familiar faces and to make new friendships, bringing together guests from across the country in the true spirit of Round Table fellowship.</p>
<p>Set against the backdrop of Cardiff’s vibrant city centre, this relaxed and sociable evening provides a wonderful complement to the formal proceedings elsewhere, ensuring an enjoyable and memorable start to the weekend for all attending.</p>
""", "holiday-inn-dining-room.jpg", "Dining Room", flip=True) + """
<section class="day-head"><div class="wrap"><h2>Saturday 16th May 2026</h2><p>Morning &amp; Early Afternoon</p></div></section>
""" + split("""
<h3>Private Tour of Cardiff Castle</h3>
<p>Saturday begins with a guided private tour of Cardiff Castle, one of Wales’s most iconic and historic landmarks, set at the very heart of the city. Steeped in over 2,000 years of history, the Castle offers a fascinating journey from its Roman foundations through to its transformation into a spectacular Victorian Gothic masterpiece.</p>
<p>Guests will enjoy exclusive access as expert guides bring the Castle’s rich heritage to life, revealing its stories, architecture, and significance in a truly memorable way.</p>
<p>Following the tour, guests will be welcomed into the Castle’s exclusive Hospitality Suite to enjoy a relaxed lunch and refreshments. This unique setting, overlooking the Castle grounds, provides the perfect opportunity to unwind, reflect on the morning’s experience, and enjoy the company of fellow attendees in elegant surroundings.</p>
""", "cardiff-castle-tour.jpg", "Cardiff Castle") + split("""
<p class="slot">Afternoon</p>
<h3>Free Time in Cardiff</h3>
<p>The afternoon is yours to enjoy at leisure, offering the perfect opportunity to experience all that Cardiff has to offer. Wander through the city’s charming Victorian arcades, explore its museums and galleries, or relax in one of the many cafés and green spaces that give the city its welcoming character.</p>
<p>For those wishing to venture a little further, a scenic boat trip around Cardiff Bay from the jetty opposite the hotel provides a wonderful way to take in the waterfront and surrounding landmarks from a different perspective.</p>
<p>Whether you choose to explore, shop, sightsee, or simply unwind, this free time allows everyone to enjoy Cardiff in their own way and at their own pace.</p>
""", "cardiff-bay-pierhead.jpg", "Cardiff Bay", flip=True) + split("""
<p class="slot">Evening</p>
<h3>Black Tie Gala Dinner</h3>
<p>The highlight of the weekend is the Black Tie Gala Dinner at Cornerstone Cardiff, an impressive Grade II listed venue that provides a stunning and distinctive setting for this special occasion.</p>
<p>Guests will be welcomed for an evening of elegance and celebration, beginning with a drinks reception before taking their seats for a carefully curated dining experience. The evening will feature fine food, engaging speeches, and high-quality entertainment, all designed to create a memorable and enjoyable occasion for all in attendance.</p>
<p>We are delighted that the evening’s headline entertainment will be provided by Wales’s premier showman and entertainer — <em>The Man, The Hat, The Voice</em> — Deano Martini, whose charismatic performance promises to bring energy, style, and a touch of showbiz flair to the occasion.</p>
<p>In addition, guests will enjoy a contrasting programme from Anthony Stuart Lloyd, offering further variety and entertainment to ensure a rich and engaging evening throughout.</p>
<p>Bringing together members, partners, and guests from across the Lodges of Round Table, the Gala Dinner offers a fitting culmination to the Reunion — a night of fellowship, celebration, and shared enjoyment in a truly remarkable setting.</p>
""", "cornerstone-cardiff.jpg", "Cornerstone") + """
<section class="day-head"><div class="wrap"><h2>Sunday 17th May 2026</h2></div></section>
""" + split("""
<h3>Farewell Breakfast &amp; Departure</h3>
<p>The weekend concludes with a relaxed breakfast at the Holiday Inn Cardiff City Centre, offering one final opportunity to gather, reflect on the events of the past few days, and enjoy the company of friends old and new.</p>
<p>As the Reunion draws to a close, it is a time to share farewells, exchange memories, and look ahead to future meetings. Departures will follow at leisure, with guests leaving Cardiff carrying with them the spirit of fellowship and the many highlights of a memorable weekend.</p>
<p>Until we meet again at the next Lodges of Round Table Biennial Reunion, safe travels to all.</p>
""", "farewell-breakfast.jpg", "Breakfast", flip=True)
page("cardiff-2026/itinerary", "Itinerary", itin, active="cardiff-2026", description="The programme for the Cardiff 2026 Biennial Reunion.")

# ---------------------------------------------------------------- Accommodation
acc = FINISHED + SUBNAV + split("""
<h2>Holiday Inn Cardiff City Centre</h2>
<p>Our base for the weekend was the <strong>Holiday Inn Cardiff City Centre</strong>, perfectly positioned in one of the most enviable locations in the city. Overlooking the historic grounds of <strong>Cardiff Castle</strong>, with <strong>breathtaking views across the Castle, Cardiff Arms Park, and the River Taff</strong>, the hotel offers a truly memorable setting for your stay.</p>
<p>Just moments from the <strong>Principality Stadium</strong> and a short stroll from Cardiff’s renowned shopping arcades, cafés, and restaurants, the hotel places you right at the heart of the city’s vibrant atmosphere.</p>
<p>Whether you choose to explore the historic streets, relax by the riverside, or take in the scenery from the comfort of the hotel, everything is conveniently within easy reach.</p>
""", "holiday-inn-night.jpg", "Holiday Inn at Night") + split("""
<h2>Comfort &amp; Convenience</h2>
<p>The hotel offers a welcoming and comfortable environment, perfectly suited for a relaxing and enjoyable stay throughout the Reunion weekend. Guests can expect:</p>
<ul>
<li><strong>Modern, well-appointed bedrooms</strong> with Wi-Fi and air conditioning</li>
<li>An <strong>on-site restaurant and bar</strong>, many areas offering views across the Castle grounds and surrounding landmarks</li>
<li><strong>Secure on-site parking</strong> (subject to availability)</li>
<li>Excellent transport links, with <strong>Cardiff Central Station just a short walk away</strong></li>
<li>Easy access to the waterfront attractions of <strong>Cardiff Bay</strong></li>
</ul>
""", "holiday-inn-stadium-view.jpg", "Stadium View", flip=True) + split("""
<h2>A Perfect Base for the Weekend</h2>
<p>More than simply a place to stay, the <strong>Holiday Inn Cardiff City Centre</strong> serves as the social heart of the Reunion — a place where conversations continue long after the formal programme has ended.</p>
<p>Whether gathering for a drink, meeting friends before events, or unwinding after a full day of activity, the hotel provides a relaxed and welcoming environment for both brethren and guests. Its central location makes it effortless to move between venues, while also offering the opportunity to step away and enjoy the surrounding views or quiet moments by the River Taff.</p>
<p>With its unique combination of <strong>breathtaking outlooks, modern comfort, and exceptional convenience</strong>, the hotel creates the perfect setting for a weekend defined by fellowship, connection, and shared experience.</p>
""", "holiday-inn-location.jpg", "Hotel Location")
page("cardiff-2026/accommodation", "Accommodation", acc, active="cardiff-2026", description="Where we stayed for the Cardiff 2026 Reunion.")

# ---------------------------------------------------------------- Cardiff city
page("cardiff-2026/cardiff", "Cardiff", FINISHED + SUBNAV + """
<section class="section">
  <div class="wrap narrow prose">
    <h2>A Capital of Culture, History &amp; Warmth</h2>
    <p>Cardiff, the capital of Wales, is a city that blends rich history with a vibrant modern spirit. From its medieval castle at the heart of the city to the cutting-edge architecture of Cardiff Bay, the city offers something for everyone.</p>
    <h3>Landmarks &amp; Attractions</h3>
    <ul>
      <li><strong>Cardiff Castle</strong> — Over 2,000 years of history, from Roman walls to a Victorian Gothic revival mansion.</li>
      <li><strong>Principality Stadium</strong> — The home of Welsh rugby and one of the world’s most impressive sporting arenas.</li>
      <li><strong>Cardiff Bay</strong> — A stunning waterfront development with the Wales Millennium Centre, the Senedd (Welsh Parliament), and a host of restaurants and attractions.</li>
      <li><strong>Victorian Arcades &amp; Shopping</strong> — Quaint covered arcades and bustling shopping streets filled with independent stores, cafés, and boutiques.</li>
      <li><strong>Museums &amp; Galleries</strong> — Including the free National Museum Cardiff, with art, natural history, and world-class exhibitions.</li>
    </ul>
    <h3>A Walkable, Welcoming City</h3>
    <p>One of Cardiff’s greatest charms is its size. Compact and easy to explore on foot, the city centre, Bay, and cultural landmarks are all within easy reach. The people of Cardiff are renowned for their friendliness and hospitality, ensuring visitors feel at home straight away.</p>
    <h3>Food &amp; Nightlife</h3>
    <p>Whether you’re looking for fine dining, lively bars, or a quiet riverside pub, Cardiff offers a wealth of choices. The city is proud of its local produce and vibrant dining scene.</p>
    <h3>Beyond the City</h3>
    <p>For those extending their stay, Cardiff is the gateway to South Wales. Within minutes you can explore the Brecon Beacons National Park, the Glamorgan Heritage Coast, and the rolling countryside of the Vale of Glamorgan.</p>
  </div>
</section>
""", active="cardiff-2026", hero=("principality-stadium.jpg", "Cardiff 2026", "Cardiff", "The capital of Wales"))

# ---------------------------------------------------------------- Contact
page("contact-us", "Contact Us", """
<section class="section">
  <div class="wrap contact">
    <div class="prose">
      <h2>Ask us about anything</h2>
      <p>For questions about the Lodges of Round Table, the next Biennial Reunion, or adding your lodge to the directory, please email us and we’ll get back to you.</p>
      <p><a class="btn" href="mailto:lodgesofroundtable@gmail.com">Email lodgesofroundtable@gmail.com</a></p>
    </div>
    <div class="contact-card">
      <h3>Contact information</h3>
      <p><strong>Lodges of Round Table</strong></p>
      <p><a href="mailto:lodgesofroundtable@gmail.com">lodgesofroundtable@gmail.com</a></p>
      <p>18 Tarrws Close,<br>Wenvoe,<br>Cardiff.<br>CF5 6BT</p>
    </div>
  </div>
</section>
""", active="contact")

# ---------------------------------------------------------------- Bookings closed
page("cardiff-2026/book", "Bookings closed", FINISHED + """
<section class="section"><div class="wrap narrow prose">
<p>Bookings for the Cardiff 2026 Biennial Reunion are now closed. Details of the next Reunion will be published here when they are available.</p>
<p><a class="btn" href="/contact-us/">Contact us</a></p>
</div></section>
""", active="cardiff-2026")

# ---------------------------------------------------------------- 404
(OUT / "404.html").write_text((OUT / "index.html").read_text().replace(
    (OUT / "index.html").read_text().split('<main id="main">')[1].split("</main>")[0],
    '\n<section class="section"><div class="wrap narrow prose"><h2>Page not found</h2><p>Sorry, that page doesn’t exist. It may have moved when the site was rebuilt.</p><p><a class="btn" href="/">Back to the home page</a></p></div></section>\n'
).replace("<title>Lodges of Round Table</title>", "<title>Page not found | Lodges of Round Table</title>"), encoding="utf-8")

# ---------------------------------------------------------------- Old Drupal URLs
redirect("itinerary", "/cardiff-2026/itinerary/")
redirect("accommodation", "/cardiff-2026/accommodation/")
redirect("cardiff", "/cardiff-2026/cardiff/")
redirect("form/book", "/cardiff-2026/book/")
redirect("terms-and-conditions", "/cardiff-2026/")

(OUT / "CNAME").write_text("www.lodgesofroundtable.uk\n")
(OUT / ".nojekyll").write_text("")
print("built", sum(1 for _ in OUT.rglob("*.html")), "pages")
