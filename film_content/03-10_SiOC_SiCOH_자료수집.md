# 03-10 · SiOC / SiCOH — 자료 수집

수집일: 2026-10-14 · 본문 원고: `03-10_SiOC_SiCOH_본문.md`

## 수집 방법과 한계

- 웹 검색으로 서지와 요약을 확인했다. Open Access 논문 1편(S06)을 제외하면 전문은 열람하지 못했다.
- 전구체별 k–Modulus 수치의 상당수는 **특허가 다른 연구를 인용한 값**이다. 원 논문의 공정 조건을 확인하지 못했다.
- 확인 수준: **A** 서지와 수치를 초록·요약으로 확인 / **B** 서지(제목·존재)만 확인 / **C** 기억에 의존, 재확인 필요

## 1. 리뷰 · 기본 문헌

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S01 | A. Grill, “Porous pSiCOH ultralow-k dielectrics for chip interconnects prepared by PECVD,” *Annu. Rev. Mater. Res.* 39 (2009). [링크](https://www.annualreviews.org/content/journals/10.1146/annurev-matsci-082908-145305) | 리뷰 | 다공성 pSiCOH의 제조와 구조·전기·기계 물성. **k 2.0 미만까지 도달.** **k 2.4 막이 45 nm 제품에 적용.** 다공성은 증착 후 Cure로 만든다: 이중상(Dual-phase) 막을 증착하고 열 Anneal·전자빔·UV로 Cure. 저자·제목은 기억 기반, 검색 결과에 저자 표기는 없었음 | A (요약) | §0, §1, §3 |
| S02 | IBM, “Ultralow dielectric constant pSiCOH films prepared with tetramethylcyclotetrasiloxane as skeleton precursor” 등. [IBM 기록](https://researchweb.draco.res.ibm.com/publications/ultralow-dielectric-constant-psicoh-films-prepared-with-tetramethylcyclotetrasiloxane-as-skeleton-precursor) | 논문 | **TMCTS**로 Porogen 없이 **k 2.8**까지. Porogen을 섞어 증착하고 **400 °C Anneal**로 제거하면 **k 1.95**까지. TMCTS 계에서 **Porogen 편입 효율이 매우 낮고** Porogen 종류에 의존. **RF Power는 골격 전구체를 과도하게 깨지 않을 만큼 낮아야 하고, Porogen을 쪼갤 만큼은 높아야** 한다 → 쓸 수 있는 골격–Porogen 조합이 제한된다. 적합한 Porogen은 고리형 불포화 탄화수소(Terpinene, Norbornene 계) | A (요약) | §3, §4 |
| S03 | IBM Research Reports RC22009, RC22361, RC22643, RC24405. [RC22009](https://dominoweb.draco.res.ibm.com/reports/RC22009.pdf) · [RC24405](https://dominoweb.draco.res.ibm.com/reports/rc24405.pdf) | 연구 보고 | SiCOH에 유기 전구체를 함께 증착한 이중상 막으로 **k 2.1**까지. **경도와 Modulus는 k가 내려갈수록 감소.** 당시 업계 Low-k는 FSG(k 약 3.5), **SiCOH는 90 nm 노드부터, 2004년까지 업계 전반 채택.** Porogen 농도는 조합마다 다르게 필요 | A (요약) | §1, §2 |
| S04 | US 8,298,965, “Volatile precursors for deposition of C-linked SiCOH dielectrics” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8298965); US 7,282,458 · US 7,030,468 “Low k and ultra low k SiCOH dielectric films and methods to form the same” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7282458) | 특허 (타 연구 인용 포함) | 전구체로 DEMS·OMCTS·TMCTS 등을 열거. 인용 값: **DEMS(Porogen 없음) k 2.90에서 Young’s Modulus 16.5 GPa**, **Trimethylsilane k 2.85에서 8.76 GPa**, **DMDMOS k 2.88에서 6.68 GPa**. **DEMS/ATRP 다공성 막 k 2.41에서 3.2 GPa**(집적에 필요한 수준보다 크게 낮다고 평가). Porogen 내장형 전구체(VTEOS, VMDEOS) 막은 **2.94–3.78 GPa**. 원 논문 조건 미확인 | A (요약) | §2, §3 |

## 2. 기계적 강도 개선

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S05 | “Nanoporous SiCOH/CₓHᵧ dual phase films with an ultralow dielectric constant and a high Young’s modulus,” *J. Mater. Chem. C* (2013). [RSC](https://pubs.rsc.org/en/content/articlelanding/2013/tc/c3tc00587a) · [KAIST 기록](https://koasas.kaist.ac.kr/handle/10203/174801) | 논문 | PECVD Allyltrimethylsilane 막. Porogen 처리 후 **k ≈ 2.4, Young’s Modulus 8.4 GPa**. 제목–수치 대응은 검색 요약에 의존 | A (요약) | §2, §9 |
| S06 | Sa 등, “Enhanced thermo-mechanical reliability of ultralow-k dielectrics with self-organized molecular pores,” *Materials* 14(9), 2284 (2021). [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8125368/) · [MDPI](https://www.mdpi.com/1996-1944/14/9/2284/html) | 논문 (Open Access) | 분자 크기의 균일한 기공을 가진 다공성 SiCOH. **같은 k 2.1에서 Nanoindentation Modulus 13 GPa**, 기존 방식 다공성 막은 **6 GPa**. Ball Indentation에서 점소성 변형 저항이 강함. **400 °C, 4시간 압입 후 압입 깊이 5 nm로 기존 SiCOH보다 약 89 % 작다.** 리뷰 부분: 중성빔 CVD로 비다공성 초저k SiCOH에서 Modulus 10 GPa 초과 보고. **기존 HTML 승계 문헌, 이번에 재확인** | A (초록) | §2, §9 |
| S07 | Advanced PECVD SiCOH Low-k, *Microelectron. Eng.* (2013). [DOI](https://doi.org/10.1016/j.mee.2013.10.028) | 논문 | k 약 1.82 시편. **기존 HTML에서 승계. 이번 수집에서 재열람하지 않음** | B | 미사용 |

## 3. Plasma 손상 · Cure

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S08 | US 7,223,704, “Repair of carbon depletion in low-k dielectric films” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7223704); US 7,415,902 [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7415902); US 11,756,786 [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11756786) | 특허 | 다공성 SiCOH의 **k 약 1.8–2.95**, k가 낮을수록 기공률이 높다. 식각·Ash에서 Plasma에 노출된 표면의 **탄소 고갈**, 일부 공정에서는 내부까지. **Si–CH₃ 결합이 끊어져 Si Dangling Bond → Silanol(Si–OH) 생성 → k 상승, 소수성이던 막이 친수성으로.** 이후 수분 흡착으로 유효 k가 크게 오른다. **k 2.6 미만의 초저k(기공이 큼)가 k 2.6 초과의 미세 기공 막보다 손상을 훨씬 크게 받는다.** 탄소 고갈의 복구(Repair) | A (요약) | §2, §6 |
| S09 | “Effect of plasma damage on the material composition and electrical performance of different generations of SiOCH low-k films,” MRS Proc. [링크](https://www.cambridge.org/core/journals/mrs-online-proceedings-library-archive/article/abs/effect-of-plasma-damage-on-the-material-composition-and-electrical-performance-of-different-generations-of-sioch-low-k-films/3355A9CA05C99F4DCE7BADE41B8ADF6F) | 학회 논문 | 모든 Plasma 처리 시편에서 **k 상승과 절연 파괴 전압 저하.** 손상은 기공률이 가장 높은 막에서 가장 크다. 접촉각과 FTIR로 수분 흡착 확인. **증착 직후 In-situ He Plasma 처리**가 이후 Plasma 노출에 대한 저항을 높인다. 집적 중 수분 흡수 관리 필요 | A (초록) | §6 |
| S10 | 손상 전파 모델, arXiv:1102.3084. [arXiv](https://arxiv.org/pdf/1102.3084) | 논문 | 다공성 Low-k의 Plasma 손상을 반응–확산 과정으로 기술. 손상 Front 전파의 포화 | B | §6 (주석) |
| S11 | UV Cure 특허군. US 7,208,389 “Method of porogen removal from porous low-k films using UV radiation” [Google Patents](https://patents.google.com/patent/US7208389), US 7,629,272 [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7629272), US 7,265,061 [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7265061), US 8,629,068 [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8629068) | 특허 | Porogen은 최종 막에서 빈 자리가 될 위치를 차지한다. UV 제거의 두 경로: ① **UV가 Porogen을 직접 분해** ② **산소 존재하에 UV가 O₃·O 라디칼을 만들어 Porogen을 산화.** 열 제거는 **400 °C 초과에서 수 시간**이 필요. 대표 Porogen은 **α-Terpinene(ATRP)**. UV는 Porogen 제거와 함께 **기계적 강도를 높인다.** 다중 Station 순차 Cure | A (요약) | §3, §4 |
| S12 | US 8,398,816 · US 9,073,100 · US 11,177,131, “Method and apparatuses for reducing porogen accumulation from a UV-cure chamber.” [Google Patents](https://patents.google.com/patent/US8398816) | 특허 | UV Cure Chamber 안의 **Porogen 축적** 저감 | B | §7 |

## 4. 일반 지식 (기억 기반)

| ID | 내용 | 확인 | 본문 사용 |
|---|---|---|---|
| S13 | 기공률과 k의 관계(Lorentz–Lorenz 형 유효 매질 근사). 다공체의 Modulus는 (1−P)ⁿ, n ≈ 2–3에 비례 | C | §5 |
| S14 | FTIR: Si–CH₃ 약 1,275, Si–O–Si Network 약 1,040·Cage 약 1,140, C–H 약 2,970, Si–H 약 2,200 cm⁻¹ | C | §8 |
| S15 | Ellipsometric Porosimetry: 용매 증기 흡착에 따른 굴절률 변화로 기공률과 기공 크기를 구한다 | C | §8 |
| S16 | 전구체 끓는점: DEMS 약 95 °C, OMCTS 약 175 °C, ATRP 약 174 °C | C | §7 |
| S17 | 집적 대응: Metal Hardmask(TiN)로 Ash 노출 축소, 환원성·저손상 Ash, Pore Sealing, Silylation 복구 | C | §6 |

## 본문에 넣은 원문 그림 (2026-10-14 추가)

내려받아 눈으로 확인한 그림만 넣었다. 특허 도면은 Google Patents의 원본 크기 도면이고, 논문 그림은 PMC의 Open Access 판이다. 캡션의 수치는 표시가 없으면 그래프에서 읽은 값이다.

| ID | 그림 | 라이선스 | 본문 위치 |
|---|---|---|---|
| S06 | Sa 등, *Materials* 14(9), 2284 (2021), Figure 1, 3. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8125368/) | CC BY 4.0 | §2.3, §6.1 |

그림을 대조하며 확인한 것:

- Figure 4(FTIR)는 내려받았으나 그림에 적힌 수치의 정의를 확인하지 못해 넣지 않았다.

## SEM·TEM 사진 추가 (2026-10-15)

사용자 요청으로 막질마다 실제 전자현미경 사진을 찾아 넣었다. PMC의 CC BY 논문과 미국 특허 도면만 썼고, 내려받아 눈으로 확인한 그림만 넣었다. 캡션의 공정 조건과 수치는 논문 본문이나 특허 본문에서 옮겼다.

| ID | 서지 | 라이선스 | 그림 | 본문 위치 |
|---|---|---|---|---|
| S18 | M. K. Park 외, *Materials* 14(5), 1144 (2021) (03-01 S28과 같은 논문). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7957736/) | CC BY 4.0 | Figure 3: ACL Strip 전후 SiOC(H) 단면 SEM | §6.1 |

## 5. 아직 비어 있는 자료

1. **S04 인용 값의 원 논문**(DEMS 16.5 GPa 등)과 측정 조건.
2. **UV Cure 조건(파장·시간·온도)에 따른 k·Modulus·수축률**의 정량 데이터.
3. **Plasma 손상 깊이**의 실측(식각·Ash Chemistry별).
4. **TDDB·CPI 신뢰성**과 막 물성의 상관 자료.
5. 다공성 SiCOH의 **Pore Sealing** 공정 자료.
6. S07(승계) 재확인.
