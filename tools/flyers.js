// Soundline — print the two Saturday-build flyers.
//
//   node tools/flyers.js                 → print/Soundline-Flyer-Kids.pdf and -Parents.pdf (QR tagged "flyer")
//   node tools/flyers.js library dickens → print/flyers/Soundline-Flyer-{Kids,Parents}-<tag>.pdf, one pair per tag
//
// A tag is a wall: the QR code on that copy points at soundlineschool.com/build/?s=<tag>,
// so the Sources tab can say which wall produced which family. Make a new tag's code first
// with `python3 tools/qr.py <tag>`. Refuses to print a sheet that overflows.

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const SHEETS = [
  { src: 'print/flyer-kids.html', name: 'Kids' },
  { src: 'print/flyer-parents.html', name: 'Parents' },
];

(async () => {
  const tags = process.argv.slice(2);
  const jobs = [];
  for (const tag of (tags.length ? tags : ['flyer'])) {
    if (!fs.existsSync(path.join(ROOT, 'print/qr', tag + '.svg'))) throw new Error(`no QR code for "${tag}": run python3 tools/qr.py ${tag}`);
    for (const s of SHEETS) {
      const out = tag === 'flyer' ? `print/Soundline-Flyer-${s.name}.pdf` : `print/flyers/Soundline-Flyer-${s.name}-${tag}.pdf`;
      jobs.push({ src: s.src, tag, out });
    }
  }
  fs.mkdirSync(path.join(ROOT, 'print/flyers'), { recursive: true });

  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 816, height: 1056 } });
  const problems = [];
  for (const j of jobs) {
    await page.goto('file://' + path.join(ROOT, j.src) + '?tag=' + j.tag, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    const over = await page.evaluate(() => document.body.scrollHeight - document.body.clientHeight);
    if (over > 2) { problems.push(`${j.src} (${j.tag}): over by ${over}px`); continue; }
    await page.pdf({ path: path.join(ROOT, j.out), format: 'Letter', printBackground: true, margin: { top: '0', right: '0', bottom: '0', left: '0' } });
    console.log('printed', j.out);
  }
  await browser.close();
  if (problems.length) { console.error('\nNothing written for:\n  ' + problems.join('\n  ')); process.exit(1); }
})();
