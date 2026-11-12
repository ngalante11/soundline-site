"""Home, in plain language (12 Nov 2026).

Says "school" first, speaks to the parent whose kid school as usual is not reaching,
and explains every house term the first time it appears. Built by make.py as index.html.
"""
from core import *


def home_plain():
    o = head('Soundline School | A new private middle school, grades 6–8 | North Shore, Long Island') + root_open(0)
    o += chrome('home')

    # ---------------------------------------------------------------- the claim, and what we are
    o += f'''<section class="on-dark" style="background: {DEEP}; color: {PAPER}; padding: clamp(48px, 6.5vw, 96px) 0 0">
<div style="{WP}; display: flex; flex-direction: column; gap: clamp(28px, 3.4vw, 48px)">
<h1 style="margin: 0; font-family: {READ}; font-weight: 500; font-size: 15px; line-height: 1.4; color: {GLOW}">Soundline School · A new private middle school · Grades 6–8 · North Shore, Long Island</h1>
<p style="margin: 0; font-family: {SHOUT}; font-weight: 800; font-size: clamp(38px, 5vw, 74px); line-height: 1; letter-spacing: -0.045em; max-width: 21ch">
<span style="display: block; text-wrap: balance">Soundline School is a new middle school.</span>
<span style="display: block; margin-top: 0.18em; font-family: {SAY}; font-style: italic; font-weight: 400; letter-spacing: -0.02em; line-height: 1.08; color: {BEACON}; text-wrap: balance">And it is not school as usual.</span>
</p>
<div style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 28px 64px">
<p style="margin: 0; flex: 1 1 420px; min-width: 0; max-width: 640px; font-size: clamp(17px, 1.3vw, 19px); line-height: 1.55; color: {DIM_D}">Every morning there are two hours of math, reading and writing, at your child’s own level. The rest of the day is classes, labs and real projects. Every adult in the building knows your kid. Soundline is a private school for grades 6, 7 and 8, opening September 2027 on Long Island’s North Shore, most likely in Port Jefferson Station. Is your child younger or older? {quiet('Get a reminder call', '#later', dark=True)}.</p>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 16px 28px">
{btn('Ask for a call', CALL, 'beacon')}
{quiet('See what it costs', 'join.html#tuition', dark=True)}
</div>
</div>
</div>
<figure style="margin: clamp(40px, 5vw, 72px) 0 0; position: relative; height: clamp(300px, 50vw, 720px); overflow: hidden; background: {DEEP}">
<img src="{HERO}" alt="Five kids on the rocks at the edge of the Sound at sunset, in silhouette." style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 82%; display: block">
<figcaption style="position: absolute; right: 24px; bottom: 16px; font-size: 13px; color: {PAPER}; background: {DEEP}; padding: 4px 10px; border-radius: 6px">Long Island Sound, from the North Shore.</figcaption>
</figure>
</section>
'''

    # ---------------------------------------------------------------- the promise, said plainly
    figs = [('2 hours', 'of math, reading and writing, every morning',
             'Each child works at their own level, with a guide (our word for a teacher) at the table. A kid who is ahead moves ahead. A kid who is behind gets caught up. Nobody waits, and nobody gets left.'),
            ('4 hours', 'of classes, labs and projects, every day',
             'Science lab, history, books, art and music. Every six weeks your child finishes a real project and shows it to the people it was made for.'),
            ('Every adult', 'knows your kid',
             'There are ten to twelve students in a grade. One adult stays with your child for all three years, and knows what they are good at and what is hard for them.')]
    fh = ''
    for big, lab, body in figs:
        fh += (f'<div style="border-top: 1px solid {DEEP}; padding-top: 22px; display: flex; flex-direction: column; gap: 6px">\n'
               f'<span style="font-family: {SHOUT}; font-weight: 800; font-size: clamp(40px, 4.2vw, 60px); line-height: 1; letter-spacing: -0.045em">{big}</span>\n'
               f'<span style="font-family: {SAY}; font-style: italic; font-size: 21px; line-height: 1.3; color: {CHANNEL}">{lab}</span>\n'
               f'<p style="margin: 10px 0 0; font-size: 16.5px; line-height: 1.55; color: {DIM_P}; max-width: 360px">{body}</p>\n</div>\n')
    o += f'''<section style="padding: {PAD} 0 0">
<div style="{WP}">
{ph2('What makes this school different.', maxw='16ch', mb='48px')}
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr)); gap: 40px 56px">
{fh}</div>
</div>
</section>
'''

    # ---------------------------------------------------------------- the kid school isn't reaching
    kids = [('Bored.', 'They finish early and wait for the class. Here they move on the day they are ready.'),
            ('Behind, and nobody noticed.', 'Here a guide sits with them every morning, knows exactly what they can’t do yet, and works on it with them.'),
            ('Doing fine, and that’s all.', 'Good grades, no spark. Here they build things for real people and explain them out loud.'),
            ('Lost in the crowd.', 'Here there are ten to twelve kids in a grade, and the same adult looks out for yours for three years.')]
    kh = ''.join(f'<li style="border-top: 1px solid {RULE_D}; padding: 18px 0; display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 24px">\n'
                 f'<span style="flex: 1 1 220px; font-family: {SAY}; font-style: italic; font-size: 24px; line-height: 1.3; color: {BEACON}">{t}</span>\n'
                 f'<span style="flex: 1.4 1 280px; font-size: 16.5px; line-height: 1.5; color: {DIM_D}">{b}</span>\n</li>\n' for t, b in kids)
    o += f'''<section class="on-dark" style="background: {DEEP}; color: {PAPER}; padding: {PAD} 0; margin-top: {PAD}">
<div style="{WP}; display: flex; flex-wrap: wrap; align-items: center; gap: 48px 88px">
<div style="flex: 1.1 1 440px; min-width: 0; display: flex; flex-direction: column; gap: 22px">
{ph2('You know your kid. School should too.', dark=True, maxw='13ch', mb='6px')}
<p style="margin: 0; font-family: {SAY}; font-style: italic; font-size: clamp(20px, 1.9vw, 26px); line-height: 1.4; color: {DIM_D}">If one of these sounds like your house, this school was built for you.</p>
<ul style="list-style: none; margin: 8px 0 0; padding: 0; border-bottom: 1px solid {RULE_D}">
{kh}</ul>
<p style="margin: 0; font-size: 16px; color: {DIM_D}">Students with IEPs keep their district services, and we help you ask for them. Soundline is not a religious school.</p>
</div>
<div style="flex: 1 1 380px; min-width: 0; display: flex; flex-direction: column; gap: 20px">
{pic('chart', 'A 1941 nautical chart of the water off Mount Sinai: a compass rose surrounded by depth soundings.', '1 / 1', '32% 60%', 'Chart 361, Port Jefferson and Mount Sinai Harbors. U.S. Coast and Geodetic Survey, 1941.', dark=True, chart=True)}
</div>
</div>
</section>
'''

    # ---------------------------------------------------------------- the unknown future
    six = [('Learn something hard.', 'And show they really know it, not just that they sat through it.'),
           ('Make something new.', 'A video game, a robot, a short film, a song. Finished, on a deadline, for a real person in town.'),
           ('Think it through in writing.', 'Clear writing is clear thinking. They write every day.'),
           ('Stand up and explain it.', 'Every six weeks, in front of adults who ask questions. No slides.'),
           ('Do something for their town.', 'One project a year is for the community they live in.'),
           ('Know what they are good at.', 'And have a folder of real work that proves it.')]
    o += f'''<section id="future" style="padding: {PAD} 0">
<div style="{WP}">
{ph2('Nobody knows what work will look like when your child is thirty.', maxw='20ch')}
{psub('So we teach what will matter no matter what. By the end of eighth grade, a Soundline student can do six things.')}
{ledger(six)}<p style="margin: 40px 0 0; font-size: 18px; line-height: 1.6; color: {DIM_P}; max-width: 680px"><strong>What about AI?</strong> We teach it as a subject, so kids learn to use it well. It is never allowed to do their thinking for them.</p>
<div style="display: flex; flex-wrap: wrap; gap: 12px 36px; margin-top: 32px">
{quiet('More on what students learn', 'vision.html')}
{quiet('The research behind it', 'research.html')}
</div>
</div>
</section>
'''

    # ---------------------------------------------------------------- the day
    def col(title, body):
        return (f'<div>\n<h3 style="margin: 0 0 8px; font-family: {READ}; font-weight: 600; font-size: 20px; line-height: 1.3">{title}</h3>\n'
                f'<p style="margin: 0; font-size: 16.5px; line-height: 1.6; color: {DIM_P}">{body}</p>\n</div>\n')

    def dbar(name, hours, look):
        return (f'<div style="box-sizing: border-box; {look}; border-radius: 10px; padding: 8px 18px; min-height: 64px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 2px 12px">\n'
                f'<b style="font-family: {SHOUT}; font-weight: 800; font-size: 22px; letter-spacing: -0.03em">{name}</b>\n<span style="font-size: 15px">{hours}</span>\n</div>\n')
    o += f'''<section id="day" style="background: #FFFFFF; border-top: 1px solid {RULE_P}; border-bottom: 1px solid {RULE_P}; padding: {PAD} 0">
<div style="{WP}">
{ph2('What a school day looks like.', maxw='14ch')}
{psub('School runs 8:30 to 3:00, Monday to Friday.')}
<div style="display: flex; flex-wrap: wrap; gap: 40px 10px">
<div style="flex: 2 1 200px; min-width: 0; display: flex; flex-direction: column; gap: 28px">
{dbar('Morning', '8:30 to 10:30', f'background: {SHALLOWS}; color: {DEEP}')}<div style="padding-right: 22px">
{col('Math, reading and writing.', 'We call it practice. Each child works at their own level, with a guide at the table. It is hands-on. The only screen in the room is the guide’s.')}</div>
</div>
<div style="flex: 4 1 400px; min-width: 0; display: flex; flex-direction: column; gap: 28px">
{dbar('The rest of the day', '10:30 to 3:00', f'background: {MAKING}; color: {DEEP}')}{pic('woodshop', 'Illustration: a student and a woodworker measure a board together at a workbench, tools on the wall behind them.', '16 / 9', '50% 38%', 'An illustration. ' + ILLO)}
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(220px, 100%), 1fr)); gap: 24px 32px; padding-right: 22px">
{col('Classes, labs and projects.', 'We call it making. History, literature and science are taught by a person, with books, not by an app. There is lunch, time outside, and the arts every day.')}{col('Then they show it.', 'Each project lasts six weeks and is made for a real person in town. At the end your child stands up and explains it. No slides.')}</div>
</div>
<div style="flex: 2.5 1 250px; min-width: 0; display: flex; flex-direction: column; gap: 28px">
{dbar('After school', 'To 5:30, if you need it', f'border: 2px dashed {DEEP}; color: {DEEP}')}{col('Extended Day.', 'A lesson at 3:15, then a homework desk until 5:30. It costs $330 a month, and you only pay if you use it.')}</div>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 12px 36px; margin-top: 56px">
{quiet('Follow one seventh grader through a Tuesday', 'day.html#tuesday')}
{quiet('See a whole week', 'day.html#week')}
</div>
</div>
</section>
'''

    # ---------------------------------------------------------------- yes, it is a real school
    real = [('Every subject New York requires.', 'Math, English, science and history every year, plus art, music, PE and health.'),
            ('Five days a week.', 'You enroll your child and that’s it. There is no homeschool paperwork. Homeschooling families can come three days a week instead.'),
            ('Every adult is background-checked.', 'Fingerprinted through New York State, with a state and FBI check, before they start.'),
            ('We answer to New York.', 'We register with the state, and the district reviews what we teach. We are not accredited yet. That starts once we are open.'),
            ('And it is new.', 'Our first students start in September 2027, so we have no results to show you yet. We can show you the plan, the people, and the day, hour by hour.')]
    o += f'''<section id="school" style="padding: {PAD} 0 {HALF}">
<div style="{WP}">
{ph2('Yes, it’s a real school.', maxw='14ch')}
{psub('It is different on purpose. It is still a school, and it answers to New York like any other.')}
{ledger(real)}</div>
</section>
'''

    # ---------------------------------------------------------------- the people
    people = [('Founder', 'Nicole Galante, Ph.D.', 'An educator for over twenty years. She started as a classroom teacher, coached teachers in New York City schools for more than fifteen of them, and led the state team that wrote New York’s Quality Remote and Hybrid Teaching Framework and its Handbook for Virtual Schools.'),
              ('Lead guide', 'Adam King', 'A musician and teacher. He designs and runs music and STEAM programs for libraries across Long Island (escape rooms, instrument labs, world percussion) and teaches private lessons. He’ll know your child by Wednesday.'),
              ('Operations', 'Gina Dimichino', 'For more than thirty-five years she has taught dance to North Shore kids, many of them right at this age, and she has run businesses here her whole life, including her own salon. She makes sure every family feels seen, and handles every detail in between.'),
              ('Academic systems', 'Izzy Galante', 'Designs how the school teaches: what comes first, how we know a child is ready to move on, and how we know it worked. Co-wrote New York’s Quality Remote and Hybrid Teaching Framework and its Handbook for Virtual Schools. Teaches a live class every week.')]
    pp = ''
    for role, name, bio in people:
        pp += (f'<div style="border-top: 1px solid {DEEP}; padding-top: 20px">\n{ital(role, CHANNEL, "18px", "4px")}\n'
               f'<h3 style="margin: 0 0 10px; font-family: {SHOUT}; font-weight: 800; font-size: 24px; line-height: 1.05; letter-spacing: -0.035em">{name}</h3>\n'
               f'<p style="margin: 0; font-size: 15.5px; line-height: 1.55; color: {DIM_P}">{bio}</p>\n</div>\n')
    o += f'''<section style="padding: {HALF} 0 {PAD}">
<div style="{WP}">
{ph2('The people starting it.', maxw='14ch', mb='48px')}
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(240px, 100%), 1fr)); gap: 44px 32px">
{pp}</div>
<p style="margin: 48px 0 14px; font-size: 17px; color: {DIM_P}; max-width: 640px">We are hiring a math and science guide and a humanities guide for September 2027. You will meet them before the first day.</p>
<div>{quiet('More about us', 'about.html')}</div>
</div>
</section>
'''

    # ---------------------------------------------------------------- the price
    a = track(CHANNEL, 'Five days a week', 'The full school.', 'Monday to Friday, 8:30 to 3:00. You enroll, and that’s it.', '$1,350', 'a month for founding families, the first to join. The regular price is $1,500.')
    b = track(SHALLOWS, 'Three days a week', 'For homeschooling families.', 'Monday, Wednesday and Friday. We call it the Collaborative. You stay your child’s teacher, and we hand you course descriptions and hours logs for your district reports.', '$810', 'a month for founding families. The regular price is $900.')
    o += f'''<section id="cost" style="background: #FFFFFF; border-top: 1px solid {RULE_P}; border-bottom: 1px solid {RULE_P}; padding: {PAD} 0">
<div style="{WP}">
{ph2('What it costs.', maxw='14ch')}
{psub('The price is published, all of it. There is no application fee and no materials fee.')}
<div style="display: flex; flex-wrap: wrap; gap: 56px 96px">
{a}{b}</div>
<p style="margin: 48px 0 0; font-size: 17px; line-height: 1.6; color: {DIM_P}; max-width: 680px">Founding families keep their price for as long as their child is enrolled. Tuition is paid monthly, over twelve months.</p>
<div style="display: flex; flex-wrap: wrap; gap: 12px 36px; margin-top: 28px">
{quiet('See every price', 'join.html#tuition')}
{quiet('How three days a week works', 'collaborative.html')}
</div>
</div>
</section>
'''

    # ---------------------------------------------------------------- how to start
    def pstep(n, title, body, cta):
        return (f'<li style="min-width: 0; border-top: 1px solid {PAPER}; padding: 24px 0 0; display: flex; flex-direction: column; gap: 12px">\n'
                f'<span style="font-family: {SHOUT}; font-weight: 800; font-size: 66px; line-height: 0.9; letter-spacing: -0.045em; color: {BEACON}">{n}</span>\n'
                f'<h3 style="margin: 6px 0 0; font-family: {SHOUT}; font-weight: 800; font-size: 26px; line-height: 1.05; letter-spacing: -0.035em">{title}</h3>\n'
                f'<p style="margin: 0 0 8px; font-size: 16.5px; line-height: 1.6; color: {DIM_D}; flex: 1 0 auto; max-width: 340px">{body}</p>\n<div>{cta}</div>\n</li>\n')
    steps = (pstep('1', 'Call us.', 'Twenty minutes on the phone with one of the four of us. Ask anything, including about money.', btn('Ask for a call', CALL, 'beacon', small=True))
             + pstep('2', 'Look at the price.', 'All of it is published. You see what it costs before anyone asks you for anything.', quiet('See what it costs', 'join.html#tuition', dark=True))
             + pstep('3', 'Hold a seat.', '$500 holds your child’s seat. It is kept by an independent escrow agent, not by us. You get all of it back, for any reason, until the day we sign a lease.', '<span style="font-size: 16px; color: ' + DIM_D + '">We set it up with you on the call.</span>'))
    perks = ['Reserved seats at every student show.', 'A first look at each new project before it starts.', 'Brothers and sisters go first when a grade fills.', 'Your family’s name on the founders’ wall.']
    perk_html = ''.join('<li style="border-top: 1px solid ' + RULE_D + '; padding: 14px 0; font-size: 17px; color: ' + PAPER + '">' + x + '</li>\n' for x in perks)
    o += f'''<section id="founding" class="on-dark" style="background: {DEEP}; color: {PAPER}; padding: {PAD} 0">
<div style="{WP}">
{ph2('How to start.', dark=True, maxw='14ch')}
{psub('We are signing up our first families now. We call them Founding Families, and they get the lower price for good.', dark=True, mb='64px')}
<ol style="list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr)); gap: 48px 56px">
{steps}</ol>
<figure style="margin: clamp(64px, 8vw, 112px) 0; display: flex; flex-direction: column; gap: 18px">
<blockquote style="margin: 0; font-family: {SAY}; font-style: italic; font-size: clamp(30px, 3.9vw, 56px); line-height: 1.15; letter-spacing: -0.015em; color: {BEACON}; max-width: 19ch; text-wrap: balance">“This is the answer to my prayers for my daughter.”</blockquote>
<figcaption style="font-size: 15px; color: {DIM_D}">A parent, November 2026</figcaption>
</figure>
<div style="display: flex; flex-wrap: wrap; gap: 36px 96px; padding-top: 40px; border-top: 1px solid {PAPER}">
<div style="flex: 1 1 380px; min-width: 0">
<h3 style="margin: 0 0 14px; font-family: {SHOUT}; font-weight: 800; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.02; letter-spacing: -0.04em">Founding families help shape the school.</h3>
<p style="margin: 0 0 14px; font-size: 17px; line-height: 1.6; color: {DIM_D}; max-width: 480px">They sit on the Family Council. The Council helps pick the projects students take on, and brings people from town into the school. It does the fun things. It never fundraises.</p>
<p style="margin: 0; font-family: {SAY}; font-style: italic; font-size: 21px; line-height: 1.4; color: {PAPER}; max-width: 480px">Each grade has ten to twelve seats. They fill in the order families reserve. We will tell you where you stand before you pay anything.</p>
</div>
<div style="flex: 1 1 340px; min-width: 0">
{ital('Founding families also get', GLOW, '20px', '10px')}
<ul style="list-style: none; margin: 0; padding: 0; border-bottom: 1px solid {RULE_D}">
{perk_html}</ul>
</div>
</div>
</div>
</section>
'''

    # ---------------------------------------------------------------- questions
    left = (faq('Is this a real school or a homeschool program?', 'It is a school. Your child is enrolled here five days a week, we teach every subject New York requires, and you file no homeschool paperwork. We also run a separate three-day program for families who homeschool.', True)
            + faq('What subjects are taught?', 'Math, English, science and history every year, with art, music, physical education and health. Math, reading and writing happen every morning at each child’s level. History, literature and science are taught around a table and in the lab.')
            + faq('Do students take the state tests?', 'Yes. The state tests are in the spring and take three mornings. We do not do test prep. New York uses the tests to check that a new school is teaching what it should. All year long you will also see how much your own child has grown, three times a year.')
            + faq('What happens after eighth grade?', 'Ninth grade opens here in September 2028, then a grade every year through twelfth. Your child can stay, or move on with a folder of real work that shows what they can do.'))
    right = (faq('Where will the school be?', 'On the North Shore, along the Miller Place–Port Jefferson Station corridor. Port Jefferson Station is the likeliest. We announce the address the day we sign the lease.', True)
             + faq('How do I apply?', 'Ask for a call. It is twenty minutes with one of the four of us, and there is no application fee. If it’s a fit, $500 holds a seat, and the enrollment contract follows.')
             + faq('What if the school doesn’t open?', 'You get your money back. Your $500 is kept by an independent escrow agent, not by us, and it comes back in full, for any reason, until the day we sign a lease. If the school doesn’t open after that, we mail you a check.')
             + faq('Will our district bus my child?', 'Most likely. New York districts bus students to private schools up to fifteen miles away. You ask your own district by April 1, and we send you the request already filled in.'))
    o += f'''<section id="questions" style="padding: {PAD} 0 {HALF}">
<div style="{WP}">
{ph2('Questions parents ask.', maxw='14ch', mb='48px')}
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(380px, 100%), 1fr)); gap: 8px 72px; align-items: start">
<div style="min-width: 0; border-bottom: 1px solid {RULE_P}">
{left}</div>
<div style="min-width: 0; border-bottom: 1px solid {RULE_P}">
{right}</div>
</div>
<div style="margin-top: 36px">{quiet('Every question, with prices', 'join.html#questions')}</div>
</div>
</section>
'''

    o += later_section()
    o += call_section('home')
    o += footer() + '</div>\n' + tail()
    return o, 0, 0
