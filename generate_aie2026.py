#!/usr/bin/env python3
"""Generate AgentiScript icons for AI Engineer World's Fair 2026 concepts."""

import json
import os
from pathlib import Path

ICONS_DIR = Path('/Users/colin/seo/agentiscript/icons')
STROKE = '#9F792C'
SW = '1.5'

def svg(body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{STROKE}" stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'

concepts = [
    {
        "id": "AS-204",
        "slug": "x402-protocol",
        "concept": "x402 Protocol",
        "definition": "An HTTP-native payment standard enabling AI agents to pay for resources inline using HTTP 402 status codes without redirects or human intervention.",
        "aliases": ["HTTP 402", "x402"],
        "category": "agentic-commerce",
        "category_name": "Agentic Commerce",
        "tags": ["payment", "http", "protocol", "agent", "x402"],
        "svg_body": '<rect x="3" y="5" width="18" height="14" rx="2"/><text x="7" y="16" font-size="7" stroke-width="1" stroke="#9F792C" fill="none" font-family="monospace">402</text><path d="M16 9l2 2-2 2"/>',
    },
    {
        "id": "AS-205",
        "slug": "agent-wallet",
        "concept": "Agent Wallet",
        "definition": "A cryptographically secured spending capability held by an AI agent, enabling it to autonomously authorize and execute financial transactions.",
        "aliases": ["agent treasury"],
        "category": "agentic-commerce",
        "category_name": "Agentic Commerce",
        "tags": ["wallet", "payment", "agent", "spending", "crypto"],
        "svg_body": '<rect x="2" y="7" width="20" height="14" rx="2"/><rect x="15" y="11" width="5" height="4" rx="1"/><circle cx="17.5" cy="13" r="0.75" fill="#9F792C"/><path d="M2 11h20"/><circle cx="8" cy="4" r="1.5"/><path d="M8 5.5v1.5"/>',
    },
    {
        "id": "AS-206",
        "slug": "machine-to-machine-commerce",
        "concept": "Machine-to-Machine Commerce",
        "definition": "Fully autonomous economic transactions between AI agents without human intermediation, forming the basis of an agent-native economy.",
        "aliases": ["M2M commerce", "agent economy"],
        "category": "agentic-commerce",
        "category_name": "Agentic Commerce",
        "tags": ["machine", "commerce", "agent", "autonomous", "transaction"],
        "svg_body": '<rect x="2" y="8" width="7" height="8" rx="1.5"/><rect x="15" y="8" width="7" height="8" rx="1.5"/><path d="M9 10.5h6M9 13.5h6"/><polyline points="13 9 15 11.5 13 14"/><polyline points="11 9 9 11.5 11 14"/>',
    },
    {
        "id": "AS-207",
        "slug": "auth-md",
        "concept": "Auth.md",
        "definition": "An open agent authentication protocol using markdown-based identity documents to grant verifiable, revocable credentials to AI agents.",
        "aliases": ["agent auth", "auth markdown"],
        "category": "agent-security",
        "category_name": "Agent Security",
        "tags": ["authentication", "protocol", "agent", "open", "identity"],
        "svg_body": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 11h8M8 14h5"/><circle cx="17" cy="17" r="3"/><path d="M15.5 17l1 1 2-2"/>',
    },
    {
        "id": "AS-208",
        "slug": "context-as-a-service",
        "concept": "Context as a Service",
        "definition": "An infrastructure layer that dynamically assembles, manages, and delivers contextual information to AI agents on demand at inference time.",
        "aliases": ["CaaS", "context layer"],
        "category": "agent-infrastructure",
        "category_name": "Agent Infrastructure",
        "tags": ["context", "service", "infrastructure", "CaaS", "agent"],
        "svg_body": '<path d="M6 17a4 4 0 010-8 5 5 0 019.9-1A4 4 0 0118 17"/><path d="M9 17v4M12 17v4M15 17v4"/><polyline points="9 21 12 19 15 21"/>',
    },
    {
        "id": "AS-209",
        "slug": "active-graph-runtime",
        "concept": "Active Graph Runtime",
        "definition": "An event-sourced, forkable agent runtime where state is a live graph of nodes and edges, enabling branching, replay, and parallel execution.",
        "aliases": ["graph runtime", "forkable runtime"],
        "category": "agent-infrastructure",
        "category_name": "Agent Infrastructure",
        "tags": ["graph", "runtime", "event-sourced", "forkable", "agent"],
        "svg_body": '<circle cx="12" cy="12" r="2.5"/><circle cx="4" cy="6" r="1.5"/><circle cx="20" cy="6" r="1.5"/><circle cx="4" cy="18" r="1.5"/><circle cx="20" cy="18" r="1.5"/><path d="M5.2 7l5.4 3.5M18.8 7l-5.4 3.5M5.2 17l5.4-3.5M18.8 17l-5.4-3.5"/>',
    },
    {
        "id": "AS-210",
        "slug": "agent-harness",
        "concept": "Agent Harness",
        "definition": "A production control cage that constrains, monitors, and governs AI agent behavior, enforcing policy boundaries and capturing execution traces.",
        "aliases": ["control harness", "agent cage"],
        "category": "agent-ops",
        "category_name": "Agent Ops",
        "tags": ["harness", "control", "governance", "agent", "production"],
        "svg_body": '<rect x="5" y="5" width="14" height="14" rx="2"/><circle cx="12" cy="12" r="3"/><path d="M5 9h3M16 9h3M5 15h3M16 15h3M9 5v3M9 16v3M15 5v3M15 16v3"/>',
    },
    {
        "id": "AS-211",
        "slug": "lethal-trifecta",
        "concept": "Lethal Trifecta",
        "definition": "The dangerous security combination when an AI agent has access to private data, processes untrusted content, and can communicate externally — enabling data exfiltration.",
        "aliases": ["security trifecta", "agent exfiltration"],
        "category": "agent-security",
        "category_name": "Agent Security",
        "tags": ["security", "trifecta", "exfiltration", "risk", "agent"],
        "svg_body": '<polygon points="12 3 21.7 19.5 2.3 19.5"/><circle cx="12" cy="9" r="1.2" fill="#9F792C"/><circle cx="7.5" cy="17" r="1.2" fill="#9F792C"/><circle cx="16.5" cy="17" r="1.2" fill="#9F792C"/><path d="M12 10.2v4.8"/>',
    },
    {
        "id": "AS-212",
        "slug": "tokenmaxxing",
        "concept": "Tokenmaxxing",
        "definition": "The practice of maximizing useful work extracted per token consumed, optimizing prompt density, context efficiency, and output quality per token cost.",
        "aliases": ["token efficiency", "context optimization"],
        "category": "llm-engineering",
        "category_name": "LLM Engineering",
        "tags": ["tokens", "efficiency", "optimization", "cost", "llm"],
        "svg_body": '<rect x="3" y="14" width="4" height="7" rx="1"/><rect x="10" y="9" width="4" height="12" rx="1"/><rect x="17" y="4" width="4" height="17" rx="1"/><polyline points="4 13 11 8 18 3"/><polyline points="16 3 18 3 18 5"/>',
    },
    {
        "id": "AS-213",
        "slug": "mcp-apps",
        "concept": "MCP Apps",
        "definition": "User interfaces and interactive applications returned directly from MCP tool calls, enabling agents to surface rich UI components inline in responses.",
        "aliases": ["tool-call UIs", "MCP UI"],
        "category": "mcp",
        "category_name": "MCP",
        "tags": ["mcp", "ui", "tools", "interface", "apps"],
        "svg_body": '<rect x="3" y="4" width="18" height="14" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><circle cx="6" cy="6.5" r="0.8" fill="#9F792C"/><circle cx="9" cy="6.5" r="0.8" fill="#9F792C"/><rect x="6" y="12" width="5" height="3" rx="0.5"/><rect x="13" y="12" width="5" height="3" rx="0.5"/><path d="M9 18l3 2 3-2"/>',
    },
    {
        "id": "AS-214",
        "slug": "agent-supply-chain-security",
        "concept": "Agent Supply Chain Security",
        "definition": "Provenance tracking and integrity verification through multi-agent pipelines, ensuring trust and auditability from data ingestion through action execution.",
        "aliases": ["agent SBOM", "pipeline provenance"],
        "category": "agent-security",
        "category_name": "Agent Security",
        "tags": ["security", "supply-chain", "provenance", "agent", "pipeline"],
        "svg_body": '<circle cx="4" cy="12" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="20" cy="12" r="2"/><path d="M6 12h4M14 12h4"/><path d="M10 9l2-4 2 4"/><path d="M10 15l2 4 2-4"/><path d="M20 10v-4h-4"/>',
    },
    {
        "id": "AS-215",
        "slug": "self-improving-software-factory",
        "concept": "Self-Improving Software Factory",
        "definition": "A recursive loop where AI agents write, test, and deploy code that improves the agents themselves, creating compounding autonomous software development.",
        "aliases": ["recursive factory", "agent-improves-agent"],
        "category": "ai-agents",
        "category_name": "AI Agents",
        "tags": ["self-improvement", "factory", "recursive", "agent", "software"],
        "svg_body": '<path d="M12 3a9 9 0 018 5"/><path d="M20 8V3h-5"/><path d="M12 21a9 9 0 01-8-5"/><path d="M4 16v5h5"/><rect x="9" y="9" width="6" height="6" rx="1"/><path d="M11 12h2M12 11v2"/>',
    },
    {
        "id": "AS-216",
        "slug": "agentic-commerce-stack",
        "concept": "Agentic Commerce Stack",
        "definition": "The complete layered protocol stack enabling autonomous purchasing — spanning identity, payment rails, policy enforcement, and settlement for AI agents.",
        "aliases": ["agent commerce stack", "autonomous purchasing stack"],
        "category": "agentic-commerce",
        "category_name": "Agentic Commerce",
        "tags": ["commerce", "stack", "protocol", "agent", "purchasing"],
        "svg_body": '<rect x="3" y="4" width="18" height="3.5" rx="1"/><rect x="3" y="10" width="18" height="3.5" rx="1"/><rect x="3" y="16" width="18" height="3.5" rx="1"/><path d="M6 5.75h3M6 11.75h3M6 17.75h3"/><circle cx="19" cy="5.75" r="1" fill="#9F792C"/><circle cx="19" cy="11.75" r="1" fill="#9F792C"/><circle cx="19" cy="17.75" r="1" fill="#9F792C"/>',
    },
    {
        "id": "AS-217",
        "slug": "forward-deployed-engineering",
        "concept": "Forward-Deployed Engineering",
        "definition": "Embedding software engineers directly with customers to build, iterate, and deploy AI systems live in production alongside business stakeholders.",
        "aliases": ["FDE", "embedded engineering"],
        "category": "ai-engineering",
        "category_name": "AI Engineering",
        "tags": ["engineering", "deployment", "forward-deployed", "ai", "palantir"],
        "svg_body": '<circle cx="12" cy="7" r="3"/><path d="M5 21v-2a7 7 0 0114 0v2"/><path d="M17 13l3 3-3 3"/><path d="M14 16h6"/>',
    },
    {
        "id": "AS-218",
        "slug": "gradient-free-continual-learning",
        "concept": "Gradient-Free Continual Learning",
        "definition": "Model adaptation techniques that update learned behavior through inference-time mechanisms rather than backpropagation, enabling deployment-time learning.",
        "aliases": ["gradient-free learning", "inference-time adaptation"],
        "category": "ml-training",
        "category_name": "ML Training",
        "tags": ["gradient-free", "continual-learning", "adaptation", "inference", "training"],
        "svg_body": '<path d="M3 18c3-8 5-8 9 0s6 0 9-8"/><circle cx="3" cy="18" r="1.5"/><circle cx="21" cy="10" r="1.5"/><line x1="12" y1="3" x2="12" y2="21" stroke-dasharray="2 2"/><path d="M9 8l3-5 3 5"/>',
    },
    {
        "id": "AS-219",
        "slug": "dual-surface-architecture",
        "concept": "Dual-Surface Architecture",
        "definition": "A system design where the same underlying tool and capability layer serves both human-facing UI surfaces and agent-facing API surfaces simultaneously.",
        "aliases": ["dual surface", "human-agent shared layer"],
        "category": "agent-architecture",
        "category_name": "Agent Architecture",
        "tags": ["architecture", "dual-surface", "human", "agent", "design"],
        "svg_body": '<rect x="2" y="3" width="9" height="7" rx="1.5"/><rect x="13" y="3" width="9" height="7" rx="1.5"/><rect x="7" y="14" width="10" height="7" rx="1.5"/><path d="M6.5 10v2h11v-2"/>',
    },
    {
        "id": "AS-220",
        "slug": "agent-budget",
        "concept": "Agent Budget",
        "definition": "Governance controls that define and enforce spending limits, resource caps, and authorization thresholds for autonomous AI agent transactions.",
        "aliases": ["agent spend limit", "autonomous budget"],
        "category": "agentic-commerce",
        "category_name": "Agentic Commerce",
        "tags": ["budget", "governance", "spending", "agent", "control"],
        "svg_body": '<circle cx="12" cy="12" r="9"/><path d="M12 6v2M12 16v2"/><path d="M9 9.5c0-1.4 1.3-2.5 3-2.5s3 1.1 3 2.5-1.3 2.5-3 2.5-3 1.1-3 2.5 1.3 2.5 3 2.5 3-1.1 3-2.5"/>',
    },
    {
        "id": "AS-221",
        "slug": "autoresearch",
        "concept": "Autoresearch",
        "definition": "AI agents that autonomously design, run, and interpret scientific or ML experiments, compressing the research cycle without human direction.",
        "aliases": ["autonomous research", "self-directed research"],
        "category": "ai-agents",
        "category_name": "AI Agents",
        "tags": ["research", "autonomous", "agent", "science", "ml"],
        "svg_body": '<circle cx="11" cy="10" r="6"/><path d="M15.5 14.5l4 4"/><path d="M8 10a3 3 0 016 0"/><path d="M11 7v1M8.5 8.5l.7.7M13.5 8.5l-.7.7"/><path d="M7 13l4 3 4-3"/>',
    },
    {
        "id": "AS-222",
        "slug": "computer-use-2",
        "concept": "Computer Use 2.0",
        "definition": "Next-generation browser automation with multiple parallel cursors enabling AI agents to operate many browser sessions concurrently on the same machine.",
        "aliases": ["parallel browser agents", "multi-cursor agents"],
        "category": "ai-agents",
        "category_name": "AI Agents",
        "tags": ["computer-use", "browser", "parallel", "multi-cursor", "agent"],
        "svg_body": '<rect x="2" y="4" width="20" height="14" rx="2"/><line x1="2" y1="8" x2="22" y2="8"/><path d="M7 12l2 5 1.5-2 2 2.5V12"/><path d="M15 12l2 5 1.5-2 1.5 2"/>',
    },
    {
        "id": "AS-223",
        "slug": "homa-network-protocol",
        "concept": "Homa Network Protocol",
        "definition": "A low-latency datacenter transport protocol designed as an RDMA replacement to maximize inference throughput and minimize tail latency in AI clusters.",
        "aliases": ["Homa protocol", "datacenter transport"],
        "category": "ai-infrastructure",
        "category_name": "AI Infrastructure",
        "tags": ["network", "protocol", "homa", "RDMA", "inference", "latency"],
        "svg_body": '<path d="M2 12h20"/><path d="M2 7h20"/><path d="M2 17h20"/><circle cx="7" cy="12" r="1.5" fill="#9F792C"/><circle cx="12" cy="7" r="1.5" fill="#9F792C"/><circle cx="17" cy="17" r="1.5" fill="#9F792C"/><polyline points="19 5 21 7 19 9"/>',
    },
    {
        "id": "AS-224",
        "slug": "p-d-disaggregation",
        "concept": "P/D Disaggregation",
        "definition": "Separating the prefill and decode phases of LLM inference onto specialized hardware instances to optimize throughput and resource utilization independently.",
        "aliases": ["prefill-decode split", "inference disaggregation"],
        "category": "llm-inference",
        "category_name": "LLM Inference",
        "tags": ["prefill", "decode", "inference", "disaggregation", "llm"],
        "svg_body": '<rect x="2" y="6" width="8" height="12" rx="2"/><rect x="14" y="6" width="8" height="12" rx="2"/><path d="M10 10h4M10 14h4"/><path d="M6 10v4M18 10v4"/>',
    },
    {
        "id": "AS-225",
        "slug": "kv-cache-aware-routing",
        "concept": "KV Cache-Aware Routing",
        "definition": "Intelligent inference request routing that directs queries to the instance holding the most relevant KV cache state, minimizing recomputation and latency.",
        "aliases": ["cache-aware routing", "KV routing"],
        "category": "llm-inference",
        "category_name": "LLM Inference",
        "tags": ["kv-cache", "routing", "inference", "llm", "optimization"],
        "svg_body": '<rect x="2" y="9" width="5" height="6" rx="1"/><rect x="9" y="3" width="5" height="6" rx="1"/><rect x="9" y="15" width="5" height="6" rx="1"/><rect x="17" y="9" width="5" height="6" rx="1"/><path d="M7 12h2M16 12h2M11 9V7M11 15v2"/>',
    },
    {
        "id": "AS-226",
        "slug": "eval-driven-development",
        "concept": "Eval-Driven Development",
        "definition": "A software methodology where evaluations are the primary development loop — writing evals before code and using eval results to drive all engineering decisions.",
        "aliases": ["EDD", "eval-first development"],
        "category": "ai-engineering",
        "category_name": "AI Engineering",
        "tags": ["evals", "development", "methodology", "testing", "ai"],
        "svg_body": '<circle cx="12" cy="12" r="9"/><path d="M12 3v9l5 3"/><circle cx="12" cy="12" r="2" fill="#9F792C"/><path d="M8 7l-1-3M16 7l1-3M19 16l3 1M5 16l-3 1"/>',
    },
    {
        "id": "AS-227",
        "slug": "agent-bytecode",
        "concept": "Agent Bytecode",
        "definition": "Domain-specific intermediate languages designed as substrates for AI agents, enabling portable, verifiable, and optimizable agent programs across runtimes.",
        "aliases": ["agent DSL", "agent intermediate representation"],
        "category": "agent-infrastructure",
        "category_name": "Agent Infrastructure",
        "tags": ["bytecode", "DSL", "agent", "language", "substrate"],
        "svg_body": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9h2M7 12h2M7 15h2"/><path d="M13 9l2 3-2 3"/><path d="M15 9l2 3-2 3"/>',
    },
]

# Write all files
for c in concepts:
    slug = c['slug']
    svg_content = svg(c.pop('svg_body'))
    
    # Write SVG
    svg_path = ICONS_DIR / f"{slug}.svg"
    with open(svg_path, 'w') as f:
        f.write(svg_content)
    
    # Write JSON
    json_data = {
        "id": c["id"],
        "slug": c["slug"],
        "concept": c["concept"],
        "definition": c["definition"],
        "aliases": c["aliases"],
        "category": c["category"],
        "category_name": c["category_name"],
        "sources": [],
        "svg": f"{slug}.svg",
        "tags": c["tags"]
    }
    json_path = ICONS_DIR / f"{slug}.json"
    with open(json_path, 'w') as f:
        json.dump(json_data, f, indent=2)
    
    print(f"✓ {slug}")

print(f"\nGenerated {len(concepts)} icon pairs")
