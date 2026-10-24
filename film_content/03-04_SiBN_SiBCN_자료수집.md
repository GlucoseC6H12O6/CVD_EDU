# 03-04 · SiBN / SiBCN — 자료 수집

수집일: 2026-10-14 · 본문 원고: `03-04_SiBN_SiBCN_본문.md`

## 수집 방법과 한계

- 웹 검색으로 서지와 초록·요약을 확인했다. 논문 전문은 열람하지 못했다.
- **SiBCN의 k, HF Wet Etch Rate, 산화 내성을 한 표에 보고한 논문을 찾지 못했다.** Spacer용 SiBCN의 정량 자료는 IBM 학회 초록 1건과 특허뿐이다.
- 확인 수준: **A** 서지와 수치를 초록·요약으로 확인 / **B** 서지(제목·존재)만 확인 / **C** 기억에 의존, 재확인 필요

## 1. SiBN · SiBON (PECVD, 배선 절연막)

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S01 | “Use of SiBN and SiBON films prepared by plasma enhanced chemical vapor deposition from borazine as interconnection dielectrics,” *J. Electrochem. Soc.* 144(2), 658–663 (1997). [DOI](https://doi.org/10.1149/1.1837463) · [IBM 기록](https://research.ibm.com/publications/use-of-sibn-and-sibon-films-prepared-by-plasma-enhanced-chemical-vapor-deposition-from-borazine-as-interconnection-dielectrics) · [OSTI](https://www.osti.gov/biblio/465108) | 논문 | 평행평판 PECVD, **400 °C, 0.5 W/cm²**. SiBN은 Borazine + Si₂H₆ + NH₃, SiBON은 여기에 N₂O 추가. 조성 SiBN **Si₀.₀₉B₀.₃₉N₀.₅₁**, SiBON **Si₀.₁₆B₀.₂₉O₀.₄₁N₀.₁₄**. MIM으로 측정한 k: **SiBN 4.7, BN 4.1, SiBON 3.9**. 4 : 1 Trench에서 **Conformality 70 % 초과**. SiBON은 Cu 확산 Barrier로 양호. **저자 표기는 기록마다 달라 DOI로 확인 필요**(기존 HTML은 “Kone”, 색인은 “Kane”) | A (초록) | §2, §3, §4 |
| S02 | Essafti 등, “Preparation of SiNB films by CVD techniques: effect of SiH₄ addition to B₂H₆ and NH₃ gas mixtures,” *Diamond Relat. Mater.* (1996). [링크](https://www.sciencedirect.com/science/article/pii/0925963595004653) | 논문 | SiH₄–B₂H₆–NH₃ 계. NH₃ 유량을 고정하면 막의 원자 조성은 주로 [SiH₄]/[B₂H₆] 비로 정해진다. 미세 경도는 Si 함량을 따른다. 증착 방식(열·Plasma)은 초록 요약에서 확인하지 못했다 | A (초록 요약) | §3.3, §4.3 |

## 2. SiBCN · SiBN Spacer (ALD)

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S03 | “A novel ALD SiBCN low-k spacer for parasitic capacitance reduction in FinFETs,” VLSI Technology (2020), IBM. [IBM 기록](https://researcher.ibm.com/publications/a-novel-ald-sibcn-low-k-spacer-for-parasitic-capacitance-reduction-in-finfets) | 학회 논문 | 저온 ALD SiBCN과 최적화한 Spacer RIE로 Low-k 값을 유지. 14 nm RMG FinFET에 적용해 **Ring Oscillator 지연 약 8 % 개선**, 신뢰성 요구 충족. 초록에 k 값과 Etch Rate는 없다 | A (초록) | §1, §6 |
| S04 | US 10,672,773 · US 10,978,458, “Semiconductor device including ultra low-k spacer and method for fabricating the same.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10672773) | 특허 | SiBCN ALD Cycle: **SiH₂Cl₂(또는 SiH₄) / Purge / BCl₃ / Purge / C₂H₄(또는 CH₄) / Purge / NH₃ / Purge**. NF₃/H₂O Dry Etch에서 SiBCN 약 **0.2 Å / 250 s**, 일반 SiN 약 **14.6 Å / 250 s** | A (요약) | §3, §6 |
| S05 | US 9,171,736, “Spacer material modification to improve K-value and etch properties.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9171736) | 특허 | SiON·SiOCN·SiBCN 같은 Low-k Spacer는 **DHF·BHF 내성이 떨어진다.** k를 더 낮추려면 O·B를 늘려야 하고 그러면 Wet Etch Rate가 오른다. **표면 1–2 nm를 Plasma 질화**해 SiN에 가까운 Wet 내성을 얻는 방법 제안 | A (요약) | §2, §6 |
| S06 | US 9,419,101, “Multi-layer spacer used in finFET.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9419101) | 특허 | 탄소 분율이 다른 Low-k 층을 번갈아 쌓은 다층 Spacer. 가운데에 k가 낮은 층, 바깥에 k가 높은(내성 좋은) 층 | A (요약) | §6, §9 |
| S07 | US 6,962,876, “Method for forming a low-k dielectric layer for a semiconductor device.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6962876) | 특허 | ALD SiBN의 **k 약 4.4**. 비교 대상 LPCVD 막은 약 7 | A (요약) | §2 |
| S08 | US 11,515,145 B2 (공개 US 2022/0084809), “Deposition of silicon boron nitride films,” Chuanxi Yang·Hang Yu·Deenesh Padhi (Applied Materials). [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11515145) | 특허 | 기존 PECVD SiBN은 단차 피복과 Conformality가 낮고 높은 온도가 필요하다. CVD로 SiB 층을 올리고(첫 Cycle) 질소 Plasma로 처리하는(둘째 Cycle) 반복으로 윗면·바닥·측벽을 덮는 Conformal SiBN을 만든다. 실시 조건 수치는 요약에 없었다 | A (요약) | §3.4, §6.6 |
| S09 | US 7,633,125, “Integration of silicon boron nitride in high voltage and small pitch semiconductors.” [Google Patents](https://patents.google.com/patent/US7633125) | 특허 | SiBN의 소자 집적 | B | 미사용 |
| S10 | 게이트 Spacer 다단 산화 특허의 2차 요약. [링크](https://eureka.patsnap.com/triz-case/gate-spacer-oxidation-balance) | 특허 2차 요약 | C·N을 늘리면 식각 내성은 오르지만 k도 오른다. 건식 후 습식의 다단 산화로 조성 조절. **원 특허 미확인** | B | 미사용 |

## 3. PECVD SiBN · BN (배선 덮개, Cu Barrier, Spacer·Hardmask, DRAM 지지막)

사용자가 PECVD 쪽 보강을 요청해 2026-10-24에 찾았다. 특허 원문 사이트(USPTO, Google Patents)는 이 작업 환경에서 열리지 않아, US 8,084,105만 Google 특허 이미지 저장소의 원문 PDF를 받아 읽었고 나머지는 검색 요약으로 확인했다.

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S15 | US 8,084,105 B2, “Method of depositing boron nitride and boron nitride-derived materials,” Jeong-Uk Huh·Mihaela Balseanu·Li-Qun Xia·Victor T. Nguyen·Derek R. Witty·Hichem M'Saad (Applied Materials), 2011. [PDF](https://patentimages.storage.googleapis.com/dc/27/46/507a307f159d6f/US8084105.pdf) | 특허 | 300 mm Producer SE(Station 2개, 유량은 합계). 원료 B₂H₆·Borazine·알킬 Borazine, 희석 N₂·H₂·Ar, 도핑 SiH₄·TSA·TMS·HMCTZ·탄화수소·PH₃. 일반 범위 300–500 °C, 2–10 Torr, 13.56 MHz 및(또는) 300–400 kHz, 30–1,000 W. **증착–질화 반복**: B₂H₆ 400 + N₂ 2,000 sccm, 6 Torr, 480 mil, 5 s(20 Å/Cycle) → NH₃ 100 + N₂ 2,000 sccm, 300 W, 10 s. **k 4.7, n 1.810(500 Å), 밀도 2.4 g/cm³, 파괴 5 MV/cm, 단차 피복 > 95 %, PLE < 5 %**. Stress Liner 예: B₂H₆ 25·50 sccm, 400 °C, 100 W, 10 Cycle → 측벽/윗면 100·99 %, 바닥/윗면 98·100 %, 900 °C 30분 안정. B₂H₆ + NH₃ + SiH₄ 혼합 예: 바닥/윗면 91 %, 측벽/윗면 91 %, PLE 윗면 0·측벽 7·바닥 5 %. B₂H₆ + SiH₄가 굴절률 최고. B₂H₆ 유량 ↓ → N ↑, n ↓. 질화 Plasma의 HF 전력·NH₃·시간 ↑ → n ↓. UV Cure: H 제거, 치밀화, 인장 > 2.0 GPa. **동시 공급**: 증착 빠름, Hardmask용. 100 : 1 HF WERR 열산화막 대비 0.03, 열질화막 대비 0.3. Ar 첨가 → k ↓, 파괴 전압 ↑. 예: B₂H₆(5 % N₂) 3,000 + NH₃ 150 sccm, 300 W, 6 Torr, 480 mil. **SiBN Spacer**: k < 5.5, 파괴 > 6 MV/cm. SiH₄ 60, NH₃ 600, N₂ 1,000, B₂H₆ 100–1,000 sccm, 100 W, 6 Torr, 480 mil, 필요 시 400 °C UV 10분. B가 적은 BN·붕소 산화막 Liner가 B 외확산과 누설을 줄인다. FIG. 2·3 FTIR(N₂ 유량, 온도) | A (원문) | §0, §1.4, §3.3–3.5, §4.1, §4.3, §4.4, §6.4, §6.6, §8, §10 |
| S16 | US 12,451,345 B2 (공개 US 2024/0304437), “PECVD of SiBN thin films with low leakage current,” Diwakar N. Kedlaya 외 (Applied Materials), 2025. [USPTO PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12451345) | 특허 | 2019년 1월 가출원에서 이어진 계속 출원. DRAM 등 Capacitor의 지지막(Supporter)·Stopper용 PECVD SiBN. 기존 SiBN은 열 예산과 누설에서 불리. B 약 10–50 at%(약 20–40 at%), 누설 1×10⁻⁹ A/cm² 미만 @1.5 MV/cm, 증착 약 225–600 °C, 원격 또는 직접 Plasma. 청구항 1: Stopper의 B 약 18–50 at%. 종속항: 25–45 at%, N/Si 약 1.05–1.5, 같은 재료의 지지층 | A (요약) | §0, §1.4, §4.1, §4.3, §6.8, §8, §9, §10 |
| S17 | US 4,990,365, “Method for producing silicon boronitride layers,” Helmuth Treichel·Oswald Spindler·Bernhard Neureither (Siemens AG), 1991. [USPTO PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4990365) | 특허 | 배경: SiN은 습기·알칼리 이온 Barrier로 좋지만 k가 높다. M. Maeda·T. Makino, *Jpn. J. Appl. Phys.* 26(5), 660–665 (1987)가 평행평판 PECVD(SiH₄ + B₂H₆ + NH₃ + Ar)로 SiBN을 제안했으나 가스 공급이 복잡하고 조성 제어가 어렵다. 본 특허: B–N·Si–B–N 화합물 원료 PECVD, 약 300–450 °C, 조성이 재현된다 | A (요약) | §1.4 |
| S18 | US 6,967,405 · US 7,163,889(분할), “Film for copper diffusion barrier.” [USPTO PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6967405) | 특허 | B 첨가 SiN은 SiN보다 k가 낮지만 수분에 불안정해 시간이 지나며 k가 올라 Low-k Cu Barrier로 쓸 수 없게 된다. O·C를 포함한 Moisture Barrier 층과의 2층 구조로 대기에서 k 4.5 미만(좁은 청구항 3.0–4.5) 유지. 두께 100–1,500 Å. PECVD 원료 예: B₂H₆/Ar(5/95 %) 약 9,000 sccm, SiH₄ 약 50 sccm, NH₃ 약 500 sccm | A (요약) | §0, §1.4, §2.2, §4.1, §6.7, §8, §9, §10 |
| S19 | EP 0 394 054 A1 (1990), Silicon-boron nitride 배선 덮개 막. [EPO](https://data.epo.org/publication-server/rest/v1.2/patents/EP0394054NWA1/document.html) | 특허 | 배경: SiH₄ + B₂H₆ + NH₃ CVD로 만든 SiBN($\mathrm{Si}_x\mathrm{B}_y\mathrm{N}_z$, $x + y + z = 1$) 배선 덮개 막은 배선 위에 두껍고 배선 사이·측벽에 얇은 Overhang형이라 위층 배선의 단선·단락을 부른다. B₂H₆와 NH₃는 반응성이 커서 B 함량을 올리려고 B₂H₆ 분압을 높이면 기상 반응으로 단차 피복이 나빠진다. 본 발명: 유기 Si(HMCTS·HMDS) + 유기 B(TMB·TEB) + NH₃ 또는 유기 N 화합물 CVD. 출원인은 요약에 없었다 | A (요약) | §0, §1.4, §3.3, §3.5, §4.3, §6.6, §7, §10 |
| S20 | US 7,239,017 · US 7,842,604, “Low-k B-doped SiC copper diffusion barrier films” / US 7,420,275, “Boron-doped SiC copper diffusion barrier films” (Novellus Systems). [USPTO PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7420275) | 특허 | PECVD B 첨가 SiC Barrier, k 4.5 미만. 배경에서 NH₃를 쓰는 B 첨가 SiN의 Via Poisoning 우려를 든다 | A (요약) | §6.7, §9 |

## 4. 일반 지식 (기억 기반)

| ID | 내용 | 확인 | 본문 사용 |
|---|---|---|---|
| S11 | h-BN형 B–N 결합은 Si–N보다 분극률과 밀도가 낮아 k를 내린다. 비정질 BN에서 k 2 미만 보고(*Nature* 582, 511 (2020)) | C | §2, §9 |
| S12 | B–N 결합은 수분·산화성 약액에 가수분해돼 B–O(붕산)로 바뀐다. 탄소(Si–C)는 HF 내성을 준다 | C | §2, §6 |
| S13 | Chloride 전구체 + NH₃는 NH₄Cl을 만든다. 약 340 °C 아래에서 고체로 석출 | C | §7 |
| S14 | FTIR: h-BN 면내 신축 약 1,370–1,400, 면외 약 780–800, Si–N 약 830–900, N–H 약 3,350, B–H 약 2,500 cm⁻¹. XPS B1s: B–N 약 190.5, B–O 약 192–193 eV | C | §8 |

## 5. 기존 HTML(v0.9.1)에서 승계했으나 제외한 문헌

| 서지 | 제외 이유 |
|---|---|
| Laser CVD SiBCN, *J. Eur. Ceram. Soc.* (2019), [DOI](https://doi.org/10.1016/j.jeurceramsoc.2019.08.006) | 고온 구조 세라믹 코팅(최대 1,620 µm/h). 반도체 박막 공정이 아니다. |

## 6. 아직 비어 있는 자료

1. **S03 전문.** ALD SiBCN의 k, 조성, 증착 온도, Wet·Dry Etch Rate.
2. **조성(B·C·N·O)별 k와 HF Etch Rate의 관계표.** 지금은 특허의 정성 서술(S05)뿐이다.
3. **열 안정성.** S/D Epi와 Anneal 온도에서의 조성 변화, 붕소 외확산 실측.
4. **DRAM Bit Line Spacer 적용 사례.** 공개 논문으로 확인하지 못했다. 본문에서는 [현장]으로만 언급한다.
5. S02 전문(증착 방식, 조성별 성질).
6. **PECVD SiBN의 조성별 k·굴절률·HF Etch Rate 실측표.** S15는 BN 위주이고 SiBN은 k 상한만 있다. S16·S18의 실시예 수치(조성별 누설, 대기 노출 시간별 k)는 원문을 열지 못해 보지 못했다.
7. S17이 인용한 Maeda·Makino (1987) 원문, S19의 출원인.

## 본문에 넣은 원문 그림 (2026-10-15 추가)

Google Patents의 원본 크기 도면을 잘라 넣었다. 본문 첫머리에 있던 자체 제작 개념도는 빌드에서 뺐다. 캡션의 수치는 도면에 적힌 값이거나 특허 본문의 값이다.

| ID | 그림 | 라이선스 | 본문 위치 |
|---|---|---|---|
| S07 | US 6,962,876 FIG. 6 (유전율), FIG. 3·4 (RIE·Wet 식각 속도) | 미국 특허 도면 | §2.1, §2.2 |
| S15 | US 8,084,105 FIG. 2 (질화 처리 N₂ 유량별 BN FTIR), FIG. 3 (증착 온도별 BN FTIR). 원문 PDF의 1-bit 도면을 잘랐고 FIG. 3은 시계 방향으로 90° 돌렸다 | 미국 특허 도면 | §3.4, §4.3 |

## SEM·TEM 사진 추가 (2026-10-15)

사용자 요청으로 막질마다 실제 전자현미경 사진을 찾아 넣었다. PMC의 CC BY 논문과 미국 특허 도면만 썼고, 내려받아 눈으로 확인한 그림만 넣었다. 캡션의 공정 조건과 수치는 논문 본문이나 특허 본문에서 옮겼다.

| ID | 서지 | 라이선스 | 그림 | 본문 위치 |
|---|---|---|---|---|
| S07 | US 6,962,876 FIG. 5 (기존 S07 특허의 다른 도면) | 미국 특허 도면 | ALD SiBN 단차 피복 단면 SEM. 특허 본문: 단차 피복 약 95 % | §6.6 |
