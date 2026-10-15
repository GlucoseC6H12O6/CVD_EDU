# Part 00 그림 자료 수집 기록 (2026-10-15)

Part 00(00-01 ~ 00-10)의 자체 제작 그림을 실제 논문·특허 그림으로 바꾸고, 본문에 실제 자료 그림을 더했다. 출처는 PMC의 CC BY 논문과 미국 특허 도면뿐이다. 그림 파일은 `film_content/figures/00-NN_*`, 원본은 `film_content/figures/_staging/`, 자르기는 `prep_figures.py`에 있다.

확인 수준: **A** = 논문 본문(PMC XML) 또는 특허 본문(USPTO PDF를 OCR)에서 그림 설명과 수치를 직접 확인. **B** = 그림에서 값을 읽음(본문에 숫자 없음).

## 논문 (CC BY)

| ID | 서지 | 라이선스 | 그림 | 넣은 곳 | 확인 |
|---|---|---|---|---|---|
| P1 | J. Liu 등, "High-yield, wafer-scale fabrication of ultralow-loss, dispersion-engineered silicon nitride photonic circuits", *Nat. Commun.* 12, 2236 (2021). [PMC8052462](https://pmc.ncbi.nlm.nih.gov/articles/PMC8052462/) | CC BY 4.0 | Fig. 2(a) | 00-01 §3 반복 패터닝 | A: Preform Reflow 1,250 °C, LPCVD Si₃N₄ 1,000 nm |
| P2 | H. Kim 등, "Decomposition Characteristics of the TTIP Precursor for Atomic Layer Deposition", *Materials* 15, 3021 (2022). [PMC9100524](https://pmc.ncbi.nlm.nih.gov/articles/PMC9100524/) | CC BY 4.0 | Figure 1(a) | 00-02 keep:0 (자체 그림 교체) | A: 구조식. 원자 수·몰질량은 직접 계산 |
| P3 | C. Florian 등, "Single Femtosecond Laser-Pulse-Induced Superficial Amorphization and Re-Crystallization of Silicon", *Materials* 14, 1651 (2021). [PMC8037179](https://pmc.ncbi.nlm.nih.gov/articles/PMC8037179/) | CC BY 4.0 | Figure 6 | 00-03 keep:0 (자체 그림 교체) | A: 전이 영역 약 3.9 nm, FFT로 구조 차이, 30 fs Pulse |
| P4 | K. S. Kim 등, "Silicon Nitride Deposition for Flexible Organic Electronic Devices by VHF (162 MHz)-PECVD Using a Multi-Tile Push-Pull Plasma Source", *Sci. Rep.* 7, 13585 (2017). [PMC5648850](https://pmc.ncbi.nlm.nih.gov/articles/PMC5648850/) | CC BY 4.0 | Figure 5(a)(b) | 00-03 §5 수소가 들어오는 경로 | A: 피크 위치(3,340·1,185·2,155·850 cm⁻¹), 80 °C. B: Si–H/N–H 비 7→1, Si–N 839→862 cm⁻¹ |
| P5 | C. Wang, S. Yang, Y. Chen, "Determination of the vapour pressure curves and vaporization enthalpies of hafnium alkoxides using thermogravimetric analysis", *R. Soc. Open Sci.* 6, 181193 (2019). [PMC6366183](https://pmc.ncbi.nlm.nih.gov/articles/PMC6366183/) | CC BY 4.0 | Figure 5, 6 | 00-05 §1, 00-08 §3 | A: 485 K 53.9 Pa, 573 K 3,556 Pa(표), ln p = 31.157 − 13,130.57/T, ΔHvap 109.2 ± 0.47 kJ/mol, 631–659 K 분해 피크 |
| P6 | D. Mata-Hernandez 등, "Resonant MEMS Pressure Sensor in 180 nm CMOS Technology Obtained by BEOL Isotropic Etching", *Sensors* 20, 6037 (2020). [PMC7660321](https://pmc.ncbi.nlm.nih.gov/articles/PMC7660321/) | CC BY 4.0 | Figure 2 | 00-07 §5 Knudsen | A: 영역 구분(10⁻³, 0.1, 10). B: 0.85 µm 틈 Kn 대기압 약 0.07 |
| P7 | J. Zhou 등, "Deposition Contribution Rates and Simulation Model Refinement for Polysilicon Films Deposited by Large-Sized Tubular LPCVD", *Materials* 17, 5952 (2024). [PMC11643910](https://pmc.ncbi.nlm.nih.gov/articles/PMC11643910/) | CC BY 4.0 | Figure 3 | 00-08 §2 실측 점과 예측 선 | A: 지름 420 mm, 182 mm Wafer 1,200장, SiH₄ 590 sccm, 26 Pa, 882–885 K, Ellipsometer. B: 0.100–0.107 nm/s, 오차 최대 3.8 % |

## 미국 특허

특허 본문과 도면은 USPTO PDF(`image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/번호`)에서 받았다. 도면은 PDF 안의 원본 1-bit 스캔을 그대로 잘랐고, 본문은 macOS Vision OCR로 읽어 도면 번호와 수치를 확인했다.

| ID | 특허 | 그림 | 넣은 곳 | 확인 |
|---|---|---|---|---|
| T1 | US 6,140,206 (Chartered Semiconductor Manufacturing, 2000), Method to form shallow trench isolation structures | FIG. 9 | 00-01 keep:0 (자체 그림 교체) | A: 30 기판, 34 완충 SiO₂, 44 CVD SiO₂, 50 Gate, 54 Source·Drain, 58 층간 절연막, 62 금속, 66 PECVD 질화막 Passivation. CMP가 38에서 멈춤 |
| T2 | US 5,653,807 (미 공군, 1997), Low temperature vapor phase epitaxial system for depositing thin layers of silicon-germanium alloy | FIG. 1–4 | 00-04 keep:4, 00-10 keep:0 (자체 그림 교체) | A: 실린더 8–14, Purge Panel 3, 감압기 22, MFC 26, Vent 11/Run 13, Turbo 25 → 27 → 기계식 Pump 29 → Oil Trap 35 → Dry Scrubber 33 → 팬 37, 누설 감지기 85·87(질량분석기), 종래 Venturi Purge 약 20회 |
| T3 | US 6,247,842 (National Semiconductor, 2001), Method of wafer temperature measurement | FIG. 1, 3 | 00-06 keep:0 (교체), 00-06 §3 | A: Wafer–Pedestal 온도 차 10–50 °C, HDP CVD는 Wafer가 더 뜨거움, 시험 Wafer SiO₂ 3,500/Ti 500/Al 2,000/TiN 300 Å, ΔRs 0.011 Ω/□·30초 → 425 °C |
| T4 | US 6,598,615 (Applied Materials, 2003), Compact independent pressure control and vacuum isolation for a turbomolecular pumped plasma reaction chamber | FIG. 3 | 00-07 keep:1 (자체 그림 교체) | A: 390 Chamber, 393 가스 배관, 394 Nozzle, 395 배기구, 320 Throttle Valve, 340 Gate Valve, 350 저진공, 330 고진공 |
| T5 | US 7,296,465 (MKS Instruments, 2007), Vertical mount mass flow sensor | FIG. 1A | 00-07 §4 MFC | A: 122 입구, 124 주 유로, 130 Bypass, 200 Sensor Tube, 250·251 코일, 140 Valve, 150 제어기, 온도 차 → 질량 |
| T6 | US 8,360,001 (ASM America, 2013), Process for deposition of semiconductor films | FIGURE 10, 12, 15 | 00-08 §3·공학 계산, 00-03 §3 | A: FIG. 10 조건 25 sccm·40 Torr, 525 °C 아래 반응 지배, 위쪽 평탄 구간 물질전달 지배. FIG. 12 650 °C·40 Torr·15–90초. FIG. 15 600 °C 비정질, 650 °C 부분 결정, 700·750 °C 결정. B: FIG. 12 두께 105/270/410/515/775 Å, FIG. 10의 550 °C 값 |
| T7 | US 6,649,278 (Micron Technology, 2003), Process for fabricating films of uniform properties on semiconductor devices | FIG. 4, 5 | 00-09 §4·공학 계산 | A: 49점 Map, FIG. 4 평균 1,833.47·표준편차 20.56 Å(1.121 %)·범위 66.31 Å, 그릇 모양. FIG. 5 평균 1,838.30·표준편차 13.84 Å(0.753 %)·범위 48.41 Å, 냉각 단계 증착 |

## 후보였으나 넣지 않은 것

- Chen 2025 (*Nanomaterials*, PMC12251017) SiN–SiOₓNᵧ–SiO₂ FTIR: 스펙트럼 모양이 일반적인 SiO₂·SiN 흡수와 맞지 않아 교재 예로 쓰지 않았다.
- Shi 2009 (*Sensors*, PMC3280852) Figure 2 Poly-Si XRD: 2θ ≈ 90°의 언덕을 비정질상으로 표시해 해석이 일반적이지 않다. 같은 목적으로 US 8,360,001 FIGURE 15를 썼다.
- Zhang 2021 (*Nanomaterials*, PMC8706910) Si–H FTIR 경시 변화, Li 2025 (*Molecules*, PMC11902027) Cat-CVD 균일도: 내용이 겹쳐 뺐다.
- US 5,366,911 FIG. 6 다층 배선 단면: 산소 이온 주입으로 Al을 절연체로 바꾸는 특수 공정이라 표준 구조 설명에 맞지 않았다.
- US 4,785,669 정전용량 압력계, US 7,941,039 Pedestal, US 8,622,068 소형 Gas Cabinet, US 7,695,700 배기가스 처리: 도면이 복잡하거나 같은 내용을 더 잘 보여 주는 도면이 있어 뺐다.
- 리뷰 논문(Radamson 2019·2020·2024, Moon 2023)의 소자 단면 TEM: 대부분 다른 저널에서 허락받아 옮긴 그림("Reprinted with permission")이라 쓰지 않았다.

## 남은 자체 제작 그림 (Part 00)

계산·조작 위젯 5개만 남겼다: 00-04 그림 1(반응식 계수 맞추기), 그림 2(mol과 원자 수), 00-05 혼합가스 분압 그림, 00-08 성장속도–누적 두께 Slider, 00-09 Histogram Bin Slider. 학습자가 값을 바꿔 보는 도구라서 논문 그림으로 바꿀 대상이 아니다.
