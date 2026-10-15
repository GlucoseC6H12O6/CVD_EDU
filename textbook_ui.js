/* v1.2 읽기 도구. apply_textbook.py가 </body> 앞에 넣는다.
   1) 근거 표시(논문 3, 특허 S05 …)에 마우스를 올리면 장 끝 참고 목록이나 출처 표의 그 항목을 띄운다. 터치 화면에서는 누르면 뜬다.
   2) 장 끝에서 한 번 더 내리면 다음 장으로, Part의 마지막 장이면 다음 Part의 첫 장으로 넘어간다. */
(()=>{
const pane=document.getElementById('content'),nav=document.getElementById('chapNav');
if(!pane||!nav)return;
const esc=s=>s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

/* ---------- 1. 근거 표시 호버 ---------- */
const LEGEND=[['학위','학위 논문에 보고된 값'],['논문','논문에 보고된 값'],['학회','학회 발표에 보고된 값'],['특허','특허의 주장·실시예'],
 ['리뷰','교과서 수준의 정설'],['교과서','교과서 수준의 정설'],['통설','교과서 수준의 정설'],['계산','가정을 밝힌 교육용 계산'],
 ['현장','문헌으로 못 박지 못한 현장 통념. 자기 장비에서 확인해야 한다']];
let refs=new Map();
function keysOf(b){
 let t=b.textContent;const keys=[];
 t=t.replace(/S(\d\d)\s*[–-]\s*S(\d\d)/g,(_,a,z)=>{for(let i=+a;i<=+z;i++)keys.push('S'+String(i).padStart(2,'0'));return ' '});
 t=t.replace(/S\d\d/g,m=>{keys.push(m);return ' '});
 (t.match(/\d+/g)||[]).forEach(n=>keys.push('n'+(+n)));
 return keys;
}
function indexRefs(){
 refs=new Map();
 pane.querySelectorAll('li').forEach(li=>{const m=li.textContent.match(/^\s*\[(\d+)\]/);if(m&&!refs.has('n'+m[1]))refs.set('n'+m[1],{kind:'li',el:li})});
 pane.querySelectorAll('details.srcs table').forEach(tb=>{
  const heads=[...tb.querySelectorAll('thead th')].map(th=>th.textContent.trim());
  tb.querySelectorAll('tbody tr').forEach(tr=>{const id=tr.cells[0]?.textContent.trim();if(/^S\d\d$/.test(id)&&!refs.has(id))refs.set(id,{kind:'row',el:tr,heads})});
 });
 pane.querySelectorAll('.ev').forEach(b=>{if(keysOf(b).some(k=>refs.has(k))){b.classList.add('ev-linked');b.tabIndex=0}});
}
const plainLinks=h=>h.replace(/<a\b[^>]*data-ref[^>]*>(.*?)<\/a>/g,'$1');
function itemHTML(k){
 const r=refs.get(k);if(!r)return '';
 if(r.kind==='li')return `<div class="evtip-item"><span class="evtip-no">[${k.slice(1)}]</span>${plainLinks(r.el.innerHTML.replace(/^\s*\[\d+\]\s*/,''))}</div>`;
 const cell=name=>{const i=r.heads.indexOf(name);return i>=0?r.el.cells[i]||null:null};
 const main=cell('서지')||cell('내용')||cell('그림')||r.el.cells[1];
 const meta=[cell('유형'),cell('라이선스'),cell('확인')].filter(Boolean).map(c=>c.textContent.trim()).filter(Boolean).join(' · ');
 let note=cell('핵심 내용 · 수치')?.textContent.trim()||'';if(note.length>260)note=note.slice(0,258)+'…';
 return `<div class="evtip-item"><span class="evtip-no">${k}</span>${main?plainLinks(main.innerHTML):''}`+
  (meta?`<span class="evtip-meta">${esc(meta)}</span>`:'')+(note?`<span class="evtip-note">${esc(note)}</span>`:'')+'</div>';
}
function legendHTML(b){const t=b.textContent.trim(),w=LEGEND.find(([k])=>t.startsWith(k));return w?`<div class="evtip-item evtip-legend"><b>${esc(w[0])}</b> — ${esc(w[1])}</div>`:''}

const tip=document.createElement('div');tip.className='evtip';tip.id='evtip';tip.hidden=true;tip.setAttribute('role','tooltip');document.body.appendChild(tip);
let cur=null,pinned=false,showT=0,hideT=0;
function place(b){
 const r=b.getBoundingClientRect(),vw=window.innerWidth,vh=window.innerHeight;
 tip.style.left='0px';tip.style.top='0px';
 const w=tip.offsetWidth,h=tip.offsetHeight;
 const x=Math.min(Math.max(12,r.left+r.width/2-w/2),vw-w-12);
 let y=r.bottom+8;if(y+h>vh-12&&r.top-8-h>12)y=r.top-8-h;
 tip.style.left=x+'px';tip.style.top=Math.max(12,y)+'px';
}
function show(b){
 const html=keysOf(b).map(itemHTML).join('')||legendHTML(b);if(!html)return;
 if(cur&&cur!==b){cur.classList.remove('on');cur.removeAttribute('aria-describedby')}
 tip.innerHTML=html;tip.hidden=false;cur=b;b.classList.add('on');b.setAttribute('aria-describedby','evtip');place(b);
}
function hide(){clearTimeout(showT);tip.hidden=true;pinned=false;if(cur){cur.classList.remove('on');cur.removeAttribute('aria-describedby')}cur=null}
pane.addEventListener('mouseover',e=>{const b=e.target.closest('.ev');if(!b||pinned)return;clearTimeout(hideT);if(b===cur)return;clearTimeout(showT);showT=setTimeout(()=>show(b),110)});
pane.addEventListener('mouseout',e=>{const b=e.target.closest('.ev');if(!b||pinned)return;const to=e.relatedTarget;if(to&&(b.contains(to)||tip.contains(to)))return;clearTimeout(showT);hideT=setTimeout(hide,220)});
tip.addEventListener('mouseenter',()=>clearTimeout(hideT));
tip.addEventListener('mouseleave',()=>{if(!pinned)hideT=setTimeout(hide,220)});
pane.addEventListener('click',e=>{const b=e.target.closest('.ev');if(!b)return;clearTimeout(showT);if(cur===b&&pinned){hide();return}show(b);pinned=!tip.hidden});
pane.addEventListener('focusin',e=>{const b=e.target.closest('.ev.ev-linked');if(b&&!pinned)show(b)});
pane.addEventListener('focusout',e=>{if(e.target.closest('.ev')&&!pinned)hide()});
document.addEventListener('click',e=>{if(!tip.hidden&&!e.target.closest('.ev')&&!tip.contains(e.target))hide()});
document.addEventListener('keydown',e=>{if(e.key==='Escape')hide()});
window.addEventListener('scroll',()=>{if(tip.hidden||!cur)return;if(pinned)place(cur);else hide()},{passive:true});
window.addEventListener('resize',()=>{if(!tip.hidden&&cur)place(cur)});

/* ---------- 2. 다음 장 자동 넘김 ---------- */
const hint=document.createElement('div');hint.className='next-hint';hint.hidden=true;
hint.innerHTML='<button type="button"><span class="nh-label"></span><span class="nh-title"></span><span class="nh-how"></span><span class="nh-bar"><i></i></span></button>';
pane.insertAdjacentElement('afterend',hint);
const bar=hint.querySelector('.nh-bar i');
const NEED=260;
let nextId=null,acc=0,armed=false,going=false,lastWheel=0,decayT=0,ty=null;
const chapterButtons=()=>[...nav.querySelectorAll('button.chapter-link[data-ch]')];
const currentId=()=>nav.querySelector('button.chapter-link[aria-current="page"]')?.dataset.ch||(location.hash.match(/chapter=(\d\d-\d\d)/)||[])[1]||'00-01';
const partName=id=>nav.querySelector(`details[data-part="${id.slice(0,2)}"]>summary`)?.textContent.trim()||'PART '+id.slice(0,2);
const atBottom=()=>window.innerHeight+window.scrollY>=document.documentElement.scrollHeight-8;
function setBar(){bar.style.width=Math.min(100,acc/NEED*100)+'%'}
function reset(){acc=0;armed=false;setBar()}
function updateHint(){
 const list=chapterButtons(),id=currentId(),i=list.findIndex(b=>b.dataset.ch===id),nb=i>=0?list[i+1]:null;
 const lab=hint.querySelector('.nh-label'),tit=hint.querySelector('.nh-title'),how=hint.querySelector('.nh-how');
 nextId=nb?nb.dataset.ch:null;hint.hidden=false;reset();
 if(!nb){hint.classList.add('end');lab.textContent='마지막 장';tit.textContent='여기가 교과서의 끝이다.';how.textContent='';bar.parentNode.hidden=true;return}
 hint.classList.remove('end');bar.parentNode.hidden=false;
 const newPart=nextId.slice(0,2)!==id.slice(0,2),name=nb.querySelector('strong')?.textContent.trim()||nextId;
 lab.textContent=newPart?`다음 Part · ${partName(nextId)}`:`다음 장 · ${nextId}`;
 tit.textContent=newPart?`${nextId} · ${name}`:name;
 how.textContent='여기서 계속 내리거나 누르면 넘어간다.';
}
function go(){
 if(!nextId||going)return;going=true;reset();
 nav.querySelector(`button.chapter-link[data-ch="${nextId}"]`)?.click();
 setTimeout(()=>{going=false},500);
}
hint.querySelector('button').addEventListener('click',()=>{if(nextId)go()});
window.addEventListener('wheel',e=>{
 if(!nextId||e.ctrlKey||going)return;
 const now=performance.now(),gap=now-lastWheel;lastWheel=now;
 if(e.deltaY<=0||!atBottom()){reset();return}
 // 바닥에 닿게 만든 스크롤의 관성은 세지 않는다. 바닥에서 잠깐 멈췄다가 다시 내린 것부터 센다.
 if(!armed){if(gap<180)return;armed=true}
 const dy=e.deltaMode===1?e.deltaY*40:e.deltaMode===2?e.deltaY*window.innerHeight:e.deltaY;
 acc+=Math.min(dy,120);setBar();
 clearTimeout(decayT);decayT=setTimeout(()=>{acc=0;setBar()},700);
 if(acc>=NEED)go();
},{passive:true});
window.addEventListener('keydown',e=>{
 if(!nextId||going||e.altKey||e.ctrlKey||e.metaKey||e.shiftKey)return;
 if(!['ArrowDown','PageDown',' ','End'].includes(e.key))return;
 const t=e.target.closest?e.target:document.body;
 if(t.closest('input,textarea,select,[contenteditable]')||(e.key===' '&&t.closest('button,summary,a')))return;
 if(!atBottom()){reset();return}
 acc+=NEED/2;setBar();clearTimeout(decayT);decayT=setTimeout(()=>{acc=0;setBar()},1500);
 if(acc>=NEED)go();
});
window.addEventListener('touchstart',e=>{ty=(nextId&&!going&&e.touches.length===1&&atBottom())?e.touches[0].clientY:null;acc=0;setBar()},{passive:true});
window.addEventListener('touchmove',e=>{if(ty===null)return;acc=Math.max(0,(ty-e.touches[0].clientY)*1.6);setBar()},{passive:true});
window.addEventListener('touchend',()=>{if(ty!==null&&acc>=NEED)go();ty=null;acc=0;setBar()},{passive:true});

/* 장이 바뀔 때마다(#content를 통째로 바꾼다) 다시 맞춘다 */
let pend=0;
new MutationObserver(()=>{cancelAnimationFrame(pend);pend=requestAnimationFrame(()=>{hide();indexRefs();updateHint()})}).observe(pane,{childList:true});
indexRefs();updateHint();
})();
