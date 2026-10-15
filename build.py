from pathlib import Path
from html import escape as E
from bs4 import BeautifulSoup
import re,csv,json,math,zipfile,hashlib
ROOT=Path('/mnt/data/CVD_EDU_Critical_Figures_v1')
SRC=Path('/mnt/data/CVD_EDU_Film_Application_v0.9/CVD_EDU_v0.9.html')
raw=SRC.read_text(encoding='utf-8')

DATA=[
('03-01','ACL','sp²–sp³–H 삼원상도','sp²/sp³/H 성분 비율을 탄소계 재료의 구조 지도에 놓아 보고, PECVD a-C:H와 수소가 적은 ta-C를 구별한다. 삼원상도의 영역 경계는 결정론적 조성 경계가 아니며 이 그림의 영역 배치는 교육용이다.','Raman D/G는 sp² 클러스터의 크기와 질서에도 민감하다. 절대 sp³ 원자비와 H 함량은 단일 Raman 지표만으로 확정하지 않고 NEXAFS, ERDA 등 보완 계측을 결합한다.','https://doi.org/10.1016/S0927-796X(02)00005-0','Robertson (2002) Fig. 2; 원본 재현이 아닌 구조 개념도','ternary','삼원상도·Raman·Etch Selectivity·Stress'),
('03-02','SiB','막질 명칭과 원자비의 관계','B-doped Si, 비화학양론 Si–B 공증착막, 결정성 Silicon Boride는 원자비와 결합망이 다르다. 같은 SiB 표기만으로 증착 메커니즘이나 식각 선택비를 일반화하면 안 된다.','교육에서는 반드시 XPS/RBS/SIMS 원자비, B 결합상태, 결정화 유무를 먼저 측정하고 선택비·응력과 연결한다. 현재 확보한 근거는 특허 중심이므로 실제 정량 사례는 추가 확보 대상이다.','https://patents.google.com/patent/US20240339316A1/en','US20240339316A1 (특허); 데이터 미검증','sib','Si:B 조성·결합상태·선택비 원논문'),
('03-03','SiC / SiCH','수소·탄소 편입과 확산 장벽의 양면성','Si–C 골격만 생각하면 C–H, Si–H 및 기공이 생기는 실제 PECVD 막질을 설명할 수 없다. 같은 Si/C 비율에서도 전구체 분해와 네트워크 연결도 차이로 배리어 특성이 달라진다.','FTIR의 Si–C/Si–H/C–H 결합 신호와 XRR 밀도, 확산시험을 같이 보아야 한다. 한 막질의 낮은 k를 다른 막질의 동일 확산 차단 성능으로 곧바로 연결해서는 안 된다.','https://pmc.ncbi.nlm.nih.gov/articles/PMC5090375/','PECVD SiCH precursor-structure study; original figures require capture','network','Si–C / Si–H / C–H·Density·Diffusion'),
('03-04','SiBN / SiBCN','원소 편입과 결합망의 상충관계','Si–N 기반 네트워크에 B나 C를 넣으면 모든 물성이 같은 방향으로 바뀌지는 않는다. 산소·수소 잔류와 형성 결합이 유전율, 응력, 화학적 안정성을 좌우한다.','SiBN과 SiBCN을 각각 독립적인 실험계로 취급하고 FTIR/XPS 조성 자료를 확보한 뒤 모델과 비교한다. Borazine PECVD 결과를 다른 Laser CVD SiBCN의 근거로 합쳐서 사용하지 않는다.','https://research.ibm.com/publications/use-of-sibn-and-sibon-films-prepared-by-plasma-enhanced-chemical-vapor-deposition-from-borazine-as-interconnection-dielectrics','IBM SiBN/SiBON PECVD; SiBCN 별도 문헌 필요','quaternary','SiBN/SiBCN 분리·Bonding·Conformality'),
('03-05','USG','반응속도·유입·표면 성장의 경쟁','TEOS/O₃ 산화막은 공급량과 표면 반응만으로 성장률을 설명할 수 없다. 기상 반응은 성장종 소모·입자 생성·분포 변화에도 영향을 준다.','DR/T/P/가스 비율을 바꿀 때 온도 의존성뿐 아니라 경계층과 가스 공급·배기 위치를 함께 살펴야 한다. Gap-fill 형상은 평균 DR만으로 판단할 수 없다.','https://doi.org/10.1016/0022-0248(94)90304-2','TEOS/O₃ kinetic study; publication conditions cross-check','growth','Gas-phase vs Surface Flux·Gap-fill'),
('03-06','BPSG','B/P–점성–Reflow–형상의 연결','B와 P는 SiO₂ 유리 결합망과 점성·연화 거동을 바꾼다. 열처리 시 표면장력이 단차 형상을 완화하지만, 온도·시간·초기 형상·막 두께가 함께 작용한다.','왼쪽은 초기 단차, 오른쪽은 온도/시간을 변경했을 때의 교육용 표면 완화 모형이다. 실제 Reflow 성능의 Flow Angle/Gap-fill은 원논문의 실험값으로 비교해야 한다. B/P 함량과 수분·결정화 안정성도 별도 검증이 필요하다.','https://doi.org/10.1023/A:1023916502417','Vasilev (2003) Fig. 1 (단차 평탄화·Contact Rounding·Gap-fill)','reflow','Reflow 프로파일·Glass Viscosity·온도·시간·B/P'),
('03-07','PSG / BSG','도핑 유리의 목적과 화학적 안정성','P와 B는 각각 유리의 결합망과 물성에 영향을 미치지만 동일한 역할을 수행하는 것은 아니다. 역사적 사용 위치와 Gettering/흐름 특성을 화학적 안정성·후속 열처리 조건과 연결한다.','동일한 산화물 wt%라는 숫자만으로 P와 B의 작용을 비교하지 않는다. 도펀트 분포와 수분·열처리 이력을 구분해 측정한다.','https://doi.org/10.1016/0169-4332(93)90620-Q','B/ P-containing oxide annealing study; abstract','dopedglass','Gettering·도펀트 분포·수분 안정성'),
('03-08','SiON','O/N 조성과 광학 응답의 연결','SiON의 굴절률과 광학 밴드 구조는 O/N 비율뿐 아니라 수소와 밀도에도 영향을 받는다. SiO₂와 SiN 사이를 단순 직선 보간한 값이 모든 실제 PECVD 막에 적용되는 것은 아니다.','RI 측정 파장과 FTIR/XPS 기반 O/N/Si 조성비를 함께 기록한다. 광학막·패시베이션·절연 용도에서 목표 지표가 서로 다르다는 것도 구분한다.','https://doi.org/10.3390/coatings11111288','Optical SiON study; Fig. verification required','optical','O/N·RI dispersion·FTIR'),
('03-09','FSG','낮은 k와 F 안정성의 경쟁','Si–F 결합과 F 편입은 유리의 분극 특성을 바꾸고 낮은 유전율에 기여할 수 있다. 그러나 결합 상태·흡습/열처리 안정성 문제가 공정 통합 한계를 만든다.','F 함량 증가에 따른 k만 보지 말고 수분 노출 후 결합·FTIR·전기적 신뢰성 변화까지 함께 비교해야 한다. 그래프는 상충관계의 방향을 설명하는 모식도이며 실험 데이터는 아니다.','https://doi.org/10.1016/S0167-9317(96)00062-7','FSG fluorine/stability experimental publication','tradeoff','F content·k·Moisture'),
('03-10','SiOC / SiCOH','기공과 전기·기계 성능의 균형','낮은 분극률과 기공은 Low-k 달성에 유리하지만 동시에 탄성계수와 기계적 안정성을 떨어뜨릴 수 있다. 기공율과 네트워크 연결은 서로 독립적이지 않다.','유전율·Young’s Modulus·Porosity를 동시에 측정하고 Cure 및 플라즈마 손상 전후를 비교한다. 서로 다른 조성의 실험 점을 동일 곡선으로 합치지 않는다.','https://pmc.ncbi.nlm.nih.gov/articles/PMC8125368/','Open-access low-k pore and modulus research; original Figure extraction outstanding','porosity','Porosity·k·Modulus·Plasma Damage'),
('03-11','SiN','결합·수소·광학 특성의 동시 해석','SiNx:H의 굴절률은 Si/N만이 아니라 H, 밀도, 광학 측정 파장 및 전자구조에도 영향을 받는다. Si–N/Si–H/N–H 결합을 FTIR로 비교하고 조성은 RBS/ERD 등으로 확인한다.','모식 FTIR의 위치는 대표적인 진동대역을 설명하기 위한 것이며 논문 실측 Spectrum이 아니다. 응력·Barrier를 RI 하나로 대신 평가하면 원인을 놓칠 수 있다.','https://www.sciencedirect.com/science/article/pii/S0040609009000455','SiNx bond composition vs RI study; FTIR bands','ftir','Si–N/Si–H/N–H·RI·Stress·Barrier'),
('03-12','SiCN','반응 분위기에 따른 C/N 편입과 유전율','BTMSPA 단일 전구체에 He 또는 NH₃를 공급한 실제 PECVD 실험에서 FTIR·XPS와 유전율이 함께 달라졌다. 이는 반응 가스가 단순 희석제가 아니라 결합 형성 경로에 관여함을 보여준다.','Ermakova et al. (2022) Fig. 2·3·9에서 FTIR·XPS·k를 비교한다. BTMSPA/NH₃의 높은 k 결과를 다른 SiCN 전구체·장비에 그대로 대입하지 않는다.','https://doi.org/10.3390/coatings12111767','Ermakova (2022) Figs. 2, 3, 9','sicn','He/NH₃ split·FTIR/XPS·k'),
('03-13','a-Si','수소 패시베이션과 결함 준위','비정질 Si는 장거리 주기성이 없어서 결합각 변형과 Dangling Bond가 국소 상태를 만든다. H는 Dangling Bond의 일부를 패시베이션하며 전기·광학 특성을 바꾼다.','전도·가전자대의 Urbach Tail과 중간갭 결함 상태를 분리해 보고, FTIR와 광흡수/PDS·전기 측정을 연결한다.','https://doi.org/10.1103/PhysRevB.36.3479','a-Si:H metastable defect research','dos','Band-tail·Dangling Bonds·H'),
('03-14','Poly-Si','결정립계와 전기적 이동','Poly-Si는 결정립 내부와 Grain Boundary가 전류 전달에 서로 다른 역할을 한다. 결정립 크기와 도핑 활성화가 Sheet Resistance와 이동도에 영향을 준다.','열처리·Deposition Temp에 따른 Grain 성장과 도핑 프로파일을 함께 보고 Hall/SIMS/XRD/TEM으로 원인을 구분한다.','https://doi.org/10.1016/0038-1101(79)90005-4','LPCVD poly-Si electrical property study','grains','Grain Growth·Sheet Resistance·Doping'),
('03-15','SiGe & Epitaxy','조성에 따른 격자 부정합과 Strain','Si와 Ge는 격자상수가 달라 Ge 함량이 증가하면 완전 정합 성장 시 Strain 구동력이 커진다. 두께가 임계값을 넘어서면 Misfit Dislocation 가능성이 증가한다.','SiGe 격자상수는 Vegard 법칙으로 1차 근사할 수 있지만 Critical Thickness는 성장 조건과 합금 조성·결함 핵생성에 따라 달라진다.','https://pmc.ncbi.nlm.nih.gov/articles/PMC7466708/','SEG SiGe composition and scaling Figure 17','sige','Ge%·Lattice Mismatch·Critical Thickness'),
('03-16','W','핵생성·연속 성장·Void 형성','WF₆ 반응에서 초기 표면이 무엇으로 덮여 있는지가 Nucleation Delay와 선택성에 영향을 준다. Via/Contact에서는 측벽과 입구 성장률 차이가 Seam/Void를 결정한다.','이 모식도는 Via Filling의 대표 Failure Mechanism을 보여준다. 실제 공정에서는 Nucleation Layer, 반응 가스 및 구조가 달라지므로 SEM 단면으로 확인한다.','https://www.sciencedirect.com/science/article/pii/0040609089908080','Selective LPCVD W kinetics and fill study','tungsten','WF₆ Reduction·Nucleation Delay·Seam/Void'),
('03-17','TiN / WN / TaN','확산 Barrier의 연속막 형성','Barrier 성능은 명목상 재료 종류뿐 아니라 실제 유효 두께, 조성, 결함, Conformality에 달려 있다. 고종횡비 구조에서는 Sidewall/Bottom Coverage가 중요하다.','같은 평균 두께여도 구조 하부의 막이 끊기면 Barrier가 약해질 수 있다. ALD와 CVD를 동일 속도·조건으로 비교하지 않고 증착 방식별 장단점을 설명한다.','https://doi.org/10.1149/1.1837114','TiN thermal CVD study (DOI bibliographic check pending)','barrier','Step Coverage·Diffusion·Resistance'),
('03-18','Mo / Ru','두께 축소 시 저항률과 재료 선택','배선 두께가 줄면 표면·입계 산란이 커져 벌크 저항률보다 박막 저항률이 높아진다. 따라서 벌크 ρ가 낮다는 사실만으로 나노배선의 우열을 정할 수 없다.','Fuchs–Sondheimer/Mayadas–Shatzkes 등 산란 모델의 역할을 소개하고, Ru/Mo 고유 장벽·핵생성·거칠기 효과를 분리해 검증한다.','https://doi.org/10.1039/C4RA04701J','Ru CVD precursor review; Mo experimental reference pending','resistivity','Thickness Scaling·ρ·Grain Boundary'),
('03-19','High-k','EOT와 실제 막 두께의 분리','높은 유전율을 이용하면 같은 정전용량에서 SiO₂보다 물리적으로 두꺼운 절연막을 사용할 수 있다. 그러나 계면 SiO₂와 전극 구조의 직렬 정전용량도 전체 EOT에 기여한다.','High-k 5 nm, k=20이면 해당 층만의 EOT는 0.975 nm다. 여기에 예를 들어 IL이 0.4 nm 존재한다면 전체 EOT는 1.375 nm가 된다(단순 직렬 모델).','https://pmc.ncbi.nlm.nih.gov/articles/PMC5448919/','High-k interfacial-layer EOT scaling review, Eq.(1)','eot','k·EOT·Interfacial Layer·Leakage'),
]

EVIDENCE={
 '03-01':('Lee et al. (2011), 550°C 비교: C₆H₁₂ 기원 막의 DR 5,050 Å/min·밀도 1.48 g/cm³·Dry Etch Rate 1,770 Å/min, C₃H₆ 기원 막은 각각 6,360 Å/min·1.45 g/cm³·1,840 Å/min. 같은 온도의 특정 실험이며 조성량 정규화한 성장속도와 절대 DR은 구분한다.','https://pure.korea.ac.kr/en/publications/comparative-study-on-the-properties-of-amorphous-carbon-layers-de/'),
 '03-05':('TEOS/O₃ LPCVD 실험(30–90 Torr)을 해석한 1994년 모델에서는 약 365°C 이상에서 기상 부반응에 따른 DR 감소 효과가 두드러졌고, 압력이 커질수록 DR 최댓값을 나타내는 온도가 낮아졌다. 표면 반응만의 Arrhenius 설명과 구별할 실제 증거다.','https://doi.org/10.1016/0022-0248(94)90304-2'),
 '03-06':('Vasilev (2003)의 Fig. 1은 하나의 Reflow 이미지만이 아니라 (a,b) 단차 평탄화, (c,d) Contact Hole 가장자리 원형화, (e,f) Gap Filling을 열처리 전·후로 구분해 설명한다. 세 형상 지표를 동일한 개념으로 합치지 않는다.','https://doi.org/10.1023/A:1023916502417'),
 '03-09':('Passemard 등(1997)의 TEOS/O₂/C₂F₆ PECVD FSG 실험에서 F=3.5 at.% 조건은 k≈3.6을 보이며 수분 안정성을 확보했지만 4 at.% 초과에서는 수분 반응·F 방출·응력 변화와 k 증가가 관찰됐다. 85°C·85%RH·168h 처리 및 450°C 열처리 조건을 함께 비교해야 한다.','https://doi.org/10.1016/S0167-9317(96)00062-7'),
 '03-11':('SiNx 구조-물성 실험에서는 N/Si 0.2–1.5 범위를 분석하고 RBS·ERD·FTIR로 원자 수밀도·H·결합을 교차 검증했다. N/Si 증가와 RI 저하를 주로 밴드갭 증가와 연결했으며, FTIR Si–N 밴드의 해석 계수도 조성 의존성을 보였다.','https://www.sciencedirect.com/science/article/pii/S0040609009000455'),
 '03-12':('Ermakova et al. (2022) BTMSPA PECVD 100–400°C에서 He 혼합의 k는 2.99–3.51, NH₃ 혼합의 k는 3.73–3.77 범위에서 온도 상승에 따라 최대 5.39까지 보고됐다. Fig. 2·3·9의 FTIR·XPS·k를 함께 읽는 교육 사례다.','https://doi.org/10.3390/coatings12111767'),
 '03-15':('Advanced CMOS 기술 리뷰는 SiGe Source/Drain의 Ge 함량이 90 nm 세대 약 19%에서 22 nm 세대 약 45%로 증가한 문헌 사례를 정리한다(Fig. 17). 이 수치는 특정 세대의 응력 증강용 S/D를 가리키며 모든 SiGe Epitaxy의 최적 조성이 아니다.','https://pmc.ncbi.nlm.nih.gov/articles/PMC7466708/'),
 '03-19':('High-k EOT Review의 Eq. (1)은 전체 EOT가 계면층(IL)과 High-k 층의 EOT 합이라는 직렬 정전용량 표현이다. HfO₂의 대표적 k≈20을 사용해도 IL 0.4 nm가 남으면 전체 EOT에서 그만큼의 기여를 삭제할 수 없다.','https://pmc.ncbi.nlm.nih.gov/articles/PMC5448919/'),
}

# Helper functions for self-contained SVGs. All data-valued profiles are explicitly conceptual unless grounded in stated equations.
def T(x,y,s,size=14,anchor='middle',color='#2d475c',weight='normal'):
 return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{color}" font-weight="{weight}">{E(s)}</text>'
def svg(body,height=250):
 return f'<svg class="critical-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 {height}" role="img" aria-label="자료 이해를 위한 교육용 도표">{body}</svg>'
def box(x,y,w,h,label,color='#e4f0f2',stroke='#a1bdc4'):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{color}" stroke="{stroke}"/>'+T(x+w/2,y+h/2+6,label,16)
def arrow(x1,y1,x2,y2,col='#65869e'):
 return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{col}" stroke-width="2.5" fill="none"/><path d="M{x2-9} {y2-5} L{x2} {y2} L{x2-9} {y2+5}" stroke="{col}" stroke-width="2" fill="none"/>'
def axes(yname,xname, left=83,top=38,bottom=205,right=755):
 return f'<path d="M{left} {top} V{bottom} H{right}" stroke="#667e91" stroke-width="2" fill="none"/>'+T(35,40,yname,12,anchor='start')+T((right+left)/2,bottom+32,xname,13)
def polyline(pts,color='#267995',width=4,dash=''):
 return f'<polyline points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-dasharray="{dash}"/>'
def grid():return '<path d="M83 80 H755 M83 120 H755 M83 160 H755" stroke="#eaf0f5" stroke-width="1"/>'
def nodes(points,edges,colors):
 z='';
 for i,j in edges:
  z+=f'<path d="M{points[i][0]} {points[i][1]} L{points[j][0]} {points[j][1]}" stroke="#8aa7b9" stroke-width="4"/>'
 for i,(x,y) in enumerate(points):
  fill=colors[i%len(colors)];z+=f'<circle cx="{x}" cy="{y}" r="13" fill="{fill}" stroke="white" stroke-width="2"/>'
 return z

# science-specific teaching visuals
def make_visual(kind):
 if kind=='ternary':
  A=(78,214); B=(377,214); C=(78,23)
  d=f'<path d="M{A[0]} {A[1]} L{B[0]} {B[1]} L{C[0]} {C[1]} Z" fill="#e9f3f8" stroke="#6b879b" stroke-width="2"/>'
  d+='<path d="M80 214 L80 55 L150 172 L215 214 Z" fill="#bcd8e1" opacity=".6"/>'
  d+='<path d="M270 214 L375 214 L270 135 Z" fill="#e6cabb" opacity=".7"/>'
  d+='<circle id="acl-dot" cx="164" cy="137" r="9" fill="#d06143" stroke="white" stroke-width="3"/>'
  d+=T(72,12,'sp³',14,'middle')+T(68,241,'sp²',14)+T(388,241,'H',14)
  d+=T(184,58,'ta-C',13,color='#38647b')+T(181,156,'a-C:H',14,color='#375970')+T(313,199,'분자/고분자 영역',12,color='#8b4e37')
  d+=T(455,38,'조성을 움직여 구조 지도를 읽기',16,'start',weight='bold')
  d+=box(454,61,314,67,'H 원자분율 / C 중 sp³ 분율','#f1f6f9')
  d+=T(466,154,'삼각형의 점은 세 성분의 합이 100%인 위치.',14,'start')
  d+=T(466,179,'경계는 실제 실험상 고정 임계값이 아님.',13,'start',color='#64798b')
  return svg(d,256)
 if kind=='reflow':
  d=T(200,25,'증착 직후: 단차 형상',17,weight='bold')+T(590,25,'열처리 후: 점성 유동',17,weight='bold')
  for dx in [0,390]:
   d+=f'<path d="M{dx+45} 205 V180 H{dx+150} V139 H{dx+245} V180 H{dx+345} V205 Z" fill="#c6d2dc" stroke="#8aa0b3" stroke-width="2"/>'
  d+='<path d="M45 148 L116 148 L145 85 L247 85 L278 148 L345 148 L345 180 L245 180 L245 139 L150 139 L150 180 L45 180 Z" fill="#bfdfd2" fill-opacity=".85" stroke="#2e8b76" stroke-width="2"/>'
  d+='<path id="reflow-top" d="M435 148 L497 145 Q521 90 543 102 L638 102 Q670 102 694 145 L735 148" fill="none" stroke="#2e8b76" stroke-width="4"/>'
  d+='<path d="M435 180 L435 148 L735 148 L735 180 H635 V139 H540 V180 Z" fill="#bfdfd2" opacity=".44"/>'
  d+=T(412,244,'온도와 시간은 형상 변화를 촉진하지만 실제 속도는 η(T, B, P)에 의존',13)
  return svg(d,260)
 if kind=='sib':
  d=box(25,56,240,90,'B-doped Si')+box(287,56,240,90,'Si–B 혼합막','#edf1fb')+box(548,56,240,90,'Silicon boride','#f9f0e5')
  d+=T(145,181,'Si 결정망 + 치환 B',13)+T(407,181,'비화학양론 Si:B',13)+T(668,181,'독립 화합물 상',13)
  d+=T(400,226,'식각률·응력·전기특성은 원자비와 결합상태 확인 후 해석',15)
  return svg(d)
 if kind=='network':
  pts=[(83+i*85,65+j*71+8*math.sin(i*2+j)) for j in range(3) for i in range(5)]
  edges=[(j*5+i,j*5+i+1) for j in range(3) for i in range(4)]+[(j*5+i,(j+1)*5+i) for j in range(2) for i in range(5)]
  d=nodes(pts,edges,['#5d83a6','#5d83a6','#cb9d64','#5d83a6','#8fbaad'])
  d+=T(613,68,'Si–C backbone',17)+T(611,107,'Si–H / C–H',17)+T(609,146,'잔류 H·기공',17)+T(610,204,'확산 경로의 병목',15)
  return svg(d)
 if kind=='quaternary':
  d=''
  pts=[(120,80),(212,80),(304,80),(166,150),(258,150),(350,150),(212,214),(304,214)]
  ed=[(0,1),(1,2),(0,3),(1,3),(1,4),(2,5),(3,4),(4,5),(3,6),(4,6),(4,7),(5,7)]
  d+=nodes(pts,ed,['#417fa3','#64a699','#d8ad6e','#8365a9'])
  d+=T(510,75,'Si  ·  N  ·  B  ·  C',20,weight='bold')+T(518,113,'각 결합의 비율은 공정마다 다름',14)
  d+=T(520,156,'FTIR / XPS / RBS',16)+T(520,186,'→ Bonding / Composition',14)
  return svg(d)
 if kind=='growth':
  d=box(55,55,185,63,'공급 Flux, J_g')+box(322,55,185,63,'표면반응, k_s','#d8e9d7')+box(585,55,185,63,'성장, J_f','#f5eedc')
  d+=arrow(245,87,317,87)+arrow(511,87,579,87)
  d+=T(405,175,'1/J_f ≈ 1/J_g + 1/J_s',22)+T(403,213,'개념적 저항 직렬식: 상세 기구에 따라 달라짐',13)
  return svg(d)
 if kind=='dopedglass':
  d=box(28,74,220,90,'SiO₂ Glass')+arrow(252,116,321,116)+box(328,74,207,90,'+ P 또는 B','#e4ead9')+arrow(540,116,610,116)+box(617,74,176,90,'특성 변화','#f5ebdd')
  d+=T(410,204,'흐름·도펀트·흡습: 서로 다른 반응과 측정 필요',15)
  return svg(d)
 if kind=='optical':
  d=axes('RI','O/N 조성 변화 →')+grid()
  d+=polyline([(83,85),(225,102),(370,121),(515,145),(665,164),(755,178)],'#397fa6')
  d+=T(144,65,'N-rich 특성',14)+T(684,146,'O-rich 특성',14)+T(435,64,'개념적 경향 · 실측값 아님',13,color='#667a88')
  return svg(d)
 if kind=='tradeoff':
  d=axes('정규화된 특성','F 편입량 →')+grid()
  d+=polyline([(83,68),(210,87),(352,111),(490,135),(630,153),(755,171)],'#2c8f9d')
  d+=polyline([(83,188),(215,178),(347,164),(477,139),(623,99),(755,60)],'#b6714c')
  d+=T(630,183,'k(낮을수록 유리)',14,color='#267f8f')+T(637,57,'안정성 위험',14,color='#af6445')
  return svg(d)
 if kind=='porosity':
  d=axes('정규화 물성','기공률 →')+grid()
  d+=polyline([(83,58),(209,92),(355,130),(513,161),(650,181),(755,195)],'#b46f4b')
  d+=polyline([(83,70),(210,90),(361,116),(508,138),(650,155),(755,164)],'#387eaa')
  d+=T(636,132,'k',16,color='#387eaa')+T(650,200,'Modulus',16,color='#a65d41')
  d+=T(401,40,'두 경향은 실험 대상과 네트워크에 따라 달라짐',13)
  return svg(d)
 if kind=='ftir':
  d=axes('상대 신호','파수 (cm⁻¹) →')+grid()
  def g(x,m,s,a):return a*math.exp(-.5*((x-m)/s)**2)
  pts=[]
  for i in range(135):
   wn=400+(3600-400)*i/134
   zz=g(wn,850,150,117)+g(wn,2150,135,67)+g(wn,3350,165,84)
   pts.append((83+(755-83)*i/134,192-zz))
  d+=polyline(pts,'#417f9c',3)
  for wn,lab in [(850,'Si–N'),(2150,'Si–H'),(3350,'N–H')]:
   xx=83+(wn-400)/3200*(755-83);d+=T(round(xx),61,lab,13)
  d+=T(601,24,'정성 모식도 · 실측 Spectrum 아님',12)
  return svg(d)
 if kind=='sicn':
  d=box(24,47,232,70,'BTMSPA + He')+box(24,139,232,70,'BTMSPA + NH₃','#e4eede')
  d+=arrow(268,83,341,83)+arrow(268,174,341,174)
  d+=box(346,47,200,70,'C-rich 경향','#f1ecf8')+box(346,139,200,70,'N 편입 증가','#dceaf1')
  d+=arrow(551,83,625,83)+arrow(551,174,625,174)
  d+=T(712,80,'k ~3.0–3.5',16)+T(712,168,'k ~3.7–5.4',16)
  d+=T(416,236,'Ermakova 2022의 BTMSPA 특정 조건 · 일반 SiCN 기준값 아님',12)
  return svg(d)
 if kind=='dos':
  d=axes('DOS','에너지 →')+grid()
  d+=polyline([(90,75),(174,82),(257,115),(339,181),(430,192),(515,179),(611,114),(705,69),(755,60)],'#387ba4')
  d+='<path d="M83 192 H755" stroke="#7f9aab" stroke-dasharray="3 4"/>'
  d+=T(397,143,'Dangling Bond',14,color='#ac6b4b')
  d+='<circle cx="405" cy="176" r="10" fill="#c38867"/>'
  d+=T(187,48,'가전자대 Tail',14)+T(660,48,'전도대 Tail',14)
  return svg(d)
 if kind=='grains':
  d=''
  for j in range(2):
   for i in range(4):
    x=38+i*148+(j%2)*30;y=40+j*93
    d+=f'<path d="M{x} {y+8} L{x+120} {y+2} L{x+135} {y+60} L{x+104} {y+78} L{x+9} {y+84} Z" fill="{["#c9deeb","#dce9d3","#eee0cd","#d9d9ed"][i]}" stroke="#758b9f" stroke-width="2"/>'
  d+=T(687,86,'Grain',18)+T(694,126,'Boundary',18)+T(668,186,'전도 장벽/산란',13)
  d+=T(380,246,'도핑 활성도와 결정립 크기를 분리해 Rs 및 이동도 평가',13)
  return svg(d,260)
 if kind=='sige':
  d=axes('부정합 %','Ge 몰분율 x →')+grid()
  pts=[(83+(755-83)*x/100,196-125*( (5.431+0.227*x/100-5.431)/5.431)/(.227/5.431)) for x in range(0,101,4)]
  d+=polyline(pts,'#377f9c',4)
  for p in [0,20,40,60,80,100]:
   xx=83+(755-83)*p/100;d+=T(int(xx),222,str(p),11)
  d+=T(450,32,'Vegard 선형 근사: Si 5.431 Å, Ge 5.658 Å',12)
  d+=T(592,91,'x=0.2 → +0.84%',15,color='#2a718e')
  return svg(d)
 if kind=='tungsten':
  d=''
  for j,(lab,top) in enumerate([('시작: 열린 Via',0),('정상 Conformal',1),('입구 과성장/Seam',2)]):
   x=32+j*258
   d+=T(x+115,31,lab,16)
   d+=f'<path d="M{x+25} 65 H{x+100} V192 H{x+160} V65 H{x+229}" stroke="#97abb9" fill="none" stroke-width="12"/>'
   if top>0:
    d+=f'<path d="M{x+25} 65 H{x+100} V192 H{x+160} V65 H{x+229}" stroke="#418ea0" fill="none" stroke-width="{9 if top==1 else 18}"/>'
   if top==2:
    d+=f'<path d="M{x+100} 64 Q{x+131} 87 {x+160} 64" fill="none" stroke="#418ea0" stroke-width="16"/>'
    d+=f'<ellipse cx="{x+131}" cy="160" rx="12" ry="24" fill="#fff" stroke="#b76a51" stroke-dasharray="4 3"/>'
  d+=T(407,240,'Void/Seam 여부는 단면 SEM과 초기 핵생성 이력으로 확인',13)
  return svg(d,255)
 if kind=='barrier':
  d=''
  for i,(lab,w) in enumerate([('유효 Barrier 연속막',12),('비연속 Sidewall',3)]):
   x=70+i*378;d+=T(x+125,35,lab,17)
   d+=f'<path d="M{x} 66 H{x+77} V205 H{x+177} V66 H{x+254}" fill="none" stroke="#99abb8" stroke-width="13"/>'
   d+=f'<path d="M{x} 66 H{x+77} V205 H{x+177} V66 H{x+254}" fill="none" stroke="#43929a" stroke-width="{w}"/>'
   if i==1:
    d+=f'<path d="M{x+77} 115 V172" stroke="white" stroke-width="10"/>'
  d+=T(410,242,'Bottom·Sidewall Coverage를 별도 정량화: X-TEM / EDX',13)
  return svg(d,255)
 if kind=='resistivity':
  d=axes('ρ/ρbulk','막 두께 →')+grid()
  d+=polyline([(83,53),(120,77),(182,118),(262,148),(360,172),(480,184),(624,191),(755,193)],'#397c9c')
  d+=T(190,46,'표면·입계 산란 강화',14)+T(631,177,'bulk 극한',14)
  d+=T(424,27,'방향성 모식도, Mo/Ru 실측 곡선 아님',12)
  return svg(d)
 if kind=='eot':
  d=box(50,68,180,70,'SiO₂  3.9')+box(322,68,180,70,'High-k  20','#d7ecdf')+box(588,68,180,70,'IL','#f4e9d9')
  d+=T(140,178,'동일 C에서',16)+arrow(238,103,313,103)+T(412,178,'t=5 nm',16)+arrow(508,103,580,103)+T(681,178,'t=0.4 nm',16)
  d+=T(411,225,'EOT = 5×(3.9/20) + 0.4 = 1.375 nm',20)
  return svg(d,245)
 raise Exception(kind)

# Simple visual stylesheet and dynamic controls are inserted into existing single-file reader.
css='''
<style id="critical-figures-style">
.paper .critical-figure{margin:32px 0 42px;background:#fff;border:1px solid #dce5ed;border-radius:14px;padding:19px 20px 17px;max-width:100%;overflow:hidden}
.paper .critical-figure figcaption{font-size:16px;line-height:1.5;color:#173c55;font-weight:700;margin:0 0 10px}
.paper .critical-figure .critical-svg{width:100%;height:auto;display:block;background:#f9fbfc;border-radius:8px;max-width:100%}
.paper .critical-figure .crit-sub{font-size:13px;color:#6b7e8d;margin:7px 0 11px}
.paper .critical-figure .crit-insight{font-size:14px;color:#344b5c;line-height:1.8;margin:14px 0 7px}
.paper .critical-figure .crit-source{font-size:12px;color:#637a8e;line-height:1.65;margin:7px 0 0}
.paper .critical-figure .crit-source a{color:#2d6990;text-decoration:underline}
.paper .crit-controls{display:flex;flex-wrap:wrap;gap:16px;margin:12px 0 4px}
.paper .crit-controls label{font-size:12px;font-weight:600;display:flex;flex-direction:column;gap:8px;flex:1;min-width:145px}
.paper .crit-controls input[type=range]{width:100%;accent-color:#2c799d}
.paper .crit-result{font-size:14px;line-height:1.7;color:#2e617b;padding:10px 11px;background:#eef6f8;border-radius:7px;margin:10px 0}
@media(max-width:520px){.paper .critical-figure{padding:13px 10px;margin:21px 0}.paper .crit-controls label{min-width:115px}}
</style>
'''
raw=raw.replace('</head>',css+'</head>',1)

def module_html(i,entry):
 cid,title,cap,desc,insight,url,ref,kind,missing=entry
 drawing=make_visual(kind)
 controls=''
 if kind=='ternary':
  controls='''<div class="crit-controls"><label>H 원자분율 <output id="acl-h-txt">30%</output><input id="acl-h" type="range" min="0" max="65" step="1" value="30"></label><label>탄소 중 sp³ 분율 <output id="acl-sp-txt">60%</output><input id="acl-sp" type="range" min="0" max="100" step="1" value="60"></label></div><div id="acl-result" class="crit-result" aria-live="polite">원자분율: sp² 28.0%, sp³ 42.0%, H 30%</div>'''
 if kind=='reflow':
  controls='''<div class="crit-controls"><label>Anneal 온도 <output id="rf-temp-txt">800°C</output><input id="rf-temp" type="range" min="650" max="950" value="800" step="10"></label><label>Anneal 시간 <output id="rf-time-txt">30 min</output><input id="rf-time" type="range" min="0" max="120" value="30" step="5"></label></div><div id="rf-result" class="crit-result" aria-live="polite">정규화된 표면 형상 완화 모형. 실험 Reflow 예측값이 아닙니다.</div>'''
 return (f'<figure class="critical-figure" id="critical-{cid}">'
  f'<figcaption>{E(title)} — {E(cap)}</figcaption>'
  f'<p class="crit-sub">개념 이해용 자체 제작 Figure · 원본 논문 Figure와 구분</p>'
  +drawing+controls
  +f'<p class="crit-insight">{E(desc)}</p><p class="crit-insight">{E(insight)}</p>'
  +(f'<p class="crit-insight"><strong>문헌 실험 근거:</strong> {E(EVIDENCE[cid][0])} <a href="{E(EVIDENCE[cid][1])}" target="_blank" rel="noopener noreferrer">원문</a></p>' if cid in EVIDENCE else '')
  +f'<p class="crit-source">문헌 연결: <a href="{E(url)}" target="_blank" rel="noopener noreferrer">{E(ref)}</a> · 원본 그림 미내장</p></figure>')

for e in DATA:
 cid=e[0]
 # place directly before parameter effects so visual and narrative bridge structure to recipe
 pat=r'(<template\s+id="tpl-'+re.escape(cid)+r'">)(.*?)(</template>)'
 m=re.search(pat,raw,re.S)
 if not m:raise RuntimeError('Missing template '+cid)
 inner=m.group(2)
 # insert after properties block and before recipe parameter header
 p=r'(<h2 id="'+re.escape(cid)+r'-parameters")'
 if re.search(p,inner):
  inner=re.sub(p,lambda match: module_html(cid,e)+match.group(0),inner,count=1)
 else:
  inner=module_html(cid,e)+inner
 raw=raw[:m.start()]+m.group(1)+inner+m.group(3)+raw[m.end():]

# broken remote image removed, with functional link to the paper (never an empty area)
raw=re.sub(r'<img\b[^>]*\bsrc=["\']https?://[^>]*>',lambda m:'<p class="crit-source">원본 Figure 이미지: 외부 서버 접근 제한으로 미내장 · 위 문헌 링크로 열람</p>',raw)
js=r'''
<script id="critical-figure-interactions">
(function(){
 function updateACL(){
 const H=document.getElementById('acl-h'),Sp=document.getElementById('acl-sp'),dot=document.getElementById('acl-dot');if(!H||!Sp||!dot)return;
 const h=Number(H.value)/100, q=Number(Sp.value)/100,sp3=(1-h)*q,sp2=(1-h)*(1-q);
 // Triangular barycentric coordinates: sp2(78,214), H(377,214), sp3(78,23)
 dot.setAttribute('cx',(78*sp2+377*h+78*sp3).toFixed(2));dot.setAttribute('cy',(214*sp2+214*h+23*sp3).toFixed(2));
 document.getElementById('acl-h-txt').textContent=H.value+'%';document.getElementById('acl-sp-txt').textContent=Sp.value+'%';
 document.getElementById('acl-result').textContent='전체 원자분율 sp² '+(100*sp2).toFixed(1)+'% · sp³ '+(100*sp3).toFixed(1)+'% · H '+H.value+'%  /  영역은 정성적 구조 지도';
 }
 function updateReflow(){
 const t=document.getElementById('rf-temp'),a=document.getElementById('rf-time'),path=document.getElementById('reflow-top');if(!t||!a||!path)return;
 const kelvin=Number(t.value)+273.15,ref=1073.15;const R=8.314,Q=160000;const etaRatio=Math.exp(Q/R*(1/kelvin-1/ref));const tau=40*etaRatio;
 // normalized sinusoidal surface relaxation; arbitrary tau_ref for demonstration only
 const relax=Math.exp(-Number(a.value)/tau);const pts=[];
 for(let i=0;i<=80;i++){
  const x=435+300*i/80;
  const ramp=Math.exp(-Math.pow((i-40)/22,4));
  const y=148-62*ramp*relax;
  pts.push((i===0?'M':'L')+x.toFixed(1)+' '+y.toFixed(1));
 }
 path.setAttribute('d',pts.join(' '));
 document.getElementById('rf-temp-txt').textContent=t.value+'°C';document.getElementById('rf-time-txt').textContent=a.value+' min';
 document.getElementById('rf-result').textContent='표면 단차 진폭 잔류율 '+(100*relax).toFixed(1)+'% (가상 모델, η 기준 800°C, Q=160 kJ/mol·τ=40분은 교육용 가정; 실측/Recipe 예측 아님)';
 }
 function update(){updateACL();updateReflow()}
 document.addEventListener('input',e=>{if(['acl-h','acl-sp','rf-temp','rf-time'].includes(e.target?.id))update()});
 const obs=new MutationObserver(()=>{if(document.getElementById('acl-dot')||document.getElementById('reflow-top'))update()});
 const pane=document.querySelector('#content')||document.querySelector('#paper')||document.querySelector('#reader')||document.querySelector('main'); if(pane)obs.observe(pane,{childList:true,subtree:false});
 setTimeout(update,300);
})();
</script>
'''
raw=raw.replace('</body>',js+'</body>',1)
out=ROOT/'CVD_EDU_v1.0_Critical_Concepts.html';out.write_text(raw,encoding='utf8')

# Objective audit: counts are static markup (per-template), NOT proof of physical validity.
soup=BeautifulSoup(raw,'html.parser');audit=[]
for cid,title,cap,desc,insight,url,ref,kind,missing in DATA:
 tpl=soup.select_one('template#tpl-'+cid)
 assert tpl, cid
 orig_size=len(tpl.get_text(' ',strip=True))
 has=tpl.select_one('figure#critical-'+cid) is not None
 row=dict(chapter=cid,film=title,key_concept=cap,missing_before=missing,paper_url=url,figure_locator=ref,
  added_local_concept_figure='yes' if has else 'no',paper_original_embedded='no',
  evidence_status='patent_only_need_primary_experiment' if cid=='03-02' else ('primary_fig_number_checked' if cid in ('03-01','03-06','03-12','03-15','03-19') else 'publisher_abstract_or_fulltext_locator'),
  scientific_review='pending_qualified_review',browser_test='pending',chapter_words_approx=orig_size,
  target_next='원문 PDF·정확한 Figure·실험 조건 추출 후 본문 실증 그래프 대체; 추가 원문 검토')
 audit.append(row)
with (ROOT/'film_19_critical_audit.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=list(audit[0]));w.writeheader();w.writerows(audit)
(ROOT/'figure_manifest.json').write_text(json.dumps([{'chapter':i,'film':title,'visual':cap,'type':'original_educational_concept_svg','source_url':url,'paper_figure':'not_embedded','ref':ref}for i,title,cap,desc,insight,url,ref,kind,missing in DATA],ensure_ascii=False,indent=2))
(ROOT/'source_registry.csv').write_text('chapter,film,source_url,figure_locator,resource_status\n'+''.join(f'{x[0]},"{x[1]}",{x[5]},"{x[6]}",source_link_not_figure_file\n'for x in DATA))
(ROOT/'README.md').write_text('''# CVD Engineering Knowledge — Critical Concepts Audit v1.0

## 실제 반영된 결과

- v0.9 HTML의 89개 Chapter와 주요 기존 계산 기능을 보존한 파생본.
- Part 03의 19개 Chapter에 학습의 중심이 되는 물리/화학 모식도 19개를 삽입.
- ACL sp²–sp³–H ternary diagram 조작 기능과 BPSG reflow 표면형상 온도·시간 교육용 조작 기능 추가.
- SiN FTIR 정성 대역, SiGe 조성-격자 부정합, High-k 직렬 EOT 등의 17개 막질별 도표 추가.
- `film_19_critical_audit.csv`에서 19개 전체 결손과 도표·근거 상태 확인.

## 범위와 아직 미완료

- **원본 Paper Figure를 HTML에 내장한 숫자는 0**. 현재 실행환경에서 학술 원문 바이너리 다운로드가 실패했고, 출판사 이미지 핫링크는 제거했음. 원본 이미지인 것처럼 재그린 도표는 없음.
- 19개 Chapter의 모든 실험 그래프·원논문·정량 DOE를 심층 검증한 것이 아님. 이를 증명하는 데이터가 없으므로 완료 주장을 금지함.
- 이 버전의 Figure는 과학적 이해를 돕는 독자 제작 모식도로, 실제 실험 데이터/상도 경계/최적 Recipe 예측용이 아님.
- BPSG 교육용 reflow 속도 모형의 Q·tau_ref는 가정, SiGe 그래프는 Vegard 선형 근사, SiCN k 범위는 인용 논문 한정.
- 외부 원본 Figure는 원문 링크로 구분해 두었음.

## 검증

`python verify.py` 로 89개 template, 19개의 고유 Figure, 외부 img 존재 여부 검사.
Chromium 자동화 테스트는 `browser_check.py`를 실행해 검증할 것.
''',encoding='utf8')
(ROOT/'verify.py').write_text('''from bs4 import BeautifulSoup
from pathlib import Path
s=BeautifulSoup(Path(__file__).with_name('CVD_EDU_v1.0_Critical_Concepts.html').read_text(),'html.parser')
assert len(s.select('template[id^="tpl-"]'))==89
assert len(s.select('figure.critical-figure'))==19
assert not [i for i in s.select('img') if i.get('src','').startswith('http')]
assert s.select_one('#acl-h') and s.select_one('#reflow-top')
print('PASS: 89 chapters, 19 critical figures, 0 remote images, 2 interactive inputs')
''',encoding='utf8')
print('wrote',out,'size',out.stat().st_size,'audit rows',len(audit))
