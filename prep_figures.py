"""_staging의 원본 그림을 잘라(여백·머리글 제거, 필요 시 회전) film_content/figures/에 최종 파일로 둔다.
macOS의 sips만 쓴다(PIL 불필요).  실행: python3 prep_figures.py
"""
import subprocess, struct, shutil, tempfile, os
from pathlib import Path
FIG = Path(__file__).resolve().parent / 'film_content' / 'figures'
ST = FIG / '_staging'

def sips(*a): subprocess.run(['sips', *map(str, a)], check=True, capture_output=True)
def size(p):
    o = subprocess.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', str(p)], capture_output=True, text=True).stdout
    v = [int(l.split()[-1]) for l in o.splitlines() if 'pixel' in l]
    return v[0], v[1]

def bbox(png):
    """흰 여백을 뺀 내용 영역 (x0,y0,x1,y1)."""
    with tempfile.TemporaryDirectory() as d:
        bmp = os.path.join(d, 'a.bmp'); sips('-s', 'format', 'bmp', png, '--out', bmp)
        b = open(bmp, 'rb').read()
    off = struct.unpack_from('<I', b, 10)[0]; w, h = struct.unpack_from('<ii', b, 18); bpp = struct.unpack_from('<H', b, 28)[0]
    top_down = h < 0; h = abs(h); nb = bpp // 8; row = (w * nb + 3) // 4 * 4
    x0, y0, x1, y1 = w, h, -1, -1
    for r in range(h):
        line = b[off + r * row: off + r * row + w * nb]
        if min(line) >= 200: continue
        y = r if top_down else h - 1 - r
        xs = [i // nb for i in range(0, len(line), nb) if min(line[i:i + min(nb, 3)]) < 200]
        x0 = min(x0, xs[0]); x1 = max(x1, xs[-1]); y0 = min(y0, y); y1 = max(y1, y)
    return x0, y0, x1, y1

def blank_rows(png):
    """각 행이 공백인지(True) 위에서 아래 순서로."""
    with tempfile.TemporaryDirectory() as d:
        bmp = os.path.join(d, 'a.bmp'); sips('-s', 'format', 'bmp', png, '--out', bmp)
        b = open(bmp, 'rb').read()
    off = struct.unpack_from('<I', b, 10)[0]; w, h = struct.unpack_from('<ii', b, 18); bpp = struct.unpack_from('<H', b, 28)[0]
    top_down = h < 0; h = abs(h); nb = bpp // 8; row = (w * nb + 3) // 4 * 4
    r = [min(b[off + i * row: off + i * row + w * nb]) >= 200 for i in range(h)]
    return r if top_down else r[::-1]

def split(whole, window, top, bottom, pad=24):
    """여러 도면이 세로로 쌓인 장을 window(높이 비율 구간) 안의 가장 넓은 공백 띠에서 둘로 나눈다."""
    src = FIG / whole; w, h = size(src); br = blank_rows(src)
    best = (0, 0); i = int(h * window[0]); end = int(h * window[1])
    while i < end:
        if br[i]:
            j = i
            while j < h and br[j]: j += 1
            if j - i > best[1] - best[0]: best = (i, j)
            i = j
        else: i += 1
    mid = (best[0] + best[1]) // 2
    for name, (y0, y1) in ((top, (0, mid)), (bottom, (mid, h))):
        if not name: continue
        out = FIG / name; shutil.copy(src, out); crop(out, 0, y0, w, y1)
        ww, hh = size(out); x0, yy0, x1, yy1 = bbox(out)
        crop(out, max(0, x0 - pad), max(0, yy0 - pad), min(ww, x1 + pad), min(hh, yy1 + pad))
        print('%-34s %5dx%-5d %6d B' % (name, *size(out), out.stat().st_size))
    src.unlink()

def crop(p, x0, y0, x1, y1):
    # sips는 cropOffset이 0이면 '지정 안 함'으로 보고 가운데를 자른다. 그래서 최소 1로 둔다.
    x0, y0 = max(1, x0), max(1, y0)   # 범위를 벗어나면 sips가 검은 띠를 채우므로 크기도 함께 줄인다
    sips('-c', y1 - y0, x1 - x0, '--cropOffset', y0, x0, p)

def fcrop(out, frac):
    w, h = size(out); fx0, fy0, fx1, fy1 = frac
    crop(out, int(w * fx0), int(h * fy0), int(w * fx1), int(h * fy1))

def make(src, dst, frac=None, rot=0, post=None, pad=24):
    out = FIG / dst; shutil.copy(ST / src, out)
    if frac: fcrop(out, frac)
    if rot: sips('-r', rot, out)
    if post: fcrop(out, post)      # 회전한 뒤에 한 번 더 자를 때
    w, h = size(out); x0, y0, x1, y1 = bbox(out)
    crop(out, max(0, x0 - pad), max(0, y0 - pad), min(w, x1 + pad), min(h, y1 + pad))
    print('%-34s %5dx%-5d %6d B' % (dst, *size(out), out.stat().st_size))

HDR = (0, 0.085, 1, 1)   # 'U.S. Patent ... Sheet n of m' 머리글 제거
JOBS = [
 ('us7132201_d2.png', '03-01_us7132201_fig1b.png', None, 0), ('us7132201_d3.png', '03-01_us7132201_fig1c.png', None, 0),
 ('us7132201_d4.png', '03-01_us7132201_fig1d.png', None, 0), ('us7132201_d5.png', '03-01_us7132201_fig1e.png', None, 0),
 ('us7820556_d5.png', '03-01_us7820556_fig5.png', None, 0), ('us7820556_d6.png', '03-01_us7820556_fig6.png', None, 0),
 ('us11145522_d2.png', '03-02_us11145522_fig2-3.png', None, 0), ('us11145522_d3.png', '03-02_us11145522_fig4-5.png', None, 0),
 ('us10410872_d6.png', '03-02_us10410872_fig6-7.png', None, 0),
 ('us6541401_d2.png', '03-05_us6541401_fig3.png', None, 0), ('us6541401_d6.png', '03-05_us6541401_fig9c.png', None, 0),
 ('us6319324_d10.png', '03-05_us6319324_fig7-8.png', None, 0),
 ('us6989337_d2.png', '03-05_us6989337_fig4.png', (0, 0, 1, 0.42), 0),
 ('us5461011_d0.png', '03-06_us5461011_fig1-2.png', HDR, 0), ('us6177344_d1.png', '03-06_us6177344_fig2-4.png', HDR, 0),
 ('us11302583_d1.png', '03-07_us11302583_fig1.png', None, 0),
 ('us6051282_d0.png', '03-08_us6051282_fig1.png', (0, 0.085, 1, 0.47), 0), ('us6051282_d1.png', '03-08_us6051282_fig2.png', HDR, 0),
 ('us6051282_d2.png', '03-08_us6051282_fig3.png', HDR, 0),
 ('us5827785_d7.png', '03-09_us5827785_fig3.png', HDR, 0), ('us6335274_d3.png', '03-09_us6335274_fig5.png', None, 90),
 ('us5366917_d5.png', '03-13_us5366917_fig2.png', None, 90, (0, 0, 0.88, 1)),
 ('us5256566_d8.png', '03-14_us5256566_fig15.png', (0, 0.49, 1, 0.94), 0), ('us5256566_d11.png', '03-14_us5256566_fig17.png', HDR, 0),
 ('us8409987_d6.png', '03-16_us8409987_fig5.png', None, 0),
 ('us10510590_d2.png', '03-18_us10510590_fig2.png', None, 0), ('us10510590_d3.png', '03-18_us10510590_fig3.png', None, 0),
 ('us10510590_d7.png', '03-18_us10510590_fig6.png', None, 0), ('us10510590_d9.png', '03-18_us10510590_fig8.png', None, 0),
 ('us10510590_d11.png', '03-18_us10510590_fig10.png', None, 0),
 # 2026-10-15: 자체 제작 그림을 실제 도면으로 교체
 ('us7132201_d7.png', '03-01_us7132201_fig5-7.png', None, 0), ('us7132201_d8.png', '03-01_us7132201_fig8-10.png', None, 0),
 ('us6962876_d3.png', '03-04_us6962876_fig3-4.png', None, 0), ('us6962876_d4.png', '03-04_us6962876_fig6.png', (0, 0.56, 1, 1), 0),
 ('us7186446_d2.png', '03-17_us7186446_fig3.png', (0, 0, 1, 0.5), 0), ('us12180583_d2.png', '03-17_us12180583_fig2.png', None, 0),
 ('us4854263_d0.png', '01-01_us4854263_fig1.png', (0, 0.085, 1, 0.355), 0), ('us4854263_d0.png', '02-03_us4854263_fig2-3.png', (0, 0.55, 1, 0.80), 0),
 ('us5000113_d1.png', '02-03_us5000113_fig2.png', (0, 0.095, 1, 0.69), 0),
 # 2026-10-15: 막질별 실제 SEM·TEM 사진
 ('us6962876_d4.png', '03-04_us6962876_fig5.png', (0, 0, 1, 0.53), 0),
 ('us5405489_d2.png', '03-06_us5405489_fig3b.png', (0.34, 0.42, 0.88, 0.67), 0),
 ('kapur2024_f1.jpg', '03-03_kapur2024_fig1.jpg', (0, 0, 1, 0.47), 0),
 ('kia2019_f5.jpg', '03-17_kia2019_fig5b.jpg', (0.62, 0, 1, 0.80), 0),
 # 2026-10-15: Part 00 시각화 (특허 쪽 그림은 USPTO PDF에서 pdfimages로 뽑은 원본 1-bit 스캔, 파일명 _pN = PDF 쪽 번호)
 ('us6140206_p4.png', '00-01_us6140206_fig9.png', (0, 0.54, 1, 0.87), 0),
 ('liu2021_f2.jpg', '00-01_liu2021_fig2a.jpg', (0, 0, 1, 0.47), 0),
 ('kim2022_f1.jpg', '00-02_kim2022_fig1a.jpg', (0, 0, 0.437, 1), 0),
 ('us8360001_p21.png', '00-03_us8360001_fig15.png', HDR, 0),
 ('kim2017_f5.jpg', '00-03_kim2017_fig5ab.jpg', (0, 0, 1, 0.49), 0),
 ('us5653807_p3.png', '00-04_us5653807_fig2-4.png', (0, 0.11, 1, 1), 0),
 ('us6247842_p2.png', '00-06_us6247842_fig1.png', (0, 0.10, 1, 0.535), 0),
 ('us6247842_p3.png', '00-06_us6247842_fig3.png', HDR, 90),
 ('us6598615_p4.png', '00-07_us6598615_fig3.png', HDR, 90),
 ('us7296465_p2.png', '00-07_us7296465_fig1a.png', HDR, 90),
 ('us8360001_p16.png', '00-08_us8360001_fig10.png', HDR, 0),
 ('us8360001_p18.png', '00-08_us8360001_fig12.png', HDR, 0),
 ('us6649278_p4.png', '00-09_us6649278_fig4.png', HDR, 90),
 ('us6649278_p5.png', '00-09_us6649278_fig5.png', HDR, 90),
 ('us5653807_p2.png', '00-10_us5653807_fig1-3.png', (0, 0.11, 1, 1), 0),
 # 2026-10-15: Part 01 시각화
 ('us8273670_p5.png', '01-06_us8273670_fig3.png', HDR, 0),
 ('us6740601_p3.png', '01-10_us6740601_fig1a.png', HDR, 90),
 ('kim2022_f1.jpg', '01-10_kim2022_fig1b.jpg', (0.45, 0, 1, 1), 0),
 ('li2019m_f1.jpg', '01-10_li2019_fig1a.jpg', (0, 0, 0.455, 1), 0),
 # 2026-10-15: Part 02 시각화 (USPTO PDF의 원본 1-bit 도면)
 ('us4951601_p2.png', '02-01_us4951601_fig1.png', (0, 0.10, 1, 1), 0),
 ('us6444037_p5.png', '02-01_us6444037_fig1d.png', HDR, 90),
 ('us4436674_p2.png', '02-02_us4436674_fig1.png', (0, 0.10, 1, 0.57), 0),
 ('us5835678_p3.png', '02-02_us5835678_fig2.png', (0, 0.085, 1, 0.625), 0),
 ('us6444037_p10.png', '02-03_us6444037_fig5.png', (0, 0.10, 1, 1), 0),
 ('us10312058_p7.png', '02-03_us10312058_fig3.png', HDR, 90),
 ('us6444037_p17.png', '02-04_us6444037_fig11-12.png', (0, 0.10, 1, 1), 0),
 ('us6444037_p20.png', '02-04_us6444037_fig15.png', (0, 0.10, 1, 1), 0),
 ('us5967661_p10.png', '02-04_us5967661_fig9.png', HDR, 90),
 ('us5967661_p11.png', '02-04_us5967661_fig10a.png', (0, 0.52, 1, 0.95), 90),
 ('us6444037_p8.png', '02-05_us6444037_fig3.png', HDR, 90),
 ('us6194628_p5.png', '02-05_us6194628_fig3.png', (0, 0.10, 1, 1), 0),
 ('us6194628_p9.png', '02-05_us6194628_fig8-9.png', (0, 0.10, 1, 1), 0),
 ('us5656123_p2.png', '02-06_us5656123_fig1.png', (0, 0.10, 1, 1), 0),
 ('us5656123_p4.png', '02-06_us5656123_fig3.png', (0, 0.10, 1, 1), 0),
 ('us7004107_p8.png', '02-06_us7004107_fig8.png', (0, 0.10, 1, 1), 0),
 ('us7004107_p10.png', '02-06_us7004107_fig9.png', HDR, 90),
 ('us7004107_p3.png', '02-01_us7004107_fig1.png', HDR, 90),
 ('us6878214_p7.png', '02-07_us6878214_fig6.png', (0, 0.085, 1, 0.8), 0),
 ('us7588036_p5.png', '02-07_us7588036_fig5.png', HDR, 90),
 ('us6878214_p3.png', '02-08_us6878214_fig2.png', (0, 0.10, 1, 1), 0),
 ('us6878214_p6.png', '02-08_us6878214_fig5.png', HDR, 90),
 # 2026-10-15: Part 04 시각화
 ('us6139923_p5.png', '04-01_us6139923_fig5.png', (0, 0.46, 1, 0.86), 0),
 ('us6905940_p7.png', '04-01_us6905940_fig3.png', (0, 0.10, 1, 0.47), 0),
 ('us6905940_p8.png', '04-01_us6905940_fig5.png', (0, 0.10, 1, 1), 90),
 ('us6905940_p9.png', '04-06_us6905940_fig6-8.png', (0, 0.10, 1, 1), 90),
 # 2026-10-15: Part 06 시각화
 ('us6020035_p13.png', '06-07_us6020035_fig7.png', (0, 0.10, 1, 1), 90),
 ('us6846742_p4.png', '06-07_us6846742_fig5.png', (0, 0.10, 1, 0.55), 0),
 # 2026-10-15: Part 07 시각화
 ('us6846742_p3.png', '07-01_us6846742_fig4.png', (0, 0.575, 1, 0.97), 0),
 # 2026-10-15: Part 09 시각화
 ('us6444037_p15.png', '09-01_us6444037_fig9.png', (0, 0.10, 1, 1), 0),
 ('us5855681_p19.png', '09-06_us5855681_fig19.png', (0, 0.10, 1, 1), 90),
 # 2026-10-16: Part 04 보강
 ('us5862057_p7.png', '04-05_us5862057_fig4.png', (0, 0.10, 1, 0.88)),
 ('us5862057_p8.png', '04-05_us5862057_fig5.png', (0, 0.10, 1, 0.88)),
 ('us7638161_p8.png', '04-07_us7638161_fig6-7.png', HDR),
 # 2026-10-16: Part 10 소자 (Logic · DRAM · NAND)
 ('us7852675_p10.png', '10-01_us7852675_fig9.png', HDR, 90),
 ('us6413802_p3.png', '10-02_us6413802_fig1.png', (0, 0.09, 1, 0.39), 0),
 ('us6518171_p2.png', '10-03_us6518171_fig1.png', HDR, 90),
 ('us3387286_p1.png', '10-04_us3387286_fig1.png', (0, 0.16, 1, 0.52), 0),
 ('us12058850_p4.png', '10-04_us12058850_fig2.png', HDR, 0),
 ('us7852675_p6.png', '10-05_us7852675_fig5.png', HDR, 0),
]
SPLITS = [
 ('03-02_us11145522_fig2-3.png', (0.35, 0.65), '03-02_us11145522_fig2.png', '03-02_us11145522_fig3.png'),
 ('03-02_us11145522_fig4-5.png', (0.35, 0.65), '03-02_us11145522_fig4.png', '03-02_us11145522_fig5.png'),
 ('03-02_us10410872_fig6-7.png', (0.35, 0.65), '03-02_us10410872_fig6.png', '03-02_us10410872_fig7.png'),
 ('03-05_us6319324_fig7-8.png', (0.35, 0.65), '03-05_us6319324_fig7.png', '03-05_us6319324_fig8.png'),
 ('03-06_us6177344_fig2-4.png', (0.50, 0.62), '03-06_us6177344_fig2.png', '03-06_us6177344_fig4.png'),
 ('03-09_us5827785_fig3.png', (0.40, 0.60), '03-09_us5827785_fig3a.png', '03-09_us5827785_fig3b.png'),
 ('03-07_us11302583_fig1.png', (0.33, 0.46), None, '03-07_us11302583_fig1bc.png'),
]
COPY = [
 ('chen2012_f4.jpg', '03-03_chen2012_fig4.jpg'), ('chen2012_f2.jpg', '03-12_chen2012_fig2.jpg'),
 ('sa2021_f1.jpg', '03-10_sa2021_fig1.jpg'), ('sa2021_f3.jpg', '03-10_sa2021_fig3.jpg'),
 ('hegedus2021_f3.jpg', '03-11_hegedus2021_fig3.jpg'), ('hegedus2021_f4.jpg', '03-11_hegedus2021_fig4.jpg'),
 ('choi2020_f1.jpg', '03-13_choi2020_fig1.jpg'), ('choi2020_f11.jpg', '03-13_choi2020_fig11.jpg'),
 ('radamson2020_f17.jpg', '03-15_radamson2020_fig17.jpg'),
 ('ohtake2021_f11.jpg', '03-01_ohtake2021_fig11.jpg'),
 ('zhang2019_f2.jpg', '03-19_zhang2019_fig2.jpg'), ('zhang2019_f4.jpg', '03-19_zhang2019_fig4.jpg'), ('ando2012_f6.jpg', '03-19_ando2012_fig6.jpg'),
 # 2026-10-15: 막질별 실제 SEM·TEM 사진
 ('choi2022_f4.jpg', '03-05_choi2022_fig4.jpg'), ('choi2022_f10.jpg', '03-05_choi2022_fig10.jpg'), ('choi2022_f11.jpg', '03-05_choi2022_fig11.jpg'),
 ('parkhomenko2023_f1.jpg', '03-08_parkhomenko2023_fig1.jpg'), ('park2021_f3.jpg', '03-10_park2021_fig3.jpg'),
 ('shi2009_f1.jpg', '03-14_shi2009_fig1.jpg'), ('chu2023_f2.jpg', '03-15_chu2023_fig2.jpg'), ('li2025_f7.jpg', '03-15_li2025_fig7.jpg'),
 ('cui2019_f3.jpg', '03-16_cui2019_fig3.jpg'), ('cui2019_f2.jpg', '03-17_cui2019_fig2.jpg'), ('lodha2024_f7.jpg', '03-18_lodha2024_fig7.jpg'),
 # 2026-10-15: Part 00 시각화
 ('florian2021_f6.jpg', '00-03_florian2021_fig6.jpg'), ('wang2019_f5.jpg', '00-05_wang2019_fig5.jpg'),
 ('mata2020_f2.jpg', '00-07_mata2020_fig2.jpg'), ('zhou2024_f3.jpg', '00-08_zhou2024_fig3.jpg'), ('wang2019_f6.jpg', '00-08_wang2019_fig6.jpg'),
 # 2026-10-15: Part 01 시각화
 ('tian2024_f1.jpg', '01-01_tian2024_fig1.jpg'), ('zhou2024_f1.jpg', '01-01_zhou2024_fig1.jpg'),
 ('ohkubo2021_f5.jpg', '01-02_ohkubo2021_fig5.jpg'), ('ohkubo2021_f3.jpg', '01-02_ohkubo2021_fig3.jpg'),
 ('li2019m_f2.jpg', '01-04_li2019_fig2.jpg'),
 ('choolakkal2024_f3.jpg', '01-05_choolakkal2024_fig3.jpg'), ('choolakkal2024_f2.jpg', '01-05_choolakkal2024_fig2.jpg'),
 ('zhu2019_f1.jpg', '01-07_zhu2019_fig1.jpg'), ('colin2020_f9.jpg', '01-07_colin2020_fig9.jpg'),
 ('seong2023_f2.jpg', '01-08_seong2023_fig2.jpg'), ('lisovskiy2022_f2.jpg', '01-08_lisovskiy2022_fig2.jpg'),
 ('lisovskiy2022_f5.jpg', '01-08_lisovskiy2022_fig5.jpg'), ('kim2017_f2.jpg', '01-08_kim2017_fig2.jpg'),
 ('lisovskiy2022_f3.jpg', '01-09_lisovskiy2022_fig3.jpg'),
 # 2026-10-15: Part 04 시각화
 ('tang2026_f3.jpg', '04-02_tang2026_fig3.jpg'), ('tang2026_f2.jpg', '04-03_tang2026_fig2.jpg'), ('tang2026_f8.jpg', '04-03_tang2026_fig8.jpg'),
 ('gosar2019_f2.jpg', '04-03_gosar2019_fig2.jpg'), ('gosar2019_f8.jpg', '04-04_gosar2019_fig8.jpg'),
 ('smietana2014_f6.jpg', '04-04_smietana2014_fig6.jpg'), ('kim2022_f4.jpg', '04-05_kim2022_fig4.jpg'),
 ('bolkenbaas2025_f1.jpg', '04-07_bolkenbaas2025_fig1.jpg'), ('smietana2014_f2.jpg', '04-08_smietana2014_fig2.jpg'),
 ('vandepoll2025_f5.jpg', '04-06_vandepoll2025_fig5.jpg'),
 # 2026-10-15: Part 05 시각화
 ('lehmann2014_f5.jpg', '05-01_lehmann2014_fig5.jpg'), ('chandra2017_f13.jpg', '05-02_chandra2017_fig13.jpg'),
 ('parkhomenko2023_f3.jpg', '05-03_parkhomenko2023_fig3.jpg'), ('ekar2022_f4.jpg', '05-03_ekar2022_fig4.jpg'),
 ('gao2025_f25.jpg', '05-04_gao2025_fig25.jpg'), ('parkhomenko2023_f5.jpg', '05-05_parkhomenko2023_fig5.jpg'),
 ('kim2022_f7.jpg', '05-05_kim2022_fig7.jpg'), ('gao2025_f26.jpg', '05-07_gao2025_fig26.jpg'),
 # 2026-10-15: Part 06 시각화
 ('lin2017_f8.jpg', '06-01_lin2017_fig8.jpg'), ('choi2022s_f1.jpg', '06-01_choi2022_fig1.jpg'),
 ('tang2026_f4.jpg', '06-03_tang2026_fig4.jpg'), ('ni2017_f4.jpg', '06-05_ni2017_fig4.jpg'),
 ('zhang2021_f3.jpg', '06-06_zhang2021_fig3.jpg'),
 # 2026-10-15: Part 07 시각화
 ('park2024w_f10.jpg', '07-02_park2024_fig10.jpg'), ('yang2014_f8.jpg', '07-03_yang2014_fig8.jpg'), ('yang2014_f9.jpg', '07-03_yang2014_fig9.jpg'),
 ('yang2014_f1.jpg', '07-05_yang2014_fig1.jpg'), ('lee2024_f4.jpg', '07-06_lee2024_fig4.jpg'),
 ('chang2021_f4.jpg', '07-07_chang2021_fig4.jpg'), ('chang2021_f1.jpg', '07-07_chang2021_fig1.jpg'), ('kwon2021_f6.jpg', '07-07_kwon2021_fig6.jpg'),
 # 2026-10-15: Part 08 시각화 (07-04 포함)
 ('li2018_f12.jpg', '07-04_li2018_fig12.jpg'), ('tian2024_f7.jpg', '08-01_tian2024_fig7.jpg'),
 ('zhou2024_f5.jpg', '08-02_zhou2024_fig5.jpg'), ('li2018_f3.jpg', '08-03_li2018_fig3.jpg'), ('li2018_f2.jpg', '08-03_li2018_fig2.jpg'),
 ('becker2019_f5.jpg', '08-04_becker2019_fig5.jpg'), ('vandepoll2025_f10.jpg', '08-04_vandepoll2025_fig10.jpg'),
 ('li2018_f13.jpg', '08-06_li2018_fig13.jpg'), ('tchatchoua2023_f1.jpg', '08-07_tchatchoua2023_fig1.jpg'),
 # 2026-10-15: Part 09 시각화
 ('song2022_f3.jpg', '09-04_song2022_fig3.jpg'),
 # 2026-10-16: 08-05 그림
 ('yangoes2014_f2.jpg', '08-05_yangoes2014_fig2.jpg'), ('yangoes2014_f6.jpg', '08-05_yangoes2014_fig6.jpg'),
 # 2026-10-16: 03-18 Mo 비저항 크기 효과
 ('jog2023_f3.jpg', '03-18_jog2023_fig3.jpg'),
 # 2026-10-16: Part 10 소자 (Logic · DRAM · NAND)
 ('zhang2024nsr_f1.jpg', '10-02_zhang2024_fig1.jpg'), ('chu2023gaa_f2.jpg', '10-02_chu2023_fig2.jpg'), ('chu2023gaa_f5.jpg', '10-02_chu2023_fig5.jpg'),
 ('cui2019via_f2.jpg', '10-03_cui2019_fig2.jpg'), ('cui2019via_f3.jpg', '10-03_cui2019_fig3.jpg'),
 ('zhao2022ic_f5.jpg', '10-03_zhao2022_fig5.jpg'),
 ('sun2022bcat_f1.jpg', '10-04_sun2022_fig1.jpg'), ('kim2025hfo_f2.jpg', '10-04_kim2025_fig2.jpg'),
 ('lee2022nand_f1.jpg', '10-05_lee2022_fig1.jpg'), ('lee2022nand_f2.jpg', '10-05_lee2022_fig2.jpg'),
 ('jia2023deck_f2.jpg', '10-05_jia2023_fig2.jpg'), ('ramesh2021mg_f9.jpg', '10-05_ramesh2021_fig9.jpg'),
]
if __name__ == '__main__':
    for j in JOBS: make(*j)
    for sp in SPLITS: split(*sp)
    for s, d in COPY:
        shutil.copy(ST / s, FIG / d); print('%-34s %5dx%-5d %6d B' % (d, *size(FIG / d), (FIG / d).stat().st_size))
