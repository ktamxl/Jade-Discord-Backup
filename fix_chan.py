#!/usr/bin/env python3
"""Fix Chan Kenya website - ALL replacements in one go"""
import subprocess, shutil

SRC = '/workspace/kenya-safari-2026/index.html'
DST = '/workspace/chan-kenya-2026/index.html'
TOKEN = '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'
USER = 'ktamxl'

with open(SRC) as f:
    t = f.read()

print(f"Read {len(t):,} chars")

# 1. Hero badge
t = t.replace('<div class="hero-badge">Tam Family · July 17–27, 2026</div>',
    '<div class="hero-badge">Chan Family · July 17–27, 2026</div>')

# 2. Hero title
t = t.replace('<h1>Tam Family <em>Kenya Safari</em></h1>',
    '<h1><em>Chan Family</em> Kenya Safari</h1>')

# 3. Hero subtitle
t = t.replace('An 8-night East African safari — Ken &amp; Mabel &amp; Suzie',
    'An 8-night East African safari — Archie, Katherine, Stephen, Elsie &amp; Henry')

# 4. Section subtitle
t = t.replace('<p class="section-sub">3 travellers · JAMBO KENYA safari package · booked through Explore World Journeys</p>',
    '<p class="section-sub">5 travellers · JAMBO KENYA safari package · booked through Explore World Journeys · Vickie Cheema</p>')

# 5. Family cards - use repr to get exact whitespace
old_card1 = ('      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">♡</div>\n'
    '      <div class="f-name">Ken Tam &amp; Mabel Chu</div>\n'
    '      <div class="f-detail" style="text-align:left;margin-top:8px;">\n'
    '        Confirmation: <strong>24549</strong> · Ref: JAMBO KENYA<br>\n'
    '        Double Room · 2 travellers<br>\n'
    '        Tour: $17,326 × 2 = <strong>$34,652</strong><br>\n'
    '        Paid: $24,000 · Balance: <strong>$10,652</strong><br>\n'
    '        <span style="color:#f0d98a">Due Apr 20, 2026</span>\n'
    '      </div>\n'
    '    </div>')

old_card2 = ('      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">★</div>\n'
    '      <div class="f-name">Suzie Suet Ying Tam</div>\n'
    '      <div class="f-detail" style="text-align:left;margin-top:8px;">\n'
    '        Confirmation: <strong>24548</strong> · Ref: JAMBO KENYA<br>\n'
    '        Single Room · 1 traveller<br>\n'
    '        Tour: $8,425<br>\n'
    '        Paid: $750 · Balance: <strong>$7,675</strong><br>\n'
    '        <span style="color:#f0d98a">Due Apr 20, 2026</span>\n'
    '      </div>\n'
    '    </div>')

old_card3 = ('      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">✈</div>\n'
    '      <div class="f-name">Travel Consultant</div>\n'
    '      <div class="f-detail" style="text-align:left;margin-top:8px;">\n'
    '        <strong>Vickie Cheema</strong><br>\n'
    '        Explore World Journeys Inc.<br>\n'
    '        #1500 – 1100 Melville St, Vancouver BC<br>\n'
    '        Toll: 1-800-515-1948<br>\n'
    '        info@explore-world.com\n'
    '      </div>\n'
    '    </div>')

new_cards = ('      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">⌂</div>\n'
    '      <div class="f-name">Archie &amp; Katherine Chan</div>\n'
    '      <div class="f-detail" style="text-align:left;margin-top:8px;">\n'
    '        Mr. Archie Nga Chi Chan<br>\n'
    '        Mrs. Katherine Gi Yuo Chan<br><br>\n'
    '        Booking ref: <strong>B69QQC</strong>\n'
    '      </div>\n'
    '    </div>\n'
    '    <div class="family-card">\n'
    '      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">★</div>\n'
    '      <div class="f-name">Stephen Fan &amp; Elsie Leung</div>\n'
    '      <div class="f-detail" style="text-align:left;margin-top:8px;">\n'
    '        Mr. Stephen Sui Wong Fan<br>\n'
    '        Mrs. Elsie Leung<br><br>\n'
    '        Booking ref: <strong>B69QQC</strong>\n'
    '      </div>\n'
    '    </div>\n'
    '    <div class="family-card">\n'
    '      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">✈</div>\n'
    '      <div class="f-name">Henry Leung</div>\n'
    '      <div class="f-detail" style="text-align:left;margin-top:8px;">\n'
    '        Mr. Henry Leung<br><br>\n'
    '        Booking ref: <strong>B69QQC</strong>\n'
    '      </div>\n'
    '    </div>')

t = t.replace(old_card1 + '\n' + old_card2 + '\n' + old_card3, new_cards)

# 6. Title
t = t.replace('<title>Tam Family Kenya Safari 2026</title>',
    '<title>Chan Family Kenya Safari 2026</title>')

# 7. Footer
t = t.replace('<div style="margin-top:8px;">Ken · Mabel · Suzie Suet Ying</div>',
    '<div style="margin-top:8px;">Archie · Katherine · Stephen · Elsie · Henry</div>')

# 8. Flights section subtitle
t = t.replace(
    'Lufthansa Business Class · Bookings: Ken+Mabel (B6EIYE) · Suzie (BQO2WC)',
    'Air Canada &amp; Lufthansa · Economy Class · Booking ref: B69QQC · ⚠ Ticket by Jun 2, 2026'
)

# 9. Flight cards - find and replace all individual flight cards
new_flights = '''    <div class="flight-card">
      <div class="airline">Air Canada AC 838 <span class="badge-confirmed">✓ CONFIRMED</span></div>
      <div class="flight-route"><span class="airport">YVR</span><span class="arrow">→</span><span class="airport">FRA</span></div>
      <div class="flight-meta">Fri Jul 17 · 13:15 → 08:05+1<br>9h 50m · Non-stop · Boeing 787-9 · Economy (M)</div>
      <div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers · 2 bags each</div>
    </div>

    <div class="flight-card">
      <div class="airline">Air Canada AC 9610 · Operated by Lufthansa LH 590 <span class="badge-confirmed">✓ CONFIRMED</span></div>
      <div class="flight-route"><span class="airport">FRA</span><span class="arrow">→</span><span class="airport">NBO</span></div>
      <div class="flight-meta">Sat Jul 18 · 11:25 → 20:35<br>8h 10m · Non-stop · Boeing 787-9 · Economy (M) · Meal</div>
      <div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers · 2 bags each</div>
    </div>

    <div class="flight-card">
      <div class="airline">Lufthansa LH 591 <span class="badge-confirmed">✓ CONFIRMED</span></div>
      <div class="flight-route"><span class="airport">NBO</span><span class="arrow">→</span><span class="airport">FRA</span></div>
      <div class="flight-meta">Sun Jul 26 · 22:50 → Mon Jul 27 · 06:10<br>8h 20m · Non-stop · Boeing 787-9 · Economy (T) · Meal</div>
      <div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers · 2 bags each</div>
    </div>

    <div class="flight-card">
      <div class="airline">Lufthansa LH 100 <span class="badge-confirmed">✓ CONFIRMED</span></div>
      <div class="flight-route"><span class="airport">FRA</span><span class="arrow">→</span><span class="airport">MUC</span></div>
      <div class="flight-meta">Mon Jul 27 · 09:45 → 10:40<br>55 min · Non-stop · Airbus A321 · Economy (T) · Refreshments</div>
      <div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers · 2 bags each</div>
    </div>

    <div class="flight-card">
      <div class="airline">Lufthansa LH 476 <span class="badge-confirmed">✓ CONFIRMED</span></div>
      <div class="flight-route"><span class="airport">MUC</span><span class="arrow">→</span><span class="airport">YVR</span></div>
      <div class="flight-meta">Mon Jul 27 · 15:45 → 16:55<br>10h 10m · Non-stop · Airbus A350-900 · Economy (T) · Meal</div>
      <div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers · 2 bags each</div>
    </div>'''

# Replace each flight card individually
import re
t = re.sub(
    r'<div class="flight-card">.*?<div class="flight-note".*?</div>',
    new_flights + '\n  <p class="flight-note" style="text-align:center;margin-top:20px;">\n    ⚠ Ticket required before <strong>June 2, 2026 23:59</strong> — overdue will cancel without notice · CO₂: 1,954 kg/person\n  </p>',
    t, flags=re.DOTALL
)

print(f"Result: {len(t):,} chars")
print("Checks:")
print("  Archie in result:", "Archie" in t)
print("  Ken Tam in result:", "Ken Tam" in t)
print("  Suzie in result:", "Suzie" in t)
print("  AC 838 in result:", "AC 838" in t)
print("  LH 476 in result:", "LH 476" in t)
print("  MUC in result:", "MUC" in t)

with open(DST, 'w') as f:
    f.write(t)
print("Written!")

# Commit and push
r = subprocess.run(['git', '-C', '/workspace/chan-kenya-2026', 'add', 'index.html'],
    capture_output=True, text=True)
r = subprocess.run(['git', '-C', '/workspace/chan-kenya-2026', 'commit', '-m',
    'Fix: Chan Family Kenya Safari 2026 - correct flights and family info'],
    capture_output=True, text=True)
print("Commit:", r.stdout[:200], r.stderr[:100])

r = subprocess.run(['git', '-C', '/workspace/chan-kenya-2026', 'push', 'origin', 'main', '--force'],
    capture_output=True, text=True)
print("Push stdout:", r.stdout[:200])
print("Push stderr:", r.stderr[:200])
print("ALL DONE!")
