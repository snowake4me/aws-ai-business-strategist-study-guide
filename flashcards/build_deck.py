#!/usr/bin/env python3
"""Generate deck.html from deck.md. Re-run after editing the deck.

Card format in deck.md:
    ## Section name
    **Question text**
    → *Answer text* · `source`
"""
import html, json, re, pathlib

here = pathlib.Path(__file__).parent
md = (here / "deck.md").read_text(encoding="utf-8")

cards, section = [], "Untitled"
lines = md.splitlines()
for i, line in enumerate(lines):
    if line.startswith("## "):
        section = line[3:].strip()
    elif line.startswith("**") and i + 1 < len(lines) and lines[i + 1].startswith("→"):
        q = line.strip().strip("*").strip()
        a_line = lines[i + 1][1:].strip()
        m = re.match(r"\*(.+?)\*\s*(?:·\s*(.*))?$", a_line)
        if m:
            a, src = m.group(1).strip(), (m.group(2) or "").strip().strip("`")
        else:
            a, src = a_line, ""
        cards.append({"s": section, "q": q, "a": a, "src": src})

def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    return s

for c in cards:
    c["q"], c["a"] = inline(c["q"]), inline(c["a"])

sections = sorted({c["s"] for c in cards}, key=lambda s: [c["s"] for c in cards].index(s))

page = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AIB-C01 Flashcards</title>
<style>
:root{--ink:#14181D;--ink-2:#48525E;--ink-3:#7C8794;--paper:#FCFCFA;--panel:#fff;--rule:#DCE0E4;--rule-2:#EDEFF1;
--deep:#26426B;--deep-tint:#EEF2F8;--ok:#2C6E52;--ok-tint:#EAF3EE;--no:#A63F35;--no-tint:#FAEEEC;
--mono:ui-monospace,SFMono-Regular,Menlo,monospace;--sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
--serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.55 var(--sans)}
.wrap{max-width:760px;margin:0 auto;padding:24px 20px 80px}
h1{font:600 22px/1.2 var(--serif);margin:0 0 4px}.sub{font:11px/1 var(--mono);color:var(--ink-3);text-transform:uppercase;letter-spacing:.09em;margin-bottom:22px}
.card{background:var(--panel);border:1px solid var(--rule);border-radius:8px;padding:26px;margin:14px 0;min-height:180px}
.eyebrow{font:11px/1 var(--mono);color:var(--ink-3);text-transform:uppercase;letter-spacing:.09em;margin-bottom:10px}
.q{font:500 20px/1.4 var(--serif)}.a{margin-top:18px;padding-top:16px;border-top:1px solid var(--rule-2);color:var(--ink-2)}
.a b{color:var(--ink)}.src{font:12px var(--mono);color:var(--ink-3);margin-top:8px}
.row{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}
button{font:inherit;cursor:pointer;border-radius:5px;padding:10px 18px;border:1px solid var(--deep);background:var(--deep);color:#fff;font-weight:500}
button.ghost{background:transparent;color:var(--deep)}button.ok{background:var(--ok);border-color:var(--ok)}button.no{background:var(--no);border-color:var(--no)}
button:disabled{opacity:.4;cursor:not-allowed}
.meter{height:3px;background:var(--rule-2);margin:10px 0 18px}.meter i{display:block;height:3px;background:var(--deep);width:0;transition:width .2s}
.stats{font:13px var(--mono);color:var(--ink-3)}
label{display:inline-flex;gap:6px;align-items:center;margin:4px 14px 4px 0;font-size:14px}
.missed{background:var(--no-tint);border-left:3px solid var(--no);padding:12px 16px;border-radius:0 5px 5px 0;margin:10px 0}
.missed .q{font-size:16px}
kbd{font:12px var(--mono);border:1px solid var(--rule);border-radius:3px;padding:1px 5px;color:var(--ink-2)}
[hidden]{display:none!important}
</style></head><body><div class="wrap">
<h1>AIB-C01 Flashcards</h1><div class="sub">__N__ cards · built from deck.md</div>

<div id="setup" class="card">
  <div class="eyebrow">Sections</div>
  <div id="secs"></div>
  <div class="row" style="margin-top:18px">
    <button id="start">Start (shuffled)</button>
    <button id="startOrd" class="ghost">Start (deck order)</button>
  </div>
  <p class="stats" style="margin-top:16px"><kbd>space</kbd> reveal · <kbd>1</kbd> got it · <kbd>2</kbd> missed</p>
</div>

<div id="run" hidden>
  <div class="meter"><i id="bar"></i></div>
  <div class="card">
    <div class="eyebrow" id="sec"></div>
    <div class="q" id="q"></div>
    <div class="a" id="a" hidden><div id="atext"></div><div class="src" id="src"></div></div>
  </div>
  <div class="row">
    <button id="reveal">Reveal</button>
    <button id="got" class="ok" hidden>Got it</button>
    <button id="miss" class="no" hidden>Missed</button>
  </div>
  <p class="stats" id="prog"></p>
</div>

<div id="done" hidden>
  <div class="card">
    <div class="eyebrow">Result</div>
    <div class="q" id="score"></div>
    <div id="missedList" style="margin-top:16px"></div>
    <div class="row"><button id="again" class="no" hidden>Drill the missed cards</button><button id="reset" class="ghost">Back to setup</button></div>
  </div>
</div>
</div>
<script>
const CARDS=__CARDS__, SECTIONS=__SECTIONS__;
const $=id=>document.getElementById(id);
let deck=[],i=0,got=0,missed=[],revealed=false;
SECTIONS.forEach((s,k)=>{const l=document.createElement('label');l.innerHTML=`<input type="checkbox" checked data-s="${k}"> ${s} <span class="stats">(${CARDS.filter(c=>c.s===s).length})</span>`;$('secs').appendChild(l);});
function chosen(){const on=[...document.querySelectorAll('#secs input')].filter(x=>x.checked).map(x=>SECTIONS[x.dataset.s]);return CARDS.filter(c=>on.includes(c.s));}
function shuffle(a){for(let j=a.length-1;j>0;j--){const k=Math.floor(Math.random()*(j+1));[a[j],a[k]]=[a[k],a[j]];}return a;}
function begin(cards){deck=cards;i=0;got=0;missed=[];$('setup').hidden=true;$('done').hidden=true;$('run').hidden=false;show();}
function show(){if(i>=deck.length)return finish();const c=deck[i];revealed=false;$('sec').textContent=c.s;$('q').innerHTML=c.q;$('atext').innerHTML=c.a;$('src').textContent=c.src;$('a').hidden=true;$('reveal').hidden=false;$('got').hidden=true;$('miss').hidden=true;$('bar').style.width=(100*i/deck.length)+'%';$('prog').textContent=`${i+1} / ${deck.length} · got ${got} · missed ${missed.length}`;}
function reveal(){if(revealed)return;revealed=true;$('a').hidden=false;$('reveal').hidden=true;$('got').hidden=false;$('miss').hidden=false;}
function mark(ok){if(!revealed)return;if(ok)got++;else missed.push(deck[i]);i++;show();}
function finish(){$('run').hidden=true;$('done').hidden=false;$('score').textContent=`${got} / ${deck.length} got it`;const L=$('missedList');L.innerHTML='';missed.forEach(c=>{const d=document.createElement('div');d.className='missed';d.innerHTML=`<div class="q">${c.q}</div><div class="a" style="margin-top:8px;padding-top:8px">${c.a}</div><div class="src">${c.src}</div>`;L.appendChild(d);});$('again').hidden=missed.length===0;}
$('start').onclick=()=>begin(shuffle(chosen()));$('startOrd').onclick=()=>begin(chosen());
$('reveal').onclick=reveal;$('got').onclick=()=>mark(true);$('miss').onclick=()=>mark(false);
$('again').onclick=()=>begin(shuffle(missed.slice()));$('reset').onclick=()=>{$('done').hidden=true;$('setup').hidden=false;};
document.addEventListener('keydown',e=>{if($('run').hidden)return;if(e.key===' '){e.preventDefault();reveal();}else if(e.key==='1')mark(true);else if(e.key==='2')mark(false);});
</script></body></html>
"""
out = (page.replace("__N__", str(len(cards)))
           .replace("__CARDS__", json.dumps(cards, ensure_ascii=False))
           .replace("__SECTIONS__", json.dumps(sections, ensure_ascii=False)))
(here / "deck.html").write_text(out, encoding="utf-8")
print(f"deck.html: {len(cards)} cards across {len(sections)} sections")
