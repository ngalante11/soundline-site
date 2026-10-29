// Soundline — print the family packet and the tuition sheet.
//
//   node tools/packet.js            → both
//   node tools/packet.js packet     → just the nine-page packet
//   node tools/packet.js tuition    → just the tuition sheet
//
// Sources live in print/. Every fact in them must match the live site;
// each source names the pages it has to agree with. Refuses to write a
// PDF if a page overflows its sheet, because a silent overflow drops
// content off the bottom where nobody looks.

const { chromium } = require('playwright');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const DOCS = {
  packet:  { src: 'print/packet.html',  out: 'soundline-school-information.pdf' },
  tuition: { src: 'print/tuition.html', out: 'print/Soundline-Tuition-2027-28.pdf' },
};

(async () => {
  const want = process.argv.slice(2);
  const names = want.length ? want : Object.keys(DOCS);
  for (const n of names) if (!DOCS[n]) throw new Error(`no document "${n}" — known: ${Object.keys(DOCS).join(', ')}`);

  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 816, height: 1056 } });
  const problems = [];

  for (const n of names) {
    const { src, out } = DOCS[n];
    await page.goto('file://' + path.join(ROOT, src), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(400);

    // A sheet that overflows loses whatever sat past the fold.
    const over = await page.evaluate(() => {
      const sheets = document.querySelectorAll('.page');
      const list = sheets.length ? [...sheets] : [document.body];
      return list.map((el, i) => ({ sheet: i + 1, px: el.scrollHeight - el.clientHeight }))
                 .filter((x) => x.px > 2);
    });
    if (over.length) {
      problems.push(`${src}: ${over.map((o) => `sheet ${o.sheet} over by ${o.px}px`).join(', ')}`);
      continue;
    }

    await page.pdf({
      path: path.join(ROOT, out),
      format: 'Letter',
      printBackground: true,
      margin: { top: '0', right: '0', bottom: '0', left: '0' },
    });
    console.log('printed', out);
  }

  await browser.close();
  if (problems.length) {
    console.error('\nNothing written for:\n  ' + problems.join('\n  '));
    process.exit(1);
  }
})();
