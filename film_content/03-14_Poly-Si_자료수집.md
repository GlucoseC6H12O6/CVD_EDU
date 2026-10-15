# 03-14 · Poly-Si (Polycrystalline Silicon) — 자료 수집

수집일: 2026-10-14 · 본문 원고: `03-14_Poly-Si_본문.md`

## 수집 방법과 한계

- 웹 검색으로 서지와 초록·요약을 확인했다. 논문 전문은 열람하지 못했다.
- **응력의 부호가 바뀌는 온도가 출처마다 다르다.** 장비·압력·측정법이 다르기 때문이다. 본문에서 차이를 그대로 적었다.
- 비정질/다결정 전이에 관한 자료는 03-13 a-Si와 겹친다. 같은 문헌은 그쪽 ID를 함께 적었다.
- 확인 수준: **A** 서지와 수치를 초록·요약으로 확인 / **B** 서지(제목·존재)만 확인 / **C** 기억에 의존, 재확인 필요

## 1. 증착 속도론

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S01 | EESemi, “Polysilicon Deposition.” [웹](https://eesemi.com/polysilicon-deposition.htm) | 웹 해설 | SiH₄ 열분해로 **580–650 °C**에서 증착. **활성화 에너지 약 1.7 eV.** 통상 증착 속도 **10–20 nm/min**. 600 °C에서는 결정립이 매우 미세, 625 °C에서는 뚜렷하고 막 면에 수직인 주상 구조 가능 | A (요약) | §0, §3, §4 |
| S02 | 급속 열 LPCVD 연구(OSTI 기록). [링크](https://www.osti.gov/biblio/68542) | 논문 | 약 780 °C 아래에서는 **표면 반응 지배, 활성화 에너지 39 ± 2 kcal/mol**(약 1.7 eV). 780 °C 위에서는 활성화 에너지 감소. 고속 증착에서 비정질/다결정 전이 약 600 °C | A (요약) | §3 |
| S03 | AVS 50th Symposium (2003), TF-WeP23. [초록](https://www2.avs.org/symposium2003/Papers/Paper_TF-WeP23.html) | 학회 초록 | 온도와 Wafer 간격을 바꿔 **표면 반응의 활성화 에너지와 기상 반응 속도 상수를 분리.** PH₃가 SiH₄ 반응에 미치는 영향이 상당히 크다 | A (요약) | §3 |
| S04 | “Low pressure polycrystalline Si silane CVD,” *J. Cryst. Growth* (1981). [DOI](https://doi.org/10.1016/0022-0248(81)90475-9) | 논문 | 625 °C·725 °C 영역과 기상 중합. **기존 HTML에서 승계. 이번 수집에서 재열람하지 않음** | B | 미사용 |

## 2. 미세 구조 · 집합 조직 · 응력

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S05 | “Stress and microstructure analysis of polycrystalline silicon films deposited by LPCVD,” MRS Proc. (Ford). [링크](https://resolve.cambridge.org/core/journals/mrs-online-proceedings-library-archive/article/stress-and-microstructure-analysis-of-polycrystalline-silicon-films-deposited-by-lpcvd/17BFE435850EFAFA7774D9B519AD798B) | 학회 논문 | **580 °C 부분 비정질(성장 속도 최저) → 600 °C 무작위 방위 등축 → 620 °C 주상·강한 우선 방위.** 응력은 **580 °C와 620 °C에서 압축, 600 °C 부근의 좁은 영역에서 인장** (03-13 자료수집 S03과 동일 문헌) | A (초록) | §2, §4 |
| S06 | “Effect of deposition temperature on the microstructure of LPCVD polysilicon films” 및 “Stress and microstructure in LPCVD polycrystalline silicon films: experimental results and closed form modeling of stresses,” MRS Proc. [링크](https://www.cambridge.org/core/journals/mrs-online-proceedings-library-archive/article/abs/stress-and-microstructure-in-lpcvd-polycrystalline-silicon-films-experimental-results-and-closed-form-modeling-of-stresses/71D5C210E4A6C638CEC57F93A117CA06) | 학회 논문 | 605–700 °C 막. **605 °C 부근 막은 인장**(비정질 → 결정 상변화에서 유래). 저온(약 605 °C)·고압(약 400 mTorr)에서는 **비정질로 증착된 뒤 증착 중에 결정화**해 등축 결정립과 인장 응력. **630 °C 초과에서는 SiO₂ 계면의 미세 결정립 전이층에서 주상 구조가 자란다** | A (초록) | §2, §4 |
| S07 | 응력 부호 변화 연구(검색 요약, *J. Mater. Sci.* 계열). [링크](https://link.springer.com/article/10.1023/A:1026333707011) | 논문 | 570–620 °C 사이에서 응력이 **압축 → 인장 → 압축**으로 변화. 580–587 °C는 등축 결정립이고 부피 응력이 지배해 인장. 제목–내용 대응은 검색 요약에 의존 | A (요약) | §4 |
| S08 | 집합 조직 서술(검색 요약의 특허·해설) | 특허·해설 | 표준 조건에서 **600–650 °C는 {110}, 650–700 °C는 {100}** 방위가 우세 | A (요약) | §2 |
| S09 | “Elastic properties and microstructure of LPCVD polysilicon films” / Young’s Modulus 연구. [PDF](https://sensors.myu-group.co.jp/sm_pdf/SM363.pdf) | 논문 | 620 °C, 100 mTorr 막: **증착 직후 항상 압축, 뚜렷한 (110) 집합 조직, 결정립 약 55 nm.** 잔류 응력은 막 두께, Anneal 온도, 이온 주입에 크게 좌우 | A (요약) | §2, §4 |

## 3. In-situ 도핑

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S10 | US 5,256,566, “Method for in-situ doping of deposited silicon.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5256566) | 특허 | **PH₃ 농도를 크게 올리면 증착 속도가 줄어** 공정이 길어진다. **PH₃/SiH₄ 비 0.001 미만**이면 도펀트 농도가 고용 한계 아래이고 면저항이 높다. 550–600 °C In-situ P 도핑 공정의 **활성화 에너지 1.5 eV.** 수직로에서 가스 유량·압력·PH₃/SiH₄ 비를 두께·비저항 균일도 기준으로 최적화. 예: **약 560 °C, PH₃/SiH₄ = 0.0008, 약 300 mTorr** | A (요약) | §3, §4 |
| S11 | Puchner 박사 논문(TU Wien). [웹](https://www.iue.tuwien.ac.at/phd/puchner/node32.html) | 학위 논문 | **PH₃와 AsH₃는 표면에 흡착해 SiH₄의 부착을 막아** 증착 속도를 낮춘다. **B₂H₆는 증착 속도를 크게 올린다**(반응을 촉진하는 라디칼 형성으로 설명) | A (요약) | §3 |
| S12 | Nalivaiko·Turtsevich, “The adsorptive-kinetic model of in-situ phosphorus doped film polysilicon deposition process.” [링크](https://tkea.com.ua/index.php/journal/article/view/627) | 논문 | SiH₄와 PH₃의 불균일 반응 상수와 탈착 상수를 정한 흡착–속도 모델 | A (요약) | §3 |
| S13 | UHasselt 논문(In-situ P-doped LPCVD). [기록](https://documentserver.uhasselt.be/handle/1942/36632) | 논문 | In-situ P 도핑에서의 증착 속도 저하는 알려진 문제. 온도와 Carrier(H₂)·PH₃ 유량 최적화로 저하를 제한해 **0.078 nm/s**(약 4.7 nm/min) | A (초록) | §4 |

## 4. 일반 지식 (기억 기반)

| ID | 내용 | 확인 | 본문 사용 |
|---|---|---|---|
| S14 | 결정립계가 도펀트를 붙잡고(편석) 전하를 Trap해 전위 장벽을 만든다. 저농도에서 비저항이 급격히 높고 어느 농도를 넘으면 급락한다 | C | §2, §5 |
| S15 | Poly-Si의 산화 속도는 결정 방위와 도핑에 의존. 결정립계를 따라 빠르다 | C | §6 |
| S16 | Batch Furnace에서 SiH₄가 Tube를 따라 소모되므로 온도 구배로 보상한다. 고농도 P 도핑에서는 Wafer 가장자리와 중앙의 차이가 커 Cage Boat 등을 쓴다 | C | §4, §7 |
| S17 | 게이트 Poly 공핍, 붕소 침투, Metal Gate로의 전환 | C | §1, §6 |

## 본문에 넣은 원문 그림 (2026-10-14 추가)

내려받아 눈으로 확인한 그림만 넣었다. 특허 도면은 Google Patents의 원본 크기 도면이고, 논문 그림은 PMC의 Open Access 판이다. 캡션의 수치는 표시가 없으면 그래프에서 읽은 값이다.

| ID | 그림 | 라이선스 | 본문 위치 |
|---|---|---|---|
| S10 | US 5,256,566 FIG. 15, 17 | 미국 특허 도면 | §2.1, §3.2 |

그림을 대조하며 확인한 것:

- S10의 “PH₃/SiH₄ 비 0.001 미만이면 면저항이 높다”는 문장은 특허 본문(Description)에서 찾지 못했다. 본문 §3.2에 미재확인으로 표시했다.
- FIG. 16 설명: 550 °C 증착 막은 사실상 비정질(이 공정의 전이 온도 약 550 °C), 560 °C 결정립 약 3,000 Å, 570 °C 약 2,000 Å, 600 °C 약 300 Å.
- FIG. 15의 T는 Tang(IEDM 1989)의 TBP 도핑, L은 Learn 등(*J. Appl. Phys.* 61, 1898 (1987))의 고농도 PH₃ 값이다.

## SEM·TEM 사진 추가 (2026-10-15)

사용자 요청으로 막질마다 실제 전자현미경 사진을 찾아 넣었다. PMC의 CC BY 논문과 미국 특허 도면만 썼고, 내려받아 눈으로 확인한 그림만 넣었다. 캡션의 공정 조건과 수치는 논문 본문이나 특허 본문에서 옮겼다.

| ID | 서지 | 라이선스 | 그림 | 본문 위치 |
|---|---|---|---|---|
| S18 | C. Shi, X. Liu, R. Chuai, “Piezoresistive Sensitivity, Linearity and Resistance Time Drift of Polysilicon Nanofilms with Different Deposition Temperatures,” *Sensors* 9(2), 1141 (2009). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3280852/) | CC BY 3.0 | Figure 1: 560–670 °C LPCVD Poly-Si 표면 SEM, 620 °C TEM. 결정립 30 → 70 nm | §2.1 |

## 5. 아직 비어 있는 자료

1. **응력–온도 곡선의 통일된 그림.** S05·S06·S07이 인장 구간을 각각 600 °C 부근, 605 °C 부근, 580–587 °C로 달리 준다. 압력과 장비를 맞춘 자료가 필요하다.
2. **도핑 농도–비저항 곡선**과 결정립 크기의 관계 수치.
3. **3D NAND의 Poly-Si**(채널, 소스 라인) 증착·도핑 조건의 공개 자료.
4. **DRAM Buried Channel·Storage Node Contact용 Poly Plug**의 Gap-fill과 접촉 저항 자료.
5. 승계 문헌(S04) 재확인.
