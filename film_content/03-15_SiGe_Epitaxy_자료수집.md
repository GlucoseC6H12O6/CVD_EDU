# 03-15 · SiGe & Epitaxy — 자료 수집

수집일: 2026-10-14 · 본문 원고: `03-15_SiGe_Epitaxy_본문.md`

## 수집 방법과 한계

- 웹 검색으로 서지와 초록·요약을 확인했다. 논문 전문은 열람하지 못했다.
- **임계 두께의 수치는 대부분 특허에 인용된 값**이다. 원 논문(Matthews–Blakeslee 1974, People–Bean 1985)은 열람하지 못했다. 검색에서 얻은 식으로는 인용된 수치가 재현되지 않아(식의 형태·단위 차이로 추정) **본문에 식을 싣지 않고 인용 값만 실었다.**
- GAA Nanosheet용 Si/SiGe 적층의 **두께·Ge 농도·균일도 사양 수치는 확보하지 못했다.**
- GeH₄가 성장 속도를 올리는 메커니즘(수소 탈착 촉진)은 이번 검색에서 직접 확인하지 못했다. 붕소에 대해서만 같은 메커니즘이 확인됐다. 본문에서 구분해 적었다.
- 확인 수준: **A** 서지와 수치를 초록·요약으로 확인 / **B** 서지(제목·존재)만 확인 / **C** 기억에 의존, 재확인 필요

## 1. 성장 속도 · 선택 성장 · Loading

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S01 | “Fabrication of high quality strained SiGe on Si substrate by RPCVD,” *Chin. Sci. Bull.* (2012). [Springer](https://link.springer.com/article/10.1007/s11434-012-5020-7) | 논문 | RPCVD, SiH₂Cl₂ + GeH₄. **GeH₄ 유량이 늘면 SiGe 성장 속도가 가속되고, Ge 함량은 더 완만하게 증가.** Ge 함량과 GeH₄/SiH₂Cl₂ 유량 비의 경험식 제시. Chamber 압력이 오르면 성장 속도와 Ge 함량 모두 증가 | A (초록) | §3, §4 |
| S02 | ECS Meeting Abstract 206, 1345. [PDF](https://www.electrochem.org/dl/ma/206/pdfs/1345.pdf) | 학회 초록 | Si:B·SiGe:B의 성장 속도는 화학계에 관계없이 **B₂H₆ 유량과 함께 증가. 붕소 표면 자리에서 수소 탈착이 늘기 때문.** 다결정 SiGe의 성장은 GeH₄ 분압과 온도와 함께 증가, HCl을 넣으면 감소 | A (요약) | §3 |
| S03 | 선택 성장 해설(Semiconductor Digest 기사). [웹](https://sst.semiconductor-digest.com/issue/?id=17787) | 기사 | 선택 공정은 HCl로 열린 Si 영역에만 성장시키고 유전체 위에는 증착되지 않게 한다. **HCl은 Si 성장 속도를 낮추고 사용 가능한 온도 범위의 하한을 위로 민다.** 고온에서는 물질 전달 지배: DCS 유량을 두 배로 하면 성장 속도가 두 배, 온도 영향은 작다 | A (요약) | §3, §4 |
| S04 | Loading 효과 연구(검색 요약, 산업용 LPCVD 모듈의 선택 Si·SiGe). [색인](https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/7198485) | 논문 | 선택 Si 성장의 Global Loading 효과는 온도에 따라 완만히 감소. 반면 **저온 SiGe 성장 속도는 산화막 피복률에 강하게 의존.** **HCl 첨가로 SiGe 성장 속도의 산화막 피복률·Window 크기 의존성을 최소화** | A (요약) | §4, §6 |
| S05 | US 8,415,236, “Methods for reducing loading effects during film formation.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8415236) | 특허 | **SiH₄는 Seed Window가 작을수록 증착 속도가 낮고, SiH₂Cl₂는 반대로 작을수록 높다.** 두 전구체의 비를 골라 Window 크기 의존성을 상쇄. 최적 비는 온도와 HCl·GeH₄ 유량에 의존 | A (요약) | §6 |
| S06 | “Selective Si and SiGe epitaxy for MOS transistors,” *J. Cryst. Growth* (2003). [링크](https://www.sciencedirect.com/science/article/pii/S0022024803016300) | 논문 | 20 Torr, Mask 패턴 대 Blanket 성장과 Loading. **기존 HTML에서 승계. 이번 수집에서 재열람하지 않음** | B | 미사용 |

## 2. Nanosheet용 Si/SiGe 적층

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S07 | IBM·GlobalFoundries, ECS AiMES 2018. [초록](https://ecs.confex.com/ecs/aimes2018/webprogram/Paper113422.html) | 학회 초록 | 적층 수평 Nanosheet 트랜지스터는 SiGe/Si 초격자로 만든다. **SiGe는 희생층으로 채널 사이 간격을 정한다.** 넓은 Ge 농도 범위에서 결함 없는 Pseudomorphic 다층막, 300 mm Blanket 균일도 제시(수치는 초록에 없음). **저온 STI 공정**으로 Ge의 Si 채널 내 상호 확산과 SiGe의 소성 이완 결함을 억제. SiGe와 Ge–Si 혼합 영역은 Inner Spacer 형성과 채널 Release에서 선택 식각으로 제거 | A (초록) | §1, §6 |
| S08 | “Growth of complex SiGe/Ge superlattices by reduced pressure chemical vapour deposition.” [기록](https://pure.uhi.ac.uk/en/publications/growth-of-complex-sigege-superlattices-by-reduced-pressure-chemic/) | 논문 | **조성 변화의 급준성은 (Si)Ge 표면 위에 Si를 성장시킬 때 일어나는 Ge 편석이 제한.** 저온 성장으로 확산과 편석을 최소화. 층 두께는 설계에 근접, 계면 급준, 구조 전체 균일. HAADF-STEM이 두께·계면 평가에 적합 | A (초록) | §2, §6, §8 |
| S09 | US 12,363,971, “Graded superlattice structure for gate all around devices.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12363971) | 특허 | **Chlorosilane 전구체는 높은 성장 속도와 염소 표면 종결을 주어 계면 급준성이 뛰어나다.** 계면 급준성이 SiGe와 Si의 식각 선택비를 높인다. Ge가 낮은 Core와 양쪽의 Ge 높은 Cladding으로 전위 저감 | A (요약) | §3, §6 |
| S10 | US 10,892,368 · US 11,355,649, “Nanosheet transistor having abrupt junctions…” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10892368) | 특허 | 희생 SiGe **약 35 % Ge**, 채널 SiGe 약 10 % Ge의 예. Ge 농도 차이가 식각 선택비를 준다 | A (요약) | §1, §6 |
| S11 | “Ge/Si multilayer epitaxy and removal of dislocations from Ge-nanosheet-channel MOSFETs,” *Sci. Rep.* (2022). [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8770505/) | 논문 (Open Access) | Ge/SiGe 대신 **Ge/Si 다층**을 성장시켜 Ge와 Si의 큰 물성 차이를 선택 식각에 이용. 식각 후 Ge Nanosheet 형상이 거의 유지 | A (초록) | §9 |

## 3. 임계 두께

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S12 | J. W. Matthews, A. E. Blakeslee, *J. Cryst. Growth* 27, 118 (1974); R. People, J. C. Bean, *Appl. Phys. Lett.* 47, 322 (1985) | 논문 (기준 문헌) | Matthews–Blakeslee: 역학적 평형 모델(기존 전위가 변형에 의해 Misfit 전위로 늘어남). People–Bean: 에너지 균형 모델. 원문 미열람 | B | §2 |
| S13 | US 10,062,782 · US 10,727,344 · US 11,158,742, “Method of manufacturing a semiconductor device with multilayered channel structure.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10062782) | 특허 | **People–Bean 모델로 x = 0.3일 때 임계 두께 약 52 nm.** **실용 임계 두께는 People–Bean 값의 70 % 이하.** x가 클 때 People–Bean이 실험과 잘 맞는다 | A (요약) | §2, §5 |
| S14 | 임계 두께 해설(검색 요약의 특허·논문). US 6,989,058 [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6989058), US 7,273,799 [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7273799) 등 | 특허 | Matthews–Blakeslee는 **안정(평형) 한계**로, 750–900 °C에서 약 30분 Anneal해야 도달. People–Bean은 **준안정 한계**로, 550 °C MBE 성장 막의 실험과 일치. **Ge 10 %: 약 700 °C에서 안정 약 300 Å, 준안정 약 2,000 Å (Si(100) 위).** **Ge 약 50 %: 준안정 약 100 Å.** 온도가 높을수록 임계 두께가 작다. 성장 조건을 잘 고르면 준안정 변형 SiGe도 결함이 없다 | A (특허군) | §2, §5 |
| S15 | arXiv:2409.11081. [arXiv](https://arxiv.org/pdf/2409.11081) | 논문 | 이 곡선들은 Ge 40 % 미만의 SiGe에서만 실험적으로 검증됐다. 더 높은 Ge에서는 탄성 이완(양자점 형성)이 주된 이완 방식 | A (요약) | §2 |

## 4. 일반 지식 (기억 기반)

| ID | 내용 | 확인 | 본문 사용 |
|---|---|---|---|
| S16 | 격자 상수: Si 5.431 Å, Ge 5.658 Å(차이 4.18 %). Si₁₋ₓGeₓ: a(x) ≈ 5.431 + 0.200x + 0.027x² Å. Si(100)의 이축 탄성 계수 약 180 GPa | C | §2, §5 |
| S17 | Epi 전 표면 준비: HF-last 세정, H₂ Bake, 저온용 건식 화학 세정(NF₃/NH₃ Remote Plasma로 산화막을 승화성 염으로 바꿔 제거). 계면의 O·C가 결함의 씨앗 | C | §3, §6 |
| S18 | Source/Drain Epi: pFET은 SiGe:B(압축 변형으로 정공 이동도 향상), nFET은 Si:P. Facet 형성, Fin 간 Merge | C | §1, §6 |
| S19 | HR-XRD: 기판 피크와 막 피크의 각도 차로 Ge 농도, 간섭 무늬로 두께. 역격자 공간 Map으로 이완도 | C | §8 |
| S20 | 선택성의 원리: 유전체 위의 핵을 HCl이 Si 위의 막보다 빨리 식각한다. 증착과 식각을 번갈아 하는 Cyclic 방식 | C | §3 |

## 본문에 넣은 원문 그림 (2026-10-14 추가)

내려받아 눈으로 확인한 그림만 넣었다. 특허 도면은 Google Patents의 원본 크기 도면이고, 논문 그림은 PMC의 Open Access 판이다. 캡션의 수치는 표시가 없으면 그래프에서 읽은 값이다.

| ID | 그림 | 라이선스 | 본문 위치 |
|---|---|---|---|
| S21 | Radamson 등, *Nanomaterials* 10(8), 1555 (2020), Figure 17. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7466708/) | CC BY 4.0 | §1 |

새로 등록한 출처:

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S21 | H. H. Radamson 등, “State of the art and future perspectives in advanced CMOS technology,” *Nanomaterials* 10(8), 1555 (2020). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7466708/) | 리뷰 (Open Access) | 노드별 S/D SiGe의 Ge 농도. 그림: 90 nm 17 %, 65 nm 23 %, 45 nm 30 %, 32 nm 40 %, 22 nm 55 %. 본문 서술: 90 nm → 22 nm에서 19 % → 45 %, 10 nm Fin에서 50 % 초과 전망. **그림과 본문 수치가 다르다.** 그림의 원 자료는 논문의 참고문헌 [92] | A (요약) | §1 |

## SEM·TEM 사진 추가 (2026-10-15)

사용자 요청으로 막질마다 실제 전자현미경 사진을 찾아 넣었다. PMC의 CC BY 논문과 미국 특허 도면만 썼고, 내려받아 눈으로 확인한 그림만 넣었다. 캡션의 공정 조건과 수치는 논문 본문이나 특허 본문에서 옮겼다.

| ID | 서지 | 라이선스 | 그림 | 본문 위치 |
|---|---|---|---|---|
| S22 | C.-L. Chu, S.-H. Hsu, W.-Y. Chang 외, “Stacked SiGe nanosheets p-FET for Sub-3 nm logic applications,” *Sci. Rep.* 13, 9433 (2023). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10256751/) | CC BY 4.0 | Figure 2: LPCVD(DCS + GeH₄) Si₀.₈Ge₀.₂/Si 다층 단면 TEM | §1 |
| S23 | J. Li, X. Sun, Z. Huang 외, “Highly Selective Isotropic Etching of Si to SiGe Using CF₄/O₂/N₂ Plasma for Advanced GAA Nanosheet Transistor,” *Nanomaterials* 15(19), 1469 (2025). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12525734/) | CC BY 4.0 | Figure 7: Si 제거 뒤 SiGe Nanosheet 단면 TEM, EDS | §1 |

## 5. 아직 비어 있는 자료

1. **S12 원 논문**과 임계 두께 식. 본문에 식을 싣지 않았다.
2. **GeH₄에 의한 성장 속도 증가의 메커니즘**을 직접 다룬 문헌.
3. **Nanosheet 적층의 정량 사양**(층 두께, Ge %, 두께 균일도, 계면 폭). S07 전문.
4. **Source/Drain Epi**(SiGe:B, Si:P)의 농도·온도·Facet 자료. 본문 해당 부분은 [리뷰]·[현장] 수준이다.
5. **Pre-epi Clean** 조건과 계면 O·C 농도의 관계.
6. **Ge 상호 확산 계수**의 온도·농도 의존성(열 예산 계산용).
7. 승계 문헌(S06) 재확인.
