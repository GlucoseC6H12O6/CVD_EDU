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
| S02 | Essafti 등, SiNB CVD, *Diamond Relat. Mater.* (1996). [링크](https://www.sciencedirect.com/science/article/pii/0925963595004653) | 논문 | SiH₄와 B₂H₆가 NH₃와 경쟁적으로 반응. **기존 HTML에서 승계. 이번 수집에서 재열람하지 않음** | B | §3 (주석) |

## 2. SiBCN · SiBN Spacer (ALD)

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S03 | “A novel ALD SiBCN low-k spacer for parasitic capacitance reduction in FinFETs,” VLSI Technology (2020), IBM. [IBM 기록](https://researcher.ibm.com/publications/a-novel-ald-sibcn-low-k-spacer-for-parasitic-capacitance-reduction-in-finfets) | 학회 논문 | 저온 ALD SiBCN과 최적화한 Spacer RIE로 Low-k 값을 유지. 14 nm RMG FinFET에 적용해 **Ring Oscillator 지연 약 8 % 개선**, 신뢰성 요구 충족. 초록에 k 값과 Etch Rate는 없다 | A (초록) | §1, §6 |
| S04 | US 10,672,773 · US 10,978,458, “Semiconductor device including ultra low-k spacer and method for fabricating the same.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10672773) | 특허 | SiBCN ALD Cycle: **SiH₂Cl₂(또는 SiH₄) / Purge / BCl₃ / Purge / C₂H₄(또는 CH₄) / Purge / NH₃ / Purge**. NF₃/H₂O Dry Etch에서 SiBCN 약 **0.2 Å / 250 s**, 일반 SiN 약 **14.6 Å / 250 s** | A (요약) | §3, §6 |
| S05 | US 9,171,736, “Spacer material modification to improve K-value and etch properties.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9171736) | 특허 | SiON·SiOCN·SiBCN 같은 Low-k Spacer는 **DHF·BHF 내성이 떨어진다.** k를 더 낮추려면 O·B를 늘려야 하고 그러면 Wet Etch Rate가 오른다. **표면 1–2 nm를 Plasma 질화**해 SiN에 가까운 Wet 내성을 얻는 방법 제안 | A (요약) | §2, §6 |
| S06 | US 9,419,101, “Multi-layer spacer used in finFET.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9419101) | 특허 | 탄소 분율이 다른 Low-k 층을 번갈아 쌓은 다층 Spacer. 가운데에 k가 낮은 층, 바깥에 k가 높은(내성 좋은) 층 | A (요약) | §6, §9 |
| S07 | US 6,962,876, “Method for forming a low-k dielectric layer for a semiconductor device.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6962876) | 특허 | ALD SiBN의 **k 약 4.4**. 비교 대상 LPCVD 막은 약 7 | A (요약) | §2 |
| S08 | US 11,515,145, “Deposition of silicon boron nitride films.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11515145) | 특허 | SiBN 증착 | B | 미사용 |
| S09 | US 7,633,125, “Integration of silicon boron nitride in high voltage and small pitch semiconductors.” [Google Patents](https://patents.google.com/patent/US7633125) | 특허 | SiBN의 소자 집적 | B | 미사용 |
| S10 | 게이트 Spacer 다단 산화 특허의 2차 요약. [링크](https://eureka.patsnap.com/triz-case/gate-spacer-oxidation-balance) | 특허 2차 요약 | C·N을 늘리면 식각 내성은 오르지만 k도 오른다. 건식 후 습식의 다단 산화로 조성 조절. **원 특허 미확인** | B | 미사용 |

## 3. 일반 지식 (기억 기반)

| ID | 내용 | 확인 | 본문 사용 |
|---|---|---|---|
| S11 | h-BN형 B–N 결합은 Si–N보다 분극률과 밀도가 낮아 k를 내린다. 비정질 BN에서 k 2 미만 보고(*Nature* 582, 511 (2020)) | C | §2, §9 |
| S12 | B–N 결합은 수분·산화성 약액에 가수분해돼 B–O(붕산)로 바뀐다. 탄소(Si–C)는 HF 내성을 준다 | C | §2, §6 |
| S13 | Chloride 전구체 + NH₃는 NH₄Cl을 만든다. 약 340 °C 아래에서 고체로 석출 | C | §7 |
| S14 | FTIR: h-BN 면내 신축 약 1,370–1,400, 면외 약 780–800, Si–N 약 830–900, N–H 약 3,350, B–H 약 2,500 cm⁻¹. XPS B1s: B–N 약 190.5, B–O 약 192–193 eV | C | §8 |

## 4. 기존 HTML(v0.9.1)에서 승계했으나 제외한 문헌

| 서지 | 제외 이유 |
|---|---|
| Laser CVD SiBCN, *J. Eur. Ceram. Soc.* (2019), [DOI](https://doi.org/10.1016/j.jeurceramsoc.2019.08.006) | 고온 구조 세라믹 코팅(최대 1,620 µm/h). 반도체 박막 공정이 아니다. |

## 5. 아직 비어 있는 자료

1. **S03 전문.** ALD SiBCN의 k, 조성, 증착 온도, Wet·Dry Etch Rate.
2. **조성(B·C·N·O)별 k와 HF Etch Rate의 관계표.** 지금은 특허의 정성 서술(S05)뿐이다.
3. **열 안정성.** S/D Epi와 Anneal 온도에서의 조성 변화, 붕소 외확산 실측.
4. **DRAM Bit Line Spacer 적용 사례.** 공개 논문으로 확인하지 못했다. 본문에서는 [현장]으로만 언급한다.
5. S02(승계) 재확인.

## 본문에 넣은 원문 그림 (2026-10-15 추가)

Google Patents의 원본 크기 도면을 잘라 넣었다. 본문 첫머리에 있던 자체 제작 개념도는 빌드에서 뺐다. 캡션의 수치는 도면에 적힌 값이거나 특허 본문의 값이다.

| ID | 그림 | 라이선스 | 본문 위치 |
|---|---|---|---|
| S07 | US 6,962,876 FIG. 6 (유전율), FIG. 3·4 (RIE·Wet 식각 속도) | 미국 특허 도면 | §2.1, §2.2 |

## SEM·TEM 사진 추가 (2026-10-15)

사용자 요청으로 막질마다 실제 전자현미경 사진을 찾아 넣었다. PMC의 CC BY 논문과 미국 특허 도면만 썼고, 내려받아 눈으로 확인한 그림만 넣었다. 캡션의 공정 조건과 수치는 논문 본문이나 특허 본문에서 옮겼다.

| ID | 서지 | 라이선스 | 그림 | 본문 위치 |
|---|---|---|---|---|
| S07 | US 6,962,876 FIG. 5 (기존 S07 특허의 다른 도면) | 미국 특허 도면 | ALD SiBN 단차 피복 단면 SEM. 특허 본문: 단차 피복 약 95 % | §6.6 |
