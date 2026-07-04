#!/usr/bin/env python3
"""
Scrape GitHub trending repositories to extract developer vocabulary for AgentiScript.
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import time
from collections import defaultdict
from urllib.parse import urlencode

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xhtml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with",
    "by", "from", "up", "about", "into", "through", "during", "is", "are", "was", "were",
    "be", "been", "being", "have", "has", "had", "do", "does", "did", "will", "would",
    "could", "should", "may", "might", "shall", "can", "this", "that", "these", "those",
    "i", "you", "he", "she", "it", "we", "they", "what", "which", "who", "when", "where",
    "how", "all", "each", "every", "both", "few", "more", "most", "other", "some", "such",
    "no", "not", "only", "same", "so", "than", "too", "very", "just", "as", "if", "then",
    "new", "use", "using", "used", "get", "got", "make", "made", "like", "also", "your",
    "our", "its", "any", "one", "two", "three", "based", "simple", "easy", "fast", "free",
    "open", "source", "project", "code", "library", "tool", "framework", "app", "application",
    "built", "build", "run", "running", "work", "works", "working", "support", "supports",
    "provide", "provides", "provides", "allow", "allows", "enable", "enables", "multiple",
    "via", "etc", "vs", "pro", "plus", "let", "set", "help", "full", "real", "high", "low",
    "repo", "repository", "github", "git", "version", "v1", "v2", "v3", "v4",
}

def slugify(text):
    """Convert text to kebab-case slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', ' ', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    return text

def extract_concepts(text):
    """Extract meaningful concept slugs from text."""
    if not text:
        return []
    
    # Split on common delimiters
    words = re.findall(r'[a-zA-Z][a-zA-Z0-9]*(?:[._-][a-zA-Z0-9]+)*', text)
    
    concepts = []
    for word in words:
        # Handle camelCase, PascalCase
        parts = re.sub(r'([A-Z][a-z])', r' \1', word)
        parts = re.sub(r'([a-z])([A-Z])', r'\1 \2', parts)
        subwords = parts.split()
        
        for w in subwords:
            slug = slugify(w)
            if slug and len(slug) > 2 and slug not in STOPWORDS and not slug.isdigit():
                concepts.append(slug)
    
    # Also extract bigrams for compound concepts
    clean_words = [slugify(w) for w in re.findall(r'\b[a-zA-Z][a-zA-Z0-9]{2,}\b', text.lower())]
    clean_words = [w for w in clean_words if w not in STOPWORDS and not w.isdigit() and len(w) > 2]
    
    for i in range(len(clean_words) - 1):
        bigram = f"{clean_words[i]}-{clean_words[i+1]}"
        concepts.append(bigram)
    
    return concepts

def parse_stars(star_text):
    """Parse star count from text like '1.2k' or '15,234'."""
    if not star_text:
        return 0
    star_text = star_text.strip().replace(',', '').replace(' ', '').lower()
    if 'k' in star_text:
        try:
            return int(float(star_text.replace('k', '')) * 1000)
        except:
            return 0
    try:
        return int(re.sub(r'[^\d]', '', star_text))
    except:
        return 0

def scrape_github_trending(since="daily", language=""):
    """Scrape GitHub trending page."""
    url = "https://github.com/trending"
    params = {}
    if language:
        url = f"https://github.com/trending/{language}"
    if since:
        params['since'] = since
    
    if params:
        url = f"{url}?{urlencode(params)}"
    
    print(f"  Fetching: {url}")
    
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except Exception as e:
        print(f"  ERROR: {e}")
        return []
    
    soup = BeautifulSoup(resp.text, 'html.parser')
    repos = []
    
    # Find all repository articles
    articles = soup.select('article.Box-row')
    
    for article in articles:
        repo = {}
        
        # Repo name
        h2 = article.select_one('h2.h3 a')
        if h2:
            repo['full_name'] = h2.get_text(strip=True).replace(' ', '').replace('\n', '')
            parts = repo['full_name'].split('/')
            repo['name'] = parts[-1] if parts else repo['full_name']
            repo['owner'] = parts[0] if len(parts) > 1 else ''
        
        # Description
        p = article.select_one('p.col-9')
        repo['description'] = p.get_text(strip=True) if p else ''
        
        # Stars
        star_el = article.select_one('a[href$="/stargazers"]')
        repo['stars'] = parse_stars(star_el.get_text(strip=True)) if star_el else 0
        
        # Stars today
        stars_today_el = article.select_one('span.d-inline-block.float-sm-right')
        repo['stars_today'] = parse_stars(
            re.sub(r'stars today', '', stars_today_el.get_text(strip=True), flags=re.I)
        ) if stars_today_el else 0
        
        # Language
        lang_el = article.select_one('[itemprop="programmingLanguage"]')
        repo['language'] = lang_el.get_text(strip=True) if lang_el else ''
        
        # Topics (may not be on trending page but try)
        topic_els = article.select('a.topic-tag')
        repo['topics'] = [t.get_text(strip=True) for t in topic_els]
        
        repo['source'] = f"{since}/{language or 'all'}"
        
        if repo.get('name'):
            repos.append(repo)
    
    print(f"  Found {len(repos)} repos")
    return repos

def main():
    all_repos = []
    
    # Scrape different time periods
    print("\n=== Scraping GitHub Trending ===\n")
    
    periods = [
        ("daily", ""),
        ("weekly", ""),
        ("monthly", ""),
    ]
    
    languages = ["python", "javascript", "typescript", "rust", "go"]
    
    for since, lang in periods:
        repos = scrape_github_trending(since=since, language=lang)
        all_repos.extend(repos)
        time.sleep(1.5)
    
    for lang in languages:
        repos = scrape_github_trending(since="daily", language=lang)
        all_repos.extend(repos)
        time.sleep(1.5)
    
    print(f"\nTotal repos scraped: {len(all_repos)}")
    
    # Deduplicate repos by full_name, keeping highest star count
    repo_map = {}
    for repo in all_repos:
        key = repo.get('full_name', repo.get('name', ''))
        if key not in repo_map or repo.get('stars', 0) > repo_map[key].get('stars', 0):
            repo_map[key] = repo
    
    unique_repos = list(repo_map.values())
    print(f"Unique repos: {len(unique_repos)}")
    
    # Extract concepts and score them
    concept_scores = defaultdict(float)
    concept_sources = defaultdict(set)
    
    for repo in unique_repos:
        stars = repo.get('stars', 0)
        stars_today = repo.get('stars_today', 0)
        
        # Weight: use stars as base score, boost by stars_today
        base_score = stars + (stars_today * 10)
        
        all_text_concepts = []
        
        # From repo name
        name = repo.get('name', '')
        name_concepts = extract_concepts(name)
        all_text_concepts.extend([(c, 3.0) for c in name_concepts])  # name gets 3x weight
        
        # From description
        desc = repo.get('description', '')
        desc_concepts = extract_concepts(desc)
        all_text_concepts.extend([(c, 1.0) for c in desc_concepts])
        
        # From topics
        for topic in repo.get('topics', []):
            topic_concepts = extract_concepts(topic)
            all_text_concepts.extend([(c, 2.0) for c in topic_concepts])  # topics get 2x
        
        # Score each concept
        for concept, weight in all_text_concepts:
            if len(concept) > 2 and not concept.isdigit():
                # Skip pure numbers and too-short concepts
                score_contribution = (base_score * weight) / 1000.0  # normalize
                concept_scores[concept] += score_contribution
                concept_sources[concept].add(repo.get('language', 'unknown'))
    
    # Filter out stopwords that snuck through
    filtered_concepts = {
        k: v for k, v in concept_scores.items()
        if k not in STOPWORDS
        and len(k) > 2
        and not k.isdigit()
        and not re.match(r'^[0-9-]+$', k)
    }
    
    # Sort by score descending
    sorted_concepts = sorted(filtered_concepts.items(), key=lambda x: x[1], reverse=True)
    
    # Build top 500
    top_500 = []
    seen = set()
    for concept, score in sorted_concepts:
        if concept not in seen:
            seen.add(concept)
            top_500.append({
                "slug": concept,
                "score": round(score, 2),
                "languages": sorted(list(concept_sources.get(concept, set())))
            })
        if len(top_500) >= 500:
            break
    
    # Build output structure
    output = {
        "meta": {
            "source": "github-trending",
            "scraped_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "total_repos": len(unique_repos),
            "total_concepts": len(filtered_concepts),
            "output_concepts": len(top_500),
            "periods": ["daily", "weekly", "monthly"],
            "languages": languages,
        },
        "repos_sample": [
            {
                "full_name": r.get('full_name', ''),
                "description": r.get('description', ''),
                "stars": r.get('stars', 0),
                "language": r.get('language', ''),
                "topics": r.get('topics', []),
            }
            for r in sorted(unique_repos, key=lambda x: x.get('stars', 0), reverse=True)[:50]
        ],
        "concepts": top_500
    }
    
    # Save
    output_path = "/Users/colin/seo/agentiscript/kw-research/github-trending.json"
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\nSaved to: {output_path}")
    
    # Print top 50
    print("\n=== TOP 50 DEVELOPER CONCEPTS (from GitHub Trending) ===\n")
    print(f"{'Rank':<6} {'Slug':<40} {'Score':<12} {'Languages'}")
    print("-" * 80)
    for i, item in enumerate(top_500[:50], 1):
        langs = ', '.join(item['languages'][:3]) if item['languages'] else 'mixed'
        print(f"{i:<6} {item['slug']:<40} {item['score']:<12.1f} {langs}")
    
    print(f"\n✅ Total: {len(top_500)} concepts from {len(unique_repos)} trending repos")
    return output

if __name__ == "__main__":
    main()
