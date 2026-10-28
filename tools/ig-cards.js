// Soundline — Instagram Phase One cards.
// Nine 4:5 type cards in the Oct 25 flyer style, one per Phase One slot on the
// rotation board. Track colour carries the audience: homeschool on Shallows,
// public school on Making, shared on Beacon.

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const OUT = process.argv[2];

// Accent text is wrapped in {braces}. Lines break exactly where they are written.
const CARDS = [
  {
    file: 'p1-fine-on-paper',
    track: 'public',
    kicker: 'Grades 6–8 · Miller Place · September 2027',
    head: ['Fine on paper', 'and quietly', '{checked out.}'],
    sub: 'Middle school is three years. They go fast.',
    foot: 'Eight to ten in a grade. One advisor for three years.',
  },
  {
    file: 's2-every-child',
    track: 'shared',
    kicker: 'Soundline · A school on the Sound',
    head: ['Every child has', 'a {soundline.}'],
    sub: 'Sailors dropped a weighted rope to learn the depth — and a dab of tallow brought up a piece of the bottom.',
    foot: 'Only then did they set a course.',
  },
  {
    file: 'p9-tuition-nov-12',
    track: 'public',
    kicker: 'Founding families · a rate that stays locked',
    head: ['Tuition,', '{November 12.}', 'Enrollment that night.'],
    sub: 'We publish what it costs that evening, before anyone is asked to commit.',
    foot: 'Eight to ten in a grade. Three grades. That is the whole building.',
  },
  {
    file: 'h2-hard-part',
    track: 'home',
    kicker: 'The Collaborative · three days a week',
    head: ['The hard part was', '{never the teaching.}'],
    sub: 'It’s the lab. The ensemble. The seminar that needs eight kids who have all actually read the book.',
    foot: 'Monday, Wednesday, Friday. You keep the rest of the week.',
  },
  {
    file: 'p2-not-the-problem',
    track: 'public',
    kicker: 'Grades 6–8 · Miller Place · September 2027',
    head: ['The teachers are', '{not the problem.}'],
    sub: 'Twenty-eight kids in a room is. Forty-two minutes is. A pacing calendar that moves whether or not your child got it is.',
    foot: 'So we built the other version.',
  },
  {
    file: 's1-know-your-child',
    track: 'shared',
    kicker: 'Adam King · lead guide',
    head: ['“He’ll know', 'your child', '{by Wednesday.}”'],
    sub: 'A musician and a teacher who builds music and STEAM programs for libraries across Long Island.',
    foot: 'Four adults in the building. Every student known.',
  },
  {
    file: 's4-information-night',
    track: 'shared',
    kicker: 'Free and open to all',
    head: ['Information night,', '{November 12.}'],
    sub: 'What Soundline is. What a day looks like. What it costs.',
    foot: 'Grades six through eight, Miller Place, opening September 2027.',
  },
  {
    file: 'h6-only-screen',
    track: 'home',
    kicker: 'Mornings at a table, with a person',
    head: ['The only screen', 'in the morning', '{belongs to the guide.}'],
    sub: 'AI is a subject here. Taught on purpose, never used as a shortcut.',
    foot: 'Seminar, lab and the defense happen with no screen at all.',
  },
  {
    file: 'h1-didnt-leave-school',
    track: 'home',
    kicker: 'The Collaborative · three days a week',
    head: ['You didn’t leave school', 'to {join another one.}'],
    sub: 'Monday, Wednesday, Friday, 8:30 to 3:00. Same guides, same rooms, same studio as the full-time school.',
    foot: 'Your plan stays yours.',
  },
];

const MARK = `<svg class="mark" viewBox="0 0 160 160" aria-hidden="true">
  <path d="M80 24 L88 56 L120 64 L88 72 L80 104 L72 72 L40 64 L72 56 Z" fill="#F2C14E" stroke="#F7F5F0" stroke-width="7" stroke-linejoin="round"/>
  <path d="M44 24 L52 32 M116 24 L108 32 M80 6 V12" stroke="#F7F5F0" stroke-width="6" stroke-linecap="round"/>
  <path d="M12 122 H148" stroke="#F7F5F0" stroke-width="9" stroke-linecap="round"/>
  <path d="M14 144 C28 134, 40 154, 54 144 S80 134, 94 144 S120 154, 134 144 L146 136" stroke="#7FE0C9" stroke-width="8" stroke-linecap="round" fill="none"/>
</svg>`;

const accent = (line) =>
  line.replace(/\{([^}]*)\}/g, '<em>$1</em>');

const page = (c) => `<!doctype html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Instrument+Sans:wght@400;500;600&family=Newsreader:ital,wght@0,400;1,400&display=swap">
<style>
  :root{
    --deep:#12222B; --beacon:#F2C14E; --channel:#1B4B6E; --shallows:#5FB4E6;
    --glow:#7FE0C9; --paper:#F7F5F0; --making:#FF5A7A; --making-edge:#FF8A47;
    --on-dark-dim:rgba(247,245,240,.78);
    --shout:"Bricolage Grotesque","Helvetica Neue",Arial,sans-serif;
    --reassure:"Newsreader",Georgia,serif;
    --read:"Instrument Sans",Arial,sans-serif;
  }
  *{box-sizing:border-box;margin:0;padding:0}
  body{width:1080px;height:1350px;background:var(--deep);color:var(--paper);
       font-family:var(--read);overflow:hidden}
  .card{width:1080px;height:1350px;padding:72px;display:flex;flex-direction:column}

  /* the five-colour rule, as on the Oct 25 flyer */
  .rule{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-bottom:56px}
  .rule i{height:11px;border-radius:999px;display:block}
  .rule i:nth-child(1){background:var(--shallows)}
  .rule i:nth-child(2){background:var(--glow)}
  .rule i:nth-child(3){background:var(--beacon)}
  .rule i:nth-child(4){background:var(--making-edge)}
  .rule i:nth-child(5){background:var(--making)}

  .lockup{display:flex;align-items:center;gap:18px}
  .mark{width:66px;height:66px;flex:none}
  .name{display:flex;flex-direction:column;gap:5px}
  .wordmark{font-family:var(--shout);font-weight:800;font-size:34px;line-height:1;
            letter-spacing:-.045em;text-transform:uppercase}
  .where{font-family:var(--read);font-weight:600;font-size:14px;letter-spacing:.17em;
         text-transform:uppercase;color:var(--on-dark-dim)}

  .body{flex:1;display:flex;flex-direction:column;justify-content:center;gap:40px;
        padding-block:56px}
  h1{font-family:var(--shout);font-weight:800;letter-spacing:-.045em;line-height:.98;
     font-size:96px}
  h1 span{display:block}
  h1 em{font-style:normal;color:var(--accent)}
  .sub{font-family:var(--reassure);font-style:italic;font-size:38px;line-height:1.32;
       color:var(--glow);max-width:22ch}

  .tail{display:flex;flex-direction:column;gap:28px}
  .kicker{align-self:flex-start;font-family:var(--read);font-weight:600;font-size:19px;
          letter-spacing:.02em;color:var(--paper);border:3px solid var(--accent);
          border-radius:999px;padding:12px 24px}
  .foot-line{font-family:var(--read);font-size:25px;line-height:1.45;color:var(--on-dark-dim);
             max-width:34ch}
  .base{display:flex;align-items:baseline;justify-content:space-between;gap:24px;
        border-top:2px solid rgba(247,245,240,.18);padding-top:26px}
  .say{font-family:var(--reassure);font-style:italic;font-size:26px;color:var(--beacon)}
  .url{font-family:var(--read);font-weight:600;font-size:17px;letter-spacing:.14em;
       text-transform:uppercase;color:var(--on-dark-dim)}
</style></head><body>
<div class="card" style="--accent:var(--${c.track === 'home' ? 'shallows' : c.track === 'public' ? 'making' : 'beacon'})">
  <div class="rule"><i></i><i></i><i></i><i></i><i></i></div>
  <div class="lockup">${MARK}
    <span class="name"><span class="wordmark">Soundline</span>
    <span class="where">School · Miller Place, NY</span></span>
  </div>
  <div class="body">
    <h1 id="head">${c.head.map((l) => `<span>${accent(l)}</span>`).join('')}</h1>
    <p class="sub">${c.sub}</p>
  </div>
  <div class="tail">
    <span class="kicker">${c.kicker}</span>
    <p class="foot-line">${c.foot}</p>
    <div class="base">
      <span class="say">Depth with direction.</span>
      <span class="url">soundlineschool.com</span>
    </div>
  </div>
</div>
</body></html>`;

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const ctx = await browser.newContext({
    viewport: { width: 1080, height: 1350 },
    deviceScaleFactor: 1,
  });
  const p = await ctx.newPage();

  for (const c of CARDS) {
    await p.setContent(page(c), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);

    // Shrink the headline until it fits the measure without wrapping a written line.
    await p.evaluate(() => {
      const h = document.getElementById('head');
      const card = document.querySelector('.card');
      const room = card.clientWidth - 144;
      let size = 96;
      const fits = () =>
        [...h.children].every((s) => s.scrollWidth <= room);
      while (!fits() && size > 48) {
        size -= 2;
        h.style.fontSize = size + 'px';
      }
    });

    const file = path.join(OUT, c.file + '.png');
    await p.screenshot({ path: file });
    console.log('wrote', file);
  }

  await browser.close();
})();
