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
<span style="display: block; text-wrap: balance">Mornings are for skills.</span>
<span style="display: block; font-family: {SAY}; font-style: italic; font-weight: 400; letter-spacing: -0.02em; line-height: 1.08; color: {BEACON}; text-wrap: balance">The rest of the day is for real work.</span>
</p>
<p style="margin: 0; max-width: 640px; font-size: clamp(17px, 1.3vw, 19px); line-height: 1.55; color: {DIM_D}">Every morning there are two hours of math, reading and writing, each child at their own level. We call it practice. The rest of the day is classes, labs and projects. We call it making. School ends at 3:00, and your child can stay until 5:30 if you need it.</p>
<div aria-label="The school day" style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 12px">
<div style="flex: 2 1 200px; min-width: 0">{bar('Practice', '8:30 to 10:30', f'background: {SHALLOWS}; color: {DEEP}')}</div>
<div style="flex: 4 1 400px; min-width: 0">{bar('Making', '10:30 to 3:00', f'background: {MAKING}; color: {DEEP}')}</div>
<div style="flex: 2.5 1 250px; min-width: 0">{bar('Extended Day', 'To 5:30, if you need it', f'border: 2px dashed {PAPER}; color: {PAPER}')}</div>
</div>
</div>
</section>
'''
    entries = [
        ('8:30', 'Arrival', None, 'The door.', 'The same adult greets them every morning. Bag on the hook, phone in the box, a word about the weekend.'),
        ('8:45', 'Morning meeting', None, 'Fifteen minutes with their guide.', 'A guide is our word for a teacher. Ten to twelve students meet with the guide who stays with them for three years. Each sets a goal for the day. Today’s: pass the check on proportions, and draft a question for science lab.'),
        ('9:00', 'Practice, 50 min', 'p', 'Math, at their own level.', 'A student moves to the next skill when they can show a guide they have it, not when the calendar says so. Across the table, a sixth grader is working on a skill this student passed in week one. Beside them, an eighth grader is on one they will reach by winter.'),
        ('9:50', 'Practice, 40 min', 'p', 'Reading and writing.', 'Today they read about how ice carved Long Island Sound, because science lab needs it. Then they write two paragraphs. One has to make an argument.'),
        ('10:30', 'Whole school, 30 min', 'p', 'Everyone together. Today, math.', 'Every morning at 10:30 the whole school sits down with one real problem from town and talks it through. We call it seminar. Tuesday is math. One student proves why a shortcut works. This student finds the case where it doesn’t, on the fourth try.'),
        ('11:00', 'Outside, 40 min', None, 'Lunch and outside.', 'Kids go outside every day, whatever the weather. A guide learns a lot about a student out here.'),
        ('11:40', 'Science lab, 95 min', 'm', 'Building a depth sensor.', 'They are building a sensor on a line that measures how deep a tank of water is. Today they test it, and the graph bends where it shouldn’t. On Friday they explain why, out loud.'),
        ('1:15', 'Project time, 60 min', 'm', 'The six-week project.', 'We call it a Quest. This is week three of six. The children’s librarian asked for an exhibit on how sound travels through water. The group has a plan, forty dollars, and a speaker that won’t stay sealed. A guide is in the room and does not fix it for them.'),
        ('2:15', 'Music, 45 min', 'm', 'The school band.', 'Everyone plays something. Nobody has to be good yet. This student has the bass part.'),
        ('3:00', 'To 5:30, if you need it', 'x', 'Home, or Extended Day.', 'Pickup is at 3:00. Or your child stays: a lesson at 3:15, then a homework desk until 5:30. The project stays at school.'),
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
{ph2('One seventh grader’s Tuesday, hour by hour.', maxw='13ch')}
{psub('This is a Tuesday in September, the way we plan to run it. We follow one student from the door to pickup. There is no name, because our first students start in September 2027.', mb='0')}
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
{ledger([('Practice: two hours.', 'Ninety minutes of math, reading and writing at their own level, then thirty minutes talking a problem through together. It is hands-on, at a table with a guide. The only screen in the morning belongs to the guide.'), ('Making: four hours.', 'Science lab, the project, music, and lunch with forty minutes outside. It is taught by a person, and the project is built for someone who asked for it.'), ('Where it was hard.', 'The fourth try at 10:30, and the graph that has to be explained on Friday. The guide knows which one was hard for this student.'), ('What they keep.', 'The math skill, if they passed it. The paragraph. The graph. Every student keeps a folder of real work. By eighth grade it shows what they can do. This Tuesday is one page of it.')])}</div>
</section>
'''
    week = [('Monday', 'The plan', 'At 8:45 each student sets one goal and one plan for the week.', False),
            ('Tuesday', 'Science lab, then projects', 'Ninety minutes of hands-on science, written up before they leave the lab. Then everyone works on their project: a video game, a robot, a portrait, a sculpture, a song.', False),
            ('Wednesday', 'Books', 'The long discussion of the week: a novel, a question, and a paragraph. Every discussion ends in writing.', False),
            ('Thursday', 'Apprenticeships', 'Seventh and eighth graders work alongside an adult who does a job for a living. Sixth graders work on their project.', False),
            ('Friday', 'One big build, then the show', 'The whole school builds one thing together: a song, a mural, a project for someone in town. At 2:00 students present their work and something is performed. It is usually loud. Families are welcome.', True)]
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
{psub('The schedule is the same every week, so the work can change. Every morning at 10:30 the whole school sits down together with one real problem from town.', mb='0')}
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
{ph2('Be one of our first families.', dark=True, maxw='14ch')}
<p style="margin: 0; font-family: {SAY}; font-style: italic; font-size: clamp(20px, 1.9vw, 27px); line-height: 1.4; color: {DIM_D}; max-width: 640px">Founding Families pay less, keep that price for as long as their child is enrolled, and help shape the school.</p>
</div>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 16px 28px">
{btn('Ask for a call', CALL, 'beacon')}
{quiet('See what it costs', 'join.html#tuition', dark=True)}
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
<p style="margin: 0; font-family: {SHOUT}; font-weight: 800; font-size: clamp(40px, 5.4vw, 80px); line-height: 0.98; letter-spacing: -0.045em; max-width: 19ch; text-wrap: balance">Here is what it costs.</p>
<p style="margin: 0; font-family: {SAY}; font-style: italic; font-size: clamp(22px, 2.3vw, 33px); line-height: 1.3; color: {BEACON}">You see every price before anyone asks you for anything.</p>
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
                + srow('Founding Families', f[0], f[1], '44px', True) + srow('Regular price', s[0], s[1], '28px') + '</div>\n')
    stack = ('<div class="only-narrow">\n<p style="margin: 0 0 20px; font-size: 15px; color: ' + DIM_P + '">Prices are per month, paid over twelve months. Founding Families are the first families to join. They pay 10% less and keep that price through twelfth grade.</p>\n'
             + scard(CHANNEL, 'The School', 'Five days a week, 8:30 to 3:00', ('$1,350', '$16,200 a year'), ('$1,500', '$18,000 a year'))
             + scard(SHALLOWS, 'The Collaborative', 'Three days a week, for homeschooling families', ('$810', '$9,720 a year'), ('$900', '$10,800 a year'))
             + '</div>\n')
    details = [('What’s included', 'Everything in the school day: classes, science labs, projects, art and music. There is no materials fee.'),
               ('Extended Day', 'After school, 3:00 to 5:30, for five-day students. It is $330 a month over twelve months, or $297 for Founding Families. You pay only if you use it.'),
               ('Two kids', 'The second child is 10% off.'),
               ('Class size', 'Ten to twelve students in a grade. One adult stays with your child for all three years.'),
               ('Paying in full', 'Pay for the whole year by March 1 and take another 3% off.'),
               ('No application fee', 'It costs nothing to apply. Anything you pay now counts toward tuition.')]
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
<span style="font-size: 15px; color: {DIM_P}">The first families to join. 10% off, and you keep that price through twelfth grade.</span>
</div>
<div role="cell" style="padding: 34px 24px 34px 0">{fig('$1,350', '$16,200 a year', BIG)}</div>
<div role="cell" style="padding: 34px 24px 34px 0">{fig('$810', '$9,720 a year', BIG)}</div>
</div>
<div role="row" style="display: grid; {cols}; align-items: center; border-top: 1px solid {RULE_P}">
<div role="rowheader" style="padding: 26px 24px 26px 0">
<span style="display: block; font-family: {SAY}; font-style: italic; font-size: 22px; line-height: 1.2; color: {DIM_P}">Regular price</span>
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
{ph2('What you pay, and when.', dark=True, maxw='14ch')}
{psub('There are no extra fees. Each payment counts toward the next one.', dark=True, mb='64px')}
<ol style="list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr)); gap: 48px 56px">
{chain('$500', 'Holds a seat.', 'It is kept by an independent escrow agent, not by us. You get all of it back, for any reason, until the day we sign a lease.', True)}{chain('$2,500', 'Your deposit.', 'This is due when you sign the enrollment contract. Your $500 counts toward it. You will know the school’s address before we ask for it.')}{chain('Tuition', 'Twelve monthly payments.', 'Your deposit counts toward tuition. Monthly payments start the summer before school opens. You do not owe two big payments in August and January.')}</ol>
<p style="margin: 64px 0 0; font-family: {SAY}; font-style: italic; font-size: clamp(21px, 2vw, 27px); line-height: 1.4; color: {PAPER}; max-width: 760px">If the school doesn’t open, your money comes back. We mail you a check.</p>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 16px 28px; margin-top: 44px">
{btn('Ask for a call', CALL, 'beacon')}
<span style="font-size: 16px; color: {DIM_D}; max-width: 520px">It starts with a twenty-minute call. Each grade has ten to twelve seats, and they fill in the order families reserve.</span>
</div>
</div>
</section>
'''
    dates = [('Nov 12', 'Prices are published. Sign-up opens for our first families.', True),
             ('Dec 12', 'Information night, Saturday. Details to follow.', False),
             ('Jan 14', 'Information night. Details to follow.', False),
             ('Mar 1', 'The last day to pay for the whole year and take 3% off.', False),
             ('Apr 1', 'Your bus request to your own district is due. We send you the form already filled in.', False),
             ('Jun 1', 'If your child has an IEP, your request for services is due to the district. We help you with it.', False),
             ('Aug 2027', 'Sign-up opens for September 2028.', False),
             ('Sept 2027', 'The first day of school.', False)]
    dt = ''
    for d, t, now in dates:
        top = f'8px solid {BEACON}' if now else f'1px solid {DEEP}'
        pt = '13px' if now else '20px'
        dt += (f'<li style="border-top: {top}; padding: {pt} 18px 0 0; min-width: 0">\n'
               f'<time style="display: block; font-family: {SHOUT}; font-weight: 800; font-size: 26px; letter-spacing: -0.035em; line-height: 1.1; margin-bottom: 8px">{d}</time>\n'
               f'<span style="font-size: 15.5px; line-height: 1.5; color: {DIM_P}">{t}</span>\n</li>\n')
    o += f'''<section style="padding: {PAD} 0 {HALF}">
<div style="{WP}">
{ph2('Dates to know.', maxw='14ch', mb='56px')}
<ol style="list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(150px, 100%), 1fr)); gap: 36px 0">
{dt}</ol>
</div>
</section>
'''
    money = (faq('What is a Founding Family?', 'One of the first families to join. Founding Families pay 10% less, and the price they start at is the price they pay every year their child is here, through twelfth grade. It does not go up when our costs go up, and it does not go up when the school fills.', True)
             + faq('How is it paid?', 'Monthly, over twelve months, starting the summer before school opens. You do not owe two big payments in August and January.')
             + faq('What if the school doesn’t open?', 'You get your money back. Your $500 comes back in full, for any reason, until the day we sign a lease. If the school doesn’t open after that, we mail you a check.')
             + faq('Is there financial aid?', 'Not yet. We do not have a scholarship fund, and we will not promise one before it exists. Scholarships are a goal for us. If cost is the question for you, tell us. It does not count against your child, and it tells us how much help families need.')
             + faq('Is the bus really free?', 'In most cases, yes. Your own district buses students to private schools up to fifteen miles from home, and the district pays for it. You have to ask by April 1. We send you the form already filled in.'))
    school = (faq('How many students will there be?', 'Ten to twelve in a grade. Nobody is stuck in their grade, because students work at their own level across the school. On Fridays the whole school builds one thing together. It is few enough that no child gets overlooked, and enough for a real class discussion.', True)
              + faq('Where will the school be?', 'On the North Shore, along the Miller Place–Port Jefferson Station corridor. Port Jefferson Station is the likeliest. We announce the address the day we sign the lease.')
              + faq('What about high school?', 'Ninth grade opens here in September 2028. Then we add a grade every year through twelfth. New York has decided a diploma should stand for six things a graduate can do, not only test scores. Your child practices all six here, every six weeks.')
              + faq('How much screen time is there?', 'Very little. Morning math, reading and writing are hands-on, at a table with a guide (our word for a teacher). The only screen in the morning belongs to the guide. Class discussions, science lab and presentations happen without screens. AI is taught as a subject. It is never used as a shortcut.'))
    ny = (faq('Is Soundline approved by New York?', 'New York does not license private schools. A private school registers with the state, and the local district reviews what it teaches. We do both. We are not accredited yet. We start that process once we are open.', True)
          + faq('Do students take the state tests?', 'Yes. The state tests are in the spring and take three mornings. We do not do test prep. New York uses the tests to check that a new school is teaching what it should. All year long you will also see how much your own child has grown, three times a year.')
          + faq('How do you screen the adults who work with my child?', 'Every adult who works with students is fingerprinted through the New York State Education Department before they start, and is checked against the sex offender registry. Everyone completes mandated reporter training. There are always at least two adults in the building.')
          + faq('My child has an IEP. What happens to services?', 'Your child can still receive services from the public school district. You request them from the district where the school is located by June 1, and we’ll help you do it.'))

    def group(title, body):
        return (f'<div style="min-width: 0; border-bottom: 1px solid {RULE_P}">\n{ital(title, CHANNEL, "24px", "14px")}\n{body}</div>\n')
    o += f'''<section id="questions" style="padding: {HALF} 0 {HALF}">
<div style="{WP}">
{ph2('Questions parents ask.', maxw='14ch', mb='56px')}
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(320px, 100%), 1fr)); gap: 48px 56px; align-items: start">
{group('Money', money)}{group('The school', school)}{group('New York', ny)}</div>
</div>
</section>
'''
    o += f'''<section id="scholarship" style="background: #FFFFFF; border-top: 1px solid {RULE_P}; border-bottom: 1px solid {RULE_P}; padding: {HALF} 0">
<div style="{WP}; display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px 64px">
<div style="flex: 1 1 460px; min-width: 0">
<h2 style="margin: 0 0 12px; font-family: {SHOUT}; font-weight: 800; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.02; letter-spacing: -0.04em; max-width: 22ch">A new federal scholarship may help with tuition.</h2>
<p style="margin: 0; font-size: 17px; line-height: 1.6; color: {DIM_P}; max-width: 640px">A federal tax credit for private school scholarships begins January 1, 2027. New York has said it will take part and has not filed yet. Nothing is final. We wrote up what we know.</p>
</div>
{quiet('The federal scholarship, in full', 'scholarship.html')}
</div>
</section>
'''
    o += later_section()
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
{ph2('Be one of our first families.', dark=True, maxw='14ch')}
<p style="margin: 0; font-family: {SAY}; font-style: italic; font-size: clamp(20px, 1.9vw, 27px); line-height: 1.4; color: {DIM_D}; max-width: 640px">Founding Families pay less, keep that price for as long as their child is enrolled, and help shape the school.</p>
</div>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 16px 28px">
{btn('Ask for a call', CALL, 'beacon')}
{quiet('See what it costs', 'join.html#tuition', dark=True)}
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
          ('Academic systems', 'Izzy Galante', 'Designs how the school teaches: what comes first, how we know a child is ready to move on, and how we know it worked. Co-wrote New York’s Quality Remote and Hybrid Teaching Framework and its Handbook for Virtual Schools. Teaches a live class every week.')]


# ------------------------------------------------------------------ OUR VISION
def vision():
    o = head('Our vision | Soundline School, private middle school on Long Island’s North Shore') + root_open(0) + chrome('vision')
    six = [('Learn something hard.', 'And show they really know it.'), ('Make something new.', 'For a real person in town, on a deadline.'), ('Think it through in writing.', 'Clear writing is clear thinking.'),
           ('Stand up and explain it.', 'To adults who ask questions. No slides.'), ('Do something for their town.', 'One project a year is for the community.'), ('Know what they are good at.', 'And where they want to go next.')]
    sx = ''.join(f'<li style="border-top: 1px solid {RULE_D}; padding: 22px 0 6px">\n'
                 f'<h2 style="margin: 0 0 6px; font-family: {SHOUT}; font-weight: 800; font-size: clamp(24px, 2.4vw, 33px); line-height: 1.05; letter-spacing: -0.04em; color: {PAPER}">{t}</h2>\n'
                 f'<p style="margin: 0; font-size: 17px; color: {DIM_D}">{b}</p>\n</li>\n' for t, b in six)
    extra = f'''<ol style="list-style: none; margin: 12px 0 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr)); gap: 12px 56px">
{sx}</ol>
<p style="margin: 28px 0 0; font-family: {SAY}; font-style: italic; font-size: clamp(22px, 2.3vw, 33px); line-height: 1.3; color: {BEACON}; max-width: 760px">New York has decided a diploma should stand for six things a graduate can do, not only test scores. We built the school around those six.</p>
<p style="margin: 0; max-width: 640px; font-size: 18px; color: {DIM_D}">Every six weeks your child adds real work to a folder: something they made, something they explained out loud, and proof that they grew. By eighth grade the folder shows what they can do.</p>
'''
    o += page_hero('Our vision · What a Soundline student can do by eighth grade', ['By eighth grade, a student who can:'], extra=extra)
    o += f'''<section style="padding: {PAD} 0 {HALF}">
<div style="{WP}">
{ph2('How you’ll know it’s working.', maxw='14ch', mb='48px')}
{ledger([('We test growth three times a year.', 'Every student takes a test called NWEA MAP in fall, winter and spring. We publish how much the whole school grew, counting every student. No child’s score is public. Your child’s comes home to you.'), ('You will see the work.', 'The robot, the performance, and your child explaining how they did it.'), ('We teach AI as a subject.', 'Kids learn to use it well. It is never allowed to do their thinking for them.'), ('We answer to New York.', 'We register with the state, and the district reviews what we teach. We are not accredited yet. That starts once we are open.')])}</div>
</section>
<section style="padding: {HALF} 0 {PAD}">
<div style="{WP}">
{ph2('Each part has been studied for decades. Putting them in one school is new.', maxw='20ch', mb='48px')}
{ledger([('A child moves on when they have it.', 'More than a hundred studies show this works better than moving the whole class on a schedule. Students who struggle gain the most.'), ('Long projects raise test scores.', 'In controlled studies, students who learned through long projects scored higher on state tests than students taught the usual way.'), ('Writing and talking make it stick.', 'Students remember what they have to write about and explain out loud.'), ('Kids work harder for an adult who knows them.', 'One close relationship with a teacher is among the strongest predictors of how hard a student tries, and it matters more as kids get older. That is why one adult stays with your child for three years.')])}<div style="display: flex; flex-wrap: wrap; gap: 12px 36px; margin-top: 36px">
{quiet('The research, with sources', 'research.html')}
{quiet('The people starting it', 'about.html#people')}
</div>
</div>
</section>
'''
    o += founding_plate() + footer() + '</div>\n' + tail()
    return o, 0, 0


# ------------------------------------------------------------------ ABOUT US
def about():
    o = head('About us | Soundline School, private middle school on Long Island’s North Shore') + root_open(0) + chrome('about')
    o += page_hero('About Soundline School, a new private middle school', ['Every adult here', 'knows your kid.'], 'There are ten to twelve students in a grade. One adult stays with your child for three years. And the four people starting the school will know your child by name.')
    story = ['Before sonar, sailors dropped a sounding line over the side of the boat. It was a rope with a lead weight on the end, and it told them how deep the water was. A dab of grease on the weight brought up a bit of the bottom (sand, shell, mud), so they knew what was down there too. Only then did they pick a direction.',
             'That is how we get to know your child. We find out where they really are in each subject. We also find out what they love, and how far it goes. Middle schoolers do well when an adult truly knows what they need.',
             'Then we pick a direction together. What your child loves becomes part of the work: the next skill, the next project, the next thing worth showing their classmates and their town. That gives a student more than a grade on a report card.',
             'We teach everything New York requires. What we learn about your child is what we build on.']
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
{ph2('Where the name comes from.', maxw='12ch', mb='28px')}
{prose(story)}<p style="margin: 8px 0 0; font-family: {SAY}; font-style: italic; font-size: 27px; line-height: 1.3; color: {CHANNEL}">Depth with direction.</p>
</div>
</div>
</section>
<section style="background: #FFFFFF; border-top: 1px solid {RULE_P}; border-bottom: 1px solid {RULE_P}; padding: {PAD} 0">
<div style="{WP}">
{ph2('Ten to twelve in a grade, and nobody is stuck in it.', maxw='16ch')}
{psub('Students work at their own level across the school, and on Fridays the whole school builds one thing together. It is few enough that no child gets overlooked, and enough for a real class discussion.')}
{ledger([('One adult for three years.', 'Every student has the same guide (our word for a teacher) looking out for them from the day they start, in a group of ten to twelve.'), ('Each child works at their own level.', 'A sixth grader and an eighth grader can work on the same skill at the same table. Each moves on when they have it.'), ('Three grades, one building.', 'We add a grade every year through twelfth, starting with ninth in September 2028. Older students spend part of the week out in town, working alongside adults.')])}</div>
</section>
<section id="people" style="padding: {PAD} 0">
<div style="{WP}">
{ph2('The people starting it.', maxw='14ch', mb='48px')}
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
    extra = f'''<p style="margin: 0; max-width: 640px; font-size: 17px; color: {GLOW}">You keep your own homeschool plan and file your own reports. We hand you course descriptions and hours logs to go with them.</p>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 14px 28px; margin-top: 8px">
{btn('Ask for a call', CALL, 'beacon')}
<span style="font-size: 16px; color: {DIM_D}; max-width: 460px">Tell us you homeschool. We run the Collaborative conversation separately, and we will write back ourselves.</span>
</div>
'''
    o += page_hero('The Collaborative · A three-day homeschool program for grades 6–8 on Long Island’s North Shore',
                   ['You keep teaching your child.', 'We take Monday, Wednesday, Friday.'],
                   'The Collaborative is Soundline School three days a week, for homeschooling families on the North Shore. Your child has the same guides (our word for teachers), the same rooms and the same Friday project as the full-time students. The rest of the week, your child is home with you.', extra)
    two = ['Most families who homeschool a twelve-year-old are not short on instruction. They are short on two specific things: a room of peers who will argue with your child about a book, and a workshop with tools in it.',
           'That is what the three days are for. Monday and Wednesday, 9:15 to 12:30, are math, writing and the long project, at a table with a guide who knows exactly where your child is. Friday, 9:15 to 2:45, is the whole school together, full-time and three-day students, building one thing and showing it at 2:00. Nobody is a visitor on Friday.',
           'Your child works at their own level, whatever their age and whether they come three days or five. A three-day seventh grader sits at the same table as a full-time eighth grader working on the same skill.']
    o += f'''<section style="padding: {PAD} 0">
<div style="{WP}; display: flex; flex-wrap: wrap; gap: 36px 88px; align-items: flex-start">
<div style="flex: 1 1 380px; min-width: 0">
{ph2('The two things a kitchen table cannot do.', maxw='13ch')}
{psub('A good discussion needs eight kids who read the same book and disagree. A science lab needs equipment nobody buys for one child.', mb='0')}
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
{ledger([('Course descriptions that match the IHIP.', 'For every subject your child touches here, written in syllabus form, before you file.'), ('Hours and attendance logs, quarterly.', 'Dated, by subject, ready to paste into your quarterly report.'), ('Real work, not just grades.', 'Every six weeks your child presents a piece of work and answers questions about it. You get the scoring sheet, the result and the work itself. That is exactly what an annual assessment asks for.')])}<div style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 8px 16px; margin-top: 48px">
<span style="font-family: {SHOUT}; font-weight: 800; font-size: clamp(44px, 4.6vw, 66px); line-height: 1; letter-spacing: -0.045em">$810</span>
<span style="font-size: 17px; color: {DIM_P}">a month for Founding Families, the first to join. The regular price is $900 a month, $10,800 a year, paid over twelve months.</span>
</div>
<div style="margin-top: 20px">{quiet('See every price', 'join.html#tuition')}</div>
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
             + faq('Can we move to full-time later?', 'Yes, if there is a seat, and Collaborative families get first refusal on one. Going the other way is fine too. Some years need more kitchen table, not less.')
             + faq('Will our district bus my child?', 'Transportation rules are written for enrolled private school students, so a Collaborative child is a different case and it varies by district. Tell us your district and we will find out the real answer for yours before you have to ask them.')
             + faq('Does my child have to be ahead, or behind, or anything?', 'No. We find out where your child is in each subject and move them on when they have it. That is how the whole school works, and it is why kids from different backgrounds learn well in the same room.'))
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
    o += page_hero('The federal scholarship tax credit, starting January 1, 2027', ['A new federal scholarship', 'may help with tuition.'],
                   'A federal tax credit for private school scholarships starts January 1, 2027. Here is what we know so far, and what is still not decided.')
    body = ['A 2025 federal tax law created a scholarship tax credit that begins <strong>January 1, 2027</strong>. It works through non-profit groups called scholarship granting organizations. A taxpayer gives to one of these groups and gets the same amount taken off their federal taxes, up to $1,700 a person. The group then gives the money to families as tuition scholarships.',
            'Many North Shore families would qualify. A household qualifies if it earns up to <strong>300% of the area’s median income</strong>. On Long Island the median for a family of four is around $164,000, so the limit is close to half a million dollars. Here, this is not only a program for low-income families.',
            'The timing is tight. Each state has to choose to take part. New York’s governor said on October 9 that <strong>New York will</strong>. The state has to file that choice with the IRS by January 1, and its list of approved scholarship groups is due February 15. That is a few weeks after you would be choosing a school for September.',
            'We will not promise what is not final. New York has announced its choice and has not filed it yet. No scholarship group is working with us yet, and we do not have a scholarship fund of our own. Scholarships are a goal for us, not a promise. We will tell you the day anything is official, and we will go through the real numbers with you before you sign anything.']
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
{ph2('If you would like to help a local family.', maxw='18ch')}
{psub('Under the new credit, a taxpayer can give up to $1,700 to an approved scholarship group and take the same amount off their federal taxes. The money goes to families as tuition scholarships.')}
{ledger([('The gift goes to an approved group, not to us.', 'The group decides who gets a scholarship. A gift cannot be set aside for one particular child.'), ('It comes straight off the tax you owe.', 'It is a credit, not a deduction: up to $1,700 a person, starting with the 2027 tax year.'), ('Nothing is set up yet.', 'New York has not published its list of approved groups. If you want to hear when there is a way to give, write to hello@soundlineschool.com and we will tell you.')])}<div style="margin-top: 36px">{quiet('Write to us about scholarships', 'mailto:hello@soundlineschool.com?subject=Scholarships')}</div>
</div>
</section>
'''
    o += call_section() + footer() + '</div>\n' + tail()
    return o, 0, 0
