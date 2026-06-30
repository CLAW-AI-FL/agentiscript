#!/usr/bin/env python3
"""Generate new AgentiScript icons for a16z concepts and NIST/government data concepts."""

import json
from pathlib import Path

ICONS_DIR = Path("/Users/colin/seo/agentiscript/icons")
BASE_DIR = Path("/Users/colin/seo/agentiscript")

# SVG stroke color from existing icons
COLOR = "#9F792C"

icons = [
    # ─── A16Z Priority List ───────────────────────────────────────────────────
    {
        "id": "AS-179",
        "slug": "machine-readability",
        "concept": "Machine Readability",
        "definition": "The degree to which data, documents, or information is structured and formatted so software agents can parse, interpret, and act upon it without human intervention",
        "aliases": ["structured data", "parseable format", "machine-parseable", "semantic markup"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "sources": ["https://a16z.com/big-ideas-2025/"],
        "tags": ["machine readability", "structured data", "parsing", "AI", "automation"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<rect x="4" y="3" width="12" height="16" rx="1.5" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<path d="M7 7 h6 M7 10 h4 M7 13 h5 M7 16 h3" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<circle cx="18" cy="17" r="3.5" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<path d="M17 17 l1 1 l1.5-2" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>'
            '</svg>'
        ),
    },
    {
        "id": "AS-180",
        "slug": "identity-autonomous-agents",
        "concept": "Identity for Autonomous Agents",
        "definition": "Cryptographic and policy-based frameworks that assign verifiable, persistent identities to AI agents, enabling trust, accountability, and access control in multi-agent systems",
        "aliases": ["agent identity", "AI agent ID", "autonomous agent credentials", "decentralized agent identity"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "sources": ["https://a16z.com/big-ideas-2025/"],
        "tags": ["identity", "autonomous agents", "AI", "credentials", "trust"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<rect x="3" y="8" width="13" height="10" rx="2" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<circle cx="9.5" cy="13" r="2.5" fill="none" stroke="{COLOR}" stroke-width="1.2"/>'
            f'<path d="M13 18 a3.5 3.5 0 0 0-7 0" fill="none" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<rect x="17" y="3" width="4" height="5" rx="1" fill="none" stroke="{COLOR}" stroke-width="1.2"/>'
            f'<path d="M19 3 v-1.5 M19 8 v1.5" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<path d="M16 5.5 h1 M20 5.5 h1" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            '</svg>'
        ),
    },
    {
        "id": "AS-181",
        "slug": "programmable-financial-internet",
        "concept": "Internet as Programmable Financial System",
        "definition": "The evolution of the internet into a platform where financial transactions, contracts, and value transfers are natively programmable, composable, and automated via smart contracts and open protocols",
        "aliases": ["programmable money", "financial internet", "money legos", "composable finance"],
        "category": "economics-finance",
        "category_name": "Economics & Finance",
        "sources": ["https://a16z.com/big-ideas-2025/"],
        "tags": ["programmable finance", "internet", "smart contracts", "DeFi", "fintech"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<circle cx="12" cy="12" r="8" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<ellipse cx="12" cy="12" rx="3.5" ry="8" fill="none" stroke="{COLOR}" stroke-width="1"/>'
            f'<line x1="4" y1="12" x2="20" y2="12" stroke="{COLOR}" stroke-width="1"/>'
            f'<text x="12" y="15.5" text-anchor="middle" font-size="6" font-weight="bold" font-family="sans-serif" fill="{COLOR}">$</text>'
            '</svg>'
        ),
    },
    {
        "id": "AS-182",
        "slug": "ai-native-data-stack",
        "concept": "AI-Native Data Stack",
        "definition": "A data infrastructure purpose-built for AI workloads, with vector databases, feature stores, streaming pipelines, and retrieval-augmented systems as first-class primitives",
        "aliases": ["AI data infrastructure", "vector data stack", "ML data pipeline", "AI-first database"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "sources": ["https://a16z.com/big-ideas-2025/"],
        "tags": ["data stack", "AI", "vector database", "infrastructure", "ML"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<ellipse cx="12" cy="18" rx="7" ry="2.5" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<path d="M5 18 v-4" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<path d="M19 18 v-4" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<ellipse cx="12" cy="14" rx="7" ry="2.5" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<path d="M5 14 v-4" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<path d="M19 14 v-4" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<ellipse cx="12" cy="10" rx="7" ry="2.5" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<path d="M10 7 L12 5 L14 7" fill="none" stroke="{COLOR}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<line x1="12" y1="5" x2="12" y2="3" stroke="{COLOR}" stroke-width="1.3" stroke-linecap="round"/>'
            '</svg>'
        ),
    },
    {
        "id": "AS-183",
        "slug": "multi-agent-orchestration",
        "concept": "Multi-Agent Orchestration",
        "definition": "The coordination, scheduling, and management of multiple specialized AI agents working in concert to accomplish complex tasks, including delegation, context sharing, and result aggregation",
        "aliases": ["agent orchestration", "AI swarm", "agent coordination", "multi-agent system"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "sources": ["https://a16z.com/big-ideas-2025/"],
        "tags": ["multi-agent", "orchestration", "AI agents", "coordination", "swarm"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<circle cx="12" cy="12" r="2.5" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<circle cx="4.5" cy="6" r="2" fill="none" stroke="{COLOR}" stroke-width="1.2"/>'
            f'<circle cx="19.5" cy="6" r="2" fill="none" stroke="{COLOR}" stroke-width="1.2"/>'
            f'<circle cx="4.5" cy="18" r="2" fill="none" stroke="{COLOR}" stroke-width="1.2"/>'
            f'<circle cx="19.5" cy="18" r="2" fill="none" stroke="{COLOR}" stroke-width="1.2"/>'
            f'<line x1="6.5" y1="7" x2="10" y2="10.5" stroke="{COLOR}" stroke-width="1"/>'
            f'<line x1="17.5" y1="7" x2="14" y2="10.5" stroke="{COLOR}" stroke-width="1"/>'
            f'<line x1="6.5" y1="17" x2="10" y2="13.5" stroke="{COLOR}" stroke-width="1"/>'
            f'<line x1="17.5" y1="17" x2="14" y2="13.5" stroke="{COLOR}" stroke-width="1"/>'
            '</svg>'
        ),
    },
    {
        "id": "AS-184",
        "slug": "outcome-based-metrics",
        "concept": "Outcome-Based Metrics",
        "definition": "Performance measurement frameworks that evaluate AI systems by their real-world results and impact rather than process or output proxies, enabling value-aligned incentives",
        "aliases": ["results-based metrics", "impact metrics", "value metrics", "KPI outcomes"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "sources": ["https://a16z.com/big-ideas-2025/"],
        "tags": ["metrics", "outcomes", "KPI", "measurement", "AI evaluation"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<circle cx="12" cy="12" r="8.5" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<circle cx="12" cy="12" r="5.5" fill="none" stroke="{COLOR}" stroke-width="1"/>'
            f'<circle cx="12" cy="12" r="2.5" fill="none" stroke="{COLOR}" stroke-width="1"/>'
            f'<circle cx="12" cy="12" r="1" fill="{COLOR}"/>'
            f'<path d="M12 3.5 v2 M12 18.5 v2 M3.5 12 h2 M18.5 12 h2" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            '</svg>'
        ),
    },
    {
        "id": "AS-185",
        "slug": "voice-agent",
        "concept": "Voice Agent",
        "definition": "An AI system that interacts with users through spoken natural language, combining speech recognition, language understanding, and speech synthesis to complete tasks conversationally",
        "aliases": ["voice AI", "conversational AI", "speech agent", "voice assistant AI"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "sources": ["https://a16z.com/big-ideas-2025/"],
        "tags": ["voice", "agent", "speech", "AI", "conversational"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<rect x="9" y="3" width="6" height="10" rx="3" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<path d="M5.5 11 a6.5 6.5 0 0 0 13 0" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round"/>'
            f'<line x1="12" y1="17.5" x2="12" y2="21" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round"/>'
            f'<line x1="9" y1="21" x2="15" y2="21" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round"/>'
            f'<path d="M2.5 9.5 q1-1 1 1 q1 2 1 0 q1-2 1 0 q1 2 1 0" fill="none" stroke="{COLOR}" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M18.5 9.5 q1-1 1 1 q1 2 1 0 q1-2 1 0 q1 2 1 0" fill="none" stroke="{COLOR}" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"/>'
            '</svg>'
        ),
    },
    {
        "id": "AS-186",
        "slug": "onchain-rwa-origination",
        "concept": "Onchain RWA Origination",
        "definition": "The process of creating blockchain-native representations of real-world assets such as real estate, commodities, or receivables, enabling 24/7 global liquidity and programmable ownership",
        "aliases": ["RWA tokenization", "real-world asset origination", "asset tokenization", "onchain assets"],
        "category": "economics-finance",
        "category_name": "Economics & Finance",
        "sources": ["https://a16z.com/big-ideas-2025/"],
        "tags": ["RWA", "real-world assets", "onchain", "tokenization", "blockchain"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<rect x="3" y="10" width="5" height="8" rx="1" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<rect x="9.5" y="6" width="5" height="12" rx="1" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<rect x="16" y="13" width="5" height="5" rx="1" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<path d="M8 5 l3-3 3 3" fill="none" stroke="{COLOR}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<line x1="11" y1="2" x2="11" y2="6" stroke="{COLOR}" stroke-width="1.3" stroke-linecap="round"/>'
            f'<path d="M16 12 l2-2 2 2" fill="none" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>'
            '</svg>'
        ),
    },
    {
        "id": "AS-187",
        "slug": "stablecoin-on-off-ramp",
        "concept": "Stablecoin On/Off Ramp",
        "definition": "Infrastructure enabling seamless conversion between fiat currencies and stablecoins, bridging traditional banking rails with blockchain networks for mainstream adoption",
        "aliases": ["crypto on-ramp", "fiat to stablecoin", "stablecoin gateway", "fiat offramp"],
        "category": "economics-finance",
        "category_name": "Economics & Finance",
        "sources": ["https://a16z.com/big-ideas-2025/"],
        "tags": ["stablecoin", "on-ramp", "off-ramp", "fiat", "crypto"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<circle cx="5" cy="12" r="3.5" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<text x="5" y="14.5" text-anchor="middle" font-size="5" font-weight="bold" font-family="sans-serif" fill="{COLOR}">$</text>'
            f'<circle cx="19" cy="12" r="3.5" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<text x="19" y="14.5" text-anchor="middle" font-size="5" font-weight="bold" font-family="sans-serif" fill="{COLOR}">₮</text>'
            f'<path d="M8.5 10 l3 -2 l3 2" fill="none" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M8.5 14 l3 2 l3 -2" fill="none" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<line x1="8.5" y1="10" x2="15.5" y2="10" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<line x1="8.5" y1="14" x2="15.5" y2="14" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            '</svg>'
        ),
    },
    {
        "id": "AS-188",
        "slug": "preventive-health-platform",
        "concept": "Preventive Health Platform",
        "definition": "AI-driven health systems that proactively monitor biomarkers, predict disease risk, and deliver personalized interventions before conditions become acute, shifting from reactive to preventive care",
        "aliases": ["preventive care AI", "proactive health", "health monitoring platform", "predictive health"],
        "category": "health-science",
        "category_name": "Health & Science",
        "sources": ["https://a16z.com/big-ideas-2025/"],
        "tags": ["preventive health", "platform", "AI health", "monitoring", "wellness"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<path d="M12 20 C12 20 4 15 4 9 a4 4 0 0 1 8 -2 a4 4 0 0 1 8 2 C20 15 12 20 12 20z" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<path d="M7 10 l2 2 l2-4 l2 4 l2-2" fill="none" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M12 4 l1 1" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            '</svg>'
        ),
    },
    {
        "id": "AS-189",
        "slug": "factory-style-ai-deployment",
        "concept": "Factory-Style AI Deployment",
        "definition": "Systematic, repeatable processes for deploying AI models at scale with standardized infrastructure, automated testing, and continuous monitoring — analogous to industrial manufacturing principles",
        "aliases": ["AI factory", "scaled AI deployment", "AI production line", "ML deployment pipeline"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "sources": ["https://a16z.com/big-ideas-2025/"],
        "tags": ["AI deployment", "factory", "scale", "MLOps", "production"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<rect x="2" y="14" width="20" height="8" rx="1" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<path d="M2 14 l5-6 v6" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linejoin="round"/>'
            f'<path d="M7 14 l5-6 v6" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linejoin="round"/>'
            f'<path d="M12 14 l5-6 v6" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linejoin="round"/>'
            f'<rect x="16" y="8" width="4" height="6" rx="0.5" fill="none" stroke="{COLOR}" stroke-width="1.2"/>'
            f'<line x1="5" y1="17" x2="5" y2="19" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<line x1="10" y1="17" x2="10" y2="19" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<line x1="15" y1="17" x2="15" y2="19" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<line x1="19" y1="17" x2="19" y2="19" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            '</svg>'
        ),
    },
    {
        "id": "AS-190",
        "slug": "physical-observability",
        "concept": "Physical Observability",
        "definition": "The ability to monitor, measure, and interpret the state of physical systems and environments in real time using sensors, IoT devices, and AI analytics",
        "aliases": ["physical monitoring", "sensor observability", "IoT observability", "real-world sensing"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "sources": ["https://a16z.com/big-ideas-2025/"],
        "tags": ["observability", "physical", "IoT", "sensors", "monitoring"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<ellipse cx="12" cy="12" rx="9" ry="5.5" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<circle cx="12" cy="12" r="2.5" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<circle cx="12" cy="12" r="0.8" fill="{COLOR}"/>'
            f'<path d="M4" y1="12" M4 8 q4-5 8 0" fill="none" stroke="{COLOR}" stroke-width="1" stroke-dasharray="1.5,1"/>'
            f'<line x1="5" y1="19" x2="7" y2="17" stroke="{COLOR}" stroke-width="1" stroke-linecap="round"/>'
            f'<line x1="12" y1="21" x2="12" y2="19" stroke="{COLOR}" stroke-width="1" stroke-linecap="round"/>'
            f'<line x1="19" y1="19" x2="17" y2="17" stroke="{COLOR}" stroke-width="1" stroke-linecap="round"/>'
            '</svg>'
        ),
    },
    {
        "id": "AS-191",
        "slug": "prompt-free-proactive-ai",
        "concept": "Prompt-Free Proactive AI",
        "definition": "AI systems that autonomously initiate actions, surface insights, and complete tasks without waiting for explicit user prompts, driven by context, goals, and ambient signals",
        "aliases": ["proactive AI", "autonomous AI", "ambient AI", "unprompted AI"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "sources": ["https://a16z.com/big-ideas-2025/"],
        "tags": ["proactive AI", "autonomous", "prompt-free", "ambient intelligence"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<circle cx="12" cy="10" r="5" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<path d="M10 9 l1.5 1.5 l2.5-3" fill="none" stroke="{COLOR}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M9 15 l3 4 l3-4" fill="none" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<line x1="12" y1="15" x2="12" y2="19" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<line x1="3" y1="4" x2="5" y2="6" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<line x1="21" y1="4" x2="19" y2="6" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<line x1="1.5" y1="10" x2="4" y2="10" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<line x1="22.5" y1="10" x2="20" y2="10" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            '</svg>'
        ),
    },
    {
        "id": "AS-192",
        "slug": "ai-enhanced-prediction-market",
        "concept": "AI-Enhanced Prediction Market",
        "definition": "Prediction markets augmented with AI to improve forecasting accuracy, automate market making, aggregate diverse signals, and surface insights from collective intelligence at scale",
        "aliases": ["AI prediction markets", "algorithmic prediction markets", "ML forecasting markets"],
        "category": "economics-finance",
        "category_name": "Economics & Finance",
        "sources": ["https://a16z.com/big-ideas-2025/"],
        "tags": ["prediction market", "AI", "forecasting", "trading", "probability"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<polyline points="3,18 7,13 10,15 14,8 18,10 21,5" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<line x1="3" y1="21" x2="21" y2="21" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<line x1="3" y1="3" x2="3" y2="21" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<circle cx="21" cy="5" r="2" fill="none" stroke="{COLOR}" stroke-width="1.2"/>'
            f'<line x1="20" y1="4" x2="22" y2="6" stroke="{COLOR}" stroke-width="1" stroke-linecap="round"/>'
            f'<line x1="22" y1="4" x2="20" y2="6" stroke="{COLOR}" stroke-width="1" stroke-linecap="round"/>'
            '</svg>'
        ),
    },
    # ─── NIST / Government Data Concepts ────────────────────────────────────
    {
        "id": "AS-193",
        "slug": "zero-trust",
        "concept": "Zero Trust",
        "definition": "A security model (NIST SP 800-207) that requires continuous verification of every user, device, and connection — no entity is trusted by default, even inside the network perimeter",
        "aliases": ["zero trust architecture", "ZTA", "never trust always verify", "NIST zero trust"],
        "category": "security",
        "category_name": "Security",
        "sources": ["https://csrc.nist.gov/publications/detail/sp/800-207/final"],
        "tags": ["zero trust", "security", "NIST", "authentication", "network security"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<path d="M12 3 L4 7 v5 c0 5 4 8 8 10 c4-2 8-5 8-10 V7 z" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linejoin="round"/>'
            f'<line x1="9" y1="9" x2="15" y2="15" stroke="{COLOR}" stroke-width="1.8" stroke-linecap="round"/>'
            f'<line x1="15" y1="9" x2="9" y2="15" stroke="{COLOR}" stroke-width="1.8" stroke-linecap="round"/>'
            '</svg>'
        ),
    },
    {
        "id": "AS-194",
        "slug": "digital-identity",
        "concept": "Digital Identity",
        "definition": "A unique digital representation of an entity (person, organization, or device) consisting of attributes, credentials, and identifiers used to authenticate and authorize actions in digital systems (NIST SP 800-63)",
        "aliases": ["digital ID", "digital credentials", "electronic identity", "NIST digital identity"],
        "category": "security",
        "category_name": "Security",
        "sources": ["https://csrc.nist.gov/publications/detail/sp/800-63/4/final"],
        "tags": ["digital identity", "NIST", "credentials", "authentication", "identity"],
        "svg_content": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">'
            f'<rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="{COLOR}" stroke-width="1.5"/>'
            f'<circle cx="8.5" cy="11" r="2.5" fill="none" stroke="{COLOR}" stroke-width="1.2"/>'
            f'<path d="M5.5 17 a3 3 0 0 1 6 0" fill="none" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<line x1="14" y1="9" x2="19" y2="9" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<line x1="14" y1="12" x2="19" y2="12" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            f'<line x1="14" y1="15" x2="17" y2="15" stroke="{COLOR}" stroke-width="1.2" stroke-linecap="round"/>'
            '</svg>'
        ),
    },
]

def write_icon(icon):
    slug = icon["slug"]
    # Write SVG
    svg_path = ICONS_DIR / f"{slug}.svg"
    svg_path.write_text(icon["svg_content"])

    # Write JSON
    meta = {
        "id": icon["id"],
        "slug": slug,
        "concept": icon["concept"],
        "definition": icon["definition"],
        "aliases": icon["aliases"],
        "category": icon["category"],
        "category_name": icon["category_name"],
        "sources": icon["sources"],
        "svg": f"{slug}.svg",
        "tags": icon["tags"],
    }
    json_path = ICONS_DIR / f"{slug}.json"
    json_path.write_text(json.dumps(meta, indent=2))
    print(f"  ✓ {slug} ({icon['id']})")
    return meta

# Write all icons
print(f"Writing {len(icons)} new icons...")
new_metas = [write_icon(i) for i in icons]

# Update master agentiscript.json
master_path = BASE_DIR / "agentiscript.json"
master = json.loads(master_path.read_text())
existing_slugs = {x["slug"] for x in master["icons"]}

added = 0
for meta in new_metas:
    if meta["slug"] not in existing_slugs:
        master["icons"].append(meta)
        added += 1

master["total"] = len(master["icons"])
master_path.write_text(json.dumps(master, indent=2))
print(f"\nMaster index updated: {added} icons added, total={master['total']}")
