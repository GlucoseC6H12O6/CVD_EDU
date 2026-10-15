r"""문장 속에 그냥 적힌 수식(k_m, J = k_m(C_b − C_s), Da = k_s/k_m …)을 찾아 $LaTeX$로 바꾼다.

수식으로 보는 구간: 수식 문자로만 이루어진 구간 가운데 아래첨자(_)나 관계 기호(= ≈ ≪ ≫ ∝ ≤ ≥)가 있는 것.
링크·코드·이미 $…$인 부분·표의 칸 구분(|)은 건드리지 않는다. 규칙으로 처리하기 애매한 것은 OVERRIDE에 직접 적었다.
사용: from prose_math import convert_text
"""
import re

GREEK = {'α': r'\alpha', 'β': r'\beta', 'γ': r'\gamma', 'δ': r'\delta', 'ε': r'\varepsilon', 'η': r'\eta', 'θ': r'\theta',
         'κ': r'\kappa', 'λ': r'\lambda', 'μ': r'\mu', 'ν': r'\nu', 'ξ': r'\xi', 'π': r'\pi', 'ρ': r'\rho', 'σ': r'\sigma',
         'τ': r'\tau', 'φ': r'\varphi', 'χ': r'\chi', 'ψ': r'\psi', 'ω': r'\omega', 'Δ': r'\Delta', 'Γ': r'\Gamma',
         'Σ': r'\Sigma', 'Ω': r'\Omega', 'Φ': r'\Phi', 'Λ': r'\Lambda', 'ṅ': r'\dot{n}', 'Ṅ': r'\dot{N}'}
OPMAP = {'×': r'\times', '·': r'\cdot', '≈': r'\approx', '≪': r'\ll', '≫': r'\gg', '∝': r'\propto', '≤': r'\le',
         '≥': r'\ge', '−': '-', '∇': r'\nabla', '∂': r'\partial', '∞': r'\infty', '→': r'\rightarrow', '°': r'^{\circ}'}
DIMLESS = {'Sh', 'Sc', 'Pe', 'Da', 'Re', 'Kn', 'Bi', 'Nu', 'Pr', 'Gr', 'Ma'}
WORDS = {'DR', 'EOT', 'NU', 'SC', 'ER', 'RI', 'WERR', 'LER', 'LWR', 'CD', 'AR', 'OE', 'TDS'}
CHEMW = {'Si', 'Ge', 'Ti', 'Ta', 'Al', 'Hf', 'Zr', 'Ru', 'Mo', 'Cl', 'Ar', 'He', 'Ga', 'Se'}
FUNCS = {'exp', 'ln', 'log', 'min', 'max'}
UNITS = {'Torr', 'mTorr', 'Pa', 'kPa', 'MPa', 'GPa', 'atm', 'bar', 'sccm', 'slm', 'mol', 's', 'ms', 'min', 'h', 'K',
         'J', 'kJ', 'eV', 'W', 'kW', 'V', 'g', 'kg', 'L', 'cm', 'mm', 'm', 'µm', 'μm', 'nm', 'Å', 'ppm', 'ppb', 'Hz',
         'kHz', 'MHz', 'Ω', '°C', 'N', 'mW'}
CHEM1 = set('HONF')
SUBD = '₀₁₂₃₄₅₆₇₈₉'
SUPC = '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻'
LET = r'A-Za-zα-ωΑ-ΩṅṄµÅ'
ALLOWED = r"%s0-9_ .,+−×·/()\[\]=≈≪≫∝≤≥<>^∇∂∞°" % LET + SUBD + SUPC + "ₐₑₓᵢⱼ'"
SPAN = re.compile(r'[%s]+' % ALLOWED)
REL = re.compile(r'[=≈≪≫∝≤≥]|_')
U1 = r'(?:°C|[A-Za-zµμÅΩ]+[²³⁻¹]*)'
UNITRE = r'%s(?:[/·](?:\(%s(?:·%s)*\)|%s))*' % (U1, U1, U1, U1)
NUM = r'\d+(?:,\d{3})*(?:\.\d+)?(?:×10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)?'
TOK = re.compile(r'(?P<num>%s)(?:(?P<usp> ?)(?P<unit>%s))?|(?P<id>[%s]+)(?P<chem>[%s]+)?(?:_(?P<sub>[A-Za-z0-9]+(?:,[0-9])?))?|(?P<sp>\s+)|(?P<o>.)'
                 % (NUM, UNITRE, LET, SUBD))

# 규칙으로 처리하기 애매한 구간: 원문 → 바꿀 Markdown(일부만 수식일 수 있다)
OVERRIDE = {
    'Q4. n = 1.9': 'Q4. $n = 1.9$',
    'LPCVD 600 °C, NH₃/TiCl₄ = 10': r'LPCVD 600 °C, $\mathrm{NH_3/TiCl_4} = 10$',
    '560 °C, PH₃/SiH₄ = 0.0008': r'560 °C, $\mathrm{PH_3/SiH_4} = 0.0008$',
    'e(t) = SP − PV, PID': r'$e(t) = \mathrm{SP} - \mathrm{PV}$, PID',
    'y = Xβ + ε, VIF·': r'$y = X\beta + \varepsilon$, VIF·',
    'Sputter 100 nm/min. D/S = 5, E/D = 0.2': r'Sputter 100 nm/min. $D/S = 5$, $E/D = 0.2$',
    '3,000 / 5 × 1.1 = 660 nm. 660 + 100 + 150 = 910 nm': r'$3{,}000/5 \times 1.1 = 660\ \mathrm{nm}$. $660 + 100 + 150 = 910\ \mathrm{nm}$',
    '1.48 g/cm³, k ≈ 0.5': r'1.48 g/cm³, $k \approx 0.5$',
    'n ≈ 1.57, k ≈ 3.57 / 193 nm': r'$n \approx 1.57$, $k \approx 3.57$ / 193 nm',
    'k = 0.5, 500 nm': r'$k = 0.5$, 500 nm',
    'Si₃N₄(N/Si = 1.33, Si/N = 0.75)': r'Si₃N₄($\mathrm{N/Si} = 1.33$, $\mathrm{Si/N} = 0.75$)',
    'N_H (cm⁻³)': r'$N_{\mathrm{H}}$ (cm⁻³)',
    'N_H': r'$N_{\mathrm{H}}$',
    'J_g. (a) n': r'$J_g$. (a) n',
    'J_g 10': r'$J_g$ 10',
    'Pa = N/m²': r'$\mathrm{Pa} = \mathrm{N/m^2}$',
    'N·m/s = J/s': r'$\mathrm{N\cdot m/s} = \mathrm{J/s}$',
    '500 sccm × 2 min + 1,000 sccm × 1 min = 2,000 standard cm³': r'$500\ \mathrm{sccm} \times 2\ \mathrm{min} + 1{,}000\ \mathrm{sccm} \times 1\ \mathrm{min} = 2{,}000\ \text{standard}\ \mathrm{cm^3}$',
    'm²/s × mol/m⁴ = mol/(m²·s)': r'$\mathrm{m^2/s} \times \mathrm{mol/m^4} = \mathrm{mol/(m^2\cdot s)}$',
    '[m²/s], ∂C_A/∂x': r'[m²/s], $\partial C_A/\partial x$',
    'S_eff[m³/s]': r'$S_{\mathrm{eff}}$[m³/s]',
    'R_th,contact, Wafer': r'$R_{\mathrm{th,contact}}$, Wafer',
    'R_th,gas': r'$R_{\mathrm{th,gas}}$',
    'σ = −120 + 100x MPa': r'$\sigma = -120 + 100x\ \mathrm{MPa}$',
    'NU = (max − min)/(2·mean) × 100': r'$\mathrm{NU} = (\mathrm{max} - \mathrm{min})/(2\cdot\mathrm{mean}) \times 100$',
    'y = β₀ + Σβᵢxᵢ + Σβᵢⱼxᵢxⱼ + ε': r'$y = \beta_0 + \sum \beta_i x_i + \sum \beta_{ij} x_i x_j + \varepsilon$',
    'Low-k(k = 2.7)': r'Low-k($k = 2.7$)',
    'Resist(n ≈ 1.7)': r'Resist($n \approx 1.7$)',
    'm, t_b = 100': r'm, $t_b = 100$',
    'J_tot = Cu + J': r'$J_{\mathrm{tot}} = C u + J$',
    '100 × 25 nm × 100 MPa = 250 N/m': r'$100 \times 25\ \mathrm{nm} \times 100\ \mathrm{MPa} = 250\ \mathrm{N/m}$',
}
SKIP = {'P=O', '1,400, P=O', 'C, C=C, C', 'Flux = Sticking'}


def ident(name, chem, sub, chemctx):
    if name in GREEK and len(name) == 1:
        b = GREEK[name]
    elif chem:
        dig = ''.join(str(SUBD.index(c)) for c in chem)
        if len(name) >= 2 or name in CHEM1:
            return r'\mathrm{%s_{%s}}' % (name, dig)
        return '%s_{%s}' % (name, dig)
    elif chemctx and (name in CHEMW or (len(name) == 1 and name.isupper())):
        b = r'\mathrm{%s}' % name
    elif name in CHEMW:
        b = r'\mathrm{%s}' % name
    elif name in FUNCS:
        b = '\\' + name
    elif len(name) == 1:
        b = name
    elif name in DIMLESS or name in WORDS:
        b = r'\mathrm{%s}' % name
    elif sub is not None and len(name) <= 3 and name.isupper():
        b = r'\mathrm{%s}' % name
    elif len(name) <= 3:
        b = ' '.join(GREEK.get(c, c) for c in name)
    else:
        b = r'\text{%s}' % name
    if sub is not None:
        s = sub if len(sub) == 1 or re.fullmatch(r'\d+(,\d)?', sub) else r'\mathrm{%s}' % sub
        b = '%s_{%s}' % (b if ' ' not in b else '{%s}' % b, s)
    return b


def to_latex(s):
    chemctx = bool(re.search(r'(?:[A-Z][a-z]?){2,}[%s]|[A-Z][a-z][%s]|(?<![A-Za-z])[HONF][%s]' % (SUBD, SUBD, SUBD), s))
    out = []
    i = 0
    while i < len(s):
        m = TOK.match(s, i)
        if m.group('num'):
            num = m.group('num')
            unit = m.group('unit')
            first = re.match(r'°C|[A-Za-zµμÅΩ]+', unit).group(0) if unit else None
            if unit and first in UNITS:
                out.append(r'%s\ \mathrm{%s}' % (num, unit)); i = m.end(); continue
            out.append(num); i = m.end('num'); continue
        if m.group('id'):
            out.append(ident(m.group('id'), m.group('chem'), m.group('sub'), chemctx))
        elif m.group('sp'):
            out.append(' ')
        else:
            c = m.group('o')
            out.append(OPMAP.get(c, c))
        i = m.end()
    t = ''
    for p in out:
        if re.search(r'\\[A-Za-z]+$', t) and re.match(r'[A-Za-z0-9]', p):
            t += ' '
        t += p
    return re.sub(r' {2,}', ' ', t).strip()


def convert_text(text, log=None):
    """한 줄을 받아 수식 구간을 $…$로 바꾼다. 링크·코드·기존 수식은 건드리지 않는다."""
    keep = []
    def hold(m):
        keep.append(m.group(0)); return '\x03%d\x03' % (len(keep) - 1)
    t = re.sub(r'\$[^$]*\$|`[^`]*`|\]\([^)]*\)|!\[[^\]]*\]|https?://\S+', hold, text)
    def rep(m):
        raw = m.group(0)
        core = raw.strip(' .,')
        lead = raw[:len(raw) - len(raw.lstrip(' .,'))]
        trail = raw[len(raw.rstrip(' .,')):]
        if core in OVERRIDE:
            if log is not None: log.append((core, OVERRIDE[core]))
            return lead + OVERRIDE[core] + trail
        if (not core or core in SKIP or not REL.search(core) or core.count('(') != core.count(')')
                or re.match(r'^[=≈≪≫∝≤≥]', core) or re.search(r'[=≈≪≫∝≤≥]$', core)):
            return raw
        idents = re.findall(r'[%s]+' % LET, core)
        if not ('_' in core or re.search(r'\d', core) or any(len(x) <= 2 for x in idents)):
            return raw
        if m.start() > 0 and re.match(r'[A-Za-z0-9\-]', t[m.start() - 1]):
            return raw
        mt = re.match(r'^(.*?[^,]),\s*([A-Za-z]{3,}[^=≈≪≫∝≤≥_]*)$', core)
        if mt and REL.search(mt.group(1)):
            core, trail = mt.group(1), ', ' + mt.group(2) + trail
        tex = to_latex(core)
        if log is not None: log.append((core, '$%s$' % tex))
        return '%s$%s$%s' % (lead, tex, trail)
    t = SPAN.sub(rep, t)
    return re.sub('\x03(\\d+)\x03', lambda m: keep[int(m.group(1))], t)


def convert_md(md, log=None):
    """원고 전체: 코드 블록·$$ 블록·그림 줄·출처 줄은 건너뛴다."""
    out, inblock = [], False
    for line in md.split('\n'):
        s = line.strip()
        if s.startswith('```') or s == '$$':
            inblock = not inblock; out.append(line); continue
        if inblock or s.startswith(('![', '*출처', '{{keep')) or s.startswith('> 근거'):
            out.append(line); continue
        out.append(convert_text(line, log))
    return '\n'.join(out)
