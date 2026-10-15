# 70개 Chapter의 그림 교체 목록

원래 HTML의 자체 제작 그림(상자를 화살표로 이은 "개념적 공정 경로" 등) 가운데 실제 자료로 바꿀 수 있는 것을 여기에 적는다. `apply_textbook.py`가 빌드할 때 `## CID keep:N` 아래의 내용으로 그 Chapter의 보존 블록 N을 바꾼다. 내용이 비어 있으면 그 그림을 뺀다.

그림 문법은 Part 03 원고와 같다: `![alt](figures/파일)` 다음 줄에 `*캡션*`, 그다음 줄에 `*출처: …*`. 그림 파일은 `film_content/figures/`에 있다(자르기는 `prep_figures.py`). 2026-10-15 추가.

## 01-01 keep:0

![평행 평판 PECVD Reactor 단면](figures/01-01_us4854263_fig1.png)

*실제 CVD Reactor에서 원료 공급, 활성화, 표면 성장, 배기가 일어나는 자리. 평행 평판 PECVD Reactor의 단면(모식도)이다. 공정 가스는 위쪽 가스 입구 Manifold(11)의 구멍으로 들어와 Susceptor(12) 위의 Wafer를 지나고, Wafer 둘레를 감싼 Baffle Plate(17)의 구멍을 거쳐 고리 모양 진공 Manifold(24)로 배기된다. 위아래의 Purge 흐름(19, 21)은 공정 가스와 따로 흐른다. Susceptor는 아래의 Lamp가 석영 창을 통해 가열하고, Plasma는 Manifold와 Susceptor 사이에서 만들어진다.*

*출처: US 4,854,263 (Applied Materials, 1989), FIG. 1. 미국 특허 도면. [Google Patents](https://patents.google.com/patent/US4854263A/en)*

## 02-03 keep:0

![열 CVD/PECVD 겸용 Reactor 단면](figures/02-03_us5000113_fig2.png)

*열 CVD/PECVD 겸용 Reactor의 단면. 공정 가스는 뚜껑의 Feed-through(36)로 들어와 가스 Manifold 공간(90)에 모이고, 그 안의 Baffle Plate(94)를 돌아 구멍 뚫린 Face Plate(92), 즉 Showerhead를 지나 Susceptor(16) 위의 Wafer(15)로 내려간다. Susceptor는 아래 석영 창(70) 너머의 Lamp(58)로 가열한다. 이 장에서 다루는 Manifold → Blocker(Baffle) Plate → Showerhead → Wafer의 경로가 실제 장비에서 어떻게 배치되는지 보여 준다.*

*출처: US 5,000,113 (Applied Materials, 1991), FIG. 2. 미국 특허 도면. [Google Patents](https://patents.google.com/patent/US5000113A/en)*

![Showerhead 구멍 하나의 단면, 원뿔형과 오목형](figures/02-03_us4854263_fig2-3.png)

*Showerhead(가스 입구 Manifold) 구멍 하나의 단면. FIG. 2는 원뿔형, FIG. 3은 오목한 곡면형 구멍이다. 가스는 위쪽의 좁은 구멍(지름 d₁)으로 들어와 아래로 넓어지는 구멍(출구 지름 d₂)을 지나 Wafer 쪽으로 나온다. 특허는 이런 모양이 구멍 안에서 가스 해리를 늘린다고 주장한다. 구멍의 모양 자체가 공정 변수가 될 수 있다는 예이다.*

*출처: US 4,854,263 (Applied Materials, 1989), FIG. 2, 3. 미국 특허 도면. [Google Patents](https://patents.google.com/patent/US4854263A/en)*

## 02-05 keep:1

![PECVD Reactor의 배기 경로](figures/01-01_us4854263_fig1.png)

*01-01에서 본 PECVD Reactor의 단면을 배기 쪽에서 다시 보자. Wafer를 지난 가스는 Wafer 둘레를 감싼 Baffle Plate(17)의 원형 구멍들을 지나 고리 모양 진공 Manifold(24)로 모이고, 거기서 Pump 쪽으로 빠진다. 구멍이 Wafer 둘레에 고르게 배열되어 있어야 가스가 한쪽으로 쏠리지 않고 반경 방향으로 고르게 빠진다. Throttle Valve, Foreline, Pump는 이 그림 밖, 진공 Manifold 아래쪽에 이어진다.*

*출처: US 4,854,263 (Applied Materials, 1989), FIG. 1. 미국 특허 도면. [Google Patents](https://patents.google.com/patent/US4854263A/en)*

## 09-02 keep:0

![BPO4 결정이 만드는 Contact 막힘과 배선 Bridge](figures/03-06_us5461011_fig1-2.png)

*BPSG Anneal 중 생긴 BPO₄ 결정이 만드는 두 가지 불량(종래 기술 설명도). 위(FIG. 1)는 단면으로, 결정(16)이 Contact 자리에 남아 개구를 막고 금속 배선 12와 14 사이에 걸쳐 있다. 아래(FIG. 2)는 위에서 본 모습으로, 결정이 이웃한 두 배선을 잇는다. 이 사례에서 다루는 형태 이상이 실제로 어떤 불량으로 이어지는지 보여 준다. 원인과 대책은 03-06 BPSG의 §6.1에서 다룬다.*

*출처: US 5,461,011 (United Microelectronics, 1995), FIG. 1, 2. 미국 특허 도면. [Google Patents](https://patents.google.com/patent/US5461011A/en)*

## 00-01 keep:0

![MOSFET, 소자 분리 절연막, 층간 절연막, 금속 배선, Passivation이 있는 소자 단면](figures/00-01_us6140206_fig9.png)

*공정을 마친 집적회로 소자의 단면도. 단결정 Si 기판(30) 위에 MOSFET의 Gate(50)와 Source·Drain(54)이 있고, 오른쪽의 얕은 홈에는 이웃한 소자를 전기적으로 떼어 놓는 CVD SiO₂(44)가 채워져 있다. 34는 기판 위의 얇은 SiO₂ 완충막이다. 그 위를 층간 절연막(58)이 덮고, 절연막에 뚫은 Contact 구멍으로 금속 배선(62)이 내려와 Source·Drain에 닿는다. 맨 위는 PECVD 질화막 Passivation(66)이다. 같은 절연막이라도 44는 소자와 소자를, 58은 배선과 소자를 떼어 놓고, 66은 칩을 바깥 환경으로부터 보호한다. 이 장에서는 막을 재료 이름보다 이런 역할로 먼저 읽는다.*

*출처: US 6,140,206 (Chartered Semiconductor Manufacturing, 2000), FIG. 9. 미국 특허 도면. [Google Patents](https://patents.google.com/patent/US6140206A/en)*

## 00-02 keep:0

![TTIP 분자의 구조식](figures/00-02_kim2022_fig1a.jpg)

*TiO₂ ALD·CVD 원료로 쓰는 TTIP(Titanium Tetraisopropoxide)의 구조식. 가운데 Ti 하나에 O 네 개가 붙고, 각 O 끝에 이소프로필기(–CH(CH₃)₂)가 하나씩 달려 있다. 이소프로필기 하나는 C 3개와 H 7개이므로 분자 전체는 Ti 1, O 4, C 12, H 28개, 화학식으로 Ti(OCH(CH₃)₂)₄ = C₁₂H₂₈O₄Ti이다. 막에 남기려는 원소는 Ti와 O이고, C 12개와 H 28개는 반응 중에 떨어져 나가야 한다. 몰질량은 약 284.2 g/mol이며 그 가운데 Ti는 47.9 g/mol, 약 17 %에 불과하다. 구조식은 어떤 원자가 어떤 원자와 이어져 있는지를 보여 줄 뿐 실제 결합 각도나 분자 모양을 그대로 그린 것은 아니다.*

*출처: Kim 등, Materials 15, 3021 (2022), Figure 1(a). CC BY 4.0. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9100524/)*

## 00-03 keep:0

![결정질 Si와 비정질 Si가 맞닿은 단면 TEM](figures/00-03_florian2021_fig6.jpg)

*같은 원소인 Si가 결정질과 비정질로 함께 있는 단면 TEM. 단결정 Si Wafer(c-Si) 표면에 30 fs 길이의 Laser Pulse를 한 번 쏘면 표면이 순간적으로 녹았다가 원자가 제자리를 찾기 전에 굳어, 표면에 비정질 Si(a-Si) 층이 생긴다. (a) 전체 모습. 위에서부터 시편 보호용 Pt, a-Si, c-Si이다. (b) Pt와 a-Si 사이에 두께 2.9 nm의 산화막이 보인다. (c) a-Si/c-Si 계면과 두 영역의 Fourier 변환(2D-FT, 삽입 그림). c-Si 쪽은 원자가 규칙적으로 반복되므로 뚜렷한 점들이 나타나고, a-Si 쪽은 장거리 질서가 없어 흐린 고리만 남는다. 두 구조 사이의 전이 영역은 약 3.9 nm이다. (d) 고배율 사진. 아래 c-Si에는 원자 열이 줄무늬처럼 이어지고, 위 a-Si에는 그런 줄무늬가 없다. 조성은 같아도 원자 배열의 규칙성이 다르면 다른 물질처럼 보인다.*

*출처: Florian 등, Materials 14, 1651 (2021), Figure 6. CC BY 4.0. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8037179/)*

## 00-04 keep:4

![CVD 장비의 Reactor와 배기·Scrubber 계통도](figures/00-04_us5653807_fig2-4.png)

*Wafer에 막이 되지 못한 원료가 가는 곳. SiGe 막을 기르는 저온 기상 Epitaxy(CVD) 장비의 Reactor 쪽(아래, FIG. 2)과 Pump·Scrubber Cabinet(위, FIG. 4)이다. 혼합 Manifold에서 배관(17)으로 들어온 원료 가스는 Reactor(19)를 지나고, Main Chamber(23)에서 Turbo Pump(25)가 뽑아낸 가스는 배관(27)을 따라 기계식 Pump(29)로 간다. 그 뒤 Oil Trap(35)과 Dry Scrubber(33)를 거쳐 배기 팬(37)으로 대기에 나간다. 막이 되지 않은 원료, 반응 부산물, Purge 가스가 모두 이 길로 빠져나가며, Trap과 Scrubber를 따로 두는 것은 상당한 양의 물질이 배기 쪽에 도달하기 때문이다. Reactor 벽에 쌓이는 막은 이 그림에 나타나지 않는다. 원소수지를 세울 때는 Wafer, 벽, 배기의 세 곳을 모두 세어야 한다.*

*출처: US 5,653,807 (미 공군, 1997), FIG. 2, 4. 미국 특허 도면. [Google Patents](https://patents.google.com/patent/US5653807A/en)*

## 00-06 keep:0

![Pedestal 안의 온도 센서로 Wafer 온도를 제어하는 방식](figures/00-06_us6247842_fig1.png)

*Wafer 온도를 Pedestal 온도로 대신 재는 일반적인 방식(종래 기술). Wafer(1)는 Pedestal(2) 위에 놓이고, 둘 사이에는 열 전달을 돕기 위해 He이나 Ar을 흘린다. 온도 센서(3, 예컨대 Thermocouple)는 Wafer가 아니라 Pedestal 안에 있고, 온도 제어기(4)는 이 센서 값을 보고 가열을 조절한다. 특허는 이렇게 하면 열 전달이 완전하지 않아 Wafer와 Pedestal의 온도 차가 10–50 °C에 이를 수 있다고 적는다. 고밀도 Plasma CVD(HDP CVD)에서는 반대로 Plasma가 Wafer 윗면을 데우므로 Wafer가 Pedestal보다 뜨겁고, 그 차이는 RF Power, 가스 유량, 압력에 따라 달라진다. 장비 화면의 온도는 센서가 있는 곳의 온도이다.*

*출처: US 6,247,842 (National Semiconductor, 2001), FIG. 1. 미국 특허 도면. [Google Patents](https://patents.google.com/patent/US6247842B1/en)*

## 00-07 keep:1

![Plasma Chamber에서 Throttle Valve와 Gate Valve를 거쳐 Pump로 가는 배기 경로](figures/00-07_us6598615_fig3.png)

*Plasma 반응 Chamber의 가스 경로. 공정 가스는 가스 배관(393)과 Nozzle(394)로 Chamber(390)에 들어와 Wafer 받침(392) 위를 지나 배기구(395)로 나간다. 배기구 아래 밸브 조립체(300)에는 Throttle Valve(320)와 Gate Valve(340)가 있다. 처음에는 Throttle Valve를 열고 저진공 배기구(350)로 Roughing Pump가 뽑는다. 낮은 진공에 이르면 Gate Valve를 열어 고진공 배기구(330) 너머의 Turbo 분자 Pump가 뽑는다. 공정 중의 Chamber 압력은 Throttle Valve를 조금씩 여닫아 맞춘다. 325와 345는 두 밸브의 구동기이다. 유입량은 MFC가, 통로의 전도도는 Throttle Valve가, 배기 능력은 Pump가 정하며 이 셋은 서로 다른 부품이다.*

*출처: US 6,598,615 (Applied Materials, 2003), FIG. 3. 미국 특허 도면. [Google Patents](https://patents.google.com/patent/US6598615B1/en)*

## 00-10 keep:0

![Gas Cabinet과 혼합 Manifold, 가스 공급원 계통도](figures/00-10_us5653807_fig1-3.png)

*SiGe 막을 기르는 저온 기상 Epitaxy(CVD) 장비의 가스 공급 쪽 계통도. 왼쪽 Gas Cabinet(2)에 SiH₄(8)와 H₂로 희석한 GeH₄(10), B₂H₆(12), PH₃(14) 실린더가 있고, 실린더마다 Purge Panel(3, 3a–3c)이 붙어 있다. 원료는 실린더 밸브(20), 감압기(22), MFC(26)를 지나 Vent 밸브(11)와 Run 밸브(13)로 나뉜다. Run 쪽은 배관(17)으로 Reactor에, Vent 쪽은 공통 Vent 배관(15)으로 배기 쪽에 간다. 오른쪽 가스 공급원(79, FIG. 3)은 Purge용 N₂, Venturi 구동용 N₂, 고순도 N₂·H₂, 밸브를 움직이는 압축 공기를 공급하고, PC(51)가 공압 Solenoid(49)로 밸브를 연다. 특허는 Purge Panel마다 Venturi Pump로 감압하는 종래의 Purge를 보통 20회쯤 되풀이해야 하는데 작업자가 이를 건너뛰기 쉽다고 지적하고, Turbo Pump로 훨씬 높은 진공을 만들어 Purge하는 구성을 제안한다.*

*출처: US 5,653,807 (미 공군, 1997), FIG. 1, 3. 미국 특허 도면. [Google Patents](https://patents.google.com/patent/US5653807A/en)*

![같은 장비의 Reactor와 Pump·Scrubber·누설 감지기 계통도](figures/00-04_us5653807_fig2-4.png)

*같은 장비의 Reactor와 배기 쪽. Reactor(19)와 Main Chamber(23)를 지난 가스는 Turbo Pump(25)와 기계식 Pump(29)를 거쳐 Oil Trap(35), Dry Scrubber(33)에서 처리된 뒤 배기 팬(37)으로 나간다. 질량분석기 방식의 누설 감지기가 Main Chamber(87)와 Vent 쪽(85)에 붙어 있어, 높은 진공이 조금이라도 무너지면 누설을 알아챈다. 공급, 반응, 배기의 구간마다 다른 보호 장치가 있고, 어느 하나가 다른 구간의 위험을 대신하지 않는다. 실제 장비의 안전 계통은 장비마다 다르므로 이 그림을 작업 절차로 쓰지 않는다.*

*출처: US 5,653,807 (미 공군, 1997), FIG. 2, 4. 미국 특허 도면. [Google Patents](https://patents.google.com/patent/US5653807A/en)*

## 01-09 keep:0

![C₂H₂ RF Plasma에서 생겨 벽에 쌓인 나노입자 덩어리의 SEM](figures/01-09_lisovskiy2022_fig3.jpg)

*기상에서 생긴 입자의 실제 모습. 13.56 MHz 용량결합 RF 방전으로 C₂H₂(처음 1 Torr) Plasma를 켠 뒤 유리관 벽에 쌓인 나노입자 덩어리의 SEM이다. (a) 벽에서 떼어 낸 조각의 단면, (b)(c) 그 일부의 확대로, 둥근 입자들이 뭉쳐 있다. (d) 500 nm가 넘는 입자들이 포도송이처럼 붙은 모습이다. (e)(f)는 관 바닥에서 모은 입자와 막 조각, (g)(h)는 전극에서 벗겨진 고분자 막이다. 논문은 관 벽에서 찾은 입자가 주로 지름 400–600 nm의 구형이라고 보고한다. 원료 기체가 Plasma 안에서 반응해 기상에서 입자를 만들고, 그 입자가 자라 벽과 바닥에 떨어진 것이다. 같은 실험에서 방전을 켜자 압력이 1 Torr에서 약 0.23 Torr로 떨어졌다(01-08 3절 그림). 원료가 막뿐 아니라 입자로도 빠르게 소모되었다는 뜻이다.*

*출처: Lisovskiy 등, ACS Omega 7, 47941 (2022), Figure 3. CC BY 4.0. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9798781/)*

## 06-01 keep:0

![Chamber 코팅에서 떨어져 Wafer에 붙은 Particle의 SEM과 EDX](figures/06-01_lin2017_fig8.jpg)

*Wafer 위 Particle의 원천을 추적한 실제 예. 양산용 CF₄/O₂ Plasma 식각 Chamber에서 처리한 300 mm Wafer(CVD TiN 막)에서 찾은 둥근 Particle의 (a) SEM 사진(눈금 50 nm)과 (b) EDX 스펙트럼이다. Particle에서는 Y, O, F와 약간의 C가 검출되었다. 이 Chamber의 안쪽 벽은 Y₂O₃ 용사 코팅이었고, 논문은 Plasma에 노출된 Y₂O₃ 표면이 수 nm 두께의 Yttrium Oxyfluoride로 바뀐 뒤 깎여 나와 Wafer에 떨어진 것으로 해석한다. 즉 Particle의 성분(Y)이 Wafer나 원료에는 없고 Chamber 부품에만 있는 원소였기 때문에 원천을 좁힐 수 있었다. 증착 Chamber에서도 같은 방식으로, Particle의 원소를 Chamber 부품·원료·이전 막의 성분과 비교해 원천 후보를 나눈다. 다만 성분이 일치한다는 것만으로 원인이 증명되지는 않는다(5절).*

*출처: Lin 등, Nanomaterials 7, 183 (2017), Figure 8. CC BY 4.0. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5535249/)*

## 07-01 keep:0

![Seasoning 조건별로 FSG 막에서 잰 Particle Adder 수](figures/07-01_us6846742_fig4.png)

*관찰에서 가설, 통제 실험, 결론으로 가는 실제 예. HDP-CVD에서 세정 뒤 FSG를 여러 장 연속으로 증착하면 Particle이 늘었다(관찰, 06-07 그림). 특허는 세정 뒤 벽에 입히는 Seasoning 막의 종류가 원인이라고 보고(가설), 같은 FSG 증착 조건에서 Seasoning만 바꾸어 세 번째 FSG 막의 Particle을 광학 표면 검사기로 쟀다(통제 실험). 조건 60과 62는 표준 SiO₂ Seasoning으로 54개와 49개, 조건 64는 Si Seasoning 30초로 3개, 66과 68은 Si와 SiO₂를 겹친 Seasoning으로 0개와 7개였다. 반복이 조건마다 한두 번뿐이므로 차이의 크기를 정밀하게 말할 수는 없지만, 차이가 열 배 이상이어서 Seasoning 막이 주요 원인이라는 결론을 지지한다. 남는 불확실성(예: 더 많은 장수에서도 유지되는가)은 다음 실험의 대상이 된다(06-07의 연속 증착 결과).*

*출처: US 6,846,742 (Applied Materials, 2005), FIG. 4. 미국 특허 도면. [Google Patents](https://patents.google.com/patent/US6846742B2/en)*

## 08-03 keep:0

![행성형 GaN-MOCVD Reactor의 CFD 결과: 속도, 유선, 온도](figures/08-03_li2018_fig3.jpg)

*실제 CVD Reactor를 CFD로 계산한 결과의 예. 6인치 Wafer 7장을 올린 행성형(Planetary) GaN-MOCVD Reactor를 Fluent로 계산했다(Susceptor 1,273 K, 압력 12.5 Torr, 입구 유속 0.2 m/s, NH₃ 몰분율 0.21). (a) Wafer 면 바로 위의 속도 크기 분포로, 여러 원판이 각자 다른 속도로 돌기 때문에 가운데는 느리고 바깥쪽 Wafer 가장자리는 빠르다. (b) 위에서 내려온 가스가 원판 위에서 바깥으로 퍼져 나가는 유선, (c) Reactor 단면의 온도 분포(K)로 뜨거운 Susceptor 위로 얇은 고온층이 생긴다. 이 장의 순서대로 형상과 경계조건(Susceptor 온도, 회전 속도, 입구 유속), 지배 방정식, 격자와 Solver(에너지 잔차 10⁻⁶, 나머지 10⁻⁴ 아래를 수렴 기준으로 삼음), 결과 해석을 거친 것이다. 이 그림은 계산 결과이다. 색이 매끄럽고 그럴듯해 보여도, 실측 압력·온도·두께와 비교해 검증하기 전에는 하나의 가설로 다루어야 한다(5절).*

*출처: Li 등, R. Soc. Open Sci. 5, 171757 (2018), Figure 3. CC BY 4.0. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5830772/)*
