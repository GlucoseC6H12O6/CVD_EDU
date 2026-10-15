"""v1.1 HTML에서 Part 03을 뺀 70개 Chapter의 본문을 원고(Markdown)로 꺼낸다.

출력  textbook/NN-NN.md          다시 쓸 원고. 그림·수식·계산기 같은 블록은 {{keep:n}} 한 줄로 남긴다.
      textbook/_keep/NN-NN.json  {{keep:n}}의 원래 HTML, 그리고 Chapter 머리(headlines, h1)

이미 있는 원고는 덮어쓰지 않는다(--force일 때만).  실행: python3 extract_textbook.py
"""
from pathlib import Path
from html.parser import HTMLParser
import re, json, html, sys

HERE = Path(__file__).resolve().parent
SRC = HERE / 'CVD_EDU_v1.1_Film_Content.html'
OUT = HERE / 'textbook'
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}


class Tree(HTMLParser):
    """최상위 요소의 (tag, attrs, start, end)만 기록한다."""
    def __init__(self, text):
        super().__init__(convert_charrefs=False)
        self.text = text
        self.lines = [0]
        for m in re.finditer('\n', text):
            self.lines.append(m.end())
        self.stack, self.top = [], []

    def off(self):
        ln, col = self.getpos()
        return self.lines[ln - 1] + col

    def handle_starttag(self, tag, attrs):
        start = self.off()
        end_of_tag = self.text.index('>', start) + 1
        if tag in VOID:
            if not self.stack:
                self.top.append((tag, dict(attrs), start, end_of_tag))
            return
        self.stack.append((tag, dict(attrs), start))

    def handle_startendtag(self, tag, attrs):
        start = self.off()
        if not self.stack:
            self.top.append((tag, dict(attrs), start, self.text.index('>', start) + 1))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        end = self.text.index('>', self.off()) + 1
        while self.stack:
            t, a, s = self.stack.pop()
            if t == tag:
                if not self.stack:
                    self.top.append((t, a, s, end))
                return


INLINE_OK = {'strong', 'b', 'em', 'i', 'code', 'a', 'sub', 'sup', 'br', 'span'}


def md_inline(h):
    """문단 안 HTML → Markdown. 바꿀 수 없는 태그가 있으면 None."""
    tags = set(re.findall(r'</?([a-z0-9]+)', h))
    if tags - INLINE_OK:
        return None
    if re.search(r'<span(?![^>]*class="ev)', h):
        return None
    s = h
    s = re.sub(r'<a [^>]*class="knowledge-ref"[^>]*data-ref="([^"]+)"[^>]*>(.*?)</a>', r'[\2](#kref:\1)', s, flags=re.S)
    s = re.sub(r'<a [^>]*data-ref="([^"]+)"[^>]*>(.*?)</a>', r'[\2](#ref:\1)', s, flags=re.S)
    s = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', s, flags=re.S)
    s = re.sub(r'</?(strong|b)>', '**', s)
    s = re.sub(r'</?(em|i)>', '*', s)
    s = re.sub(r'<code>(.*?)</code>', r'`\1`', s, flags=re.S)
    s = re.sub(r'<sub>(.*?)</sub>', r'<sub>\1</sub>', s)
    s = re.sub(r'<br\s*/?>', ' ', s)
    if re.search(r'<(?!/?su[bp]>)', s):
        return None
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()


def chapter(cid, body):
    p = Tree(body)
    p.feed(body)
    p.close()
    head, keep, md, h2 = [], [], [], []
    title = ''
    for tag, a, s, e in p.top:
        raw = body[s:e]
        inner = re.sub(r'^<[^>]+>|</[a-z0-9]+>$', '', raw, flags=re.S)
        cls = a.get('class', '')
        if tag == 'div' and cls == 'headlines' or tag == 'h1':
            head.append(raw)
            if tag == 'h1':
                title = html.unescape(re.sub(r'<[^>]+>', '', inner)).strip()
            continue
        if tag == 'h3' and 'subsection-heading' in cls:
            num = re.search(r'id="s-[0-9-]+\.(\d\d)"', raw).group(1)
            name = html.unescape(re.sub(r'<[^>]+>', '', re.search(r'<span class="section-title">(.*?)</span>', raw, flags=re.S).group(1)))
            md += ['', '## %d. %s' % (int(num), name.strip()), '']
            continue
        if tag == 'h2' and 'section-heading' in cls:
            h2.append(re.match(r'<h2[^>]*>', raw).group(0))
            md += ['', '## %s {h2:%d}' % (html.unescape(re.sub(r'<[^>]+>', '', inner)).strip(), len(h2) - 1), '']
            continue
        if tag in ('h4', 'h3') and not cls:
            md += ['', '### %s' % html.unescape(re.sub(r'<[^>]+>', '', inner)).strip(), '']
            continue
        if tag == 'p' and not cls:
            t = md_inline(inner)
            if t is not None:
                md += [t, '']
                continue
        if tag == 'blockquote' and '<' not in inner:
            md += ['> ' + re.sub(r'\s+', ' ', html.unescape(inner)).strip(), '']
            continue
        if tag == 'table' and not cls:
            rows = re.findall(r'<tr>(.*?)</tr>', inner, flags=re.S)
            cells = [[md_inline(c) for c in re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', r, flags=re.S)] for r in rows]
            if rows and all(c is not None for r in cells for c in r) and '<th' in rows[0]:
                md += ['| ' + ' | '.join(c.replace('|', '/') for c in cells[0]) + ' |', '|' + '---|' * len(cells[0])]
                md += ['| ' + ' | '.join(c.replace('|', '/') for c in r) + ' |' for r in cells[1:]] + ['']
                continue
        if tag == 'blockquote':
            ps = re.findall(r'<p>(.*?)</p>', inner, flags=re.S)
            ts = [md_inline(x) for x in ps]
            if ps and all(t is not None for t in ts) and not re.sub(r'<p>.*?</p>', '', inner, flags=re.S).strip():
                for k, t in enumerate(ts):
                    md += (['>'] if k else []) + ['> ' + t]
                md += ['']
                continue
        if tag in ('ul', 'ol') and not cls:
            lis = re.findall(r'<li>(.*?)</li>', inner, flags=re.S)
            ts = [md_inline(x) for x in lis]
            if lis and all(t is not None for t in ts):
                md += [('- ' if tag == 'ul' else '%d. ' % (k + 1)) + t for k, t in enumerate(ts)] + ['']
                continue
        keep.append(raw)
        md += ['{{keep:%d}}' % (len(keep) - 1), '']
    text = re.sub(r'\n{3,}', '\n\n', '\n'.join(md)).strip() + '\n'
    return head, keep, h2, title, text


def main(force=False):
    t = SRC.read_text(encoding='utf-8')
    (OUT / '_keep').mkdir(parents=True, exist_ok=True)
    n = 0
    for cid, body in re.findall(r'<template id="tpl-(\d\d-\d\d)">(.*?)</template>', t, flags=re.S):
        if cid.startswith('03-'):
            continue
        head, keep, h2, title, text = chapter(cid, body)
        (OUT / '_keep' / (cid + '.json')).write_text(json.dumps({'head': head, 'keep': keep, 'h2': h2}, ensure_ascii=False, indent=0), encoding='utf-8')
        f = OUT / (cid + '.md')
        if f.exists() and not force:
            continue
        f.write_text('# %s · %s\n\n%s' % (cid, title, text), encoding='utf-8')
        n += 1
        print('%s  keep %2d  %5d자  %s' % (cid, len(keep), len(text), title))
    print('원고', n, '개 작성')


if __name__ == '__main__':
    main('--force' in sys.argv)
