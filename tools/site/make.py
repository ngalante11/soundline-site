"""Build the family-facing pages.   python3 tools/site/make.py   (run from anywhere)

core.py   tokens, the header and footer, shared pieces, and Home
pages.py  A day here, Tuition and admissions, Our vision, About us, The Collaborative, the federal scholarship
make.py   writes them to the repo root, moves the old addresses, puts the new header and footer on the
          research and survey pages, and writes sitemap.xml and robots.txt

The pages carry their layout inline; premium.css holds the rest. Edit the copy in core.py / pages.py and run this again.
"""
import os, re, json, html as H, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core, pages

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
SITE = 'https://soundlineschool.com/'
WHERE = 'a private middle school for grades 6–8 on Long Island’s North Shore, opening September 2027'

PAGES = [
    ('index.html', '', core.home,
     'Soundline School is ' + WHERE + '. Two hours of practice, four hours of making, ten to twelve in a grade. Tuition is published and founding enrollment is open.'),
    ('day.html', 'day.html', pages.day,
     'A school day at Soundline, 8:30 to 3:00: two hours of practice by skill, four hours of making, and one seventh grader’s Tuesday followed hour by hour.'),
    ('join.html', 'join.html', pages.admissions,
     'Tuition for 2027–28 and how to join Soundline School, ' + WHERE + '. Five days $1,500 a month, founding families $1,350. No application fee.'),
    ('vision.html', 'vision.html', pages.vision,
     'What a Soundline student can do by eighth grade, how families will know it is working, and the research behind each part of the day.'),
    ('about.html', 'about.html', pages.about,
     'Who is building Soundline School, where the name comes from, and how ten to twelve in a grade with one advisor for three years works.'),
    ('collaborative.html', 'collaborative.html', pages.collaborative,
     'The Collaborative is Soundline three days a week for homeschooling families on Long Island’s North Shore: Monday, Wednesday and Friday, with the paperwork your district reads.'),
    ('scholarship.html', 'scholarship.html', pages.scholarship,
     'What Soundline families should know about the federal scholarship tax credit that begins January 1, 2027, and where New York stands on it.'),
]

SCHOOL = {
    '@context': 'https://schema.org', '@type': 'MiddleSchool', 'name': 'Soundline School', 'url': SITE,
    'description': 'Soundline School is a private middle school for grades 6–8 on Long Island’s North Shore, opening September 2027.',
    'email': 'hello@soundlineschool.com', 'slogan': 'Depth with direction.',
    'address': {'@type': 'PostalAddress', 'addressRegion': 'NY', 'addressCountry': 'US'},
    'areaServed': 'North Shore of Long Island, Suffolk County, New York',
    'image': SITE + 'og-image.png',
}


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>\n'


def text(s):
    return H.unescape(re.sub(r'<[^>]+>', '', s)).strip()


def faq_ld(page):
    qa = re.findall(r'<details[^>]*>\s*<summary[^>]*>(.*?)</summary>\s*<p[^>]*>(.*?)</p>', page, re.S)
    if not qa:
        return ''
    return ld({'@context': 'https://schema.org', '@type': 'FAQPage',
               'mainEntity': [{'@type': 'Question', 'name': text(q), 'acceptedAnswer': {'@type': 'Answer', 'text': text(a)}} for q, a in qa]})


def check(name, page):
    bad = [b for b in ('<form', '.dc.html', '/_blob/', 'href="#"', 'x-dc', 'support.js', 'Miller Place –', 'microschool') if b in page]
    assert not bad, (name, bad)
    for m in re.finditer(r'(?:href|src)="([^"#:]+?)(?:#[^"]*)?"', page):
        t = m.group(1)
        if t.startswith('/') or t.startswith('data'):
            continue
        assert os.path.exists(os.path.join(ROOT, t)) or t in [p[0] for p in PAGES], (name, 'missing', t)


def write(rel, s):
    with open(os.path.join(ROOT, rel), 'w', encoding='utf-8') as f:
        f.write(s)


def redirect(rel, to, note):
    write(rel, f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Soundline School</title>
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url=/{to}">
<link rel="canonical" href="{SITE}{to.split('#')[0]}">
</head>
<body>
<!-- {note} -->
<p><a href="/{to}">Continue to Soundline School</a></p>
</body>
</html>
''')


def reroot(s, root):
    s = re.sub(r'href="((?:index|day|join|vision|about|collaborative|scholarship|research)\.html[^"]*|soundline-school-information\.pdf)"', lambda m: f'href="{root}{m.group(1)}"', s)
    return s.replace(f'href="{root}index.html"', f'href="{root}"') if root == '/' else s


def rechrome(rel, root, current):
    """Research and the survey keep their own body on site.css; they get the new header and footer."""
    p = os.path.join(ROOT, rel)
    s = open(p, encoding='utf-8').read()
    core.META.clear(); core.META.update(root=root)
    top, foot = reroot(core.chrome(current), root), reroot(core.footer(), root)
    if 'premium.css' not in s:
        s = re.sub(r'(<link rel="stylesheet" href="[^"]*site\.css">)', lambda m: m.group(1) + f'\n<link rel="stylesheet" href="{root}premium.css">', s, count=1)
        assert 'premium.css' in s, rel
    a, b = s.index('<!--chrome-->') if '<!--chrome-->' in s else -1, s.index('<!--/chrome-->') if '<!--/chrome-->' in s else -1
    if a >= 0:
        s = s[:a] + '<!--chrome-->\n' + top + s[b:]
    else:
        s, n = re.subn(r'[ \t]*<header class="wrap">.*?</header>\n', '', s, count=1, flags=re.S)
        assert n == 1, rel
        s = s.replace('<div class="dark">', '<!--chrome-->\n' + top + '<!--/chrome-->\n<div class="dark">', 1)
    a, b = s.index('<!--footer-->') if '<!--footer-->' in s else -1, s.index('<!--/footer-->') if '<!--/footer-->' in s else -1
    if a >= 0:
        s = s[:a] + '<!--footer-->\n' + foot + s[b:]
    else:
        s, n = re.subn(r'<footer class="dark">.*?</footer>\n', lambda m: '<!--footer-->\n' + foot + '<!--/footer-->\n', s, count=1, flags=re.S)
        assert n == 1, rel
    s = s.replace('cost.html#table', 'join.html#tuition').replace('href="cost.html"', 'href="join.html#tuition"').replace('href="sample-day.html"', 'href="day.html#tuesday"')
    write(rel, s)


def main():
    for rel, path, fn, desc in PAGES:
        core.META.clear(); core.META.update(desc=desc, path=path, root='')
        page = fn()[0]
        extra = (ld(SCHOOL) if rel == 'index.html' else '') + faq_ld(page)
        page = page.replace('</head>', extra + '</head>', 1)
        check(rel, page)
        write(rel, page)
        print(f'{rel:22} {len(page):7,}')
    redirect('cost.html', 'join.html#tuition', 'What it costs moved into Tuition and admissions. The packet and the tuition card print this address, so it stays.')
    redirect('sample-day.html', 'day.html#tuesday', 'A Tuesday now lives on A day here.')
    rechrome('research.html', '', 'vision')
    rechrome('survey/index.html', '/', '')
    urls = [(p[1], '1.0' if not p[1] else '0.8') for p in PAGES] + [('research.html', '0.5')]
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + ''.join(f'  <url><loc>{SITE}{u}</loc><priority>{pr}</priority></url>\n' for u, pr in urls) + '</urlset>\n')
    write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n')


if __name__ == '__main__':
    main()
