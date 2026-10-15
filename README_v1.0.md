# CVD Engineering Knowledge — Critical Concepts Audit v1.0

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
