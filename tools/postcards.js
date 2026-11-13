// Soundline — print the counter postcard.
//
//   node tools/postcards.js              → print/Soundline-Postcard.pdf (6x4, two pages: front, back; for a print shop)
//                                          print/Soundline-Postcard-2up.pdf (letter, two cards a sheet, duplex, flip on the long edge)
//   node tools/postcards.js orthodontist → the same pair in print/postcards/, QR tagged for that wall
//
// Make a new tag's code first with `python3 tools/qr.py <tag>`.

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const ROOT = path.join(__dirname, '..');

(async () => {
  const tags = process.argv.slice(2);
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 816, height: 1056 } });
  fs.mkdirSync(path.join(ROOT, 'print/postcards'), { recursive: true });
  for (const tag of (tags.length ? tags : ['postcard'])) {
    if (!fs.existsSync(path.join(ROOT, 'print/qr', tag + '.svg'))) throw new Error(`no QR code for "${tag}": run python3 tools/qr.py ${tag}`);
    const dir = tag === 'postcard' ? 'print' : 'print/postcards';
    const suffix = tag === 'postcard' ? '' : '-' + tag;
    const jobs = [
      { q: `?tag=${tag}`, out: `${dir}/Soundline-Postcard${suffix}.pdf`, size: { width: '6in', height: '4in' } },
      { q: `?tag=${tag}&sheet=2up`, out: `${dir}/Soundline-Postcard-2up${suffix}.pdf`, size: { format: 'Letter' } },
    ];
    for (const j of jobs) {
      await page.goto('file://' + path.join(ROOT, 'print/postcard.html') + j.q, { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts.ready);
      await page.waitForTimeout(300);
      const over = await page.evaluate(() => [...document.querySelectorAll('.card')].map(c => c.scrollHeight - c.clientHeight).filter(x => x > 2));
      if (over.length) { console.error(`${j.out}: a card overflows by ${over.join(', ')}px; nothing written`); process.exitCode = 1; continue; }
      await page.pdf(Object.assign({ path: path.join(ROOT, j.out), printBackground: true, margin: { top: '0', right: '0', bottom: '0', left: '0' } }, j.size));
      console.log('printed', j.out);
    }
  }
  await browser.close();
})();
