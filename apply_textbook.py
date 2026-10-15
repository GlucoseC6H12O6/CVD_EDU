"""v1.2 — 89개 Chapter 전체를 교과서 원고로 만든다.

입력  CVD_EDU_v1.0_Critical_Concepts.html        (수정하지 않는다)
      film_content/03-NN_*_본문.md, *_자료수집.md   Part 03의 19개 Chapter
      textbook/NN-NN.md, textbook/_keep/NN-NN.json  나머지 70개 Chapter (extract_textbook.py로 꺼낸 원고)
출력  CVD_EDU_v1.2_Textbook.html

textbook 원고 문법은 film_content와 같다. 추가로
  ## 3. 제목          → 사이드바 절 제목(h3.subsection-heading, id s-NN-NN.03)
  ## 제목 {h2:N}      → 원래 h2.section-heading(id·data-section 그대로)
  ### 제목            → h4
  {{keep:N}}          → 원래 HTML 블록(그림·수식·계산기 등) 그대로
  [글](#ref:02-03)    → Chapter 간 연결

표준 라이브러리만 쓴다.  실행: python3 apply_textbook.py
"""
from pathlib import Path
import re, json, html
import apply_film_content as A
import texmath

HERE = Path(__file__).resolve().parent
TB = HERE / 'textbook'
OUT = HERE / 'CVD_EDU_v1.2_Textbook.html'
inline, table = A.inline, A.table


def render(md, cid, store):
    lines = md.split('\n')
    out, i, n = [], 0, len(lines)
    sec, sub = 0, 0
    is_block = lambda s: (s.startswith(('#', '|', '>', '```', '![', '{{keep:', '$$')) or re.match(r'^(- |\d+\. )', s) or s.strip() == '---')
    while i < n:
        s = lines[i].strip()
        if not s or s == '---':
            i += 1; continue
        m = re.match(r'^\{\{keep:(\d+)\}\}$', s)
        if m:
            out.append(store['keep'][int(m.group(1))]); i += 1; continue
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
            level, title = len(m.group(1)), m.group(2).strip()
            if level == 2:
                mh = re.match(r'^(.*?)\s*\{h2:(\d+)\}$', title)
                mn = re.match(r'^(\d+)\.\s+(.*)$', title)
                if mh:
                    out.append('%s%s</h2>' % (store['h2'][int(mh.group(2))], inline(mh.group(1))))
                elif mn:
                    sec, sub = int(mn.group(1)), 0
                    out.append('<h3 class="subsection-heading" id="s-%s.%02d"><span aria-hidden="true" class="section-ordinal">%02d</span>'
                               '<span class="section-title">%s</span></h3>' % (cid, sec, sec, inline(mn.group(2))))
                else:
                    out.append('<h2 class="section-heading">%s</h2>' % inline(title))
            elif level == 3:
                sub += 1
                hid = ' id="s-%s.%02d.%02d"' % (cid, sec, sub) if sec else ''
                out.append('<h4%s>%s</h4>' % (hid, inline(title)))
            elif level == 4:
                out.append('<h5>%s</h5>' % inline(title))
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
            out.append('<div class="note">%s</div>' % ''.join('<p>%s</p>' % inline(' '.join(p)) for p in paras))
            i = j; continue
        m = re.match(r'^!\[(.*?)\]\((.*?)\)\s*$', s)
        if m:
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
            out.append(A.figure(m.group(1), m.group(2), caption, credit)); i = j; continue
        m = re.match(r'^(- |\d+\. )', s)
        if m:
            ordered = not s.startswith('- ')
            j = i; items = []
            while j < n:
                t = lines[j]; ts = t.strip()
                if re.match(r'^(- |\d+\. )', ts) and (ts.startswith('- ') != ordered):
                    items.append(re.sub(r'^(- |\d+\. )', '', ts)); j += 1
                elif ts and t.startswith(('  ', '\t')) and items:
                    items[-1] += ' ' + ts; j += 1
                else: break
            tag = 'ol' if ordered else 'ul'
            out.append('<%s>%s</%s>' % (tag, ''.join('<li>%s</li>' % inline(x) for x in items), tag))
            i = j; continue
        j = i; buf = []
        while j < n and lines[j].strip() and not (j > i and is_block(lines[j].strip())):
            buf.append(lines[j].strip()); j += 1
        mq = re.match(r'^\*\*(Q\d+\..*)\*\*$', buf[0])
        if mq:
            out.append('<details class="qa"><summary>%s</summary><div class="a"><p>%s</p></div></details>'
                       % (inline(mq.group(1)), inline(' '.join(buf[1:]))))
        else:
            out.append('<p>%s</p>' % inline(' '.join(buf)))
        i = j
    h = '\n'.join(out)
    h = re.sub(r'<a href="#kref:([0-9]{2}-[0-9]{2})">', r'<a class="knowledge-ref" data-ref="\1" href="#">', h)
    h = re.sub(r'<a href="#ref:([0-9]{2}-[0-9]{2})">', r'<a data-ref="\1" href="#">', h)
    h = h.replace('&lt;sub&gt;', '<sub>').replace('&lt;/sub&gt;', '</sub>').replace('&lt;sup&gt;', '<sup>').replace('&lt;/sup&gt;', '</sup>')
    return h


def build():
    A.OUT, A.VERSION = OUT, 'v1.2'
    # 원래 HTML의 Part 03 첫머리 자체 제작 개념도(슬라이더 포함)는 넣지 않는다 (2026-10-15 사용자 요청).
    # 그 자리의 실제 그림은 film_content 원고 본문에 있다.
    A.DROP_CRIT = {'03-%02d' % k for k in range(1, 20)}
    A.build()                      # Part 03 (film_content) → OUT
    A.verify()
    raw = OUT.read_text(encoding='utf-8')
    raw = raw.replace('/  v1.2 원고 반영', '/  v1.2 교과서 원고')
    figs = figure_overrides()
    maths = math_overrides()
    done = []
    for f in sorted(TB.glob('[0-9][0-9]-[0-9][0-9].md')):
        cid = f.stem
        store = json.loads((TB / '_keep' / (cid + '.json')).read_text(encoding='utf-8'))
        # 원본(v1.0) 각주에 Markdown 굵게 표시가 그대로 남은 곳을 고친다
        store['keep'] = [re.sub(r'(<p class="gas-footnote">[^<]*?)\*\*([^*<]+)\*\*', r'\1<strong>\2</strong>', k) for k in store['keep']]
        dropped_ids = set()       # 실제 그림으로 바꾼 자체 제작 그림 안의 id(그 그림을 그리던 스크립트는 요소가 없으면 그냥 끝난다)
        for (c, k), h in figs.items():
            if c == cid:
                dropped_ids |= set(re.findall(r'\bid="([^"]+)"', store['keep'][k]))
                store['keep'][k] = h
        for (c, k), tex in maths.items():
            if c == cid:
                old_k = store['keep'][k]
                assert '<math' in old_k, (cid, k, '수식 상자가 아님')
                store['keep'][k] = re.sub(r'<math\b.*?</math>', lambda _m: texmath.tex_to_mathml(tex, display=True), old_k, count=1, flags=re.S)
        md = f.read_text(encoding='utf-8')
        used = [int(x) for x in re.findall(r'^\{\{keep:(\d+)\}\}\s*$', md, flags=re.M)]
        assert sorted(used) == list(range(len(store['keep']))), (cid, 'keep 블록 누락·중복', sorted(used))
        tpl = re.search(r'(<template id="tpl-%s">)(.*?)(</template>)' % cid, raw, flags=re.S)
        old = tpl.group(2)
        body = render(md, cid, store)
        new = '%s\n<div class="fc tb">\n%s\n<p class="rev">%s · v1.2 교과서 원고는 textbook/%s.md에서 생성했다.</p>\n</div>' % ('\n'.join(store['head']), body, cid, cid)
        check(cid, old, new, render(md, cid, dict(store, keep=[''] * len(store['keep']))), dropped_ids)
        raw = raw[:tpl.start(2)] + new + raw[tpl.end(2):]
        raw, c = re.subn(r'(<button[^>]*data-ch="%s"[^>]*>.*?<small>)[^<]*(</small>)' % cid, r'\g<1>개정\g<2>', raw, count=1, flags=re.S)
        done.append((cid, len(body)))
    # 탭 제목: 원래 HTML은 Part 03만 다루던 시절의 제목을 그대로 쓰고 있었다
    raw = re.sub(r'<title>[^<]*</title>', '<title>CVD Engineering Knowledge — CVD 엔지니어 교과서 v1.2</title>', raw, count=1)
    OUT.write_text(raw, encoding='utf-8')
    return done


def figure_overrides():
    """textbook/_figures.md: '## CID keep:N' 아래 내용으로 보존 블록 N을 바꾼다(비어 있으면 뺀다)."""
    p = TB / '_figures.md'
    if not p.exists():
        return {}
    out = {}
    parts = re.split(r'^## (\d\d-\d\d) keep:(\d+)\s*$', p.read_text(encoding='utf-8'), flags=re.M)
    for i in range(1, len(parts), 3):
        cid, k, body = parts[i], int(parts[i + 1]), parts[i + 2].strip()
        h = A.render(body, cid, 'src') if body else ''
        assert '그림 누락' not in h, (cid, k, '그림 파일 없음')
        out[(cid, k)] = h
    return out


def math_overrides():
    """textbook/_math.md: '## CID keep:N' 아래 한 줄의 LaTeX로 그 보존 블록의 수식을 바꾼다."""
    p = TB / '_math.md'
    if not p.exists():
        return {}
    parts = re.split(r'^## (\d\d-\d\d) keep:(\d+)\s*$', p.read_text(encoding='utf-8'), flags=re.M)
    return {(parts[i], int(parts[i + 1])): parts[i + 2].strip() for i in range(1, len(parts), 3)}


H4ID = re.compile(r'^(s-\d\d-\d\d\.\d\d\.\d\d|anchor-.*)$')


def check(cid, old, new, body_only, dropped_ids=frozenset()):
    ids_old = {x for x in re.findall(r'\bid="([^"]+)"', old) if not H4ID.match(x)} - set(dropped_ids)
    ids_new = set(re.findall(r'\bid="([^"]+)"', new))
    lost = ids_old - ids_new
    assert not lost, (cid, '사라진 id', sorted(lost)[:8])
    h3o = re.findall(r'<h3 class="subsection-heading" id="([^"]+)"', old)
    h3n = re.findall(r'<h3 class="subsection-heading" id="([^"]+)"', new)
    assert h3o == h3n, (cid, '절 구성이 원본과 다름', h3o, h3n)
    for tag in ('div', 'details', 'figure', 'section', 'table'):
        assert new.count('<' + tag) == new.count('</%s>' % tag), (cid, tag, '태그 짝')
    text = re.sub(r'<(svg|math|script|style)\b.*?</\1>', '', body_only, flags=re.S)
    text = re.sub(r'<[^>]+>', ' ', text)
    for bad in ('{{keep', '{h2:', '](#', '**', '$'):
        assert bad not in text, (cid, '변환 안 된 표기', bad)


def verify():
    t = OUT.read_text(encoding='utf-8')
    assert len(re.findall(r'<template id="tpl-', t)) == 89
    ids = set(re.findall(r'<template id="tpl-(\d\d-\d\d)"', t))
    bad = sorted(set(re.findall(r'data-ref="([^"]+)"', t)) - ids)
    assert not bad, ('없는 Chapter를 가리키는 연결', bad)
    assert 'class="critical-figure"' not in t and 'id="acl-h"' not in t and 'id="reflow-top"' not in t
    for (c, k), h in figure_overrides().items():
        tpl = re.search(r'<template id="tpl-%s">(.*?)</template>' % c, t, flags=re.S).group(1)
        assert (h and 'class="dfig"' in tpl) or not h, (c, k, '교체 그림 없음')


if __name__ == '__main__':
    rows = build()
    verify()
    print('textbook Chapter %d개 반영' % len(rows))
    print('PASS: 89 templates, Part 03 검증 + 70개 Chapter의 id·절 구성·보존 블록·태그 짝·Chapter 연결 확인')
    print('wrote', OUT.name, OUT.stat().st_size, 'bytes')
