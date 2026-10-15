from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).with_name('CVD_EDU_v1.0_Critical_Concepts.html')
with sync_playwright() as pw:
 b=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1280,'height':850})
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.set_content(p.read_text('utf8'),wait_until='domcontentloaded')
 report=[]
 for idx in range(1,20):
  cid=f'03-{idx:02d}'
  page.locator(f'button[data-ch="{cid}"]').evaluate('(el)=>el.click()')
  exists=page.locator(f'#critical-{cid}').count()==1
  width_ok=not page.evaluate('document.documentElement.scrollWidth>window.innerWidth+1')
  report.append((cid,exists,width_ok))
  if cid in ('03-01','03-06','03-11'):
   fig=page.locator(f'#critical-{cid}')
   fig.scroll_into_view_if_needed(timeout=8000)
   page.wait_for_timeout(130)
   page.screenshot(path=str(p.parent/f'figure_{cid}.png'))
 print(report);print('errors',errors[:3]);assert all(a and b for _,a,b in report) and not errors
 b.close()
