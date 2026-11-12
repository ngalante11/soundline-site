# soundlineschool.com: tokens, shared pieces and the Home page.
# The pages are generated: edit here (and pages.py), then run  python3 tools/site/make.py  from the repo root.
# Styles are inline on purpose, so each page is one self-contained file; premium.css carries only what
# inline styles cannot (the phone menu, the sticky bar, focus rings).
# Brand Guide: Deep Sound, Chart Paper and Beacon carry the page; Shallows and Making appear in the day bar only.
import os, json

HERO = 'img/hero-sound.jpg'

DEEP, BEACON, CHANNEL, SHALLOWS, GLOW, PAPER, MAKING = '#12222B', '#F2C14E', '#1B4B6E', '#5FB4E6', '#7FE0C9', '#F7F5F0', '#FF5A7A'
DIM_D = 'rgba(247,245,240,.78)'   # on dark
DIM_P = 'rgba(18,34,43,.78)'      # on paper
RULE_D = 'rgba(247,245,240,.18)'
RULE_P = 'rgba(18,34,43,.16)'
SHOUT = "'Bricolage Grotesque','Helvetica Neue',Arial,sans-serif"
SAY = "Newsreader,Georgia,'Times New Roman',serif"
READ = "'Instrument Sans',Arial,sans-serif"
WRAP = 'width: min(100% - 40px, 1152px); margin-inline: auto'
FONTS = ('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800'
         '&amp;family=Instrument+Sans:wght@400;500;600&amp;family=Newsreader:ital,opsz,wght@1,6..72,400;1,6..72,500&amp;display=swap')

MARK = '''<svg viewBox="0 0 160 160" aria-hidden="true" style="width: %s; height: %s; flex: none">
<path d="M80 24 L88 56 L120 64 L88 72 L80 104 L72 72 L40 64 L72 56 Z" fill="#F2C14E" stroke="#F7F5F0" stroke-width="7" stroke-linejoin="round"></path>
<path d="M44 24 L52 32 M116 24 L108 32 M80 6 V12" stroke="#F7F5F0" stroke-width="6" stroke-linecap="round"></path>
<path d="M12 122 H148" stroke="#F7F5F0" stroke-width="9" stroke-linecap="round"></path>
<path d="M14 144 C28 134, 40 154, 54 144 S80 134, 94 144 S120 154, 134 144 L146 136" stroke="#7FE0C9" stroke-width="8" stroke-linecap="round" fill="none"></path>
</svg>'''


def mark(px=42):
    return MARK % (f'{px}px', f'{px}px')


def btn(label, href, kind='beacon', small=False):
    pad = '9px 18px' if small else '12px 24px'
    size = '16px' if small else '18px'
    mh = '44px' if small else '48px'
    look = {
        'beacon': f'background: {BEACON}; border: 3px solid {BEACON}; color: {DEEP}',
        'ghost': f'background: transparent; border: 3px solid {PAPER}; color: {PAPER}',
        'channel': f'background: {CHANNEL}; border: 3px solid {CHANNEL}; color: {PAPER}',
        'outline': f'background: transparent; border: 3px solid {DEEP}; color: {DEEP}',
        'deep': f'background: {DEEP}; border: 3px solid {DEEP}; color: {PAPER}',
    }[kind]
    cls = 'btn call' if label == 'Ask for a call' else 'btn'
    if label == 'Ask for a call':
        href = CALL
    return (f'<a class="{cls}" href="{href}" style="display: inline-flex; align-items: center; justify-content: center; box-sizing: border-box; min-height: {mh}; padding: {pad}; '
            f'border-radius: 999px; {look}; font-family: {SHOUT}; font-weight: 700; font-size: {size}; letter-spacing: -0.02em; text-decoration: none; white-space: nowrap">{label}</a>')


def h2(text, dark=False, maxw='18ch', mb='20px'):
    c = PAPER if dark else DEEP
    return (f'<h2 style="margin: 0 0 {mb}; font-family: {SHOUT}; font-weight: 800; font-size: clamp(34px, 4.1vw, 59px); line-height: 1; letter-spacing: -0.045em; '
            f'color: {c}; max-width: {maxw}; text-wrap: balance">{text}</h2>')


def sub(text, dark=False, mb='40px'):
    c = DIM_D if dark else DIM_P
    return (f'<p style="margin: 0 0 {mb}; font-family: {SAY}; font-style: italic; font-size: clamp(19px, 1.7vw, 25px); line-height: 1.4; color: {c}; max-width: 608px">{text}</p>')


def label(text, color=CHANNEL, mb='8px'):
    return f'<span style="display: block; font-weight: 600; font-size: 14px; line-height: 1.3; color: {color}; margin-bottom: {mb}">{text}</span>'


def link(text, href, dark=False, size='17px'):
    c = PAPER if dark else CHANNEL
    return f'<a href="{href}" style="color: {c}; font-weight: 600; font-size: {size}; text-decoration: underline; text-decoration-thickness: 2px; text-underline-offset: 4px">{text}</a>'


def slot(text, ratio='16 / 9', dark=False, radius='16px'):
    """A labelled picture placeholder. Nothing here pretends to be a photograph."""
    c = PAPER if dark else DEEP
    bg = 'transparent' if dark else '#FFFFFF'
    tc = DIM_D if dark else DIM_P
    return (f'<div role="img" aria-label="Picture to come: {text}" style="aspect-ratio: {ratio}; box-sizing: border-box; border: 3px dashed {c}; border-radius: {radius}; background: {bg}; '
            f'display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; padding: 24px; text-align: center">'
            f'<span style="font-weight: 600; font-size: 13px; color: {tc}">Picture to come</span>'
            f'<span style="font-size: 15px; line-height: 1.4; color: {tc}; max-width: 34ch">{text}</span></div>')


IMG = {'woodshop': 'img/illo-woodshop.jpg', 'reading': 'img/illo-reading.jpg', 'painting': 'img/illo-painting.jpg', 'road': 'img/illo-road.jpg', 'chart': 'img/chart-361-rose.jpg'}
CALL = ('mailto:hello@soundlineschool.com?subject=A%20call%20about%20Soundline&amp;body=Hi%2C%20I%27d%20like%20a%20call%20about%20Soundline.%0D%0A%0D%0A'
        'My%20name%3A%0D%0ABest%20number%3A%0D%0AGood%20times%20to%20reach%20me%3A%0D%0AMy%20child%27s%20grade%20in%20September%202027%3A')
ILLO = 'Our first students arrive in September 2027.'


def pic(key, alt, ratio, pos='50% 50%', caption=None, dark=False, chart=False):
    cap = ''
    if caption:
        c = DIM_D if dark else DIM_P
        fam = f'font-size: 14px; line-height: 1.4; color: {c}' if chart else f'font-family: {SAY}; font-style: italic; font-size: 16px; line-height: 1.4; color: {c}'
        cap = f'\n<figcaption style="{fam}">{caption}</figcaption>'
    return (f'<figure style="margin: 0; display: flex; flex-direction: column; gap: 10px">\n'
            f'<img src="{IMG[key]}" alt="{alt}" loading="lazy" style="display: block; width: 100%; aspect-ratio: {ratio}; object-fit: cover; object-position: {pos}; border-radius: 16px">{cap}\n</figure>')


ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 160 160'%3E%3Crect width='160' height='160' fill='%2312222B'/%3E%3Cpath d='M80 24 L88 56 L120 64 L88 72 L80 104 L72 72 L40 64 L72 56 Z' fill='%23F2C14E' stroke='%23F7F5F0' stroke-width='7' stroke-linejoin='round'/%3E"
        "%3Cpath d='M12 122 H148' stroke='%23F7F5F0' stroke-width='9' stroke-linecap='round'/%3E%3Cpath d='M14 144 C28 134, 40 154, 54 144 S80 134, 94 144 S120 154, 134 144 L146 136' stroke='%237FE0C9' stroke-width='8' stroke-linecap='round' fill='none'/%3E%3C/svg%3E")
META = {}   # make.py fills this per page: description, path, extra head markup


def head(title):
    d = META.get('desc', '')
    p = META.get('path', '')
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="facebook-domain-verification" content="a2bndez83kc13zpnn8f4guojgduhwp">
<title>{title}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="https://soundlineschool.com/{p}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{d}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://soundlineschool.com/{p}">
<meta property="og:image" content="https://soundlineschool.com/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://soundlineschool.com/og-image.png">
<link rel="icon" href="{ICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="{META.get('root', '')}premium.css">
{META.get('head', '')}</head>
<body>
'''


def tail(w=0, h=0):
    return f'''<div class="sticky-cta"><a class="btn call" href="{CALL}">Ask for a call</a></div>
<script src="{META.get('root', '')}site.js"></script>
</body>
</html>
'''


NAV = [('A day here', 'day.html', 'day'), ('Our vision', 'vision.html', 'vision'), ('About us', 'about.html', 'about'),
       ('The Collaborative', 'collaborative.html', 'collab'), ('Tuition and admissions', 'join.html', 'adm')]


def chrome_top(current):
    items = ''
    for text, href, key in NAV:
        on = key == current
        col = PAPER if on else DIM_D
        bb = BEACON if on else 'transparent'
        cur = ' aria-current="page"' if on else ''
        items += f'<a href="{href}"{cur} style="color: {col}; text-decoration: none; font-size: 16px; padding: 12px 0 10px; border-bottom: 2px solid {bb}">{text}</a>\n'
    return f'''<div style="background: {CHANNEL}; color: {PAPER}">
<div style="{WRAP}; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 4px 24px; padding: 10px 0; font-size: 15px; line-height: 1.4">
<span>Founding enrollment is open, and tuition for 2027–28 is published.</span>
<a href="join.html" style="color: {PAPER}; font-weight: 600; text-decoration: underline; text-decoration-thickness: 2px; text-underline-offset: 3px">See the numbers</a>
</div>
</div>
<header style="background: {DEEP}; color: {PAPER}">
<div style="{WRAP}; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px 32px; padding: 22px 0">
<a href="index.html" aria-label="Soundline School home" style="display: flex; align-items: center; gap: 20px; text-decoration: none; color: {PAPER}">
{mark(42)}
<span style="display: flex; flex-direction: column; gap: 4px">
<span style="font-family: {SHOUT}; font-weight: 800; font-size: 25px; line-height: 1; letter-spacing: -0.045em; text-transform: uppercase">Soundline</span>
<span style="font-weight: 600; font-size: 13px; line-height: 1.2; color: {DIM_D}">North Shore, Long Island</span>
</span>
</a>
<nav aria-label="Main" style="display: flex; flex-wrap: wrap; align-items: center; gap: 4px 26px">
{items}{btn('Reserve a founding seat', 'join.html#reserve', 'beacon', small=True)}
</nav>
</div>
</header>
'''


def footer():
    cols = [('The school', [('A day here', 'day.html'), ('One seventh grader’s Tuesday', 'day.html#tuesday'), ('Our vision', 'vision.html'), ('The research, with sources', 'research.html')]),
            ('Joining', [('Tuition and admissions', 'join.html'), ('The Collaborative', 'collaborative.html'), ('Questions parents ask', 'join.html#questions'), ('Download our informational packet', 'soundline-school-information.pdf')]),
            ('Us', [('About us', 'about.html'), ('hello@soundlineschool.com', 'mailto:hello@soundlineschool.com'), ('Ask for a call', CALL)])]
    html = ''
    for title, links in cols:
        ls = ''.join(f'<a href="{h}" style="color: {PAPER}; font-size: 16px; text-decoration: none; padding: 5px 0">{t}</a>\n' for t, h in links)
        html += f'<div style="display: flex; flex-direction: column; gap: 2px">\n<span style="font-weight: 600; font-size: 14px; color: {GLOW}; margin-bottom: 8px">{title}</span>\n{ls}</div>\n'
    return f'''<footer class="on-dark" style="background: {DEEP}; color: {PAPER}; flex: 1 0 auto; display: flex; flex-direction: column">
<div style="{WRAP}; flex: 1 0 auto; display: flex; flex-direction: column; justify-content: space-between; gap: 56px; padding: 64px 0 40px; border-top: 1px solid {RULE_D}; box-sizing: border-box">
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 40px 64px">
<div style="display: flex; flex-direction: column; gap: 6px">
<div style="display: flex; align-items: center; gap: 16px">
{mark(36)}
<span style="font-family: {SHOUT}; font-weight: 800; font-size: 21px; line-height: 1; letter-spacing: -0.045em; text-transform: uppercase">Soundline School</span>
</div>
<span style="font-family: {SAY}; font-style: italic; font-size: 23px; line-height: 1.3; color: {BEACON}">Depth with direction.</span>
<span style="font-size: 15px; color: {DIM_D}; margin-top: 10px">A new private middle school · Grades 6–8 · Opening September 2027 · North Shore, Long Island</span>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 32px 64px">
{html}</div>
</div>
<p style="margin: 0; font-size: 14px; line-height: 1.5; color: {DIM_D}; max-width: 760px">Soundline admits students of any race, color, national and ethnic origin.</p>
</div>
</footer>
'''


def root_open(h):
    return (f'<div style="font-family: {READ}; font-size: 18px; line-height: 1.55; color: {DEEP}; background: {PAPER}; display: flex; flex-direction: column; '
            f'min-height: 100vh; -webkit-font-smoothing: antialiased">\n')


def proof_item(title, body, color=DEEP):
    return (f'<div style="border-top: 3px solid {color}; padding-top: 20px">\n'
            f'<h3 style="margin: 0 0 8px; font-family: {READ}; font-weight: 600; font-size: 19px; line-height: 1.3">{title}</h3>\n'
            f'<p style="margin: 0; font-size: 16px; line-height: 1.5; color: {DIM_P}">{body}</p>\n</div>\n')


def h3(text, color=DEEP, size='22px', mb='8px'):
    return f'<h3 style="margin: 0 0 {mb}; font-family: {SHOUT}; font-weight: 800; font-size: {size}; line-height: 1.05; letter-spacing: -0.035em; color: {color}">{text}</h3>'


def field(fid, text, kind='text', ph=''):
    return (f'<div style="display: flex; flex-direction: column; gap: 6px; flex: 1 1 220px; min-width: 0">\n'
            f'<label for="{fid}" style="font-weight: 600; font-size: 15px">{text}</label>\n'
            f'<input id="{fid}" name="{fid}" type="{kind}" placeholder="{ph}" style="box-sizing: border-box; width: 100%; height: 48px; padding: 0 14px; border: 2px solid {DEEP}; border-radius: 10px; '
            f'background: #FFFFFF; font-family: {READ}; font-size: 17px; color: {DEEP}">\n</div>\n')


def select(fid, text, options):
    opts = ''.join(f'<option>{o}</option>' for o in options)
    return (f'<div style="display: flex; flex-direction: column; gap: 6px; flex: 1 1 220px; min-width: 0">\n'
            f'<label for="{fid}" style="font-weight: 600; font-size: 15px">{text}</label>\n'
            f'<select id="{fid}" name="{fid}" style="box-sizing: border-box; width: 100%; height: 48px; padding: 0 12px; border: 2px solid {DEEP}; border-radius: 10px; '
            f'background: #FFFFFF; font-family: {READ}; font-size: 17px; color: {DEEP}">{opts}</select>\n</div>\n')


def call_form(prefix):
    return f'''<form action="#" style="background: #FFFFFF; border: 3px solid {DEEP}; border-radius: 16px; padding: clamp(20px, 3vw, 32px); display: flex; flex-direction: column; gap: 18px; box-sizing: border-box">
<div style="display: flex; flex-wrap: wrap; gap: 18px">
{field(prefix + '-name', 'Your name')}{field(prefix + '-phone', 'Phone', 'tel')}</div>
<div style="display: flex; flex-wrap: wrap; gap: 18px">
{field(prefix + '-email', 'Email', 'email')}{select(prefix + '-grade', 'Your child’s grade in September 2027', ['Sixth', 'Seventh', 'Eighth', 'Younger than sixth', 'Older than eighth'])}</div>
<div style="display: flex; flex-wrap: wrap; gap: 18px">
{select(prefix + '-track', 'Five days, or three?', ['The School, five days', 'The Collaborative, three days', 'Not sure yet'])}{field(prefix + '-when', 'A good time to reach you', 'text', 'Weekday evenings, for example')}</div>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 12px 20px">
<button type="submit" style="min-height: 48px; padding: 12px 24px; border-radius: 999px; background: {CHANNEL}; border: 3px solid {CHANNEL}; color: {PAPER}; font-family: {SHOUT}; font-weight: 700; font-size: 18px; letter-spacing: -0.02em; cursor: pointer">Ask for a call</button>
<span style="font-size: 15px; color: {DIM_P}">One of the four of us calls you back.</span>
</div>
</form>
'''


def tracks(with_price=True):
    def price(big, small, col, dim):
        if not with_price:
            return ''
        return (f'<div style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 12px; margin-top: 8px; padding-top: 20px; border-top: 1px solid {dim}">\n'
                f'<span style="font-family: {SHOUT}; font-weight: 800; font-size: 44px; line-height: 1; letter-spacing: -0.04em; color: {col}">{big}</span>\n'
                f'<span style="font-size: 16px; color: {col}">{small}</span>\n</div>\n')
    return f'''<div style="display: flex; flex-wrap: wrap; gap: 16px">
<div style="flex: 1 1 380px; min-width: 0; box-sizing: border-box; background: {CHANNEL}; color: {PAPER}; border-radius: 20px; padding: clamp(26px, 3.5vw, 42px); display: flex; flex-direction: column; gap: 12px">
{label('The School, five days', GLOW, '0')}
{h3('For families ready to make the move.', PAPER, 'clamp(24px, 2.4vw, 33px)', '0')}
<p style="margin: 0; color: {DIM_D}">Monday to Friday, 8:30 to 3:00, with Extended Day until 5:30. Enroll, and that’s it. No homeschool paperwork.</p>
{price('$1,350', 'a month, the founding rate. Standard tuition is $1,500.', PAPER, RULE_D)}</div>
<div style="flex: 1 1 380px; min-width: 0; box-sizing: border-box; background: {SHALLOWS}; color: {DEEP}; border-radius: 20px; padding: clamp(26px, 3.5vw, 42px); display: flex; flex-direction: column; gap: 12px">
{label('The Collaborative, three days', DEEP, '0')}
{h3('For homeschooling families.', DEEP, 'clamp(24px, 2.4vw, 33px)', '0')}
<p style="margin: 0; color: {DEEP}">Monday and Wednesday, 9:15 to 12:30, and Friday, 9:15 to 2:45. Same guides, same rooms, same studio. You keep your homeschool plan, and we hand you the course descriptions and hours logs to go with it.</p>
{price('$810', 'a month, the founding rate. Standard tuition is $900.', DEEP, 'rgba(18,34,43,.3)')}</div>
</div>
'''


def day_bar(dark=True):
    edge = PAPER if dark else DEEP
    tick = GLOW if dark else CHANNEL
    return f'''<div aria-label="The school day" style="display: flex; flex-wrap: wrap; gap: 8px">
<div style="flex: 2 1 200px; min-width: 0; display: flex; flex-direction: column; gap: 8px">
<span style="font-size: 15px; color: {tick}">8:30</span>
<div style="flex: 1 0 auto; box-sizing: border-box; background: {SHALLOWS}; color: {DEEP}; border-radius: 10px; padding: 14px 18px; min-height: 84px; display: flex; flex-direction: column; justify-content: center">
<b style="font-family: {SHOUT}; font-weight: 800; font-size: 25px; letter-spacing: -0.03em; line-height: 1.1">Practice</b>
<span style="font-size: 15px">Two hours: math, reading, writing, then the 10:30 seminar</span>
</div>
</div>
<div style="flex: 4 1 400px; min-width: 0; display: flex; flex-direction: column; gap: 8px">
<span style="font-size: 15px; color: {tick}">&nbsp;</span>
<div style="flex: 1 0 auto; box-sizing: border-box; background: {MAKING}; color: {DEEP}; border-radius: 10px; padding: 14px 18px; min-height: 84px; display: flex; flex-direction: column; justify-content: center">
<b style="font-family: {SHOUT}; font-weight: 800; font-size: 25px; letter-spacing: -0.03em; line-height: 1.1">Making</b>
<span style="font-size: 15px">Four hours, to 3:00: seminar, lab, studio, the quest</span>
</div>
</div>
<div style="flex: 2.5 1 250px; min-width: 0; display: flex; flex-direction: column; gap: 8px">
<span style="display: flex; justify-content: space-between; font-size: 15px; color: {tick}"><span>3:00</span><span>5:30</span></span>
<div style="flex: 1 0 auto; box-sizing: border-box; border: 3px dashed {edge}; color: {edge}; border-radius: 10px; padding: 14px 18px; min-height: 84px; display: flex; flex-direction: column; justify-content: center">
<b style="font-family: {SHOUT}; font-weight: 800; font-size: 25px; letter-spacing: -0.03em; line-height: 1.1">Extended Day</b>
<span style="font-size: 15px">3:00 to 5:30, if you need it</span>
</div>
</div>
</div>
'''


def faq(q, a, open_=False):
    op = ' open' if open_ else ''
    return (f'<details{op} style="border-top: 1px solid {RULE_P}; padding: 4px 0">\n'
            f'<summary style="cursor: pointer; padding: 14px 0; font-weight: 600; font-size: 18px; line-height: 1.35">{q}</summary>\n'
            f'<p style="margin: 0 0 18px; font-size: 16.5px; line-height: 1.55; color: {DIM_P}; max-width: 608px">{a}</p>\n</details>\n')


# ------------------------------------------------------------------ SHARED PIECES
WP = 'width: min(100% - 48px, 1200px); margin-inline: auto'
PAD = 'clamp(72px, 10vw, 148px)'
HALF = 'clamp(56px, 7vw, 104px)'


def ph2(text, dark=False, maxw='16ch', mb='22px'):
    c = PAPER if dark else DEEP
    return (f'<h2 style="margin: 0 0 {mb}; font-family: {SHOUT}; font-weight: 800; font-size: clamp(36px, 4.6vw, 66px); line-height: 0.98; letter-spacing: -0.045em; '
            f'color: {c}; max-width: {maxw}; text-wrap: balance">{text}</h2>')


def psub(text, dark=False, mb='56px'):
    c = DIM_D if dark else DIM_P
    return f'<p style="margin: 0 0 {mb}; font-family: {SAY}; font-style: italic; font-size: clamp(20px, 1.9vw, 27px); line-height: 1.4; color: {c}; max-width: 640px">{text}</p>'


def quiet(text, href, dark=False):
    c = PAPER if dark else DEEP
    return f'<a href="{href}" style="color: {c}; font-weight: 600; font-size: 16px; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 6px">{text}</a>'


def ital(text, color=CHANNEL, size='18px', mb='4px'):
    return f'<span style="display: block; font-family: {SAY}; font-style: italic; font-size: {size}; line-height: 1.3; color: {color}; margin-bottom: {mb}">{text}</span>'


def chrome(current):
    nav, panel = '', '<a href="index.html">Home</a>\n'
    for t, h, k in NAV:
        on = k == current
        col = PAPER if on else DIM_D
        bb = BEACON if on else 'transparent'
        cur = ' aria-current="page"' if on else ''
        nav += f'<a class="nav-link" href="{h}"{cur} style="color: {col}; text-decoration: none; font-size: 15px; padding: 12px 0 10px; border-bottom: 1px solid {bb}">{t}</a>\n'
        panel += f'<a href="{h}"{cur}>{t}</a>\n'
    return f'''<div class="on-dark" style="background: {DEEP}; color: {DIM_D}; border-bottom: 1px solid {RULE_D}">
<div style="{WP}; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 4px 24px; padding: 9px 0; font-size: 14px; line-height: 1.4">
<span>We are signing up our first families now. Tuition for 2027–28 is published.</span>
{quiet('See what it costs', 'join.html#tuition', dark=True)}
</div>
</div>
<header class="on-dark" style="background: {DEEP}; color: {PAPER}">
<div style="{WP}; display: flex; align-items: center; justify-content: space-between; gap: 12px 32px; padding: 22px 0">
<a href="index.html" aria-label="Soundline School home" style="display: flex; align-items: center; gap: 18px; text-decoration: none; color: {PAPER}">
{mark(40)}
<span style="display: flex; flex-direction: column; gap: 4px">
<span style="font-family: {SHOUT}; font-weight: 800; font-size: 24px; line-height: 1; letter-spacing: -0.045em; text-transform: uppercase">Soundline</span>
<span style="font-size: 13px; line-height: 1.2; color: {DIM_D}">North Shore, Long Island</span>
</span>
</a>
<nav aria-label="Main" class="nav-links">
{nav}{btn('Ask for a call', CALL, 'ghost', small=True)}
<details class="menu">
<summary aria-label="Menu"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><line x1="4" y1="8" x2="20" y2="8"></line><line x1="4" y1="16" x2="20" y2="16"></line></svg></summary>
<div class="panel">
{panel}</div>
</details>
</nav>
</div>
</header>
'''


def ledger(rows, dark=False):
    rule = RULE_D if dark else RULE_P
    dim = DIM_D if dark else DIM_P
    out = ''
    for t, b in rows:
        out += (f'<li style="border-top: 1px solid {rule}; padding: 26px 0; display: flex; flex-wrap: wrap; align-items: baseline; gap: 8px 56px">\n'
                f'<h3 style="margin: 0; flex: 1 1 320px; font-family: {SHOUT}; font-weight: 800; font-size: clamp(22px, 2.1vw, 29px); line-height: 1.08; letter-spacing: -0.035em">{t}</h3>\n'
                f'<p style="margin: 0; flex: 1.5 1 380px; font-size: 17px; line-height: 1.55; color: {dim}">{b}</p>\n</li>\n')
    return f'<ul style="list-style: none; margin: 0; padding: 0; border-bottom: 1px solid {rule}">\n{out}</ul>\n'


def track(chip, lab, title, body, big, small):
    return (f'<div style="flex: 1 1 380px; min-width: 0; display: flex; flex-direction: column; gap: 14px">\n'
            f'<span aria-hidden="true" style="display: block; width: 72px; height: 8px; border-radius: 4px; background: {chip}"></span>\n'
            f'{ital(lab, CHANNEL, "20px", "0")}\n'
            f'<h3 style="margin: 0; font-family: {SHOUT}; font-weight: 800; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.02; letter-spacing: -0.04em">{title}</h3>\n'
            f'<p style="margin: 0; font-size: 17px; line-height: 1.6; color: {DIM_P}; max-width: 480px">{body}</p>\n'
            f'<div style="margin-top: 10px; padding-top: 22px; border-top: 1px solid {RULE_P}; display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 14px">\n'
            f'<span style="font-family: {SHOUT}; font-weight: 800; font-size: clamp(44px, 4.6vw, 66px); line-height: 1; letter-spacing: -0.045em">{big}</span>\n'
            f'<span style="font-size: 16px; color: {DIM_P}">{small}</span>\n</div>\n</div>\n')


def tracks_section():
    a = track(CHANNEL, 'Five days a week', 'The full school.', 'Monday to Friday, 8:30 to 3:00. Your child can stay until 5:30 if you need it. You enroll, and that’s it. There is no homeschool paperwork.', '$1,350', 'a month for Founding Families, the first to join. The regular price is $1,500.')
    b = track(SHALLOWS, 'Three days a week', 'For homeschooling families.', 'Monday and Wednesday, 9:15 to 12:30, and Friday, 9:15 to 2:45. We call it the Collaborative. You stay your child’s teacher, and we hand you course descriptions and hours logs for your district reports.', '$810', 'a month for Founding Families. The regular price is $900.')
    return f'''<section style="background: #FFFFFF; border-top: 1px solid {RULE_P}; border-bottom: 1px solid {RULE_P}; padding: {PAD} 0">
<div style="{WP}">
{ph2('Five days a week, or three for homeschoolers.', maxw='18ch', mb='56px')}
<div style="display: flex; flex-wrap: wrap; gap: 56px 96px">
{a}{b}</div>
<div style="display: flex; flex-wrap: wrap; gap: 12px 36px; margin-top: 56px">
{quiet('See every price', 'join.html#tuition')}
{quiet('How three days a week works', 'collaborative.html')}
</div>
</div>
</section>
'''


def call_section(prefix='', sid='call'):
    return f'''<section id="{sid}" style="padding: {HALF} 0 {PAD}">
<div style="{WP}; display: flex; flex-wrap: wrap; gap: 36px 96px; align-items: flex-end">
<div style="flex: 1 1 360px; min-width: 0">
{ph2('Prefer to talk? We’ll find a time.', maxw='12ch')}
{psub('Twenty minutes on the phone with one of the four of us. Ask anything, including about money.', mb='0')}
</div>
<div style="flex: 1.2 1 440px; min-width: 0; display: flex; flex-direction: column; align-items: flex-start; gap: 18px">
{btn('Ask for a call', CALL, 'deep')}
<p style="margin: 0; font-size: 16px; line-height: 1.55; color: {DIM_P}; max-width: 520px">The button opens an email to hello@soundlineschool.com with four lines to fill in: your name, the best number, good times to reach you, and your child’s grade next September. One of the four of us calls you back.</p>
<p style="margin: 0; font-size: 15px; color: {DIM_P}">Prefer to start in writing? {quiet('Take the survey', 'https://soundlineschool.com/survey/')}.</p>
</div>
</div>
</section>
'''


def bar(name, hours, look):
    return (f'<div style="box-sizing: border-box; {look}; border-radius: 10px; padding: 0 18px; min-height: 64px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 2px 12px">\n'
            f'<b style="font-family: {SHOUT}; font-weight: 800; font-size: 22px; letter-spacing: -0.03em">{name}</b>\n<span style="font-size: 15px">{hours}</span>\n</div>\n')


# Home lives in plain.py (home_plain), rewritten in plain language on 12 Nov 2026.
