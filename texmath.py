"""LaTeX 수식의 일부 문법을 MathML로 바꾼다(표준 라이브러리만 사용).

원고에서 수식은 `$...$`(본문 속 수식)와 `$$ ... $$` 블록(한 줄에 수식 하나)으로 쓴다.
지원: \\frac \\dfrac \\sqrt \\text \\mathrm \\operatorname ^ _ { } \\left \\right, 그리스 문자, 자주 쓰는 연산자,
\\exp·\\ln 같은 함수 이름, \\bar·\\dot·\\overline·\\hat·\\tilde, 간격(\\, \\; \\quad), 유니코드 위·아래 첨자(², ₂ 등).
변수는 한 글자씩 기울여 쓰고(R T), 단위·화학식·약어는 \\mathrm{}으로 바로 세운다. 한글은 자동으로 \\text 처리한다.
"""
import re
import html

GREEK = dict(alpha='α', beta='β', gamma='γ', delta='δ', epsilon='ϵ', varepsilon='ε', zeta='ζ', eta='η', theta='θ',
             vartheta='ϑ', iota='ι', kappa='κ', lambda_='λ', mu='μ', nu='ν', xi='ξ', pi='π', rho='ρ', sigma='σ',
             tau='τ', upsilon='υ', phi='ϕ', varphi='φ', chi='χ', psi='ψ', omega='ω', Gamma='Γ', Delta='Δ',
             Theta='Θ', Lambda='Λ', Xi='Ξ', Pi='Π', Sigma='Σ', Phi='Φ', Psi='Ψ', Omega='Ω')
GREEK['lambda'] = GREEK.pop('lambda_')
OPS = dict(times='×', cdot='·', approx='≈', propto='∝', le='≤', leq='≤', ge='≥', geq='≥', ne='≠', neq='≠',
           pm='±', mp='∓', to='→', rightarrow='→', leftarrow='←', Rightarrow='⇒', Leftrightarrow='⇔',
           rightleftharpoons='⇌', leftrightarrow='↔', longrightarrow='⟶', infty='∞', partial='∂', nabla='∇',
           sim='∼', simeq='≃', equiv='≡', ll='≪', gg='≫', gtrsim='≳', lesssim='≲', gtrapprox='⪆', lessapprox='⪅',
           cdots='⋯', ldots='…', dots='…', circ='∘', div='÷', ast='∗', uparrow='↑', downarrow='↓', parallel='∥',
           perp='⊥', mid='∣', colon=':', setminus='∖', cap='∩', cup='∪', forall='∀', exists='∃', neg='¬',
           sum='∑', prod='∏', int='∫', oint='∮', prime='′', degree='°', angle='∠', checkmark='✓')
OPS['in'] = '∈'
FUNCS = {'exp', 'ln', 'log', 'sin', 'cos', 'tan', 'sinh', 'cosh', 'tanh', 'max', 'min', 'lim', 'det', 'arg', 'sup', 'inf'}
SPACE = {',': '0.1667em', ':': '0.2222em', '>': '0.2222em', ';': '0.2778em', ' ': '0.25em', 'quad': '1em', 'qquad': '2em'}
ACCENT = dict(bar='¯', overline='¯', hat='^', widehat='^', dot='˙', ddot='¨', tilde='~', widetilde='~', vec='→')
LARGE = {'∑', '∏'}
SUP = dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱˣ', '0123456789+−=()nix'))
SUB = dict(zip('₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₕₖₗₘₙₚₛₜᵢⱼᵣᵤᵥ', '0123456789+−=()aeoxhklmnpstijruv'))
OPCHARS = set('+-−=<>≤≥≈∝×·÷/()[]|,;:!→←↔⇌⇒±∓∂∇∫∑∏…′%≠≡∼≪≫≳≲∈∖⟶↑↓∥⊥∣')
HANGUL = re.compile(r'[가-힣ㄱ-ㆎ]')


def esc(s):
    return html.escape(s, quote=False)


class _P:
    def __init__(self, src, display):
        self.s, self.i, self.display = src, 0, display

    def peek(self):
        return self.s[self.i] if self.i < len(self.s) else ''

    def group_text(self):
        """{...}의 내용을 글자 그대로 돌려준다."""
        self.skip_ws()
        if self.peek() != '{':
            c = self.peek(); self.i += 1; return c
        depth, start = 0, self.i
        while self.i < len(self.s):
            c = self.s[self.i]
            if c == '\\':
                self.i += 2; continue
            if c == '{': depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    self.i += 1
                    return self.s[start + 1:self.i - 1]
            self.i += 1
        raise ValueError('닫히지 않은 { : ' + self.s)

    def skip_ws(self):
        while self.peek() == ' ':
            self.i += 1

    def arg(self, upright=False):
        return _row(_P(self.group_text(), self.display).seq(upright))

    def cmd(self):
        m = re.match(r'\\([A-Za-z]+|.)', self.s[self.i:])
        self.i += len(m.group(0))
        return m.group(1)

    def seq(self, upright=False):
        out = []
        while self.i < len(self.s):
            c = self.peek()
            if c in '^_':
                self.i += 1
                base = out.pop() if out else '<mrow></mrow>'
                out.append(self.script(base, c, upright))
                continue
            if (c in SUP or c in SUB) and out:
                table = SUP if c in SUP else SUB
                j = self.i
                while j < len(self.s) and self.s[j] in table: j += 1
                txt = ''.join(table[x] for x in self.s[self.i:j]); self.i = j
                val = _row(_P(txt, self.display).seq(upright))
                base = out.pop()
                m = re.match(r'^<msub>(.*)</msub>$', base, re.S)
                if c in SUP and m and base.count('<msub>') == 1:
                    out.append('<msubsup>%s%s</msubsup>' % (m.group(1), val))
                else:
                    out.append('<%s>%s%s</%s>' % ('msup' if c in SUP else 'msub', base, val, 'msup' if c in SUP else 'msub'))
                continue
            node = self.atom(upright)
            if node is not None:
                out.append(node)
        return out

    def script(self, base, first, upright):
        sub = sup = None
        for k in (first, None):
            kind = k
            if kind is None:
                self.skip_ws()
                if self.peek() and self.peek() in '^_' and self.peek() != first:
                    kind = self.peek(); self.i += 1
                else:
                    break
            val = self.scriptarg(upright)
            if kind == '_': sub = val
            else: sup = val
        large = any(('>%s<' % o) in base for o in LARGE) and self.display
        if sub is not None and sup is not None:
            tag = 'munderover' if large else 'msubsup'
            return '<%s>%s%s%s</%s>' % (tag, base, sub, sup, tag)
        if sub is not None:
            tag = 'munder' if large else 'msub'
            return '<%s>%s%s</%s>' % (tag, base, sub, tag)
        tag = 'mover' if large else 'msup'
        return '<%s>%s%s</%s>' % (tag, base, sup, tag)

    def scriptarg(self, upright):
        self.skip_ws()
        if self.peek() == '{':
            return _row(_P(self.group_text(), self.display).seq(upright))
        if self.peek() == '\\':
            node = self.atom(upright)
            return node
        if self.peek().isdigit():
            self.i += 1; return '<mn>%s</mn>' % self.s[self.i - 1]
        return self.atom(upright, single=True)

    def atom(self, upright, single=False):
        c = self.peek()
        if c == ' ':
            self.i += 1; return None
        if c == '{':
            return _row(_P(self.group_text(), self.display).seq(upright))
        if c == '}':
            self.i += 1; return None
        if c in '&':
            self.i += 1; return None
        if c == '\\':
            return self.command(upright)
        if c in SUP or c in SUB:
            table = SUP if c in SUP else SUB
            j = self.i
            while j < len(self.s) and self.s[j] in table: j += 1
            txt = ''.join(table[x] for x in self.s[self.i:j]); self.i = j
            return '<mrow>%s</mrow>' % ''.join(_P(txt, self.display).seq(upright))
        if HANGUL.match(c):
            m = re.match(r'[가-힣ㄱ-ㆎ][가-힣ㄱ-ㆎ ·]*', self.s[self.i:])
            t = m.group(0).rstrip(); self.i += len(t)
            return '<mtext>%s</mtext>' % esc(t)
        if c.isdigit() or (c == '.' and self.s[self.i + 1:self.i + 2].isdigit()):
            m = re.match(r'\d*\.?\d+(?:,\d{3})*(?:\.\d+)?' if not single else r'\d', self.s[self.i:])
            self.i += len(m.group(0)); return '<mn>%s</mn>' % m.group(0)
        if c.isalpha() and c.isascii():
            if upright and not single:
                m = re.match(r'[A-Za-z]+', self.s[self.i:]); self.i += len(m.group(0))
                return '<mi mathvariant="normal">%s</mi>' % m.group(0)
            self.i += 1
            return '<mi mathvariant="normal">%s</mi>' % c if upright else '<mi>%s</mi>' % c
        self.i += 1
        if c == '-': c = '−'
        if c == "'": return '<mo>′</mo>'
        if c in OPCHARS:
            if c in '([|': return '<mo stretchy="false">%s</mo>' % esc(c) if not self.display else '<mo>%s</mo>' % esc(c)
            return '<mo>%s</mo>' % esc(c)
        if c in 'ΓΔΘΛΞΠΣΦΨΩ' or upright:
            return '<mi mathvariant="normal">%s</mi>' % esc(c)
        return '<mi>%s</mi>' % esc(c)

    def command(self, upright):
        name = self.cmd()
        if name in ('frac', 'dfrac', 'tfrac'):
            a = self.arg(upright); b = self.arg(upright)
            f = '<mfrac>%s%s</mfrac>' % (a, b)
            if name == 'dfrac': f = '<mstyle displaystyle="true">%s</mstyle>' % f
            if name == 'tfrac': f = '<mstyle displaystyle="false">%s</mstyle>' % f
            return f
        if name == 'sqrt':
            self.skip_ws()
            if self.peek() == '[':
                j = self.s.index(']', self.i); idx = self.s[self.i + 1:j]; self.i = j + 1
                return '<mroot>%s%s</mroot>' % (self.arg(upright), _row(_P(idx, False).seq()))
            return '<msqrt>%s</msqrt>' % self.arg(upright)
        if name in ('text', 'textrm', 'mbox'):
            t = self.group_text()
            t = t.replace('\\%', '%').replace('\\,', ' ').replace('\\ ', ' ')
            t = t.replace(' ', ' ') if t.startswith(' ') or t.endswith(' ') else t
            return '<mtext>%s</mtext>' % esc(t)
        if name in ('mathrm', 'operatorname', 'rm', 'mathsf'):
            return _row(_P(self.group_text(), self.display).seq(upright=True))
        if name in ('mathit',):
            return _row(_P(self.group_text(), self.display).seq(upright=False))
        if name in ('mathbf', 'boldsymbol'):
            return '<mstyle mathvariant="bold">%s</mstyle>' % self.arg(upright)
        if name in ('xrightarrow', 'xleftarrow'):
            lab = self.arg(upright)
            return '<mover><mo stretchy="true">%s</mo>%s</mover>' % ('→' if name[1] == 'r' else '←', lab)
        if name in ACCENT:
            return '<mover accent="true">%s<mo>%s</mo></mover>' % (self.arg(upright), ACCENT[name])
        if name in ('left', 'right', 'big', 'Big', 'bigg', 'Bigg', 'bigl', 'bigr', 'Bigl', 'Bigr', 'displaystyle', 'limits', 'nolimits', '!'):
            return None
        if name in SPACE:
            return '<mspace width="%s"/>' % SPACE[name]
        if name == '\\':
            return None
        if name in GREEK:
            g = GREEK[name]
            return '<mi mathvariant="normal">%s</mi>' % g if (name[0].isupper() or upright) else '<mi>%s</mi>' % g
        if name in OPS:
            o = OPS[name]
            if o in LARGE or o == '∫':
                return '<mo largeop="true">%s</mo>' % o if self.display else '<mo>%s</mo>' % o
            return '<mo>%s</mo>' % o
        if name in FUNCS:
            return '<mi>%s</mi><mo>&#x2061;</mo>' % name if False else '<mi mathvariant="normal">%s</mi>' % name
        if len(name) == 1 and not name.isalpha():
            return '<mo>%s</mo>' % esc(name)
        raise ValueError('모르는 명령 \\%s' % name)


def _row(nodes):
    nodes = [n for n in nodes if n]
    return nodes[0] if len(nodes) == 1 else '<mrow>%s</mrow>' % ''.join(nodes)


def tex_to_mathml(src, display=False, label=None):
    body = ''.join(n for n in _P(src.strip(), display).seq() if n)
    attr = ' display="block"' if display else ''
    if label:
        attr += ' aria-label="%s"' % html.escape(label)
    return '<math xmlns="http://www.w3.org/1998/Math/MathML"%s>%s</math>' % (attr, body if body.count('<') else body)


def block(lines):
    """$$ 블록: 빈 줄을 뺀 한 줄마다 수식 하나."""
    rows = [l.strip() for l in lines if l.strip()]
    return '<div class="eqs">%s</div>' % ''.join(tex_to_mathml(r, display=True) for r in rows)


INLINE_RE = re.compile(r'(?<![\\$])\$(?!\$)(.+?)(?<!\\)\$')

if __name__ == '__main__':
    tests = [r'A_{\mathrm{open}} = \frac{N \pi d^2}{4}', r'k = A \exp\left(-\frac{E_a}{R T}\right)',
             r'\mathrm{SiH_4} + 2\,\mathrm{O_2} \rightarrow \mathrm{SiO_2} + 2\,\mathrm{H_2O}',
             r'\sigma_f = \frac{E_s}{1-\nu_s}\,\frac{t_s^2}{6 t_f}\left(\frac{1}{R}-\frac{1}{R_0}\right)', '축적 = 유입 − 유출',
             r'\dot{n} = \frac{P_{\mathrm{std}} Q_{\mathrm{std}}}{R T_{\mathrm{std}}}', r'u_y^2 \approx \sum_i \left(\frac{\partial f}{\partial x_i}\right)^2 u_i^2',
             r'1\,\mathrm{sccm} \approx 7.435\times10^{-7}\ \mathrm{mol/s}', 'Kn ≪ 1', r'T_h⁴ − T_w⁴']
    for t in tests:
        print(t, '\n   ', tex_to_mathml(t, True)[:260])
