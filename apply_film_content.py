"""Part 03의 19개 Chapter에 film_content/*.md 원고를 반영해 새 HTML을 만든다.

입력  CVD_EDU_v1.0_Critical_Concepts.html   (수정하지 않는다)
      film_content/03-NN_*_본문.md, *_자료수집.md, figures/*
출력  CVD_EDU_v1.1_Film_Content.html

각 Chapter에서 유지하는 것: 제목(h1), 기존 핵심 개념도(figure.critical-figure, 조작 기능 포함)
바꾸는 것: 나머지 본문 전체 → 원고(12절) + 접힌 '자료 수집 기록'

표준 라이브러리만 쓴다.  실행: python3 apply_film_content.py
"""
from pathlib import Path
import re, html, base64, mimetypes, sys
import texmath

HERE = Path(__file__).resolve().parent
BASE = HERE / 'CVD_EDU_v1.0_Critical_Concepts.html'
OUT = HERE / 'CVD_EDU_v1.1_Film_Content.html'
CONTENT = HERE / 'film_content'
VERSION = 'v1.1'
DROP_CRIT = set()   # 원래 HTML의 critical figure를 넣지 않을 Chapter (예: {'03-01'})
SRC_FILTER = None   # 자료수집.md 본문을 HTML로 바꾸기 전에 거르는 함수 (v1.2: 작업 일지 문구 제거)

EV_WORDS = ('논문', '특허', '리뷰', '계산', '현장', '발표', '학회', '기사', '웹', '보고', '통설', '교과서',
            '학위', '기술', '응용', '데이터', '포럼', '소식지', '교육')
EV_CLASS = {'논문': 'p', '학회': 'p', '학위': 'p', '특허': 't', '리뷰': 'r', '교과서': 'r', '통설': 'r', '계산': 'c'}

LINK_RE = re.compile(r'\[([^\]\[]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)')
TAG_RE = re.compile(r'\[([^\[\]]{1,90})\]')
XREF_RE = re.compile(r'→ (0[0-9]-[0-9]{2})')


def inline(text):
    """한 줄(또는 문단) 안의 Markdown을 HTML로."""
    codes = []
    def stash(m):
        codes.append(html.escape(m.group(1)))
        return '\x00%d\x00' % (len(codes) - 1)
    text = re.sub(r'`([^`]+)`', stash, text)
    maths = []
    def mstash(m):
        maths.append(texmath.tex_to_mathml(m.group(1)))
        return '\x02%d\x02' % (len(maths) - 1)
    text = texmath.INLINE_RE.sub(mstash, text)
    text = html.escape(text, quote=False)
    links = []
    def link(m):
        label, url = m.group(1), m.group(2)
        ext = url.startswith('http')
        attr = ' target="_blank" rel="noopener noreferrer"' if ext else ''
        links.append('<a href="%s"%s>%s</a>' % (url.replace('"', '%22'), attr, label))
        return '\x01%d\x01' % (len(links) - 1)
    text = LINK_RE.sub(link, text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<![\*\w])\*(?!\s)([^*]+?)(?<!\s)\*(?![\*\w])', r'<em>\1</em>', text)
    def tag(m):
        body = m.group(1)
        if not (re.search(r'S\d\d', body) or body.startswith(EV_WORDS)):
            return m.group(0)
        cls = next((c for w, c in EV_CLASS.items() if body.startswith(w)), '')
        return '<span class="ev%s">%s</span>' % (' ' + cls if cls else '', body)
    text = TAG_RE.sub(tag, text)
    text = XREF_RE.sub(r'→ <a href="#" data-ref="\1">\1</a>', text)
    text = re.sub('\x01(\\d+)\x01', lambda m: links[int(m.group(1))], text)
    text = re.sub('\x00(\\d+)\x00', lambda m: '<code>%s</code>' % codes[int(m.group(1))], text)
    text = re.sub('\x02(\\d+)\x02', lambda m: maths[int(m.group(1))], text)
    return text


def split_row(line):
    s = line.strip()
    if s.startswith('|'): s = s[1:]
    if s.endswith('|'): s = s[:-1]
    return [c.strip() for c in s.split('|')]


def table(rows):
    head = split_row(rows[0])
    body = rows[2:] if len(rows) > 1 and re.match(r'^\|[\s:\-|]+\|?\s*$', rows[1]) else rows[1:]
    out = ['<div class="tw"><table><thead><tr>']
    out += ['<th>%s</th>' % inline(c) for c in head]
    out.append('</tr></thead><tbody>')
    for r in body:
        cells = split_row(r)
        cells += [''] * (len(head) - len(cells))
        out.append('<tr>' + ''.join('<td>%s</td>' % inline(c) for c in cells[:len(head)]) + '</tr>')
    out.append('</tbody></table></div>')
    return ''.join(out)


def figure(alt, src, caption, credit):
    path = CONTENT / src
    if not path.exists():
        return '<p><em>[그림 누락: %s]</em></p>' % html.escape(src)
    if path.suffix.lower() == '.svg':
        media = re.sub(r'<\?xml[^>]*\?>', '', path.read_text(encoding='utf-8')).strip()
    else:
        mime = mimetypes.guess_type(path.name)[0] or 'image/png'
        data = base64.b64encode(path.read_bytes()).decode('ascii')
        media = '<img alt="%s" src="data:%s;base64,%s"/>' % (html.escape(alt), mime, data)
    badge = '<span class="badge">원문 Figure</span>' if credit else '<span class="badge own">자체 제작 모식도</span>'
    cap = '<figcaption>%s%s</figcaption>' % (badge, inline(caption) if caption else html.escape(alt))
    cred = '<p class="credit">%s</p>' % inline(credit) if credit else ''
    return '<figure class="dfig">%s%s%s</figure>' % (media, cap, cred)


def render(md, cid, mode):
    """mode='body': 본문(절 제목을 사이드바용 h3로).  mode='src': 자료 수집(절 제목을 h4로)."""
    lines = md.split('\n')
    out, i, n = [], 0, len(lines)
    first_quote = True
    crit_marked = False
    is_block = lambda s: (s.startswith(('#', '|', '>', '```', '![', '$$')) or re.match(r'^(- |\d+\. )', s) or s.strip() == '---')
    while i < n:
        line = lines[i]
        s = line.strip()
        if not s or s == '---':
            i += 1; continue
        if s == '$$':
            j = i + 1; buf = []
            while j < n and lines[j].strip() != '$$':
                buf.append(lines[j]); j += 1
            out.append(texmath.block(buf))
            i = j + 1; continue
        if s.startswith('```'):
            j = i + 1; buf = []
            while j < n and not lines[j].strip().startswith('```'):
                buf.append(lines[j]); j += 1
            out.append('<pre class="eq">%s</pre>' % html.escape('\n'.join(buf), quote=False))
            i = j + 1; continue
        m = re.match(r'^(#{1,4})\s+(.*)$', s)
        if m:
            level, title = len(m.group(1)), m.group(2)
            if level == 1:
                pass
            elif level == 2 and mode == 'body':
                mm = re.match(r'^(\d+)\.\s+(.*)$', title)
                num, name = (int(mm.group(1)), mm.group(2)) if mm else (0, title)
                if num >= 1 and not crit_marked:
                    out.append('<!--CRITICAL-FIGURE-->'); crit_marked = True
                out.append('<h3 class="subsection-heading" id="s-%s.%02d"><span aria-hidden="true" class="section-ordinal">%02d</span>'
                           '<span class="section-title">%s</span></h3>' % (cid, num, num, inline(name)))
            else:
                out.append('<h4>%s</h4>' % inline(title))
            i += 1; continue
        if s.startswith('|'):
            j = i; rows = []
            while j < n and lines[j].strip().startswith('|'):
                rows.append(lines[j]); j += 1
            out.append(table(rows)); i = j; continue
        if s.startswith('>'):
            j = i; paras, cur = [], []
            while j < n and lines[j].strip().startswith('>'):
                t = re.sub(r'^>\s?', '', lines[j].strip())
                if t: cur.append(t)
                elif cur: paras.append(cur); cur = []
                j += 1
            if cur: paras.append(cur)
            if first_quote and mode == 'body':
                keep = [' '.join(p) for p in paras if '근거 표시' in ' '.join(p) or '공개 논문이 거의 없다' in ' '.join(p) or '근거가 가장 얇다' in ' '.join(p)]
                keep.append('근거 번호 <code>S##</code>는 이 Chapter 끝의 ‘자료 수집 기록’ 표의 ID다. 논문은 초록·요약 수준까지만 확인했다.')
                out.append('<div class="fc-head">%s</div>' % ''.join('<p>%s</p>' % (inline(p) if not p.startswith('근거 번호') else p) for p in keep))
            else:
                out.append('<div class="note">%s</div>' % ''.join('<p>%s</p>' % inline(' '.join(p)) for p in paras))
            first_quote = False
            i = j; continue
        m = re.match(r'^!\[(.*?)\]\((.*?)\)\s*$', s)
        if m:
            alt, src = m.group(1), m.group(2)
            j = i + 1; caption = credit = ''
            while j < n and not lines[j].strip(): j += 1
            for _ in range(2):
                if j < n:
                    t = lines[j].strip()
                    mc = re.match(r'^\*([^*].*)\*$', t)
                    if mc and mc.group(1).startswith('출처'):
                        credit = mc.group(1); j += 1
                    elif mc and not caption:
                        caption = mc.group(1); j += 1
                    else: break
                    while j < n and not lines[j].strip(): j += 1
            out.append(figure(alt, src, caption, credit)); i = j; continue
        m = re.match(r'^(- |\d+\. )', s)
        if m:
            ordered = not s.startswith('- ')
            j = i; items = []
            while j < n:
                t = lines[j]
                ts = t.strip()
                if re.match(r'^(- |\d+\. )', ts) and (ts.startswith('- ') != ordered):
                    items.append(re.sub(r'^(- |\d+\. )', '', ts)); j += 1
                elif ts and t.startswith(('  ', '\t')) and items:
                    items[-1] += ' ' + ts; j += 1
                else: break
            tagname = 'ol' if ordered else 'ul'
            out.append('<%s>%s</%s>' % (tagname, ''.join('<li>%s</li>' % inline(x) for x in items), tagname))
            i = j; continue
        # 문단
        j = i; buf = []
        while j < n and lines[j].strip() and not (j > i and is_block(lines[j].strip())):
            buf.append(lines[j].strip()); j += 1
        mq = re.match(r'^\*\*(Q\d+\..*)\*\*$', buf[0])
        if mq and mode == 'body':
            out.append('<details class="qa"><summary>%s</summary><div class="a"><p>%s</p></div></details>'
                       % (inline(mq.group(1)), inline(' '.join(buf[1:]))))
        else:
            out.append('<p>%s</p>' % inline(' '.join(buf)))
        i = j
    return '\n'.join(out)


def build():
    raw = BASE.read_text(encoding='utf-8')
    done = []
    for k in range(1, 20):
        cid = '03-%02d' % k
        body_md = sorted(CONTENT.glob(cid + '_*_본문.md'))
        src_md = sorted(CONTENT.glob(cid + '_*_자료수집.md'))
        assert len(body_md) == 1 and len(src_md) == 1, cid
        tpl = re.search(r'(<template id="tpl-%s">)(.*?)(</template>)' % cid, raw, flags=re.S)
        assert tpl, cid
        old = tpl.group(2)
        h1 = re.search(r'<h1 class="chapter-heading"[^>]*>.*?</h1>', old, flags=re.S).group(0)
        crit = re.search(r'<figure class="critical-figure" id="critical-%s">.*?</figure>' % cid, old, flags=re.S).group(0)
        body = render(body_md[0].read_text(encoding='utf-8'), cid, 'body')
        assert '<!--CRITICAL-FIGURE-->' in body, cid
        body = body.replace('<!--CRITICAL-FIGURE-->', '' if cid in DROP_CRIT else crit, 1)
        src_text = src_md[0].read_text(encoding='utf-8')
        srcs = render(SRC_FILTER(src_text) if SRC_FILTER else src_text, cid, 'src')
        n_src = len(re.findall(r'^\|\s*S\d\d\s*\|', src_md[0].read_text(encoding='utf-8'), flags=re.M))
        new = ('<p class="part03-label">PART 03 · FILM ENGINEERING  /  %s 원고 반영</p>%s\n<div class="fc">\n%s\n'
               '<details class="srcs"><summary>자료 수집 기록 · 출처 %d건과 확인 수준</summary>\n%s\n</details>\n'
               '<p class="rev">%s · %s 원고와 자료 수집 기록은 film_content/ 폴더의 Markdown에서 생성했다.</p>\n</div>'
               % (VERSION, h1, body, n_src, srcs, cid, VERSION))
        raw = raw[:tpl.start(2)] + new + raw[tpl.end(2):]
        raw, c = re.subn(r'(<button[^>]*data-ch="%s"[^>]*>.*?<small>)[^<]*(</small>)' % cid, r'\g<1>개정\g<2>', raw, count=1, flags=re.S)
        done.append((cid, len(body), n_src, c))
    css = (HERE / 'film_content.css').read_text(encoding='utf-8')
    raw = raw.replace('</head>', '<style id="film-content-%s">\n%s</style></head>' % (VERSION, css), 1)
    raw = re.sub(r'(<title>)([^<]*?)( v0\.9)?(</title>)', r'\g<1>\g<2> %s\g<4>' % VERSION, raw, count=1)
    OUT.write_text(raw, encoding='utf-8')
    return done


def verify():
    t = OUT.read_text(encoding='utf-8')
    assert len(re.findall(r'<template id="tpl-', t)) == 89, 'template 수'
    assert len(re.findall(r'<figure class="critical-figure"', t)) == 19 - len(DROP_CRIT), 'critical figure 수'
    assert not re.findall(r'<img[^>]+src="https?:', t), '원격 이미지'
    assert ('03-01' in DROP_CRIT or 'id="acl-h"' in t) and ('03-06' in DROP_CRIT or 'id="reflow-top"' in t), '조작 기능'
    for k in range(1, 20):
        cid = '03-%02d' % k
        b = re.search(r'<template id="tpl-%s">(.*?)</template>' % cid, t, flags=re.S).group(1)
        assert len(re.findall(r'<h3 class="subsection-heading" id="s-%s\.\d\d"' % re.escape(cid), b)) == 13, cid + ' 절 수'
        assert '그림 누락' not in b, cid + ' 그림'
        assert b.count('<div') == b.count('</div>') and b.count('<details') == b.count('</details>'), cid + ' 태그 짝'
    return True


if __name__ == '__main__':
    rows = build()
    verify()
    for cid, size, n_src, nav in rows:
        print(cid, '본문 HTML %6d자' % size, '출처 %2d건' % n_src, 'nav' if nav else 'nav 미변경')
    print('PASS: 89 templates, 19 critical figures, 19 chapters × 13 sections, 0 remote images')
    print('wrote', OUT.name, OUT.stat().st_size, 'bytes')
