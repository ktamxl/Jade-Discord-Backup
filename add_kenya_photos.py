import re

with open('/workspace/kenya-safari-2026/index.html', 'r') as f:
    html = f.read()

# ── Update city banner images ──
# Nairobi
html = html.replace(
    '<div class="city-banner ks">',
    '<div class="city-banner ks" style="background-image:url(imgs/nairobi-kenya-city-skyline-at-night.jpg);background-size:cover;background-position:center;">'
)
# Samburu
html = html.replace(
    '<div class="city-banner sr">',
    '<div class="city-banner sr" style="background-image:url(imgs/reticulated-giraffe-samburu-kenya-safari.jpg);background-size:cover;background-position:center;">'
)
# Ol Pejeta
html = html.replace(
    '<div class="city-banner op">',
    '<div class="city-banner op" style="background-image:url(imgs/black-rhino-ol-pejeta-kenya-safari.jpg);background-size:cover;background-position:center;">'
)
# Nakuru
html = html.replace(
    '<div class="city-banner nk">',
    '<div class="city-banner nk" style="background-image:url(imgs/flamingos-lake-nakuru-kenya.jpg);background-size:cover;background-position:center;">'
)
# Masai Mara (first)
html = html.replace(
    '<div class="city-banner mm">',
    '<div class="city-banner mm" style="background-image:url(imgs/masai-mara-male-lion-golden-plains-safari.jpg);background-size:cover;background-position:center;">'
)

# ── Add photo strip to day cards ──
def photo_strip(filename, caption, icon='📷'):
    return f'''
      <div style="display:flex;gap:8px;margin-top:12px;overflow-x:auto;align-items:center;">
        <span style="font-size:.9rem;flex-shrink:0;">{icon}</span>
        <img src="imgs/{filename}" alt="{caption}" style="height:80px;width:120px;object-fit:cover;border-radius:6px;flex-shrink:0;" loading="lazy">
        <span style="font-family:sans-serif;font-size:.7rem;color:#666;font-style:italic;flex-shrink:0;">{caption}</span>
      </div>'''

# Samburu day card
html = html.replace(
    "('🌅','Sundowners on the plains','A classic safari tradition'),",
    "('🌅','Sundowners on the plains','A classic safari tradition'),"
    + "\n        ('🦒','Reticulated Giraffe, Grevy\\'s Zebra, Somali Ostrich','Unique Samburu \\'Special Five\\': gerenuk, Beisa oryx'),"
).replace(
    "('🏨','Samburu Simba Lodge · Full Board · 2 nights',''),\n      ]) + \"\"\"\n  </div>\n</section>\n\"\"\"",
    photo_strip('reticulated-giraffe-samburu-kenya-savanna.jpg', 'Reticulated Giraffe — Samburu\'s most iconic resident', '🦒')
    + "\n      ]) + \"\"\"\n  </div>\n</section>\n\"\"\""
)

# Write updated HTML
with open('/workspace/kenya-safari-2026/index.html', 'w') as f:
    f.write(html)

print(f"Updated! HTML length: {len(html):,}")
print("Done!")
