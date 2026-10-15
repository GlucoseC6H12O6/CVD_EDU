"""Google Patents 페이지에서 도면 설명과 원본 크기 도면 URL을 뽑는다.
사용: python3 patent_figs.py US7132201 US7820556 ...      (목록만 출력)
      python3 patent_figs.py --get US7132201 2 3 --out DIR  (도면 장 번호를 지정해 내려받기)
"""
import sys, re, html, subprocess, time, pathlib
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'

def fetch(url):
    time.sleep(1.5)
    return subprocess.run(['curl', '-sS', '-L', '--max-time', '60', '-A', UA, url], capture_output=True, check=True).stdout

def page(pn):
    return fetch('https://patents.google.com/patent/%s/en' % pn).decode('utf-8', 'replace')

def info(pn):
    t = page(pn)
    full = re.findall(r'itemprop="full"\s+content="([^"]+)"', t)
    title = re.search(r'<meta name="DC.title" content="([^"]*)"', t)
    assignee = re.search(r'itemprop="assigneeOriginal"[^>]*>([^<]*)<', t)
    text = html.unescape(re.sub(r'<[^>]+>', ' ', t))
    text = re.sub(r'\s+', ' ', text)
    m = re.search(r'BRIEF DESCRIPTION OF (?:THE )?(?:SEVERAL VIEWS OF THE )?(?:DRAWINGS?|FIGURES)(.{0,1700})', text, flags=re.I)
    return full, (title.group(1).strip() if title else ''), (assignee.group(1).strip() if assignee else ''), (m.group(1).strip() if m else '(도면 설명 절을 찾지 못함)')

if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--get':
        pn = a[1]; out = pathlib.Path(a[a.index('--out') + 1]); sheets = [int(x) for x in a[2:a.index('--out')]]
        full, *_ = info(pn)
        for s in sheets:
            url = full[s]
            dst = out / ('%s_d%d.png' % (pn.lower(), s))
            dst.write_bytes(fetch(url))
            print('saved', dst.name, dst.stat().st_size)
    else:
        for pn in a:
            try:
                full, title, asg, desc = info(pn)
                print('=== %s | %s | %s | 도면 %d장' % (pn, title[:70], asg[:30], len(full)))
                print(desc[:1150])
            except Exception as e:
                print('=== %s 실패: %s' % (pn, e))
