// Soundline — social cards for the rotation board.
//
// Redraws the Phase One look (img/social/01..09) and carries it through
// phases two, three and four. One PNG per card, not per slot: a card that
// runs twice is one file used twice, so a date move never orphans artwork.
//
//   node tools/social-cards.js 2        → phase two cards into img/social/
//   node tools/social-cards.js 1        → the November 11 information-night card
//   node tools/social-cards.js 3 4      → phases three and four
//   node tools/social-cards.js all      → everything
//   node tools/social-cards.js --audit  → what the rotation actually sells
//
// Prints the slot schedule it expects, and refuses to run if a scheduled
// date falls on the wrong weekday for its slot.

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const OUT = path.join(__dirname, '..', 'img', 'social');

// ---------------------------------------------------------------- the wheel
// Four slots a week. Monday is the drop-off scroll, Wednesday night is when
// the week has gone badly enough to read this, Friday noon is sharable,
// Sunday at seven is the only hour a parent fills in a form.
const WHEEL = {
  mechanism: { day: 'Mon', time: '07:30', job: 'How the day actually works' },
  mirror:    { day: 'Wed', time: '20:30', job: 'Name the thing they already feel' },
  place:     { day: 'Fri', time: '12:00', job: 'People, town, the name, the Showcase' },
  ask:       { day: 'Sun', time: '19:00', job: 'Survey, tuition, the next information night' },
};

// --------------------------------------------------------------- the cards
// track: home → Glow, public → Making, shared → Beacon. The last headline
// line takes the track colour, as in Phase One.
//
// pillar: what the card actually sells. An eleven-to-fourteen-year-old needs
// three things, and a parent of one is shopping for all three:
//
//   significance — the work matters to somebody besides a gradebook
//   belonging    — they are known, by name, by the same adults, for years
//   fun          — they want to walk in the door
//
// Two other values are not pillars and are capped deliberately. 'trust'
// answers the parent's anxiety (the bus, the paperwork, the deposit, the
// research): necessary, and it converts nobody on its own. 'event' is the
// standing invitation. Run --audit to see the balance.
const CARDS = {
  // ---- homeschool -------------------------------------------------------
  h3: {
    track: 'home',
    pillar: 'trust',
    head: ["We'll keep", 'your hours log.'],
    foot: ['Course descriptions, hours, the quarterly report.',
           'The Collaborative · three days a week'],
  },
  h4: {
    track: 'home',
    pillar: 'significance',
    head: ['A sixth grader and', 'an eighth grader,', 'same table, same skill.'],
    foot: ['Each moves on when they have got it.', 'Not in June. Not when the class catches up.'],
  },
  h5: {
    track: 'home',
    pillar: 'significance',
    head: ['They explain their work', 'out loud. To someone', "who isn't you."],
    foot: ['Every six weeks. No slides.',
           'It is hard to do at home. Here it is part of school.'],
  },
  h7: {
    track: 'home',
    pillar: 'significance',
    head: ['Thursdays, they work', 'next to someone who', 'does it for a living.'],
    foot: ['Seventh and eighth grade apprenticeships.',
           'Real work, beside a real adult, in their own town.'],
  },
  h8: {
    track: 'home',
    pillar: 'trust',
    head: ['Homeschooling?', 'Come three days', 'a week.'],
    foot: ['Mon and Wed 9:15 to 12:30 · Fri 9:15 to 2:45',
           'We hand you the paperwork for your district.'],
  },

  // ---- public school ----------------------------------------------------
  p1v2: {
    track: 'public',
    pillar: 'belonging',
    head: ['Doing fine.', 'And that’s all.'],
    foot: ['Good grades, no spark. Middle school goes fast.',
           'Information night January 14.'],
  },
  p3: {
    track: 'public',
    pillar: 'trust',
    head: ['Eleven minutes', 'in a folding chair,', 'twice a year.'],
    foot: ['An 88 does not tell you what your child can do.',
           'A folder of proof does.'],
  },
  p4: {
    track: 'public',
    pillar: 'trust',
    head: ['Six hours on a Chromebook', 'is not a curriculum.'],
    foot: ['Taught by a person with a book, never by an app.',
           'How much screen time? Less than you would think.'],
  },
  p5: {
    track: 'public',
    pillar: 'significance',
    head: ['Mornings: math,', 'reading and writing.', 'Then classes, labs', 'and real projects.'],
    foot: ['School is 8:30 to 3:00. After school until 5:30.',
           'Grades 6–8 · North Shore · September 2027'],
  },
  p6: {
    track: 'public',
    pillar: 'trust',
    head: ['Each part has been', 'studied for decades.', 'One school is new.'],
    foot: ['Moving on when you have it. Long projects. One close teacher.',
           'The research, with sources, is on our site.'],
  },
  p7: {
    track: 'public',
    pillar: 'significance',
    head: ['Four minutes of work.', 'Thirty-eight of waiting.'],
    foot: ['Here, a kid who is ready moves on.',
           'Each child works at their own level.'],
  },
  p8: {
    track: 'public',
    pillar: 'trust',
    head: ['The bus. The IEP.', 'And sports.'],
    foot: ['Three questions every parent asks first.',
           'All three are answered on our site.'],
  },
  // Phase two onward: tuition is published and enrollment is live, so the
  // Ask stops promising a date and starts naming what is open.
  p9v2: {
    track: 'public',
    pillar: 'trust',
    head: ['Tuition is published.', 'Sign-up is open.'],
    foot: ['Our first families pay less,',
           'and keep that price through twelfth grade.'],
  },

  // ---- belonging --------------------------------------------------------
  // Being known is a function of arithmetic and of time. Both are things we
  // can state as fact rather than promise, which is the only way to say
  // "your child will be known" without sounding like a brochure.
  b1: {
    track: 'shared',
    pillar: 'belonging',
    head: ['Ten to twelve', 'in a grade.', 'There is no back row.'],
    foot: ['No child gets overlooked.',
           'Every adult in the building knows your kid.'],
  },
  b2: {
    track: 'shared',
    pillar: 'belonging',
    head: ['The same adult,', 'September of sixth', 'to June of eighth.'],
    foot: ['Long enough to notice when something is off.',
           'Long enough to be believed when they say it.'],
  },
  b3: {
    track: 'home',
    pillar: 'belonging',
    head: ['A sixth grader can be', 'the best in the room', 'at something.'],
    foot: ['Each child works at their own level,',
           'so everyone is ahead at something.'],
  },

  // ---- fun --------------------------------------------------------------
  // The hardest of the three to claim, because a school that says it is fun
  // sounds unserious. So none of these say "fun" — they describe what it
  // looks like from the passenger seat.
  f1: {
    track: 'public',
    pillar: 'fun',
    head: ['They tell you about it', 'in the car.'],
    foot: ['The whole way home, without being asked.',
           'That is how you know school is working.'],
  },
  f2: {
    track: 'public',
    pillar: 'fun',
    head: ['When did school', 'get so quiet?'],
    foot: ['Here, kids build things all afternoon.',
           'Loud is allowed.'],
  },
  f3: {
    track: 'shared',
    pillar: 'fun',
    head: ['Ask yours what', "they'd build,", 'given six weeks.'],
    foot: ['Then ask where they could do that now.',
           'Here, every student finishes a project every six weeks.'],
  },

  // ---- the plain-language message (12 Nov 2026) --------------------------
  // What the site now says first: it is a school, it is new, and it is not
  // school as usual. "School as usual" is aimed at the model, never at a
  // school or a district.
  n1: {
    track: 'shared',
    pillar: 'significance',
    head: ['A new middle school.', 'Not school as usual.'],
    foot: ['Soundline School · grades 6, 7 and 8',
           'Opening September 2027'],
  },
  n2: {
    track: 'public',
    pillar: 'belonging',
    head: ['You know your kid.', 'School should too.'],
    foot: ['Ten to twelve students in a grade.',
           'Every adult knows your kid.'],
  },
  n3: {
    track: 'shared',
    pillar: 'significance',
    head: ['Nobody knows what', 'work will look like', 'when they are thirty.'],
    foot: ['So we teach what will matter no matter what:',
           'learn hard things, make things, explain them out loud.'],
  },
  n4: {
    track: 'shared',
    pillar: 'trust',
    head: ['Is your child younger?', 'We will call you', 'when it is their turn.'],
    foot: ['Sign-up for September 2028 opens in August 2027.',
           'Ask for a reminder call on our site.'],
  },

  // ---- shared -----------------------------------------------------------
  s1: {
    track: 'shared',
    pillar: 'belonging',
    head: ['“He’ll know your child', 'by Wednesday.”'],
    foot: ['Adam King, lead guide (our word for teacher)',
           'Every adult here knows your kid.'],
  },
  s2v2: {
    track: 'shared',
    pillar: 'significance',
    head: ['Depth', 'with direction.'],
    sub: 'Every child has a soundline.',
    foot: ['Where they are, skill by skill —',
           'and what sparks them, and how deep it runs.'],
  },
  s3: {
    track: 'shared',
    pillar: 'fun',
    head: ['Friday, 2:00.', 'Usually loud.'],
    foot: ['Every Friday, students show their work.',
           'Families are welcome.'],
  },
  // The night itself. Phase One art (img/social/01..09) predates this
  // generator and is not redrawn here; this is the one Phase One card the
  // generator owns, because the hour and the venue were confirmed late.
  s4nov: {
    track: 'shared',
    pillar: 'event',
    head: ['Information night,', 'November 11.'],
    foot: ['7:00 pm · Port Jefferson Free Library',
           'Founding enrollment opens the next morning.'],
  },
  // The deposit sits with an independent agent, not with us. No other
  // school says this, and it answers the question a school without a
  // building gets asked before any other.
  x1escrow: {
    track: 'shared',
    pillar: 'trust',
    head: ['We do not hold', 'your deposit.'],
    foot: ['$500 holds a seat. An independent agent keeps it.',
           'You get all of it back until we sign a lease.'],
  },
  s4dec: {
    track: 'shared',
    pillar: 'event',
    head: ['Information night,', 'December 12.'],
    foot: ['What Soundline is. What a day looks like.',
           'Free and open to all.'],
  },
  s4jan: {
    track: 'shared',
    pillar: 'event',
    head: ['Information night,', 'January 14.'],
    foot: ['What Soundline is. What a day looks like.',
           'Free and open to all.'],
  },
};

// ------------------------------------------------------------ the schedule
// A proposal, not gospel — the board names which posts belong to a phase but
// not which date each lands on. The posts actually queued (Facebook, Instagram,
// Threads) live in the scheduler; on 12 Nov 2026 the queue through Dec 4 was
// given these images and plain-language captions. n4 (the reminder call) is
// drawn and not yet scheduled. Edit freely; the weekday check below keeps
// an edit from quietly drifting off the wheel.
const SCHEDULE = {
  // Phase One ran on hand-drawn art; only the information-night card is
  // regenerated here, because the venue and the hour were confirmed after
  // the rest of that set was made.
  1: { window: 'Oct 28 – Nov 11 · warm', slots: [
    ['2026-11-08', 'ask',       's4nov'],
  ]},
  2: { window: 'Nov 12 – Nov 30 · open', slots: [
    ['2026-11-13', 'place',     'n1'],
    ['2026-11-15', 'ask',       'p9v2'],
    ['2026-11-16', 'mechanism', 'b1'],
    ['2026-11-18', 'mirror',    'f1'],
    ['2026-11-20', 'place',     'n2'],        // was x1escrow: held until the escrow account is confirmed open
    ['2026-11-22', 'ask',       's4dec'],
    ['2026-11-23', 'mechanism', 'p8'],
    ['2026-11-25', 'mirror',    'h5'],
    ['2026-11-27', 'place',     's1'],
    ['2026-11-29', 'ask',       'p9v2'],
    ['2026-11-30', 'mechanism', 'p5'],
  ]},
  3: { window: 'Dec 1 – Dec 12 · report card', slots: [
    ['2026-12-02', 'mirror',    'p7'],
    ['2026-12-04', 'place',     's3'],
    ['2026-12-06', 'ask',       's4dec'],
    ['2026-12-07', 'mechanism', 'b2'],
    ['2026-12-09', 'mirror',    'f3'],
    ['2026-12-11', 'place',     'h7'],
  ]},
  4: { window: 'Jan 2 – Jan 14 · the switch window', slots: [
    ['2027-01-03', 'ask',       's4jan'],
    ['2027-01-04', 'mechanism', 'p5'],
    ['2027-01-06', 'mirror',    'p1v2'],
    ['2027-01-08', 'place',     'n3'],
    ['2027-01-10', 'ask',       'h8'],
    ['2027-01-11', 'mechanism', 'b3'],
    ['2027-01-13', 'mirror',    'f2'],
  ]},
};

// ------------------------------------------------------------------ drawing
const ACCENT = { home: 'var(--glow)', public: 'var(--making)', shared: 'var(--beacon)' };

const MARK = `<svg class="mark" viewBox="0 0 160 160" aria-hidden="true">
  <path d="M80 24 L88 56 L120 64 L88 72 L80 104 L72 72 L40 64 L72 56 Z" fill="#F2C14E" stroke="#F7F5F0" stroke-width="7" stroke-linejoin="round"/>
  <path d="M44 24 L52 32 M116 24 L108 32 M80 6 V12" stroke="#F7F5F0" stroke-width="6" stroke-linecap="round"/>
  <path d="M12 122 H148" stroke="#F7F5F0" stroke-width="9" stroke-linecap="round"/>
  <path d="M14 144 C28 134, 40 154, 54 144 S80 134, 94 144 S120 154, 134 144 L146 136" stroke="#7FE0C9" stroke-width="8" stroke-linecap="round" fill="none"/>
</svg>`;

// One full period across the plate, riding off both edges.
const WAVE = `<svg class="wave" viewBox="0 0 1080 90" preserveAspectRatio="none" aria-hidden="true">
  <path d="M-10 52 C 130 14, 270 14, 410 52 S 690 90, 830 52 S 1090 14, 1090 30"
        fill="none" stroke="currentColor" stroke-width="11" stroke-linecap="round"/>
</svg>`;

const page = (c) => `<!doctype html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Instrument+Sans:wght@400;500;600;700&family=Newsreader:ital,wght@0,400;1,400&display=swap">
<style>
  :root{
    --deep:#12222B; --beacon:#F2C14E; --glow:#7FE0C9; --paper:#F7F5F0; --making:#FF5A7A;
    --dim:rgba(247,245,240,.62); --rule:rgba(247,245,240,.22);
    --shout:"Bricolage Grotesque","Helvetica Neue",Arial,sans-serif;
    --reassure:"Newsreader",Georgia,serif;
    --read:"Instrument Sans",Arial,sans-serif;
    --accent:${ACCENT[c.track]};
  }
  *{box-sizing:border-box;margin:0;padding:0}
  body{width:1080px;height:1350px;background:var(--deep);color:var(--paper);
       font-family:var(--read);overflow:hidden}
  .card{width:1080px;height:1350px;padding:78px 80px 0;display:flex;flex-direction:column;
        position:relative}

  .lockup{display:flex;align-items:center;gap:20px;flex:none}
  .mark{width:58px;height:58px;flex:none}
  .name{display:flex;flex-direction:column;gap:6px}
  .wordmark{font-family:var(--shout);font-weight:800;font-size:31px;line-height:1;
            letter-spacing:-.01em;text-transform:uppercase}
  .where{font-weight:600;font-size:15px;letter-spacing:.18em;text-transform:uppercase;color:var(--dim)}

  /* headline sits in the room between the lockup and the rule */
  .body{flex:1;display:flex;flex-direction:column;justify-content:center;
        padding-bottom:40px;min-height:0}
  h1{font-family:var(--shout);font-weight:800;letter-spacing:-.04em;line-height:.96;
     font-size:84px}
  h1 span{display:block}
  h1 span:last-child{color:var(--accent)}
  h1 em{font-style:normal;color:var(--accent)}
  .sub{font-family:var(--reassure);font-style:italic;font-size:40px;line-height:1.38;
       color:rgba(247,245,240,.82);margin-top:30px;max-width:21ch}

  /* the plate: hairline, two lines of footing, the domain, the wave */
  .plate{flex:none;padding-bottom:74px}
  .hair{height:1px;background:var(--rule);margin-bottom:26px}
  .foot-row{display:flex;align-items:flex-end;justify-content:space-between;gap:40px}
  .foot{font-size:26px;line-height:1.36;color:rgba(247,245,240,.92);white-space:nowrap}
  .url{font-weight:700;font-size:26px;white-space:nowrap}
  .wave{position:absolute;left:0;right:0;bottom:-16px;width:1080px;height:90px;
        color:var(--accent)}
</style></head><body>
<div class="card">
  <div class="lockup">${MARK}
    <span class="name"><span class="wordmark">Soundline</span>
    <span class="where">A new middle school · North Shore, Long Island</span></span>
  </div>
  <div class="body">
    <h1 id="head">${c.head.map((l) => `<span>${l.replace(/\{([^}]*)\}/g, '<em>$1</em>')}</span>`).join('')}</h1>
    ${c.sub ? `<p class="sub">${c.sub}</p>` : ''}
  </div>
  <div class="plate">
    <div class="hair"></div>
    <div class="foot-row">
      <p class="foot" id="foot">${c.foot.join('<br>')}</p>
      <span class="url">soundlineschool.com</span>
    </div>
  </div>
  ${WAVE}
</div>
</body></html>`;

// ------------------------------------------------------------------ running
function resolve(argv) {
  const want = argv.length ? argv : ['all'];
  const phases = want.includes('all') ? [1, 2, 3, 4] : want.map(Number);
  for (const p of phases) {
    if (!SCHEDULE[p]) throw new Error(`no phase ${p} — known phases are 1, 2, 3, 4`);
  }
  return phases;
}

function check(phases) {
  const problems = [];
  const DAY = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  for (const p of phases) {
    for (const [date, slot, id] of SCHEDULE[p].slots) {
      if (!CARDS[id]) problems.push(`phase ${p}: no card "${id}"`);
      const want = WHEEL[slot];
      if (!want) { problems.push(`phase ${p}: no slot "${slot}"`); continue; }
      const got = DAY[new Date(date + 'T12:00:00Z').getUTCDay()];
      if (got !== want.day) {
        problems.push(`phase ${p}: ${date} is a ${got}, but the ${slot} slot runs ${want.day}`);
      }
    }
  }
  if (problems.length) {
    console.error('The schedule has drifted off the wheel:\n  ' + problems.join('\n  '));
    process.exit(1);
  }
}

// What a phase sells, counted off the wheel rather than off the deck: a card
// scheduled twice argues twice, and a card nobody scheduled argues nothing.
// Trust is capped because it answers the parent's anxiety and converts no
// one on its own, and because it is the easiest kind of card to keep writing.
function audit() {
  const PILLARS = ['significance', 'belonging', 'fun', 'trust', 'event'];
  const warn = [];
  const total = Object.fromEntries(PILLARS.map((k) => [k, 0]));

  for (const n of [1, 2, 3, 4]) {
    const runs = SCHEDULE[n].slots.map((s) => CARDS[s[2]].pillar);
    const by = Object.fromEntries(PILLARS.map((k) =>
      [k, runs.filter((r) => r === k).length]));
    PILLARS.forEach((k) => { total[k] += by[k]; });

    console.log(`\nPhase ${n} · ${SCHEDULE[n].window}  (${runs.length} posts)`);
    for (const k of PILLARS) {
      if (!by[k] && k === 'event') continue;
      const share = runs.length ? Math.round((by[k] / runs.length) * 100) : 0;
      console.log(`  ${k.padEnd(13)} ${String(by[k]).padStart(2)}  ${'█'.repeat(by[k])}${by[k] ? ' ' : ''}${share}%`);
    }
    if (n > 1) {
      for (const k of ['belonging', 'fun']) {
        if (!by[k]) warn.push(`phase ${n} argues ${k} nowhere`);
      }
      if (by.trust > by.significance + by.belonging + by.fun) {
        warn.push(`phase ${n} is more reassurance than offer`);
      }
    }
  }

  const runs = Object.values(total).reduce((a, b) => a + b, 0);
  console.log(`\nAcross the rotation · ${runs} posts`);
  for (const k of PILLARS) {
    console.log(`  ${k.padEnd(13)} ${String(total[k]).padStart(2)}  ${Math.round((total[k] / runs) * 100)}%`);
  }

  const unused = Object.keys(CARDS).filter((id) =>
    ![1, 2, 3, 4].some((n) => SCHEDULE[n].slots.some((s) => s[2] === id)));
  if (unused.length) console.log(`\nDrawn but not scheduled: ${unused.join(', ')}`);
  if (warn.length) console.log('\nThin:\n  ' + warn.join('\n  '));
}

(async () => {
  const argv = process.argv.slice(2);
  if (argv.includes('--audit')) { audit(); return; }

  const phases = resolve(argv);
  check(phases);

  const needed = [...new Set(phases.flatMap((p) => SCHEDULE[p].slots.map((s) => s[2])))];
  fs.mkdirSync(OUT, { recursive: true });

  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const ctx = await browser.newContext({
    viewport: { width: 1080, height: 1350 },
    deviceScaleFactor: 1,
  });
  const p = await ctx.newPage();

  for (const id of needed) {
    const card = CARDS[id];
    await p.setContent(page(card), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);

    // Shrink until each authored line holds on one line — headline against
    // the measure, footing against the room left beside the domain.
    await p.evaluate(() => {
      const fit = (el, start, floor, room) => {
        let size = start;
        const over = () => [...el.children].some((n) => n.scrollWidth > room)
                        || el.scrollWidth > room;
        while (over() && size > floor) { size -= 2; el.style.fontSize = size + 'px'; }
      };
      const card = document.querySelector('.card');
      const measure = card.clientWidth - 160;
      fit(document.getElementById('head'), 84, 46, measure);
      const url = document.querySelector('.url');
      fit(document.getElementById('foot'), 26, 17, measure - url.offsetWidth - 40);
    });

    const file = path.join(OUT, `p${phases.find((n) =>
      SCHEDULE[n].slots.some((s) => s[2] === id))}-${id}.png`);
    await p.screenshot({ path: file });
    console.log('drew', path.relative(path.join(__dirname, '..'), file));
  }
  await browser.close();

  for (const n of phases) {
    const ph = SCHEDULE[n];
    console.log(`\nPhase ${n} · ${ph.window}`);
    for (const [date, slot, id] of ph.slots) {
      const w = WHEEL[slot];
      console.log(`  ${date} ${w.day} ${w.time}  ${slot.padEnd(10)} ${id}`);
    }
  }
})();
