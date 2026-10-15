# 03-07 · PSG / BSG — 자료 수집

수집일: 2026-10-14 · 본문 원고: `03-07_PSG_BSG_본문.md`

## 수집 방법과 한계

- 웹 검색으로 서지와 요약을 확인했다. 논문 전문은 열람하지 못했다.
- **PSG의 인 농도와 흡습·Al 부식의 관계를 수치로 준 출처를 이번 검색에서 찾지 못했다.** 본문의 해당 서술은 교과서 수준 통설로 표시했고 문턱 농도는 적지 않았다.
- HDP-PSG, DRAM Mold 산화막, BSG Hardmask에 관한 공개 자료도 확보하지 못했다. 본문에서 [현장]으로만 언급한다.
- 확인 수준: **A** 서지와 수치를 요약으로 확인 / **B** 서지(제목·존재)만 확인 / **C** 기억에 의존, 재확인 필요

## 1. PSG — Gettering과 조성

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S01 | Enigmatic Consulting, “Gettering and Transport of Mobile Ions.” [웹](https://enigmatic-consulting.com/semiconductor_processing/selected_shorts/Gettering.html) | 웹 해설 | P-doped 유리는 **Na·K 이온의 Sink**로 작용하고, 한 번 붙잡은 이온은 전계가 걸려도 잘 놓지 않는다. 이동성 이온 문제를 억제하는 가장 강력한 수단이 P-doped 산화막. 현대 IC의 BPSG 층에도 공정 유래 Na가 상당량 들어 있다(청정도만으로는 부족). Passivation은 SiN 또는 PSG/Nitride 적층 | A (요약) | §1, §2 |
| S02 | US 5,897,364, “Method of forming N- and P-channel transistors with shallow junctions.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5897364) 외 | 특허 | PSG 층이 Gettering 층으로 Na 이온을 가두어 게이트 산화막을 보호. 한 특허에서 **PSG의 최적 P 농도 약 3–5 %**(해당 공정 한정) | A (요약) | §2, §4 |
| S03 | BPSG 특허군(→ 03-06 자료수집 S02) | 특허 | **PSG는 950–1,100 °C에서 연화·Reflow** | A | §2 |
| S04 | POCl₃ 확산의 PSG(태양전지 문헌). [기록](https://kops.uni-konstanz.de/entities/publication/0ef7808d-1444-40ec-9e6f-f540b85147b5) | 논문 | 약 800–900 °C의 POCl₃ + O₂ 분위기에서 Si 표면에 PSG가 형성되고, 이것이 P 확산원이 된다 | A (요약) | §1 |

## 2. BSG · PSG — 고체 확산원 (Solid-source Doping)

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S05 | AVS 63rd Symposium (2016), TF-ThP16. [초록](https://www2.avs.org/symposium2016/Papers/Paper_TF-ThP16.html) | 학회 초록 | **14 nm 노드에서 Sub-fin 도핑을 고체 확산원으로 구현**한 기술이 보고됨(Punch-through Stopper 최적화). BSG·PSG를 Drive-in Anneal 조건과 Cap 종류별로 평가. 고체 확산원은 채널 아래에 고농도를 만들 수 있는 반면, 이온 주입은 채널의 불순물 농도 상승과 Si 손상을 일으킨다 | A (초록) | §1, §5 |
| S06 | US 11,302,583, “Solid-phase source doping method for FinFET structure.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11302583) | 특허 | **BSG 두께 2–5 nm, B 농도 1×10²⁰ – 5×10²¹ cm⁻³.** Cap 증착 전 상면의 PSG·BSG를 제거해 Fin 측벽에만 남긴다. Anneal로 P·B를 기판으로 확산. Cap이 도펀트 유출을 막고, Drive-in 후 유리를 제거한 뒤 산화막을 채운다 | A (요약) | §4, §5, §6 |
| S07 | US 9,583,489, “Solid state diffusion doping for bulk finFET devices.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9583489) | 특허 | 도핑 유리 층 **1–10 nm**. CVD 또는 PEALD. BSG를 **B₂O₃ Cycle과 SiO₂ Cycle을 번갈아** 쌓아 만들고, 각 Cycle에서 O₂ Plasma로 산화. B 전구체 **TEB 또는 TMB**. **B 농도는 B₂O₃ : SiO₂ Cycle 비로 조절** | A (요약) | §3, §4 |
| S08 | US 9,698,018, “Introducing self-aligned dopants in semiconductor fins.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9698018) | 특허 | SiN Cap으로 도펀트를 Fin으로만 밀어 넣고 STI로는 가지 않게 하는 자기정렬 방식. BSG 층이 손상될 수 있고 도펀트가 STI로 들어갈 수 있다는 문제 제기 | A (요약) | §6 |
| S09 | US 9,218,973, “Methods of doping substrates with ALD.” [Google Patents](https://patents.google.com/patent/US9218973); US 10,896,852 [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10896852) | 특허 | ALD 붕소(BCl₃ 등) 직접 증착에 의한 Conformal 도핑, Sub-fin 도핑 | B | §9 |
| S10 | UIUC ECE444 실습 Recipe(Boron Pre-deposition). [웹](https://fabweb.ece.illinois.edu/recipe/bpre.aspx) | 교육 자료 | B₂O₃가 Si와 반응해 BSG를 만들고 붕소가 Si로 들어간다. 표면 농도는 고용 한계로 고정, 분포는 상보 오차 함수 | A (요약) | §5 |

## 3. 기존 HTML(v0.9.1)에서 승계한 문헌

| 서지 | 비고 |
|---|---|
| Osório 등, BSG/BPSG의 Anneal, *Appl. Surf. Sci.* (1993). [링크](https://www.sciencedirect.com/science/article/pii/016943329390620Q) | 200–900 °C N₂ Anneal에서 B·P 조성 응답. 이번 수집에서 재열람하지 않음 |

## 4. 일반 지식 (기억 기반)

| ID | 내용 | 확인 | 본문 사용 |
|---|---|---|---|
| S11 | P₂O₅가 SiO₂에 들어가면 P=O 말단과 비가교 산소 자리가 생겨 양이온(Na⁺)을 붙잡는다 | C | §2 |
| S12 | 인 농도가 높은 PSG는 흡습해 인산을 만들고 Al 배선을 부식시킨다. 그래서 Passivation의 PSG는 농도를 제한하고 SiN으로 덮는다 | C | §2, §6 |
| S13 | B₂O₃는 흡습성이 강하고 물에 녹는다. BSG는 PSG보다 대기 중에서 불안정하다 | C | §2, §6 |
| S14 | HDP-CVD로 SiH₄ + PH₃ + O₂ PSG를 증착해 Reflow 없이 PMD를 채운다 | C | §1, §3 |
| S15 | 도핑 산화막은 HF에 USG보다 빨리 녹는다. 희생막·Mold 산화막에서 이 차이를 이용한다 | C | §1, §6 |

## 본문에 넣은 원문 그림 (2026-10-14 추가)

내려받아 눈으로 확인한 그림만 넣었다. 특허 도면은 Google Patents의 원본 크기 도면이고, 논문 그림은 PMC의 Open Access 판이다. 캡션의 수치는 표시가 없으면 그래프에서 읽은 값이다.

| ID | 그림 | 라이선스 | 본문 위치 |
|---|---|---|---|
| S06 | US 11,302,583 FIG. 1b, 1c | 미국 특허 도면 | §1.3 |

## 5. 아직 비어 있는 자료

1. **PSG 인 농도와 흡습·Al 부식의 정량 관계.** 통설의 원 출처.
2. **Gettering 용량.** 인 농도·막 두께 대비 붙잡을 수 있는 Na 양의 정량 자료.
3. **HDP-PSG**의 조성·Gap-fill·막질에 관한 공개 자료.
4. **S05 전문.** BSG·PSG의 Drive-in 조건별 접합 깊이와 Dose.
5. **DRAM Mold 산화막, BSG Hardmask**의 공개 자료.
6. 도핑 농도별 HF Wet Etch Rate 수치.
