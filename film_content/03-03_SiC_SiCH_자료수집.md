# 03-03 · SiC / SiCH — 자료 수집

수집일: 2026-10-14 · 본문 원고: `03-03_SiC_SiCH_본문.md`

## 수집 방법과 한계

- 웹 검색으로 서지와 초록·요약을 확인했다. 논문 전문은 열람하지 못했다.
- Cu Cap/Etch Stop용 a-SiC:H의 **k, 누설 전류, 밀도를 같은 시편에서 비교한 수치표를 확보하지 못했다.** 본문의 k 범위는 [현장] 수준의 통용 값이다.
- 확인 수준: **A** 서지와 수치를 초록·요약으로 확인 / **B** 서지(제목·존재)만 확인 / **C** 기억에 의존, 재확인 필요

## 1. a-SiC:H · SiCH 막

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S01 | Shimizu 등, “Material design of plasma-enhanced chemical vapour deposition SiCH films for low-k cap layers in the further scaling of ultra-large-scale integrated devices-Cu interconnects,” *Sci. Technol. Adv. Mater.* 14, 055005 (2013). [DOI](https://doi.org/10.1088/1468-6996/14/5/055005) · [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5090375/) | 논문 (Open Access) | Cap 층은 **낮은 k와 Cu·수분 Barrier 성능이 Trade-off**. 양자화학 계산으로 **Si–C₂H₄–Si 네트워크**가 저공극·저k임을 예측. 전구체 4종 설계(Isobutyl trimethylsilane, Diisobutyl dimethylsilane, 1,1-Divinylsilacyclopentane, 5-Silaspiro[4,4]nonane). 양전자 소멸 분광으로 저공극 확인 | A (초록) | §2, §9 |
| S02 | 大陽日酸 技報 29호(위 논문 공동 소속의 기술 보고). [PDF](https://www.tn-sanso.co.jp/Portals/0/resources/jp/rd/giho/pdf/29/tnscgiho29_03.pdf) | 기술 보고 | Si–C₂H₄–Si 네트워크로 Cu 확산을 억제하면서 **k = 3.1** | A (2차) | §2, §9 |
| S03 | “A Study of Trimethylsilane (3MS) and Tetramethylsilane (4MS) Based α-SiCN:H/α-SiCO:H Diffusion Barrier Films,” *Materials* 5(3), 377 (2012). [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5448926/) · [MDPI](https://www.mdpi.com/1996-1944/5/3/377) | 논문 (Open Access) | 3MS·4MS + NH₃ PECVD 비교. SIMS 깊이 분석에서 **3MS 기반 막이 Cu Barrier 성능이 더 좋다.** FTIR에서 3MS 막의 Si–CH₃ 신호가 더 강하다. 4MS SiCN 위에 O-doped SiC Cap을 올린 이중층도 평가 | A (초록) | §3, §4 |
| S04 | 3MS 기반 a-SiC:H Barrier, IEEE IITC (2001). [기관 기록](https://ir.lib.nycu.edu.tw/handle/11536/19023) | 학회 논문 | N 첨가로 누설 전류가 줄지만 **N이 많으면 TDDB 수명이 나빠진다.** 중간 조성이 절충점. (요약에는 N 첨가로 k가 낮아졌다는 서술도 있으나 일반 경향과 달라 전문 확인 전에는 채택하지 않음) | A (요약) | §4 |
| S05 | CH₄/SiH₄ 기반 a-SiC:H 연구(대만, 2000). [기관 기록](https://ir.lib.nycu.edu.tw:443/handle/11536/66640) | 논문 | SiH₄ 유량 최소 조건에서 **k 3.6**. 비교 기준 SiN은 k 약 7.2. H₂·NH₃ Plasma 처리 모두 누설 감소. NH₃ 처리는 길어질수록 k 상승 | A (요약) | §2, §6 |
| S06 | SiCN Barrier 특허(검색 결과의 US 6,444,568 “Method of forming a copper diffusion barrier” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6444568) 등. **어느 특허의 수치인지 요약만으로 특정하지 못함**) | 특허 | SiCN 누설 90 nA/cm² @1 MV/cm 대 SiC 300 µA/cm² 주장. **단위 차이가 3자리 이상이라 신뢰도 낮음.** 메틸실란류 + NH₃로 SiCN 형성 | A (요약) | 미사용 (수치), §4 (경향만) |
| S07 | US 7,964,442, “Methods to obtain low k dielectric barrier with superior etch resistivity.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7964442) | 특허 | 3MS + C₂H₄ Barrier. C₂H₄/3MS 비가 오르면 밀도는 거의 그대로인데 식각 내성이 오른다 | A (요약) | §4 |
| S08 | US 7,867,917 · US 7,476,626, “Etch stop layer for a metallization layer with enhanced adhesion, etch selectivity and hermeticity.” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7867917) | 특허 | Etch Stop의 요구를 접착·식각 선택비·기밀성으로 정리 | B | §1 |
| S09 | Study of Cu diffusion in C-rich SiCN:H from trimethylphenylsilane, *Thin Solid Films* (2015). [기록](https://sinorg.niic.nsc.ru/public/article/1776/en) | 논문 | 다른 전구체의 C-rich SiCN:H도 Cu Barrier로 양호 | B | 미사용 |

## 2. 일반 지식 (기억 기반)

| ID | 내용 | 확인 | 본문 사용 |
|---|---|---|---|
| S10 | Cu Dual Damascene에서 Cu 상면은 금속 Barrier 없이 유전체 Cap과 직접 닿는다. Cu/Cap 계면이 Electromigration의 주 확산 경로이고, Cap 증착 전 NH₃·H₂ Plasma로 CuOₓ를 환원한다 | C | §1, §6 |
| S11 | N 함유 막(SiN, SiCN)과 NH₃ Plasma에서 나온 Amine이 Low-k를 통해 확산해 화학증폭형 Resist를 중화(Resist Poisoning). N-free SiC·SiCO 또는 이중층으로 대응 | C | §6 |
| S12 | 3MS: 끓는점 약 7 °C, 가연성. 4MS: 끓는점 약 27 °C. SiH₄와 달리 자연발화성이 아니다 | C | §3, §7 |
| S13 | FTIR 대역: Si–C 약 780–800, Si–CH₃ 약 1,250, Si–H 약 2,100, C–H 약 2,900 cm⁻¹ | C | §8 |

## 3. 기존 HTML(v0.9.1)에서 승계한 문헌

| 서지 | 비고 |
|---|---|
| S01과 동일 (PMC5090375) | 이번 수집에서 초록 재확인 |

## 본문에 넣은 원문 그림 (2026-10-14 추가)

내려받아 눈으로 확인한 그림만 넣었다. 특허 도면은 Google Patents의 원본 크기 도면이고, 논문 그림은 PMC의 Open Access 판이다. 캡션의 수치는 표시가 없으면 그래프에서 읽은 값이다.

| ID | 그림 | 라이선스 | 본문 위치 |
|---|---|---|---|
| S03 | Chen 등, *Materials* 5(3), 377 (2012), Figure 4. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5448926/) | CC BY 3.0 | §3.1 |

그림을 대조하며 확인한 것:

- S03을 PMC 전문 요약으로 대조했다. 350 °C 증착. 3MS 막은 Applied Materials Producer SE, 4MS 막은 Novellus Vector(둘 다 300 mm). k 4.81(3MS), 5.68(4MS).
- SIMS 전에 Anneal이나 Bias-Temperature Stress를 했다는 서술은 없다.

## SEM·TEM 사진 추가 (2026-10-15)

사용자 요청으로 막질마다 실제 전자현미경 사진을 찾아 넣었다. PMC의 CC BY 논문과 미국 특허 도면만 썼고, 내려받아 눈으로 확인한 그림만 넣었다. 캡션의 공정 조건과 수치는 논문 본문이나 특허 본문에서 옮겼다.

| ID | 서지 | 라이선스 | 그림 | 본문 위치 |
|---|---|---|---|---|
| S14 | O. Kapur, D. Guo, J. Reynolds 외, “An ultra high-endurance memristor using back-end-of-line amorphous SiC,” *Sci. Rep.* 14, 14008 (2024). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11189404/) | CC BY 4.0 | Figure 1(a)–(c): PECVD a-SiC/Si 적층의 단면 TEM, EDX. Memristor 시편 | §2.1 |

## 4. 아직 비어 있는 자료

1. **조성별 k·누설·밀도·Modulus 수치표.** SiC:H / SiCN:H / SiCO:H를 같은 장비에서 비교한 값. S03 전문에 있을 가능성이 높다.
2. **Barrier 성능의 정량 기준.** BTS 조건(온도·전계·시간)과 판정 기준.
3. **Cu/Cap 계면 접착 에너지**(4-point Bend)와 EM 수명의 상관 데이터.
4. **Cu Hillock**과 Cap 증착 온도·시간의 관계.
5. 장비사 제품(상용 Barrier Low-k 막)의 세대별 k 값. 공개 논문으로 확인되지 않았다.
