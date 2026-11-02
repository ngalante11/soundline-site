// Soundline — paid creative for the November 11 information night.
//
// Same look as the organic cards in tools/social-cards.js, re-cut for Meta
// Ads Manager placements. One creative, three aspect ratios: Ads Manager
// wants a separate upload per ratio and will letterbox anything it has to
// crop itself.
//
//   node tools/ads-nov11.js            → all three sizes into img/ads/
//
// Stories keeps Meta's safe area clear: nothing that must be read sits in
// the top 14% (profile row) or the bottom 20% (the swipe-up furniture).

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const OUT = path.join(__dirname, '..', 'img', 'ads');

const MARK = `<svg class="mark" viewBox="0 0 160 160" aria-hidden="true">
  <path d="M80 24 L88 56 L120 64 L88 72 L80 104 L72 72 L40 64 L72 56 Z" fill="#F2C14E" stroke="#F7F5F0" stroke-width="7" stroke-linejoin="round"/>
  <path d="M44 24 L52 32 M116 24 L108 32 M80 6 V12" stroke="#F7F5F0" stroke-width="6" stroke-linecap="round"/>
  <path d="M12 122 H148" stroke="#F7F5F0" stroke-width="9" stroke-linecap="round"/>
  <path d="M14 144 C28 134, 40 154, 54 144 S80 134, 94 144 S120 154, 134 144 L146 136" stroke="#7FE0C9" stroke-width="8" stroke-linecap="round" fill="none"/>
</svg>`;

const WAVE = `<svg class="wave" viewBox="0 0 1080 90" preserveAspectRatio="none" aria-hidden="true">
  <path d="M-10 52 C 130 14, 270 14, 410 52 S 690 90, 830 52 S 1090 14, 1090 30"
        fill="none" stroke="currentColor" stroke-width="11" stroke-linecap="round"/>
</svg>`;

// The event is the offer, so the date carries the weight a headline usually
// carries and the hook sits under it. Beacon throughout: this is a shared
// card, it has to work for a homeschooling parent and a public-school one.
//
// The headline sells the three things a middle schooler needs and a parent
// of one is actually shopping for: significance, belonging, fun. Publishing
// tuition is what sets us apart from other schools, but to a cold parent it
// reads as a pitch, so price and logistics sit in the footing as
// reassurance rather than leading.
const COPY = {
  kicker: 'Wednesday, November 11 · 7:00 pm',
  head: ['They matter.', 'They belong.', 'They want to be here.'],
  sub: 'Port Jefferson Free Library',
  foot: ['Free · no sign-up · about an hour',
         'Grades 6–8 · opening September 2027'],
};

// width, height, and the type scale each ratio can carry. `floor` is where
// the last line of type sits above the bottom edge; `wave` is where the rule
// rides. In Stories both clear Meta's bottom furniture, and the wave sits
// below the footing rather than through it.
const SIZES = [
  { id: 'feed-4x5',   w: 1080, h: 1350, head: 92,  kick: 29, sub: 40, foot: 26, pad: '78px 80px 0',  floor: 74,  wave: -16 },
  { id: 'feed-1x1',   w: 1080, h: 1080, head: 80,  kick: 27, sub: 34, foot: 24, pad: '62px 80px 0',  floor: 74,  wave: -16 },
  { id: 'story-9x16', w: 1080, h: 1920, head: 104, kick: 32, sub: 46, foot: 28, pad: '270px 80px 0', floor: 494, wave: 368 },
];

const page = (s) => `<!doctype html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Instrument+Sans:wght@400;500;600;700&family=Newsreader:ital,wght@0,400;1,400&display=swap">
<style>
  :root{
    --deep:#12222B; --beacon:#F2C14E; --glow:#7FE0C9; --paper:#F7F5F0;
    --dim:rgba(247,245,240,.62); --rule:rgba(247,245,240,.22);
    --shout:"Bricolage Grotesque","Helvetica Neue",Arial,sans-serif;
    --reassure:"Newsreader",Georgia,serif;
    --read:"Instrument Sans",Arial,sans-serif;
    --accent:var(--beacon);
  }
  *{box-sizing:border-box;margin:0;padding:0}
  body{width:${s.w}px;height:${s.h}px;background:var(--deep);color:var(--paper);
       font-family:var(--read);overflow:hidden}
  .card{width:${s.w}px;height:${s.h}px;padding:${s.pad};display:flex;flex-direction:column;
        position:relative}

  .lockup{display:flex;align-items:center;gap:20px;flex:none}
  .mark{width:58px;height:58px;flex:none}
  .name{display:flex;flex-direction:column;gap:6px}
  .wordmark{font-family:var(--shout);font-weight:800;font-size:31px;line-height:1;
            letter-spacing:-.01em;text-transform:uppercase}
  .where{font-weight:600;font-size:15px;letter-spacing:.18em;text-transform:uppercase;color:var(--dim)}

  .body{flex:1;display:flex;flex-direction:column;justify-content:center;
        padding-bottom:40px;min-height:0}

  /* the date, boxed, because it is the single thing the ad is selling */
  .kicker{display:inline-flex;align-self:flex-start;font-family:var(--shout);font-weight:700;
          font-size:${s.kick}px;letter-spacing:-.01em;line-height:1;white-space:nowrap;
          color:var(--deep);background:var(--beacon);padding:14px 20px 15px;margin-bottom:34px}
  h1{font-family:var(--shout);font-weight:800;letter-spacing:-.04em;line-height:.96;
     font-size:${s.head}px}
  h1 span{display:block;white-space:nowrap}
  h1 span:last-child{color:var(--accent)}
  .sub{font-family:var(--reassure);font-style:italic;font-size:${s.sub}px;line-height:1.3;
       color:rgba(247,245,240,.82);margin-top:28px;max-width:22ch}

  .plate{flex:none;padding-bottom:${s.floor}px}
  .hair{height:1px;background:var(--rule);margin-bottom:26px}
  .foot-row{display:flex;align-items:flex-end;justify-content:space-between;gap:40px}
  .foot{font-size:${s.foot}px;line-height:1.36;color:rgba(247,245,240,.92);white-space:nowrap}
  .url{font-weight:700;font-size:${s.foot}px;white-space:nowrap}
  .wave{position:absolute;left:0;right:0;bottom:${s.wave}px;
        width:${s.w}px;height:90px;color:var(--accent)}
</style></head><body>
<div class="card">
  <div class="lockup">${MARK}
    <span class="name"><span class="wordmark">Soundline</span>
    <span class="where">School · Miller Place, NY</span></span>
  </div>
  <div class="body">
    <span class="kicker">${COPY.kicker}</span>
    <h1 id="head">${COPY.head.map((l) => `<span>${l}</span>`).join('')}</h1>
    <p class="sub">${COPY.sub}</p>
  </div>
  <div class="plate">
    <div class="hair"></div>
    <div class="foot-row">
      <p class="foot" id="foot">${COPY.foot.join('<br>')}</p>
      <span class="url">soundlineschool.com</span>
    </div>
  </div>
  ${WAVE}
</div>
</body></html>`;

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch({ args: ['--no-sandbox'] });

  for (const s of SIZES) {
    const ctx = await browser.newContext({
      viewport: { width: s.w, height: s.h },
      deviceScaleFactor: 1,
    });
    const p = await ctx.newPage();
    await p.setContent(page(s), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);

    // Shrink until every authored line holds on one line, as the organic
    // cards do: the kicker and the footing must never wrap.
    const overflow = await p.evaluate(() => {
      const fit = (el, start, floor, room) => {
        let size = start;
        const over = () => [...el.children].some((n) => n.scrollWidth > room)
                        || el.scrollWidth > room;
        while (over() && size > floor) { size -= 2; el.style.fontSize = size + 'px'; }
        return !over();
      };
      const card = document.querySelector('.card');
      const measure = card.clientWidth - 160;
      const ok = [];
      ok.push(fit(document.getElementById('head'), parseFloat(getComputedStyle(document.getElementById('head')).fontSize), 44, measure));
      const url = document.querySelector('.url');
      ok.push(fit(document.getElementById('foot'), parseFloat(getComputedStyle(document.getElementById('foot')).fontSize), 16, measure - url.offsetWidth - 40));
      ok.push(document.querySelector('.kicker').scrollWidth <= measure);
      // No type may spill past the frame. The wave is deliberately bled off
      // the bottom edge, so measure the plate rather than the card's scroll.
      const plate = document.querySelector('.plate').getBoundingClientRect();
      ok.push(plate.bottom <= card.clientHeight + 1);
      const b = document.querySelector('.body');
      ok.push(b.scrollHeight <= b.clientHeight + 1);
      // .plate's rect includes its bottom padding, so measure the type.
      const wave = document.querySelector('.wave').getBoundingClientRect();
      ok.push(wave.top >= document.querySelector('.foot-row').getBoundingClientRect().bottom - 1);
      return ok.every(Boolean) ? null : 'copy does not fit the frame';
    });
    if (overflow) throw new Error(`${s.id}: ${overflow}`);

    const file = path.join(OUT, `nov11-${s.id}.png`);
    await p.screenshot({ path: file });
    console.log('drew', path.relative(path.join(__dirname, '..'), file), `${s.w}x${s.h}`);
    await ctx.close();
  }
  await browser.close();
})();
