#!/usr/bin/env python3
"""Generate Tam Family Majestic Princess British Isles Cruise 2027 webpage"""
import subprocess

PROJECT = '/workspace/tam-cruise-2027'
TOKEN = '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'
USER = 'ktamxl'

# Check available images
import os
imgs = os.listdir(f'{PROJECT}/imgs')
print("Project images:", imgs[:10])

# The full HTML - built as a Python string
html = open(f'{PROJECT}/imgs/route-map.svg').read()

# Now build the full page
page = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tam Family — Majestic Princess British Isles 2027</title>
<style>
  *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
  :root{--ink:#1a1a2e;--soft:#f5f2ec;--white:#fff;--gold:#c9a84c;--gold-lt:#f0d98a;--navy:#0d2540;--navy2:#0d3a5c;--radius:12px;--shadow:0 4px 20px rgba(0,0,0,.15)}
  html{scroll-behavior:smooth}
  body{font-family:Georgia,'Times New Roman',serif;background:var(--soft);color:var(--ink);line-height:1.7}
  /* HERO */
  .hero{background:linear-gradient(160deg,#061825 0%,#0d3a5c 55%,#061018 100%);color:var(--white);text-align:center;padding:72px 24px 0;overflow:hidden;position:relative}
  .hero-ship{width:100%;max-height:380px;object-fit:cover;display:block;margin:0 auto;opacity:.85}
  .hero-overlay{background:linear-gradient(to top,rgba(6,16,24,.9) 0%,transparent 60%);padding:48px 24px 40px}
  .hero-badge{display:inline-block;border:1px solid var(--gold);color:var(--gold-lt);font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;padding:4px 18px;border-radius:20px;margin-bottom:20px}
  .hero h1{font-size:clamp(1.8rem,5vw,3rem);font-weight:normal;letter-spacing:.02em;margin-bottom:12px;color:var(--white);line-height:1.25}
  .hero h1 em{color:var(--gold-lt);font-style:normal}
  .hero-sub{font-size:1.05rem;opacity:.8;margin-bottom:28px}
  .hero-dates{display:flex;justify-content:center;gap:36px;flex-wrap:wrap;margin-bottom:28px}
  .hero-date-item{text-align:center}
  .hero-date-item .label{font-family:sans-serif;font-size:.72rem;letter-spacing:.15em;text-transform:uppercase;color:var(--gold);display:block;margin-bottom:4px}
  .hero-date-item .value{font-size:1.05rem}
  .hero-key{padding:0 0 36px;display:flex;justify-content:center;gap:24px;flex-wrap:wrap}
  .hero-key span{font-family:sans-serif;font-size:.82rem;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.15);border-radius:20px;padding:5px 16px;color:rgba(255,255,255,.75)}
  /* STICKY NAV */
  .sticky-nav{position:sticky;top:0;z-index:100;background:var(--ink);display:flex;justify-content:center;overflow-x:auto;scrollbar-width:none}
  .sticky-nav a{color:rgba(255,255,255,.65);text-decoration:none;font-family:sans-serif;font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;padding:13px 18px;white-space:nowrap;border-bottom:2px solid transparent;transition:all .2s}
  .sticky-nav a:hover{color:var(--gold)}
  /* SECTIONS */
  .dark-section{background:var(--ink);color:var(--white);padding:48px 24px}
  .dark-section h2{text-align:center;font-weight:normal;font-size:1.6rem;color:var(--gold-lt);margin-bottom:8px}
  .section-sub{text-align:center;opacity:.6;margin-bottom:36px;font-size:.9rem;font-family:sans-serif}
  /* SHIP INFO GRID */
  .ship-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;max-width:900px;margin:0 auto}
  .ship-card{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:var(--radius);padding:20px;text-align:center}
  .ship-card .s-value{font-size:1.3rem;font-family:Georgia;color:var(--gold-lt);margin-bottom:4px}
  .ship-card .s-label{font-family:sans-serif;font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;opacity:.55}
  /* BOOKING GRID */
  .booking-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;max-width:900px;margin:0 auto}
  .booking-card{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.1);border-radius:var(--radius);padding:20px}
  .booking-card .b-label{font-family:sans-serif;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);margin-bottom:6px}
  .booking-card .b-value{font-size:1rem;color:var(--white);line-height:1.5}
  .booking-card .b-note{font-family:sans-serif;font-size:.78rem;opacity:.5;margin-top:4px}
  .highlight-box{background:rgba(201,168,76,.12);border:1px solid var(--gold);border-radius:var(--radius);padding:20px;text-align:center;margin-top:24px;max-width:600px;margin-left:auto;margin-right:auto}
  .highlight-box .hb-label{font-family:sans-serif;font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);margin-bottom:6px}
  .highlight-box .hb-value{font-size:1.3rem;color:var(--gold-lt)}
  /* ROUTE MAP */
  .map-section{padding:48px 24px;max-width:960px;margin:0 auto}
  .map-section h2{text-align:center;font-weight:normal;font-size:1.6rem;margin-bottom:8px}
  .map-section .section-sub{text-align:center;opacity:.55;margin-bottom:32px;font-size:.9rem;font-family:sans-serif}
  .map-container{border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow)}
  .map-container img,.map-container svg{width:100%;height:auto;display:block}
  /* ITINERARY */
  .itinerary-section{padding:48px 24px;max-width:860px;margin:0 auto}
  .itinerary-section h2{text-align:center;font-weight:normal;font-size:1.6rem;margin-bottom:8px}
  .itinerary-section .section-sub{text-align:center;opacity:.55;margin-bottom:36px;font-size:.9rem;font-family:sans-serif}
  .day-card{background:#fff;border-radius:var(--radius);box-shadow:var(--shadow);margin-bottom:18px;overflow:hidden;display:grid;grid-template-columns:80px 1fr;min-width:0}
  .day-card.at-sea{background:#f8f6f0}
  .day-label{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px 8px;color:#fff;font-family:sans-serif;text-align:center;min-height:120px}
  .day-label .dn{font-size:1.4rem;font-weight:bold;line-height:1}
  .day-label .dm{font-size:.6rem;opacity:.85;letter-spacing:.04em;text-transform:uppercase;margin-top:3px}
  .day-label .dw{font-size:.6rem;opacity:.65;margin-top:3px}
  .day-body{padding:18px 22px 18px 18px}
  .day-body h3{font-size:1.05rem;margin-bottom:10px;color:var(--ink);font-weight:normal;font-style:italic}
  .port-meta{font-family:sans-serif;font-size:.78rem;opacity:.65;margin-bottom:12px;display:flex;gap:16px;flex-wrap:wrap}
  .port-meta span{display:flex;align-items:center;gap:4px}
  .act-list{list-style:none}
  .act-list li{display:flex;gap:8px;padding:4px 0;font-size:.88rem;border-bottom:1px solid rgba(0,0,0,.05);align-items:flex-start}
  .act-list li:last-child{border:none}
  .act-icon{min-width:18px;text-align:center;margin-top:2px}
  .city-pill{background:var(--ink);color:var(--white);padding:4px 14px;border-radius:20px;font-family:sans-serif;font-size:.78rem}
  /* TIPS */
  .tips-section{padding:48px 24px}
  .tips-section h2{text-align:center;font-weight:normal;font-size:1.6rem;margin-bottom:32px}
  .tips-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;max-width:900px;margin:0 auto}
  .tip-card{background:#fff;border-radius:var(--radius);padding:20px;box-shadow:0 2px 12px rgba(0,0,0,.07)}
  .tip-icon{font-size:1.5rem;margin-bottom:8px}
  .tip-title{font-size:.9rem;font-weight:bold;font-family:sans-serif;margin-bottom:6px}
  .tip-body{font-size:.82rem;color:#555;line-height:1.5}
  footer{background:var(--ink);color:rgba(255,255,255,.4);text-align:center;padding:28px 24px;font-family:sans-serif;font-size:.8rem}
  footer .gold{color:var(--gold-lt)}
  /* COLOUR LABELS for days */
  .l-southampton .day-label{background:#1a4a7a}
  .l-falmouth .day-label{background:#2a6a8a}
  .l-cork .day-label{background:#1a5a3a}
  .l-dublin .day-label{background:#7a3a8a}
  .l-liverpool .day-label{background:#8a2a2a}
  .l-belfast .day-label{background:#3a3a7a}
  .l-glasgow .day-label{background:#3a6a5a}
  .l-invergordon .day-label{background:#4a3a2a}
  .l-edinburgh .day-label{background:#5a2a4a}
  .l-lehavre .day-label{background:#5a3a2a}
  .l-atsea .day-label{background:#3a4a5a}
  .l-depart .day-label{background:#1a3a5a}
  @media(max-width:600px){.day-card{grid-template-columns:64px 1fr}.day-body{padding:14px}.hero-dates{gap:20px}}
</style>
</head>
<body>

<!-- HERO -->
<header class="hero">
  <div style="position:relative;">
    <img class="hero-ship" src="imgs/majestic-princess-cruise-ship-at-sea.jpg" alt="Majestic Princess cruise ship at sea">
    <div class="hero-overlay">
      <div class="hero-badge">Tam Family · May 1–13, 2027</div>
      <h1>Majestic Princess<br><em>British Isles Adventure</em></h1>
      <p class="hero-sub">12 Nights · Southampton to Southampton · Princess Cruises</p>
      <div class="hero-dates">
        <div class="hero-date-item"><span class="label">Embark</span><span class="value">May 1, 2027 · Southampton</span></div>
        <div class="hero-date-item"><span class="label">Disembark</span><span class="value">May 13, 2027 · Southampton</span></div>
      </div>
      <div class="hero-key">
        <span>🛳 Majestic Princess</span>
        <span>🏛 Cabin R616 · Deck</span>
        <span>👤 Ken &amp; Mabel</span>
        <span>✈ No flights required</span>
        <span>🌊 12 nights / 13 days</span>
      </div>
    </div>
  </div>
</header>

<!-- NAV -->
<nav class="sticky-nav">
  <a href="#booking">Booking</a>
  <a href="#ship">The Ship</a>
  <a href="#map">Route Map</a>
  <a href="#itinerary">Itinerary</a>
  <a href="#tips">Tips</a>
</nav>

<!-- BOOKING -->
<section class="dark-section" id="booking">
  <h2>Booking Details</h2>
  <p class="section-sub">Confirmed · Booking Ref: DN8N7C · Tokui Travel Services</p>
  <div class="booking-grid">
    <div class="booking-card">
      <div class="b-label">Passengers</div>
      <div class="b-value">Mr. Ken Kwok Wai Tam<br>Ms. Mabel Tak Ching Chu</div>
    </div>
    <div class="booking-card">
      <div class="b-label">Stateroom</div>
      <div class="b-value">R616 · Category S4<br>Queen Bed · Middle Ship</div>
    </div>
    <div class="booking-card">
      <div class="b-label">Voyage</div>
      <div class="b-value">8720 · 12 Days Europe — British Isles<br>Embarkation: May 1, 2027</div>
    </div>
    <div class="booking-card">
      <div class="b-label">Agency</div>
      <div class="b-value">Tokui Travel Services<br>Mei King · Richmond BC · 604-303-0520</div>
    </div>
  </div>
  <div class="highlight-box">
    <div class="hb-label">Fare (per person / total)</div>
    <div class="hb-value">CAD $7,900.02 / CAD $15,800.04</div>
  </div>
  <div style="max-width:600px;margin:24px auto 0;text-align:center;">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;text-align:left;">
      <div style="background:rgba(255,255,255,.05);border-radius:8px;padding:14px 16px;">
        <div style="font-family:sans-serif;font-size:.7rem;color:var(--gold);letter-spacing:.1em;text-transform:uppercase;margin-bottom:4px;">Deposit Due</div>
        <div style="font-size:1.05rem;color:#fff;">CAD $1,360.00</div>
        <div style="font-family:sans-serif;font-size:.75rem;opacity:.5;margin-top:4px;">By March 10, 2026</div>
      </div>
      <div style="background:rgba(255,255,255,.05);border-radius:8px;padding:14px 16px;">
        <div style="font-family:sans-serif;font-size:.7rem;color:var(--gold);letter-spacing:.1em;text-transform:uppercase;margin-bottom:4px;">Final Payment</div>
        <div style="font-size:1.05rem;color:#fff;">CAD $15,800.04</div>
        <div style="font-family:sans-serif;font-size:.75rem;opacity:.5;margin-top:4px;">By January 31, 2027</div>
      </div>
    </div>
    <div style="margin-top:16px;font-family:sans-serif;font-size:.78rem;opacity:.45;line-height:1.6;">
      ⚠ Cancellation: 25% from Feb 1 · 50% from Feb 16 · 75% from Mar 2 · 100% from Apr 1, 2027
    </div>
  </div>
</section>

<!-- SHIP -->
<section class="dark-section" id="ship" style="background:#061825;">
  <h2>🛳 The Ship — Majestic Princess</h2>
  <p class="section-sub">Registered under the Bermudan flag · A Princess Class cruise ship</p>
  <div class="ship-grid">
    <div class="ship-card"><div class="s-value">145,000</div><div class="s-label">Gross Tons</div></div>
    <div class="ship-card"><div class="s-value">3,560</div><div class="s-label">Guest Capacity</div></div>
    <div class="ship-card"><div class="s-value">19</div><div class="s-label">Decks</div></div>
    <div class="ship-card"><div class="s-value">2017</div><div class="s-label">Year Built</div></div>
    <div class="ship-card"><div class="s-value">Princess</div><div class="s-label">Cruise Line</div></div>
    <div class="ship-card"><div class="s-value">Bermudan</div><div class="s-label">Registry</div></div>
  </div>
</section>

<!-- ROUTE MAP -->
<section class="map-section" id="map">
  <h2>🗺️ Cruise Route Map</h2>
  <p class="section-sub">12-day British Isles itinerary · Southampton round-trip</p>
  <div class="map-container">
    <img src="imgs/route-map.svg" alt="British Isles cruise route map" width="100%">
  </div>
</section>

<!-- ITINERARY -->
<section class="itinerary-section" id="itinerary">
  <h2>🗓 Day-by-Day Itinerary</h2>
  <p class="section-sub">May 1–13, 2027 · 12 nights · Majestic Princess</p>

  <div class="day-card l-southampton">
    <div class="day-label"><span class="dn">D1</span><span class="dm">May 1</span><span class="dw">Fri</span></div>
    <div class="day-body">
      <h3>Embarkation — Southampton, England</h3>
      <div class="port-meta"><span>📍 Southampton · No Transfer To Ship</span><span>🕛 Board from 4:00 PM</span></div>
      <ul class="act-list">
        <li><span class="act-icon">🚢</span><span>Board the Majestic Princess at Southampton Cruise Terminal</span></li>
        <li><span class="act-icon">🍽️</span><span>Explore the ship's restaurants, pools, and amenities</span></li>
        <li><span class="act-icon">🌅</span><span>Set sail and enjoy dinner with views of the Solent</span></li>
      </ul>
    </div>
  </div>

  <div class="day-card l-falmouth">
    <div class="day-label"><span class="dn">D2</span><span class="dm">May 2</span><span class="dw">Sat</span></div>
    <div class="day-body">
      <h3>Falmouth, Cornwall — The Cornish Riviera</h3>
      <div class="port-meta"><span>📍 Falmouth, Cornwall · Docked</span><span>🕖 Arrive 7:00 AM · Depart 6:00 PM</span></div>
      <ul class="act-list">
        <li><span class="act-icon">⚓</span><span>Explore the historic harbour — Britain's deepest natural port</span></li>
        <li><span class="act-icon">🏖️</span><span>Stroll the River Fal walks and the old town</span></li>
        <li><span class="act-icon">🐟</span><span>Try fresh Cornish pasties and local seafood at the waterfront</span></li>
        <li><span class="act-icon">🌊</span><span>Optional: Day trip to the Eden Project or St Ives</span></li>
      </ul>
    </div>
  </div>

  <div class="day-card l-cork">
    <div class="day-label"><span class="dn">D3</span><span class="dm">May 3</span><span class="dw">Sun</span></div>
    <div class="day-body">
      <h3>Cobh (Cork), Ireland — Queenstown</h3>
      <div class="port-meta"><span>📍 Cobh, County Cork · Docked</span><span>🕖 Arrive 7:00 AM · Depart 6:00 PM</span></div>
      <ul class="act-list">
        <li><span class="act-icon">🎺</span><span>Cobh — Ireland's only cruise-only port, famed for its Victorian architecture</span></li>
        <li><span class="act-icon">🚢</span><span>The Titanic's last port of call in 1912 — visit the Titanic Experience</span></li>
        <li><span class="act-icon">⛪</span><span>Stroll the "Deck of Cards" — rows of brightly coloured houses above the harbour</span></li>
        <li><span class="act-icon">🍀</span><span>Traditional Irish music in the pubs of Cobh</span></li>
      </ul>
    </div>
  </div>

  <div class="day-card l-dublin">
    <div class="day-label"><span class="dn">D4</span><span class="dm">May 4</span><span class="dw">Mon</span></div>
    <div class="day-body">
      <h3>Dublin (Dun Laoghaire), Ireland — The Fair City</h3>
      <div class="port-meta"><span>📍 Dun Laoghaire · Docked</span><span>🕖 Arrive 7:00 AM · Depart 7:00 PM</span></div>
      <ul class="act-list">
        <li><span class="act-icon">🏛️</span><span>Dublin — Trinity College, Temple Bar, Grafton Street</span></li>
        <li><span class="act-icon">🪶</span><span>Guinness Storehouse and the legendary Temple Bar pub district</span></li>
        <li><span class="act-icon">🏰</span><span>St. Patrick's Cathedral and Dublin Castle</span></li>
        <li><span class="act-icon">🍺</span><span>Enjoy an evening in Dublin's world-famous pub culture</span></li>
      </ul>
    </div>
  </div>

  <div class="day-card l-liverpool">
    <div class="day-label"><span class="dn">D5</span><span class="dm">May 5</span><span class="dw">Tue</span></div>
    <div class="day-body">
      <h3>Liverpool, England — Maritime Heritage City</h3>
      <div class="port-meta"><span>📍 Liverpool · Docked</span><span>🕗 Arrive 8:30 AM · Depart 7:00 PM</span></div>
      <ul class="act-list">
        <li><span class="act-icon">🎭</span><span>The Three Graces — Liverpool's iconic UNESCO waterfront landmark</span></li>
        <li><span class="act-icon">�Beatles</span><span>The Beatles Story at the Royal Albert Dock</span></li>
        <li><span class="act-icon">⚽</span><span>Home of Liverpool FC and Everton FC — football culture alive and well</span></li>
        <li><span class="act-icon">🚢</span><span>Maritime Museum and the historic Albert Dock</span></li>
      </ul>
    </div>
  </div>

  <div class="day-card l-belfast">
    <div class="day-label"><span class="dn">D6</span><span class="dm">May 6</span><span class="dw">Wed</span></div>
    <div class="day-body">
      <h3>Belfast, Northern Ireland — Titanic's Birthplace</h3>
      <div class="port-meta"><span>📍 Belfast · Docked</span><span>🕢 Arrive 7:30 AM · Depart 8:00 PM</span></div>
      <ul class="act-list">
        <li><span class="act-icon">🚢</span><span>Titanic Belfast — the world's largest Titanic visitor experience</span></li>
        <li><span class="act-icon">🏭</span><span>Harland &amp; Wolff shipyard — where the Titanic was built</span></li>
        <li><span class="act-icon">🏛️</span><span>Belfast City Hall and the historic Cathedral Quarter</span></li>
        <li><span class="act-icon">🍀</span><span>Traditional Ulster cuisine and the famous Crown Bar</span></li>
      </ul>
    </div>
  </div>

  <div class="day-card l-glasgow">
    <div class="day-label"><span class="dn">D7</span><span class="dm">May 7</span><span class="dw">Thu</span></div>
    <div class="day-body">
      <h3>Glasgow (Greenock), Scotland — Industrial Heritage &amp; Culture</h3>
      <div class="port-meta"><span>📍 Greenock · Docked</span><span>🕗 Arrive 8:00 AM · Depart 7:30 PM</span></div>
      <ul class="act-list">
        <li><span class="act-icon">🏛️</span><span>Kelvingrove Art Gallery &amp; Museum and George Square</span></li>
        <li><span class="act-icon">🎨</span><span>UNESCO World Heritage Centre and the Riverside Museum</span></li>
        <li><span class="act-icon">🌿</span><span>Glasgow's "Dear Green Place" — pollok park and the West End</span></li>
        <li><span class="act-icon">🥃</span><span>Scottish whisky tasting — a dram not to be missed</span></li>
      </ul>
    </div>
  </div>

  <div class="day-card l-atsea">
    <div class="day-label"><span class="dn">D8</span><span class="dm">May 8</span><span class="dw">Fri</span></div>
    <div class="day-body">
      <h3>At Sea — Relax &amp; Enjoy the Majestic Princess</h3>
      <div class="port-meta"><span>🚢 Full day at sea</span></div>
      <ul class="act-list">
        <li><span class="act-icon">🏊</span><span>Enjoy the ship's pools, spa, and fitness centre</span></li>
        <li><span class="act-icon">🎭</span><span>Broadway-style shows, live music, and enrichment programs</span></li>
        <li><span class="act-icon">🍽️</span><span>Dining in multiple restaurants — explore the ship's culinary offerings</span></li>
        <li><span class="act-icon">☕</span><span>High tea at sea — a classic Princess tradition</span></li>
      </ul>
    </div>
  </div>

  <div class="day-card l-invergordon">
    <div class="day-label"><span class="dn">D9</span><span class="dm">May 9</span><span class="dw">Sat</span></div>
    <div class="day-body">
      <h3>Invergordon, Scotland — Gateway to the Highlands</h3>
      <div class="port-meta"><span>📍 Invergordon · Docked</span><span>🕖 Arrive 7:00 AM · Depart 6:00 PM</span></div>
      <ul class="act-list">
        <li><span class="act-icon">🏰</span><span>Explore the Scottish Highlands — ancient castles and dramatic landscapes</span></li>
        <li><span class="act-icon">🥃</span><span>Whisky distilleries of the Glenmorangie and Dalmore</span></li>
        <li><span class="act-icon">🏔️</span><span>Loch Ness, Culloden Battlefield, and Dornoch Firth</span></li>
        <li><span class="act-icon">🌿</span><span>Scenic drives through the stunning Highland scenery</span></li>
      </ul>
    </div>
  </div>

  <div class="day-card l-edinburgh">
    <div class="day-label"><span class="dn">D10</span><span class="dm">May 10</span><span class="dw">Sun</span></div>
    <div class="day-body">
      <h3>Edinburgh (Leith), Scotland — A Tale of Two Cities</h3>
      <div class="port-meta"><span>📍 Leith Port · Docked</span><span>🕗 Arrive 8:00 AM · Depart 8:00 PM</span></div>
      <ul class="act-list">
        <li><span class="act-icon">🏰</span><span>Edinburgh Castle and the UNESCO-listed Royal Mile</span></li>
        <li><span class="act-icon">👑</span><span>Palace of Holyroodhouse — the King's official Scottish residence</span></li>
        <li><span class="act-icon">🏛️</span><span>Scottish Parliament and Arthur's Seat — the ancient volcano hike</span></li>
        <li><span class="act-icon">🎻</span><span>Old Town, New Town, and the city's legendary underground vaults</span></li>
      </ul>
    </div>
  </div>

  <div class="day-card l-atsea">
    <div class="day-label"><span class="dn">D11</span><span class="dm">May 11</span><span class="dw">Mon</span></div>
    <div class="day-body">
      <h3>At Sea — Another Day in Paradise</h3>
      <div class="port-meta"><span>🚢 Full day at sea</span></div>
      <ul class="act-list">
        <li><span class="act-icon">📚</span><span>Princesses' enrichment lectures and destination talks</span></li>
        <li><span class="act-icon">🛍️</span><span>Shopping in the ship's boutiques — duty-free luxury goods</span></li>
        <li><span class="act-icon">🌅</span><span>Final evening at sea — dress up for the Captain's Dinner</span></li>
        <li><span class="act-icon">🍾</span><span>Celebrate a wonderful voyage with a cocktail in the星空酒吧</span></li>
      </ul>
    </div>
  </div>

  <div class="day-card l-lehavre">
    <div class="day-label"><span class="dn">D12</span><span class="dm">May 12</span><span class="dw">Tue</span></div>
    <div class="day-body">
      <h3>Le Havre (Paris &amp; Normandy), France — The Gateway to Paris</h3>
      <div class="port-meta"><span>📍 Le Havre, Normandy · Docked</span><span>🕖 Arrive 7:00 AM · Depart 8:00 PM</span></div>
      <ul class="act-list">
        <li><span class="act-icon">🗼</span><span>Day trip to Paris — Eiffel Tower, Louvre, Notre-Dame</span></li>
        <li><span class="act-icon">⛵</span><span>Honfleur — the most picturesque fishing port in France</span></li>
        <li><span class="act-icon">🏖️</span><span>Omaha Beach and the D-Day landing beaches of Normandy</span></li>
        <li><span class="act-icon">🍷</span><span>Calvados distilleries and Normandy's famous cider and cheese</span></li>
      </ul>
    </div>
  </div>

  <div class="day-card l-depart">
    <div class="day-label"><span class="dn">D13</span><span class="dm">May 13</span><span class="dw">Wed</span></div>
    <div class="day-body">
      <h3>Disembarkation — Southampton, England</h3>
      <div class="port-meta"><span>📍 Southampton · No Transfer From Ship</span><span>🕖 Disembark from 7:00 AM</span></div>
      <ul class="act-list">
        <li><span class="act-icon">🏠</span><span>Disembark the Majestic Princess — home port Southampton</span></li>
        <li><span class="act-icon">✈️</span><span>Onward travel or overnight stay in London as preferred</span></li>
      </ul>
    </div>
  </div>
</section>

<!-- TIPS -->
<section class="tips-section" id="tips">
  <h2>📋 Cruise Travel Tips</h2>
  <div class="tips-grid">
    <div class="tip-card">
      <div class="tip-icon">📄</div>
      <div class="tip-title">Passports Required</div>
      <div class="tip-body">Valid passport required — must be valid 6 months beyond completion of travel with enough blank pages. Ensure your name matches exactly as on the booking.</div>
    </div>
    <div class="tip-card">
      <div class="tip-icon">💱</div>
      <div class="tip-title">Onboard Currency</div>
      <div class="tip-body">The ship's currency is US Dollars. Princess MedallionClass allows cashless payments. Credit cards are accepted for onboard accounts.</div>
    </div>
    <div class="tip-card">
      <div class="tip-icon">🚬</div>
      <div class="tip-title">Smoking Policy</div>
      <div class="tip-body">Smoking is not permitted in staterooms, balconies, or most indoor areas. Designated outdoor smoking areas only.</div>
    </div>
    <div class="tip-card">
      <div class="tip-icon">🦽</div>
      <div class="tip-title">Mobility</div>
      <div