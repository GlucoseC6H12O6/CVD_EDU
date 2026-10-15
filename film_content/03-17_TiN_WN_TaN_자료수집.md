# 03-17 · TiN / WN / TaN — 자료 수집

수집일: 2026-10-14 · 본문 원고: `03-17_TiN_WN_TaN_본문.md`

## 수집 방법과 한계

- 웹 검색으로 서지와 초록·요약을 확인했다. 논문 전문은 열람하지 못했다.
- **ALD TaN의 비저항은 출처마다 수백 µΩ·cm에서 수만 µΩ·cm까지 다르다.** 상(Ta₃N₅인지 TaN인지), 조성, 두께, 하부막에 따라 달라진다. 본문에서 범위로 적고 한 값으로 정리하지 않았다.
- TiCl₄/NH₃ 공정의 **NH₄Cl 부산물**에 관한 자료는 이번 검색에서 찾지 못했다. 본문에서 통설로 표시했다.
- DRAM Capacitor 전극, Metal Gate 일함수 금속으로서의 TiN에 관한 공개 자료도 확보하지 못했다.
- 확인 수준: **A** 서지와 수치를 초록·요약으로 확인 / **B** 서지(제목·존재)만 확인 / **C** 기억에 의존, 재확인 필요

## 1. TiN — TiCl₄ / NH₃

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S01 | “Synthesis and characterization of low pressure chemically vapor deposited titanium nitride films using TiCl₄ and NH₃,” NJIT. [기록](https://researchwith.njit.edu/en/publications/synthesis-and-characterization-of-low-pressure-chemically-vapor-d/) | 논문 | LPCVD. **막의 염소가 450 °C에서 7.2 at%, 850 °C에서 0.15 at%로 감소.** 증착 온도를 낮추고 NH₃ 분압을 올릴수록 화학양론에 가까워진다. 최저 비저항 **86 µΩ·cm**(600 °C, NH₃/TiCl₄ 유량 비 10 : 1) | A (초록) | §2, §4 |
| S02 | US 6,767,582 “Method of modifying source chemicals in an ALD process” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6767582) 등 ALD 특허 | 특허 | ALD TiN, **400 °C: 염소 1.5 wt% 미만, 비저항 약 200 µΩ·cm.** **350 °C로 낮추면 염소 4.0 wt%, 비저항 450 µΩ·cm.** 다른 예: 400 °C에서 150 µΩ·cm, 성장 약 0.17 Å/cycle. 수치의 출처 특허는 요약만으로 확정하지 못함 | A (요약) | §2, §4, §5 |
| S03 | Pulsed CVD TiN 연구(TU Delft 저장소). [PDF](https://repository.tudelft.nl/file/File_9373fbbd-8fa2-4b91-ae37-94a72bfbf185?preview=1) | 논문 | 통상의 TiCl₄/NH₃ ALD는 **Cycle당 성장이 0.2 Å뿐**인 것이 큰 단점. CVD 단계 뒤에 자기 제한적 NH₃ Flush를 두는 Pulsed CVD를 350–500 °C에서 조사. **500 °C 아래에서는 막에 Cl이 더 많이 갇혀 비저항이 높다** | A (요약) | §3, §4 |
| S04 | “Comparison study for TiN films deposited from different method: chemical vapor deposition and atomic layer deposition,” MRS Proc. [링크](https://www.cambridge.org/core/journals/mrs-online-proceedings-library-archive/article/abs/comparison-study-for-tin-films-deposited-from-different-method-chemical-vapor-deposition-and-atomic-layer-deposition/DC919E3E803A3EFF47DC27C57EAD4EBF) | 학회 논문 | 600 °C CVD + NH₃ 후처리: **약 180 µΩ·cm, 종횡비 6(지름 0.35 µm Contact)에서 단차 피복 95 % 초과, 염소 2 at% 미만.** ALD는 CVD보다 100 °C 낮은 공정 온도에서 후처리 없이도 더 좋은 막질 | A (초록) | §3, §4 |
| S05 | EP 0 599 991 B1, “Process for forming low resistivity titanium nitride films” [Google Patents](https://patents.google.com/patent/EP0599991B1/en); 유량 변조 CVD 연구([CiNii](https://cir.nii.ac.jp/crid/1390001206253803520)) | 특허·논문 | TiCl₄ + NH₃ LPCVD TiN은 **염소가 많이 들어간다.** 증착 후 NH₃ 처리로 잔류 염소 제거(수소가 Cl과 반응해 HCl로 빠진다는 설명). 유량 변조 CVD: **380 °C에서 250 µΩ·cm, 염소 2 at%**, 균일한 단차 피복 | A (요약) | §3, §4 |

## 2. TiN — 금속 유기 전구체 (TDMAT · TDEAT)

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S06 | US 7,521,379 · US 7,838,441, “Deposition and densification process for titanium nitride barrier layers” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7521379); US 12,180,583 [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12180583) | 특허 | TDMAT·TDEAT 고압 MOCVD로 열증착한 막은 **Titanium Nitride Carbide.** 이후 **H₂/N₂ Plasma(약 750–1,250 W, 저주파 350 kHz 예)** 로 처리해 탄소를 줄이고 비저항을 낮춘다. 약 15 Å 층에 처리 약 10–20초. 처리로 N/Ti 비 약 1.04–1.28 | A (요약) | §3, §4 |
| S07 | CN 1426092 A (2차 요약). [Patsnap](https://eureka.patsnap.com/patent-CN1426092A) | 특허 | In-situ H₂/N₂ RF Plasma 처리가 **C·O·H 불순물을 줄이고, 비저항을 낮추고, 결정립을 고르게 키우고, 막을 치밀화.** 예: 1.5 Torr, 35초. 증착과 처리를 **반복**해 35 nm까지 | A (요약) | §3, §4 |
| S08 | Remote Plasma MOCVD TiN(TDEAT), POSTECH. [기록](https://oasis.postech.ac.kr/handle/2014.oak/29237) | 논문 | Plasma에 H₂를 넣은 막이 탄소 혼입이 적어 비저항이 낮다. H 라디칼이 TDEAT의 N과 반응해 탄소가 적은 Ti-rich 막을 만들고, N 라디칼은 탄화수소가 훨씬 많은 막을 만든다. **Plasma 40 W: 결정성 높고 거칠고 저저항 / 80 W: 결정성 낮고 매끄럽고 고저항** | A (초록) | §3 |
| S09 | TDMAT 기반 Ti(C,N) 연구, *J. Phys. IV*. [링크](https://jp4.journaldephysique.org/10.1051/jp4:1999876) | 논문 | 활성 수소가 금속–Ligand 결합을 공격해 Ligand를 떼어낸다. 탄화수소 혼입을 막는다 | A (요약) | §3 |

## 3. TaN

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S10 | US 7,928,006 “Structure for a semiconductor device and a method of manufacturing the same” [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7928006); US 7,485,349 [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7485349); US 7,186,446 [PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7186446) | 특허 | **기상 증착 Tantalum Nitride는 항상 비전도성 Ta₃N₅ 상으로 얻어진다.** NH₃의 환원력이 Ta⁵⁺를 Ta³⁺로 환원하기에 너무 약하다. **약한 Ar Plasma 120초로 절연막을 전도성 TaN으로 전환**(조성비 1.6 → 1.1. 요약은 Ta/N으로 적었으나 Ta₃N₅의 N/Ta = 1.67을 감안하면 N/Ta로 보인다). PDMAT 같은 금속 유기 전구체가 Halide보다 유리: 부피 큰 Ligand가 다공성 Low-k로의 침투를 줄인다. N-rich 막이 Cu Barrier 성능을 높인다 | A (요약) | §2, §3, §6 |
| S11 | Semiconductor Digest 기사. [웹](https://sst.semiconductor-digest.com/issue/?id=17044) | 기사 | ALD TaN은 **PDMAT Pulse와 NH₃ 반응을 번갈아** 진행. Barrier 두께 목표 **45 nm 노드 5 nm, 32 nm 노드 3.5 nm** | A (요약) | §1, §3 |
| S12 | ECS Meeting Abstract 224, E2-1883. [PDF](https://ecs.confex.com/ecs/224/webprogram/Abstract/Paper24388/E2-1883.pdf) | 학회 초록 | Blanket ALD TaN 비저항 **약 5,000 µΩ·cm, PVD TaN 약 240 µΩ·cm.** 그럼에도 **3 nm ALD TaN Barrier의 Via 저항이 PVD보다 약 28 % 낮았다.** Blanket 비저항만으로는 Via 저항이 설명되지 않고 핵생성과 계면 청정도가 중요 | A (요약) | §2, §5, §6 |
| S13 | ALD-TaN Via 저항 보고(검색 요약, ECS 226 등). [초록](https://ecs.confex.com/ecs/226/webprogram/Paper42137.html) | 학회 초록 | ALD-TaN의 높은 비저항(**약 50 mΩ·cm**)이 Barrier 박막화를 제한. **두께 1 → 2 nm에서 Via 저항이 급증.** **N/Ta 비가 하부막에 의존: SiO₂ 위 약 4/5, Ta 위 약 1/2.** Ta 위의 Ta-rich 막은 약 2 mΩ·cm | A (요약) | §2, §5, §6 |
| S14 | imec, TaCl₅ 기반 Ta₃N₅ 연구(검색 요약, ECS E2-1881 등). [PDF](https://ecs.confex.com/ecs/224/webprogram/Abstract/Paper24070/E2-1881.pdf) | 학회 초록 | TaCl₅ 기반 Ta₃N₅의 비저항은 증착 온도가 오르면 내려간다. **약 10 nm 아래에서는 너무 저항이 커 측정 불가**, 그 위에서는 컨덕턴스가 두께에 선형 | A (요약) | §2 |
| S15 | PEALD TaN 학위 논문(KAIST). [기록](https://koasas.kaist.ac.kr/handle/10203/51621) | 학위 논문 | ALD-TaN은 얇은 두께에서 PVD-TaN보다 Cu Barrier 성능이 대체로 낮다. 밀도가 낮고 불순물이 많기 때문 | A (요약) | §2, §6 |

## 4. WN · WNₓCᵧ

| ID | 서지 | 유형 | 핵심 내용 · 수치 | 확인 | 본문 사용 |
|---|---|---|---|---|---|
| S16 | “Characterization of atomic layer deposited WNₓCᵧ thin film as a diffusion barrier for copper metallization,” MRS Proc. [링크](https://resolve.cambridge.org/core/journals/mrs-online-proceedings-library-archive/article/abs/characterization-of-atomic-layer-depositedwnxcy-thin-film-as-a-diffusion-barrier-for-coppermetallization/479FECCC84E9D2E63C6A7D485AE2DB31); UNIST 기록 [1](https://scholarworks.unist.ac.kr/handle/201301/64178) · [2](https://scholarworks.unist.ac.kr/handle/201301/64179); Semiconductor Digest [기사](https://sst.semiconductor-digest.com/issue/?id=17366) | 논문·기사 | **WF₆ + NH₃ + Triethylboron(TEB), 275–325 °C** ALD. TEB가 환원제. 증착 직후 **비저항 약 350 µΩ·cm, 밀도 15.37 g/cm³.** 조성 **W 48, C 32, N 20 at%.** O·F·B 각 0.5 at% 미만, H 4 at% 미만. **면심 입방(β-WC₁₋ₓ·β-W₂N과 비슷한 격자), 등축 미세 구조**(비정질이 아니다). 낮은 비저항은 Tungsten Carbide 성분 덕. Cu/Si 사이 **12 nm 막이 700 °C 30분에서 파괴. Sputter Ta는 650 °C, ALD TiN은 600 °C에서 파괴.** **종횡비 40 : 1 Trench에서 단차 피복 90 % 초과.** 600 °C까지 안정, 대기 보관 1년간 비저항 변화 없음. 30 Å 미만 초박막이 PVD-Ta 계보다 우수 | A (초록) | §2, §3, §9 |
| S17 | “Atomic-layer-deposited WNₓCᵧ thin films as diffusion barrier for copper metallization.” [ResearchGate](https://www.researchgate.net/publication/224426956_Atomic-layer-deposited_WNxCy_thin_films_as_diffusion_barrier_for_copper_metallization) | 논문 | **기존 HTML에서 승계.** S16과 같은 계열 연구로 보인다. 이번 수집에서 재열람하지 않음 | B | 미사용 |

## 5. 일반 지식 (기억 기반)

| ID | 내용 | 확인 | 본문 사용 |
|---|---|---|---|
| S18 | 6 TiCl₄ + 8 NH₃ → 6 TiN + 24 HCl + N₂. HCl + NH₃ → NH₄Cl(약 340 °C 아래 고체). 저온에서 TiCl₄·NH₃ 부가물 생성 | C | §3, §7 |
| S19 | TiN은 대기 중에서 표면이 산화되고 결정립계로 산소가 들어간다. O₃ 기반 High-k ALD에서 TiN 전극 표면이 산화돼 계면층이 생긴다 | C | §6 |
| S20 | Cu 배선 Barrier는 TaN/Ta 이중층: TaN이 유전체 접착과 Barrier, Ta가 Cu 접착(Wetting) | C | §1 |
| S21 | TiN의 일함수는 약 4.5–4.9 eV 범위에서 두께·조성·열 이력에 따라 변한다 | C | §1 |
| S22 | 도체 막의 수직 저항 R = ρ t / A | C | §5 |

## 6. 아직 비어 있는 자료

1. **NH₄Cl과 부가물**의 생성 조건, 배기계 영향에 관한 문헌.
2. **ALD TaN 비저항의 통일된 그림.** 상·조성·두께·하부막을 맞춘 자료. S12–S14가 240 µΩ·cm에서 50 mΩ·cm까지 걸쳐 있다.
3. **DRAM Capacitor TiN 전극**(고종횡비 ALD, 산화 계면층, 염소 영향)의 공개 자료.
4. **Metal Gate 일함수 금속**으로서의 TiN·TaN·TiAl 계 ALD 자료.
5. **TDMAT 막의 대기 노출 후 산소 흡수와 비저항 Drift** 자료(이번 검색에서 찾지 못함).
6. 승계 문헌(S17) 재확인.

## 본문에 넣은 원문 그림 (2026-10-15 추가)

Google Patents의 원본 크기 도면을 잘라 넣었다. 본문 첫머리에 있던 자체 제작 개념도는 빌드에서 뺐다. 캡션의 수치는 도면에 적힌 값이거나 특허 본문의 값이다.

| ID | 그림 | 라이선스 | 본문 위치 |
|---|---|---|---|
| S06 | US 12,180,583 FIG. 2 (TiCl₄ + N₂H₄ ALD TiN의 조성과 비저항) | 미국 특허 도면 | §2.2 |
| S10 | US 7,186,446 FIG. 3 (PE-ALD TaN의 N/Ta 비와 비저항) | 미국 특허 도면 | §2.3 |

## SEM·TEM 사진 추가 (2026-10-15)

사용자 요청으로 막질마다 실제 전자현미경 사진을 찾아 넣었다. PMC의 CC BY 논문과 미국 특허 도면만 썼고, 내려받아 눈으로 확인한 그림만 넣었다. 캡션의 공정 조건과 수치는 논문 본문이나 특허 본문에서 옮겼다.

| ID | 서지 | 라이선스 | 그림 | 본문 위치 |
|---|---|---|---|---|
| S23 | Cui 외, *Micromachines* 11(1), 32 (2020) (03-16 S23과 같은 논문). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7019522/) | CC BY 4.0 | Figure 2: Contact 입구·바닥의 IMP Ti/CVD TiN 단면 TEM. 바닥 피복 Ti 57 %, TiN 80 % | §6.2 |
| S24 | A. M. Kia, N. Haufe, S. Esmaeili 외, “ToF-SIMS 3D Analysis of Thin Films Deposited in High Aspect Ratio Structures via Atomic Layer Deposition and Chemical Vapor Deposition,” *Nanomaterials* 9(7), 1035 (2019). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6669757/) | CC BY 4.0 | Figure 5(b): TSV 측벽 아래쪽의 ALD TaN/Co 단면 TEM | §6.2 |
