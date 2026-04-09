import re

with open('/workspace/china-trip-2026/index.html', 'r') as f:
    china = f.read()

with open('/workspace/kenya-safari-2026/index_bak.html', 'r') as f:
    kenya_content = f.read()

# Extract CSS from China
css_match = re.search(r'<style>(.*?)</style>', china, re.DOTALL)
china_css = css_match.group(1)

# ─── BUILD KENYA HTML ───
# Replace CSS in-place with Kenya-specific overrides
kenya_css = china_css.replace('#1a1a2e', '#1a1a2e')  # keep base ink

# City colour overrides for Kenya
kenya_css += """
  /* Kenya city colour scheme */
  .city-pill.ks { background:#8b4513; }
  .city-pill.sr { background:#8b6914; }
  .city-pill.op { background:#2d6a30; }
  .city-pill.nk { background:#8b1444; }
  .city-pill.mm { background:#4a148c; }
  .city-banner.ks { background:linear-gradient(135deg,#2d1a0f,#8b4513,#c07820); }
  .city-banner.sr { background:linear-gradient(135deg,#3d2800,#8b6914,#c8a030); }
  .city-banner.op { background:linear-gradient(135deg,#0f2d1a,#2d6a30,#50a850); }
  .city-banner.nk { background:linear-gradient(135deg,#2d0f1a,#8b1444,#e05080); }
  .city-banner.mm { background:linear-gradient(135deg,#1a0f2d,#4a148c,#8060c0); }
  .day-card.ks .day-label { background:#8b4513; }
  .day-card.sr .day-label { background:#8b6914; }
  .day-card.op .day-label { background:#2d6a30; }
  .day-card.nk .day-label { background:#8b1444; }
  .day-card.mm .day-label { background:#4a148c; }
"""

# ── HERO ──
kenya_hero = """
<section class="hero">
  <div class="hero-badge">Tam Family · July 17–27, 2026</div>
  <h1><span class="sh-city">Nairobi</span> · <span class="sz-city">Samburu</span> · <span class="hk-city">Masai Mara</span></h1>
  <p class="hero-sub">An 8-night East African safari — Ken &amp; Mabel &amp; Suzie</p>
  <div class="hero-dates">
    <div class="hero-date-item"><span class="label">Depart YVR</span><span class="value">Fri · Jul 17, 2026</span></div>
    <div class="hero-date-item"><span class="label">Arrive Nairobi</span><span class="value">Sat · Jul 18, 2026</span></div>
    <div class="hero-date-item"><span class="label">Back in SF</span><span class="value">Mon · Jul 27, 2026</span></div>
  </div>
  <div class="hero-cities">
    <span class="city-pill sh">🏙 Nairobi · Nights 1 &amp; 8</span>
    <span class="city-pill sz">🏝 Samburu · 2 nights</span>
    <span class="city-pill hk">🦏 Ol Pejeta · 1 night</span>
  </div>
</section>
"""

# ── TRAVELLER SECTION (dark) ──
kenya_family = """
<section class="dark-section" id="family">
  <h2>Our Safari Party</h2>
  <p class="section-sub">3 travellers · JAMBO KENYA safari package · booked through Explore World Journeys</p>
  <div class="family-grid">
    <div class="family-card">
      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">♡</div>
      <div class="f-name">Ken Tam &amp; Mabel Chu</div>
      <div class="f-detail" style="text-align:left;margin-top:8px;">
        Confirmation: <strong>24549</strong> · Ref: JAMBO KENYA<br>
        Double Room · 2 travellers<br>
        Tour: $17,326 × 2 = <strong>$34,652</strong><br>
        Paid: $24,000 · Balance: <strong>$10,652</strong><br>
        <span style="color:#f0d98a">Due Apr 20, 2026</span>
      </div>
    </div>
    <div class="family-card">
      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">★</div>
      <div class="f-name">Suzie Suet Ying Tam</div>
      <div class="f-detail" style="text-align:left;margin-top:8px;">
        Confirmation: <strong>24548</strong> · Ref: JAMBO KENYA<br>
        Single Room · 1 traveller<br>
        Tour: $8,425<br>
        Paid: $750 · Balance: <strong>$7,675</strong><br>
        <span style="color:#f0d98a">Due Apr 20, 2026</span>
      </div>
    </div>
    <div class="family-card">
      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">✈</div>
      <div class="f-name">Travel Consultant</div>
      <div class="f-detail" style="text-align:left;margin-top:8px;">
        <strong>Vickie Cheema</strong><br>
        Explore World Journeys Inc.<br>
        #1500 – 1100 Melville St, Vancouver BC<br>
        Toll: 1-800-515-1948<br>
        info@explore-world.com
      </div>
    </div>
  </div>
</section>
"""

# ── FLIGHTS SECTION ──
kenya_flights = """
<section class="dark-section" id="flights" style="background:#111827;">
  <h2>✈ Flights</h2>
  <p class="section-sub">
    <span class="badge-confirmed" style="margin-right:8px;">✓ CONFIRMED</span>
    Lufthansa Business Class · Bookings: Ken+Mabel (B6EIYE) · Suzie (BQO2WC)
  </p>
  <div class="flights-grid">
    <div class="flight-card">
      <div class="airline">Lufthansa LH 6527 · Operated by Air Canada AC838 <span class="badge-confirmed">✓ CONFIRMED</span></div>
      <div class="flight-route"><span class="airport">YVR</span><span class="arrow">✈</span><span class="airport">FRA</span></div>
      <div class="flight-meta">Fri Jul 17 · 13:15 → 08:05+1<br>9h 50m · Non-stop · Boeing 787-9</div>
      <div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">
        Ken: <strong>3G</strong> · Mabel: <strong>3D</strong> · Suzie: <strong>3K</strong>
      </div>
    </div>
    <div class="flight-card">
      <div class="airline">Lufthansa LH 590 <span class="badge-confirmed">✓ CONFIRMED</span></div>
      <div class="flight-route"><span class="airport">FRA</span><span class="arrow">✈</span><span class="airport">NBO</span></div>
      <div class="flight-meta">Sat Jul 18 · 11:25 → 20:35<br>8h 10m · Non-stop · Boeing 787-9 · Meal included</div>
      <div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">
        Ken: <strong>7G</strong> · Mabel: <strong>7D</strong> · Suzie: <strong>7K</strong>
      </div>
    </div>
    <div class="flight-card">
      <div class="airline">Lufthansa LH 591 · Operated by United UA 8730 <span class="badge-confirmed">✓ CONFIRMED</span></div>
      <div class="flight-route"><span class="airport">NBO</span><span class="arrow">✈</span><span class="airport">FRA</span></div>
      <div class="flight-meta">Sun Jul 26 · 22:50 → Mon Jul 27 · 06:10<br>8h 20m · Non-stop · Boeing 787-9 · Meal included</div>
      <div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">
        Ken: <strong>7G</strong> · Mabel: <strong>7D</strong> · Suzie: <strong>6K</strong>
      </div>
    </div>
    <div class="flight-card">
      <div class="airline">Lufthansa LH 454 · Operated by United UA 8829 <span class="badge-confirmed">✓ CONFIRMED</span></div>
      <div class="flight-route"><span class="airport">FRA</span><span class="arrow">✈</span><span class="airport">SFO</span></div>
      <div class="flight-meta">Mon Jul 27 · 10:25 → 12:40<br>11h 15m · Non-stop · Boeing 747-8 · Meal included</div>
      <div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">
        Ken: <strong>8K</strong> · Mabel: <strong>8H</strong> · Suzie: <strong>8G</strong>
      </div>
    </div>
  </div>
  <p class="flight-note" style="text-align:center;margin-top:20px;">
    ⚠ Reconfirm all flights at least 72 hours prior to departure · e-Ticket: LH/ETKT 220-6026062155/2156
  </p>
</section>
"""

# ── CITY SECTIONS ──
def day_card(city_class, city_name_cn, day_num, day_date, night_label, title, transit_items, activities):
    acts_html = ''
    for icon, name, tip in activities:
        tip_html = f' <span class="act-tip">{tip}</span>' if tip else ''
        acts_html += f'<li><span class="act-icon">{icon}</span><span class="act-main"><span class="act-name">{name}</span>{tip_html}</span></li>'
    transit_html = ''
    for t in transit_items:
        cls = t.get('cls', '')
        icon = t['icon']
        text = t['text']
        transit_html += f'<div class="transit-bar {cls}">{icon} {text}</div>'
    return f"""
  <div class="day-card {city_class}">
    <div class="day-label">
      <span class="dn">{day_num}</span>
      <span class="dm">{day_date}</span>
      <span class="dw">{night_label}</span>
    </div>
    <div class="day-body">
      <h3>{title}</h3>
      {transit_html}
      <ul class="act-list">{acts_html}</ul>
    </div>
  </div>"""

def city_banner(city_class, eyebrow, h2, dates_tag, hotel_items):
    chips = ''.join(f'<span class="hotel-chip">🏨 {h}</span>' for h in hotel_items)
    return f"""
  <div class="city-banner {city_class}">
    <div class="city-banner-inner">
      <div class="eyebrow">{eyebrow}</div>
      <h2>{h2}</h2>
      <div class="dates-tag">{dates_tag}</div>
      <div class="hotel-chips">{chips}</div>
    </div>
  </div>"""

nairobi_section = """
<section class="city-section" id="nairobi">
  """ + city_banner('ks', 'City 01 · Nairobi, Kenya · Nights 1 & 8', 'Nairobi', 'Jul 17 (arrival) &amp; Jul 24 (departure) · 2 nights', [
    'Mövenpick Hotel &amp; Residences Nairobi · B&amp;B',
    'Hilton Garden Inn Nairobi Airport · B&amp;B + Lunch · Free shuttle'
  ]) + """
  <div class="days-container">
    <div class="day-card ks">
      <div class="day-label">
        <span class="dn">D0</span>
        <span class="dm">Jul 17</span>
        <span class="dw">Evening</span>
      </div>
      <div class="day-body">
        <h3>Day 0 — Depart Vancouver</h3>
        <div class="transit-bar flight">✈ LH 6527 · YVR 13:15 → FRA 08:05+1 · then LH 590 FRA 11:25 → NBO 20:35</div>
        <ul class="act-list">
          <li><span class="act-icon">✈</span><span class="act-main"><span class="act-name">LH 6527 YVR → FRA</span> · 13:15 dep · Business Class · Ken 3G · Mabel 3D · Suzie 3K</span></li>
          <li><span class="act-icon">🛬</span><span class="act-main"><span class="act-name">Arrive Nairobi Jomo Kenyatta Intl</span> · 20:35 local time</span></li>
          <li><span class="act-icon">🏨</span><span class="act-main"><span class="act-name">Check in: Mövenpick Hotel &amp; Residences Nairobi</span></span></li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

samburu_section = """
<section class="city-section" id="samburu">
  """ + city_banner('sr', 'City 02 · Samburu National Reserve · Nights 2–3', 'Samburu', 'Jul 18–20 · 2 nights', [
    'Samburu Simba Lodge · Full Board'
  ]) + """
  <div class="days-container">
    """ + day_card('sr', 'Samburu', 'D1–2', 'Jul 18–19', '2 nights', 'Samburu — Rare &amp; Beautiful',
      [{'cls':'transfer','icon':'🚙','text':'Transfer from Nairobi to Samburu National Reserve (~5–6 hrs by road)'}],
      [
        ('🦁','Game drives in 4×4 Land Cruiser with pop-up roof','Early morning &amp; late afternoon'),
        ('🦒','Reticulated Giraffe — unique to northern Kenya','Grevy\'s Zebra and Somali Ostrich also nearby'),
        ('🐘','Elephant herds &amp; predator sightings','Lion and leopard commonly spotted'),
        ('🌅','Sundowners on the plains','A classic safari tradition'),
        ('🏨','Samburu Simba Lodge · Full Board · 2 nights',''),
      ]) + """
  </div>
</section>
"""

olpejeta_section = """
<section class="city-section" id="olpejeta">
  """ + city_banner('op', 'City 03 · Ol Pejeta Conservancy · Night 4', 'Ol Pejeta', 'Jul 20 · 1 night', [
    'Sweetwaters Serena Camp · Full Board'
  ]) + """
  <div class="days-container">
    """ + day_card('op', 'Ol Pejeta', 'D3', 'Jul 20', '1 night', 'Ol Pejeta — Last Chance for the Northern White Rhino',
      [{'cls':'transfer','icon':'🚙','text':'Drive from Samburu to Ol Pejeta Conservancy (~2–3 hrs)'}],
      [
        ('🦏','Northern White Rhino — the last two on earth','Sweetwaters is the only place to see them'),
        ('🦍','Chimpanzee Sanctuary','Only chimpanzees in Kenya — rescued individuals'),
        ('🦁','Big Five game drives','Lion, elephant, buffalo, rhino'),
        ('🏨','Sweetwaters Serena Camp · Full Board · 1 night',''),
      ]) + """
  </div>
</section>
"""

nakuru_section = """
<section class="city-section" id="nakuru">
  """ + city_banner('nk', 'City 04 · Lake Nakuru · Night 5', 'Lake Nakuru', 'Jul 21 · 1 night', [
    'Lake Nakuru Sopa Lodge · Full Board'
  ]) + """
  <div class="days-container">
    """ + day_card('nk', 'Nakuru', 'D4', 'Jul 21', '1 night', 'Lake Nakuru — Flamingos &amp; White Rhino',
      [{'cls':'transfer','icon':'🚙','text':'Drive from Ol Pejeta to Lake Nakuru (~2–3 hrs)'}],
      [
        ('🦩','Thousands of flamingos on the soda lake','The lake turns pink — a spectacular sight'),
        ('🦏','White Rhino sanctuary in the national park','Both black &amp; white rhinos present'),
        ('🦁','Leopard frequently spotted in the acacia woods','Lion and buffalo also common'),
        ('🏨','Lake Nakuru Sopa Lodge · Full Board · 1 night',''),
      ]) + """
  </div>
</section>
"""

mara_section = """
<section class="city-section" id="mara">
  """ + city_banner('mm', 'City 05 · Masai Mara National Reserve · Nights 6–7', 'Masai Mara', 'Jul 22–24 · 2 nights', [
    'Mara Serena Safari Lodge · Full Board'
  ]) + """
  <div class="days-container">
    """ + day_card('mm', 'Mara', 'D5', 'Jul 22', 'Morning', 'Masai Mara — The Greatest Wildlife Spectacle on Earth',
      [{'cls':'transfer','icon':'🚙','text':'Drive from Nakuru to Masai Mara via Naivasha (~5–6 hrs)'}],
      [
        ('🦁','Full-day game drives','Big cats — lion, leopard, cheetah on the golden plains'),
        ('🐊','Mara River crocodiles','Wildebeest crossing (July–December migration)'),
        ('🦁','Morning &amp; late afternoon game drives','Best light for wildlife photography'),
        ('🌅','Sunset over the Mara plains','One of Africa\'s most iconic landscapes'),
        ('🏨','Mara Serena Safari Lodge · Full Board · 2 nights',''),
      ]) + """
    """ + day_card('mm', 'Mara', 'D6', 'Jul 23', 'Evening', 'Masai Mara — Second Full Day',
      [{'cls':'transfer','icon':'🌅','text':'Departure morning — return to Nairobi'}],
      [
        ('🦁','Early morning game drive','Predators most active at dawn'),
        ('🦘','Wildebeest &amp; zebra on the move','July marks the start of the migration'),
        ('🏨','Check out Mara Serena · Drive back to Nairobi (~5 hrs)',''),
        ('🏨','Hilton Garden Inn Nairobi Airport · B&amp;B + Lunch · Free shuttle',''),
      ]) + """
  </div>
</section>
"""

departure_section = """
<section class="city-section" id="departure">
  <div class="city-banner ks">
    <div class="city-banner-inner">
      <div class="eyebrow">City 06 · Departure · Day 8</div>
      <h2>Fly Home</h2>
      <div class="dates-tag">Sun Jul 26 · Evening departure · Arrive Mon Jul 27 San Francisco</div>
    </div>
  </div>
  <div class="days-container">
    <div class="day-card ks">
      <div class="day-label">
        <span class="dn">D7</span>
        <span class="dm">Jul 26</span>
        <span class="dw">Day</span>
      </div>
      <div class="day-body">
        <h3>Day 7 — Last Day in Nairobi</h3>
        <div class="transit-bar transfer">🚗 Free morning in Nairobi — rest or last-minute shopping</div>
        <ul class="act-list">
          <li><span class="act-icon">✈</span><span class="act-main"><span class="act-name">LH 591 · NBO 22:50 → FRA 06:10+1</span> Boeing 787-9 · Ken 7G · Mabel 7D · Suzie 6K</span></li>
          <li><span class="act-icon">✈</span><span class="act-main"><span class="act-name">LH 454 · FRA 10:25 → SFO 12:40</span> Boeing 747-8 · Ken 8K · Mabel 8H · Suzie 8G</span></li>
          <li><span class="act-icon">🏠</span><span class="act-main"><span class="act-name">Arrive San Francisco</span> Mon Jul 27 · 12:40pm · Welcome home</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

# ── TIPS SECTION ──
kenya_tips = """
<section class="tips-section">
  <h2>📋 Safari Travel Tips</h2>
  <div class="tips-grid">
    <div class="tip-card">
      <div class="tip-icon">🌡️</div>
      <div class="tip-title">July Weather in Kenya</div>
      <div class="tip-body">Nairobi: 10–22°C · Samburu &amp; Mara: 14–26°C. Cool mornings &amp; evenings, warm midday. Bring layers — early game drives can be cold!</div>
    </div>
    <div class="tip-card">
      <div class="tip-icon">🎒</div>
      <div class="tip-title">Packing for Safari</div>
      <div class="tip-body">Neutral-coloured clothing (no bright colours for game drives) · Sun hat · Sunglasses · binoculars · High-SPF sunscreen · Long-sleeve shirts</div>
    </div>
    <div class="tip-card">
      <div class="tip-icon">💊</div>
      <div class="tip-title">Health</div>
      <div class="tip-body">Malaria prophylaxis recommended — visit a travel clinic. Yellow fever vaccine required if arriving from an endemic area. DEET mosquito repellent essential.</div>
    </div>
    <div class="tip-card">
      <div class="tip-icon">💳</div>
      <div class="tip-title">Money in Kenya</div>
      <div class="tip-body">Kenyan Shilling (KES) — withdraw at ATM or exchange at airport. US Dollars widely accepted at lodges. Tip your safari guide USD 10–20/day.</div>
    </div>
    <div class="tip-card">
      <div class="tip-icon">📱</div>
      <div class="tip-title">Communications</div>
      <div class="tip-body">Safari camps have limited WiFi — a perfect excuse to disconnect! Purchase a Safaricom or Airtel SIM at Nairobi airport for data.</div>
    </div>
    <div class="tip-card">
      <div class="tip-icon">⚕️</div>
      <div class="tip-title">Safari Safety</div>
      <div class="tip-body">Always follow your guide's instructions. Stay inside the Land Cruiser unless your guide says otherwise. Animals are wild — never approach on foot.</div>
    </div>
    <div class="tip-card">
      <div class="tip-icon">🦁</div>
      <div class="tip-title">Photography</div>
      <div class="tip-body">Best light: early morning &amp; golden hour. Bring a zoom lens (200mm+). Extra memory cards &amp; batteries — the Mara is incredibly photogenic.</div>
    </div>
    <div class="tip-card">
      <div class="tip-icon">🕕</div>
      <div class="tip-title">Safari Rhythm</div>
      <div class="tip-body">Early wake-up (~5–6 AM), breakfast, game drive until midday, rest during the heat, late afternoon drive until dark. This is how the professionals do it.</div>
    </div>
  </div>
</section>
"""

# ── NAV ──
kenya_nav = """
<nav class="sticky-nav">
  <a href="#family">Family</a>
  <a href="#flights">Flights</a>
  <a href="#nairobi">Nairobi</a>
  <a href="#samburu">Samburu</a>
  <a href="#olpejeta">Ol Pejeta</a>
  <a href="#nakuru">Nakuru</a>
  <a href="#mara">Masai Mara</a>
  <a href="#departure">Departure</a>
  <a href="#tips">Tips</a>
</nav>
"""

# ── FOOTER ──
kenya_footer = """
<footer>
  <div class="gold">✦ Tam Family Kenya Safari 2026 ✦</div>
  <div style="margin-top:8px;">Ken · Mabel · Suzie Suet Ying</div>
  <div style="margin-top:4px;">Prepared with 💚 by Jade &nbsp;·&nbsp; July 17–27, 2026</div>
  <div style="margin-top:10px;font-size:.75rem;">Tour: Explore World Journeys Inc. · Vickie Cheema · Vancouver BC · 1-800-515-1948</div>
</footer>
"""

# ── ASSEMBLE ──
kenya_html = (
    '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
    '<meta charset="UTF-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    '<title>Tam Family Kenya Safari 2026</title>\n'
    '<style>\n' + kenya_css + '\n</style>\n'
    '</head>\n<body>\n\n'
    + kenya_hero + '\n'
    + kenya_nav + '\n'
    + kenya_family + '\n'
    + kenya_flights + '\n'
    + nairobi_section + '\n'
    + samburu_section + '\n'
    + olpejeta_section + '\n'
    + nakuru_section + '\n'
    + mara_section + '\n'
    + departure_section + '\n'
    + kenya_tips + '\n'
    + kenya_footer + '\n'
    '</body>\n</html>'
)

with open('/workspace/kenya-safari-2026/index.html', 'w') as f:
    f.write(kenya_html)

print(f"Done! Written {len(kenya_html):,} characters, {kenya_html.count(chr(10))} lines")
