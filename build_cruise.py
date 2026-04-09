#!/usr/bin/env python3
"""Build Tam Family Majestic Princess British Isles Cruise webpage"""
import subprocess, os, shutil

PROJECT = '/workspace/tam-cruise-2027'
SRC_IMGS = '/workspace/imgs'

# Copy project skeleton
if os.path.exists(PROJECT):
    shutil.rmtree(PROJECT)
os.makedirs(PROJECT)
os.makedirs(f'{PROJECT}/imgs')

# Copy any available images
available = {}
for f in os.listdir(SRC_IMGS):
    p = f'{SRC_IMGS}/{f}'
    if os.path.isfile(p) and not f.startswith('.'):
        shutil.copy2(p, f'{PROJECT}/imgs/{f}')
        available[f.lower()] = f

print("Available images:", list(available.keys()))

# Create SVG route map
route_svg = '''<svg viewBox="0 0 900 620" xmlns="http://www.w3.org/2000/svg" style="background:#0d2540;border-radius:16px;">
  <title>British Isles Cruise Route Map - Majestic Princess 2027</title>
  <defs>
    <filter id="glow"><feGaussianBlur stdDeviation="3" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <linearGradient id="oceanGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#0d2540"/><stop offset="100%" stop-color="#1a4060"/></linearGradient>
    <linearGradient id="landGrad"><stop offset="0%" stop-color="#2d6a30"/><stop offset="100%" stop-color="#1a4020"/></linearGradient>
    <linearGradient id="lineGrad" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#f0d98a"/><stop offset="50%" stop-color="#ffffff"/><stop offset="100%" stop-color="#f0d98a"/></linearGradient>
  </defs>
  <!-- Ocean -->
  <rect width="900" height="620" fill="url(#oceanGrad)" rx="16"/>
  <!-- Land masses - simplified British Isles -->
  <!-- Ireland -->
  <path d="M 380 200 Q 420 180 480 190 Q 530 200 550 240 Q 570 280 560 330 Q 550 380 520 400 Q 480 420 450 400 Q 420 380 400 340 Q 380 300 370 260 Q 360 220 380 200Z" fill="#2d5a20" opacity="0.9"/>
  <!-- Great Britain -->
  <path d="M 160 140 Q 200 100 280 100 Q 360 100 400 120 Q 440 140 460 180 Q 480 220 500 280 Q 520 340 520 400 Q 520 460 500 520 Q 480 560 440 570 Q 400 580 340 560 Q 280 540 240 500 Q 200 460 180 400 Q 160 340 150 280 Q 140 220 160 140Z" fill="#2d5a20" opacity="0.9"/>
  <!-- Scotland north -->
  <path d="M 240 80 Q 260 60 290 70 Q 320 80 310 110 Q 290 130 260 120 Q 230 110 220 90Z" fill="#1e4020"/>
  <!-- France/Belgium hint (for Le Havre) -->
  <path d="M 480 440 Q 510 420 550 430 Q 580 440 570 470 Q 550 490 520 480 Q 490 470 480 440Z" fill="#2d5a20" opacity="0.6"/>
  
  <!-- Cruise route line -->
  <path d="M 500 440 C 480 420 460 410 450 400 C 440 390 430 380 440 360 C 450 340 470 330 490 320 C 510 310 530 300 545 290 C 560 280 565 260 555 250 C 545 240 525 235 510 230 C 495 225 480 230 470 250 C 460 270 455 300 440 330 C 425 360 410 380 390 400 C 370 420 350 435 330 445 C 310 455 290 460 270 455 C 250 450 240 435 245 415 C 250 395 265 380 280 365 C 295 350 310 340 320 325 C 330 310 335 295 345 285 C 355 275 370 268 390 265 C 410 262 430 265 445 260 C 460 255 468 245 475 230" 
    stroke="url(#lineGrad)" stroke-width="3.5" fill="none" stroke-dasharray="12,6" filter="url(#glow)" opacity="0.9"/>
  
  <!-- Animated dots along route -->
  <circle r="5" fill="#f0d98a" filter="url(#glow)">
    <animateMotion dur="6s" repeatCount="indefinite" path="M 500 440 C 480 420 460 410 450 400 C 440 390 430 380 440 360 C 450 340 470 330 490 320 C 510 310 530 300 545 290 C 560 280 565 260 555 250 C 545 240 525 235 510 230 C 495 225 480 230 470 250 C 460 270 455 300 440 330 C 425 360 410 380 390 400 C 370 420 350 435 330 445 C 310 455 290 460 270 455 C 250 450 240 435 245 415 C 250 395 265 380 280 365 C 295 350 310 340 320 325 C 330 310 335 295 345 285 C 355 275 370 268 390 265 C 410 262 430 265 445 260 C 460 255 468 245 475 230"/>
  </circle>

  <!-- Port markers with numbers -->
  <!-- 1 Southampton -->
  <circle cx="500" cy="440" r="14" fill="#f0d98a" filter="url(#glow)"/>
  <text x="500" y="445" text-anchor="middle" fill="#1a1a2e" font-size="10" font-weight="bold">1</text>
  <text x="500" y="470" text-anchor="middle" fill="#f0d98a" font-size="10" font-weight="bold">Southampton</text>
  <text x="500" y="484" text-anchor="middle" fill="#aaa" font-size="9">May 1</text>

  <!-- 2 Falmouth -->
  <circle cx="445" cy="400" r="12" fill="#f0d98a"/>
  <text x="445" y="405" text-anchor="middle" fill="#1a1a2e" font-size="9" font-weight="bold">2</text>
  <text x="430" y="424" text-anchor="middle" fill="#f0d98a" font-size="9" font-weight="bold">Falmouth</text>
  <text x="430" y="437" text-anchor="middle" fill="#aaa" font-size="8">May 2</text>

  <!-- 3 Cork -->
  <circle cx="490" cy="320" r="12" fill="#f0d98a"/>
  <text x="490" y="325" text-anchor="middle" fill="#1a1a2e" font-size="9" font-weight="bold">3</text>
  <text x="508" y="315" text-anchor="start" fill="#f0d98a" font-size="9" font-weight="bold">Cork (Cobh)</text>
  <text x="508" y="328" text-anchor="start" fill="#aaa" font-size="8">May 3</text>

  <!-- 4 Dublin -->
  <circle cx="555" cy="250" r="12" fill="#f0d98a"/>
  <text x="555" y="255" text-anchor="middle" fill="#1a1a2e" font-size="9" font-weight="bold">4</text>
  <text x="570" y="245" text-anchor="start" fill="#f0d98a" font-size="9" font-weight="bold">Dublin</text>
  <text x="570" y="258" text-anchor="start" fill="#aaa" font-size="8">May 4</text>

  <!-- 5 Liverpool -->
  <circle cx="390" cy="400" r="12" fill="#f0d98a"/>
  <text x="390" y="405" text-anchor="middle" fill="#1a1a2e" font-size="9" font-weight="bold">5</text>
  <text x="370" y="424" text-anchor="middle" fill="#f0d98a" font-size="9" font-weight="bold">Liverpool</text>
  <text x="370" y="437" text-anchor="middle" fill="#aaa" font-size="8">May 5</text>

  <!-- 6 Belfast -->
  <circle cx="465" cy="265" r="12" fill="#f0d98a"/>
  <text x="465" y="270" text-anchor="middle" fill="#1a1a2e" font-size="9" font-weight="bold">6</text>
  <text x="448" y="255" text-anchor="end" fill="#f0d98a" font-size="9" font-weight="bold">Belfast</text>
  <text x="448" y="268" text-anchor="end" fill="#aaa" font-size="8">May 6</text>

  <!-- 7 Glasgow -->
  <circle cx="320" cy="325" r="12" fill="#f0d98a"/>
  <text x="320" y="330" text-anchor="middle" fill="#1a1a2e" font-size="9" font-weight="bold">7</text>
  <text x="300" y="310" text-anchor="middle" fill="#f0d98a" font-size="9" font-weight="bold">Glasgow</text>
  <text x="300" y="323" text-anchor="middle" fill="#aaa" font-size="8">May 7</text>

  <!-- 8 Invergordon (at sea day then Invergordon) -->
  <circle cx="280" cy="250" r="12" fill="#f0d98a"/>
  <text x="280" y="255" text-anchor="middle" fill="#1a1a2e" font-size="9" font-weight="bold">8</text>
  <text x="262" y="236" text-anchor="end" fill="#f0d98a" font-size="9" font-weight="bold">Invergordon</text>
  <text x="262" y="249" text-anchor="end" fill="#aaa" font-size="8">May 9</text>

  <!-- 9 Edinburgh -->
  <circle cx="370" cy="265" r="12" fill="#f0d98a"/>
  <text x="370" y="270" text-anchor="middle" fill="#1a1a2e" font-size="9" font-weight="bold">9</text>
  <text x="390" y="255" text-anchor="start" fill="#f0d98a" font-size="9" font-weight="bold">Edinburgh</text>
  <text x="390" y="268" text-anchor="start" fill="#aaa" font-size="8">May 10</text>

  <!-- 10 Le Havre -->
  <circle cx="475" cy="465" r="12" fill="#f0d98a"/>
  <text x="475" y="470" text-anchor="middle" fill="#1a1a2e" font-size="9" font-weight="bold">10</text>
  <text x="475" y="492" text-anchor="middle" fill="#f0d98a" font-size="9" font-weight="bold">Le Havre (Paris)</text>
  <text x="475" y="505" text-anchor="middle" fill="#aaa" font-size="8">May 12</text>

  <!-- Back to Southampton -->
  <circle cx="500" cy="440" r="8" fill="#f0d98a" opacity="0.5" stroke="#fff" stroke-width="1.5"/>
  <text x="510" y="444" text-anchor="start" fill="#aaa" font-size="8">→ Southampton</text>
  <text x="510" y="456" text-anchor="start" fill="#aaa" font-size="8">May 13</text>

  <!-- At Sea markers -->
  <circle cx="472" cy="418" r="4" fill="#ffffff" opacity="0.6"/>
  <circle cx="420" cy="372" r="4" fill="#ffffff" opacity="0.6"/>
  <circle cx="295" cy="370" r="4" fill="#ffffff" opacity="0.6"/>
  <circle cx="340" cy="285" r="4" fill="#ffffff" opacity="0.6"/>

  <!-- Title -->
  <text x="450" y="38" text-anchor="middle" fill="#f0d98a" font-size="16" font-weight="bold" letter-spacing="3">BRITISH ISLES CRUISE ROUTE</text>
  <text x="450" y="58" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-size="11" letter-spacing="1">Majestic Princess · May 1–13, 2027 · Southampton to Southampton</text>
  
  <!-- Legend -->
  <rect x="20" y="540" width="200" height="65" rx="8" fill="rgba(0,0,0,0.4)"/>
  <line x1="32" y1="558" x2="70" y2="558" stroke="#f0d98a" stroke-width="2.5" stroke-dasharray="5,3"/>
  <text x="78" y="562" fill="rgba(255,255,255,0.7)" font-size="9">= Cruise route</text>
  <circle cx="42" cy="578" r="5" fill="#f0d98a"/>
  <text x="78" y="582" fill="rgba(255,255,255,0.7)" font-size="9">= Port of call</text>
  <circle cx="42" cy="594" r="3" fill="#fff" opacity="0.6"/>
  <text x="78" y="598" fill="rgba(255,255,255,0.7)" font-size="9">= At sea</text>

  <!-- Ship icon -->
  <text x="880" y="590" text-anchor="end" fill="rgba(255,255,255,0.3)" font-size="10">🛳 Majestic Princess</text>
</svg>'''

with open(f'{PROJECT}/imgs/route-map.svg', 'w') as f:
    f.write(route_svg)

print("Route map created!")
print(f"Project dir: {PROJECT}")
print(f"Images: {os.listdir(PROJECT+'/imgs')}")
