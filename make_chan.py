#!/usr/bin/env python3
import re, shutil, os, subprocess

# Copy project
src = '/workspace/kenya-safari-2026'
dst = '/workspace/chan-kenya-2026'
if os.path.exists(dst): shutil.rmtree(dst)
shutil.copytree(src, dst)
os.makedirs(f'{dst}/imgs', exist_ok=True)
for img in ['masai-mara-male-lion-golden-plains-safari.jpg','flamingos-lake-nakuru-kenya.jpg',
    'black-rhino-ol-pejeta-kenya-safari.jpg','reticulated-giraffe-samburu-kenya-safari.jpg',
    'nairobi-kenya-city-skyline-at-night.jpg']:
    shutil.copy2(f'{src}/imgs/{img}', f'{dst}/imgs/{img}')

with open(f'{src}/index.html','r') as f:
    t = f.read()

# Change hero title
t = t.replace('Tam Family <em>Kenya Safari</em>','<em>Chan Family</em> Kenya Safari')
t = t.replace('An 8-night East African safari — Ken &amp; Mabel &amp; Suzie','An 8-night East African safari — Archie, Katherine, Stephen, Elsie &amp; Henry')

# Replace family cards
old = '<div class="family-card"><div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">♡</div><div class="f-name">Ken Tam &amp; Mabel Chu</div><div class="f-detail" style="text-align:left;margin-top:8px;">Confirmation: <strong>24549</strong> · Ref: JAMBO KENYA<br>Double Room · 2 travellers<br>Tour: $17,326 × 2 = <strong>$34,652</strong><br>Paid: $24,000 · Balance: <strong>$10,652</strong><br><span style="color:#f0d98a">Due Apr 20, 2026</span></div></div><div class="family-card"><div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">★</div><div class="f-name">Suzie Suet Ying Tam</div><div class="f-detail" style="text-align:left;margin-top:8px;">Confirmation: <strong>24548</strong> · Ref: JAMBO KENYA<br>Single Room · 1 traveller<br>Tour: $8,425<br>Paid: $750 · Balance: <strong>$7,675</strong><br><span style="color:#f0d98a">Due Apr 20, 2026</span></div></div><div class="family-card"><div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">✈</div><div class="f-name">Travel Consultant</div><div class="f-detail" style="text-align:left;margin-top:8px;"><strong>Vickie Cheema</strong><br>Explore World Journeys Inc.<br>#1500 – 1100 Melville St, Vancouver BC<br>Toll: 1-800-515-1948<br>info@explore-world.com</div></div>'
new = '<div class="family-card"><div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">⌂</div><div class="f-name">Archie &amp; Katherine Chan</div><div class="f-detail" style="text-align:left;margin-top:8px;">Mr. Archie Nga Chi Chan<br>Mrs. Katherine Gi Yuo Chan<br><br>Booking ref: <strong>B69QQC</strong></div></div><div class="family-card"><div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">★</div><div class="f-name">Stephen Fan &amp; Elsie Leung</div><div class="f-detail" style="text-align:left;margin-top:8px;">Mr. Stephen Sui Wong Fan<br>Mrs. Elsie Leung<br><br>Booking ref: <strong>B69QQC</strong></div></div><div class="family-card"><div style="font-size:2.2rem;margin-bottom:10px;color:var(--gold);">✈</div><div class="f-name">Henry Leung</div><div class="f-detail" style="text-align:left;margin-top:8px;">Mr. Henry Leung<br><br>Booking ref: <strong>B69QQC</strong></div></div>'
t = t.replace(old, new)
t = t.replace('3 travellers','5 travellers')

# Update hero subtitle in case it still says Suzie
t = t.replace('Ken &amp; Mabel &amp; Suzie','Archie, Katherine, Stephen, Elsie &amp; Henry')

# Footer
t = t.replace('<div style="margin-top:8px;">Ken · Mabel · Suzie Suet Ying</div>',
               '<div style="margin-top:8px;">Archie · Katherine · Stephen · Elsie · Henry</div>')

with open(f'{dst}/index.html','w') as f:
    f.write(t)

# Create GitHub repo
token = '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'
user = 'ktamxl'
r = subprocess.run(['curl','-s','-X','POST',f'https://api.github.com/user/repos',
    '-H',f'Authorization: token {token}',
    '-H','Content-Type: application/json',
    '-d','{"name":"chan-kenya-2026","description":"Chan Family Kenya Safari 2026","private":false}'],
    capture_output=True, text=True)
print("Repo create:", r.stdout[:200])

# Init git
subprocess.run(['rm','-rf',f'{dst}/.git'], capture_output=True)
subprocess.run(['git','init'], cwd=dst, capture_output=True)
subprocess.run(['git','config','-f',f'{dst}/.git/config','user.email','jade@openclaw.ai'], capture_output=True)
subprocess.run(['git','config','-f',f'{dst}/.git/config','user.name','Jade'], capture_output=True)
subprocess.run(['git','-C',dst,'add','index.html','imgs/'], capture_output=True)
r = subprocess.run(['git','-C',dst,'commit','-m','Chan Family Kenya Safari 2026'], capture_output=True, text=True)
print("Commit:", r.stdout[:100])
subprocess.run(['git','-C',dst,'branch','-M','main'], capture_output=True)
r = subprocess.run(['git','-C',dst,'remote','add','origin',
    f'https://{token}:{token}@github.com/{user}/chan-kenya-2026.git'],
    capture_output=True, text=True)
r = subprocess.run(['git','-C',dst,'push','-u','origin','main','--force'],
    capture_output=True, text=True)
print("Push:", r.stdout[:200], r.stderr[:200])

# Enable Pages
r = subprocess.run(['curl','-s','-X','POST',
    f'https://api.github.com/repos/{user}/chan-kenya-2026/pages',
    '-H',f'Authorization: token {token}',
    '-H','Content-Type: application/json',
    '-d','{"build_type":"legacy","source":{"branch":"main","path":"/"}}'],
    capture_output=True, text=True)
print("Pages:", r.stdout[:300])

print("DONE")
print("URL: https://ktamxl.github.io/chan-kenya-2026/")
