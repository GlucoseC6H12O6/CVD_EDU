# CVD EDU v1.2 — 교과서 원고 반영

## 무엇이 바뀌었나

- 89개 Chapter 전체를 교과서처럼 설명하는 투로 다시 썼다. 개념을 정의하고, 왜 그런지 설명하고, 예를 들고, 절마다 그 절에 맞춘 `이해 확인` 질문을 둔다. 어미는 ~이다/~한다로 통일했고, 영어 공정 용어(Wafer, Plasma, Recipe…)는 그대로 둔다.
- Part 00–02, 04–09의 70개 Chapter: 한 줄짜리 상투 문장만 있던 소제목을 실제 설명 문단으로 채웠다. 잘린 소제목은 완결된 제목으로 고쳤다. 아래쪽의 공통 문구(식·수량·단위, 데이터 해석 순서, 오해와 적용 범위)도 Chapter마다 내용에 맞게 다시 썼다.
- Part 03의 19개 막질: 표·그림·계산 예·근거 표시([논문 S08] 등)·수치는 그대로 두었다. 절마다 도입 설명을 넣고, 표 뒤에 근거 꼬리표만 있던 줄은 문장으로 바꾸고, 절 끝에 `이해 확인` 질문을 넣었다.
- Part 04의 8개 Chapter에도 절별 `이해 확인` 질문(모두 43개)을 넣었다.
- 원래 HTML의 그림·수식·조작 기능(widget), 절 id, 사이드바 목차, Chapter 사이 연결은 그대로 유지했다.

## 수식 조판 (2026-10-15, 사용자 요청)

- 모든 수식을 MathML로 조판한다. 분수는 위아래로 쌓고, 변수는 기울이고, 첨자는 작게 올리거나 내린다. 외부 라이브러리 없이 브라우저가 직접 그리므로 HTML 한 파일로 오프라인에서도 보인다.
- 원고 문법: 문장 속 수식은 `$...$`, 따로 세우는 수식은 `$$`로 시작하고 끝나는 블록(한 줄에 수식 하나)이다. 둘 다 LaTeX 문법이다. 변수는 한 글자씩(`R T`) 쓰고, 단위·화학식·약어는 `\mathrm{}`, 한글·설명은 `\text{}`로 쓴다. 변환은 `texmath.py`가 한다(표준 라이브러리만 사용).
- 바꾼 범위:
  - Part 03의 코드 블록 수식 61개 → `$$` 수식, 기호 설명 문장, 공정 순서 목록
  - 70개 장 본문의 `` `...` `` 수식 146개 → `$...$`. 단위·수치·화학식 이름 53종은 일반 글자로 바꿨다.
  - 문장 속에 그냥 적혀 있던 수식(`J = k_m(C_b − C_s)` 등) → `prose_math.py`로 찾아 `$...$`로 바꿨다. 규칙으로 애매한 것은 그 파일의 `OVERRIDE`에 직접 적었다.
  - 원래 HTML의 평문 수식 상자 45개(예: `Aopen = Nπd²/4`) → `textbook/_math.md`의 LaTeX로 바꿨다.
- 원래 HTML에서 이미 그림(SVG)으로 조판돼 있던 Part 00의 수식은 그대로 두었다.

## 자체 제작 그림 정리 (2026-10-15, 사용자 요청)

- Part 03 19개 장 첫머리의 자체 제작 개념도(ACL 삼원상도·BPSG Reflow 슬라이더 포함)를 모두 뺐다. `apply_textbook.py`의 `A.DROP_CRIT`가 이 일을 한다. 각 장 본문에는 실제 논문·특허 그림이 있다.
- 실제 그림으로 바꾼 것:
  - 03-01 ACL Figure 1(패턴 전사 모식도) → US 7,132,201 FIG. 5–7, 8–10의 실제 공정 단면
  - 03-01 ACL Figure 2(삼원 상도 모식도) → Ohtake 외, *Materials* 14, 315 (2021) Figure 11, 비정질 탄소 막 74종 실측(CC BY 4.0, 근거 S27)
  - 03-04 SiBN: 그림이 없던 장에 US 6,962,876 FIG. 6(유전율), FIG. 3·4(식각 속도) 추가
  - 03-17 TiN/TaN: 그림이 없던 장에 US 12,180,583 FIG. 2(TiN 조성·비저항), US 7,186,446 FIG. 3(TaN N/Ta–비저항) 추가
  - 01-01, 02-03, 02-05, 09-02의 상자 4개짜리 “개념적 공정 경로” → US 4,854,263 FIG. 1–3, US 5,000,113 FIG. 2, US 5,461,011 FIG. 1–2. 목록과 캡션은 `textbook/_figures.md`에 있다.
- 남은 자체 제작 그림: 계산 위젯 6개(01-03, 01-05, 02-05, 05-02, 07-04, 08-03)와 Part 00의 조작 위젯 5개뿐이다. “개념적 공정 경로” 개념도는 모두 실제 그림으로 바꿨다(02-03, 02-05, 09-02는 처음에, 01-09는 “Part 01 시각화”에서, 06-01, 07-01, 08-03은 “Part 02·04–09 시각화”에서). 계산 도구는 논문 그림으로 바꿀 대상이 아니다.

## SEM·TEM 사진 추가 (2026-10-15, 사용자 요청)

- 막질마다 실제 전자현미경 사진을 넣었다. 출처는 PMC의 CC BY 논문과 미국 특허 도면뿐이다. 그림마다 출처를 적었고, 각 장 `_자료수집.md`의 "SEM·TEM 사진 추가" 절에 서지와 라이선스를 기록했다.
- 사진이 있는 막질은 4개에서 16개로 늘었다.

| 장 | 넣은 사진 | 출처 |
|---|---|---|
| 03-01 ACL | Low-k 위 ACL 단면, Strip 뒤 단면 SEM | Park 2021 (*Materials*) |
| 03-03 SiC | PECVD a-SiC 적층 TEM·EDX (Memristor 시편) | Kapur 2024 (*Sci. Rep.*) |
| 03-04 SiBN | ALD SiBN 단차 피복 SEM | US 6,962,876 FIG. 5 |
| 03-05 USG | Gap-fill 단면 SEM, 묽은 HF로 드러낸 Seam | Choi 2022 (*Sci. Rep.*) |
| 03-06 BPSG | **Reflow 뒤 배선을 덮은 BPSG 단면 SEM** | US 5,405,489 FIG. 3B (1995년 스캔이라 거칠다) |
| 03-08 SiON | RTA 전후 SiNₓ·SiOₓ·SiOₓNᵧ 단면 SEM, TEM | Parkhomenko 2023 (*ACS Omega*) |
| 03-10 SiOCH | ACL Strip 전후 SiOC(H) 단면 SEM | Park 2021 (*Materials*) |
| 03-14 Poly-Si | 증착 온도별 결정립 SEM, TEM | Shi 2009 (*Sensors*, CC BY 3.0) |
| 03-15 SiGe | LPCVD SiGe/Si 다층 TEM, 띄운 Nanosheet TEM | Chu 2023 (*Sci. Rep.*), Li 2025 (*Nanomaterials*) |
| 03-16 W | Via 모양에 따른 W Plug 채움 SEM | Cui 2020 (*Micromachines*) |
| 03-17 TiN/TaN | Contact 입구·바닥 Ti/TiN TEM, TSV 측벽 ALD TaN TEM | Cui 2020, Kia 2019 (*Nanomaterials*) |
| 03-18 Mo/Ru | 영역 선택 Ru ALD 단면 TEM | Lodha 2024 (*Nanomaterials*) |

- 같은 사진을 Part 05·06에도 넣었다: 05-06(TEM 높이별 두께, TEM-EDX 깊이 분포), 06-02(결정립이 만드는 거칠기), 06-04(Void, HF로 드러낸 Seam, Via 모양과 W Void), 06-05(수소 Blister).
- 아직 사진이 없는 막질은 PSG/BSG, FSG, SiCN과 Mo다. 공개 논문이 거의 없고, 사진이 있는 자료는 유료 저널이거나 오래된 특허 스캔이라 알아볼 수 없었다.
- Choi 2022 논문은 Trench를 "종횡비 25:1, 입구 200 nm, 깊이 2.5 µm"로 적었는데 치수로 계산하면 12.5:1이다. 본문에는 종횡비를 빼고 치수만 적었다.

## Part 00 시각화 (2026-10-15, 사용자 요청)

- Part 00의 자체 제작 그림 7개를 실제 특허 도면과 논문 그림으로 바꾸고, 본문에 실제 자료 그림을 더 넣었다. 10개 장에 그림 21장(특허 도면 12, CC BY 논문 9)이 들어갔다. 출처·라이선스·확인 수준은 `textbook/_자료수집_part00.md`, 각 장 `참고 자료` 절에도 적었다.
- 특허는 Google Patents가 연속 요청을 막아 USPTO PDF를 받았다. 도면은 PDF 안의 원본 1-bit 스캔을 잘라 파일이 작고(그림당 15–110 KB), 도면 번호와 수치는 특허 본문을 OCR로 읽어 확인했다.

| 장 | 바꾸거나 넣은 그림 | 출처 |
|---|---|---|
| 00-01 | 소자 단면(STI·Gate·층간 절연막·금속·Passivation) ← 자체 그림 교체 / Damascene 공정 순서와 단계별 SEM | US 6,140,206 FIG. 9 / Liu 2021 (*Nat. Commun.*) |
| 00-02 | TTIP 구조식으로 화학식 읽기 ← 교체 | Kim 2022 (*Materials*) |
| 00-03 | 결정 Si 위 비정질 Si 단면 TEM·FFT ← 교체 / 증착 온도별 Si 막 XRD / SiNₓ FTIR의 Si–H·N–H | Florian 2021 (*Materials*) / US 8,360,001 FIG. 15 / Kim 2017 (*Sci. Rep.*) |
| 00-04 | Reactor → Pump → Oil Trap → Scrubber 배기 계통 ← 교체 | US 5,653,807 FIG. 2, 4 |
| 00-05 | 원료 증기압–온도 곡선 | Wang 2019 (*R. Soc. Open Sci.*) |
| 00-06 | Pedestal 센서로 Wafer 온도를 대신 재는 방식(온도 차 10–50 °C) ← 교체 / 시험 Wafer 면저항으로 실제 온도 읽기 | US 6,247,842 FIG. 1, 3 |
| 00-07 | Chamber → Throttle Valve → Turbo·Roughing Pump ← 교체 / 열식 MFC 구조 / µm 틈의 Knudsen 수 | US 6,598,615 FIG. 3 / US 7,296,465 FIG. 1A / Mata-Hernandez 2020 (*Sensors*) |
| 00-08 | 실측 대 계산(잘린 축 주의) / ln p 대 1/T 직선 / Silane·Disilane·Trisilane Arrhenius / 시간별 두께로 성장률 | Zhou 2024 (*Materials*) / Wang 2019 / US 8,360,001 FIGURE 10, 12 |
| 00-09 | 49점 두께 등고선 Map 두 장(평균 같고 표준편차 다름) | US 6,649,278 FIG. 4, 5 |
| 00-10 | Gas Cabinet·Purge Panel·Vent/Run 밸브 계통 ← 교체 / Reactor·Pump·Scrubber·누설 감지기 | US 5,653,807 FIG. 1–4 |

- 남긴 것: 00-04 그림 1·2, 00-05 혼합가스 그림, 00-08·00-09 Slider는 학습자가 값을 바꿔 보는 위젯이라 그대로 두었다.
- 00-08의 시간별 두께(105–775 Å)와 그 기울기·절편, 00-03 FTIR의 Si–H/N–H 비 같은 값은 그래프에서 읽은 것이며 캡션에 그렇게 적었다.
- `apply_textbook.py`: 실제 그림으로 바꾼 자체 제작 그림 안의 id(00-03의 원자 배열 SVG 등)는 사라져도 검사에서 오류로 보지 않게 했다. 그 SVG를 그리던 스크립트는 요소가 없으면 아무 일도 하지 않는다.

## Part 01 시각화 (2026-10-15, 사용자 요청)

- 원래 그림이 거의 없던 Part 01 이론 장 10개에 실제 그림 21장을 넣었다(새로 넣은 CC BY 논문 그림 16, 특허 도면 2, Part 00·03에 이미 있던 그림 재사용 3). 01-09의 자체 제작 개념도는 실제 사진으로 바꿨다. 출처와 확인 수준은 `textbook/_자료수집_part01.md`, 각 장 끝의 `그림 출처`에 적었다.

| 장 | 넣은 그림 | 출처 |
|---|---|---|
| 01-01 | 같은 Contact의 PVD Ti 대 CVD TiN 피복 / CVD 기본 단계 모식도 / 1,200장 관형 LPCVD 로 | Cui 2020 / Tian 2024 / Zhou 2024 |
| 01-02 | 원소 B 대 B 수소화물 증기압 / 성장 속도에 따라 갈리는 TiN 막 구조 지도 | Ohkubo 2021 |
| 01-03 | Silane·Disilane·Trisilane Arrhenius와 겉보기 활성화에너지 계산 / ALD 포화 곡선 | US 8,360,001 / Zhu 2019 |
| 01-04 | 압력·회전 속도에 따른 MOCVD Chamber 흐름 안정성 지도 | Li 2019 |
| 01-05 | 흐름 방향 증착 속도 지도 / 10:1 Trench Step Coverage 0.71 → 0.97 | Choolakkal 2024 |
| 01-06 | 압력이 내려가면 저항 가열에서 복사 가열로 바꾸는 시점(약 10 Torr) | US 8,273,670 |
| 01-07 | 영역 선택 Ru ALD / 온도에 따른 초기 섬 크기·밀도 | Lodha 2024 / Colin 2020 |
| 01-08 | 전자온도·EEPF / OES 시간 변화 / Sheath 구조 / 전력·압력별 이온 밀도 | Seong 2023 / Lisovskiy 2022 / Kim 2017 |
| 01-09 | 기상에서 생겨 벽에 쌓인 나노입자 SEM ← 자체 그림 교체 | Lisovskiy 2022 |
| 01-10 | HDP-CVD 장비 단면 / 회전 원판 MOCVD / ALD 한 Cycle 시간표 | US 6,740,601 / Li 2019 / Kim 2022 |

- Part 01 원고에는 원래 참고 문헌 절이 없어, 각 장 맨 끝에 `그림 출처` 목록을 붙였다(새 소절을 만들면 원본 절 구성 검사에 걸리므로 목록만 둔다).
- 01-03의 활성화에너지(약 160 kJ/mol)와 여러 캡션의 일부 값은 그래프에서 읽은 것이며 그렇게 적었다.
- HTML은 12.7 MB가 됐다.

## Part 02·04–09 시각화 (2026-10-15, 사용자 요청)

- 나머지 50개 장에 실제 그림 79장을 넣었다(새 그림 72장: 미국 특허 도면 31, CC BY 논문 41 / 다른 Part 그림 재사용 7). 06-01, 07-01, 08-03의 자체 제작 개념도를 실제 그림으로 바꿨다. 출처와 확인 수준은 `textbook/_자료수집_part02-09.md`, 각 장 끝의 `그림 출처`(Part 04는 `참고 연구와 원문 연결` 목록)에 적었다.

| Part | 그림 | 주요 내용 |
|---|---|---|
| 02 장비 | 22 (특허 22) | 다중 Chamber 평면도, PECVD 단면, 제어 Software 계층, Bubbler·액체 기화기, Blocker·Showerhead 구멍, 세라믹 Heater Coil·열전대, TC Wafer, 압력 제어 계통, Foreline 가루 SEM, 이중 주파수 전극·VI Probe 측정, RPS 대 In-situ 세정, 과세정·미세정 Particle, 배기관 IR 종말점 |
| 04 공정 | 16 (특허 4, 논문 10, 재사용 2) | Recipe Step 순서와 RF Ramp, 액체 유량계 지연, TEOS 비율·간격의 시간 변화, 저온 SiN의 온도·압력 의존성, 유량과 체류시간, 전력과 증착 속도, 전극 위 높이 효과, 원료 열 이력, 고종횡비 침투, Void·Seam, 핵생성 지연, Taguchi 주효과 |
| 05 계측 | 9 (논문 8, 재사용 1) | 타원편광 모델 선택, Map 색 척도, XPS 화학적 이동, SIMS 구덩이 거칠기, Wafer 응력 Map, n·k 분산, C–V·I–V, 두 응력 측정기 비교 |
| 06 결함 | 7 (논문 5, 특허 2) | 코팅에서 떨어진 Particle(교체), 기상 핵생성 분말, 균일도의 반대 경향, 전화선 Blister, 저온 SiN 산화, Seasoning과 Particle·균일도 Drift |
| 07 문제 해결·제어 | 10 (논문 9, 특허 1) | Seasoning 비교 실험(교체), Wafer형 Plasma 센서, OES 이상 감지와 거짓 경보, 벽 퇴적 센서, Trace 구간·고장 패턴, 가상 계측, 반응표면 잔차 진단 |
| 08 모델링 | 8 (논문 8) | 다중 규모 모델, 기상 중간체 기여율, MOCVD CFD 유선·온도(교체)와 격자, 원자 수준 MC, 침투 깊이로 매개변수 보정, 반응표면 최적화, 센서 데이터 구조 |
| 09 사례 | 7 (특허 2, 논문 1, 재사용 4) | Heater Lift·Bellows 단면, BPSG 액체 원료 지연, USG 균일도 Drift, SiCN 조성과 원료비, SiB 조성·응력, Tandem Chamber의 공유 자원 |

- 특허 본문은 USPTO PDF를 OCR로 읽어 도면 번호와 수치를 확인했다. 그래프에서 읽은 값은 캡션에 “그래프에서 읽음”으로 표시했다.
- 다른 Part의 그림을 다시 쓴 경우(Chen 2012, Parkhomenko 2023, US 6,649,278, US 6,905,940, US 6,020,035, US 10,410,872, US 11,145,522)는 그 장의 관점으로 캡션을 새로 썼다.
- 08-05는 맞는 실제 그림을 찾지 못해 그림이 없다.
- HTML은 20.5 MB가 됐다.

## 원고 위치

| 대상 | 원고 | 비고 |
|---|---|---|
| 70개 Chapter | `textbook/NN-NN.md` | 보존 블록(그림·수식·widget)은 `textbook/_keep/NN-NN.json` |
| Part 03 본문 | `film_content/03-NN_*_본문.md` | 자료 수집 기록은 `_자료수집.md` |
| 그림 파일 | `film_content/figures/` | 원본은 `figures/_staging`, 자르기·복사는 `prep_figures.py` |
| Part 00·01·02·04–09 그림 자료 | `textbook/_자료수집_part00.md`, `_자료수집_part01.md`, `_자료수집_part02-09.md` | 출처·라이선스·확인 수준 |

원고 문법: `## N. 제목`은 원래 절(번호를 바꾸지 않는다), `## 제목 {h2:N}`은 원래 h2 절, `{{keep:N}}`은 보존 블록(각각 한 번만), `[글](#ref:XX-YY)`는 Chapter 연결, `>`로 시작하는 줄은 상자(이해 확인 등)다.

## 다시 만들기

```bash
python3 apply_textbook.py
```

결과는 `CVD_EDU_v1.2_Textbook.html`이다. 실행할 때마다 89개 template, 절 id와 사이드바 목차, 보존 블록, 태그 짝, Chapter 연결, Part 03의 13개 절과 그림을 검사하고, 하나라도 어긋나면 파일을 쓰지 않는다.

`extract_textbook.py --force`는 실행하지 않는다. 다시 쓴 70개 원고를 원래 HTML에서 다시 뽑은 원고로 덮어쓴다.

## 확인한 것

- 브라우저에서 89개 Chapter 모두: 제목 표시, 절별 `이해 확인` 상자, 깨진 그림 0, 원고 표기(`{{keep`, `**`, `](#`) 노출 0, Console 오류 0.
- Part 03: 바꾸기 전 원고와 비교해 그림 블록, 근거 번호(S##), 단위가 붙은 수치, Q&A 수가 모두 그대로다.

## 아직 안 된 것

- `~/Downloads`에는 아직 v1.2를 복사하지 않았다.
- 이 폴더는 시스템 임시 폴더라 macOS가 지울 수 있다. 계속 쓸 거라면 다른 곳으로 옮겨야 한다.
- SiBN·TiN용으로 받아 둔 그림 후보(`film_content/figures/_staging`)는 본문에 넣지 않았다.
- Shimizu(STAM 2013, CC BY-NC-SA) 그림은 라이선스 확인 전이라 넣지 않았다.
