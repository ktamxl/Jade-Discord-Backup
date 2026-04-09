const sharp = require('sharp');
const path = require('path');
const fs = require('fs');

async function createOverlay() {
  // Load original image to get dimensions
  const inputPath = '/workspace/user_input_files/image.png';
  const meta = await sharp(inputPath).metadata();
  const W = meta.width;   // 3294
  const H = meta.height;  // 1834
  
  console.log(`Image size: ${W} x ${H}`);
  
  // Building footprint boundaries (from analysis)
  // Left = Family Room far wall, Right = Garage/Porch front wall
  // These are the BUILDING walls only (not yard/driveway)
  const bLeft = 86;
  const bRight = 2176;
  const bTop = 186;
  const bBottom = 1636;
  
  const bW = bRight - bLeft;   // building width in pixels
  const bH = bBottom - bTop;   // building height in pixels
  
  // Each palace cell size
  const cellW = bW / 3;
  const cellH = bH / 3;
  
  // Palace data - layout based on: 
  // LEFT = South (坐方/back), RIGHT = North (向首/front)
  // TOP = East, BOTTOM = West
  // Grid layout [row][col]:
  // [0][0]=SE巽  [0][1]=E震   [0][2]=NE艮
  // [1][0]=S離   [1][1]=Center [1][2]=N坎
  // [2][0]=SW坤  [2][1]=W兌   [2][2]=NW乾
  
  const palaces = [
    // row 0 (top)
    [
      { name: '巽 SE', stars: '山4 向3 運7', rating: '中', color: '#4FC3F7', alpha: 0.45, extra: '' },
      { name: '震 E', stars: '山5 向2 運6', rating: '⚠️', color: '#EF5350', alpha: 0.45, extra: '五二交加' },
      { name: '艮 NE', stars: '山9 向7 運2', rating: '⭐⭐', color: '#66BB6A', alpha: 0.45, extra: '' },
    ],
    // row 1 (middle)
    [
      { name: '離 S 坐方', stars: '山8 向8 運3', rating: '⭐⭐⭐⭐', color: '#43A047', alpha: 0.5, extra: '雙星到坐' },
      { name: '中宮', stars: '山3 向4 運8', rating: '', color: '#90A4AE', alpha: 0.35, extra: '' },
      { name: '坎 N 向首', stars: '山7 向9 運4', rating: '⭐⭐⭐⭐⭐', color: '#2E7D32', alpha: 0.55, extra: '九運大財位' },
    ],
    // row 2 (bottom)
    [
      { name: '坤 SW', stars: '山6 向1 運5', rating: '⭐', color: '#FFF176', alpha: 0.45, extra: '' },
      { name: '兌 W', stars: '山1 向6 運1', rating: '⭐⭐⭐', color: '#AED581', alpha: 0.45, extra: '財官雙美' },
      { name: '乾 NW', stars: '山2 向5 運9', rating: '⚠️⚠️', color: '#C62828', alpha: 0.5, extra: '最凶' },
    ],
  ];

  // Build SVG overlay
  // SVG covers the entire image
  let svgCells = '';
  
  for (let row = 0; row < 3; row++) {
    for (let col = 0; col < 3; col++) {
      const p = palaces[row][col];
      const x = bLeft + col * cellW;
      const y = bTop + row * cellH;
      
      // Convert hex color to rgba
      const hex = p.color.replace('#','');
      const r = parseInt(hex.substr(0,2),16);
      const g = parseInt(hex.substr(2,2),16);
      const b = parseInt(hex.substr(4,2),16);
      
      // Cell background
      svgCells += `<rect x="${x}" y="${y}" width="${cellW}" height="${cellH}" fill="rgba(${r},${g},${b},${p.alpha})" />`;
      
      // Palace name (large, bold)
      const cx = x + cellW / 2;
      const nameY = y + cellH * 0.22;
      const starsY = y + cellH * 0.45;
      const extraY = y + cellH * 0.65;
      const ratingY = y + cellH * 0.82;
      
      const fontSize1 = Math.round(cellH * 0.15);
      const fontSize2 = Math.round(cellH * 0.12);
      const fontSize3 = Math.round(cellH * 0.10);
      
      svgCells += `<text x="${cx}" y="${nameY}" text-anchor="middle" font-family="Noto Sans CJK TC, WenQuanYi Micro Hei, Arial" font-weight="bold" font-size="${fontSize1}" fill="#1a1a1a" stroke="white" stroke-width="3" paint-order="stroke">${p.name}</text>`;
      svgCells += `<text x="${cx}" y="${starsY}" text-anchor="middle" font-family="Noto Sans CJK TC, WenQuanYi Micro Hei, Arial" font-size="${fontSize2}" fill="#1a1a1a" stroke="white" stroke-width="2" paint-order="stroke">${p.stars}</text>`;
      if (p.extra) {
        svgCells += `<text x="${cx}" y="${extraY}" text-anchor="middle" font-family="Noto Sans CJK TC, WenQuanYi Micro Hei, Arial" font-size="${fontSize3}" fill="#1a1a1a" stroke="white" stroke-width="2" paint-order="stroke">${p.extra}</text>`;
      }
      if (p.rating) {
        svgCells += `<text x="${cx}" y="${ratingY}" text-anchor="middle" font-family="Arial" font-size="${fontSize2}" fill="#FF6F00" stroke="white" stroke-width="2" paint-order="stroke">${p.rating}</text>`;
      }
    }
  }
  
  // Grid lines (bold, dark blue)
  const lineColor = '#0D47A1';
  const lw = 8;
  
  // Outer border
  svgCells += `<rect x="${bLeft}" y="${bTop}" width="${bW}" height="${bH}" fill="none" stroke="${lineColor}" stroke-width="${lw*1.5}" />`;
  
  // Vertical dividers (2 lines)
  for (let i = 1; i <= 2; i++) {
    const lx = Math.round(bLeft + i * cellW);
    svgCells += `<line x1="${lx}" y1="${bTop}" x2="${lx}" y2="${bBottom}" stroke="${lineColor}" stroke-width="${lw}" />`;
  }
  // Horizontal dividers (2 lines)
  for (let i = 1; i <= 2; i++) {
    const ly = Math.round(bTop + i * cellH);
    svgCells += `<line x1="${bLeft}" y1="${ly}" x2="${bRight}" y2="${ly}" stroke="${lineColor}" stroke-width="${lw}" />`;
  }
  
  // Compass rose in top-right area (outside the building)
  const crX = 2600;
  const crY = 250;
  const crR = 100;
  svgCells += `<circle cx="${crX}" cy="${crY}" r="${crR}" fill="rgba(255,255,255,0.85)" stroke="#0D47A1" stroke-width="4" />`;
  svgCells += `<text x="${crX}" y="${crY - crR - 20}" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="80" fill="#0D47A1">N 北</text>`;
  svgCells += `<polygon points="${crX},${crY-crR+15} ${crX-30},${crY+20} ${crX},${crY-10} ${crX+30},${crY+20}" fill="#0D47A1" />`;
  svgCells += `<polygon points="${crX},${crY+crR-15} ${crX-30},${crY-20} ${crX},${crY+10} ${crX+30},${crY-20}" fill="#999" />`;
  svgCells += `<text x="${crX}" y="${crY+crR+60}" text-anchor="middle" font-family="Arial" font-size="55" fill="#0D47A1">向首</text>`;
  
  // Arrow pointing right (toward North = toward Yerba Buena Ave)
  svgCells += `<text x="${W - 150}" y="${H/2}" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="70" fill="#0D47A1">←N</text>`;

  // Legend at bottom
  const legendY = H - 80;
  svgCells += `<rect x="50" y="${legendY - 50}" width="${W - 100}" height="100" fill="rgba(255,255,255,0.85)" rx="10" />`;
  svgCells += `<text x="${W/2}" y="${legendY + 20}" text-anchor="middle" font-family="Noto Sans CJK TC, Arial" font-size="55" fill="#333">`;
  svgCells += `🟢旺位(⭐⭐⭐⭐+)  🟡中吉(⭐⭐⭐)  🔵平(中)  🔴化解(⚠️)  坐方=南/左  向首=北/右`;
  svgCells += `</text>`;
  
  const svg = `<svg width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg">
    ${svgCells}
  </svg>`;
  
  const svgBuffer = Buffer.from(svg);
  
  // Composite SVG over original image
  await sharp(inputPath)
    .composite([{
      input: svgBuffer,
      top: 0,
      left: 0,
    }])
    .png()
    .toFile('/workspace/fengshui_house_overlay_v3.png');
  
  console.log('Done! Saved to /workspace/fengshui_house_overlay_v3.png');
}

createOverlay().catch(console.error);
