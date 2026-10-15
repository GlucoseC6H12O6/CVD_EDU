# Part 10 소자(Logic·DRAM·NAND) 자료 수집 기록 (2026-10-16)

사용자가 "DRAM / FLASH / LOGIC 등을 가르쳐 주는 Part 또는 Chapter를 추가하고 싶다"고 해 Part 10(Device Integration)을 새로 만들었다. 5개 장(10-01 소자 지도, 10-02 Logic Transistor, 10-03 Logic 배선, 10-04 DRAM, 10-05 NAND Flash)에 그림 18장을 넣었다(미국 특허 도면 7, CC BY 논문 11, 00-01 그림 재사용 1).

확인 수준: **A** = 논문 본문(PMC XML) 또는 특허 본문(Google Patents 설명)에서 설명과 수치를 확인. **B** = 서지(Crossref)만 확인하고 원문은 열람하지 못함. **T** = 교과서.

특허 도면은 USPTO PDF(`image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/번호`)의 원본 스캔을 `pdfimages`로 꺼내 잘랐다(`prep_figures.py` JOBS). 논문 그림은 PMC 기사 페이지의 그림을 받았다(`prep_figures.py` COPY). 후보는 NCBI E-utilities(`"cc by license"[filter]`)로 찾고, 리뷰 논문의 그림 가운데 캡션에 "Reprinted/Adapted with permission"이 붙은 것은 CC BY가 아니므로 쓰지 않았다(예: Radamson 외 2024, Nanomaterials, PMC11123950의 그림 대부분).

## 그림

| 출처 | 그림 | 넣은 곳 | 확인 |
|---|---|---|---|
| US 7,852,675 (Toshiba, 2010) Three dimensional stacked nonvolatile semiconductor memory | FIG. 9 | 10-01 §2 | A: Memory cell array 31, Sense amplifier 32, Driver 33L·33R, Level shifter 34, Address decoder 35, Block BK<0>–BK<n> |
| US 6,140,206 (Chartered, 2000) | FIG. 9 | 10-01 §3 | 00-01 그림 재사용 |
| Q. Zhang 외, Natl. Sci. Rev. 11, nwae008 (2024), CC BY 4.0, PMC10883695 | Figure 1 | 10-02 §4 | A: 구조 변천, 미세화 단계. 본문: Nanosheet 공정의 약 80 %가 HKMG-last FinFET과 같음, 새 공정 4가지(기생 Channel Implant, GeSi/Si 초격자 Epitaxy, Inner Spacer, Channel 해제), 초격자는 RPCVD로 650 °C 미만, Inner Spacer는 얇은 SiNx Conformal 증착, α-Si Dummy Gate, Samsung SF3 MBCFET |
| US 6,413,802 (Univ. of California, 2002) FinFET transistor structures having a double gate channel | FIG. 1 | 10-02 §3 | A: 절연층 2, Drain 4, Source 6, Fin 8, Hard Mask 9, 이중 Gate, Fin 도핑 불필요, 일함수로 Vt 조절, 제조 순서(Hard Mask→Fin 식각→희생 산화→Gate 절연막→Gate→Spacer) |
| C.-L. Chu 외, Sci. Rep. 13, 9433 (2023), CC BY 4.0, PMC10256751 | Figure 2, 5 | 10-02 §4 | A: SOI 위 Si/Si₀.₈Ge₀.₂ 다층 TEM, LPCVD 다층 Epitaxy, TMAH(60 °C) Si 선택 식각, ALD Y₂O₃·PVD TiN, Gate 길이 90 nm |
| US 6,518,171 (Intel, 2003) Dual damascene process using a low k interlayer | FIG. 1A–1D(종래 기술) | 10-03 §3 | A: Via 10→Trench 11→Etch Stop 제거→Barrier, Trench 영역을 두 번 식각하는 문제, Etch Stop SiN·SiC, 두 번째 Low-k를 나쁜 Step Coverage로 증착해 Via를 덮기만 함 |
| Y. Cui 외, Micromachines 11, 32 (2020), CC BY 4.0, PMC7019522 | Figure 2, 3 | 10-03 §2 | A: IMP Ti 200 Å + CVD TiN 2×50 Å, 비저항 73·280 µΩ·cm, 바닥 피복 57 %·80 %(종횡비 3.2), W 약 11.5 µΩ·cm, Via 저항 20 Ω 미만, 5층 Via Plug. 그림에서 Ti/TiN 위 150/100 Å, 바닥 85/80 Å |
| K. Zhao 외, Nanomaterials 12, 1760 (2022), CC BY 4.0, PMC9145433 | Figure 5 | 10-03 §5 | A: Liner Cu 3 nm·Ru 0.3 nm·Co 1 nm·W 0, 종횡비 1, Co·Ru·W는 M0·M1 Cu 대체 후보 |
| US 3,387,286 (IBM, R. H. Dennard, 1968) Field-effect transistor memory | FIG. 1 | 10-04 §1 | A: Cell 10 = Transistor 12 + Capacitor 14, Word Line 24, Bit Line 26, Driver 20·22, 저장 노드 30, 충전=1 |
| US 12,058,850 (Samsung Electronics, 2024) Semiconductor memory device and method of fabricating the same | FIG. 2 | 10-04 §2·§3 | A: 102 소자 분리, WL 홈 속(윗면이 ACT보다 낮음), 107 Gate 절연막, 110 덮개(SiN·SiO₂), BL = 130 Poly·131 실리사이드·132 금속, 137 SiN 덮개, Spacer 121·123·125(123 대신 Air Gap 가능), BC Poly·금속, LP, BE·DL·TE, Mold 172·176(SiO₂)·지지층 174(SiN), 구멍 축 기울어짐·정렬 어긋남, 지지 패턴 174a 남기고 Mold 등방 식각 |
| M. Sun, H. W. Baac, C. Shin, Micromachines 13, 1476 (2022), CC BY 4.0, PMC9505224 | Figure 1 | 10-04 §2 | A: BCAT 채택 이유(유효 Channel 길이 증가로 단채널 효과 억제), W Gate, SiO₂, Si₃N₄, Gate 길이 20 nm TCAD |
| J. Kim 외, Nanomaterials 15, 783 (2025), CC BY 4.0, PMC12156898 | Figure 2 | 10-01 §5, 10-04 §3 | A: Trench 종횡비 7 : 1·피치 76 nm·폭 38 nm, Capacitor 종횡비 100 : 1 초과(인용), 위아래 균일도 5 % 미만 요구, ZAZ 널리 사용, Thermal ALD 선호, 대안 HfO₂·ZrO₂·TiO₂·Al-doped TiO₂·SrTiO₃. 그림 값 DP 18.91/17.42 nm, RP 세움 12.41/12.32 nm |
| D. Lee, C. Shin, Micromachines 13, 1139 (2022), CC BY 4.0, PMC9322117 | Figure 1, 2 | 10-01 §1, 10-05 §2·§3 | A: 200층 넘는 8세대 양산 직전, Z-stacking·Z-scaling·XY-scaling, WL 수 2배에 Channel 높이 1.5배(인용), 마카로니→Nanowire, 위아래 Cell Vt 차이 |
| J. Jia 외, Micromachines 14, 1779 (2023), CC BY 4.0, PMC10536591 | Figure 2 | 10-01 §5, 10-05 §4 | A: Dual-deck로 깊은 Hole 식각 부담 완화, Poly-Plug 없음(Carbon 마개, Gate 막·Channel 한 번에)·있음(두 번), 정렬 어긋남에 의한 아래 Deck 맨 위 Cell 2차 식각, Deck 사이 산화막 두껍게·Dummy Cell 제안, Plug 방식은 전류 감소·편차 증가 |
| S. Ramesh 외, Micromachines 12, 1084 (2021), CC BY 4.0, PMC8467353 | Figure 9 | 10-05 §3 | A: 업계 WL은 W, WL 얇아지고 층 늘며 RC 지연, High-k Liner(Al₂O₃·HfO₂·ZrO₂)로 Erase 개선, 평면 시편 SiON 6/SiN 6/SiO₂ 7 nm + 2 nm High-k, 5층 3D 시험 구조와 정성적으로 비슷 |

## 본문에만 인용한 문헌

| 문헌 | 쓴 곳 | 확인 |
|---|---|---|
| D. Hisamoto 외, IEEE TED 47, 2320 (2000), doi:10.1109/16.887014 | 10-02 | B. Crossref 저자 순서가 원문과 달라 첫 저자는 원문 표기(Hisamoto)를 따랐다 |
| T. Ghani 외, IEDM 2003, 11.6.1, doi:10.1109/IEDM.2003.1269442 | 10-02 | B |
| K. Mistry 외, IEDM 2007, 247, doi:10.1109/IEDM.2007.4418914 | 10-01, 10-02, 10-03 | B |
| C. Auth 외, VLSI 2012, 131, doi:10.1109/VLSIT.2012.6242496 | 10-02 | B |
| N. Loubet 외, VLSI 2017, T230, doi:10.23919/VLSIT.2017.7998183 | 10-02 | B |
| D. Edelstein 외, IEDM 1997, 773, doi:10.1109/IEDM.1997.650496 | 10-03 | B |
| A. Grill 외, Appl. Phys. Rev. 1, 011306 (2014), doi:10.1063/1.4861876 | 10-03 | B |
| D. Gall, J. Appl. Phys. 127, 050901 (2020), doi:10.1063/1.5133671 | 10-03 | B. 금속별 ρ₀·λ 값은 03-18의 S01·S22 |
| C. Auth 외, IEDM 2017, 29.1.1, doi:10.1109/IEDM.2017.8268472 | 10-03 | B |
| J. Y. Kim 외, VLSI 2003, 11, doi:10.1109/VLSIT.2003.1221061 | 10-04 | B |
| T. Schloesser 외, IEDM 2008, doi:10.1109/IEDM.2008.4796820 | 10-04 | B |
| D.-S. Kil 외, VLSI 2006, 38, doi:10.1109/VLSIT.2006.1705205 | 10-04 | B |
| S. K. Kim, M. Popovici, MRS Bull. 43, 334 (2018), doi:10.1557/mrs.2018.95 | 10-01, 10-04 | B |
| J. A. Mandelman 외, IBM J. Res. Dev. 46, 187 (2002), doi:10.1147/rd.462.0187 | 10-04 | B |
| F. Masuoka 외, IEDM 1987, 552, doi:10.1109/IEDM.1987.191485 | 10-05 | B |
| H. Tanaka 외, VLSI 2007, 14, doi:10.1109/VLSIT.2007.4339708 | 10-05 | B |
| C. Monzio Compagnoni 외, Proc. IEEE 105, 1609 (2017), doi:10.1109/JPROC.2017.2665781 | 10-01, 10-05 | B |
| S. M. Sze, K. K. Ng, Physics of Semiconductor Devices (2007); J. D. Plummer 외, Silicon VLSI Technology (2000) | 10-01–10-05 | T |

## 찾았으나 쓰지 않은 것

- Samsung TCAT(Jang 외, VLSI 2009): Crossref에서 서지를 찾지 못해 인용하지 않았다. Gate Replacement 방식은 Compagnoni 2017 리뷰를 근거로 적었다.
- Q. Zhang 외 2024의 Figure 2(GAA 공정 흐름과 TEM): PMC 그림 해상도가 낮아 패널을 잘라 쓰면 글자를 읽을 수 없어 Chu 2023 Figure 2로 바꾸었다.
- Radamson 외 2019(Micromachines, "Miniaturization of CMOS", PMC6563067)와 2024(Nanomaterials, "CMOS Scaling for the 5 nm Node and Beyond", PMC11123950): 그림 다수가 다른 출판사 그림을 옮겨 실은 것이라 쓰지 않았다.
- 10-04의 Capacitor 용량과 읽기 신호(ΔV) 계산은 교육용 가정값(지름 40 nm, 높이 1.5 µm, 유효 유전율 30, 두께 6 nm, C_BL 50 fF)이며 특정 제품의 값이 아니다.

## 아직 비어 있는 자료

1. 3D NAND 산화막/질화막 적층의 층별 두께·응력 사양과 Wafer Bow의 공개 수치.
2. DRAM Capacitor Mold·지지막 두께와 Hole 식각 Hard Mask(ACL) 두께의 공개 수치.
3. 학회 논문(IEDM·VLSI) 원문. 지금은 서지만 확인했다.
4. HBM·Packaging(TSV, Hybrid Bonding), CMOS Image Sensor, 전력 반도체 장.
