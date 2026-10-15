# Part 01 그림 자료 수집 기록 (2026-10-15)

Part 01(01-01 ~ 01-10)에 실제 논문·특허 그림을 넣었다. 원래 그림이 거의 없던 이론 장들이라, 장마다 본문 설명에 맞는 실측·계산 자료를 골라 해당 소절 끝에 넣었다. 01-09의 자체 제작 개념도("개념적 공정 경로")는 실제 사진으로 바꿨다(`_figures.md`의 `01-09 keep:0`). 출처는 PMC의 CC BY 논문과 미국 특허 도면뿐이다. 그림 파일은 `film_content/figures/01-NN_*`, 원본은 `_staging/`, 자르기는 `prep_figures.py`에 있다.

확인 수준: **A** = 논문 본문(PMC XML) 또는 특허 본문(USPTO PDF OCR)에서 설명과 수치를 확인. **B** = 그림에서 값을 읽음.

## 새로 받은 논문 (CC BY 4.0)

| ID | 서지 | 그림 | 넣은 곳 | 확인 |
|---|---|---|---|---|
| Q1 | Y. Tian 등, "Multiscale Models of CVD Process: Review and Prospective", *Materials* 17, 5131 (2024). [PMC11509692](https://pmc.ncbi.nlm.nih.gov/articles/PMC11509692/) | Figure 1 (저자 작성, 다른 문헌 인용 없음) | 01-01 §2 | A: MTS SiC 예, 균일·불균일 반응, 기상 핵생성 경고 |
| Q2 | J. Zhou 등, *Materials* 17, 5952 (2024). [PMC11643910](https://pmc.ncbi.nlm.nih.gov/articles/PMC11643910/) | Figure 1 | 01-01 §4 | A: 지름 420 mm, 182 mm Wafer 1,200장, 2 mm 간격, 26 Pa, 882–885 K |
| Q3 | I. Ohkubo 등, "Control of Competing Thermodynamics and Kinetics in Vapor Phase Thin-Film Growth of Nitrides and Borides", *Front. Chem.* 9, 642388 (2021). [PMC8353106](https://pmc.ncbi.nlm.nih.gov/articles/PMC8353106/) | Figure 3, 5 | 01-02 §5, §6 | A: 0.3 Å/s 아래 다결정, 영역 I–III 정의, B 증기압 자료는 문헌 모음. B: Epitaxy 창 약 700 °C 이상·0.5–0.8 Å/s |
| Q4 | Z. Zhu 등, "Low-Temperature Plasma-Enhanced Atomic Layer Deposition of SiO₂ Using Carbon Dioxide", *Nanoscale Res. Lett.* 14, 55 (2019). [PMC6372707](https://pmc.ncbi.nlm.nih.gov/articles/PMC6372707/) | Fig. 1 | 01-03 §5 | A: 90 °C, BTBAS, CO₂ Plasma, 포화 GPC 약 1.15 Å/cycle |
| Q5 | J. Li 등, "Stability Analysis of Multi Process Parameters for Metal-Organic Chemical Vapor Deposition Reaction Cavity", *Molecules* 24, 876 (2019). [PMC6429165](https://pmc.ncbi.nlm.nih.gov/articles/PMC6429165/) | Figure 1(a), 2 | 01-10 §5, 01-04 §5 | A: 네 가지 흐름 상태, Plug·Plug 회전 유도 흐름은 안정. B: 경계 압력 최대 약 22 Torr(약 250 rpm). 흐름 상태 분류 자체는 논문이 인용한 Mitrovic 등의 틀 |
| Q6 | A. H. Choolakkal 등, "Competitive co-diffusion as a route to enhanced step coverage in chemical vapor deposition", *Nat. Commun.* 15, 10667 (2024). [PMC11634887](https://pmc.ncbi.nlm.nih.gov/articles/PMC11634887/) | Fig. 2, 3 | 01-05 §6, §3 | A: SC 정의, TEB/H₂, 550 °C, Xe·Ar 100 sccm, 증착 속도 범위 7.6–0 → 7.3–1.5 nm/min, 450 °C까지 SC = 1. B: 두께 453/323, 436/423, 447/312 nm(그림 속 표기) |
| Q7 | J. Colin 등, "In Situ and Real-Time Nanoscale Monitoring of Ultra-Thin Metal Film Growth Using Optical and Electrical Diagnostic Tools", *Nanomaterials* 10, 2225 (2020). [PMC7697846](https://pmc.ncbi.nlm.nih.gov/articles/PMC7697846/) | Figure 9 (공저자 Pliatsikas·Sarakinos의 미발표 자료) | 01-07 §4 | A: Ag/SiO₂, 0.1 nm/s, 300·500 K. B: 피복률 58·44 %, 평균 섬 면적 82.3·110.9 nm² |
| Q8 | I. Seong 등, "On the Quenching of Electron Temperature in Inductively Coupled Plasma", *Materials* 16, 3219 (2023). [PMC10141103](https://pmc.ncbi.nlm.nih.gov/articles/PMC10141103/) | Figure 2 | 01-08 §2 | A: Ar, 13.56 MHz ICP, 206 mTorr, Langmuir Probe, Maxwell화 설명. B: 2.6 → 2.1 eV |
| Q9 | V. Lisovskiy 등, "Synthesis of Nanoparticles and Theoretical Model of Their Retention in Plasma of RF Capacitive Discharge with Vertically Positioned Electrodes", *ACS Omega* 7, 47941 (2022). [PMC9798781](https://pmc.ncbi.nlm.nih.gov/articles/PMC9798781/) | Figure 2, 3, 5 | 01-08 §3, §4, 01-09 keep:0 | A: C₂H₂ 1 Torr, 13.56 MHz, 압력이 2–5배 감소("진공 Pump"), 입자 400–600 nm, Sheath 모델. B: 약 0.23 Torr |

## 다시 쓴 그림 (다른 Part에서 이미 받은 것)

| 그림 | 넣은 곳 |
|---|---|
| Cui 2020 (*Micromachines*, PMC7019522) Figure 2: PVD Ti 대 CVD TiN 바닥 피복률 | 01-01 §1 |
| US 8,360,001 FIGURE 10: Silane·Disilane·Trisilane Arrhenius (00-08과 같은 파일) | 01-03 §3. 그래프에서 두 점을 읽어 겉보기 활성화에너지 약 160 kJ/mol을 계산(B) |
| Lodha 2024 (*Nanomaterials*, PMC11280396) Figure 7: 영역 선택 Ru ALD | 01-07 §1 |
| Kim 2022 (*Materials*, PMC9100524) Figure 1(b): ALD 시간표 | 01-10 §6 |
| Kim 2017 (*Sci. Rep.*, PMC5648850) Figure 2: 이온 밀도 | 01-08 §5 |

## 미국 특허 (USPTO PDF)

| 특허 | 그림 | 넣은 곳 | 확인 |
|---|---|---|---|
| US 8,273,670 (Novellus Systems, 2012), Load lock design for rapid wafer heating | Figure 3 | 01-06 §4 | A: 전이 압력 약 10 Torr(1–100 Torr), 간격 10–2,000 µm, He·N₂·Ar, 전이 압력은 간격과 기체에 따라 다름 |
| US 6,740,601 (Applied Materials, 2004), HDP-CVD deposition process for filling high aspect ratio gaps | FIG. 1A | 01-10 §4 | A: 13 Chamber, 14 Ceramic Dome, 29·30 Coil, 31A·31B Source RF, 80B Bias(17 받침 부분), 37·39 Gas Ring·Nozzle, 45 위쪽 Nozzle, 26 Throttle Valve, 27 Gate Valve, 28 Turbo, 50 원격 Plasma 세정, Sputtering이 Gap-fill을 돕는다는 설명 |

## 후보였으나 넣지 않은 것

- An 2021 (*Sci. Rep.*, PMC8065108) MOCVD 온도·속도장: PMC 이미지가 664 × 157 px로 작아 글자를 읽을 수 없다.
- Martínez 2024 (*Beilstein J. Nanotechnol.*, PMC11665448) HFCVD 온도·농도 지도: 대기압 Hot-filament 장치로 일반 CVD와 거리가 멀고, 표에 적힌 기판 온도(26 °C)와 측정 온도(450–500 °C)가 맞지 않아 교재 예로 쓰지 않았다.
- Yang 2010 (*Sensors*, PMC3247728) OES 스펙트럼: 가로축이 파장이 아니라 채널 번호다.
- Colin 2020 Figure 3, Radamson·Moon 리뷰의 그림: 다른 저널에서 허락받아 옮긴 그림이다.
- US 6,649,278 FIG. 12 (Hot-wall 로): 너무 단순해 Zhou 2024 Figure 1을 썼다.

## 남은 자체 제작 그림 (Part 01)

01-03, 01-05의 계산 위젯 2개만 남았다. 값을 바꿔 보는 도구라 그대로 둔다.
