#!/usr/bin/env python3
"""Add 4th passenger card to Chan Kenya page"""
with open('/workspace/chan-kenya-2026/index.html') as f:
    t = f.read()

# Fix grid to handle 4 cards
t = t.replace(
    '.family-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;max-width:900px;margin:0 auto}',
    '.family-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;max-width:900px;margin:0 auto}'
)

# Find Stephen's closing tag and add 4th card after it
marker = '    </div>\n  </div>'
idx = t.rfind('>Stephen Sui Wong Fan<')
end_idx = t.find(marker, idx)
new_card = (
    '\n    <div class="family-card">\n'
    '      <div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">&#9992;</div>\n'
    '      <div class="f-name">Grace &amp; Irene</div>\n'
    '      <div class="f-detail" style="text-align:left;margin-top:8px;">\n'
    '        Ms. Grace Gigi Fan Ep Dupont<br>\n'
    '        Ms. Irene Yuen Mei Chan<br><br>\n'
    '        <span style="font-size:.72rem;opacity:.7;">(Couple)</span><br>\n'
    '        Bookings: <strong>YP87L5</strong> &amp; <strong>B6J24T</strong>\n'
    '      </div>\n'
    '    </div>'
)
t = t[:end_idx] + new_card + t[end_idx:]
print(f"Result: {len(t):,} chars")
print("Grace in result:", "Grace" in t)
print("Irene in result:", "Irene" in t)

with open('/workspace/chan-kenya-2026/index.html', 'w') as f:
    f.write(t)
print("Written!")
