"""v1.2 — 원래 89개 Chapter와 새로 더한 Chapter(Part 10)를 교과서 원고로 만든다.

입력  CVD_EDU_v1.0_Critical_Concepts.html        (수정하지 않는다)
      film_content/03-NN_*_본문.md, *_자료수집.md   Part 03의 19개 Chapter
      textbook/NN-NN.md, textbook/_keep/NN-NN.json  나머지 70개 Chapter (extract_textbook.py로 꺼낸 원고)
      textbook/10-NN.md (_keep 없음)               원래 HTML에 없던 새 Chapter (add_chapter)
      textbook_ui.css, textbook_ui.js              읽기 도구(근거 호버, 다음 장 자동 넘김)
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
    A.SRC_FILTER = reader_srcs
    A.build()                      # Part 03 (film_content) → OUT
    A.verify()
    raw = OUT.read_text(encoding='utf-8')
    # Part 03 머리표를 다른 Part와 같은 형식으로 (원래는 판 번호가 붙어 있었다)
    raw = re.sub(r'<p class="part03-label">[^<]*</p>(<h1 class="chapter-heading" id="s-(03-\d\d)")',
                 r'<div class="headlines">PART 03 · CHAPTER \2</div>\n\1', raw)
    raw = raw.replace('근거 번호 <code>S##</code>는 이 Chapter 끝의 ‘자료 수집 기록’ 표의 ID다.',
                      '근거 번호 <code>S##</code>는 이 장 끝 ‘출처와 확인 수준’ 표의 번호다. 표시에 마우스를 올리면 그 출처가 뜬다.')
    raw = re.sub(r'<summary>자료 수집 기록 · 출처 (\d+)건과 확인 수준</summary>', r'<summary>출처와 확인 수준 · \1건</summary>', raw)
    figs = figure_overrides()
    maths = math_overrides()
    texts = text_overrides()
    done, added = [], []
    for f in sorted(TB.glob('[0-9][0-9]-[0-9][0-9].md')):
        cid = f.stem
        if not (TB / '_keep' / (cid + '.json')).exists():
            added.append(f)        # 원래 HTML에 없는 새 Chapter(Part 10 등)
            continue
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
        for (c, k), pairs in texts.items():
            if c == cid:
                for old_t, new_t in pairs:
                    assert store['keep'][k].count(old_t) == 1, (cid, k, old_t)
                    store['keep'][k] = store['keep'][k].replace(old_t, html.escape(new_t, quote=False))
        md = f.read_text(encoding='utf-8')
        used = [int(x) for x in re.findall(r'^\{\{keep:(\d+)\}\}\s*$', md, flags=re.M)]
        assert sorted(used) == list(range(len(store['keep']))), (cid, 'keep 블록 누락·중복', sorted(used))
        tpl = re.search(r'(<template id="tpl-%s">)(.*?)(</template>)' % cid, raw, flags=re.S)
        old = tpl.group(2)
        body = render(md, cid, store)
        new = '%s\n<div class="fc tb">\n%s\n</div>' % ('\n'.join(store['head']), body)
        check(cid, old, new, render(md, cid, dict(store, keep=[''] * len(store['keep']))), dropped_ids)
        raw = raw[:tpl.start(2)] + new + raw[tpl.end(2):]
        done.append((cid, len(body)))
    for f in added:
        raw = add_chapter(raw, f)
        done.append((f.stem, 0))
    raw = chapter_titles(raw)
    raw = reader_chrome(raw)
    OUT.write_text(raw, encoding='utf-8')
    return done


# 원래 HTML에 없는 Part의 사이드바 제목
NEW_PARTS = {'10': 'Device Integration — Logic · DRAM · NAND'}


def add_chapter(raw, f):
    """textbook/NN-NN.md 중 원래 HTML에 template이 없는 Chapter를 새로 넣는다.
    첫 줄 '# NN-NN · English Name — 한국어 부제'에서 제목을, '## N. 제목'에서 절을 읽는다."""
    cid, md = f.stem, f.read_text(encoding='utf-8')
    assert '<template id="tpl-%s">' % cid not in raw, (cid, '이미 있는 Chapter')
    title = re.match(r'^# \d\d-\d\d · (.+)$', md.split('\n', 1)[0]).group(1).strip()
    name = title.split(' — ')[0].strip()
    plans = re.findall(r'^## \d+\.\s+(.+)$', md, flags=re.M)
    body = render(md, cid, {'keep': [], 'h2': []})
    for tag in ('div', 'details', 'figure', 'table', 'ul', 'ol'):
        assert body.count('<' + tag) == body.count('</%s>' % tag), (cid, tag, '태그 짝')
    assert '그림 누락' not in body, (cid, '그림 파일 없음')
    text = re.sub(r'<(svg|math|script|style)\b.*?</\1>', '', body, flags=re.S)
    text = re.sub(r'<[^>]+>', ' ', text)
    for bad in ('{{keep', '{h2:', '](#', '**', '$'):
        assert bad not in text, (cid, '변환 안 된 표기', bad)
    part = cid[:2]
    tpl = ('<template id="tpl-%s"><div class="headlines">PART %s · CHAPTER %s</div>\n'
           '<h1 class="chapter-heading" id="s-%s">%s</h1>\n<div class="fc tb">\n%s\n</div></template>'
           % (cid, part, cid, cid, html.escape(title, quote=False), body))
    i = raw.rindex('</template>') + len('</template>')
    raw = raw[:i] + '\n' + tpl + raw[i:]
    btn = ('<button aria-current="false" class="chapter-link" data-ch="%s" type="button"><span class="chapter-id">%s</span>'
           '<strong>%s</strong></button>' % (cid, cid[3:], html.escape(name, quote=False)))
    if 'data-part="%s"' % part in raw:
        m = re.search(r'(<details class="part-disclosure" data-part="%s">.*?)(</div></details>)' % part, raw, flags=re.S)
        raw = raw[:m.end(1)] + btn + raw[m.end(1):]
    else:
        det = ('<details class="part-disclosure" data-part="%s"><summary>PART %s · %s</summary><div class="chapter-nav-items">%s</div></details>'
               % (part, part, html.escape(NEW_PARTS[part], quote=False), btn))
        i = raw.index('</div></aside>')
        raw = raw[:i] + det + raw[i:]
    for var, val in (('chapters', {'name': name, 'ready': True}), ('allNames', name), ('chapterPlans', plans)):
        m = re.search(r'const %s=(\{.*?\});' % var, raw)
        obj = json.loads(m.group(1)); obj[cid] = val
        raw = raw[:m.start(1)] + json.dumps(obj, ensure_ascii=False) + raw[m.end(1):]
    return raw


def chapter_titles(raw):
    """장 제목(h1)은 원래 HTML이 아니라 원고 첫 줄 '# NN-NN · 제목'에서 가져온다."""
    srcs = sorted(TB.glob('[0-9][0-9]-[0-9][0-9].md')) + sorted(A.CONTENT.glob('03-[0-9][0-9]_*_본문.md'))
    for f in srcs:
        m = re.match(r'# (\d\d-\d\d) · (.+?)\s*$', f.read_text(encoding='utf-8').split('\n', 1)[0])
        assert m, (f.name, '첫 줄 제목 형식')
        cid, title = m.groups()
        raw, n = re.subn(r'(<h1 class="chapter-heading" id="s-%s">).*?(</h1>)' % cid,
                         lambda mm: mm.group(1) + inline(title) + mm.group(2), raw, flags=re.S)
        assert n == 1, (cid, 'h1 개수', n)
    return raw


def reader_chrome(raw):
    """독자에게 쓸모없는 제작 정보(판 번호, 원고 파일 이름, '1차 집필본', 장마다 붙은 초안·개정 표시)를 빼고
    읽기 도구(textbook_ui.css/js: 근거 호버, 다음 장 자동 넘김)를 넣는다 (2026-10-16 사용자 요청)."""
    raw = re.sub(r'\n?<p class="rev">[^<]*</p>', '', raw)
    raw = re.sub(r'<div class="kicker">[^<]*</div>', '', raw, count=1)
    raw = re.sub(r'<span class="topright">[^<]*</span>', '', raw, count=1)
    raw = re.sub(r'(<button[^>]*class="chapter-link"[^>]*>.*?)<small>[^<]*</small>', r'\1', raw, flags=re.S)
    raw = re.sub(r'<meta content="[^"]*" name="cvdedu-revision"/>', '', raw)
    # 사이드바 머리의 홍보 문구("읽고, 계산하고, 다시 돌아오는 교과서")는 책 이름으로 바꾼다
    raw, n = re.subn(r'(<div class="brand"><b>[^<]*<br/>[^<]*</b>)<p>.*?</p>', r'\1<p>CVD 엔지니어 교과서</p>', raw, count=1)
    assert n == 1, '사이드바 머리 문구'
    # 탭 제목: 원래 HTML은 Part 03만 다루던 시절의 제목을 그대로 쓰고 있었다
    raw = re.sub(r'<title>[^<]*</title>', '<title>CVD Engineering Knowledge — CVD 엔지니어 교과서</title>', raw, count=1)
    css = (HERE / 'textbook_ui.css').read_text(encoding='utf-8')
    js = (HERE / 'textbook_ui.js').read_text(encoding='utf-8')
    raw = raw.replace('</head>', '<style id="textbook-ui">\n%s</style></head>' % css, 1)
    i = raw.rindex('</body>')
    raw = raw[:i] + '<script id="textbook-ui-js">\n%s</script>\n' % js + raw[i:]
    return raw


def reader_srcs(md):
    """Part 03 자료수집.md를 장 끝 '출처와 확인 수준'으로 보일 때 작업 일지 문구를 뺀다.
    원본 md(연구 기록)는 그대로 두고 HTML에만 적용한다."""
    keep = []
    for sec in re.split(r'(?m)^(?=## )', md):
        head = sec.split('\n', 1)[0]
        has_rows = re.search(r'(?m)^\|\s*S\d\d\s*\|', sec)
        if not has_rows and re.search(r'재검색 기록|사진 후보 검토|기존 본문\(v0\.9', head):
            continue
        keep.append(sec)
    md = ''.join(keep)
    md = re.sub(r'(?m)^수집일:.*\n', '', md)
    md = re.sub(r'(?m)^(- |\d+\. )?(사용자 요청으로|기존 사용자 BPSG|사용자 보유 BPSG).*\n', '', md)
    md = md.replace('본문 첫머리에 있던 자체 제작 개념도는 빌드에서 뺐다. ', '')
    md = re.sub(r'(?m)^## SEM·TEM 사진 추가.*$', '## 본문에 넣은 전자현미경 사진', md)
    md = re.sub(r'(?m)^## (\d+\. )?2026-\d\d-\d\d 보강 기록', r'## \1보강 자료', md)
    md = re.sub(r'\s*\(20\d\d-\d\d-\d\d[^)]*\)', '', md)
    md = re.sub(r'20\d\d-\d\d-\d\d:\s*', '', md)
    md = md.replace('기존 HTML(v0.9.1)', '이전 판').replace('기존 HTML', '이전 판')
    return md


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


def text_overrides():
    """textbook/_text.md: '- CID keep:N | 원래 문구 | 바꾼 문구' 줄로 보존 블록 안의 문구를 바꾼다."""
    p = TB / '_text.md'
    out = {}
    if p.exists():
        for m in re.finditer(r'^- (\d\d-\d\d) keep:(\d+) \| (.+?) \| (.+?)\s*$', p.read_text(encoding='utf-8'), flags=re.M):
            out.setdefault((m.group(1), int(m.group(2))), []).append((m.group(3), m.group(4)))
    return out


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
    n_md = len(list(TB.glob('[0-9][0-9]-[0-9][0-9].md'))) + 19
    assert len(re.findall(r'<template id="tpl-', t)) == n_md, ('template 수', n_md)
    ids = set(re.findall(r'<template id="tpl-(\d\d-\d\d)"', t))
    assert ids == set(re.findall(r'<button[^>]*class="chapter-link" data-ch="(\d\d-\d\d)"', t)), '사이드바와 template 불일치'
    for meta in ('first draft', '1차 집필본', '생성했다.</p>', 'class="rev"'):
        assert meta not in t, ('제작 정보 문구가 남음', meta)
    bad = sorted(set(re.findall(r'data-ref="([^"]+)"', t)) - ids)
    assert not bad, ('없는 Chapter를 가리키는 연결', bad)
    assert 'class="critical-figure"' not in t and 'id="acl-h"' not in t and 'id="reflow-top"' not in t
    for (c, k), h in figure_overrides().items():
        tpl = re.search(r'<template id="tpl-%s">(.*?)</template>' % c, t, flags=re.S).group(1)
        assert (h and 'class="dfig"' in tpl) or not h, (c, k, '교체 그림 없음')


if __name__ == '__main__':
    rows = build()
    verify()
    print('textbook Chapter %d개 반영 (새 Chapter %d개)' % (len(rows), sum(1 for r in rows if r[1] == 0)))
    print('PASS: %d templates, Part 03 검증 + textbook Chapter의 id·절 구성·보존 블록·태그 짝·Chapter 연결 확인' % (len(rows) + 19))
    print('wrote', OUT.name, OUT.stat().st_size, 'bytes')
