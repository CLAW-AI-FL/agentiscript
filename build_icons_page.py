#!/usr/bin/env python3
"""Generate icons/index.html — the full icon library page."""
import json
from pathlib import Path

data = json.loads(Path('/Users/colin/seo/agentiscript/agentiscript.json').read_text())
icons = data['icons']
categories = data['categories']

# Build category filter buttons
cat_buttons = '<button class="filter-btn active" data-cat="all">All <span class="count">157</span></button>\n'
for cat in categories:
    slug = cat.lower().replace(' / ', '-').replace(' & ', '-').replace(' ', '-')
    count = sum(1 for ic in icons if ic['category_name'] == cat)
    cat_buttons += f'<button class="filter-btn" data-cat="{slug}">{cat} <span class="count">{count}</span></button>\n'

# Build icon cards
icon_cards = ''
for ic in icons:
    cat_slug = ic['category_name'].lower().replace(' / ', '-').replace(' & ', '-').replace(' ', '-')
    icon_cards += f'''<div class="icon-card" data-cat="{cat_slug}" data-name="{ic['concept'].lower()}" data-tags="{' '.join(ic['tags'])}">
  <div class="icon-img-wrap">
    <img src="../icons/{ic['slug']}.svg" alt="{ic['concept']}" loading="lazy" width="40" height="40">
  </div>
  <div class="icon-info">
    <div class="icon-name">{ic['concept']}</div>
    <div class="icon-cat-badge">{ic['category_name']}</div>
  </div>
  <div class="icon-actions">
    <a href="../icons/{ic['slug']}.svg" download="{ic['slug']}.svg" class="dl-btn" title="Download SVG">↓ SVG</a>
    <button class="copy-btn" data-slug="{ic['slug']}" title="Copy embed code">&lt;/&gt;</button>
  </div>
</div>
'''

HTML = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Icon Library — AgentiScript</title>
  <meta name="description" content="Browse 157 free SVG icons for the agentic economy. AI agents, blockchain, DeFi, quantum, defense, and more.">
  <link rel="icon" href="../icons/agentic-loop.svg" type="image/svg+xml">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-QYFEV9J581"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-QYFEV9J581');</script>
  <style>
    :root {{
      --gold: #9F792C; --gold-light: #C4992E; --gold-dim: #6B5220;
      --black: #000; --dark: #0A0A0A; --card: #111; --border: #1E1E1E;
      --white: #FFF; --gray: #888;
    }}
    * {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{ background:var(--black); color:var(--white); font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',system-ui,sans-serif; }}
    a {{ color:var(--gold); text-decoration:none; }}
    nav {{
      position:sticky; top:0; z-index:100;
      background:rgba(0,0,0,0.92); backdrop-filter:blur(12px);
      border-bottom:1px solid var(--border);
      padding:0 2rem; display:flex; align-items:center; justify-content:space-between; height:56px;
    }}
    .nav-brand {{ font-size:1.1rem; font-weight:700; color:var(--gold); }}
    .nav-links {{ display:flex; gap:2rem; }}
    .nav-links a {{ color:var(--gray); font-size:0.9rem; transition:color 0.2s; }}
    .nav-links a:hover {{ color:var(--white); }}

    .hero {{ max-width:800px; margin:0 auto; padding:4rem 2rem 2rem; }}
    h1 {{ font-size:clamp(1.8rem,5vw,2.8rem); font-weight:800; letter-spacing:-0.03em; color:var(--white); margin-bottom:0.5rem; }}
    h1 span {{ color:var(--gold); }}
    .hero-sub {{ color:var(--gray); font-size:1rem; margin-bottom:2rem; }}

    .search-bar {{ display:flex; gap:1rem; margin-bottom:2rem; max-width:600px; }}
    .search-bar input {{
      flex:1; background:var(--card); border:1px solid var(--border);
      color:var(--white); padding:0.75rem 1rem; border-radius:8px; font-size:0.95rem; outline:none;
    }}
    .search-bar input:focus {{ border-color:var(--gold); }}

    .filters {{
      display:flex; flex-wrap:wrap; gap:0.5rem;
      padding:0 2rem; max-width:1200px; margin:0 auto 2rem;
    }}
    .filter-btn {{
      background:var(--card); border:1px solid var(--border);
      color:var(--gray); padding:0.4rem 0.9rem; border-radius:100px;
      font-size:0.8rem; cursor:pointer; transition:all 0.2s;
    }}
    .filter-btn:hover {{ border-color:var(--gold-dim); color:var(--white); }}
    .filter-btn.active {{ background:var(--gold); color:var(--black); border-color:var(--gold); font-weight:700; }}
    .filter-btn .count {{ opacity:0.7; }}

    .grid-wrap {{ max-width:1200px; margin:0 auto; padding:0 2rem 4rem; }}
    .result-count {{ color:var(--gray); font-size:0.85rem; margin-bottom:1rem; }}

    .icons-grid {{
      display:grid; grid-template-columns:repeat(auto-fill,minmax(200px,1fr));
      gap:1px; background:var(--border); border:1px solid var(--border); border-radius:12px; overflow:hidden;
    }}
    .icon-card {{
      background:var(--dark); padding:1.5rem 1.25rem;
      display:flex; flex-direction:column; gap:0.75rem;
      transition:background 0.15s;
    }}
    .icon-card:hover {{ background:var(--card); }}
    .icon-card.hidden {{ display:none; }}
    .icon-img-wrap {{
      width:48px; height:48px;
      display:flex; align-items:center; justify-content:center;
    }}
    .icon-img-wrap img {{ width:40px; height:40px; }}
    .icon-name {{ font-size:0.85rem; font-weight:600; color:var(--white); }}
    .icon-cat-badge {{
      font-size:0.65rem; color:var(--gold);
      background:rgba(159,121,44,0.12); border:1px solid rgba(159,121,44,0.2);
      padding:0.15rem 0.5rem; border-radius:100px; display:inline-block;
    }}
    .icon-actions {{ display:flex; gap:0.5rem; margin-top:0.25rem; }}
    .dl-btn, .copy-btn {{
      font-size:0.75rem; padding:0.3rem 0.6rem; border-radius:6px;
      cursor:pointer; transition:all 0.2s; border:1px solid var(--border);
    }}
    .dl-btn {{ background:transparent; color:var(--gold); text-decoration:none; }}
    .dl-btn:hover {{ background:var(--gold); color:var(--black); }}
    .copy-btn {{ background:transparent; color:var(--gray); }}
    .copy-btn:hover {{ border-color:var(--gold-dim); color:var(--white); }}

    .no-results {{ text-align:center; padding:4rem; color:var(--gray); display:none; }}

    /* Toast */
    .toast {{
      position:fixed; bottom:2rem; left:50%; transform:translateX(-50%) translateY(100px);
      background:var(--gold); color:var(--black); padding:0.75rem 1.5rem;
      border-radius:8px; font-size:0.9rem; font-weight:600;
      transition:transform 0.3s; z-index:999; pointer-events:none;
    }}
    .toast.show {{ transform:translateX(-50%) translateY(0); }}

    footer {{
      border-top:1px solid var(--border); padding:2rem;
      display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;
      max-width:1200px; margin:0 auto;
    }}
    .footer-links {{ display:flex; gap:1.5rem; }}
    .footer-links a {{ font-size:0.85rem; color:var(--gray); }}
    .footer-copy {{ font-size:0.8rem; color:var(--gold-dim); }}

    @media(max-width:600px) {{ .nav-links {{ display:none; }} }}
  </style>
</head>
<body>
<nav>
  <a class="nav-brand" href="/">AgentiScript</a>
  <div class="nav-links">
    <a href="/icons/" style="color:var(--white)">Browse Icons</a>
    <a href="/docs/">Docs</a>
    <a href="/store/">Pro Pack</a>
    <a href="/submit/">Submit</a>
    <a href="https://github.com/CLAW-AI-FL/agentiscript" target="_blank">GitHub</a>
  </div>
</nav>

<div class="hero">
  <h1>Icon Library <span>✦</span></h1>
  <p class="hero-sub">Browse the language. Take what you need. It's free. <strong style="color:var(--gold)">157 icons</strong> across 10 categories.</p>
  <div class="search-bar">
    <input type="text" id="search" placeholder="Search concepts... try 'oracle' or 'quantum'" autocomplete="off">
  </div>
</div>

<div class="filters">
{cat_buttons}
</div>

<div class="grid-wrap">
  <div class="result-count" id="result-count">Showing all 157 icons</div>
  <div class="icons-grid" id="icons-grid">
{icon_cards}
  </div>
  <div class="no-results" id="no-results">
    No icons found for that search. <a href="/submit/">Submit a concept →</a>
  </div>
</div>

<footer>
  <div class="footer-links">
    <a href="/">Home</a>
    <a href="/docs/">Docs</a>
    <a href="/store/">Pro Pack</a>
    <a href="/submit/">Submit a Concept</a>
    <a href="https://github.com/CLAW-AI-FL/agentiscript" target="_blank">GitHub</a>
  </div>
  <div class="footer-copy">AgentiScript · CC0 · Free forever.</div>
</footer>

<div class="toast" id="toast">Copied to clipboard!</div>

<script>
const cards = document.querySelectorAll('.icon-card');
const searchInput = document.getElementById('search');
const filterBtns = document.querySelectorAll('.filter-btn');
const resultCount = document.getElementById('result-count');
const noResults = document.getElementById('no-results');

let currentCat = 'all';
let currentSearch = '';

function slugify(s) {{
  return s.toLowerCase().replace(/ \\/ /g,'-').replace(/ & /g,'-').replace(/ /g,'-');
}}

function applyFilters() {{
  let visible = 0;
  cards.forEach(card => {{
    const cat = card.dataset.cat;
    const name = card.dataset.name;
    const tags = card.dataset.tags;
    const matchesCat = currentCat === 'all' || cat === currentCat;
    const matchesSearch = !currentSearch || name.includes(currentSearch) || tags.includes(currentSearch);
    if (matchesCat && matchesSearch) {{
      card.classList.remove('hidden');
      visible++;
    }} else {{
      card.classList.add('hidden');
    }}
  }});
  resultCount.textContent = visible === 157 ? 'Showing all 157 icons' : `Showing ${{visible}} of 157 icons`;
  noResults.style.display = visible === 0 ? 'block' : 'none';
}}

searchInput.addEventListener('input', e => {{
  currentSearch = e.target.value.toLowerCase();
  applyFilters();
}});

filterBtns.forEach(btn => {{
  btn.addEventListener('click', () => {{
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentCat = btn.dataset.cat;
    applyFilters();
  }});
}});

// Copy embed code
document.querySelectorAll('.copy-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    const slug = btn.dataset.slug;
    const code = `<img src="https://agentiscript.com/icons/${{slug}}.svg" alt="${{slug}}" width="24" height="24">`;
    navigator.clipboard.writeText(code).then(() => {{
      const toast = document.getElementById('toast');
      toast.textContent = 'Embed code copied!';
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 2500);
    }});
  }});
}});
</script>
</body>
</html>'''

Path('/Users/colin/seo/agentiscript/icons/index.html').write_text(HTML, encoding='utf-8')
print(f"icons/index.html generated ({len(HTML)} chars)")
