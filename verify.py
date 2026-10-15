from bs4 import BeautifulSoup
from pathlib import Path
s=BeautifulSoup(Path(__file__).with_name('CVD_EDU_v1.0_Critical_Concepts.html').read_text(),'html.parser')
assert len(s.select('template[id^="tpl-"]'))==89
assert len(s.select('figure.critical-figure'))==19
assert not [i for i in s.select('img') if i.get('src','').startswith('http')]
assert s.select_one('#acl-h') and s.select_one('#reflow-top')
print('PASS: 89 chapters, 19 critical figures, 0 remote images, 2 interactive inputs')
