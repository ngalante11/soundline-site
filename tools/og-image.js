// Soundline — draw the link preview image (og-image.png, 1200 x 630).
//
//   node tools/og-image.js
//
// The source is print/og-image.html. It has to agree with the site's header:
// the mark, the promise, and the location line.

const { chromium } = require('playwright');
const path = require('path');

const ROOT = path.join(__dirname, '..');

(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
  await page.goto('file://' + path.join(ROOT, 'print/og-image.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(400);
  await page.screenshot({ path: path.join(ROOT, 'og-image.png') });
  console.log('drew og-image.png');
  await browser.close();
})();
