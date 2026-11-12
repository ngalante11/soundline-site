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
            ('Joining', [('Tuition and admissions', 'join.html'), ('The Collaborative', 'collaborative.html'), ('Questions families ask', 'join.html#questions'), ('Download our informational packet', 'soundline-school-information.pdf')]),
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
<span style="font-size: 15px; color: {DIM_D}; margin-top: 10px">Private middle school · Grades 6–8 · Opening September 2027 · North Shore, Long Island</span>
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
<span>Founding enrollment is open, and tuition for 2027–28 is published.</span>
{quiet('See the numbers', 'join.html#tuition', dark=True)}
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
    a = track(CHANNEL, 'The School, five days', 'For families ready to make the move.', 'Monday to Friday, 8:30 to 3:00, with Extended Day until 5:30. Enroll, and that’s it. No homeschool paperwork.', '$1,350', 'a month, the founding rate. Standard tuition is $1,500.')
    b = track(SHALLOWS, 'The Collaborative, three days', 'For homeschooling families.', 'Monday and Wednesday, 9:15 to 12:30, and Friday, 9:15 to 2:45. Same guides, same rooms, same studio. You keep your homeschool plan, and we hand you the course descriptions and hours logs to go with it.', '$810', 'a month, the founding rate. Standard tuition is $900.')
    return f'''<section style="background: #FFFFFF; border-top: 1px solid {RULE_P}; border-bottom: 1px solid {RULE_P}; padding: {PAD} 0">
<div style="{WP}">
{ph2('Five days a week, or three for homeschoolers.', maxw='18ch', mb='56px')}
<div style="display: flex; flex-wrap: wrap; gap: 56px 96px">
{a}{b}</div>
<div style="display: flex; flex-wrap: wrap; gap: 12px 36px; margin-top: 56px">
{quiet('The whole tuition table', 'join.html#tuition')}
{quiet('How the Collaborative works', 'collaborative.html')}
</div>
</div>
</section>
'''


def call_section(prefix='', sid='call'):
    return f'''<section id="{sid}" style="padding: {HALF} 0 {PAD}">
<div style="{WP}; display: flex; flex-wrap: wrap; gap: 36px 96px; align-items: flex-end">
<div style="flex: 1 1 360px; min-width: 0">
{ph2('Prefer to talk? We’ll find a time.', maxw='12ch')}
{psub('Twenty minutes on the phone with one of the four of us. Ask anything, the money questions included.', mb='0')}
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


# ------------------------------------------------------------------ HOME
def home():
    H = 0

    o = head('Soundline School | Private middle school, grades 6–8 | North Shore, Long Island') + root_open(H)

    o += chrome('home')

    # hero: the promise at full width, the third line in the reassuring face; then the photograph, left alone
    o += f'''<section style="background: {DEEP}; color: {PAPER}; padding: clamp(48px, 6.5vw, 96px) 0 0">
<div style="{WP}; display: flex; flex-direction: column; gap: clamp(28px, 3.4vw, 48px)">
<h1 style="margin: 0; font-family: {READ}; font-weight: 500; font-size: 15px; line-height: 1.4; letter-spacing: 0; color: {GLOW}">Private middle school · Grades 6–8 · North Shore, Long Island</h1>
<p style="margin: 0; font-family: {SHOUT}; font-weight: 800; font-size: clamp(44px, 6vw, 88px); line-height: 0.98; letter-spacing: -0.045em">
<span style="display: block; text-wrap: balance">Two hours of practice.</span>
<span style="display: block; text-wrap: balance">Four hours of making.</span>
<span style="display: block; font-family: {SAY}; font-style: italic; font-weight: 400; letter-spacing: -0.02em; line-height: 1.08; color: {BEACON}; text-wrap: balance">Every adult knows your kid.</span>
</p>
<div style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 28px 64px">
<p style="margin: 0; flex: 1 1 420px; min-width: 0; max-width: 640px; font-size: clamp(17px, 1.3vw, 19px); line-height: 1.55; color: {DIM_D}">Soundline School is a private middle school for grades 6–8 on Long Island’s North Shore, opening September 2027. We’re choosing a building along the Miller Place–Port Jefferson Station corridor, and Port Jefferson Station is the likeliest. Ninth grade follows in September 2028, then a grade a year through twelfth.</p>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 16px 28px">
{btn('Ask for a call', '#call', 'beacon')}
{quiet('See tuition', 'join.html#tuition', dark=True)}
</div>
</div>
</div>
<figure style="margin: clamp(40px, 5vw, 72px) 0 0; position: relative; height: clamp(300px, 50vw, 720px); overflow: hidden; background: {DEEP}">
<img src="{HERO}" alt="Five kids on the rocks at the edge of the Sound at sunset, in silhouette." style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 82%; display: block">
<figcaption style="position: absolute; right: 24px; bottom: 16px; font-size: 13px; color: {PAPER}; background: {DEEP}; padding: 4px 10px; border-radius: 6px">Long Island Sound, from the North Shore.</figcaption>
</figure>
</section>
'''

    # three figures, set like a ledger
    figs = [('10–12', 'students in a grade', 'Every student keeps the same advisor from sixth through eighth grade, and works by skill across the school, not by age.'),
            ('$1,350', 'a month for founding families', 'Standard tuition for 2027–28 is $1,500 a month for five days. The founding rate stays fixed for as long as your child is enrolled. No application fee.'),
            ('8:30–3:00', 'the school day', 'Two hours of math, reading and writing with a guide (our word for a teacher) at the table. Then four hours of seminar, science lab and six-week projects.')]
    fh = ''
    for big, lab, body in figs:
        fh += (f'<div style="border-top: 1px solid {DEEP}; padding-top: 22px; display: flex; flex-direction: column; gap: 6px">\n'
               f'<span style="font-family: {SHOUT}; font-weight: 800; font-size: clamp(44px, 4.6vw, 66px); line-height: 1; letter-spacing: -0.045em">{big}</span>\n'
               f'<span style="font-family: {SAY}; font-style: italic; font-size: 21px; line-height: 1.3; color: {CHANNEL}">{lab}</span>\n'
               f'<p style="margin: 10px 0 0; font-size: 16px; line-height: 1.55; color: {DIM_P}; max-width: 340px">{body}</p>\n</div>\n')
    o += f'''<section style="padding: clamp(56px, 7vw, 104px) 0 0">
<div style="{WP}; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr)); gap: 40px 56px">
{fh}</div>
</section>
'''

    # the day: the one place the page turns on its color
    def col(title, body):
        return (f'<div>\n<h3 style="margin: 0 0 8px; font-family: {READ}; font-weight: 600; font-size: 20px; line-height: 1.3">{title}</h3>\n'
                f'<p style="margin: 0; font-size: 16.5px; line-height: 1.6; color: {DIM_P}">{body}</p>\n</div>\n')

    def bar(name, hours, look):
        return (f'<div style="box-sizing: border-box; {look}; border-radius: 10px; padding: 0 18px; height: 64px; display: flex; align-items: center; justify-content: space-between; gap: 12px">\n'
                f'<b style="font-family: {SHOUT}; font-weight: 800; font-size: 22px; letter-spacing: -0.03em">{name}</b>\n<span style="font-size: 15px">{hours}</span>\n</div>\n')
    o += f'''<section id="day" style="padding: {PAD} 0">
<div style="{WP}">
{ph2('What a school day looks like.', maxw='14ch')}
{psub('Students do real work, finish it, and show it to someone.')}
<div style="display: flex; flex-wrap: wrap; gap: 40px 10px">
<div style="flex: 2 1 200px; min-width: 0; display: flex; flex-direction: column; gap: 28px">
{bar('Practice', 'Two hours', f'background: {SHALLOWS}; color: {DEEP}')}<div style="padding-right: 22px">
{col('Mornings are practice.', 'Math, reading, and writing at each student’s own pace, with a guide in the room. Nobody waits for the class to catch up, and nobody gets left behind it. Two hours, done well, and done.')}</div>
</div>
<div style="flex: 4 1 400px; min-width: 0; display: flex; flex-direction: column; gap: 28px">
{bar('Making', 'Four hours, to 3:00', f'background: {MAKING}; color: {DEEP}')}{pic('woodshop', 'Illustration: a student and a woodworker measure a board together at a workbench, tools on the wall behind them.', '16 / 9', '50% 38%', 'An illustration. ' + ILLO)}
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(220px, 100%), 1fr)); gap: 24px 32px; padding-right: 22px">
{col('Afternoons are for making.', 'History, literature, and science are taught by a person with a book, never by an app. Studio runs in six-week projects with a real audience: a video game, a robot, a sculpture, a short documentary, a zine the school press publishes, a song the ensemble performs.')}{col('Big work gets defended out loud.', 'No slides, no screen. A student, their work, and good questions.')}</div>
</div>
<div style="flex: 2.5 1 250px; min-width: 0; display: flex; flex-direction: column; gap: 28px">
{bar('Extended Day', 'To 5:30', f'border: 2px dashed {DEEP}; color: {DEEP}')}{col('Home, or not yet.', 'A lesson at 3:15, then the homework desk until 5:30. Or the carline. The project stays at school.')}</div>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 12px 36px; margin-top: 56px">
{quiet('Follow one seventh grader’s Tuesday', 'day.html#tuesday')}
{quiet('See a week at Soundline', 'day.html#week')}
</div>
</div>
</section>
'''

    # the story and who it suits, on one plate, with the chart given room
    suits = [('Doing fine, and bored.', 'Waiting for everyone else, and ready for work that asks more.'),
             ('Working hard, and unnoticed.', 'In a room where nobody has the time to see it.'),
             ('Making things at home.', 'With nowhere to show them, and nobody to show them to.')]
    sh = ''.join(f'<li style="border-top: 1px solid {RULE_D}; padding: 18px 0; display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 24px">\n'
                 f'<span style="flex: 1 1 240px; font-family: {SAY}; font-style: italic; font-size: 24px; line-height: 1.3; color: {BEACON}">{t}</span>\n'
                 f'<span style="flex: 1.2 1 260px; font-size: 16px; line-height: 1.5; color: {DIM_D}">{b}</span>\n</li>\n' for t, b in suits)
    o += f'''<section style="background: {DEEP}; color: {PAPER}; padding: {PAD} 0">
<div style="{WP}; display: flex; flex-wrap: wrap; align-items: center; gap: 48px 88px">
<div style="flex: 1 1 400px; min-width: 0">
{pic('chart', 'A 1941 nautical chart of the water off Mount Sinai: a compass rose surrounded by depth soundings.', '1 / 1', '32% 60%', 'Chart 361, Port Jefferson and Mount Sinai Harbors. U.S. Coast and Geodetic Survey, 1941. Every number is a sounding.', dark=True, chart=True)}
</div>
<div style="flex: 1.1 1 440px; min-width: 0; display: flex; flex-direction: column; gap: 22px">
{ph2('Every child has a soundline.', dark=True, maxw='11ch', mb='6px')}
<p style="margin: 0; color: {DIM_D}">Before sonar, sailors dropped a sounding line over the side to learn how deep the water was and what lay on the bottom. Only then did they set a course.</p>
<p style="margin: 0; color: {DIM_D}">That’s where we start with your child: where they are, skill by skill, what sparks them, and how deep it runs. Then we set a direction together.</p>
<p style="margin: 14px 0 0; font-size: 16px; color: {PAPER}">Middle school is three years. They go fast. Soundline suits a kid who is:</p>
<ul style="list-style: none; margin: 0; padding: 0; border-bottom: 1px solid {RULE_D}">
{sh}</ul>
<p style="margin: 0; font-size: 16px; color: {DIM_D}">Students with IEPs keep their district services, and we help you request them. Soundline is not a religious school or a test-prep program.</p>
<div style="margin-top: 6px">{quiet('The whole story, and how we come to know your child', 'about.html#story', dark=True)}</div>
</div>
</div>
</section>
'''

    # what is true today, as a ledger
    truths = [('We open in September 2027.', 'We have no students yet, so we have no results to show you. What we can show you is the plan, the people, and the day, hour by hour.'),
              ('We are not accredited yet.', 'New York doesn’t license private schools. We register with the state, the district reviews that what we teach is equivalent, and we start accreditation once we’re open.'),
              ('Every adult is fingerprinted.', 'Through the New York State Education Department, which runs a state and FBI criminal history check, before they start. New York makes this optional for private schools. We do it.'),
              ('Your $500 goes into escrow.', 'It is held by an independent escrow agent, not by us, and it comes back in full, for any reason, until the day we sign a lease.'),
              ('You will see the number.', 'We measure every student’s growth three times a year and publish whole-school growth, counting everyone. No child’s score is public; yours comes home.'),
              ('You will see the work.', 'Every Friday at 2:00, someone presents and something is performed. Families welcome.')]
    th = ''.join(f'<li style="border-top: 1px solid {RULE_P}; padding: 26px 0; display: flex; flex-wrap: wrap; align-items: baseline; gap: 8px 56px">\n'
                 f'<h3 style="margin: 0; flex: 1 1 320px; font-family: {SHOUT}; font-weight: 800; font-size: clamp(22px, 2.1vw, 29px); line-height: 1.08; letter-spacing: -0.035em">{t}</h3>\n'
                 f'<p style="margin: 0; flex: 1.5 1 380px; font-size: 17px; line-height: 1.55; color: {DIM_P}">{b}</p>\n</li>\n' for t, b in truths)
    o += f'''<section style="padding: {PAD} 0 clamp(56px, 7vw, 104px)">
<div style="{WP}">
{ph2('What’s true today.', maxw='14ch')}
{psub('We would rather you hear all of it from us.')}
<ul style="list-style: none; margin: 0; padding: 0; border-bottom: 1px solid {RULE_P}">
{th}</ul>
<div style="margin-top: 36px">{quiet('The research, with sources', 'research.html')}</div>
</div>
</section>
'''

    people = [('Founder', 'Nicole Galante, Ph.D.', 'An educator for over twenty years. She started as a classroom teacher, coached teachers in New York City schools for more than fifteen of them, and led the state team that wrote New York’s Quality Remote and Hybrid Teaching Framework and its Handbook for Virtual Schools.'),
              ('Lead guide', 'Adam King', 'A musician and teacher. He designs and runs music and STEAM programs for libraries across Long Island (escape rooms, instrument labs, world percussion) and teaches private lessons. He’ll know your child by Wednesday.'),
              ('Operations', 'Gina Dimichino', 'For more than thirty-five years she has taught dance to North Shore kids, many of them right at this age, and she has run businesses here her whole life, including her own salon. She makes sure every family feels seen, and handles every detail in between.'),
              ('Academic systems', 'Izzy Galante', 'Designs how the school teaches: the sequence, the mastery gates, and how we know it worked. Co-wrote New York’s Quality Remote and Hybrid Teaching Framework and its Handbook for Virtual Schools. Teaches a live seminar every week.')]
    pp = ''
    for role, name, bio in people:
        pp += (f'<div style="border-top: 1px solid {DEEP}; padding-top: 20px">\n<div>\n'
               f'<span style="display: block; font-family: {SAY}; font-style: italic; font-size: 18px; color: {CHANNEL}; margin-bottom: 4px">{role}</span>\n'
               f'<h3 style="margin: 0 0 10px; font-family: {SHOUT}; font-weight: 800; font-size: 24px; line-height: 1.05; letter-spacing: -0.035em">{name}</h3>\n'
               f'<p style="margin: 0; font-size: 15.5px; line-height: 1.55; color: {DIM_P}">{bio}</p>\n</div>\n</div>\n')
    o += f'''<section style="padding: clamp(56px, 7vw, 104px) 0 {PAD}">
<div style="{WP}">
{ph2('Who’s building it.', maxw='14ch', mb='48px')}
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(240px, 100%), 1fr)); gap: 44px 32px">
{pp}</div>
<p style="margin: 48px 0 14px; font-size: 17px; color: {DIM_P}; max-width: 640px">We are hiring a math and science guide and a humanities guide for September 2027. You will meet them before the first day.</p>
<div>{quiet('About us', 'about.html')}</div>
</div>
</section>
'''

    # five days or three: two columns and a rule, the color kept to a chip
    def track(chip, lab, title, body, big, small):
        return (f'<div style="flex: 1 1 380px; min-width: 0; display: flex; flex-direction: column; gap: 14px">\n'
                f'<span aria-hidden="true" style="display: block; width: 72px; height: 8px; border-radius: 4px; background: {chip}"></span>\n'
                f'<span style="font-family: {SAY}; font-style: italic; font-size: 20px; color: {CHANNEL}">{lab}</span>\n'
                f'<h3 style="margin: 0; font-family: {SHOUT}; font-weight: 800; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.02; letter-spacing: -0.04em">{title}</h3>\n'
                f'<p style="margin: 0; font-size: 17px; line-height: 1.6; color: {DIM_P}; max-width: 480px">{body}</p>\n'
                f'<div style="margin-top: 10px; padding-top: 22px; border-top: 1px solid {RULE_P}; display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 14px">\n'
                f'<span style="font-family: {SHOUT}; font-weight: 800; font-size: clamp(44px, 4.6vw, 66px); line-height: 1; letter-spacing: -0.045em">{big}</span>\n'
                f'<span style="font-size: 16px; color: {DIM_P}">{small}</span>\n</div>\n</div>\n')
    o += f'''<section style="background: #FFFFFF; border-top: 1px solid {RULE_P}; border-bottom: 1px solid {RULE_P}; padding: {PAD} 0">
<div style="{WP}">
{ph2('Five days a week, or three for homeschoolers.', maxw='18ch', mb='56px')}
<div style="display: flex; flex-wrap: wrap; gap: 56px 96px">
{track(CHANNEL, 'The School, five days', 'For families ready to make the move.', 'Monday to Friday, 8:30 to 3:00, with Extended Day until 5:30. Enroll, and that’s it. No homeschool paperwork.', '$1,350', 'a month, the founding rate. Standard tuition is $1,500.')}{track(SHALLOWS, 'The Collaborative, three days', 'For homeschooling families.', 'Monday and Wednesday, 9:15 to 12:30, and Friday, 9:15 to 2:45. Same guides, same rooms, same studio. You keep your homeschool plan, and we hand you the course descriptions and hours logs to go with it.', '$810', 'a month, the founding rate. Standard tuition is $900.')}</div>
<div style="display: flex; flex-wrap: wrap; gap: 12px 36px; margin-top: 56px">
{quiet('The whole tuition table', 'join.html#tuition')}
{quiet('How the Collaborative works', 'collaborative.html')}
</div>
</div>
</section>
'''

    # founding families: three steps on rules, one button
    def pstep(n, title, body, cta):
        return (f'<li style="min-width: 0; border-top: 1px solid {PAPER}; padding: 24px 0 0; display: flex; flex-direction: column; gap: 12px">\n'
                f'<span style="font-family: {SHOUT}; font-weight: 800; font-size: 66px; line-height: 0.9; letter-spacing: -0.045em; color: {BEACON}">{n}</span>\n'
                f'<h3 style="margin: 6px 0 0; font-family: {SHOUT}; font-weight: 800; font-size: 26px; line-height: 1.05; letter-spacing: -0.035em">{title}</h3>\n'
                f'<p style="margin: 0 0 8px; font-size: 16.5px; line-height: 1.6; color: {DIM_D}; flex: 1 0 auto; max-width: 340px">{body}</p>\n<div>{cta}</div>\n</li>\n')
    steps = (pstep('1', 'Talk to us.', 'Twenty minutes on the phone with one of the four of us. Ask anything, the money questions included.', btn('Ask for a call', '#call', 'beacon', small=True))
             + pstep('2', 'See the number.', 'Tuition is published, the whole table. You see the number first, then decide — never the other way round.', quiet('What it costs', 'join.html#tuition', dark=True))
             + pstep('3', 'Reserve a founding seat.', 'After the call, if it’s a fit, $500 reserves a seat. It is held by an independent escrow agent, not by us, and comes back in full, for any reason, until the day we sign a lease.', '<span style="font-size: 16px; color: ' + DIM_D + '">We set it up with you on the call.</span>'))
    perks = ['Reserved seats at every production.', 'A first look at each new project before it starts.', 'Sibling priority when a grade fills.', 'Your family’s name on the founders’ wall.']
    perk_html = ''.join('<li style="border-top: 1px solid ' + RULE_D + '; padding: 14px 0; font-size: 17px; color: ' + PAPER + '">' + x + '</li>\n' for x in perks)
    o += f'''<section id="founding" style="background: {DEEP}; color: {PAPER}; padding: {PAD} 0">
<div style="{WP}">
{ph2('Be one of our Founding Families.', dark=True, maxw='14ch')}
{psub('Three grades under one roof, grouped by skill, not age — and we’re taking founding families now.', dark=True, mb='18px')}
<p style="margin: 0 0 64px; font-size: 17px; color: {DIM_D}; max-width: 640px">A rate that stays locked for as long as your child is enrolled, and a seat on the Family Council.</p>
<ol style="list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr)); gap: 48px 56px">
{steps}</ol>
<figure style="margin: clamp(64px, 8vw, 112px) 0; display: flex; flex-direction: column; gap: 18px">
<blockquote style="margin: 0; font-family: {SAY}; font-style: italic; font-size: clamp(30px, 3.9vw, 56px); line-height: 1.15; letter-spacing: -0.015em; color: {BEACON}; max-width: 19ch; text-wrap: balance">“This is the answer to my prayers for my daughter.”</blockquote>
<figcaption style="font-size: 15px; color: {DIM_D}">A parent, November 2026</figcaption>
</figure>
<div style="display: flex; flex-wrap: wrap; gap: 36px 96px; padding-top: 40px; border-top: 1px solid {PAPER}">
<div style="flex: 1 1 380px; min-width: 0">
<h3 style="margin: 0 0 14px; font-family: {SHOUT}; font-weight: 800; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.02; letter-spacing: -0.04em">The Family Council never fundraises.</h3>
<p style="margin: 0 0 14px; font-size: 17px; line-height: 1.6; color: {DIM_D}; max-width: 480px">It does the fun things. Council families help choose the projects students take on, and work with people in town to bring kids and experiences together.</p>
<p style="margin: 0; font-family: {SAY}; font-style: italic; font-size: 21px; line-height: 1.4; color: {PAPER}; max-width: 480px">Each grade has ten to twelve seats, filled in the order families reserve. We’ll tell you where you stand before you pay anything.</p>
</div>
<div style="flex: 1 1 340px; min-width: 0">
<span style="display: block; font-family: {SAY}; font-style: italic; font-size: 20px; color: {GLOW}; margin-bottom: 10px">Founding families also get</span>
<ul style="list-style: none; margin: 0; padding: 0; border-bottom: 1px solid {RULE_D}">
{perk_html}</ul>
</div>
</div>
</div>
</section>
'''

    left = (faq('What subjects are taught?', 'Math, English, science and history every year, with the arts, physical education and health. That is everything New York expects of a middle school. Math, reading and writing are practiced every morning at each student’s level; history, literature and science are taught in seminar and lab.', True)
            + faq('Do students take the state tests?', 'Yes — the state tests in the spring, three mornings, no test prep. New York uses them to confirm a new school is teaching what it should, and we’d rather show that than argue about it. What you’ll see all year is growth, three times a year, for your own child.')
            + faq('What happens after eighth grade?', 'Ninth grade opens here in September 2028, then a grade every year through twelfth. Your child can stay, or move on with a folder of work that shows what they can do: made, defended, and grown, every six weeks.')
            + faq('Where will the school be?', 'On the North Shore, along the Miller Place–Port Jefferson Station corridor. Port Jefferson Station is the likeliest. We announce the address the day we sign the lease.'))
    right = (faq('How do I apply?', 'Ask for a call. It is twenty minutes with one of the four of us, and there is no application fee. If it’s a fit, $500 reserves a seat, and the enrollment contract follows.', True)
             + faq('What if the school doesn’t open?', 'Your $500 is held by an independent escrow agent, not by us, and it comes back in full, for any reason, until the day we sign a lease. If the school doesn’t open after that, your money comes back too: we mail you a check.')
             + faq('Will our district bus my child?', 'Most likely. New York districts provide transportation to private schools up to fifteen miles away. You request it from your own district by April 1, and we’ll send you the request already filled in.'))
    o += f'''<section id="questions" style="padding: {PAD} 0 clamp(56px, 7vw, 104px)">
<div style="{WP}">
{ph2('Questions families ask.', maxw='14ch', mb='48px')}
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(380px, 100%), 1fr)); gap: 8px 72px; align-items: start">
<div style="min-width: 0; border-bottom: 1px solid {RULE_P}">
{left}</div>
<div style="min-width: 0; border-bottom: 1px solid {RULE_P}">
{right}</div>
</div>
<div style="margin-top: 36px">{quiet('Every question, with tuition', 'join.html#questions')}</div>
</div>
</section>
'''

    o += call_section('home')
    o += footer() + '</div>\n' + tail(1440, H)
    return o, 1440, H


