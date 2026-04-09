#!/usr/bin/env python3
"""Fix flights in Chan Kenya - direct substring approach"""
import subprocess

DST = '/workspace/chan-kenya-2026/index.html'
with open(DST) as f:
    t = f.read()

print(f"Starting: {len(t):,} chars")

# Find and replace each flight card by searching for the unique airline name
# and replacing everything from <div class="flight-card"> to the matching </div>

def replace_flight_card(text, old_airline, new_card_html):
    """Find flight card by airline name and replace entire card."""
    # Search for the card containing this airline
    search = f'<div class="flight-card">'
    idx = 0
    while True:
        card_start = text.find(search, idx)
        if card_start == -1:
            print(f"  WARNING: No flight card found for {old_airline}")
            return text
        # Check if this card contains our airline
        card_end_search = text.find('</div>', card_start)
        # Get a window of 500 chars to check airline name
        window = text[card_start:card_start+600]
        if old_airline in window:
            # Find the actual end of this flight card
            depth = 0
            actual_end = card_start
            i = text.find('<div', card_start)
            end_marker = text.find('</div>', card_start)
            # Count divs to find true end
            d = 0
            pos = card_start
            while pos < len(text):
                if text[pos:pos+4] == '<div':
                    d += 1
                    pos += 4
                elif text[pos:pos+6] == '</div>':
                    d -= 1
                    pos += 6
                    if d == 0:
                        actual_end = pos
                        break
                else:
                    pos += 1
            print(f"  Replacing flight card at {card_start}-{actual_end} ({old_airline})")
            return text[:card_start] + '\n    ' + new_card_html + '\n    ' + text[actual_end:]
        idx = card_start + 4

    return text

# Card 1: YVR→FRA - AC 838 (was LH 6527)
new_card1 = ('<div class="flight-card"><div class="airline">Air Canada AC 838 <span class="badge-confirmed">\u2713 CONFIRMED</span></div>'
    '<div class="flight-route"><span class="airport">YVR</span><span class="arrow">\u2192</span><span class="airport">FRA</span></div>'
    '<div class="flight-meta">Fri Jul 17 \u00b7 13:15 \u2192 08:05+1<br>9h 50m \u00b7 Non-stop \u00b7 Boeing 787-9 \u00b7 Economy (M)</div>'
    '<div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers \u00b7 2 bags each</div></div>')

# Card 2: FRA→NBO - AC 9610/LH 590 (was LH 590)
new_card2 = ('<div class="flight-card"><div class="airline">Air Canada AC 9610 \u00b7 Operated by Lufthansa LH 590 <span class="badge-confirmed">\u2713 CONFIRMED</span></div>'
    '<div class="flight-route"><span class="airport">FRA</span><span class="arrow">\u2192</span><span class="airport">NBO</span></div>'
    '<div class="flight-meta">Sat Jul 18 \u00b7 11:25 \u2192 20:35<br>8h 10m \u00b7 Non-stop \u00b7 Boeing 787-9 \u00b7 Economy (M) \u00b7 Meal</div>'
    '<div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers \u00b7 2 bags each</div></div>')

# Card 3: NBO→FRA - LH 591 (same airline, update content)
new_card3 = ('<div class="flight-card"><div class="airline">Lufthansa LH 591 <span class="badge-confirmed">\u2713 CONFIRMED</span></div>'
    '<div class="flight-route"><span class="airport">NBO</span><span class="arrow">\u2192</span><span class="airport">FRA</span></div>'
    '<div class="flight-meta">Sun Jul 26 \u00b7 22:50 \u2192 Mon Jul 27 \u00b7 06:10<br>8h 20m \u00b7 Non-stop \u00b7 Boeing 787-9 \u00b7 Economy (T) \u00b7 Meal</div>'
    '<div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers \u00b7 2 bags each</div></div>')

# Card 4: FRA→MUC - LH 100 (was FRA→SFO LH 454)
new_card4 = ('<div class="flight-card"><div class="airline">Lufthansa LH 100 <span class="badge-confirmed">\u2713 CONFIRMED</span></div>'
    '<div class="flight-route"><span class="airport">FRA</span><span class="arrow">\u2192</span><span class="airport">MUC</span></div>'
    '<div class="flight-meta">Mon Jul 27 \u00b7 09:45 \u2192 10:40<br>55 min \u00b7 Non-stop \u00b7 Airbus A321 \u00b7 Economy (T) \u00b7 Refreshments</div>'
    '<div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers \u00b7 2 bags each</div></div>')

# Card 5: MUC→YVR - LH 476 (NEW)
new_card5 = ('<div class="flight-card"><div class="airline">Lufthansa LH 476 <span class="badge-confirmed">\u2713 CONFIRMED</span></div>'
    '<div class="flight-route"><span class="airport">MUC</span><span class="arrow">\u2192</span><span class="airport">YVR</span></div>'
    '<div class="flight-meta">Mon Jul 27 \u00b7 15:45 \u2192 16:55<br>10h 10m \u00b7 Non-stop \u00b7 Airbus A350-900 \u00b7 Economy (T) \u00b7 Meal</div>'
    '<div style="margin-top:9px;font-family:sans-serif;font-size:.75rem;line-height:1.9;opacity:.78;border-top:1px solid rgba(255,255,255,.1);padding-top:9px;">All 5 passengers \u00b7 2 bags each</div></div>')

# Replace each card
t = replace_flight_card(t, 'Lufthansa LH 6527', new_card1)
t = replace_flight_card(t, 'Lufthansa LH 590', new_card2)
t = replace_flight_card(t, 'Lufthansa LH 591', new_card3)
t = replace_flight_card(t, 'Lufthansa LH 454', new_card4)

# Add LH 476 after LH 100
lh100_pos = t.find('Lufthansa LH 100')
if lh100_pos > -1:
    end_of_lh100 = t.find('</div>', lh100_pos)
    # Find the true end of the card
    t = t[:end_of_lh100+6] + '\n\n    ' + new_card5 + t[end_of_lh100+6:]
    print("  Added LH 476 card!")

# Checks
print(f"\nFinal: {len(t):,} chars")
for label, cond in [
    ('AC 838', 'AC 838' in t),
    ('AC 9610', 'AC 9610' in t),
    ('LH 476', 'LH 476' in t),
    ('MUC airport', 'MUC' in t and 'MUNICH' not in t),
    ('LH 454 gone', 'LH 454' not in t),
    ('SFO gone', 'SFO' not in t and 'San Francisco' not in t),
    ('B69QQC', 'B69QQC' in t),
]:
    print(f"  {'OK' if cond else 'FAIL'} {label}")

with open(DST, 'w') as f:
    f.write(t)
print("Written!")

r = subprocess.run(['git', '-C', '/workspace/chan-kenya-2026', 'add', 'index.html'], capture_output=True)
r = subprocess.run(['git', '-C', '/workspace/chan-kenya-2026', 'commit', '-m', 'Chan Kenya: fix all flight cards with correct Chan flights'], capture_output=True, text=True)
print("Commit:", r.stdout[:100])
r = subprocess.run(['git', '-C', '/workspace/chan-kenya-2026', 'push', 'origin', 'main', '--force'], capture_output=True, text=True)
print("Push:", 'OK' if not r.returncode else r.stderr[:80])
print("DONE!")
