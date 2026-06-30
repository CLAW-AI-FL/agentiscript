#!/usr/bin/env python3
"""
Generate AgentiScript icons for all new concepts from Wikipedia AI + Ethereum glossaries.
"""

import json
import re
import os
import math
from pathlib import Path
from html.parser import HTMLParser

ICONS_DIR = Path('/Users/colin/seo/agentiscript/icons')

# --- Gather existing icons ---
existing = {f.stem for f in ICONS_DIR.glob('*.json')}
print(f"Existing icons: {len(existing)}")

# ─────────────────────────────────────────────────────────
# 1. Parse Wikipedia AI glossary (HTML → dt terms)
# ─────────────────────────────────────────────────────────
class DTParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_dt = False
        self.depth = 0
        self.terms = []
        self._buf = []

    def handle_starttag(self, tag, attrs):
        if tag == 'dt':
            self.in_dt = True
            self.depth = 1
            self._buf = []
        elif self.in_dt:
            self.depth += 1

    def handle_endtag(self, tag):
        if self.in_dt:
            if tag == 'dt':
                self.depth -= 1
                if self.depth == 0:
                    self.in_dt = False
                    term = ''.join(self._buf).strip()
                    if term:
                        self.terms.append(term)
            else:
                self.depth -= 1

    def handle_data(self, data):
        if self.in_dt:
            self._buf.append(data)

with open('/tmp/wiki_ai.json') as f:
    wiki_data = json.load(f)
html = wiki_data['parse']['text']['*']

parser = DTParser()
parser.feed(html)
ai_raw_terms = parser.terms
print(f"Raw AI terms from Wikipedia: {len(ai_raw_terms)}")

def to_slug(term):
    """Convert a term to a URL-safe slug."""
    t = term.lower()
    t = re.sub(r'[^\w\s-]', '', t)
    t = re.sub(r'[\s_]+', '-', t)
    t = re.sub(r'-+', '-', t)
    t = t.strip('-')
    return t

def to_label(slug):
    return ' '.join(w.capitalize() for w in slug.replace('-', ' ').split())

ai_slugs = []
for t in ai_raw_terms:
    s = to_slug(t)
    if s and len(s) >= 3:
        ai_slugs.append((s, t.strip()))

# ─────────────────────────────────────────────────────────
# 2. Parse Ethereum glossary (markdown → GlossaryDefinition terms)
# ─────────────────────────────────────────────────────────
with open('/tmp/eth_glossary.md') as f:
    md = f.read()

eth_raw = re.findall(r'<GlossaryDefinition term="([^"]+)"', md)
print(f"Raw ETH terms from GitHub: {len(eth_raw)}")

eth_slugs = [(to_slug(t), t) for t in eth_raw if len(to_slug(t)) >= 2]

# ─────────────────────────────────────────────────────────
# 3. Merge & filter new concepts
# ─────────────────────────────────────────────────────────
all_concepts = {}  # slug -> (label, category)

for slug, raw in ai_slugs:
    if slug not in existing and slug not in all_concepts:
        all_concepts[slug] = (to_label(slug), 'ai')

for slug, raw in eth_slugs:
    if slug not in existing and slug not in all_concepts:
        all_concepts[slug] = (to_label(slug), 'blockchain')

print(f"New concepts to generate: {len(all_concepts)}")

# ─────────────────────────────────────────────────────────
# 4. SVG generator — distinct icons per concept
# ─────────────────────────────────────────────────────────
COLORS = {
    'ai':         '#9F792C',   # golden (matches existing AI icons)
    'blockchain': '#3B7DD8',   # blue for blockchain/ethereum
}

def make_svg_ai(slug, label):
    """Generate contextually-appropriate SVG for AI concepts."""
    color = COLORS['ai']
    words = slug.split('-')

    # Map keywords to specific SVG shapes
    kw = set(words)

    if 'neural' in kw or 'network' in kw and 'neural' in slug:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="4" cy="6" r="1.5"/><circle cx="4" cy="12" r="1.5"/><circle cx="4" cy="18" r="1.5"/>
<circle cx="12" cy="4" r="1.5"/><circle cx="12" cy="10" r="1.5"/><circle cx="12" cy="16" r="1.5"/><circle cx="12" cy="20" r="1.5"/>
<circle cx="20" cy="8" r="1.5"/><circle cx="20" cy="14" r="1.5"/>
<line x1="5.5" y1="6" x2="10.5" y2="4"/><line x1="5.5" y1="6" x2="10.5" y2="10"/><line x1="5.5" y1="6" x2="10.5" y2="16"/>
<line x1="5.5" y1="12" x2="10.5" y2="4"/><line x1="5.5" y1="12" x2="10.5" y2="10"/><line x1="5.5" y1="12" x2="10.5" y2="20"/>
<line x1="5.5" y1="18" x2="10.5" y2="10"/><line x1="5.5" y1="18" x2="10.5" y2="16"/><line x1="5.5" y1="18" x2="10.5" y2="20"/>
<line x1="13.5" y1="4" x2="18.5" y2="8"/><line x1="13.5" y1="10" x2="18.5" y2="8"/><line x1="13.5" y1="16" x2="18.5" y2="14"/>
<line x1="13.5" y1="20" x2="18.5" y2="14"/>
</svg>'''

    if 'tree' in kw or 'decision' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="3" r="1.5"/>
<line x1="12" y1="4.5" x2="7" y2="9.5"/>
<line x1="12" y1="4.5" x2="17" y2="9.5"/>
<circle cx="7" cy="11" r="1.5"/><circle cx="17" cy="11" r="1.5"/>
<line x1="7" y1="12.5" x2="4" y2="17.5"/>
<line x1="7" y1="12.5" x2="10" y2="17.5"/>
<line x1="17" y1="12.5" x2="14" y2="17.5"/>
<line x1="17" y1="12.5" x2="20" y2="17.5"/>
<circle cx="4" cy="19" r="1.5"/><circle cx="10" cy="19" r="1.5"/><circle cx="14" cy="19" r="1.5"/><circle cx="20" cy="19" r="1.5"/>
</svg>'''

    if 'gradient' in kw or 'descent' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<path d="M3 20 Q6 18 8 14 Q10 10 12 12 Q14 14 16 8 Q18 4 21 4"/>
<circle cx="21" cy="4" r="1.5"/>
<line x1="17" y1="14" x2="21" y2="14"/><line x1="21" y1="14" x2="21" y2="10"/>
<polyline points="18,17 21,14 18,11" fill="none"/>
</svg>'''

    if 'cluster' in kw or 'clustering' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="7" cy="7" r="2"/><circle cx="5" cy="11" r="1.5"/><circle cx="9" cy="12" r="1.5"/>
<circle cx="17" cy="8" r="2"/><circle cx="15" cy="12" r="1.5"/><circle cx="19" cy="13" r="1.5"/>
<circle cx="11" cy="18" r="2"/><circle cx="8" cy="19" r="1.5"/><circle cx="14" cy="19" r="1.5"/>
<ellipse cx="7" cy="10" rx="4" ry="5" stroke-dasharray="2,2"/>
<ellipse cx="17" cy="11" rx="4" ry="5" stroke-dasharray="2,2"/>
<ellipse cx="11" cy="19" rx="4" ry="3" stroke-dasharray="2,2"/>
</svg>'''

    if 'graph' in kw or 'knowledge' in kw and 'graph' in slug:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="5" r="2"/><circle cx="5" cy="17" r="2"/><circle cx="19" cy="17" r="2"/><circle cx="12" cy="13" r="2"/>
<line x1="12" y1="7" x2="12" y2="11"/><line x1="6.7" y1="15.7" x2="10.7" y2="13.7"/>
<line x1="17.3" y1="15.7" x2="13.3" y2="13.7"/><line x1="6.7" y1="16.3" x2="10.3" y2="7.3"/>
<line x1="17.3" y1="16.3" x2="13.7" y2="7.3"/>
</svg>'''

    if 'transform' in kw or 'attention' in kw or 'transformer' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="2" y="2" width="4" height="4" rx="1"/>
<rect x="10" y="2" width="4" height="4" rx="1"/>
<rect x="18" y="2" width="4" height="4" rx="1"/>
<rect x="6" y="10" width="4" height="4" rx="1"/>
<rect x="14" y="10" width="4" height="4" rx="1"/>
<rect x="10" y="18" width="4" height="4" rx="1"/>
<line x1="4" y1="6" x2="7" y2="10"/><line x1="12" y1="6" x2="8" y2="10"/><line x1="12" y1="6" x2="15" y2="10"/>
<line x1="20" y1="6" x2="16" y2="10"/><line x1="8" y1="14" x2="11" y2="18"/><line x1="16" y1="14" x2="13" y2="18"/>
</svg>'''

    if 'convolut' in slug or 'cnn' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="2" y="2" width="10" height="10" rx="1"/>
<rect x="5" y="5" width="4" height="4" rx="0.5" stroke-dasharray="2,1"/>
<rect x="12" y="7" width="8" height="8" rx="1"/>
<rect x="19" y="14" width="4" height="4" rx="1"/>
<line x1="12" y1="7" x2="7" y2="7"/><line x1="12" y1="15" x2="7" y2="12"/>
<line x1="19" y1="14" x2="16" y2="11"/>
</svg>'''

    if 'reinforcement' in kw or 'reward' in kw and 'reinforc' in slug:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="12" r="4"/>
<path d="M12 8 A4 4 0 0 1 16 12" stroke-dasharray="2,1"/>
<polyline points="16,9 16,12 13,12" fill="none"/>
<circle cx="12" cy="12" r="9" stroke-dasharray="3,3"/>
<line x1="12" y1="2" x2="12" y2="4"/><line x1="20" y1="6" x2="18.5" y2="7.5"/>
<line x1="22" y1="12" x2="20" y2="12"/><text x="9.5" y="14" font-size="5" fill="{color}" stroke="none">R</text>
</svg>'''

    if 'recurrent' in kw or 'lstm' in kw or 'rnn' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="8" y="8" width="8" height="8" rx="2"/>
<path d="M16 10 Q20 10 20 6 Q20 2 16 2 Q12 2 12 4"/>
<polyline points="12,3 12,6 15,6" fill="none"/>
<line x1="8" y1="12" x2="4" y2="12"/><line x1="16" y1="12" x2="20" y2="12"/>
<line x1="12" y1="16" x2="12" y2="20"/>
</svg>'''

    if 'bayes' in kw or 'bayesian' in kw or 'probab' in slug:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<path d="M3 20 Q5 5 12 5 Q19 5 21 20"/>
<line x1="3" y1="20" x2="21" y2="20"/>
<line x1="12" y1="5" x2="12" y2="20" stroke-dasharray="2,2"/>
<line x1="7" y1="12" x2="17" y2="12" stroke-dasharray="2,2"/>
<circle cx="12" cy="5" r="1.5"/>
</svg>'''

    if 'optim' in slug or 'optimiz' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<path d="M3 17 Q5 14 7 16 Q9 18 11 10 Q13 3 15 8 Q17 12 19 10 Q21 8 21 9"/>
<circle cx="13" cy="6" r="1.5" fill="{color}"/>
<line x1="13" y1="7.5" x2="13" y2="20" stroke-dasharray="2,2"/>
</svg>'''

    if 'embed' in kw or 'vector' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<line x1="2" y1="20" x2="22" y2="20"/><line x1="2" y1="20" x2="2" y2="4"/>
<line x1="2" y1="20" x2="8" y2="10"/><line x1="2" y1="20" x2="13" y2="7"/>
<line x1="2" y1="20" x2="18" y2="12"/>
<circle cx="8" cy="10" r="1.5"/><circle cx="13" cy="7" r="1.5"/><circle cx="18" cy="12" r="1.5"/>
<polyline points="7,10 9,10" fill="none"/><polyline points="12,7 14,7" fill="none"/>
</svg>'''

    if 'classif' in slug or 'classif' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="7" cy="8" r="2"/><circle cx="6" cy="14" r="2"/><circle cx="8" cy="18" r="2"/>
<circle cx="17" cy="6" r="2"/><circle cx="18" cy="11" r="2"/><circle cx="16" cy="16" r="2"/>
<line x1="11" y1="2" x2="11" y2="22" stroke-dasharray="3,2"/>
</svg>'''

    if 'autoencod' in slug or 'latent' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="2" y="6" width="4" height="12" rx="1"/>
<rect x="10" y="9" width="4" height="6" rx="1"/>
<rect x="18" y="6" width="4" height="12" rx="1"/>
<line x1="6" y1="9" x2="10" y2="10"/><line x1="6" y1="12" x2="10" y2="12"/><line x1="6" y1="15" x2="10" y2="14"/>
<line x1="14" y1="10" x2="18" y2="9"/><line x1="14" y1="12" x2="18" y2="12"/><line x1="14" y1="14" x2="18" y2="15"/>
</svg>'''

    if 'generat' in kw or 'gan' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="2" y="8" width="6" height="8" rx="1"/>
<rect x="16" y="8" width="6" height="8" rx="1"/>
<path d="M8 12 L11 12 M13 12 L16 12" stroke-dasharray="1,1"/>
<path d="M11 10 L13 12 L11 14" fill="none"/>
<circle cx="12" cy="12" r="1"/>
</svg>'''

    if 'regress' in slug:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<line x1="3" y1="21" x2="3" y2="3"/><line x1="3" y1="21" x2="21" y2="21"/>
<circle cx="5" cy="17" r="1"/><circle cx="8" cy="14" r="1"/><circle cx="11" cy="12" r="1"/>
<circle cx="14" cy="10" r="1"/><circle cx="17" cy="7" r="1"/><circle cx="20" cy="5" r="1"/>
<line x1="4" y1="18" x2="21" y2="4" stroke-dasharray="2,1"/>
</svg>'''

    if 'entrop' in kw or 'cross-entrop' in slug or 'loss' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<line x1="3" y1="3" x2="3" y2="21"/><line x1="3" y1="21" x2="21" y2="21"/>
<path d="M3 5 Q8 5 10 12 Q12 19 17 19 Q20 19 21 17"/>
<path d="M3 19 Q6 3 12 3 Q18 3 21 10" stroke-dasharray="2,2"/>
</svg>'''

    if 'natural' in kw and 'language' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="2" y="4" width="20" height="14" rx="2"/>
<line x1="6" y1="9" x2="18" y2="9"/><line x1="6" y1="13" x2="14" y2="13"/>
<polyline points="2,22 6,18 18,18 22,22" fill="none"/>
</svg>'''

    if 'support' in kw and 'vector' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<line x1="2" y1="18" x2="22" y2="6"/>
<circle cx="6" cy="6" r="1.5"/><circle cx="8" cy="9" r="1.5" fill="{color}"/>
<circle cx="16" cy="15" r="1.5" fill="{color}"/><circle cx="18" cy="18" r="1.5"/>
<line x1="2" y1="14" x2="22" y2="2" stroke-dasharray="3,2"/>
<line x1="2" y1="22" x2="22" y2="10" stroke-dasharray="3,2"/>
</svg>'''

    if 'semantic' in kw or 'meaning' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="12" r="4"/>
<circle cx="12" cy="12" r="8" stroke-dasharray="2,2"/>
<line x1="12" y1="4" x2="12" y2="8"/><line x1="16" y1="5" x2="14" y2="9"/>
<line x1="19" y1="8" x2="15.5" y2="10"/>
<line x1="12" y1="16" x2="12" y2="20"/><line x1="8" y1="19" x2="10" y2="15"/>
</svg>'''

    if 'predict' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<polyline points="3,18 7,11 10,15 14,7 17,10 21,4"/>
<circle cx="21" cy="4" r="1.5" fill="{color}"/>
<line x1="17" y1="4" x2="21" y2="4"/><line x1="21" y1="4" x2="21" y2="8"/>
</svg>'''

    if 'search' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="10" cy="10" r="7"/>
<line x1="15" y1="15" x2="21" y2="21"/>
<line x1="7" y1="10" x2="13" y2="10"/><line x1="10" y1="7" x2="10" y2="13"/>
</svg>'''

    if 'plan' in kw or 'planning' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="3" y="4" width="18" height="17" rx="1"/>
<line x1="3" y1="8" x2="21" y2="8"/>
<line x1="7" y1="4" x2="7" y2="8"/><line x1="17" y1="4" x2="17" y2="8"/>
<line x1="7" y1="12" x2="17" y2="12"/><line x1="7" y1="15" x2="14" y2="15"/>
<circle cx="18" cy="18" r="3"/>
<line x1="17" y1="18" x2="19" y2="18"/><line x1="18" y1="17" x2="18" y2="19"/>
</svg>'''

    if 'percept' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="5" cy="8" r="2"/><circle cx="5" cy="16" r="2"/>
<circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/>
<circle cx="19" cy="12" r="2"/>
<line x1="7" y1="8" x2="10" y2="5"/><line x1="7" y1="8" x2="10" y2="12"/>
<line x1="7" y1="16" x2="10" y2="12"/><line x1="7" y1="16" x2="10" y2="19"/>
<line x1="14" y1="5" x2="17" y2="12"/><line x1="14" y1="12" x2="17" y2="12"/><line x1="14" y1="19" x2="17" y2="12"/>
</svg>'''

    if 'fuzzy' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<path d="M3 18 Q7 4 12 4 Q17 4 21 18"/>
<path d="M6 18 Q8 8 12 8 Q16 8 18 18" stroke-dasharray="2,1"/>
<path d="M8 18 Q9 12 12 12 Q15 12 16 18" stroke-dasharray="1,2"/>
<line x1="3" y1="18" x2="21" y2="18"/>
</svg>'''

    if 'markov' in kw or 'mdp' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="5" cy="12" r="2.5"/>
<circle cx="12" cy="5" r="2.5"/>
<circle cx="19" cy="12" r="2.5"/>
<circle cx="12" cy="19" r="2.5"/>
<line x1="7" y1="10.5" x2="10" y2="7"/><line x1="14" y1="7" x2="17" y2="10.5"/>
<line x1="17" y1="13.5" x2="14" y2="17"/><line x1="10" y1="17" x2="7" y2="13.5"/>
<path d="M5 9.5 Q5 5 12 5" stroke-dasharray="2,1"/>
</svg>'''

    if 'featur' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="2" y="2" width="20" height="20" rx="2"/>
<line x1="2" y1="7" x2="22" y2="7"/>
<line x1="8" y1="2" x2="8" y2="22"/>
<circle cx="5" cy="12" r="1"/><circle cx="5" cy="17" r="1"/>
<line x1="10" y1="10" x2="20" y2="10"/><line x1="10" y1="15" x2="18" y2="15"/>
</svg>'''

    # Default fallback: minimal unique icon based on slug hash
    h = sum(ord(c) * i for i, c in enumerate(slug, 1)) % 6
    icons = [
        f'<circle cx="12" cy="12" r="8"/><line x1="12" y1="4" x2="12" y2="20"/><line x1="4" y1="12" x2="20" y2="12"/>',
        f'<polygon points="12,3 21,20 3,20"/><line x1="12" y1="10" x2="12" y2="15"/><circle cx="12" cy="17" r="1"/>',
        f'<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M9 12 L11 14 L15 10"/>',
        f'<circle cx="12" cy="12" r="8"/><path d="M9 9 Q12 6 15 9 Q18 12 15 15 Q12 18 9 15 Q6 12 9 9"/>',
        f'<path d="M4 20 L12 4 L20 20"/><line x1="7" y1="14" x2="17" y2="14"/>',
        f'<line x1="4" y1="4" x2="20" y2="20"/><line x1="20" y1="4" x2="4" y2="20"/><circle cx="12" cy="12" r="5"/>',
    ]
    body = icons[h]
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">\n{body}\n</svg>'


def make_svg_blockchain(slug, label):
    """Generate contextually-appropriate SVG for blockchain concepts."""
    color = COLORS['blockchain']
    words = slug.split('-')
    kw = set(words)

    if 'block' in kw and 'chain' not in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="2" y="7" width="8" height="10" rx="1"/>
<rect x="14" y="7" width="8" height="10" rx="1"/>
<line x1="10" y1="12" x2="14" y2="12"/>
<line x1="5" y1="10" x2="7" y2="10"/><line x1="5" y1="13" x2="7" y2="13"/>
<line x1="17" y1="10" x2="19" y2="10"/><line x1="17" y1="13" x2="19" y2="13"/>
</svg>'''

    if 'blockchain' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="1" y="9" width="6" height="6" rx="1"/>
<rect x="9" y="9" width="6" height="6" rx="1"/>
<rect x="17" y="9" width="6" height="6" rx="1"/>
<line x1="7" y1="12" x2="9" y2="12"/><line x1="15" y1="12" x2="17" y2="12"/>
</svg>'''

    if 'smart' in kw and 'contract' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="4" y="2" width="16" height="20" rx="2"/>
<line x1="8" y1="7" x2="16" y2="7"/>
<line x1="8" y1="11" x2="16" y2="11"/>
<line x1="8" y1="15" x2="12" y2="15"/>
<path d="M14 14 L17 17 L14 20" fill="none"/>
</svg>'''

    if 'consensus' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="12" r="3"/>
<circle cx="4" cy="6" r="2"/><circle cx="20" cy="6" r="2"/>
<circle cx="4" cy="18" r="2"/><circle cx="20" cy="18" r="2"/>
<line x1="6" y1="7" x2="10" y2="10"/><line x1="18" y1="7" x2="14" y2="10"/>
<line x1="6" y1="17" x2="10" y2="14"/><line x1="18" y1="17" x2="14" y2="14"/>
</svg>'''

    if 'hash' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<line x1="8" y1="4" x2="6" y2="20"/><line x1="16" y1="4" x2="14" y2="20"/>
<line x1="5" y1="9" x2="19" y2="9"/><line x1="5" y1="15" x2="19" y2="15"/>
</svg>'''

    if 'wallet' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="2" y="6" width="20" height="14" rx="2"/>
<path d="M16 6 L16 4 Q16 2 14 2 L4 2 Q2 2 2 4 L2 6"/>
<circle cx="17" cy="13" r="2"/>
</svg>'''

    if 'gas' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="4" y="10" width="12" height="12" rx="1"/>
<path d="M4 10 L4 4 Q4 2 6 2 L14 2 Q16 2 16 4 L16 10"/>
<path d="M16 8 L20 6 L20 18 L16 16"/>
<line x1="8" y1="14" x2="12" y2="14"/>
</svg>'''

    if 'token' in kw or 'nft' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="12" r="9"/>
<path d="M9 8 L9 16 M15 8 L15 16 M9 10 L15 10 M9 14 L15 14"/>
</svg>'''

    if 'stake' in kw or 'staking' in kw or 'validator' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="7" r="4"/>
<path d="M4 20 Q4 14 12 14 Q20 14 20 20"/>
<line x1="12" y1="14" x2="12" y2="20"/>
<polyline points="9,17 12,20 15,17" fill="none"/>
</svg>'''

    if 'defi' in kw or 'liquidity' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="7" cy="12" r="4"/>
<circle cx="17" cy="12" r="4"/>
<path d="M11 12 L13 12"/>
<path d="M7 8 Q7 4 12 4 Q17 4 17 8"/>
<path d="M7 16 Q7 20 12 20 Q17 20 17 16"/>
</svg>'''

    if 'zk' in kw or 'proof' in kw or 'rollup' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="3" y="8" width="18" height="12" rx="2"/>
<path d="M7 8 L7 5 Q7 3 12 3 Q17 3 17 5 L17 8"/>
<circle cx="12" cy="14" r="2"/>
<line x1="12" y1="16" x2="12" y2="18"/>
</svg>'''

    if 'encrypt' in kw or 'key' in kw or 'sign' in kw or 'crypto' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="8" cy="11" r="4"/>
<line x1="12" y1="11" x2="21" y2="11"/>
<line x1="18" y1="11" x2="18" y2="14"/>
<line x1="21" y1="11" x2="21" y2="14"/>
</svg>'''

    if 'fork' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<line x1="12" y1="3" x2="12" y2="10"/>
<path d="M12 10 Q12 14 7 17 Q7 19 7 21"/>
<path d="M12 10 Q12 14 17 17 Q17 19 17 21"/>
<circle cx="7" cy="21" r="1.5"/><circle cx="17" cy="21" r="1.5"/>
<circle cx="12" cy="3" r="1.5"/>
</svg>'''

    if 'node' in kw or 'network' in kw or 'peer' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="12" r="2"/>
<circle cx="4" cy="4" r="2"/><circle cx="20" cy="4" r="2"/>
<circle cx="4" cy="20" r="2"/><circle cx="20" cy="20" r="2"/>
<line x1="5.4" y1="5.4" x2="10.6" y2="10.6"/>
<line x1="18.6" y1="5.4" x2="13.4" y2="10.6"/>
<line x1="5.4" y1="18.6" x2="10.6" y2="13.4"/>
<line x1="18.6" y1="18.6" x2="13.4" y2="13.4"/>
</svg>'''

    if 'oracle' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="12" r="9"/>
<path d="M8 9 Q12 5 16 9 Q18 12 16 15 Q12 19 8 15 Q6 12 8 9" stroke-dasharray="2,1"/>
<circle cx="12" cy="12" r="2"/>
</svg>'''

    if 'mining' in kw or 'miner' in kw or 'pow' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<path d="M3 21 L10 14"/>
<rect x="10" y="10" width="4" height="4" transform="rotate(45 12 12)"/>
<line x1="14" y1="10" x2="20" y2="4"/>
<line x1="17" y1="3" x2="21" y2="7"/>
</svg>'''

    if 'merkle' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="9" y="2" width="6" height="4" rx="1"/>
<rect x="3" y="10" width="6" height="4" rx="1"/>
<rect x="15" y="10" width="6" height="4" rx="1"/>
<rect x="1" y="18" width="5" height="4" rx="1"/>
<rect x="7" y="18" width="5" height="4" rx="1"/>
<rect x="13" y="18" width="5" height="4" rx="1"/>
<rect x="19" y="18" width="4" height="4" rx="1"/>
<line x1="12" y1="6" x2="6" y2="10"/><line x1="12" y1="6" x2="18" y2="10"/>
<line x1="6" y1="14" x2="3.5" y2="18"/><line x1="6" y1="14" x2="9.5" y2="18"/>
<line x1="18" y1="14" x2="15.5" y2="18"/><line x1="18" y1="14" x2="21" y2="18"/>
</svg>'''

    if 'dapp' in kw or 'dao' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="5" r="3"/>
<circle cx="4" cy="19" r="3"/>
<circle cx="20" cy="19" r="3"/>
<line x1="12" y1="8" x2="6" y2="16.5"/><line x1="12" y1="8" x2="18" y2="16.5"/>
<line x1="7" y1="19" x2="17" y2="19"/>
</svg>'''

    if 'layer' in kw or 'shard' in kw or 'rollup' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="3" y="4" width="18" height="5" rx="1"/>
<rect x="3" y="11" width="18" height="5" rx="1"/>
<rect x="3" y="18" width="18" height="4" rx="1"/>
<line x1="12" y1="4" x2="12" y2="9"/><line x1="12" y1="11" x2="12" y2="16"/>
</svg>'''

    if 'bridge' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<line x1="2" y1="18" x2="22" y2="18"/>
<line x1="5" y1="18" x2="5" y2="12"/><line x1="19" y1="18" x2="19" y2="12"/>
<path d="M5 12 Q12 6 19 12"/>
<line x1="2" y1="18" x2="2" y2="22"/><line x1="22" y1="18" x2="22" y2="22"/>
</svg>'''

    if 'address' in kw or 'account' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="8" r="4"/>
<path d="M4 20 Q4 14 12 14 Q20 14 20 20"/>
<rect x="14" y="16" width="7" height="5" rx="1"/>
<line x1="16" y1="18" x2="19" y2="18"/>
</svg>'''

    if 'evm' in kw or 'virtual' in kw or 'bytecode' in kw:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="2" y="4" width="20" height="16" rx="2"/>
<line x1="2" y1="8" x2="22" y2="8"/>
<text x="4" y="7" font-size="4" fill="{color}" stroke="none">01</text>
<line x1="6" y1="13" x2="8" y2="11"/><line x1="8" y1="11" x2="10" y2="13"/>
<line x1="12" y1="13" x2="18" y2="13"/>
<line x1="6" y1="17" x2="18" y2="17"/>
</svg>'''

    if 'finality' in kw or 'finalit' in slug:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<rect x="3" y="8" width="6" height="8" rx="1"/>
<rect x="11" y="8" width="6" height="8" rx="1"/>
<rect x="19" y="8" width="3" height="8" rx="1"/>
<line x1="9" y1="12" x2="11" y2="12"/><line x1="17" y1="12" x2="19" y2="12"/>
<polyline points="5,11 7,13 10,9" stroke="{color}" fill="none"/>
</svg>'''

    # Default blockchain fallback
    h = sum(ord(c) * (i+3) for i, c in enumerate(slug, 1)) % 5
    icons = [
        f'<circle cx="12" cy="12" r="9"/><path d="M8 12 Q12 6 16 12 Q12 18 8 12"/>',
        f'<polygon points="12,2 22,20 2,20"/><circle cx="12" cy="14" r="2"/>',
        f'<rect x="4" y="4" width="16" height="16" rx="2"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="12" y1="4" x2="12" y2="20"/>',
        f'<path d="M12 2 L22 7 L22 17 L12 22 L2 17 L2 7 Z"/>',
        f'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><line x1="12" y1="3" x2="12" y2="8"/><line x1="12" y1="16" x2="12" y2="21"/>',
    ]
    body = icons[h]
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">\n{body}\n</svg>'


def make_tags(slug, category):
    words = [w for w in slug.replace('-', ' ').split() if len(w) > 2]
    tags = words[:4]
    if category == 'blockchain':
        tags.insert(0, 'blockchain')
    elif category == 'ai':
        tags.insert(0, 'ai')
    return list(dict.fromkeys(tags))[:5]


# ─────────────────────────────────────────────────────────
# 5. Generate icons
# ─────────────────────────────────────────────────────────
generated = []
for slug, (label, category) in all_concepts.items():
    if category == 'ai':
        svg = make_svg_ai(slug, label)
    else:
        svg = make_svg_blockchain(slug, label)

    json_data = {
        "name": slug,
        "label": label,
        "category": category,
        "tags": make_tags(slug, category),
        "version": "1.3"
    }

    svg_path = ICONS_DIR / f'{slug}.svg'
    json_path = ICONS_DIR / f'{slug}.json'

    svg_path.write_text(svg)
    json_path.write_text(json.dumps(json_data, indent=2))
    generated.append(slug)

print(f"\n✅ Generated {len(generated)} new icons")
print(f"   AI icons: {sum(1 for s in generated if all_concepts[s][1]=='ai')}")
print(f"   Blockchain icons: {sum(1 for s in generated if all_concepts[s][1]=='blockchain')}")

total = len(list(ICONS_DIR.glob('*.json')))
print(f"   Total icons now: {total}")

# Save generated list for next step
with open('/tmp/generated_icons.txt', 'w') as f:
    f.write('\n'.join(generated))
