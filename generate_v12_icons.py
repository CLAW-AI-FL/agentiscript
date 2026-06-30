#!/usr/bin/env python3
"""Generate 25 new AgentiScript icons: a16z priorities + NIST/gov concepts."""

import json, os

ICONS_DIR = "/Users/colin/seo/agentiscript/icons"
INDEX_PATH = "/Users/colin/seo/agentiscript/agentiscript.json"
STROKE = "#9F792C"
SW = "1.5"

def svg(paths, extra=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
        f'fill="none" stroke="{STROKE}" stroke-width="{SW}" '
        f'stroke-linecap="round" stroke-linejoin="round">{paths}{extra}</svg>'
    )

# ── icon definitions ─────────────────────────────────────────────────────────
NEW_ICONS = [

# ── a16z priorities ──────────────────────────────────────────────────────────
{
  "slug": "machine-readability",
  "concept": "Machine Readability",
  "definition": "Structuring data and documents so AI agents can parse, interpret, and act on them without human intermediation.",
  "category": "ai-agents",
  "category_name": "AI Agents",
  "tags": ["machine-readable", "structured data", "parsing", "a16z", "agent input"],
  "svg_body": (
    '<rect x="3" y="2" width="14" height="18" rx="1.5"/>'
    '<line x1="7" y1="7" x2="13" y2="7"/>'
    '<line x1="7" y1="11" x2="13" y2="11"/>'
    '<line x1="7" y1="15" x2="11" y2="15"/>'
    '<polyline points="17 9 21 12 17 15"/>'
  )
},
{
  "slug": "agent-identity",
  "concept": "Agent Identity",
  "definition": "Cryptographically verifiable credentials that uniquely identify an AI agent across systems and transactions.",
  "category": "ai-agents",
  "category_name": "AI Agents",
  "tags": ["identity", "credentials", "agent", "a16z", "authentication"],
  "svg_body": (
    '<circle cx="12" cy="8" r="3.5"/>'
    '<path d="M5 20c0-4 3.1-7 7-7s7 3 7 7"/>'
    '<circle cx="12" cy="8" r="1" fill="'+STROKE+'"/>'
    '<polyline points="9 19 11 21 15 17"/>'
  )
},
{
  "slug": "programmable-financial-system",
  "concept": "Programmable Financial System",
  "definition": "A financial infrastructure where money movement, compliance, and settlement are encoded as executable logic rather than manual process.",
  "category": "finance-defi",
  "category_name": "Finance & DeFi",
  "tags": ["programmable money", "fintech", "smart contracts", "a16z", "settlement"],
  "svg_body": (
    '<rect x="3" y="5" width="18" height="14" rx="2"/>'
    '<line x1="3" y1="10" x2="21" y2="10"/>'
    '<text x="9" y="16.5" font-size="6" stroke="'+STROKE+'" stroke-width="0.8" fill="'+STROKE+'" font-family="monospace">&lt;$&gt;</text>'
  )
},
{
  "slug": "ai-native-data-stack",
  "concept": "AI-Native Data Stack",
  "definition": "Data infrastructure built from the ground up for LLM ingestion, retrieval-augmented generation, and agentic pipelines.",
  "category": "infrastructure",
  "category_name": "Infrastructure",
  "tags": ["data stack", "RAG", "AI infra", "a16z", "vector store"],
  "svg_body": (
    '<ellipse cx="12" cy="6" rx="7" ry="2.5"/>'
    '<path d="M5 6v4c0 1.4 3.1 2.5 7 2.5s7-1.1 7-2.5V6"/>'
    '<path d="M5 10v4c0 1.4 3.1 2.5 7 2.5s7-1.1 7-2.5v-4"/>'
    '<path d="M5 14v4c0 1.4 3.1 2.5 7 2.5s7-1.1 7-2.5v-4"/>'
    '<line x1="16" y1="4" x2="20" y2="2"/>'
    '<circle cx="21" cy="2" r="1.2" fill="'+STROKE+'"/>'
  )
},
{
  "slug": "multi-agent-orchestration",
  "concept": "Multi-Agent Orchestration",
  "definition": "Coordinating multiple AI agents with distinct roles, tools, and memory to collaboratively complete complex tasks.",
  "category": "ai-agents",
  "category_name": "AI Agents",
  "tags": ["orchestration", "multi-agent", "coordination", "a16z", "workflow"],
  "svg_body": (
    '<circle cx="12" cy="4" r="2"/>'
    '<circle cx="4" cy="18" r="2"/>'
    '<circle cx="20" cy="18" r="2"/>'
    '<circle cx="12" cy="13" r="2"/>'
    '<line x1="12" y1="6" x2="12" y2="11"/>'
    '<line x1="12" y1="15" x2="5.5" y2="16.5"/>'
    '<line x1="12" y1="15" x2="18.5" y2="16.5"/>'
  )
},
{
  "slug": "outcome-based-metrics",
  "concept": "Outcome-Based Metrics",
  "definition": "Measuring AI agent performance by real-world results delivered rather than activity proxies like tokens generated or tasks initiated.",
  "category": "ai-agents",
  "category_name": "AI Agents",
  "tags": ["metrics", "KPI", "outcomes", "a16z", "evaluation"],
  "svg_body": (
    '<circle cx="12" cy="12" r="9"/>'
    '<circle cx="12" cy="12" r="5.5"/>'
    '<circle cx="12" cy="12" r="2"/>'
    '<line x1="12" y1="3" x2="12" y2="1"/>'
    '<polyline points="9 12 11 14 15 10"/>'
  )
},
{
  "slug": "voice-agent",
  "concept": "Voice Agent",
  "definition": "An AI agent that perceives, processes, and responds through spoken language, enabling hands-free agentic interaction.",
  "category": "ai-agents",
  "category_name": "AI Agents",
  "tags": ["voice", "speech", "audio", "a16z", "conversational AI"],
  "svg_body": (
    '<rect x="9" y="2" width="6" height="11" rx="3"/>'
    '<path d="M5 10a7 7 0 0 0 14 0"/>'
    '<line x1="12" y1="17" x2="12" y2="21"/>'
    '<line x1="9" y1="21" x2="15" y2="21"/>'
    '<path d="M4 9 Q3 12 5 14"/>'
    '<path d="M20 9 Q21 12 19 14"/>'
  )
},
{
  "slug": "onchain-rwa-origination",
  "concept": "Onchain RWA Origination",
  "definition": "The minting and management of real-world asset tokens — debt, real estate, commodities — directly on a programmable blockchain.",
  "category": "finance-defi",
  "category_name": "Finance & DeFi",
  "tags": ["RWA", "tokenization", "onchain", "a16z", "real-world assets"],
  "svg_body": (
    '<rect x="2" y="8" width="8" height="10" rx="1"/>'
    '<path d="M10 12h4l3-3 3 3"/>'
    '<path d="M14 12v7"/>'
    '<circle cx="6" cy="5" r="2"/>'
    '<line x1="6" y1="7" x2="6" y2="8"/>'
    '<line x1="17" y1="12" x2="17" y2="19"/>'
    '<line x1="14" y1="19" x2="20" y2="19"/>'
  )
},
{
  "slug": "stablecoin-onramp",
  "concept": "Stablecoin Onramp",
  "definition": "Infrastructure that converts fiat currency into stablecoins seamlessly, enabling agents and users to enter crypto-native financial rails.",
  "category": "finance-defi",
  "category_name": "Finance & DeFi",
  "tags": ["stablecoin", "onramp", "fiat", "a16z", "USDC"],
  "svg_body": (
    '<circle cx="12" cy="12" r="9"/>'
    '<line x1="12" y1="6" x2="12" y2="8"/>'
    '<line x1="12" y1="16" x2="12" y2="18"/>'
    '<path d="M15 8.5a3 3 0 0 0-6 0c0 1.6 1.3 2.5 3 3s3 1.5 3 3a3 3 0 0 1-6 0"/>'
    '<polyline points="8 3 12 7 16 3"/>'
  )
},
{
  "slug": "factory-style-ai-deployment",
  "concept": "Factory-Style AI Deployment",
  "definition": "Industrialized pipelines for building, evaluating, and deploying AI agents at scale using repeatable, automated manufacturing metaphors.",
  "category": "infrastructure",
  "category_name": "Infrastructure",
  "tags": ["deployment", "factory", "automation", "a16z", "MLOps"],
  "svg_body": (
    '<rect x="2" y="12" width="20" height="9" rx="1"/>'
    '<polyline points="2 12 2 8 6 8 6 12"/>'
    '<polyline points="9 12 9 6 13 6 13 12"/>'
    '<polyline points="16 12 16 4 20 4 20 12"/>'
    '<line x1="2" y1="17" x2="22" y2="17"/>'
    '<line x1="6" y1="17" x2="6" y2="21"/>'
    '<line x1="12" y1="17" x2="12" y2="21"/>'
    '<line x1="18" y1="17" x2="18" y2="21"/>'
  )
},
{
  "slug": "physical-observability",
  "concept": "Physical Observability",
  "definition": "Equipping AI systems with real-time sensor data from the physical world — cameras, LIDAR, IoT — to ground decisions in material reality.",
  "category": "infrastructure",
  "category_name": "Infrastructure",
  "tags": ["observability", "sensors", "IoT", "a16z", "physical AI"],
  "svg_body": (
    '<circle cx="12" cy="12" r="3"/>'
    '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/>'
    '<line x1="12" y1="2" x2="12" y2="4"/>'
    '<line x1="12" y1="20" x2="12" y2="22"/>'
    '<line x1="2" y1="12" x2="4" y2="12"/>'
    '<line x1="20" y1="12" x2="22" y2="12"/>'
    '<circle cx="12" cy="12" r="1" fill="'+STROKE+'"/>'
  )
},
{
  "slug": "prompt-free-ai",
  "concept": "Prompt-Free AI",
  "definition": "AI systems that infer intent from context, behavior, and structured goals rather than requiring explicit natural-language prompts.",
  "category": "ai-agents",
  "category_name": "AI Agents",
  "tags": ["prompt-free", "intent inference", "a16z", "context-aware", "autonomy"],
  "svg_body": (
    '<rect x="3" y="5" width="14" height="11" rx="2"/>'
    '<path d="M17 10h2a2 2 0 0 1 0 4h-2"/>'
    '<line x1="7" y1="9" x2="13" y2="9" stroke-dasharray="2 1.5"/>'
    '<line x1="7" y1="13" x2="11" y2="13" stroke-dasharray="2 1.5"/>'
    '<line x1="5" y1="3" x2="19" y2="21"/>'
  )
},
{
  "slug": "ai-prediction-market",
  "concept": "AI Prediction Market",
  "definition": "Markets where AI agents trade probability contracts on real-world outcomes, creating decentralized forecasting mechanisms.",
  "category": "finance-defi",
  "category_name": "Finance & DeFi",
  "tags": ["prediction market", "forecasting", "a16z", "AI trading", "probability"],
  "svg_body": (
    '<polyline points="3 18 7 12 11 15 15 7 21 9"/>'
    '<circle cx="7" cy="12" r="1.2" fill="'+STROKE+'"/>'
    '<circle cx="11" cy="15" r="1.2" fill="'+STROKE+'"/>'
    '<circle cx="15" cy="7" r="1.2" fill="'+STROKE+'"/>'
    '<line x1="3" y1="21" x2="3" y2="18"/>'
    '<line x1="3" y1="21" x2="21" y2="21"/>'
    '<path d="M19 6l2 3h-4z" fill="'+STROKE+'" stroke="none"/>'
  )
},
{
  "slug": "vertical-ai",
  "concept": "Vertical AI",
  "definition": "AI systems purpose-built for a single industry domain — legal, healthcare, finance — with domain-specific data, models, and workflows.",
  "category": "ai-agents",
  "category_name": "AI Agents",
  "tags": ["vertical AI", "industry AI", "a16z", "domain-specific", "enterprise"],
  "svg_body": (
    '<rect x="3" y="3" width="5" height="18" rx="1"/>'
    '<rect x="10" y="7" width="5" height="14" rx="1"/>'
    '<rect x="17" y="11" width="5" height="10" rx="1"/>'
    '<circle cx="5.5" cy="5.5" r="1" fill="'+STROKE+'"/>'
    '<circle cx="12.5" cy="9.5" r="1" fill="'+STROKE+'"/>'
    '<circle cx="19.5" cy="13.5" r="1" fill="'+STROKE+'"/>'
  )
},
{
  "slug": "agent-scale-infrastructure",
  "concept": "Agent-Scale Infrastructure",
  "definition": "Compute, networking, and orchestration platforms engineered to run millions of concurrent AI agents reliably and economically.",
  "category": "infrastructure",
  "category_name": "Infrastructure",
  "tags": ["infrastructure", "scale", "agents", "a16z", "cloud"],
  "svg_body": (
    '<rect x="2" y="9" width="5" height="5" rx="1"/>'
    '<rect x="9.5" y="6" width="5" height="11" rx="1"/>'
    '<rect x="17" y="3" width="5" height="17" rx="1"/>'
    '<line x1="7" y1="12" x2="9.5" y2="12"/>'
    '<line x1="14.5" y1="12" x2="17" y2="12"/>'
    '<polyline points="20 1 22 3 20 5"/>'
  )
},

# ── NIST / Government concepts ────────────────────────────────────────────────
{
  "slug": "zero-trust",
  "concept": "Zero Trust",
  "definition": "A security model that eliminates implicit trust — every request, from any source, must be continuously authenticated and authorized.",
  "category": "security",
  "category_name": "Security",
  "tags": ["zero trust", "NIST", "security", "authentication", "micro-segmentation"],
  "svg_body": (
    '<path d="M12 2L3 7v5c0 5.25 3.75 10.15 9 11.35C17.25 22.15 21 17.25 21 12V7z"/>'
    '<line x1="9" y1="9" x2="15" y2="15"/>'
    '<line x1="15" y1="9" x2="9" y2="15"/>'
  )
},
{
  "slug": "digital-identity",
  "concept": "Digital Identity",
  "definition": "A verifiable, portable representation of an individual or entity's attributes in digital systems, governed by standards like NIST SP 800-63.",
  "category": "security",
  "category_name": "Security",
  "tags": ["digital identity", "NIST", "IAM", "credentials", "SSI"],
  "svg_body": (
    '<path d="M9 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2h-4"/>'
    '<rect x="9" y="1" width="6" height="4" rx="1"/>'
    '<circle cx="12" cy="11" r="3"/>'
    '<path d="M7 21v-1a5 5 0 0 1 10 0v1"/>'
  )
},
{
  "slug": "cyber-resilience",
  "concept": "Cyber Resilience",
  "definition": "The capacity to anticipate, withstand, recover from, and adapt to adverse cyber events while maintaining continuous operations.",
  "category": "security",
  "category_name": "Security",
  "tags": ["cyber resilience", "NIST", "recovery", "business continuity", "CISA"],
  "svg_body": (
    '<path d="M12 2L3 7v5c0 5.25 3.75 10.15 9 11.35C17.25 22.15 21 17.25 21 12V7z"/>'
    '<polyline points="9 12 11 14 16 9"/>'
    '<path d="M12 6v2M12 14v2" stroke-dasharray="1.5 1"/>'
  )
},
{
  "slug": "supply-chain-risk",
  "concept": "Supply Chain Risk",
  "definition": "Threats introduced through third-party software, hardware, or service dependencies — a top NIST and CISA concern in federal security frameworks.",
  "category": "security",
  "category_name": "Security",
  "tags": ["supply chain", "NIST", "SBOM", "third-party risk", "CISA"],
  "svg_body": (
    '<circle cx="4" cy="12" r="2"/>'
    '<circle cx="12" cy="12" r="2"/>'
    '<circle cx="20" cy="12" r="2"/>'
    '<line x1="6" y1="12" x2="10" y2="12"/>'
    '<line x1="14" y1="12" x2="18" y2="12"/>'
    '<path d="M12 10V5l-2-2"/>'
    '<path d="M12 5l2-2"/>'
    '<path d="M4 10V7l2-3"/>'
    '<line x1="17" y1="9" x2="20" y2="6"/>'
    '<line x1="20" y1="6" x2="17" y2="3"/>'
  )
},
{
  "slug": "cryptographic-agility",
  "concept": "Cryptographic Agility",
  "definition": "Designing systems to swap cryptographic algorithms quickly — critical for post-quantum migration per NIST PQC standards.",
  "category": "security",
  "category_name": "Security",
  "tags": ["cryptography", "NIST", "post-quantum", "PQC", "agility"],
  "svg_body": (
    '<rect x="5" y="11" width="14" height="10" rx="1"/>'
    '<path d="M8 11V7a4 4 0 0 1 8 0v4"/>'
    '<circle cx="12" cy="16" r="1.5" fill="'+STROKE+'"/>'
    '<path d="M10 4 Q12 2 14 4"/>'
    '<polyline points="8 4 10 4 10 6"/>'
    '<polyline points="16 4 14 4 14 6"/>'
  )
},
{
  "slug": "sovereign-data",
  "concept": "Sovereign Data",
  "definition": "The principle that data is subject to the laws and governance of the nation or entity where it originates, resists foreign extraction.",
  "category": "governance",
  "category_name": "Governance",
  "tags": ["data sovereignty", "government", "GDPR", "jurisdiction", "data governance"],
  "svg_body": (
    '<path d="M2 19h20"/>'
    '<rect x="6" y="11" width="12" height="8" rx="1"/>'
    '<path d="M10 11V9a2 2 0 0 1 4 0v2"/>'
    '<path d="M12 4l-4 4h8z" fill="'+STROKE+'"/>'
    '<line x1="12" y1="2" x2="12" y2="4"/>'
  )
},
{
  "slug": "federated-identity",
  "concept": "Federated Identity",
  "definition": "An arrangement allowing users to authenticate once across multiple independent systems using shared identity standards like SAML, OIDC, or FIDO2.",
  "category": "security",
  "category_name": "Security",
  "tags": ["federation", "NIST", "SSO", "OIDC", "identity management"],
  "svg_body": (
    '<circle cx="12" cy="12" r="2"/>'
    '<circle cx="4" cy="6" r="2"/>'
    '<circle cx="20" cy="6" r="2"/>'
    '<circle cx="4" cy="18" r="2"/>'
    '<circle cx="20" cy="18" r="2"/>'
    '<line x1="6" y1="7" x2="10.5" y2="10.5"/>'
    '<line x1="18" y1="7" x2="13.5" y2="10.5"/>'
    '<line x1="6" y1="17" x2="10.5" y2="13.5"/>'
    '<line x1="18" y1="17" x2="13.5" y2="13.5"/>'
  )
},
{
  "slug": "critical-infrastructure",
  "concept": "Critical Infrastructure",
  "definition": "The 16 CISA-designated sectors — energy, water, finance, communications — whose disruption would have severe national security consequences.",
  "category": "governance",
  "category_name": "Governance",
  "tags": ["critical infrastructure", "CISA", "national security", "government", "resilience"],
  "svg_body": (
    '<rect x="4" y="10" width="16" height="11" rx="1"/>'
    '<path d="M2 10l10-7 10 7"/>'
    '<rect x="9" y="14" width="6" height="7"/>'
    '<line x1="9" y1="14" x2="9" y2="21"/>'
    '<polyline points="12 2 12 4"/>'
    '<line x1="4" y1="10" x2="4" y2="21"/>'
    '<line x1="20" y1="10" x2="20" y2="21"/>'
  )
},
{
  "slug": "privacy-enhancing-technology",
  "concept": "Privacy-Enhancing Technology",
  "definition": "Tools like differential privacy, homomorphic encryption, and secure multi-party computation that process data without exposing raw personal information.",
  "category": "security",
  "category_name": "Security",
  "tags": ["PET", "privacy", "NIST", "differential privacy", "homomorphic encryption"],
  "svg_body": (
    '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/>'
    '<circle cx="12" cy="12" r="3"/>'
    '<line x1="5" y1="5" x2="19" y2="19"/>'
    '<path d="M12 9v6M9 12h6" stroke-dasharray="1.5 1.5"/>'
  )
},
{
  "slug": "algorithmic-accountability",
  "concept": "Algorithmic Accountability",
  "definition": "The obligation for organizations to explain, audit, and accept responsibility for automated decisions affecting individuals — core to AI governance frameworks.",
  "category": "governance",
  "category_name": "Governance",
  "tags": ["accountability", "AI governance", "NIST AI RMF", "explainability", "audit"],
  "svg_body": (
    '<rect x="2" y="3" width="20" height="18" rx="1.5"/>'
    '<line x1="2" y1="9" x2="22" y2="9"/>'
    '<line x1="8" y1="9" x2="8" y2="21"/>'
    '<line x1="12" y1="13" x2="18" y2="13"/>'
    '<line x1="12" y1="17" x2="16" y2="17"/>'
    '<polyline points="4 5 5.5 6.5 8 4"/>'
  )
},
]

# ── helpers ──────────────────────────────────────────────────────────────────
def make_svg(body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
        f'fill="none" stroke="{STROKE}" stroke-width="{SW}" '
        f'stroke-linecap="round" stroke-linejoin="round">'
        f'{body}</svg>'
    )

# ── load existing index ──────────────────────────────────────────────────────
with open(INDEX_PATH) as f:
    index = json.load(f)

existing_ids = [int(x["id"].replace("AS-", "")) for x in index["icons"] if x.get("id","").startswith("AS-")]
next_id = max(existing_ids) + 1

# ── write files ──────────────────────────────────────────────────────────────
added = []
for icon in NEW_ICONS:
    slug = icon["slug"]
    svg_content = make_svg(icon["svg_body"])
    svg_path = os.path.join(ICONS_DIR, f"{slug}.svg")
    json_path = os.path.join(ICONS_DIR, f"{slug}.json")

    # Write SVG
    with open(svg_path, "w") as f:
        f.write(svg_content)

    icon_id = f"AS-{next_id}"
    meta = {
        "id": icon_id,
        "slug": slug,
        "concept": icon["concept"],
        "definition": icon["definition"],
        "aliases": [],
        "category": icon["category"],
        "category_name": icon["category_name"],
        "sources": [],
        "svg": f"{slug}.svg",
        "tags": icon["tags"]
    }

    # Write JSON
    with open(json_path, "w") as f:
        json.dump(meta, f, indent=2)

    # Add to index
    index["icons"].append(meta)
    added.append(icon_id)
    next_id += 1
    print(f"  ✓ {icon_id}  {slug}")

# ── rebuild master index ─────────────────────────────────────────────────────
index["total"] = len(index["icons"])
index["version"] = "1.2"

with open(INDEX_PATH, "w") as f:
    json.dump(index, f, indent=2)

print(f"\n✅ Added {len(added)} icons (IDs {added[0]}–{added[-1]})")
print(f"📦 Master index updated: {index['total']} total icons")
