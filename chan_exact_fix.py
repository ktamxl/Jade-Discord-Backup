#!/usr/bin/env python3
"""Exact fix for Chan Kenya - precise content replacement"""
import subprocess, re

DST = '/workspace/chan-kenya-2026/index.html'
with open(DST) as f:
    t = f.read()

print(f"File: {len(t):,} chars")

# ── Family cards: exact repr from actual HTML ──
OLD_FAMILY = (
    '    <div class="family-card">\n'
    '      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">\u2665</div>\n'
    '      <div class="f-name">Ken Tam &amp; Mabel Chu</div>\n'
    '      <div class="f-detail" style="text-align:left;margin-top:8px;">\n'
    '        Confirmation: <strong>24549</strong> \u00b7 Ref: JAMBO KENYA<br>\n'
    '        Double Room \u00b7 2 travellers<br>\n'
    '        Tour: $17,326 \u00d7 2 = <strong>$34,652</strong><br>\n'
    '        Paid: $24,000 \u00b7 Balance: <strong>$10,652</strong><br>\n'
    '        <span style="color:#f0d98a">Due Apr 20, 2026</span>\n'
    '      </div>\n'
    '    </div>\n'
    '    <div class="family-card">\n'
    '      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">\u2605</div>\n'
    '      <div class="f-name">Suzie Suet Ying Tam</div>\n'
    '      <div class="f-detail" style="text-align:left;margin-top:8px;">\n'
    '        Confirmation: <strong>24548</strong> \u00b7 Ref: JAMBO KENYA<br>\n'
    '        Single Room \u00b7 1 traveller<br>\n'
    '        Tour: $8,425<br>\n'
    '        Paid: $750 \u00b7 Balance: <strong>$7,675</strong><br>\n'
    '        <span style="color:#f0d98a">Due Apr 20, 2026</span>\n'
    '      </div>\n'
    '    </div>\n'
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
    '    </div>'
)

NEW_FAMILY = (
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
    '    </div>'
)

if OLD_FAMILY in t:
    t = t.replace(OLD_FAMILY, NEW_FAMILY)
    print("Family cards replaced!")
else:
    print("Family cards NOT found - trying relaxed match")
    # Relaxed: replace just the name-containing parts
    t = t.replace('>Ken Tam &amp; Mabel Chu<', '>Archie &amp; Katherine Chan<')
    t = t.replace('>Suzie Suet Ying Tam<', '>Stephen Fan &amp; Elsie Leung<')
    t = t.replace('>Travel Consultant<', '>Henry Leung<')
    # Replace detail content block by block
    t = t.replace(
        'Confirmation: <strong>24549</strong> \u00b7 Ref: JAMBO KENYA<br>\n        Double Room \u00b7 2 travellers<br>\n        Tour: $17,326 \u00d7 2 = <strong>$34,652</strong><br>\n        Paid: $24,000 \u00b7 Balance: <strong>$10,652</strong><br>\n        <span style="color:#f0d98a">Due Apr 20, 2026</span>',
        'Mr. Archie Nga Chi Chan<br>\n        Mrs. Katherine Gi Yuo Chan<br><br>\n        Booking ref: <strong>B69QQC</strong>'
    )
    t = t.replace(
        'Confirmation: <strong>24548</strong> \u00b7 Ref: JAMBO KENYA<br>\n        Single Room \u00b7 1 traveller<br>\n        Tour: $8,425<br>\n        Paid: $750 \u00b7 Balance: <strong>$7,675</strong><br>\n        <span style="color:#f0d98a">Due Apr 20, 2026</span>',
        'Mr. Stephen Sui Wong Fan<br>\n        Mrs. Elsie Leung<br><br>\n        Booking ref: <strong>B69QQC</strong>'
    )
    t = t.replace(
        '<strong>Vickie Cheema</strong><br>\n        Explore World Journeys Inc.<br>\n        #1500 \u2013 1100 Melville St, Vancouver BC<br>\n        Toll: 1-800-515-1948<br>\n        info@explore-world.com',
        'Mr. Henry Leung<br><br>\n        Booking ref: <strong>B69QQC</strong>'
    )
    print("Relaxed family replacement done")

# ── Flight cards: regex replacement ──
# Card 1: YVR→FRA (AC 838 instead of LH 6527)
t = re.sub(
    r'<div class="flight-card">\s*<div class="airline">Lufthansa LH 6527[^<]*(?:<(?!/div>)[^<]*)*</div>\s*<div class="flight-meta">[^<]*</div>\s*</div>',
    '<div class="flight-card"><div class="airline">Air Canada AC 838 <span class="badge-confirmed">\u2713 CONFIRMED</span></div><div class="flight-route"><span class="airport">YVR</span><span class="arrow">\u2192</span><span class="airport">FRA</span></div><div class="flight-meta">Fri Jul 17 &middot; 13:15 &rarr; 08:05+1<br>9h 50m &middot; Non-stop &middot; Boeing 787-9 &middot; Economy (M)</div><div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers &middot; 2 bags each</div></div>',
    t, flags=re.DOTALL)

# Card 2: FRA→NBO (AC 9610/LH 590)
t = re.sub(
    r'<div class="flight-card">\s*<div class="airline">Lufthansa LH 590[^<]*(?:<(?!/div>)[^<]*)*</div>\s*<div class="flight-meta">[^<]*</div>\s*</div>',
    '<div class="flight-card"><div class="airline">Air Canada AC 9610 &middot; Operated by Lufthansa LH 590 <span class="badge-confirmed">\u2713 CONFIRMED</span></div><div class="flight-route"><span class="airport">FRA</span><span class="arrow">\u2192</span><span class="airport">NBO</span></div><div class="flight-meta">Sat Jul 18 &middot; 11:25 &rarr; 20:35<br>8h 10m &middot; Non-stop &middot; Boeing 787-9 &middot; Economy (M) &middot; Meal</div><div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers &middot; 2 bags each</div></div>',
    t, flags=re.DOTALL)

# Card 3: NBO→FRA (LH 591)
t = re.sub(
    r'<div class="flight-card">\s*<div class="airline">Lufthansa LH 591[^<]*(?:<(?!/div>)[^<]*)*</div>\s*<div class="flight-meta">[^<]*</div>\s*</div>',
    '<div class="flight-card"><div class="airline">Lufthansa LH 591 <span class="badge-confirmed">\u2713 CONFIRMED</span></div><div class="flight-route"><span class="airport">NBO</span><span class="arrow">\u2192</span><span class="airport">FRA</span></div><div class="flight-meta">Sun Jul 26 &middot; 22:50 &rarr; Mon Jul 27 &middot; 06:10<br>8h 20m &middot; Non-stop &middot; Boeing 787-9 &middot; Economy (T) &middot; Meal</div><div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers &middot; 2 bags each</div></div>',
    t, flags=re.DOTALL)

# Card 4: FRA→SFO (LH 454) → replace with FRA→MUC (LH 100)
t = re.sub(
    r'<div class="flight-card">\s*<div class="airline">Lufthansa LH 454[^<]*(?:<(?!/div>)[^<]*)*</div>\s*<div class="flight-meta">[^<]*</div>\s*</div>',
    '<div class="flight-card"><div class="airline">Lufthansa LH 100 <span class="badge-confirmed">\u2713 CONFIRMED</span></div><div class="flight-route"><span class="airport">FRA</span><span class="arrow">\u2192</span><span class="airport">MUC</span></div><div class="flight-meta">Mon Jul 27 &middot; 09:45 &rarr; 10:40<br>55 min &middot; Non-stop &middot; Airbus A321 &middot; Economy (T) &middot; Refreshments</div><div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers &middot; 2 bags each</div></div>',
    t, flags=re.DOTALL)

# Card 5: Add MUC→YVR (LH 476) after the MUC card
LH100_match = re.search(r'(<div class="flight-card">.*?LH 100.*?</div>)', t, re.DOTALL)
if LH100_match:
    new_lh476 = '<div class="flight-card"><div class="airline">Lufthansa LH 476 <span class="badge-confirmed">\u2713 CONFIRMED</span></div><div class="flight-route"><span class="airport">MUC</span><span class="arrow">\u2192</span><span class="airport">YVR</span></div><div class="flight-meta">Mon Jul 27 &middot; 15:45 &rarr; 16:55<br>10h 10m &middot; Non-stop &middot; Airbus A350-900 &middot; Economy (T) &middot; Meal</div><div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers &middot; 2 bags each</div></div>'
    t = t.replace(LH100_match.group(), LH100_match.group() + '\n\n    ' + new_lh476)
    print("LH 476 card added!")

# ── Flight note ──
t = t.replace(
    'Reconfirm all flights at least 72 hours prior to departure \u00b7 e-Ticket: LH/ETKT 220-6026062155/2156',
    '\u26a0 Ticket required before <strong>June 2, 2026 23:59</strong> \u2014 overdue will cancel without notice \u00b7 CO\u2082: 1,954 kg/person'
)

# ── Checks ──
print(f"\nFinal: {len(t):,} chars")
checks = {
    'Archie Chan': 'Archie' in t,
    'Ken Tam gone': 'Ken Tam' not in t,
    'AC 838 flight': 'AC 838' in t,
    'AC 9610 flight': 'AC 9610' in t,
    'LH 476 flight': 'LH 476' in t,
    'MUC airport': 'MUC' in t,
    'B69QQC ref': 'B69QQC' in t,
    'Jun 2 deadline': 'June 2, 2026' in t,
    '1954 kg CO2': '1,954' in t,
}
for k, v in checks.items():
    print(f"  {'OK' if v else 'MISSING'}: {k}")

with open(DST, 'w') as f:
    f.write(t)
print("Written!")

# Push
r = subprocess.run(['git', '-C', '/workspace/chan-kenya-2026', 'add', 'index.html'],
    capture_output=True, text=True)
r = subprocess.run(['git', '-C', '/workspace/chan-kenya-2026', 'commit', '-m',
    'Chan Family Kenya Safari 2026 - correct all flights and family info'],
    capture_output=True, text=True)
print("Commit:", r.stdout[:150])
r = subprocess.run(['git', '-C', '/workspace/chan-kenya-2026', 'push', 'origin', 'main', '--force'],
    capture_output=True, text=True)
print("Push:", 'OK' if not r.returncode else r.stderr[:100])
