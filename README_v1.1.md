# CVD EDU v1.1 — Part 03 본문 원고 반영

## 무엇이 바뀌었나

- 출력: `CVD_EDU_v1.1_Film_Content.html`. `CVD_EDU_v1.0_Critical_Concepts.html`은 수정하지 않았다.
- Part 03의 19개 Chapter 본문을 `film_content/03-NN_*_본문.md` 원고로 교체했다. Chapter마다 13개 절(00 한 장 요약 ~ 12 참고문헌)이고, 사이드바에 절 목록이 나온다.
- Chapter마다 유지한 것: 제목, v1.0의 핵심 개념도(`figure.critical-figure`) 19개와 조작 기능 2개(ACL 삼원 상도, BPSG Reflow).
- Chapter 끝에 `film_content/03-NN_*_자료수집.md`를 접힌 “자료 수집 기록”으로 넣었다. 출처별 확인 수준(A/B/C)이 적혀 있다.
- Part 00–02, 04–09의 70개 Chapter는 v1.0 그대로다.

## 다시 만들기

```
python3 apply_film_content.py
```

표준 라이브러리만 쓴다. `film_content/*.md`를 고친 뒤 실행하면 HTML이 다시 만들어지고, 끝에서 다음을 검사한다: template 89개, critical figure 19개, 19개 Chapter × 13개 절, 원격 이미지 0개, 조작 기능 존재, 태그 짝.

## 그림을 넣는 법

본문 Markdown에 다음처럼 쓰면 `film_content/figures/`의 파일이 HTML에 내장된다(SVG는 Inline, PNG·JPG는 Base64).

```
![대체 텍스트](figures/파일명.png)

*그림 설명*

*출처: 저자, 저널 (연도), Fig. N. CC BY 4.0. 링크*
```

`*출처:`로 시작하는 줄이 있으면 “원문 Figure” 표지가, 없으면 “자체 제작 모식도” 표지가 붙는다.

## 아직 안 된 것

- **원문 Figure 48장 내장(17개 장).** 미국 특허 도면 35장과 CC BY 논문 그림 13장이다. 그림마다 출처·라이선스·링크가 붙어 있고, 장별 목록은 각 자료 수집 기록의 “본문에 넣은 원문 그림” 절에 있다. 유료 저널 그림은 넣지 않았다.
- 원본 도면은 `film_content/figures/_staging/`에 있고, `python3 prep_figures.py`가 여백 제거·회전·분할을 해서 `film_content/figures/`에 최종 파일을 만든다. `patent_figs.py`는 Google Patents에서 도면을 받는 도구다.
- **03-04 SiBN/SiBCN, 03-17 TiN/WN/TaN에는 아직 원문 그림이 없다.** 후보 도면은 `_staging`에 받아 두었다(US 6,962,876 FIG. 3·4·6, US 7,186,446 Fig. 2·3·5, US 12,180,583 FIG. 2·6·7). 자르기와 본문 삽입이 남았다. Ru는 후보를 찾지 못했다.
- 수정한 원고와 그림은 아직 `~/Downloads/CVD_EDU_Film_Content/`에 되돌려 복사하지 않았다. 그쪽은 그림을 넣기 전 판이다.
- 본문의 근거는 초록·검색 요약·특허 요약 수준이다. 논문 전문은 열람하지 못했다. 각 자료 수집 기록 끝의 “아직 비어 있는 자료” 절 참고.
- `[현장]` 표시 내용은 문헌 근거가 없다.
