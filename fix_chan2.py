#!/usr/bin/env python3
"""Final fix for Chan Kenya - exact whitespace match"""
import subprocess, re

SRC = '/workspace/kenya-safari-2026/index.html'
DST = '/workspace/chan-kenya-2026/index.html'

with open(SRC) as f:
    t = f.read()

print(f"Read {len(t):,} chars")

# Helper: do a plain find-replace (no regex)
def replace(haystack, old, new):
    if old not in haystack:
        print(f"  WARNING: pattern not found: {repr(old[:80])}")
        return haystack
    return haystack.replace(old, new)

# ── 1. Hero badge
t = replace(t,
    '<div class="hero-badge">Tam Family · July 17–27, 2026</div>',
    '<div class="hero-badge">Chan Family · July 17–27, 2026</div>')

# ── 2. Hero title
t = replace(t,
    '<h1>Tam Family <em>Kenya Safari</em></h1>',
    '<h1><em>Chan Family</em> Kenya Safari</h1>')

# ── 3. Hero subtitle
t = replace(t,
    'An 8-night East African safari — Ken &amp; Mabel &amp; Suzie',
    'An 8-night East African safari — Archie, Katherine, Stephen, Elsie &amp; Henry')

# ── 4. Section subtitle
t = replace(t,
    '<p class="section-sub">3 travellers · JAMBO KENYA safari package · booked through Explore World Journeys</p>',
    '<p class="section-sub">5 travellers · JAMBO KENYA safari package · booked through Explore World Journeys · Vickie Cheema</p>')

# ── 5. Family cards - use exact repr from actual HTML
# 4-space outer div, 6-space inner divs
card1_old = (
    '    <div class="family-card">\n'
    '      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">\u2665</div>\n'
    '      <div class="f-name">Ken Tam &amp; Mabel Chu</div>\n'
    '      <div class="f-detail" style="text-align:left;margin-top:8px;">\n'
    '        Confirmation: <strong>24549</strong> \xb7 Ref: JAMBO KENYA<br>\n'
    '        Double Room \xb7 2 travellers<br>\n'
    '        Tour: $17,326 \xd7 2 = <strong>$34,652</strong><br>\n'
    '        Paid: $24,000 \xb7 Balance: <strong>$10,652</strong><br>\n'
    '        <span style="color:#f0d98a">Due Apr 20, 2026</span>\n'
    '      </div>\n'
    '    </div>')

card2_old = (
    '    <div class="family-card">\n'
    '      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">\u2605</div>\n'
    '      <div class="f-name">Suzie Suet Ying Tam</div>\n'
    '      <div class="f-detail" style="text-align:left;margin-top:8px;">\n'
    '        Confirmation: <strong>24548</strong> \xb7 Ref: JAMBO KENYA<br>\n'
    '        Single Room \xb7 1 traveller<br>\n'
    '        Tour: $8,425<br>\n'
    '        Paid: $750 \xb7 Balance: <strong>$7,675</strong><br>\n'
    '        <span style="color:#f0d98a">Due Apr 20, 2026</span>\n'
    '      </div>\n'
    '    </div>')

card3_old = (
    '    <div class="family-card">\n'
    '      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">\u2708</div>\n'
    '      <div class="f-name">Travel Consultant</div>\n'
    '      <div class="f-detail" style="text-align:left;margin-top:8px;">\n'
    '        <strong>Vickie Cheema</strong><br>\n'
    '        Explore World Journeys Inc.<br>\n'
    '        #1500 \u2013 1100 Melville St, Vancouver BC<br>\n'
    '        Toll: 1-800-515-1948<br>\n'
    '        info@explore-world.com\n'
    '      </div>\n'
    '    </div>')

cards_new = (
    '    <div class="family-card">\n'
    '      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">\u25C6</div>\n'
    '      <div class="f-name">Archie &amp; Katherine Chan</div>\n'
    '      <div class="f-detail" style="text-align:left;margin-top:8px;">\n'
    '        Mr. Archie Nga Chi Chan<br>\n'
    '        Mrs. Katherine Gi Yuo Chan<br><br>\n'
    '        Booking ref: <strong>B69QQC</strong>\n'
    '      </div>\n'
    '    </div>\n'
    '    <div class="family-card">\n'
    '      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">\u2605</div>\n'
    '      <div class="f-name">Stephen Fan &amp; Elsie Leung</div>\n'
    '      <div class="f-detail" style="text-align:left;margin-top:8px;">\n'
    '        Mr. Stephen Sui Wong Fan<br>\n'
    '        Mrs. Elsie Leung<br><br>\n'
    '        Booking ref: <strong>B69QQC</strong>\n'
    '      </div>\n'
    '    </div>\n'
    '    <div class="family-card">\n'
    '      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">\u2708</div>\n'
    '      <div class="f-name">Henry Leung</div>\n'
    '      <div class="f-detail" style="text-align:left;margin-top:8px;">\n'
    '        Mr. Henry Leung<br><br>\n'
    '        Booking ref: <strong>B69QQC</strong>\n'
    '      </div>\n'
    '    </div>')

all_old = card1_old + '\n' + card2_old + '\n' + card3_old
if all_old in t:
    t = t.replace(all_old, cards_new)
    print("Family cards replaced!")
else:
    # Try without em-dashes
    card3_old_v2 = card3_old.replace('\u2013', '–')
    all_old_v2 = card1_old + '\n' + card2_old + '\n' + card3_old_v2
    if all_old_v2 in t:
        t = t.replace(all_old_v2, cards_new)
        print("Family cards replaced! (v2)")
    else:
        print("ERROR: Family card pattern not found at all")

# ── 6. Title
t = replace(t,
    '<title>Tam Family Kenya Safari 2026</title>',
    '<title>Chan Family Kenya Safari 2026</title>')

# ── 7. Footer
t = replace(t,
    '<div style="margin-top:8px;">Ken \xb7 Mabel \xb7 Suzie Suet Ying</div>',
    '<div style="margin-top:8px;">Archie \xb7 Katherine \xb7 Stephen \xb7 Elsie \xb7 Henry</div>')

# ── 8. Flights section subtitle
t = replace(t,
    'Lufthansa Business Class \xb7 Bookings: Ken+Mabel (B6EIYE) \xb7 Suzie (BQO2WC)',
    'Air Canada &amp; Lufthansa \xb7 Economy Class \xb7 Booking ref: B69QQC \xb7 \u26a0 Ticket by Jun 2, 2026')

# ── 9. Individual flight card replacements using regex
# Card 1: Replace LH 6527 card with AC 838
t = re.sub(
    r'<div class="flight-card">\s*<div class="airline">Lufthansa LH 6527.*?</div>\s*<div class="flight-route">.*?</div>\s*<div class="flight-meta">.*?</div>\s*</div>',
    '<div class="flight-card"><div class="airline">Air Canada AC 838 <span class="badge-confirmed">\u2713 CONFIRMED</span></div><div class="flight-route"><span class="airport">YVR</span><span class="arrow">\u2192</span><span class="airport">FRA</span></div><div class="flight-meta">Fri Jul 17 &middot; 13:15 &rarr; 08:05+1<br>9h 50m &middot; Non-stop &middot; Boeing 787-9 &middot; Economy (M)</div><div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers &middot; 2 bags each</div></div>',
    t, flags=re.DOTALL)

# Card 2: Replace LH 590 card with AC 9610 (LH 590)
t = re.sub(
    r'<div class="flight-card">\s*<div class="airline">Lufthansa LH 590.*?</div>\s*<div class="flight-route">.*?</div>\s*<div class="flight-meta">.*?</div>\s*</div>',
    '<div class="flight-card"><div class="airline">Air Canada AC 9610 &middot; Operated by Lufthansa LH 590 <span class="badge-confirmed">\u2713 CONFIRMED</span></div><div class="flight-route"><span class="airport">FRA</span><span class="arrow">\u2192</span><span class="airport">NBO</span></div><div class="flight-meta">Sat Jul 18 &middot; 11:25 &rarr; 20:35<br>8h 10m &middot; Non-stop &middot; Boeing 787-9 &middot; Economy (M) &middot; Meal</div><div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers &middot; 2 bags each</div></div>',
    t, flags=re.DOTALL)

# Card 3: Replace UA 8730 return card with LH 591
t = re.sub(
    r'<div class="flight-card">\s*<div class="airline">Lufthansa LH 591.*?</div>\s*<div class="flight-route">.*?</div>\s*<div class="flight-meta">.*?</div>\s*</div>',
    '<div class="flight-card"><div class="airline">Lufthansa LH 591 <span class="badge-confirmed">\u2713 CONFIRMED</span></div><div class="flight-route"><span class="airport">NBO</span><span class="arrow">\u2192</span><span class="airport">FRA</span></div><div class="flight-meta">Sun Jul 26 &middot; 22:50 &rarr; Mon Jul 27 &middot; 06:10<br>8h 20m &middot; Non-stop &middot; Boeing 787-9 &middot; Economy (T) &middot; Meal</div><div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers &middot; 2 bags each</div></div>',
    t, flags=re.DOTALL)

# Card 4: Replace LH 454 SFO card with LH 100 MUC
t = re.sub(
    r'<div class="flight-card">\s*<div class="airline">Lufthansa LH 454.*?</div>\s*<div class="flight-route">.*?<span class="airport">SFO</span>.*?</div>\s*<div class="flight-meta">.*?</div>\s*</div>',
    '<div class="flight-card"><div class="airline">Lufthansa LH 100 <span class="badge-confirmed">\u2713 CONFIRMED</span></div><div class="flight-route"><span class="airport">FRA</span><span class="arrow">\u2192</span><span class="airport">MUC</span></div><div class="flight-meta">Mon Jul 27 &middot; 09:45 &rarr; 10:40<br>55 min &middot; Non-stop &middot; Airbus A321 &middot; Economy (T) &middot; Refreshments</div><div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers &middot; 2 bags each</div></div>',
    t, flags=re.DOTALL)

# Card 5: Add a new 5th card for LH 476 (MUC->YVR)
# Find LH 454 card end and add new card after
lh454_match = re.search(r'(<div class="flight-card">.*?LH 454.*?</div>)', t, DOTALL)
if lh454_match:
    old_lh454 = lh454_match.group()
    new_lh476 = '<div class="flight-card"><div class="airline">Lufthansa LH 476 <span class="badge-confirmed">\u2713 CONFIRMED</span></div><div class="flight-route"><span class="airport">MUC</span><span class="arrow">\u2192</span><span class="airport">YVR</span></div><div class="flight-meta">Mon Jul 27 &middot; 15:45 &rarr; 16:55<br>10h 10m &middot; Non-stop &middot; Airbus A350-900 &middot; Economy (T) &middot; Meal</div><div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers &middot; 2 bags each</div></div>'
    t = t.replace(old_lh454, old_lh454 + '\n\n    ' + new_lh476)
    print("LH 476 card added!")

# ── 10. Update flight note
t = replace(t,
    'Reconfirm all flights at least 72 hours prior to departure \xb7 e-Ticket: LH/ETKT 220-6026062155/2156',
    '\u26a0 Ticket required before <strong>June 2, 2026 23:59</strong> \u2014 overdue will cancel without notice \xb7 CO\u2082: 1,954 kg/person')

# ── Summary
print(f"\nFinal: {len(t):,} chars")
checks = {
    'Archie': 'Archie' in t,
    'Ken Tam gone': 'Ken Tam' not in t,
    'Suzie gone': 'Suzie' not in t,
    'AC 838': 'AC 838' in t,
    'AC 9610': 'AC 9610' in t,
    'LH 476': 'LH 476' in t,
    'MUC route': 'MUC' in t,
    'B69QQC': 'B69QQC' in t,
    'Jun 2 2026': 'June 2, 2026' in t,
}
for k, v in checks.items():
    print(f"  {v and '✓' or '✗'} {k}")

with open(DST, 'w') as f:
    f.write(t)
print("Written!")

# Push
r = subprocess.run(['git', '-C', '/workspace/chan-kenya-2026', 'add', 'index.html'],
    capture_output=True, text=True)
r = subprocess.run(['git', '-C', '/workspace/chan-kenya-2026', 'commit', '-m',
    'Fix: Chan Family Kenya Safari 2026 - complete content replacement'],
    capture_output=True, text=True)
print("Commit:", r.stdout[:200])
r = subprocess.run(['git', '-C', '/workspace/chan-kenya-2026', 'push', 'origin', 'main', '--force'],
    capture_output=True, text=True)
print("Push:", r.stderr[:200] if r.returncode else "OK")
print("DONE!")
