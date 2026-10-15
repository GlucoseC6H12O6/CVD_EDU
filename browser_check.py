from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).with_name('CVD_EDU_v1.0_Critical_Concepts.html')
with sync_playwright() as pw:
 b=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for width,height in [(1440,900),(375,812)]:
  page=b.new_page(viewport={'width':width,'height':height})
  errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.set_content(p.read_text('utf8'),wait_until='domcontentloaded',timeout=30000)
  page.wait_for_timeout(200)
  def open_ch(cid):
   page.locator(f'button[data-ch="{cid}"]').evaluate('(el)=>el.click()')
   page.wait_for_timeout(200)
  open_ch('03-01')
  assert page.locator('#critical-03-01').count()==1
  original=page.locator('#acl-dot').get_attribute('cx');page.locator('#acl-h').evaluate('(el)=>{el.value=40;el.dispatchEvent(new Event("input",{bubbles:true}))}')
  changed=page.locator('#acl-dot').get_attribute('cx')
  assert original!=changed,(original,changed)
  open_ch('03-06');assert page.locator('#critical-03-06').count()==1
  original_result=page.locator('#rf-result').text_content()
  page.locator('#rf-temp').evaluate('(el)=>{el.value=900;el.dispatchEvent(new Event("input",{bubbles:true}))}')
  page.locator('#rf-time').evaluate('(el)=>{el.value=90;el.dispatchEvent(new Event("input",{bubbles:true}))}')
  changed_result=page.locator('#rf-result').text_content()
  assert original_result!=changed_result,(original_result,changed_result)
  open_ch('03-19');assert page.locator('#critical-03-19').count()==1
  image=page.locator('main .critical-svg').count()
  overflow=page.evaluate('document.documentElement.scrollWidth>window.innerWidth+1')
  print({'width':width,'nav_buttons':page.locator('button[data-ch]').count(),'acl_before_after':[original,changed],'bpsg_updated':changed_result[:75],'highk_figures':image,'horizontal_overflow':overflow,'page_errors':errors[:3]})
  page.screenshot(path=str(p.parent/f'highk_{width}.png'))
  assert not overflow and not errors
  page.close()
 b.close()
