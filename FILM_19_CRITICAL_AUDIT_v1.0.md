# CVD EDU — 19개 막질 핵심 현상 전수 감사 v1.0

## 판정과 범위

- **기존 89개 Chapter 유지:** 완료 (정적 및 브라우저 단위 확인).
- **Part 03 필수 개념 시각화 19개:** 교안에 직접 삽입하여 19개 모두 렌더링 확인.
- **조작형 모형:** ACL sp²/sp³/H 조성, BPSG 온도·시간에 따른 정규화 형상 완화 2개.
- **문헌에 근거한 실험 조건/수치 설명:** 현재 8개 Chapter에 새 근거 문단 삽입. 숫자가 없는 장을 연구 완료라고 처리하지 않음.
- **원논문 Figure 이미지 내장:** 0개. PDF 바이너리 네트워크 접근 실패. 자체 모식도는 논문 원본으로 표시하지 않음.
- **19개 Chapter 전문 교과서 심사:** 미완료. 기존 v0.9 교안 전체의 학술 감수/공정 적용 검증이 완료된 것은 아님.

## 19개 막질별 핵심 질문·Figure 감사

| Chapter | 막질 | 놓치면 안 되는 현상 | 이번 삽입 | 검증·자료 부족 |
|---|---|---|---|---|
| 03-01 | ACL | sp²–sp³–H 삼원상도 | 자체 SVG 시각화 | 삼원상도·Raman·Etch Selectivity·Stress |
| 03-02 | SiB | 막질 명칭과 원자비의 관계 | 자체 SVG 시각화 | Si:B 조성·결합상태·선택비 원논문 |
| 03-03 | SiC / SiCH | 수소·탄소 편입과 확산 장벽의 양면성 | 자체 SVG 시각화 | Si–C / Si–H / C–H·Density·Diffusion |
| 03-04 | SiBN / SiBCN | 원소 편입과 결합망의 상충관계 | 자체 SVG 시각화 | SiBN/SiBCN 분리·Bonding·Conformality |
| 03-05 | USG | 반응속도·유입·표면 성장의 경쟁 | 자체 SVG 시각화 | Gas-phase vs Surface Flux·Gap-fill |
| 03-06 | BPSG | B/P–점성–Reflow–형상의 연결 | 자체 SVG 시각화 | Reflow 프로파일·Glass Viscosity·온도·시간·B/P |
| 03-07 | PSG / BSG | 도핑 유리의 목적과 화학적 안정성 | 자체 SVG 시각화 | Gettering·도펀트 분포·수분 안정성 |
| 03-08 | SiON | O/N 조성과 광학 응답의 연결 | 자체 SVG 시각화 | O/N·RI dispersion·FTIR |
| 03-09 | FSG | 낮은 k와 F 안정성의 경쟁 | 자체 SVG 시각화 | F content·k·Moisture |
| 03-10 | SiOC / SiCOH | 기공과 전기·기계 성능의 균형 | 자체 SVG 시각화 | Porosity·k·Modulus·Plasma Damage |
| 03-11 | SiN | 결합·수소·광학 특성의 동시 해석 | 자체 SVG 시각화 | Si–N/Si–H/N–H·RI·Stress·Barrier |
| 03-12 | SiCN | 반응 분위기에 따른 C/N 편입과 유전율 | 자체 SVG 시각화 | He/NH₃ split·FTIR/XPS·k |
| 03-13 | a-Si | 수소 패시베이션과 결함 준위 | 자체 SVG 시각화 | Band-tail·Dangling Bonds·H |
| 03-14 | Poly-Si | 결정립계와 전기적 이동 | 자체 SVG 시각화 | Grain Growth·Sheet Resistance·Doping |
| 03-15 | SiGe & Epitaxy | 조성에 따른 격자 부정합과 Strain | 자체 SVG 시각화 | Ge%·Lattice Mismatch·Critical Thickness |
| 03-16 | W | 핵생성·연속 성장·Void 형성 | 자체 SVG 시각화 | WF₆ Reduction·Nucleation Delay·Seam/Void |
| 03-17 | TiN / WN / TaN | 확산 Barrier의 연속막 형성 | 자체 SVG 시각화 | Step Coverage·Diffusion·Resistance |
| 03-18 | Mo / Ru | 두께 축소 시 저항률과 재료 선택 | 자체 SVG 시각화 | Thickness Scaling·ρ·Grain Boundary |
| 03-19 | High-k | EOT와 실제 막 두께의 분리 | 자체 SVG 시각화 | k·EOT·Interfacial Layer·Leakage |

## 실험 근거로 추가한 대표 분석

### 03-01 ACL

Lee et al. (2011), 550°C 비교: C₆H₁₂ 기원 막의 DR 5,050 Å/min·밀도 1.48 g/cm³·Dry Etch Rate 1,770 Å/min, C₃H₆ 기원 막은 각각 6,360 Å/min·1.45 g/cm³·1,840 Å/min. 같은 온도의 특정 실험이며 조성량 정규화한 성장속도와 절대 DR은 구분한다.

원문: https://pure.korea.ac.kr/en/publications/comparative-study-on-the-properties-of-amorphous-carbon-layers-de/

### 03-05 USG

TEOS/O₃ LPCVD 실험(30–90 Torr)을 해석한 1994년 모델에서는 약 365°C 이상에서 기상 부반응에 따른 DR 감소 효과가 두드러졌고, 압력이 커질수록 DR 최댓값을 나타내는 온도가 낮아졌다. 표면 반응만의 Arrhenius 설명과 구별할 실제 증거다.

원문: https://doi.org/10.1016/0022-0248(94)90304-2

### 03-06 BPSG

Vasilev (2003)의 Fig. 1은 하나의 Reflow 이미지만이 아니라 (a,b) 단차 평탄화, (c,d) Contact Hole 가장자리 원형화, (e,f) Gap Filling을 열처리 전·후로 구분해 설명한다. 세 형상 지표를 동일한 개념으로 합치지 않는다.

원문: https://doi.org/10.1023/A:1023916502417

### 03-09 FSG

Passemard 등(1997)의 TEOS/O₂/C₂F₆ PECVD FSG 실험에서 F=3.5 at.% 조건은 k≈3.6을 보이며 수분 안정성을 확보했지만 4 at.% 초과에서는 수분 반응·F 방출·응력 변화와 k 증가가 관찰됐다. 85°C·85%RH·168h 처리 및 450°C 열처리 조건을 함께 비교해야 한다.

원문: https://doi.org/10.1016/S0167-9317(96)00062-7

### 03-11 SiN

SiNx 구조-물성 실험에서는 N/Si 0.2–1.5 범위를 분석하고 RBS·ERD·FTIR로 원자 수밀도·H·결합을 교차 검증했다. N/Si 증가와 RI 저하를 주로 밴드갭 증가와 연결했으며, FTIR Si–N 밴드의 해석 계수도 조성 의존성을 보였다.

원문: https://www.sciencedirect.com/science/article/pii/S0040609009000455

### 03-12 SiCN

Ermakova et al. (2022) BTMSPA PECVD 100–400°C에서 He 혼합의 k는 2.99–3.51, NH₃ 혼합의 k는 3.73–3.77 범위에서 온도 상승에 따라 최대 5.39까지 보고됐다. Fig. 2·3·9의 FTIR·XPS·k를 함께 읽는 교육 사례다.

원문: https://doi.org/10.3390/coatings12111767

### 03-15 SiGe & Epitaxy

Advanced CMOS 기술 리뷰는 SiGe Source/Drain의 Ge 함량이 90 nm 세대 약 19%에서 22 nm 세대 약 45%로 증가한 문헌 사례를 정리한다(Fig. 17). 이 수치는 특정 세대의 응력 증강용 S/D를 가리키며 모든 SiGe Epitaxy의 최적 조성이 아니다.

원문: https://pmc.ncbi.nlm.nih.gov/articles/PMC7466708/

### 03-19 High-k

High-k EOT Review의 Eq. (1)은 전체 EOT가 계면층(IL)과 High-k 층의 EOT 합이라는 직렬 정전용량 표현이다. HfO₂의 대표적 k≈20을 사용해도 IL 0.4 nm가 남으면 전체 EOT에서 그만큼의 기여를 삭제할 수 없다.

원문: https://pmc.ncbi.nlm.nih.gov/articles/PMC5448919/

## 누락이 반복되지 않도록 적용할 Chapter 승인 기준

1. 재료 선정 배경과 소자 내 위치가 그림/단면으로 확인되는가?
2. 조성과 결합 상태를 구분하고 이를 계측할 방법(FTIR/XPS/SIMS 등)이 설명되는가?
3. 공급-기상반응-표면반응-막질 특성에 걸친 원인사슬이 정량적 또는 반증 가능한 형태인가?
4. 파라미터별 역할, 변화 방향, 경쟁 효과, 비교 조건, 측정 지표가 명시됐는가?
5. 원논문의 **실제 Figure 이미지**가 표시되고 Figure 번호·축·단위·실험 조건을 판독할 수 있는가?
6. 종속/동시 변화 파라미터가 구분되고 이론 모형을 실험으로 가장하지 않았는가?
7. 앞의 요건이 미달하면 깊이 있는 교안으로 표시하지 않는가?

## 확보되지 않은 원논문 이미지 처리

기존 v0.9.1 Figure 목록의 18건 모두 미확보였고, 이번 작업에서도 네트워크 다운로드는 실패했다. 링크와 출처를 복구했으나 원본 비트맵을 내장하지 못했다. Figure는 **학습에 필요한 형식으로 자체 제작한 모식도**와 명확히 구분했으며 외부 URL 이미지가 깨진 상태를 그대로 방치하지 않았다.

## 브라우저 검증

- Chromium 1440×900 및 375×812에서 ACL ternary 변경 전/후 좌표 변화, BPSG Reflow 슬라이더 응답 확인.
- 19개 Chapter 순차 전환 후 각 Chapter별 고유 Figure 표시, console pageerror 없음.
- 모바일 375px 및 데스크톱 1280/1440px에서 document 가로 overflow 없음.
- 브라우저는 file:///·localhost 접근이 관리자 정책으로 차단돼 `page.set_content` 주입 방식으로 테스트함. 서버 배포·GitHub Pages 검증과는 별개.
- 기존 모든 수학/실습 구성의 완전 회귀 테스트는 수행하지 못함.

## 다음 원문 Figure 우선순위 (원본 확인 후)

| 우선 | Chapter | 찾을 실증 자료 |
|---:|---|---|
| 1 | ACL | Robertson 2002 Fig.2 삼원상도 + Lee 2011 실제 Raman/Etch/DR 비교 |
| 1 | BPSG | Vasilev 2003 Fig.1 Reflow 세 형태 + 1999 DR/B/P 조성 Fig.2~4 |
| 1 | SiN / SiCN | FTIR/RBS/ERD·XPS 실측 원도와 Recipe 조건 |
| 1 | W / High-k | Contact Hole/Barrier 단면과 EOT/Leakage 실측 결과 |
| 2 | SiCOH / FSG / SiGe | 기공율–Modulus, F 안정성, Strain/Ge 조성 실험 원도 |
| 2 | 나머지 11개 막질 | 각 재료가 선택된 이유를 보이는 실측 단면/전자적·광학적 측정 원도 확보 |

## 결론

이번 v1.0은 **이전까지 누락되었던 19개 핵심 개념의 시각화·본문 연결과 누락 감사**를 완료한 버전이다. 그러나 19개 막질 전체를 기존 BPSG 심층 보고서 수준으로 검증했다고 주장할 수 없다. 특히 원본 Figure 확보·정량적 DOE 문헌 검증·개별 장 집필 심화가 다음 품질 게이트다.