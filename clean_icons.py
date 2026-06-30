#!/usr/bin/env python3
"""
AgentiScript Icon Cleaner
Removes all icons with no commercial value for developers/AI/blockchain/tech buyers.
Keeps only high-value categories.
"""

import json
import os
import re
import shutil
from collections import Counter

icons_dir = '/Users/colin/seo/agentiscript/icons/'
agentiscript_json = '/Users/colin/seo/agentiscript/agentiscript.json'

# ============================================================
# KEEP CATEGORIES (high commercial value)
# ============================================================
KEEP_CATEGORIES = {
    # Direct AI/Agentic
    'ai', 'ml', 'agentic', 'agentic-economy', 'agents', 'ai-agents',
    'multi-agent', 'llm', 'rag', 'nlp', 'alignment', 'patterns',
    'reasoning', 'retrieval', 'evaluation', 'optimization',
    'rl',  # reinforcement learning
    
    # Blockchain
    'blockchain', 'finance-defi',
    
    # Quantum / Nano
    'quantum', 'nanotechnology',
    
    # Security
    'security', 'cryptography', 'privacy',
    
    # Infrastructure / Dev
    'infrastructure', 'networking', 'cloud', 'database', 'devops',
    'web', 'product', 'workflow', 'resilience', 'distributed',
    
    # Data Science
    'data', 'bioinformatics',
    
    # Finance/Economics (tech-adjacent)
    'finance', 'economics-finance', 'prediction-markets', 'game-theory',
    
    # Philosophy/Futurism
    'philosophy', 'Philosophy',
    
    # Project/Business
    'business', 'governance', 'Project Management',
    
    # Specialized tech networks
    'flare', 'near', 'ripple-hedera', 'space-defense',
    
    # Embeddings / cognitive (when tech-relevant)
    'embeddings', 'cognitive-science',
    
    # Hardware
    'hardware', 'robotics',
    
    # Other tech
    'science-tech', 'complex-systems', 'training', 'planning',
    'tools', 'debugging', 'standards', 'research',
}

# ============================================================
# DELETE CATEGORIES (no commercial value)
# ============================================================
DELETE_CATEGORIES = {
    'agriculture', 'Agriculture',
    'nautical',
    'sports',
    'chess',
    'music',
    'literature',
    'virology', 'Virology',
    'meteorology', 'Meteorology',
    'cinema',
    'numismatics',
    'rhetoric',
    'patent-law',
    'archaeology',
    'ecology',
    'Plant Morphology', 'Plant Pathology',
    'American Politics',
    'Political Theory',
    'sociology',
    'medicine', 'Medicine',
    'Library and Information Science',
    'psychology',
    'Geology',
    'astronomy',
    'Language Education',
    'culture',
    'ux',
    'Aerospace Engineering',  # mechanical aerospace (not quantum/computing)
    'system',  # too vague, check samples
}

# ============================================================
# AMBIGUOUS categories that need source-based filtering
# ============================================================
# 'general'  -- depends on source
# 'science'  -- depends on source  
# 'engineering' -- depends on source (ee = electrical engineering → keep, others may not)
# 'physics' -- keep (quantum/particle physics is relevant)
# 'chemistry' -- keep some, delete most
# 'neuroscience' -- mostly delete (biological, not AI)
# 'biology' -- delete
# 'statistics' -- keep (math/data relevant)
# 'tensor' -- keep (ML relevant)
# 'topology' -- keep (graph/math relevant)
# 'geometry' -- keep (math relevant)
# 'math' -- keep
# 'economics' -- partially keep (tech-adjacent concepts)
# 'Climate Change' -- keep (AI + climate tech)

# Sources that indicate DELETE even in general/science/engineering categories
DELETE_SOURCES = {
    'nautical',
    'sports',
    'Agriculture_glossary', 'agriculture',
    'chess',
    'music',
    'literature',
    'virology',
    'Glossary_of_meteorology', 'meteorology',
    'cinema',
    'numismatics',
    'rhetoric',
    'patent-law',
    'archaeology',
    'Glossary_of_ecology', 'ecology',
    'political-science',
    'library-info-science',
    'life-sciences',  # mostly biological
    'neuro',  # neuroscience/biology
    'Positive_psychology',
    'Cognitive_psychology',
    'earth-sciences',  # geology
    'Glossary_of_architecture',
    'linguistics',
}

# Sources that indicate KEEP even in ambiguous categories
KEEP_SOURCES = {
    'ee',  # electrical engineering
    'ai',
    'economics',
    'Glossary_of_graph_theory',
    'Glossary_of_general_topology',
    'Glossary_of_tensor_theory',
    'Glossary_of_mathematical_jargon',
    'stats',
    'Glossary_of_philosophy',
    'philosophy',
    'climate-change',
    'finance',
    'biology',  # sometimes has relevant concepts
    'project-management',
    'law',  # sometimes has IP/tech law
}

# AMBIGUOUS categories - rules differ
AMBIGUOUS_CATEGORIES = {
    'general', 'science', 'engineering', 'physics', 'chemistry',
    'neuroscience', 'biology', 'statistics', 'tensor', 'topology',
    'geometry', 'math', 'economics', 'Climate Change',
    'tech',  # mostly keep tech category
    'graph',  # graph theory → keep
}


def should_keep_icon(data):
    """Determine if an icon should be kept based on its category, source, name."""
    cat = data.get('category', 'unknown')
    src = data.get('source', '')
    name = data.get('name', '').lower()
    slug = data.get('slug', '').lower()
    tags = data.get('tags', [])
    
    # Explicit KEEP categories
    if cat in KEEP_CATEGORIES:
        return True, f"keep_category:{cat}"
    
    # Explicit DELETE categories
    if cat in DELETE_CATEGORIES:
        return False, f"delete_category:{cat}"
    
    # Handle tech category - mostly keep (has computing/software/EE content)
    if cat == 'tech':
        # Delete if source is clearly non-tech
        if src in DELETE_SOURCES:
            return False, f"tech_delete_source:{src}"
        return True, f"tech_keep"
    
    # Handle ambiguous categories
    if cat in AMBIGUOUS_CATEGORIES:
        # Source-based rules
        if src in DELETE_SOURCES:
            return False, f"ambig_delete_source:{src}"
        if src in KEEP_SOURCES:
            return True, f"ambig_keep_source:{src}"
        
        # Category-specific logic
        if cat == 'general':
            # Glossary_of_meteorology, Glossary_of_ecology, Glossary_of_architecture → delete
            if src in ('Glossary_of_meteorology', 'Glossary_of_ecology', 'Glossary_of_architecture'):
                return False, f"general_delete_source:{src}"
            # economics, ee, graph/topology, stats, tensor, philosophy, ai → keep
            if src in ('economics', 'ee', 'Glossary_of_graph_theory', 'Glossary_of_general_topology',
                      'Glossary_of_tensor_theory', 'stats', 'Glossary_of_mathematical_jargon',
                      'Glossary_of_philosophy', 'ai', 'finance', 'climate-change',
                      'Positive_psychology', 'Cognitive_psychology'):
                return True, f"general_keep_source:{src}"
            # Default general: delete (too broad)
            return False, f"general_default_delete"
        
        if cat == 'science':
            # science has mix of astronomy, biology, chemistry... but also physics
            # If source is ecology, neuro, life-sciences → delete
            if src in ('', ):
                # No source - check if it looks like a tech/physics/quantum concept
                tech_keywords = ['quantum', 'neural', 'algorithm', 'ai', 'data', 'compute',
                                 'model', 'network', 'digital', 'crypto', 'encode', 'logic',
                                 'signal', 'electron', 'photon', 'laser', 'spectral', 'fractal',
                                 'chaos', 'entropy', 'information', 'coherence']
                if any(kw in slug or kw in name for kw in tech_keywords):
                    return True, f"science_tech_keyword"
                return False, f"science_default_delete"
            return False, f"science_no_source_delete"
        
        if cat == 'engineering':
            if src == 'ee':
                return True, f"engineering_ee"
            # Other engineering sources - check for tech relevance
            if src in DELETE_SOURCES:
                return False, f"engineering_delete_source:{src}"
            # No source - keep if looks like tech
            tech_keywords = ['software', 'computer', 'digital', 'algorithm', 'data', 'network',
                            'signal', 'system', 'control', 'filter', 'circuit', 'crypto',
                            'quantum', 'logic', 'neural', 'ai', 'model', 'formal']
            if any(kw in slug or kw in name for kw in tech_keywords):
                return True, f"engineering_tech_keyword"
            return False, f"engineering_default_delete"
        
        if cat == 'physics':
            # Physics is mostly useful (quantum, particle, computational physics)
            # Delete pure classical mechanics not useful for tech
            delete_physics = ['anatomy', 'medical', 'clinical', 'surgery', 'organ',
                             'bone', 'muscle', 'artery', 'vein', 'tissue']
            if any(kw in slug or kw in name for kw in delete_physics):
                return False, f"physics_biology_keyword"
            return True, f"physics_keep"
        
        if cat == 'chemistry':
            # Keep chemistry if related to materials, quantum, computational, nano
            keep_chem_keywords = ['quantum', 'computational', 'nano', 'semiconductor', 'polymer',
                                  'catalyst', 'electrode', 'electrochemical', 'crystal', 'molecular',
                                  'spectroscopy', 'reaction', 'organic', 'inorganic', 'thermodynamic']
            if any(kw in slug or kw in name for kw in keep_chem_keywords):
                return True, f"chemistry_keep_keyword"
            # Don't be too selective - chemistry has real value
            return True, f"chemistry_default_keep"
        
        if cat == 'neuroscience':
            # Keep if AI-adjacent (neural networks, brain-computer, cognitive)
            keep_neuro = ['neural', 'network', 'learning', 'memory', 'cognitive', 'cortex',
                         'artificial', 'computational', 'brain-computer', 'plasticity', 'hebbian',
                         'perceptron', 'backprop', 'synapse', 'neuron', 'activation']
            if any(kw in slug or kw in name for kw in keep_neuro):
                return True, f"neuro_ai_keyword"
            return False, f"neuro_biological_delete"
        
        if cat == 'biology':
            # Keep only if AI/tech related
            keep_bio = ['bioinformatics', 'computational', 'synthetic', 'genetic', 'algorithm',
                       'evolution', 'neural', 'network', 'sequence', 'genome', 'protein-folding',
                       'crispr', 'digital', 'artificial']
            if any(kw in slug or kw in name for kw in keep_bio):
                return True, f"biology_tech_keyword"
            return False, f"biology_default_delete"
        
        if cat in ('statistics', 'tensor', 'topology', 'geometry', 'math', 'graph'):
            return True, f"math_keep:{cat}"
        
        if cat == 'economics':
            # Keep economics - lots of relevant concepts (game theory, market, incentives)
            return True, f"economics_keep"
        
        if cat == 'Climate Change':
            return True, f"climate_keep"
    
    # Unknown categories: default delete
    return False, f"unknown_category:{cat}"


# Run the analysis
keep_icons = []
delete_icons = []
keep_reasons = Counter()
delete_reasons = Counter()

for f in sorted(os.listdir(icons_dir)):
    if not f.endswith('.json'):
        continue
    slug = f[:-5]  # remove .json
    json_path = os.path.join(icons_dir, f)
    svg_path = os.path.join(icons_dir, slug + '.svg')
    
    try:
        data = json.load(open(json_path))
        keep, reason = should_keep_icon(data)
        if keep:
            keep_icons.append((slug, json_path, svg_path, data, reason))
            keep_reasons[reason] += 1
        else:
            delete_icons.append((slug, json_path, svg_path, data, reason))
            delete_reasons[reason] += 1
    except Exception as e:
        print(f"ERROR reading {f}: {e}")

print(f"\n{'='*60}")
print(f"ANALYSIS COMPLETE")
print(f"{'='*60}")
print(f"Total icons: {len(keep_icons) + len(delete_icons)}")
print(f"KEEP:   {len(keep_icons)}")
print(f"DELETE: {len(delete_icons)}")
print(f"\nTop KEEP reasons:")
for reason, count in sorted(keep_reasons.items(), key=lambda x: -x[1])[:20]:
    print(f"  {count:5d}  {reason}")
print(f"\nTop DELETE reasons:")
for reason, count in sorted(delete_reasons.items(), key=lambda x: -x[1])[:20]:
    print(f"  {count:5d}  {reason}")
