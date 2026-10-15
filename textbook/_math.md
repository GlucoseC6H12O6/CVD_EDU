# 70개 Chapter의 수식 상자 교체 목록

원래 HTML의 수식 상자(`div.math-figure`)는 수식을 글자 그대로(`<mtext>`) 넣어 분수·첨자가 조판되지 않았다. 빌드할 때 `## CID keep:N` 아래 한 줄의 LaTeX로 그 보존 블록의 수식을 바꾼다(texmath.py가 MathML로 바꾼다). 2026-10-15 추가.

## 01-01 keep:1
\mathrm{DR} = \frac{h_2 - h_1}{t_2 - t_1}

## 01-02 keep:0
\Delta G = \Delta G^{\circ} + R T \ln Q

## 01-07 keep:0
\theta = \frac{K C}{1 + K C}

## 01-08 keep:0
1\ \mathrm{eV} = 1.602176634\times10^{-19}\ \mathrm{J}

## 01-09 keep:1
\text{축적} = \text{유입} - \text{유출} + \text{생성} - \text{소모}

## 01-10 keep:0
\text{같은 막질} \neq \text{같은 전구체·활성화·형상}

## 02-01 keep:0
\text{Wafer} \rightarrow \text{Chamber} \rightarrow \text{Module} \rightarrow \text{Platform}

## 02-02 keep:0
\dot{n} = \frac{P_{\mathrm{std}}\, Q_{\mathrm{std}}}{R\, T_{\mathrm{std}}}

## 02-03 keep:1
A_{\mathrm{open}} = \frac{N \pi d^2}{4}

## 02-04 keep:0
R_{\mathrm{th}} = \frac{L}{k A}

## 02-06 keep:0
\frac{P_{\mathrm{reflected}}}{P_{\mathrm{forward}}} \neq \text{Ion flux}

## 02-07 keep:0
\text{Clean cycle} \;/\; \text{Exposure} \;/\; \text{Thermal cycle}

## 02-08 keep:0
e(t) = \text{Setpoint} - \text{Feedback}

## 05-02 keep:1
\mathrm{NU} = 100 \times \frac{h_{\max} - h_{\min}}{2\, h_{\mathrm{mean}}}\ [\%]

## 05-03 keep:0
\text{FTIR} \neq \text{XPS} \neq \text{SIMS}

## 05-04 keep:0
\rho = \frac{m}{A\, h}

## 05-05 keep:0
\rho \approx R_s \times t

## 05-06 keep:0
R_q = \sqrt{\mathrm{mean}\left[(z_i - \bar{z})^2\right]}

## 05-07 keep:0
u_y^2 \approx \sum_i \left(\frac{\partial f}{\partial x_i}\right)^2 u_i^2

## 06-01 keep:1
\text{Count} = f(\text{size threshold},\ \text{inspected area})

## 06-02 keep:0
\text{bump} \neq \text{external particle}

## 06-03 keep:0
\Delta\mathrm{DR} = \text{process} + \text{metrology} + \text{time effects}

## 06-04 keep:0
\text{step coverage} = \frac{t_{\mathrm{side}}}{t_{\mathrm{top}}}

## 06-05 keep:0
\sigma \approx \frac{E\, \Delta\alpha\, \Delta T}{1 - \nu}

## 06-06 keep:0
\text{Atomic concentration} \neq \text{surface density}

## 06-07 keep:0
Y_n = \text{baseline} + \text{transient after clean}

## 07-01 keep:1
\text{Observation} \rightarrow \text{Hypothesis} \rightarrow \text{Control} \rightarrow \text{Result}

## 07-02 keep:0
\Delta Y = Y_A - Y_B \pm \text{uncertainty}

## 07-03 keep:0
C_{pk} = \min\left[\frac{\mathrm{USL} - \mu}{3\sigma},\ \frac{\mu - \mathrm{LSL}}{3\sigma}\right]

## 07-04 keep:1
Y = \beta_0 + \beta_1 A + \beta_2 B + \beta_{12} A B

## 07-05 keep:0
\text{Correlation} \neq \text{Causal attribution}

## 07-06 keep:0
\text{Measured response} \in \text{validated criteria}

## 07-07 keep:0
\text{Next recipe} = \text{current recipe} + \text{correction}

## 08-01 keep:0
\frac{dN}{dt} = F_{\mathrm{in}} - F_{\mathrm{out}} + R\, V

## 08-02 keep:0
\frac{\partial C}{\partial t} + \nabla\cdot(\mathbf{u}\, C) = \nabla\cdot(D \nabla C) + R

## 08-03 keep:2
\nabla\cdot\mathbf{u} = 0 \qquad (\text{applicability checked})

## 08-05 keep:0
\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}

## 08-06 keep:0
\min_{x} f(x) \quad \text{subject to} \quad g(x) \le 0

## 08-07 keep:0
\text{Residual} = y_{\mathrm{measured}} - y_{\mathrm{predicted}}

## 09-01 keep:0
\text{same mesh/geometry; change one BC}

## 09-02 keep:1
\mathbf{Y} = [\,\mathrm{DR},\ \text{B wt%},\ \text{P wt%},\ \text{particle count}\,]

## 09-03 keep:0
\text{same grid} \cdot \text{same scale} \cdot \text{same wafer condition}

## 09-04 keep:0
\mathbf{Y} = [\,\text{Si:C:N},\ \mathrm{H},\ \text{stress},\ \text{barrier}\,]

## 09-05 keep:0
\mathbf{Y} = [\,\text{Si:B},\ \text{selectivity},\ \mathrm{LER},\ \text{adhesion}\,]

## 09-06 keep:0
\text{Risk} = \frac{\text{affected wafers}}{\text{exposed wafers}}
