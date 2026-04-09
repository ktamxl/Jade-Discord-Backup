// PDF printer compatibility conversion using pdf-lib
// pdf-lib can load and re-save PDFs in a compatible format

import { execSync } from 'child_process';
import { existsSync, statSync, readFileSync, writeFileSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

// First, install pdf-lib if not present
const nodeModulesPath = '/workspace/node_pdf_modules';

console.log('Installing pdf-lib...');
try {
  execSync(`mkdir -p ${nodeModulesPath} && cd ${nodeModulesPath} && npm init -y --quiet 2>/dev/null && npm install pdf-lib --save --quiet 2>&1`, {
    stdio: 'pipe',
    timeout: 120000
  });
  console.log('pdf-lib installed successfully');
} catch (e) {
  console.error('npm install failed:', e.message);
  process.exit(1);
}

// Now load and use pdf-lib
const { PDFDocument } = await import(`${nodeModulesPath}/node_modules/pdf-lib/cjs/index.js`);

const files = [
  { src: '/workspace/eulogy_ngongchor.pdf', dst: '/workspace/eulogy_print.pdf' },
  { src: '/workspace/fengshui_final_report.pdf', dst: '/workspace/fengshui_print.pdf' },
];

for (const { src, dst } of files) {
  if (!existsSync(src)) {
    console.log(`SOURCE NOT FOUND: ${src}`);
    continue;
  }
  const srcSize = statSync(src).size;
  console.log(`Processing: ${src} (${srcSize.toLocaleString()} bytes)`);
  
  try {
    const srcBytes = readFileSync(src);
    const pdfDoc = await PDFDocument.load(srcBytes, { ignoreEncryption: true });
    
    // Save as PDF 1.4 compatible - pdf-lib outputs compatible PDFs
    const pdfBytes = await pdfDoc.save({
      useObjectStreams: false, // Better compatibility with older printers
    });
    
    writeFileSync(dst, pdfBytes);
    const dstSize = statSync(dst).size;
    console.log(`  -> ${dst}: ${dstSize.toLocaleString()} bytes  ✓`);
  } catch (err) {
    console.error(`  ERROR processing ${src}:`, err.message);
  }
}

console.log('Done!');
