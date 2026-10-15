# CVD Engineering Knowledge

반도체 CVD 공정을 처음 맡는 엔지니어를 위한 한국어 교과서다. HTML 한 파일로 되어 있어 내려받아 브라우저로 열면 오프라인에서도 읽을 수 있다.

**읽기:** [`CVD_EDU_v1.2_Textbook.html`](CVD_EDU_v1.2_Textbook.html)을 내려받아 브라우저로 연다.

## 구성

| Part | 내용 | 장 |
|---|---|---|
| 00 | 기초: 반도체 소자, 원자·결합, 화학반응, 농도, 물리·에너지, 기체·진공, 공학 수학, 측정·데이터, 안전 | 10 |
| 01 | 이론: CVD 개요, 열역학, 반응 속도론, 유체, 물질 전달, 열전달, 표면 화학, Plasma, 기상 화학, 증착 기술 | 10 |
| 02 | 장비: 장비 구조, Gas·원료 공급, Gas 분배, 가열, 진공·배기, RF, Chamber 부품·정비, 센서·제어 | 8 |
| 03 | 막질: ACL, SiB, SiC, SiBN, USG, BPSG, PSG/BSG, SiON, FSG, SiOCH, SiN, SiCN, a-Si, Poly-Si, SiGe, W, TiN/TaN, Mo/Ru, High-k | 19 |
| 04 | 공정 엔지니어링: Recipe 구조, 온도, 압력·유량, Plasma·형상, 원료·반응, Gap-fill, 계면·Integration, 공정 창 | 8 |
| 05 | 계측: 두께, 균일도, 조성·결합, 기계 물성, 전기·광학, 현미경, 측정 신뢰도 | 7 |
| 06 | 결함: Particle, 막 형태, 증착 속도·균일도 이상, Void·Seam, 응력·밀착, 화학 오염, Chamber 노화 | 7 |
| 07 | 문제 해결·제어: 문제 해결 절차, Chamber Matching, SPC, DOE, 고장 진단, Qualification, APC | 7 |
| 08 | 모델링: 기본 모델, 반응·수송, CFD, Feature-scale, 통계·인과, 최적화, 데이터 기반 공정 | 7 |
| 09 | 사례: ACL 오염, BPSG 형상 이상, USG 불균일, SiCN 조성·응력, SiB Hardmask, 다중 Chamber Matching | 6 |

## 그림의 출처와 라이선스

본문 그림은 두 종류의 공개 자료에서만 가져왔다.

- **미국 특허 도면**: USPTO 공개 문서다. 그림마다 특허 번호와 도면 번호를 적었다.
- **CC BY 논문 그림**: PubMed Central에서 받은 오픈 액세스 논문(CC BY 3.0/4.0)이다. 그림마다 저자, 학술지, 연도, 라이선스를 적었다.

유료 저널 그림과 비상업 조건(CC BY-NC 계열) 그림은 넣지 않았다. 그림 원본은 `film_content/figures/_staging/`, 출처 기록은 `textbook/_자료수집_*.md`와 `film_content/*_자료수집.md`에 있다. 그림을 다시 쓸 때는 원래 라이선스와 출처 표기를 따른다.

계산 위젯과 Part 00의 조작 위젯은 이 교재를 위해 만든 것이다.

## 다시 만들기

Python 3 표준 라이브러리만 쓴다.

```bash
python3 prep_figures.py    # 그림 원본을 자르고 회전해 film_content/figures/에 둔다
python3 apply_textbook.py  # CVD_EDU_v1.2_Textbook.html을 만든다
```

`apply_textbook.py`는 89개 장의 절 id, 사이드바 목차, 보존 블록, 태그 짝, 장 사이 연결을 검사하고, 하나라도 어긋나면 파일을 쓰지 않는다.

## 원고 위치

| 대상 | 원고 |
|---|---|
| Part 00–02, 04–09 (70개 장) | `textbook/NN-NN.md`, 그림·수식·위젯 보존 블록은 `textbook/_keep/NN-NN.json` |
| 70개 장의 교체 그림 | `textbook/_figures.md` |
| Part 03 (19개 막질) | `film_content/03-NN_*_본문.md`, 자료 수집 기록은 `*_자료수집.md` |
| 그림 | `film_content/figures/` (원본은 `_staging/`, 자르기·복사는 `prep_figures.py`) |

원고 문법과 버전별 변경 내용은 [`README_v1.2.md`](README_v1.2.md)에 있다. `CVD_EDU_v1.0_Critical_Concepts.html`은 빌드 입력이라 고치지 않는다.

## 근거 표시

본문 주장 뒤의 표시는 근거의 종류를 뜻한다. **[논문]** 논문에 보고된 값, **[특허]** 특허의 주장·실시예, **[리뷰]** 교과서 수준의 정설, **[계산]** 가정을 밝힌 교육용 계산, **[현장]** 문헌으로 못 박지 못한 현장 통념이다. 번호는 장 끝 참고 목록의 번호이며, 목록마다 서지만 확인했는지 내용까지 확인했는지 적었다.

## 한계

- 공정 조건과 수치는 공개 논문·특허에서 가져왔다. 실제 양산 Recipe나 특정 회사 장비의 데이터가 아니다.
- 공정 창 예시와 계산 예의 입력값은 설명을 위한 가상의 숫자다.
- 반도체 CVD 현업 전문가의 검수를 아직 받지 않았다.
- `이해 확인` 질문에는 아직 해설이 없다.
- 남은 공백은 [`README_v1.2.md`](README_v1.2.md)의 "아직 안 된 것"에 적었다.
