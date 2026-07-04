import json
import time
import re
import urllib.request
import urllib.parse
from collections import Counter

SEEDS = [
    "mesothelioma lawyer",
    "drug rehab",
    "tax debt relief",
    "semaglutide",
    "personal injury",
    "DUI lawyer",
    "bankruptcy",
    "dental implants",
    "plastic surgery",
    "solar panels",
    "HVAC repair",
    "roofing",
    "AI agents",
    "agentic economy",
    "XRP",
    "passive income",
    "make money online",
    "real estate investing",
    "crypto wallet",
    "mortgage broker",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def fetch(url, extra_headers=None):
    req = urllib.request.Request(url, headers={**HEADERS, **(extra_headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        return None


def bing_autocomplete(seed):
    url = "https://api.bing.com/osjson.aspx?query=" + urllib.parse.quote(seed)
    raw = fetch(url)
    if not raw:
        return []
    try:
        data = json.loads(raw)
        return data[1] if len(data) > 1 else []
    except Exception as e:
        print(f"  Parse error Bing autocomplete [{seed}]: {e}")
        return []


def ddg_instant(seed):
    url = "https://api.duckduckgo.com/?q=" + urllib.parse.quote(seed) + "&format=json&no_redirect=1"
    raw = fetch(url)
    if not raw:
        return []
    try:
        data = json.loads(raw)
        texts = []
        for topic in data.get("RelatedTopics", []):
            if isinstance(topic, dict):
                t = topic.get("Text", "")
                if t:
                    texts.append(t)
                # handle sub-topics
                for sub in topic.get("Topics", []):
                    if isinstance(sub, dict):
                        st = sub.get("Text", "")
                        if st:
                            texts.append(st)
        return texts
    except Exception as e:
        print(f"  Parse error DDG [{seed}]: {e}")
        return []


def bing_related(seed):
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(seed)
    raw = fetch(url, {"Accept": "text/html"})
    if not raw:
        return []
    # .b_rs a — related searches block
    matches = re.findall(r'class="[^"]*b_rs[^"]*"[^>]*>.*?</(?:div|ul)>', raw, re.DOTALL)
    anchors = []
    for block in matches:
        anchors += re.findall(r'<a[^>]*>([^<]+)</a>', block)
    if not anchors:
        # fallback: look for <a> near "Related searches" heading
        pos = raw.find("Related searches")
        if pos != -1:
            chunk = raw[pos:pos+3000]
            anchors = re.findall(r'<a[^>]*>([^<]+)</a>', chunk)
    return [a.strip() for a in anchors if a.strip() and len(a.strip()) > 3]


def to_slug(text):
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[\s_]+', '-', text.strip())
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


results = {}
all_terms = []

for seed in SEEDS:
    print(f"\n[{seed}]")
    
    ac = bing_autocomplete(seed)
    print(f"  Bing autocomplete: {ac}")
    time.sleep(0.4)

    ddg = ddg_instant(seed)
    print(f"  DDG topics: {len(ddg)}")
    time.sleep(0.4)

    rel = bing_related(seed)
    print(f"  Bing related: {rel[:5]}")
    time.sleep(0.8)

    results[seed] = {
        "bing_autocomplete": ac,
        "ddg_related_texts": ddg,
        "bing_related_searches": rel,
    }

    all_terms.extend(ac)
    all_terms.extend(rel)
    # Extract first ~10 words from each DDG text as a phrase
    for t in ddg:
        first_phrase = " ".join(t.split()[:8])
        all_terms.append(first_phrase)

# Build slug counter
slug_counter = Counter()
for term in all_terms:
    sl = to_slug(term)
    if sl and len(sl) > 2:
        slug_counter[sl] += 1

top50 = slug_counter.most_common(50)

output = {
    "metadata": {
        "seeds": SEEDS,
        "total_terms": len(all_terms),
        "unique_slugs": len(slug_counter),
        "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    },
    "by_seed": results,
    "top_50_slugs": [{"slug": s, "count": c} for s, c in top50],
    "all_slugs": [{"slug": s, "count": c} for s, c in slug_counter.most_common()],
}

out_path = "/Users/colin/seo/agentiscript/kw-research/bing-ddg-kw.json"
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)

print("\n\n========== TOP 50 UNIQUE SLUGS ==========")
for i, (slug, count) in enumerate(top50, 1):
    print(f"{i:2d}. {slug} ({count})")

print(f"\n✅  Saved to {out_path}")
print(f"    Total raw terms: {len(all_terms)}  |  Unique slugs: {len(slug_counter)}")
