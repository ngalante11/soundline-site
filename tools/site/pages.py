# soundlineschool.com: every page but Home. Edit, then run  python3 tools/site/make.py  from the repo root.
from core import *  # noqa: F401,F403

# ------------------------------------------------------------------ A DAY HERE
def day():
    H = 0
    o = head('A day at Soundline School | Private middle school, grades 6–8') + root_open(H) + chrome('day')
    o += f'''<section style="background: {DEEP}; color: {PAPER}; padding: clamp(48px, 6.5vw, 96px) 0 {HALF}">
<div style="{WP}; display: flex; flex-direction: column; gap: clamp(28px, 3.4vw, 48px)">
<h1 style="margin: 0; font-family: {READ}; font-weight: 500; font-size: 15px; line-height: 1.4; color: {GLOW}">A day at Soundline School · 8:30 to 3:00</h1>
<p style="margin: 0; font-family: {SHOUT}; font-weight: 800; font-size: clamp(44px, 6vw, 88px); line-height: 0.98; letter-spacing: -0.045em">
<span style="display: block; text-wrap: balance">Two hours of practice.</span>
<span style="display: block; font-family: {SAY}; font-style: italic; font-weight: 400; letter-spacing: -0.02em; line-height: 1.08; color: {BEACON}; text-wrap: balance">Four hours of making.</span>
</p>
<p style="margin: 0; max-width: 640px; font-size: clamp(17px, 1.3vw, 19px); line-height: 1.55; color: {DIM_D}">Mornings are for skills, at each student’s own pace. Afternoons are for real work with a real audience. Then everyone goes home, or stays for Extended Day.</p>
<div aria-label="The school day" style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 12px">
<div style="flex: 2 1 200px; min-width: 0">{bar('Practice', '8:30, two hours', f'background: {SHALLOWS}; color: {DEEP}')}</div>
<div style="flex: 4 1 400px; min-width: 0">{bar('Making', 'Four hours, to 3:00', f'background: {MAKING}; color: {DEEP}')}</div>
<div style="flex: 2.5 1 250px; min-width: 0">{bar('Extended Day', 'To 5:30, if you need it', f'border: 2px dashed {PAPER}; color: {PAPER}')}</div>
</div>
</div>
</section>
'''
    entries = [
        ('8:30', 'Arrival', None, 'The door.', 'The same face every morning. Bag on the hook, phone in the box, a word about the weekend.'),
        ('8:45', 'Launch', None, 'Advisory, fifteen minutes.', 'Ten to twelve students, one guide for three years. Today’s goal: clear the proportions gate, draft the lab question.'),
        ('9:00', 'Practice, 50 min', 'p', 'Math, at their own gate.', 'The gate opens when they can show it to a guide, not when the unit ends. Across the table, a sixth grader is on a gate this student cleared in week one; beside them, an eighth grader is on one they’ll reach by winter.'),
        ('9:50', 'Practice, 40 min', 'p', 'Reading and writing.', 'Today’s text: how ice carved the Sound, because the lab needs it. Two paragraphs, one an argument.'),
        ('10:30', 'Seminar, 30 min', 'p', 'The seminar. Today, math.', 'Every morning at 10:30 the whole school sits down with one real thing from town and one question, and the students name the skills it takes. Tuesday is math: someone proves why the shortcut works; this student finds the case where it doesn’t. The fourth try lands.'),
        ('11:00', 'Outside, 40 min', None, 'Lunch and outside.', 'Outside, every day, whatever the weather. Most of what a guide learns about a student, they learn here.'),
        ('11:40', 'Lab, 95 min', 'm', 'The sounder.', 'A sensor on a line that reads the depth of a tank: the sounding line, rebuilt. Today is calibration, and the graph bends where it shouldn’t. Defended Friday.'),
        ('1:15', 'Studio, 60 min', 'm', 'The Quest.', 'Week three of six. The client is the children’s librarian: an exhibit on how sound travels through water. The group has a plan, forty dollars, and a speaker that won’t stay sealed. A guide is in the room and does not fix it.'),
        ('2:15', 'Ensemble, 45 min', 'm', 'The ensemble.', 'Everyone plays something; nobody has to be good yet. The bass part is this student’s.'),
        ('3:00', 'To 5:30, if you need it', 'x', 'Home, or not yet.', 'A lesson at 3:15, then the homework desk until 5:30. Or the carline. The quest stays at school.'),
    ]
    rows = ''
    for t, meta, kind, title, body in entries:
        look = {'p': f'background: {SHALLOWS}', 'm': f'background: {MAKING}', 'x': f'border-left: 2px dashed {DEEP}', None: 'background: transparent'}[kind]
        rows += (f'<li style="border-top: 1px solid {RULE_P}; padding: 22px 0; display: flex; gap: 22px; align-items: stretch">\n'
                 f'<div style="flex: none; width: 84px; text-align: right"><time style="font-family: {SHOUT}; font-weight: 800; font-size: 24px; line-height: 1.15; letter-spacing: -0.03em">{t}</time></div>\n'
                 f'<div aria-hidden="true" style="flex: none; width: 8px; border-radius: 4px; box-sizing: border-box; {look}"></div>\n'
                 f'<div style="flex: 1 1 auto; min-width: 0">\n{ital(meta, CHANNEL, "17px", "2px")}\n'
                 f'<h3 style="margin: 0 0 6px; font-family: {SHOUT}; font-weight: 800; font-size: 24px; line-height: 1.08; letter-spacing: -0.035em">{title}</h3>\n'
                 f'<p style="margin: 0; font-size: 16.5px; line-height: 1.6; color: {DIM_P}; max-width: 560px">{body}</p>\n</div>\n</li>\n')
    key = (f'<div style="display: flex; flex-wrap: wrap; gap: 10px 24px; font-size: 15px; color: {DIM_P}">'
           f'<span style="display: flex; align-items: center; gap: 8px"><span aria-hidden="true" style="width: 28px; height: 8px; border-radius: 4px; background: {SHALLOWS}"></span>Practice</span>'
           f'<span style="display: flex; align-items: center; gap: 8px"><span aria-hidden="true" style="width: 28px; height: 8px; border-radius: 4px; background: {MAKING}"></span>Making</span>'
           f'<span style="display: flex; align-items: center; gap: 8px"><span aria-hidden="true" style="width: 28px; height: 0; border-top: 2px dashed {DEEP}"></span>Extended Day</span></div>')
    o += f'''<section id="tuesday" style="padding: {PAD} 0 {HALF}">
<div style="{WP}; display: flex; flex-wrap: wrap; gap: 48px 88px; align-items: flex-start">
<div style="flex: 1 1 340px; min-width: 0; display: flex; flex-direction: column; gap: 28px">
<div>
{ph2('One seventh grader. One day. Hour by hour.', maxw='11ch')}
{psub('September, the first six-week cycle. The Tuesday we’ll run, followed through one student’s day. No name, because it isn’t any one child’s day yet.', mb='0')}
</div>
{key}
{pic('reading', 'Illustration: a student with long braids writing at a wooden desk by a window, a stack of books beside her.', '4 / 3', '50% 40%')}
{pic('painting', 'Illustration: a student with red curls, grinning, painting a blue and yellow wave on a sheet of plywood.', '4 / 3', '50% 40%', 'Illustrations. ' + ILLO)}
</div>
<ol style="flex: 1.35 1 460px; min-width: 0; list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; border-bottom: 1px solid {RULE_P}">
{rows}</ol>
</div>
<div style="{WP}"><p style="margin: 28px 0 0; text-align: right; font-family: {SAY}; font-style: italic; font-size: 19px; color: {DIM_P}">Imagined. Our first students arrive in September 2027.</p></div>
</section>
<section style="padding: {HALF} 0 {PAD}">
<div style="{WP}">
{ph2('How the day adds up.', maxw='14ch', mb='48px')}
{ledger([('Practice: two hours.', 'Ninety minutes at their own gate, thirty out loud. Hands-on, at a table with a guide; the only screen in the morning belongs to the guide.'), ('Making: four hours.', 'Lab, quest, ensemble, and forty minutes outside. Taught by a person, built for someone who asked.'), ('Where the stretch is.', 'The fourth try at 10:30, and Friday’s graph. The guide knows which one is hard.'), ('What goes in the folder.', 'The gate, if it opened. The paragraph. The graph. By eighth grade the folder is a portfolio; this Tuesday is one page.')])}</div>
</section>
'''
    week = [('Monday', 'Launch', '8:45. One question, one goal, one plan for the week.', False),
            ('Tuesday', 'Lab, then studio', 'Ninety minutes, hands on, written up before studio. Then everyone makes something: a video game, a robot, a portrait, a sculpture, a song for the ensemble.', False),
            ('Wednesday', 'Seminar', 'The long one. A novel, a question, a paragraph. Every seminar ends in writing.', False),
            ('Thursday', 'Apprenticeships', 'Grades 7 and 8 work alongside someone who does it for a living. Younger students build their quest.', False),
            ('Friday', 'All In, then Showcase', 'The whole school takes on one thing together. A song, a mural, a project for someone in town. At 2:00, someone presents and something is performed. Usually loud. Families welcome.', True)]
    wh = ''
    for d, t, b, fri in week:
        top = f'8px solid {MAKING}' if fri else f'1px solid {DEEP}'
        pt = '15px' if fri else '22px'
        wh += (f'<div style="border-top: {top}; padding-top: {pt}">\n{ital(d, CHANNEL, "19px", "6px")}\n'
               f'<h3 style="margin: 0 0 10px; font-family: {SHOUT}; font-weight: 800; font-size: 23px; line-height: 1.08; letter-spacing: -0.035em">{t}</h3>\n'
               f'<p style="margin: 0; font-size: 16px; line-height: 1.55; color: {DIM_P}">{b}</p>\n</div>\n')
    o += f'''<section id="week" style="background: #FFFFFF; padding: {PAD} 0; border-top: 1px solid {RULE_P}">
<div style="{WP}">
<div style="display: flex; flex-wrap: wrap; gap: 36px 88px; align-items: flex-end; margin-bottom: 64px">
<div style="flex: 1.2 1 380px; min-width: 0">
{ph2('A week at Soundline.', maxw='12ch')}
{psub('Same rhythm every week, so the work can be different. Every morning at 10:30, the whole school: one real thing from town, one question, and the students name the skills it takes.', mb='0')}
</div>
<div style="flex: 1 1 320px; min-width: 0">
{pic('road', 'Illustration: three students walking and talking down a tree-lined road in autumn.', '16 / 9', '50% 88%', 'An illustration. ' + ILLO)}
</div>
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(200px, 100%), 1fr)); gap: 40px 28px">
{wh}</div>
</div>
</section>
'''
    o += tracks_section()
    o += f'''<section style="background: {DEEP}; color: {PAPER}; padding: {PAD} 0">
<div style="{WP}; display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 36px 64px">
<div style="flex: 1 1 460px; min-width: 0">
{ph2('Be one of our Founding Families.', dark=True, maxw='14ch')}
<p style="margin: 0; font-family: {SAY}; font-style: italic; font-size: clamp(20px, 1.9vw, 27px); line-height: 1.4; color: {DIM_D}; max-width: 640px">A rate that stays locked for as long as your child is enrolled, and a seat on the Family Council.</p>
</div>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 16px 28px">
{btn('Ask for a call', CALL, 'beacon')}
{quiet('See tuition', 'join.html#tuition', dark=True)}
</div>
</div>
</section>
'''
    o += footer() + '</div>\n' + tail(1440, H)
    return o, 1440, H


# ------------------------------------------------------------------ TUITION AND ADMISSIONS
def admissions():
    H = 0
    o = head('Tuition and admissions, 2027–28 | Soundline School') + root_open(H) + chrome('adm')
    o += f'''<section style="background: {DEEP}; color: {PAPER}; padding: clamp(48px, 6.5vw, 96px) 0 {HALF}">
<div style="{WP}; display: flex; flex-direction: column; gap: clamp(28px, 3.4vw, 48px)">
<h1 style="margin: 0; font-family: {READ}; font-weight: 500; font-size: 15px; line-height: 1.4; color: {GLOW}">Soundline School tuition and admissions, 2027–28</h1>
<p style="margin: 0; font-family: {SHOUT}; font-weight: 800; font-size: clamp(40px, 5.4vw, 80px); line-height: 0.98; letter-spacing: -0.045em; max-width: 19ch; text-wrap: balance">We tell you the number before we ask you for anything.</p>
<p style="margin: 0; font-family: {SAY}; font-style: italic; font-size: clamp(22px, 2.3vw, 33px); line-height: 1.3; color: {BEACON}">Twelve monthly payments. Here is the whole table.</p>
</div>
</section>
'''

    def fig(big, small, size):
        return (f'<div style="display: flex; flex-direction: column; gap: 6px">'
                f'<span style="font-family: {SHOUT}; font-weight: 800; font-size: {size}; line-height: 1; letter-spacing: -0.045em">{big}</span>'
                f'<span style="font-size: 15px; color: {DIM_P}">{small}</span></div>')

    def colhead(chip, name, note):
        return (f'<div role="columnheader" style="padding: 26px 24px 26px 0; display: flex; flex-direction: column; gap: 8px">'
                f'<span aria-hidden="true" style="display: block; width: 72px; height: 8px; border-radius: 4px; background: {chip}"></span>'
                f'<span style="font-family: {SHOUT}; font-weight: 800; font-size: 26px; letter-spacing: -0.035em; line-height: 1.05">{name}</span>'
                f'<span style="font-size: 15px; color: {DIM_P}">{note}</span></div>')
    cols = 'grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr) minmax(0, 1fr)'
    BIG, MID = 'clamp(44px, 4.6vw, 66px)', 'clamp(28px, 2.8vw, 38px)'
    def srow(name, big, small, size, lead=False):
        fam = f'font-family: {SAY}; font-style: italic; font-size: {"22px" if lead else "19px"}; line-height: 1.2' + ('' if lead else f'; color: {DIM_P}')
        return (f'<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 16px; padding: 16px 0; border-top: 1px solid {RULE_P}">'
                f'<span style="{fam}">{name}</span>'
                f'<span style="text-align: right"><span style="display: block; font-family: {SHOUT}; font-weight: 800; font-size: {size}; line-height: 1; letter-spacing: -0.045em">{big}</span>'
                f'<span style="font-size: 14px; color: {DIM_P}">{small}</span></span></div>\n')

    def scard(chip, name, note, f, s):
        return (f'<div style="border-top: 2px solid {DEEP}; padding: 22px 0 8px">\n'
                f'<span aria-hidden="true" style="display: block; width: 72px; height: 8px; border-radius: 4px; background: {chip}; margin-bottom: 10px"></span>\n'
                f'<h2 style="margin: 0 0 4px; font-family: {SHOUT}; font-weight: 800; font-size: 26px; letter-spacing: -0.035em; line-height: 1.05">{name}</h2>\n'
                f'<p style="margin: 0 0 16px; font-size: 15px; color: {DIM_P}">{note}</p>\n'
                + srow('Founding Families', f[0], f[1], '44px', True) + srow('Standard tuition', s[0], s[1], '28px') + '</div>\n')
    stack = ('<div class="only-narrow">\n<p style="margin: 0 0 20px; font-size: 15px; color: ' + DIM_P + '">A month, over twelve months. Founding Families pay 10% less, and the rate holds through twelfth grade.</p>\n'
             + scard(CHANNEL, 'The School', 'Five days a week, 8:30 to 3:00', ('$1,350', '$16,200 a year'), ('$1,500', '$18,000 a year'))
             + scard(SHALLOWS, 'The Collaborative', 'Three days a week, for homeschooling families', ('$810', '$9,720 a year'), ('$900', '$10,800 a year'))
             + '</div>\n')
    details = [('What’s included', 'Everything in the day: the two hours of practice, the four hours of making, the Quest, the arts, Showcase Friday. There is no materials fee on top of tuition.'),
               ('Extended Day', 'Until 5:30, priced separately. Founding Families pay 10% less for it too.'),
               ('Two kids', '10% off the second.'),
               ('Class size', 'Ten to twelve students in a grade, three grades, and one advisor for three years.'),
               ('Paying in full', 'Pay the year by March 1 and take 3% off, on top of the founding rate.'),
               ('No application fee', 'Nothing is due to apply, and nothing you pay now is on top of tuition.')]
    dh = ''.join(f'<div style="border-top: 1px solid {DEEP}; padding-top: 20px">\n<h3 style="margin: 0 0 8px; font-family: {READ}; font-weight: 600; font-size: 19px; line-height: 1.3">{t}</h3>\n'
                 f'<p style="margin: 0; font-size: 16px; line-height: 1.55; color: {DIM_P}">{b}</p>\n</div>\n' for t, b in details)
    o += f'''<section id="tuition" style="padding: {PAD} 0">
<div style="{WP}">
{stack}<div class="only-wide">
<div role="table" aria-label="Tuition, 2027–28" style="min-width: 660px; border-top: 2px solid {DEEP}; border-bottom: 1px solid {DEEP}">
<div role="row" style="display: grid; {cols}; align-items: end">
<div role="columnheader" style="padding: 26px 24px 26px 0; font-size: 15px; color: {DIM_P}">A month, over twelve months</div>
{colhead(CHANNEL, 'The School', 'Five days a week, 8:30 to 3:00')}
{colhead(SHALLOWS, 'The Collaborative', 'Three days a week, for homeschooling families')}
</div>
<div role="row" style="display: grid; {cols}; align-items: center; border-top: 1px solid {DEEP}">
<div role="rowheader" style="padding: 34px 24px 34px 0">
<span style="display: block; font-family: {SAY}; font-style: italic; font-size: 27px; line-height: 1.2">Founding Families</span>
<span style="font-size: 15px; color: {DIM_P}">10% off, and your rate holds through twelfth grade</span>
</div>
<div role="cell" style="padding: 34px 24px 34px 0">{fig('$1,350', '$16,200 a year', BIG)}</div>
<div role="cell" style="padding: 34px 24px 34px 0">{fig('$810', '$9,720 a year', BIG)}</div>
</div>
<div role="row" style="display: grid; {cols}; align-items: center; border-top: 1px solid {RULE_P}">
<div role="rowheader" style="padding: 26px 24px 26px 0">
<span style="display: block; font-family: {SAY}; font-style: italic; font-size: 22px; line-height: 1.2; color: {DIM_P}">Standard tuition</span>
</div>
<div role="cell" style="padding: 26px 24px 26px 0">{fig('$1,500', '$18,000 a year', MID)}</div>
<div role="cell" style="padding: 26px 24px 26px 0">{fig('$900', '$10,800 a year', MID)}</div>
</div>
</div>
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr)); gap: 44px 40px; margin-top: 88px">
{dh}</div>
</div>
</section>
'''

    def chain(amount, title, body, first=False):
        col = BEACON if first else PAPER
        return (f'<li style="min-width: 0; border-top: 1px solid {PAPER}; padding: 24px 0 0; display: flex; flex-direction: column; gap: 10px">\n'
                f'<span style="font-family: {SHOUT}; font-weight: 800; font-size: clamp(44px, 4.6vw, 66px); line-height: 0.95; letter-spacing: -0.045em; color: {col}">{amount}</span>\n'
                f'<h3 style="margin: 4px 0 0; font-family: {SHOUT}; font-weight: 800; font-size: 26px; line-height: 1.05; letter-spacing: -0.035em">{title}</h3>\n'
                f'<p style="margin: 0; font-size: 16.5px; line-height: 1.6; color: {DIM_D}; max-width: 340px">{body}</p>\n</li>\n')
    o += f'''<section id="reserve" style="background: {DEEP}; color: {PAPER}; padding: {PAD} 0">
<div style="{WP}">
{ph2('What you pay, and where it goes.', dark=True, maxw='14ch')}
{psub('Nothing you pay is on top. Each payment counts toward the next.', dark=True, mb='64px')}
<ol style="list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr)); gap: 48px 56px">
{chain('$500', 'Reserves a seat.', 'Held by an independent escrow agent, not by us. It comes back in full, for any reason, until the day we sign a lease.', True)}{chain('$2,500', 'Your deposit.', 'Due with the enrollment contract. The $500 counts toward it, and you will have the address in hand before you are ever asked for it.')}{chain('Tuition', 'Twelve monthly payments.', 'The deposit counts toward tuition. Payments start the summer before your child walks in. Not two lump sums in August and January.')}</ol>
<p style="margin: 64px 0 0; font-family: {SAY}; font-style: italic; font-size: clamp(21px, 2vw, 27px); line-height: 1.4; color: {PAPER}; max-width: 760px">If the school doesn’t open, your money comes back. We mail you a check.</p>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 16px 28px; margin-top: 44px">
{btn('Ask for a call', CALL, 'beacon')}
<span style="font-size: 16px; color: {DIM_D}; max-width: 520px">Reserving starts with a twenty-minute call. Each grade has ten to twelve seats, filled in the order families reserve.</span>
</div>
</div>
</section>
'''
    dates = [('Nov 12', 'Tuition published. Founding enrollment opens.', True),
             ('Dec 12', 'Information night, Saturday. Details to follow.', False),
             ('Jan 14', 'Information night. Details to follow.', False),
             ('Mar 1', 'Pay the year in full by today and take 3% off.', False),
             ('Apr 1', 'Busing: your request to your own district is due. We send it to you already filled in.', False),
             ('Jun 1', 'IEP services: your request to the district is due. We help you do it.', False),
             ('Sept 2027', 'The first day.', False)]
    dt = ''
    for d, t, now in dates:
        top = f'8px solid {BEACON}' if now else f'1px solid {DEEP}'
        pt = '13px' if now else '20px'
        dt += (f'<li style="border-top: {top}; padding: {pt} 18px 0 0; min-width: 0">\n'
               f'<time style="display: block; font-family: {SHOUT}; font-weight: 800; font-size: 26px; letter-spacing: -0.035em; line-height: 1.1; margin-bottom: 8px">{d}</time>\n'
               f'<span style="font-size: 15.5px; line-height: 1.5; color: {DIM_P}">{t}</span>\n</li>\n')
    o += f'''<section style="padding: {PAD} 0 {HALF}">
<div style="{WP}">
{ph2('The dates, on the line.', maxw='14ch', mb='56px')}
<ol style="list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(150px, 100%), 1fr)); gap: 36px 0">
{dt}</ol>
</div>
</section>
'''
    money = (faq('What is a founding rate, exactly?', 'The tuition you enroll at is the tuition you pay, every year your child is here, through twelfth grade. It does not rise with our costs, and it does not rise when the school gets harder to get into. Founding families carry their rate the whole way.', True)
             + faq('How is it paid?', 'Monthly, over twelve months, starting the summer before your child walks in. Not two lump sums in August and January.')
             + faq('What if the school doesn’t open?', 'Your $500 comes back in full, for any reason, until the day we sign a lease. If the school doesn’t open after that, your money comes back too: we mail you a check.')
             + faq('Is there financial aid of your own?', 'Yes, and it is a real line in our first budget rather than an afterthought. Tell us that cost is the question for you. It changes how we build the aid pool, and it does not count against your child.')
             + faq('Is busing really free?', 'Your own district provides it to a private school up to fifteen miles from your home, at their cost, if you request it by April 1. We will send you the request already filled in.'))
    school = (faq('How many students will there be?', 'Ten to twelve in a grade — and nobody’s stuck in their grade. Students work by skill across the school, and on Fridays the whole school builds one thing together. Few enough that there’s nowhere to hide, enough for a real seminar.', True)
              + faq('Where will the school be?', 'On the North Shore, along the Miller Place–Port Jefferson Station corridor. Port Jefferson Station is the likeliest. We announce the address the day we sign the lease.')
              + faq('What about high school?', 'Ninth grade opens here in September 2028, then a grade every year through twelfth. New York has moved to a diploma built on evidence of six things a graduate can do, and every one of them is something your child makes, defends, or shows here, every six weeks.')
              + faq('How much screen time is there?', 'Less than you’d think. Morning practice is hands-on, at a table with a guide; the only screen in the morning belongs to the guide. Seminar, lab, and the defense happen without screens. AI is taught as a subject, never used as a shortcut.'))
    ny = (faq('Is Soundline approved by New York?', 'New York doesn’t license private schools. You register with the state, and the district reviews that what you teach is equivalent. We do all of it, then start accreditation once we’re open.', True)
          + faq('Do students take the state tests?', 'Yes — the state tests in the spring, three mornings, no test prep. New York uses them to confirm a new school is teaching what it should, and we’d rather show that than argue about it. What you’ll see all year is growth, three times a year, for your own child.')
          + faq('How do you screen the adults who work with my child?', 'Every adult who works with students is fingerprinted through the New York State Education Department before they start, and is checked against the sex offender registry. Everyone completes mandated reporter training. There are always at least two adults in the building.')
          + faq('My child has an IEP. What happens to services?', 'Your child can still receive services from the public school district. You request them from the district where the school is located by June 1, and we’ll help you do it.'))

    def group(title, body):
        return (f'<div style="min-width: 0; border-bottom: 1px solid {RULE_P}">\n{ital(title, CHANNEL, "24px", "14px")}\n{body}</div>\n')
    o += f'''<section id="questions" style="padding: {HALF} 0 {HALF}">
<div style="{WP}">
{ph2('Questions families ask.', maxw='14ch', mb='56px')}
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(320px, 100%), 1fr)); gap: 48px 56px; align-items: start">
{group('Money', money)}{group('The school', school)}{group('New York', ny)}</div>
</div>
</section>
'''
    o += f'''<section id="scholarship" style="background: #FFFFFF; border-top: 1px solid {RULE_P}; border-bottom: 1px solid {RULE_P}; padding: {HALF} 0">
<div style="{WP}; display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px 64px">
<div style="flex: 1 1 460px; min-width: 0">
<h2 style="margin: 0 0 12px; font-family: {SHOUT}; font-weight: 800; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.02; letter-spacing: -0.04em; max-width: 22ch">A federal scholarship starts the January before we open.</h2>
<p style="margin: 0; font-size: 17px; line-height: 1.6; color: {DIM_P}; max-width: 640px">A new federal tax credit for private school scholarships begins January 1, 2027. New York has said it will opt in and has not yet filed. We have written up everything we know.</p>
</div>
{quiet('The federal scholarship, in full', 'scholarship.html')}
</div>
</section>
'''
    o += call_section() + footer() + '</div>\n' + tail(1440, H)
    return o, 1440, H




# ------------------------------------------------------------------ SHARED BY THE PAGES BELOW
def page_hero(label, lines, lede='', extra=''):
    """Dark opener: a small descriptive H1, the display line(s), a lede. The last display line is set in the reassuring face."""
    spans = ''
    for i, t in enumerate(lines):
        if i == len(lines) - 1 and len(lines) > 1:
            spans += f'<span style="display: block; font-family: {SAY}; font-style: italic; font-weight: 400; letter-spacing: -0.02em; line-height: 1.08; color: {BEACON}; text-wrap: balance">{t}</span>\n'
        else:
            spans += f'<span style="display: block; text-wrap: balance">{t}</span>\n'
    led = f'<p style="margin: 0; max-width: 640px; font-size: clamp(17px, 1.3vw, 19px); line-height: 1.55; color: {DIM_D}">{lede}</p>\n' if lede else ''
    return f'''<section class="on-dark" style="background: {DEEP}; color: {PAPER}; padding: clamp(48px, 6.5vw, 96px) 0 {HALF}">
<div style="{WP}; display: flex; flex-direction: column; gap: clamp(24px, 3vw, 40px)">
<h1 style="margin: 0; font-family: {READ}; font-weight: 500; font-size: 15px; line-height: 1.4; color: {GLOW}">{label}</h1>
<p style="margin: 0; font-family: {SHOUT}; font-weight: 800; font-size: clamp(40px, 5.4vw, 80px); line-height: 0.98; letter-spacing: -0.045em; max-width: 20ch">
{spans}</p>
{led}{extra}</div>
</section>
'''


def founding_plate():
    return f'''<section class="on-dark" style="background: {DEEP}; color: {PAPER}; padding: {PAD} 0">
<div style="{WP}; display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 36px 64px">
<div style="flex: 1 1 460px; min-width: 0">
{ph2('Be one of our Founding Families.', dark=True, maxw='14ch')}
<p style="margin: 0; font-family: {SAY}; font-style: italic; font-size: clamp(20px, 1.9vw, 27px); line-height: 1.4; color: {DIM_D}; max-width: 640px">A rate that stays locked for as long as your child is enrolled, and a seat on the Family Council.</p>
</div>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 16px 28px">
{btn('Ask for a call', CALL, 'beacon')}
{quiet('See tuition', 'join.html#tuition', dark=True)}
</div>
</div>
</section>
'''


def prose(paras, dark=False):
    c = DIM_D if dark else DIM_P
    return ''.join(f'<p style="margin: 0 0 20px; font-size: 18px; line-height: 1.6; color: {c}; max-width: 640px">{t}</p>\n' for t in paras)


PEOPLE = [('Founder', 'Nicole Galante, Ph.D.', 'An educator for over twenty years. She started as a classroom teacher, coached teachers in New York City schools for more than fifteen of them, and led the state team that wrote New York’s Quality Remote and Hybrid Teaching Framework and its Handbook for Virtual Schools.'),
          ('Lead guide', 'Adam King', 'A musician and teacher. He designs and runs music and STEAM programs for libraries across Long Island (escape rooms, instrument labs, world percussion) and teaches private lessons. He’ll know your child by Wednesday.'),
          ('Operations', 'Gina Dimichino', 'For more than thirty-five years she has taught dance to North Shore kids, many of them right at this age, and she has run businesses here her whole life, including her own salon. She makes sure every family feels seen, and handles every detail in between.'),
          ('Academic systems', 'Izzy Galante', 'Designs how the school teaches: the sequence, the mastery gates, and how we know it worked. Co-wrote New York’s Quality Remote and Hybrid Teaching Framework and its Handbook for Virtual Schools. Teaches a live seminar every week.')]


# ------------------------------------------------------------------ OUR VISION
def vision():
    o = head('Our vision | Soundline School, private middle school on Long Island’s North Shore') + root_open(0) + chrome('vision')
    six = [('Learn something hard.', 'And prove it.'), ('Make something new.', 'For a client in town, on a deadline.'), ('Think it through.', 'In writing, first.'),
           ('Say it out loud.', 'And defend it, no screen.'), ('Show up for their town.', 'One project a year is for the town.'), ('Know where they’re headed.', 'And how they got there.')]
    sx = ''.join(f'<li style="border-top: 1px solid {RULE_D}; padding: 22px 0 6px">\n'
                 f'<h2 style="margin: 0 0 6px; font-family: {SHOUT}; font-weight: 800; font-size: clamp(24px, 2.4vw, 33px); line-height: 1.05; letter-spacing: -0.04em; color: {PAPER}">{t}</h2>\n'
                 f'<p style="margin: 0; font-size: 17px; color: {DIM_D}">{b}</p>\n</li>\n' for t, b in six)
    extra = f'''<ol style="list-style: none; margin: 12px 0 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr)); gap: 12px 56px">
{sx}</ol>
<p style="margin: 28px 0 0; font-family: {SAY}; font-style: italic; font-size: clamp(22px, 2.3vw, 33px); line-height: 1.3; color: {BEACON}; max-width: 760px">New York just decided a diploma should mean six things, not a set of test scores. We built the school on those six.</p>
<p style="margin: 0; max-width: 640px; font-size: 18px; color: {DIM_D}">Every six weeks, your child adds to a folder of proof: made, defended, grown. By eighth grade it’s a portfolio.</p>
'''
    o += page_hero('Our vision · What a Soundline student can do by eighth grade', ['By eighth grade, a student who can:'], extra=extra)
    o += f'''<section style="padding: {PAD} 0 {HALF}">
<div style="{WP}">
{ph2('How you’ll know it’s working.', maxw='14ch', mb='48px')}
{ledger([('We measure growth three times a year and publish it.', 'NWEA MAP, three times a year. We publish whole-school growth, counting everyone. No child’s score is public; yours comes home.'), ('You’ll see the work.', 'The robot, the performance, your child explaining it.'), ('AI is a subject here.', 'Taught on purpose. Never a shortcut in seminar, lab, or the defense.'), ('We answer to New York.', 'We register with the state, the district reviews our program, and accreditation starts once we’re open.')])}</div>
</section>
<section style="padding: {HALF} 0 {PAD}">
<div style="{WP}">
{ph2('None of this is new. Putting it in one building is.', maxw='18ch', mb='48px')}
{ledger([('Mornings: you don’t move on until you’ve got it.', 'Mastery before moving on beats the calendar, in over a hundred studies. Struggling students gain most.'), ('Afternoons: real projects raise real scores.', 'In randomized trials, long projects beat the usual way on state tests.'), ('Seminar: writing it down is how it sticks.', 'Writing about it, and saying it out loud, is how it sticks.'), ('Advisory: being known changes how hard a student works.', 'One close teacher relationship is among the strongest predictors of effort, more so with age. Hence one advisor for three years.')])}<div style="display: flex; flex-wrap: wrap; gap: 12px 36px; margin-top: 36px">
{quiet('The research, with sources', 'research.html')}
{quiet('Who’s building it', 'about.html#people')}
</div>
</div>
</section>
'''
    o += founding_plate() + footer() + '</div>\n' + tail()
    return o, 0, 0


# ------------------------------------------------------------------ ABOUT US
def about():
    o = head('About us | Soundline School, private middle school on Long Island’s North Shore') + root_open(0) + chrome('about')
    o += page_hero('About Soundline School', ['Every student,', 'known.'], 'Ten to twelve in a grade, one advisor for three years, and four people who will know your child by name.')
    story = ['Before sonar, sailors dropped a sounding line over the side: a rope marked in fathoms, weighted with lead. A dab of tallow pressed into the base of the weight brought up a piece of the bottom (sand, shell, mud), so they knew what was underneath, too. Only then did they set a course.',
             'That’s how we come to know your child. Not only where they are, skill by skill, but what sparks them and how deep it runs. Middle schoolers thrive when they feel seen, when the adult mentoring them truly knows what they need.',
             'Then we set a direction together. What sparks your child becomes part of the actual work, approached with intention: the next skill, the next project, the next thing worth showing their peers and their town. That gives a student more than a written grade ever could.',
             'We teach everything New York expects. Your child’s soundline is what we build on.']
    ph = ''
    for role, name, bio in PEOPLE:
        ph += (f'<div style="border-top: 1px solid {DEEP}; padding-top: 20px">\n{ital(role, CHANNEL, "18px", "4px")}\n'
               f'<h3 style="margin: 0 0 10px; font-family: {SHOUT}; font-weight: 800; font-size: 24px; line-height: 1.05; letter-spacing: -0.035em">{name}</h3>\n'
               f'<p style="margin: 0; font-size: 15.5px; line-height: 1.55; color: {DIM_P}">{bio}</p>\n</div>\n')
    o += f'''<section id="story" style="padding: {PAD} 0">
<div style="{WP}; display: flex; flex-wrap: wrap; align-items: flex-start; gap: 48px 88px">
<div style="flex: 1 1 380px; min-width: 0">
{pic('chart', 'A 1941 nautical chart of the water off Mount Sinai: a compass rose surrounded by depth soundings.', '1 / 1', '32% 60%', 'Chart 361, Port Jefferson and Mount Sinai Harbors. U.S. Coast and Geodetic Survey, 1941. Every number is a sounding.', chart=True)}
</div>
<div style="flex: 1.1 1 440px; min-width: 0">
{ph2('Every child has a soundline.', maxw='11ch', mb='28px')}
{prose(story)}<p style="margin: 8px 0 0; font-family: {SAY}; font-style: italic; font-size: 27px; line-height: 1.3; color: {CHANNEL}">Depth with direction.</p>
</div>
</div>
</section>
<section style="background: #FFFFFF; border-top: 1px solid {RULE_P}; border-bottom: 1px solid {RULE_P}; padding: {PAD} 0">
<div style="{WP}">
{ph2('Ten to twelve in a grade. Nobody’s stuck in it.', maxw='16ch')}
{psub('Students work by skill across the school, and on Fridays the whole school builds one thing together. Few enough that there’s nowhere to hide, enough for a real seminar.')}
{ledger([('One advisor, three years.', 'Every student has the same guide as their advisor from the day they start, in a group of ten to twelve.'), ('Grouped by skill, not age.', 'A sixth grader and an eighth grader can work the same skill at the same table. Each moves on when it’s mastered.'), ('Three grades, one building.', 'And a grade added every year through twelfth, starting with ninth. The older students are out in town on apprenticeships.')])}</div>
</section>
<section id="people" style="padding: {PAD} 0">
<div style="{WP}">
{ph2('Who’s building it.', maxw='14ch', mb='48px')}
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(240px, 100%), 1fr)); gap: 44px 32px">
{ph}</div>
<p style="margin: 48px 0 0; font-size: 17px; color: {DIM_P}; max-width: 640px">We are hiring a math and science guide and a humanities guide for September 2027. You will meet them before the first day.</p>
</div>
</section>
'''
    o += founding_plate() + footer() + '</div>\n' + tail()
    return o, 0, 0


# ------------------------------------------------------------------ THE COLLABORATIVE
def collaborative():
    o = head('The Collaborative | Three days a week for homeschooling families | Soundline School') + root_open(0) + chrome('collab')
    extra = f'''<p style="margin: 0; max-width: 640px; font-size: 17px; color: {GLOW}">Your plan stays yours. Your filings stay yours. We hand you the course descriptions and hours logs to go with them.</p>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 14px 28px; margin-top: 8px">
{btn('Ask for a call', CALL, 'beacon')}
<span style="font-size: 16px; color: {DIM_D}; max-width: 460px">Tell us you homeschool. We run the Collaborative conversation separately, and we will write back ourselves.</span>
</div>
'''
    o += page_hero('The Collaborative · A three-day homeschool program for grades 6–8 on Long Island’s North Shore',
                   ['You keep teaching your child.', 'We take Monday, Wednesday, Friday.'],
                   'The Collaborative is Soundline three days a week for homeschooling families on the North Shore. Same guides, same rooms, same studio, same Friday build as the full-time students — and your child goes home with you the rest of the week.', extra)
    two = ['Most families who homeschool a twelve-year-old are not short on instruction. They are short on two specific things: a room of peers who will argue with your child about a book, and a workshop with tools in it.',
           'That is what the three days are. Monday and Wednesday, 9:15 to 12:30, are practice and studio — math, writing, and the long project, at a table with a guide who knows where your child actually is. Friday, 9:15 to 2:45, is the whole school, full-time and Collaborative together, building one thing and showing it at 2:00. Nobody is a visitor on Friday.',
           'Your child is grouped by skill, not age, and not by whether they come three days or five. A Collaborative seventh grader sits at the same table as a full-time eighth grader working the same skill.']
    o += f'''<section style="padding: {PAD} 0">
<div style="{WP}; display: flex; flex-wrap: wrap; gap: 36px 88px; align-items: flex-start">
<div style="flex: 1 1 380px; min-width: 0">
{ph2('The two things a kitchen table cannot do.', maxw='13ch')}
{psub('A seminar needs eight people who read the same thing and disagree. A lab needs equipment nobody buys for one child.', mb='0')}
</div>
<div style="flex: 1.1 1 440px; min-width: 0">
{prose(two)}<p style="margin: 8px 0 24px; font-family: {SAY}; font-style: italic; font-size: 27px; line-height: 1.3; color: {CHANNEL}">Depth with direction, three days of it.</p>
<div style="display: flex; flex-wrap: wrap; gap: 12px 36px">
{quiet('See how a day works', 'day.html')}
{quiet('Follow one Tuesday', 'day.html#tuesday')}
</div>
</div>
</div>
</section>
<section style="background: #FFFFFF; border-top: 1px solid {RULE_P}; border-bottom: 1px solid {RULE_P}; padding: {PAD} 0">
<div style="{WP}">
{ph2('The paperwork is the part we can actually take off you.', maxw='18ch')}
{psub('New York asks a homeschooling family for an IHIP, four quarterly reports, and an annual assessment. Three of those four get easier when a third of the week is documented by someone else. We write it in the form your district already reads.')}
{ledger([('Course descriptions that match the IHIP.', 'For every subject your child touches here, written in syllabus form, before you file.'), ('Hours and attendance logs, quarterly.', 'Dated, by subject, ready to paste into your quarterly report.'), ('Evidence, not grades.', 'Every six weeks your child defends a piece of work. You get the rubric, the result, and the artifact — which is exactly what an annual assessment wants to see.')])}<div style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 8px 16px; margin-top: 48px">
<span style="font-family: {SHOUT}; font-weight: 800; font-size: clamp(44px, 4.6vw, 66px); line-height: 1; letter-spacing: -0.045em">$810</span>
<span style="font-size: 17px; color: {DIM_P}">a month for founding families. Standard tuition is $900 a month, $10,800 a year, over twelve payments.</span>
</div>
<div style="margin-top: 20px">{quiet('The whole tuition table', 'join.html#tuition')}</div>
</div>
</section>
'''
    left = (faq('Do we stop being a homeschooling family?', 'No. You remain the educator of record. Your IHIP is yours, your district relationship is yours, and your child’s program is yours to set. We are three days of it, documented.', True)
            + faq('Does this fit New York’s homeschool rules?', 'Yes, and the schedule is built around the rule. New York lets a homeschooling family use group instruction for part of the program, as long as it is not the majority of it. The state asks for 900 hours a year in sixth grade and 990 in seventh and eighth. The Collaborative is about 432, so most of your child’s instruction stays with you, and so does your IHIP. If you would like your district to confirm that before you commit, we will give you the hours in writing to show them.')
            + faq('Does my child need to be vaccinated?', 'Yes. Soundline is a school, and New York’s school immunization law covers every child who attends classes in a school building, whether they come three days or five. That includes homeschooled students taking classes here. The only exemption New York allows is a medical one. We would rather you hear that from us now than find out in August.')
            + faq('Which days, and what hours?', 'Monday and Wednesday, 9:15 to 12:30. Friday, 9:15 to 2:45. Friday runs longer on purpose: the whole school builds one thing together that morning and shows it at 2:00, and your child presents with everyone else. It is the day we would ask you not to skip. Altogether that is about 432 hours a year, under half of what New York asks of a homeschooling family in any of our grades, so you stay the educator of record.')
            + faq('How many Collaborative seats are there?', 'A few alongside each grade, so every child stays known. Tell us you are interested and we will tell you exactly where you stand, by name, rather than leaving you to wonder.')
            + faq('Which grades?', 'Grades six through eight for our first year, then a grade a year through twelfth, the same as the full-time school.'))
    right = (faq('What does it cost?', 'Three days a week is $900 a month, $10,800 a year, paid over twelve months. Founding families pay $810 a month.', True)
             + faq('Can we try a term?', 'Yes. The Collaborative is enrolled by the term, not the year. Full-time enrollment is annual; three days is not, because we know you are testing whether it fits.')
             + faq('Can we move to full-time later?', 'Yes, if there is a seat, and Collaborative families get first refusal on one. Going the other way is fine too — some years need more kitchen table, not less.')
             + faq('Will our district bus my child?', 'Transportation rules are written for enrolled private school students, so a Collaborative child is a different case and it varies by district. Tell us your district and we will find out the real answer for yours before you have to ask them.')
             + faq('Does my child have to be ahead, or behind, or anything?', 'No. Grouped by skill means we meet your child where they are in each subject and move them when they have it. That is the whole design, and it is the reason mixed-background rooms work here.'))
    o += f'''<section id="questions" style="padding: {PAD} 0 {HALF}">
<div style="{WP}">
{ph2('Questions homeschooling families ask.', maxw='16ch', mb='48px')}
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(380px, 100%), 1fr)); gap: 8px 72px; align-items: start">
<div id="rules" style="min-width: 0; border-bottom: 1px solid {RULE_P}">
{left}</div>
<div id="health" style="min-width: 0; border-bottom: 1px solid {RULE_P}">
{right}</div>
</div>
</div>
</section>
'''
    o += call_section() + footer() + '</div>\n' + tail()
    return o, 0, 0


# ------------------------------------------------------------------ THE FEDERAL SCHOLARSHIP (the copy that lived on What it costs)
def scholarship():
    o = head('The federal scholarship tax credit | Soundline School') + root_open(0) + chrome('adm')
    o += page_hero('The federal scholarship tax credit, starting January 1, 2027', ['A federal scholarship starts', 'the January before we open.'],
                   'For the first time, there is federal money for private school tuition — and it arrives in the same school year your child would start here.')
    body = ['Last year’s federal tax law created a scholarship tax credit that begins <strong>January 1, 2027</strong>. It works through non-profit scholarship granting organizations: a taxpayer gives to one and takes a dollar-for-dollar credit on their federal return, up to $1,700 a person. The organization awards the money to families as tuition scholarships.',
            'Two things make this matter on the North Shore. The first is the income line: a household qualifies at or below <strong>300% of area median gross income</strong>. On Long Island the area median for a family of four runs around $164,000, which puts the ceiling near half a million dollars. This is not a low-income program here. It is most families.',
            'The second is the calendar. Each state has to opt in, and New York’s governor said on October 9 that <strong>New York will</strong>. The state’s election has to be filed with the IRS by January 1, and the list of approved organizations is due February 15 — weeks after you would be choosing a school for September.',
            'We are not going to overpromise a program that is not final. New York has announced and not yet filed. What we will do is tell you the day it is official, name the scholarship organization we work with the day the state’s list is published, and sit down with you and the actual numbers before you sign anything.']
    o += f'''<section style="padding: {PAD} 0">
<div style="{WP}; display: flex; flex-wrap: wrap; gap: 36px 88px; align-items: flex-start">
<div style="flex: 1 1 340px; min-width: 0">
{ph2('What we know so far.', maxw='12ch')}
{psub('You should not have to guess at this.', mb='0')}
</div>
<div style="flex: 1.2 1 460px; min-width: 0">
{prose(body)}</div>
</div>
</section>
<section id="donors" style="background: #FFFFFF; border-top: 1px solid {RULE_P}; border-bottom: 1px solid {RULE_P}; padding: {PAD} 0">
<div style="{WP}">
{ph2('Your federal taxes can pay for a neighbor’s seat.', maxw='18ch')}
{psub('Not a donation in the usual sense. A dollar-for-dollar federal credit of up to $1,700 a taxpayer means the money leaves your taxes instead of your pocket, and lands on a local family’s tuition. Twenty neighbors is a scholarship. A hundred is a scholarship fund.')}
{ledger([('It has to go through an approved organization.', 'Not to us. We will name the one we work with as soon as New York publishes its list.'), ('It is a credit, not a deduction.', 'Up to $1,700 a person, dollar for dollar, non-refundable, starting with the 2027 tax year.'), ('Tell us now if you are in.', 'Write to hello@soundlineschool.com and we will come back to you in January with the paperwork, not a pitch.')])}<div style="margin-top: 36px">{quiet('Write to us about the scholarship fund', 'mailto:hello@soundlineschool.com?subject=The%20scholarship%20fund')}</div>
</div>
</section>
'''
    o += call_section() + footer() + '</div>\n' + tail()
    return o, 0, 0
