#!/usr/bin/env python3
"""Build Chan Kenya Safari 2026 webpage"""
import shutil, os, subprocess

SRC = '/workspace/kenya-safari-2026'
DST = '/workspace/chan-kenya-2026'
TOKEN = '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'
GITHUB_USER = 'ktamxl'

# Copy project
if os.path.exists(DST):
    shutil.rmtree(DST)
shutil.copytree(SRC, DST)
os.makedirs(f'{DST}/imgs', exist_ok=True)
for img in ['masai-mara-male-lion-golden-plains-safari.jpg','flamingos-lake-nakuru-kenya.jpg',
    'black-rhino-ol-pejeta-kenya-safari.jpg','reticulated-giraffe-samburu-kenya-safari.jpg',
    'nairobi-kenya-city-skyline-at-night.jpg']:
    shutil.copy2(f'{SRC}/imgs/{img}', f'{DST}/imgs/{img}')

# Write index.html - using a separate file approach
html_body = '''<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Chan Family Kenya Safari 2026</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}:root{--ink:#1a1a2e;--soft:#f5f2ec;--white:#ffffff;--gold:#c9a84c;--gold-lt:#f0d98a;--radius:12px;--shadow:0 4px 20px rgba(0,0,0,.12)}
html{scroll-behavior:smooth}body{font-family:Georgia,'Times New Roman',serif;background:var(--soft);color:var(--ink);line-height:1.7}
.hero{background:linear-gradient(160deg,#0d2137 0%,#1a3a52 50%,#0d3d4f 100%);color:#fff;text-align:center;padding:72px 24px 56px}
.hero-badge{display:inline-block;border:1px solid var(--gold);color:var(--gold-lt);font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;padding:4px 18px;border-radius:20px;margin-bottom:20px}
.hero h1{font-size:clamp(1.8rem,5vw,3rem);font-weight:normal;letter-spacing:.02em;margin-bottom:12px;line-height:1.25;color:#fff}
.hero-sub{font-size:1.05rem;opacity:.8;margin-bottom:32px}
.hero-dates{display:flex;justify-content:center;gap:32px;flex-wrap:wrap;margin-bottom:32px}
.hero-date-item{text-align:center}.hero-date-item .label{font-family:sans-serif;font-size:.72rem;letter-spacing:.15em;text-transform:uppercase;color:var(--gold);display:block;margin-bottom:4px}
.hero-date-item .value{font-size:1.05rem;color:#fff}
.hero-cities{display:flex;justify-content:center;gap:16px;flex-wrap:wrap}
.city-pill{padding:6px 20px;border-radius:20px;font-size:.88rem;font-family:sans-serif;color:#fff}
.city-pill.sh{background:#8b4513}.city-pill.sz{background:#8b6914}.city-pill.hk{background:#2d6a30}
.sticky-nav{position:sticky;top:0;z-index:100;background:var(--ink);display:flex;justify-content:center;overflow-x:auto;scrollbar-width:none}
.sticky-nav a{color:rgba(255,255,255,.7);text-decoration:none;font-family:sans-serif;font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;padding:13px 18px;white-space:nowrap;border-bottom:2px solid transparent;transition:all .2s}
.sticky-nav a:hover{color:var(--gold)}
.dark-section{background:var(--ink);color:#fff;padding:48px 24px}
.dark-section h2{text-align:center;font-weight:normal;font-size:1.6rem;color:var(--gold-lt);margin-bottom:8px}
.section-sub{text-align:center;opacity:.6;margin-bottom:32px;font-size:.9rem;font-family:sans-serif}
.family-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;max-width:900px;margin:0 auto}
.family-card{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);border-radius:var(--radius);padding:20px;text-align:center}
.family-card .f-name{font-size:1rem;margin-bottom:6px}
.family-card .f-detail{font-family:sans-serif;font-size:.78rem;opacity:.65;line-height:1.5}
.flights-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;max-width:920px;margin:0 auto}
.flight-card{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:var(--radius);padding:20px 22px}
.flight-card .airline{font-family:sans-serif;font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:10px}
.flight-route{display:flex;align-items:center;gap:10px;margin-bottom:10px}
.flight-route .airport{font-size:1.6rem;font-weight:bold;font-family:sans-serif;letter-spacing:.05em}
.flight-route .arrow{flex:1;text-align:center;opacity:.4;font-size:1.2rem}
.flight-meta{font-family:sans-serif;font-size:.8rem;opacity:.72;line-height:1.7}
.flight-note{margin-top:8px;font-size:.76rem;opacity:.5;font-family:sans-serif;font-style:italic}
.badge-confirmed{display:inline-block;background:var(--gold);color:var(--ink);font-size:.62rem;font-family:sans-serif;letter-spacing:.1em;text-transform:uppercase;padding:2px 7px;border-radius:3px;font-weight:bold}
.city-banner{padding:48px 24px 36px;color:#fff;position:relative;overflow:hidden;background-size:cover;background-position:center}
.city-banner.ks{background-image:url(imgs/nairobi-kenya-city-skyline-at-night.jpg)}
.city-banner.sr{background-image:url(imgs/reticulated-giraffe-samburu-kenya-safari.jpg)}
.city-banner.op{background-image:url(imgs/black-rhino-ol-pejeta-kenya-safari.jpg)}
.city-banner.nk{background-image:url(imgs/flamingos-lake-nakuru-kenya.jpg)}
.city-banner.mm{background-image:url(imgs/masai-mara-male-lion-golden-plains-safari.jpg)}
.city-banner-inner{max-width:900px;margin:0 auto;position:relative;z-index:1}
.city-banner .eyebrow{font-family:sans-serif;font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;opacity:.7;margin-bottom:8px}
.city-banner h2{font-size:clamp(2rem,6vw,3rem);font-weight:normal;margin-bottom:8px}
.city-banner .dates-tag{font-family:sans-serif;font-size:.88rem;opacity:.85;margin-bottom:12px}
.hotel-chips{display:flex;flex-wrap:wrap;gap:8px}
.hotel-chip{display:inline-flex;align-items:center;gap:5px;background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:4px 14px;font-size:.8rem;font-family:sans-serif}
.city-section{padding-bottom:48px}
.days-container{max-width:900px;margin:0 auto;padding:28px 24px 0}
.day-card{background:#fff;border-radius:var(--radius);box-shadow:var(--shadow);margin-bottom:18px;overflow:hidden;display:grid;grid-template-columns:76px 1fr}
.day-label{display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding:20px 6px;color:#fff;font-family:sans-serif;text-align:center}
.day-card.sh .day-label{background:#8b4513}.day-card.sr .day-label{background:#8b6914}.day-card.op .day-label{background:#2d6a30}.day-card.nk .day-label{background:#8b1444}.day-card.mm .day-label{background:#4a148c}
.day-label .dn{font-size:1.5rem;font-weight:bold;line-height:1}.day-label .dm{font-size:.62rem;opacity:.85;letter-spacing:.04em;text-transform:uppercase;margin-top:2px}.day-label .dw{font-size:.6rem;opacity:.65;margin-top:3px}
.day-body{padding:18px 22px 18px 18px}
.day-body h3{font-size:1rem;margin-bottom:12px;color:var(--ink);font-weight:normal;font-style:italic}
.transit-bar{background:#f8f6f0;border:1px solid rgba(0,0,0,.08);border-radius:8px;padding:8px 12px;margin-bottom:12px;font-size:.8rem;font-family:sans-serif;color:#555}
.transit-bar.flight{background:#fffbf0;border-color:#e6c96e;color:#5a4200}
.transit-bar.transfer{background:#f0f8f0;border-color:#7cb87c;color:#2a5a2a}
.act-list{list-style:none}.act-list li{display:flex;gap:8px;padding:5px 0;border-bottom:1px solid rgba(0,0,0,.05);font-size:.88rem;align-items:flex-start}
.act-list li:last-child{border:none}.act-icon{min-width:18px;text-align:center;font-size:.85rem;margin-top:3px}.act-main{flex:1}.act-name{color:var(--ink)}.act-tip{font-size:.75rem;color:#777;font-style:italic;margin-top:1px}
.tips-section{padding:48px 24px}.tips-section h2{text-align:center;font-weight:normal;font-size:1.6rem;margin-bottom:32px}
.tips-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;max-width:900px;margin:0 auto}
.tip-card{background:#fff;border-radius:var(--radius);padding:20px;box-shadow:0 2px 12px rgba(0,0,0,.07)}
.tip-icon{font-size:1.5rem;margin-bottom:8px}.tip-title{font-size:.9rem;font-weight:bold;font-family:sans-serif;margin-bottom:6px}.tip-body{font-size:.82rem;color:#555;line-height:1.5}
footer{background:var(--ink);color:rgba(255,255,255,.45);text-align:center;padding:28px 24px;font-family:sans-serif;font-size:.8rem}
footer .gold{color:var(--gold)}
@media(max-width:600px){.day-card{grid-template-columns:60px 1fr}.day-body{padding:14px}}
</style></head>
<body>
<section class="hero"><div class="hero-badge">Chan Family · July 17–27, 2026</div>
<h1>Nairobi · Samburu · Masai Mara</h1>
<p class="hero-sub">An 8-night East African safari — Archie, Katherine, Stephen, Elsie &amp; Henry</p>
<div class="hero-dates">
<div class="hero-date-item"><span class="label">Depart YVR</span><span class="value">Fri · Jul 17, 2026</span></div>
<div class="hero-date-item"><span class="label">Arrive Nairobi</span><span class="value">Sat · Jul 18, 2026</span></div>
<div class="hero-date-item"><span class="label">Back in YVR</span><span class="value">Mon · Jul 27, 2026</span></div>
</div>
<div class="hero-cities">
<span class="city-pill sh">Nairobi · Nights 1 &amp; 8</span>
<span class="city-pill sz">Samburu · 2 nights</span>
<span class="city-pill hk">Ol Pejeta · 1 night</span>
</div></section>

<nav class="sticky-nav">
<a href="#family">Family</a><a href="#flights">Flights</a><a href="#nairobi">Nairobi</a>
<a href="#samburu">Samburu</a><a href="#olpejeta">Ol Pejeta</a><a href="#nakuru">Nakuru</a>
<a href="#mara">Masai Mara</a><a href="#departure">Departure</a><a href="#tips">Tips</a>
</nav>

<section class="dark-section" id="family">
<h2>Our Safari Party</h2>
<p class="section-sub">5 travellers · JAMBO KENYA safari package · booked through Explore World Journeys · Vickie Cheema</p>
<div class="family-grid">
<div class="family-card"><div style="font-size:2rem;margin-bottom:8px;color:var(--gold);">&#9670;</div>
<div class="f-name">Archie &amp; Katherine Chan</div>
<div class="f-detail" style="text-align:left;margin-top:8px;">Mr. Archie Nga Chi Chan<br>Mrs. Katherine Gi Yuo Chan<br><br>Booking ref: <strong>B69QQC</strong></div>
</div>
<div class="family-card"><div style="font-size:2rem;margin-bottom:8px;color:var(--gold);">&#9733;</div>
<div class="f-name">Stephen Fan &amp; Elsie Leung</div>
<div class="f-detail" style="text-align:left;margin-top:8px;">Mr. Stephen Sui Wong Fan<br>Mrs. Elsie Leung<br><br>Booking ref: <strong>B69QQC</strong></div>
</div>
<div class="family-card"><div style="font-size:2rem;margin-bottom:8px;color:var(--gold);">&#9992;</div>
<div class="f-name">Henry Leung</div>
<div class="f-detail" style="text-align:left;margin-top:8px;">Mr. Henry Leung<br><br>Booking ref: <strong>B69QQC</strong></div>
</div>
</div></section>

<section class="dark-section" id="flights" style="background:#111827;">
<h2>&#9992 Flights</h2>
<p class="section-sub"><span class="badge-confirmed">&#10003; CONFIRMED</span> Air Canada &amp; Lufthansa · Economy Class · Booking ref: B69QQC · &#9888; Ticket by Jun 2, 2026</p>
<div class="flights-grid">
<div class="flight-card"><div class="airline">Air Canada AC 838 <span class="badge-confirmed">&#10003; CONFIRMED</span></div>
<div class="flight-route"><span class="airport">YVR</span><span class="arrow">&#9992;</span><span class="airport">FRA</span></div>
<div class="flight-meta">Fri Jul 17 · 13:15 &rarr; 08:05+1<br>9h 50m · Non-stop · Boeing 787-9 · Economy (M)</div>
<div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers · 2 bags each</div></div>
<div class="flight-card"><div class="airline">Air Canada AC 9610 · Operated by Lufthansa LH 590 <span class="badge-confirmed">&#10003; CONFIRMED</span></div>
<div class="flight-route"><span class="airport">FRA</span><span class="arrow">&#9992;</span><span class="airport">NBO</span></div>
<div class="flight-meta">Sat Jul 18 · 11:25 &rarr; 20:35<br>8h 10m · Non-stop · Boeing 787-9 · Economy (M) · Meal included</div>
<div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers · 2 bags each</div></div>
<div class="flight-card"><div class="airline">Lufthansa LH 591 <span class="badge-confirmed">&#10003; CONFIRMED</span></div>
<div class="flight-route"><span class="airport">NBO</span><span class="arrow">&#9992;</span><span class="airport">FRA</span></div>
<div class="flight-meta">Sun Jul 26 · 22:50 &rarr; Mon Jul 27 · 06:10<br>8h 20m · Non-stop · Boeing 787-9 · Economy (T) · Meal</div>
<div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers · 2 bags each</div></div>
<div class="flight-card"><div class="airline">Lufthansa LH 100 <span class="badge-confirmed">&#10003; CONFIRMED</span></div>
<div class="flight-route"><span class="airport">FRA</span><span class="arrow">&#9992;</span><span class="airport">MUC</span></div>
<div class="flight-meta">Mon Jul 27 · 09:45 &rarr; 10:40<br>55 min · Non-stop · Airbus A321 · Economy (T) · Refreshments</div>
<div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers · 2 bags each</div></div>
<div class="flight-card"><div class="airline">Lufthansa LH 476 <span class="badge-confirmed">&#10003; CONFIRMED</span></div>
<div class="flight-route"><span class="airport">MUC</span><span class="arrow">&#9992;</span><span class="airport">YVR</span></div>
<div class="flight-meta">Mon Jul 27 · 15:45 &rarr; 16:55<br>10h 10m · Non-stop · Airbus A350-900 · Economy (T) · Meal</div>
<div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers · 2 bags each</div></div>
</div>
<p class="flight-note" style="text-align:center;margin-top:20px;">&#9888; Ticket required before <strong>June 2, 2026 23:59</strong> &mdash; overdue will cancel without notice · CO&#8322;: 1,954 kg/person</p>
</section>

<section class="city-section" id="nairobi">
<div class="city-banner ks"><div class="city-banner-inner">
<div class="eyebrow">City 01 · Nairobi, Kenya · Nights 1 &amp; 8</div>
<h2>Nairobi</h2>
<div class="dates-tag">Jul 17 (arrival) &amp; Jul 26 (departure) · 2 nights</div>
<div class="hotel-chips"><span class="hotel-chip">M&#246;venpick Hotel &amp; Residences Nairobi · B&amp;B</span>
<span class="hotel-chip">Hilton Garden Inn Nairobi Airport · B&amp;B + Lunch · Free shuttle</span></div>
</div></div>
<div class="days-container">
<div class="day-card sh"><div class="day-label"><span class="dn">D0</span><span class="dm">Jul 17</span><span class="dw">Evening</span></div>
<div class="day-body"><h3>Day 0 &mdash; Depart Vancouver</h3>
<div class="transit-bar flight">&#9992; AC 838 · YVR 13:15 &rarr; FRA 08:05+1 · then AC 9610 (LH 590) FRA 11:25 &rarr; NBO 20:35</div>
<ul class="act-list">
<li><span class="act-icon">&#9992;</span><span class="act-main"><span class="act-name">AC 838 YVR &rarr; FRA</span> · 13:15 dep · Boeing 787-9 · All 5 passengers · Economy (M)</span></li>
<li><span class="act-icon">&#128742;</span><span class="act-main"><span class="act-name">Arrive Nairobi Jomo Kenyatta Intl</span> · 20:35 local time</span></li>
<li><span class="act-icon">&#127968;</span><span class="act-main"><span class="act-name">Check in: M&#246;venpick Hotel &amp; Residences Nairobi</span></span></li>
</ul></div></div></div></section>

<section class="city-section" id="samburu">
<div class="city-banner sr"><div class="city-banner-inner">
<div class="eyebrow">City 02 · Samburu National Reserve · Nights 2–3</div>
<h2>Samburu</h2>
<div class="dates-tag">Jul 18–20 · 2 nights</div>
<div class="hotel-chips"><span class="hotel-chip">Samburu Simba Lodge · Full Board</span></div>
</div></div>
<div class="days-container">
<div class="day-card sr"><div class="day-label"><span class="dn">D1–2</span><span class="dm">Jul 18–19</span><span class="dw">2 nights</span></div>
<div class="day-body"><h3>Samburu &mdash; Rare &amp; Beautiful</h3>
<div class="transit-bar transfer">&#128663; Transfer from Nairobi to Samburu National Reserve (~5–6 hrs by road)</div>
<ul class="act-list">
<li><span class="act-icon">&#129418;</span><span class="act-main"><span class="act-name">Game drives in 4×4 Land Cruiser with pop-up roof</span><span class="act-tip">Early morning &amp; late afternoon — best wildlife hours</span></span></li>
<li><span class="act-icon">&#129433;</span><span class="act-main"><span class="act-name">Reticulated Giraffe — unique to northern Kenya</span><span class="act-tip">Also: Grevy's Zebra, Somali Ostrich, Gerenuk, Beisa Oryx</span></span></li>
<li><span class="act-icon">&#128024;</span><span class="act-main"><span class="act-name">Elephant herds &amp; predator sightings</span><span class="act-tip">Lion and leopard commonly spotted</span></span></li>
<li><span class="act-icon">&#127746;</span><span class="act-main"><span class="act-name">Sundowners on the plains</span><span class="act-tip">Classic safari tradition — cold drinks at sunset</span></span></li>
<li><span class="act-icon">&#127968;</span><span class="act-main"><span class="act-name">Samburu Simba Lodge · Full Board · 2 nights</span></span></li>
</ul></div></div></div></section>

<section class="city-section" id="olpejeta">
<div class="city-banner op"><div class="city-banner-inner">
<div class="eyebrow">City 03 · Ol Pejeta Conservancy · Night 4</div>
<h2>Ol Pejeta</h2>
<div class="dates-tag">Jul 20 · 1 night</div>
<div class="hotel-chips"><span class="hotel-chip">Sweetwaters Serena Camp · Full Board</span></div>
</div></div>
<div class="days-container">
<div class="day-card op"><div class="day-label"><span class="dn">D3</span><span class="dm">Jul 20</span><span class="dw">1 night</span></div>
<div class="day-body"><h3>Ol Pejeta &mdash; Last Chance for the Northern White Rhino</h3>
<div class="transit-bar transfer">&#128663; Drive from Samburu to Ol Pejeta Conservancy (~2–3 hrs)</div>
<ul class="act-list">
<li><span class="act-icon">&#129434;</span><span class="act-main"><span class="act-name">Northern White Rhino — the last two on earth</span><span class="act-tip">Sweetwaters is the only place to see Najin &amp; Fatu</span></span></li>
<li><span class="act-icon">&#129445;</span><span class="act-main"><span class="act-name">Chimpanzee Sanctuary</span><span class="act-tip">Only chimpanzees in Kenya — rescued individuals</span></span></li>
<li><span class="act-icon">&#129418;</span><span class="act-main"><span class="act-name">Big Five game drives</span><span class="act-tip">Lion, elephant, buffalo, rhino — all present</span></span></li>
<li><span class="act-icon">&#127968;</span><span class="act-main"><span class="act-name">Sweetwaters Serena Camp · Full Board · 1 night</span></span></li>
</ul></div></div></div></section>

<section class="city-section" id="nakuru">
<div class="city-banner nk"><div class="city-banner-inner">
<div class="eyebrow">City 04 · Lake Nakuru · Night 5</div>
<h2>Lake Nakuru</h2>
<div class="dates-tag">Jul 21 · 1 night</div>
<div class="hotel-chips"><span class="hotel-chip">Lake Nakuru Sopa Lodge · Full Board</span></div>
</div></div>
<div class="days-container">
<div class="day-card nk"><div class="day-label"><span class="dn">D4</span><span class="dm">Jul 21</span><span class="dw">1 night</span></div>
<div class="day-body"><h3>Lake Nakuru &mdash; Flamingos &amp; White Rhino</h3>
<div class="transit-bar transfer">&#128663; Drive from Ol Pejeta to Lake Nakuru (~2–3 hrs)</div>
<ul class="act-list">
<li><span class="act-icon">&#129440;</span><span class="act-main"><span class="act-name">Thousands of flamingos on the soda lake</span><span class="act-tip">The lake turns vivid pink — one of Africa's most spectacular sights</span></span></li>
<li><span class="act-icon">&#129434;</span><span class="act-main"><span class="act-name">White Rhino sanctuary</span><span class="act-tip">Both black &amp; white rhinos present</span></span></li>
<li><span class="act-icon">&#129418;</span><span class="act-main"><span class="act-name">Leopard frequently spotted in the acacia woods</span><span class="act-tip">Lion and buffalo also common</span></span></li>
<li><span class="act-icon">&#127968;</span><span class="act-main"><span class="act-name">Lake Nakuru Sopa Lodge · Full Board · 1 night</span></span></li>
</ul></div></div></div></section>

<section class="city-section" id="mara">
<div class="city-banner mm"><div class="city-banner-inner">
<div class="eyebrow">City 05 · Masai Mara National Reserve · Nights 6–7</div>
<h2>Masai Mara</h2>
<div class="dates-tag">Jul 22–24 · 2 nights</div>
<div class="hotel-chips"><span class="hotel-chip">Mara Serena Safari Lodge · Full Board</span></div>
</div></div>
<div class="days-container">
<div class="day-card mm"><div class="day-label"><span class="dn">D5</span><span class="dm">Jul 22</span><span class="dw">Morning</span></div>
<div class="day-body"><h3>Masai Mara &mdash; The Greatest Wildlife Spectacle on Earth</h3>
<div class="transit-bar transfer">&#128663; Drive from Nakuru to Masai Mara via Naivasha (~5–6 hrs)</div>
<ul class="act-list">
<li><span class="act-icon">&#129418;</span><span class="act-main"><span class="act-name">Full-day game drives</span><span class="act-tip">Big cats — lion, leopard, cheetah on the golden plains</span></span></li>
<li><span class="act-icon">&#128034;</span><span class="act-main"><span class="act-name">Mara River — crocodiles &amp; crossings</span><span class="act-tip">July marks the start of the wildebeest migration</span></span></li>
<li><span class="act-icon">&#127746;</span><span class="act-main"><span class="act-name">Sunset over the Mara plains</span><span class="act-tip">One of Africa's most iconic landscapes</span></span></li>
<li><span class="act-icon">&#127968;</span><span class="act-main"><span class="act-name">Mara Serena Safari Lodge · Full Board · 2 nights</span></span></li>
</ul></div></div>
<div class="day-card mm"><div class="day-label"><span class="dn">D6</span><span class="dm">Jul 23</span><span class="dw">Full day</span></div>
<div class="day-body"><h3>Masai Mara &mdash; Second Full Day</h3>
<ul class="act-list">
<li><span class="act-icon">&#129418;</span><span class="act-main"><span class="act-name">Early morning game drive</span><span class="act-tip">Predators most active at dawn</span></span></li>
<li><span class="act-icon">&#129434;</span><span class="act-main"><span class="act-name">Wildebeest &amp; zebra on the move</span><span class="act-tip">July — the Great Migration is in full swing</span></span></li>
<li><span class="act-icon">&#127746;</span><span class="act-main"><span class="act-name">Afternoon game drive &amp; sunset</span><span class="act-tip">Final evening in the Mara</span></span></li>
<li><span class="act-icon">&#128663;</span><span class="act-main"><span class="act-name">Check out · Drive back to Nairobi (~5 hrs)</span></span></li>
</ul></div></div></div></section>

<section class="city-section" id="departure">
<div class="city-banner ks"><div class="city-banner-inner">
<div class="eyebrow">City 06 · Departure · Day 8</div>
<h2>Fly Home via Munich</h2>
<div class="dates-tag">Sun Jul 26 · Evening departure · Arrive Mon Jul 27 Vancouver</div>
</div></div>
<div class="days-container">
<div class="day-card sh"><div class="day-label"><span class="dn">D7</span><span class="dm">Jul 26</span><span class="dw">Day</span></div>
<div class="day-body"><h3>Day 7 &mdash; Last Day in Nairobi · Fly Home via Munich</h3>
<div class="transit-bar transfer">&#128663; Free morning in Nairobi — rest or last-minute shopping</div>
<ul class="act-list">
<li><span class="act-icon">&#127968;</span><span class="act-main"><span class="act-name">Check out Hilton Garden Inn Nairobi Airport · Shuttle to Jomo Kenyatta</span></span></li>
<li><span class="act-icon">&#9992;</span><span class="act-main"><span class="act-name">LH 591 · NBO 22:50 &rarr; FRA 06:10+1</span> Boeing 787-9 · All 5 passengers · Economy (T)</span></li>
<li><span class="act-icon">&#9992;</span><span class="act-main"><span class="act-name">LH 100 · FRA 09:45 &rarr; MUC 10:40</span> Airbus A321 · Short hop · Economy (T)</span></li>
<li><span class="act-icon">&#9992;</span><span class="act-main"><span class="act-name">LH 476 · MUC 15:45 &rarr; YVR 16:55</span> Airbus A350-900 · All 5 passengers · Economy (T)</span></li>
<li><span class="act-icon">&#127968;</span><span class="act-main"><span class="act-name">Arrive Vancouver</span> Mon Jul 27 · 16:55 · Welcome home!</span></li>
</ul></div></div></div></section>

<section class="tips-section" id="tips">
<h2>&#128276 Safari Travel Tips</h2>
<div class="tips-grid">
<div class="tip-card"><div class="tip-icon">&#127781;</div><div class="tip-title">July Weather in Kenya</div><div class="tip-body">Nairobi: 10–22°C · Samburu &amp; Mara: 14–26°C. Cool mornings &amp; evenings, warm midday. Bring layers — early game drives can be cold!</div></div>
<div class="tip-card"><div class="tip-icon">&#128717;</div><div class="tip-title">Packing for Safari</div><div class="tip-body">Neutral-coloured clothing (no bright colours for game drives) · Sun hat · Sunglasses · Binoculars · High-SPF sunscreen · Long-sleeve shirts</div></div>
<div class="tip-card"><div class="tip-icon">&#129514;</div><div class="tip-title">Health</div><div class="tip-body">Malaria prophylaxis recommended — visit a travel clinic. Yellow fever vaccine required. DEET mosquito repellent essential.</div></div>
<div class="tip-card"><div class="tip-icon">&#128181;</div><div class="tip-title">Money in Kenya</div><div class="tip-body">Kenyan Shilling (KES) — withdraw at ATM or exchange at airport. US Dollars widely accepted at lodges. Tip your safari guide USD 10–20/day.</div></div>
<div class="tip-card"><div class="tip-icon">&#128222;</div><div class="tip-title">Communications</div><div class="tip-body">Safari camps have limited WiFi — a perfect excuse to disconnect! Purchase a Safaricom or Airtel SIM at Nairobi airport for data.</div></div>
<div class="tip-card"><div class="tip-icon">&#9935;</div><div class="tip