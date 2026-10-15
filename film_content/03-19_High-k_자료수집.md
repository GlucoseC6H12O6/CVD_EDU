# 03-19 · High-k Dielectrics — 자료 수집

수집일: 2026-10-14 · 본문 원고: `03-19_High-k_본문.md`

## 수집 방법과 한계

- 웹 검색으로 서지와 초록·요약을 확인했다. 논문 전문은 열람하지 못했다.
- **재료별 유전율·Band Gap·Band Offset 표는 2차 자료(웹 정리표)에서 왔다.** 원 리뷰(Robertson)의 표와 대조하지 못했다. 같은 재료의 값이 출처마다 다르다(ZrO₂의 k가 20–25 또는 약 40, TiO₂의 k가 60 또는 80). 상과 측정법에 따라 달라지는 값이므로 본문에서 그렇게 적었다.
- DRAM Capacitor의 **현행 양산 공정**에 관한 공개 자료는 없다. 연구 논문·학회 초록 수준이다.
- 확인 수준: **A** 서지와 수치를 초록·요약으로 확인 / **B** 서지(제목·존재)만 확인 / **C** 기억에 의존, 재확인 필요

## 1. 재료 일반 — 유전율과 Band Gap

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S01 | GlobalSino 정리표. [표 1](https://www.globalsino.com/EM/page2311.html) · [표 2](https://www.globalsino.com/EM/page2076.html) | 웹 정리표 (2차) | 재료별 k / Band Gap (eV) / Si 대비 전도대 Offset (eV): **SiO₂ 3.9 / 9 / 3.2, Si₃N₄ 7 / 5.3 / 2.4, Al₂O₃ 9 / 8.8 / 2.8, Y₂O₃ 15 / 6 / 2.3, La₂O₃ 30 / 6 / 2.3, HfO₂ 25 / 5.8 / 1.4, ZrO₂ 25 / 5.8 / 1.5, Ta₂O₅ 22 / 4.4 / 0.35, TiO₂ 80 / 3.5 / 0, SrTiO₃ 2000 / 3.2 / 0.** 다른 표에는 TiO₂ k = 60. 원 출처 미표기 | A (2차) | §2 |
| S02 | 유전율과 Band Gap의 역관계 서술(검색 요약의 교재·리뷰). [Cambridge 발췌](https://assets.cambridge.org/97811074/12194/excerpt/9781107412194_excerpt.pdf) 등 | 교재·리뷰 | 대체 재료의 **Band Gap은 유전율이 커질수록 대체로 작아진다.** 전자 분극은 작고 Gap이 작을수록 크다. **높은 유전율은 주로 이온(격자) 분극**에서 와야 한다. 문헌에 유전율·Gap·장벽 높이의 값이 폭넓게 흩어져 있다 | A (요약) | §2 |
| S03 | Rutgers 그룹 ZrO₂ 광전자 분광. [PDF](https://www.physics.rutgers.edu/~dhv/pubs/local_copy/ss_zrstack.pdf) | 논문 | Oxynitride/Si 위 ZrO₂: Gap **5.68 eV**, 가전자대·전도대 Offset **3.40 eV·1.16 eV.** HfO₂는 같은 상에서 ZrO₂보다 Gap이 약 0.6 eV 크다. ZrO₂는 상에 따라 유전율이 크게 다르고 **정방정이 높은 k와 높은 Gap을 겸한다** | A (요약) | §2 |
| S04 | TiO₂·ZrO₂·HfO₂ Band Offset 연구(ASU). [PDF](https://nemanich.physics.asu.edu/sites/default/files/2021-12/1.1639944.pdf) | 논문 | Si와 High-k 사이의 **전도대 Offset이 광학 Band Gap에 거의 선형으로 비례.** Anneal 후 가전자대 Offset 증가(Ti·Zr·Hf 산화물: 약 1.65·0.95·2.05 → 약 2.55·3.0·2.75 eV). Offset 측정은 재현성이 낮은 경우가 많다 | A (요약) | §2 |
| S05 | J. Robertson, “High dielectric constant gate oxides for metal oxide Si transistors,” *Rep. Prog. Phys.* 69, 327 (2006) | 리뷰 (기준 문헌) | High-k 재료 선택의 기준(k, Gap, Offset, 열역학 안정성, 계면). 원문 미열람. 서지는 기억 기반 | C | §2 |

## 2. HfO₂ — 게이트

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S06 | US 7,851,377 “Chemical vapor deposition process” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7851377); US 8,007,865 [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8007865); US 7,030,043 [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7030043) | 특허 | HfCl₄/H₂O ALD의 **300 °C 정상 상태 Cycle당 성장은 단층의 15–17 %뿐.** 반응 자리인 –OH의 부족 때문. 온도가 오를수록 성장이 줄어드는 것은 **HfO₂ 표면의 수산화 감소** 탓. 계면 재성장 때문에 **EOT 1 nm 이하를 얻기 어렵다** | A (요약) | §3, §4, §6 |
| S07 | AIChE 2007, 456a (DFT 계산). [초록](https://proceedings.aiche.org/conferences/aiche-annual-meeting/2007/proceeding/paper/456a-first-priniciples-calculation-atomic-layer-deposition-hfo2) | 학회 초록 | 염소와 배위가 부족한 표면 Hf 사이의 배위 결합으로 금속 전구체 종이 강하게 붙어, H₂O Pulse의 Cl 제거가 덜 효과적 | A (요약) | §3 |
| S08 | “Initial HfO₂ growth on Si(100) and GaAs(100) substrates using TEMAH+H₂O and TDMAH+H₂O ALD processes” [기록](https://mdsoar.org/handle/11603/1062?show=full); AVS 54th, EM-FrM5 [초록](https://www2.avs.org/symposium2007/Papers/Paper_EM-FrM5.html) | 논문·학회 | **TEMAH + H₂O: 250 °C에서 약 1.2 Å/cycle. TDMAH + H₂O: 275 °C에서 약 1.0 Å/cycle.** 선형 성장. 수산화 Si 위 TEMAH/H₂O에서 **약 7 Å의 SiOₓ/Silicate 계면층**이 50 Cycle 동안 거의 불변. TDMAH/H₂O는 8–10 Å | A (초록) | §3, §4, §6 |
| S09 | KIST 기록(H₂O/H₂O₂ 공정). [기록](https://pubs.kist.re.kr/handle/201004/126784?mode=full) | 논문 | Cycle당 성장이 280 °C까지 온도와 함께 감소하다가 **325 °C 위에서 전구체 열분해로 급증** | A (요약) | §4 |
| S10 | ECS Meeting Abstract 203, 0914 등. [PDF](https://www.electrochem.org/dl/ma/203/pdfs/0914.pdf) | 학회 초록 | 실용상 가장 얇은 **3 nm HfO₂에서 증착 후 Anneal의 재성장이 0이어도 최소 EOT는 1.23 nm.** 1 nm 미만 게이트를 얻으려면 하부층을 완전히 없애야 한다(HfO₂보다 높은 k의 재료를 쓰지 않는 한) | A (요약) | §5, §6 |
| S11 | Remote Plasma ALD HfO₂의 결정화, *Nanoscale Res. Lett.* 계열. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6405792) | 논문 (Open Access) | 250 °C 증착 후 RTA. **400 °C 아래: HfO₂와 계면층 모두 비정질**(계면층은 HfO₂ + SiO₂). **450–550 °C: 다상 다결정.** **550 °C 초과: 단일상 다결정이 지배**, 계면층은 결정질 SiO₂로 | A (요약) | §2, §6 |
| S12 | InAs 위 EOT < 1 nm HfO₂, *ACS Appl. Mater. Interfaces*. [기록](https://acs.figshare.com/articles/journal_contribution/Structural_and_Electrical_Properties_of_EOT_HfO_sub_2_sub_1_nm_Grown_on_InAs_by_Atomic_Layer_Deposition_and_Its_Thermal_Stability/3101404) | 논문 | 300 °C 증착 비정질 막 EOT 0.9 nm. 600 °C Anneal 후 단결정 사방정으로 전이, **유전율 약 24.** Anneal 후 EOT 1.0 nm와 계면 결함 증가(기판의 In 확산) | A (초록) | §2 |

## 3. ZrO₂ · ZAZ — DRAM Capacitor

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S13 | Martin 등, “Macroscopic and microscopic electrical characterizations of high-k ZrO₂ and ZrO₂/Al₂O₃/ZrO₂ metal-insulator-metal structures.” [ResearchGate](https://www.researchgate.net/profile/Dominik_Martin/publication/230626902_Macroscopic_and_microscopic_electrical_characterizations_of_high-k_ZrO2_and_ZrO2Al2O3ZrO2_metal-insulator-metal_structures/links/544744d90cf22b3c14e0c294.pdf); KU Leuven 저장소 [PDF](https://lirias.kuleuven.be/retrieve/344003) | 논문 | **가장 일반적인 DRAM Capacitor는 대칭 ZrO₂/Al₂O₃/ZrO₂(ZAZ) 적층.** 얇은 ZrO₂는 정방정으로 결정화하고 **유전율 약 40**이지만 누설이 크다. 얇은 비정질 Al₂O₃ 중간층이 누설을 **DRAM 기준 100 nA/cm² 아래**로 억제하되 유효 유전율을 낮춘다. k > 30에는 정방정이 필요하고, 고온 증착이나 증착 후 Anneal로 얻는데 **둘 다 누설을 키운다.** Al₂O₃는 RTA 중 **결정립이 막 전체를 관통하는 것을 막는다.** 문장별 출처 구분은 요약에 의존 | A (요약) | §1, §2, §6 |
| S14 | TiN/ZAZ/TiN MIM 연구(IEICE 기술 보고 2016). [기록](https://ken.ieice.org/ken/paper/20160629rbJ2/eng/) | 학회 논문 | **0.3 nm Al₂O₃ 층으로 누설 전류 밀도가 TiN/ZrO₂/TiN의 1/6.** Al₂O₃ 0.4 nm 이하 영역에서 전체 유전율 약 28 유지 | A (초록) | §2, §5 |
| S15 | ZAZ RTA 연구(검색 요약). KU Leuven 저장소 등 | 논문 | **10 nm ZAZ 막, 650 °C N₂ RTA 후 EOT 1.0 nm, 누설 약 3.2×10⁻⁸ A/cm² @1 V** | A (요약) | §5 |
| S16 | ECS Meeting 233 (2018) 초록. [초록](https://ecs.confex.com/ecs/233/webprogram/Paper109613.html) | 학회 초록 | Design Rule 20 nm 미만에서는 **ZAZ가 너무 얇아 결정화가 어렵고**, 유전율이 기대보다 낮다(특히 상부 ZrO₂). 상부 ZrO₂를 TiO₂로 바꾸는 제안. TiO₂는 **Band Gap이 3.4 eV로 작아** 단일 유전층으로 쓰기 어렵다 | A (초록) | §6, §9 |
| S17 | *J. Semicond.* (In Press). [링크](https://www.jos.ac.cn/en/article/doi/10.1088/1674-4926/26040002) | 논문 | AlZrO 합금 계면층을 가진 **5.7 nm ZrO₂ 계 MIM: EOT 0.89 nm, 누설 3×10⁻¹⁰ A/cm² @1 V.** 반강유전 정방정 ZrO₂ 안정화. 전 공정 350 °C 이하 | A (초록) | §9 |
| S18 | MRS Fall 2025 초록(Bi₂O₃ 중간층). [초록](https://www.mrs.org/meetings-events/annual-meetings/archive/meeting/presentations/view/2025-mrs-fall-meeting/2025-mrs-fall-meeting-4375334) | 학회 초록 | ZrO₂/TiN MIM에 초박 Bi₂O₃ 층 삽입으로 정방정 안정화, 누설 10배 이상 감소(약 10⁻⁸ A/cm²) | A (초록) | §9 |
| S19 | US 7,592,217 · US 8,084,804, “Capacitor with zirconium oxide and method for fabricating the same.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7592217) | 특허 | ZrO₂의 Band Gap 약 7.8 eV, 유전율 약 20–25로 서술(다른 출처의 값과 다르다) | A (요약) | §2 (주석) |

## 4. 기존 HTML(v0.9.1)에서 승계한 문헌 — 미재검증

| 서지 | 비고 |
|---|---|
| Hf-based high-k materials review, *Mater. Sci. Eng. R* (2010). [링크](https://www.sciencedirect.com/science/article/pii/S0927796X10001683) | EOT, 계면 산화막, Band Offset. 이번 수집에서 재열람하지 않음 |
| High-k ALD dielectrics properties review, *ECS J. Solid State Sci. Technol.* (2017). [DOI](https://doi.org/10.1149/2.0091710jss) | High-k의 누설과 유전율. 이번 수집에서 재열람하지 않음 |

## 5. 일반 지식 (기억 기반)

| ID | 내용 | 확인 | 본문 사용 |
|---|---|---|---|
| S20 | EOT = t × 3.9 / k. 적층은 층별 EOT의 합 | C | §5 |
| S21 | ALD 전구체: HfCl₄, TEMAH, TDMAH / TEMAZ, Cp 계 Zr 전구체(열 안정성이 높아 더 높은 온도에서 ALD 가능) / TMA. 산화제 H₂O, O₃ | C | §3 |
| S22 | TMA + H₂O ALD: 약 1.1 Å/cycle. ALD의 표준 모델 반응 | C | §3 |
| S23 | O₃는 TiN 전극을 산화시켜 TiOₓNᵧ 계면층을 만든다 | C | §6 |
| S24 | 도핑·박막 HfO₂·HfZrO의 사방정 상은 강유전성을 보인다 | C | §9 |
| S25 | La₂O₃·Al₂O₃ 초박 Cap으로 계면 쌍극자를 만들어 문턱 전압을 조절 | C | §9 |

## 본문에 넣은 원문 그림 (2026-10-14 추가)

내려받아 눈으로 확인한 그림만 넣었다. 특허 도면은 Google Patents의 원본 크기 도면이고, 논문 그림은 PMC의 Open Access 판이다. 캡션의 수치는 표시가 없으면 그래프에서 읽은 값이다.

| ID | 그림 | 라이선스 | 본문 위치 |
|---|---|---|---|
| S11 | Zhang 등, *Nanoscale Res. Lett.* 14, 83 (2019), Figure 2, 4. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6405792/) | CC BY 4.0 | §2.3, §6.3 |
| S26 | Ando, *Materials* 5(3), 478 (2012), Figure 6. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5448919/) | CC BY 3.0 | §5.1 |

새로 등록한 출처:

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S26 | T. Ando, “Ultimate scaling of high-κ gate dielectrics: higher-κ or interfacial layer scavenging?” *Materials* 5(3), 478–500 (2012). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5448919/) | 리뷰 (Open Access) | 문헌의 (SiO₂)/HfO₂ 게이트 적층 EOT–J_g 비교. 이상적 SiO₂ Scaling 기울기는 **EOT 0.2 nm당 J_g 10배.** 계면층 Scavenging의 실험 기울기가 넓은 EOT 범위에서 이 기울기를 따른다. La Cap은 EOT 손해 거의 없이 J_g를 낮춘다. 순수 HfO₂로 **EOT 0.50 nm** | A (요약) | §5.1 |

그림을 대조하며 확인한 것:

- S11은 Zhang 등, *Nanoscale Res. Lett.* 14, 83 (2019)이다. TEMAH + O₂ Plasma, 250 °C, 약 15 nm, N₂ RTA. GIXRD에서는 500 °C부터 피크가 보이고, 초록은 450–550 °C를 다상 다결정이라고 적었다.

## 6. 아직 비어 있는 자료

1. **S05(Robertson) 원문의 재료 표.** S01의 2차 표를 대조해야 한다.
2. **승계 리뷰 2편** 대조. 본문 §2의 범위 값.
3. **DRAM Capacitor ZAZ의 ALD 공정 조건**(전구체, 온도, 산화제, Cycle)과 고종횡비 단차 피복 자료.
4. **TiN 전극 계면층**의 두께·조성과 EOT의 관계.
5. **Zr 전구체별 ALD 온도 창**과 불순물(C, N) 자료.
6. **Metal Gate Stack**(계면층 / HfO₂ / Cap / 일함수 금속)의 공정 자료.
7. **강유전 HfZrO**의 공정 자료(이번 수집 범위 밖).
