const sharp = require('sharp');
const fs = require('fs');

async function createOverlay() {
  const inputPath = '/workspace/user_input_files/image.png';
  const meta = await sharp(inputPath).metadata();
  const W = meta.width;
  const H = meta.height;
  console.log(`Image size: ${W} x ${H}`);

  // Building footprint in 1436x728 image
  // Left = Family Room far wall, Right = Garage/Porch front wall (before driveway)
  const bLeft   = 37;
  const bRight  = 950;
  const bTop    = 74;
  const bBottom = 649;

  const bW = bRight - bLeft;
  const bH = bBottom - bTop;
  const cellW = bW / 3;
  const cellH = bH / 3;

  // Embed CJK font as base64
  const fontData = fs.readFileSync('/workspace/NotoSansCJKtc-Regular.otf');
  const fontB64 = fontData.toString('base64');
  const fontDef = `@font-face { font-family: 'NotoTC'; src: url('data:font/otf;base64,${fontB64}') format('opentype'); }`;

  // Palaces: [row][col] where row=0 is top (East), col=0 is left (South/Back)
  const palaces = [
    [
      { name: '巽 SE', stars: '山4 向3 運7', extra: '',          rating: '中平',         r:79,  g:195, b:247, a:0.42 },
      { name: '震 E',  stars: '山5 向2 運6', extra: '五二交加', rating: '⚠ 注意化解',    r:239, g:83,  b:80,  a:0.42 },
      { name: '艮 NE', stars: '山9 向7 運2', extra: '',          rating: '★★ 吉',        r:102, g:187, b:106, a:0.42 },
    ],
    [
      { name: '離S 坐方', stars: '山8 向8 運3', extra: '雙星到坐', rating: '★★★★ 旺丁', r:46,  g:125, b:50,  a:0.52 },
      { name: '中宮',     stars: '山3 向4 運8', extra: '',          rating: '中',          r:144, g:164, b:174, a:0.30 },
      { name: '坎N 向首', stars: '山7 向9 運4', extra: '九運大財位', rating: '★★★★★ 極旺', r:27,  g:94,  b:32,  a:0.57 },
    ],
    [
      { name: '坤 SW', stars: '山6 向1 運5', extra: '',          rating: '★ 小吉',      r:255, g:241, b:118, a:0.47 },
      { name: '兌 W',  stars: '山1 向6 運1', extra: '財官雙美', rating: '★★★ 吉',      r:174, g:213, b:129, a:0.47 },
      { name: '乾 NW', stars: '山2 向5 運9', extra: '二五交加', rating: '⚠⚠ 最凶',     r:183, g:28,  b:28,  a:0.52 },
    ],
  ];

  let cells = '';

  for (let row = 0; row < 3; row++) {
    for (let col = 0; col < 3; col++) {
      const p = palaces[row][col];
      const x = Math.round(bLeft + col * cellW);
      const y = Math.round(bTop  + row * cellH);
      const w = Math.round(cellW);
      const h = Math.round(cellH);
      const cx = x + w / 2;

      const fs1 = Math.round(h * 0.18);
      const fs2 = Math.round(h * 0.13);
      const fs3 = Math.round(h * 0.12);
      const sw  = 3;
      const tf  = 'NotoTC, serif';

      cells += `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="rgba(${p.r},${p.g},${p.b},${p.a})"/>`;
      cells += `<text x="${cx}" y="${y+h*0.22}" text-anchor="middle" font-family="${tf}" font-size="${fs1}" font-weight="bold" fill="#111" stroke="white" stroke-width="${sw}" paint-order="stroke">${p.name}</text>`;
      cells += `<text x="${cx}" y="${y+h*0.42}" text-anchor="middle" font-family="${tf}" font-size="${fs2}" fill="#1a1a1a" stroke="white" stroke-width="2" paint-order="stroke">${p.stars}</text>`;
      if (p.extra) {
        cells += `<text x="${cx}" y="${y+h*0.60}" text-anchor="middle" font-family="${tf}" font-size="${fs3}" font-style="italic" fill="#333" stroke="white" stroke-width="2" paint-order="stroke">${p.extra}</text>`;
      }
      cells += `<text x="${cx}" y="${y+h*0.82}" text-anchor="middle" font-family="${tf}" font-size="${fs3}" fill="#B71C1C" stroke="white" stroke-width="2" paint-order="stroke">${p.rating}</text>`;
    }
  }

  // Grid lines — bold dark blue
  const lc = '#0D47A1';
  const lw  = 4;
  cells += `<rect x="${bLeft}" y="${bTop}" width="${bW}" height="${bH}" fill="none" stroke="${lc}" stroke-width="${lw*2}"/>`;
  for (let i = 1; i <= 2; i++) {
    const lx = Math.round(bLeft + i * cellW);
    cells += `<line x1="${lx}" y1="${bTop}" x2="${lx}" y2="${bBottom}" stroke="${lc}" stroke-width="${lw}"/>`;
  }
  for (let i = 1; i <= 2; i++) {
    const ly = Math.round(bTop + i * cellH);
    cells += `<line x1="${bLeft}" y1="${ly}" x2="${bRight}" y2="${ly}" stroke="${lc}" stroke-width="${lw}"/>`;
  }

  // Compass rose in front yard area (right side)
  const crX = 1170, crY = 220, crR = 60;
  cells += `<circle cx="${crX}" cy="${crY}" r="${crR}" fill="rgba(255,255,255,0.92)" stroke="${lc}" stroke-width="3"/>`;
  cells += `<polygon points="${crX},${crY-crR+8} ${crX-16},${crY+20} ${crX},${crY} ${crX+16},${crY+20}" fill="${lc}"/>`;
  cells += `<polygon points="${crX},${crY+crR-8} ${crX-16},${crY-20} ${crX},${crY} ${crX+16},${crY-20}" fill="#888"/>`;
  cells += `<text x="${crX}" y="${crY-crR-10}" text-anchor="middle" font-family="NotoTC, serif" font-weight="bold" font-size="34" fill="${lc}">N 北</text>`;
  cells += `<text x="${crX}" y="${crY+crR+26}" text-anchor="middle" font-family="NotoTC, serif" font-size="24" fill="${lc}">向首</text>`;
  // Arrow indicating N = Right
  cells += `<text x="${bRight+10}" y="${Math.round(bTop+bH/2)+14}" font-family="NotoTC, serif" font-size="28" font-weight="bold" fill="${lc}">N&#8594;</text>`;

  // Legend
  const lgy = H - 46;
  cells += `<rect x="6" y="${lgy}" width="${W-12}" height="42" rx="5" fill="rgba(255,255,255,0.88)"/>`;
  cells += `<text x="${W/2}" y="${lgy+28}" text-anchor="middle" font-family="NotoTC, serif" font-size="20" fill="#333">坐方(南)=左/後  向首(北)=右/前  |  ★★★★★極旺  ★★★★旺丁  ★★★吉  ★小吉  ⚠注意  ⚠⚠最凶</text>`;

  const svg = `<svg width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg">
    <defs><style>${fontDef}</style></defs>
    ${cells}
  </svg>`;

  await sharp(inputPath)
    .composite([{ input: Buffer.from(svg), top: 0, left: 0 }])
    .png()
    .toFile('/workspace/fengshui_overlay_final.png');

  console.log('Done!');
}

createOverlay().catch(e => { console.error(e.message); process.exit(1); });
