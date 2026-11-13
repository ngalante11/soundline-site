// Soundline — print the handout booklet.
//
//   node tools/booklet.js  → print/Soundline-Booklet.pdf          (eight half-letter pages, in order: give this to a print shop,
//                                                                   ask for "saddle-stitched booklet, 5.5 x 8.5")
//                            print/Soundline-Booklet-Imposed.pdf  (two letter sheets, two pages a side: print at home,
//                                                                   double-sided, landscape, flip on the SHORT edge, fold)
//
// Source: print/booklet.html. Dates come from build/builds.js. Refuses to print a page that overflows.

const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const path = require('path');
const ROOT = path.join(__dirname, '..');

(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 528, height: 816 } });
  await page.goto('file://' + path.join(ROOT, 'print/booklet.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(400);
  const over = await page.evaluate(() => [...document.querySelectorAll('.page')]
    .map((el, i) => ({ page: i + 1, px: el.scrollHeight - el.clientHeight })).filter(x => x.px > 2));
  if (over.length) { console.error('Nothing written: ' + over.map(o => `page ${o.page} over by ${o.px}px`).join(', ')); process.exit(1); }
  const seq = path.join(ROOT, 'print/Soundline-Booklet.pdf');
  await page.pdf({ path: seq, width: '5.5in', height: '8.5in', printBackground: true, margin: { top: '0', right: '0', bottom: '0', left: '0' } });
  console.log('printed print/Soundline-Booklet.pdf');
  await browser.close();
  console.log(execFileSync('python3', [path.join(ROOT, 'tools/impose.py'), seq, path.join(ROOT, 'print/Soundline-Booklet-Imposed.pdf')]).toString().trim());
})();
