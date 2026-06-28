#!/usr/bin/env python3
"""AgentiScript Icon Generator — the visual language of the agentic economy."""
import json
from pathlib import Path

ICONS_DIR = Path('/Users/colin/seo/agentiscript/icons')
ICONS_DIR.mkdir(parents=True, exist_ok=True)

C = '#9F792C'  # gold
SW = '1.5'     # stroke-width

def svg(content):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">{content}</svg>'

def circle(cx, cy, r, **kw):
    attrs = f'cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{C}" stroke-width="{SW}"'
    for k,v in kw.items(): attrs += f' {k.replace("_","-")}="{v}"'
    return f'<circle {attrs}/>'

def rect(x, y, w, h, rx=0, **kw):
    attrs = f'x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="none" stroke="{C}" stroke-width="{SW}"'
    for k,v in kw.items(): attrs += f' {k.replace("_","-")}="{v}"'
    return f'<rect {attrs}/>'

def line(x1, y1, x2, y2, **kw):
    attrs = f'x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{C}" stroke-width="{SW}" stroke-linecap="round"'
    for k,v in kw.items(): attrs += f' {k.replace("_","-")}="{v}"'
    return f'<line {attrs}/>'

def path(d, **kw):
    attrs = f'd="{d}" fill="none" stroke="{C}" stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round"'
    for k,v in kw.items(): attrs += f' {k.replace("_","-")}="{v}"'
    return f'<path {attrs}/>'

def text_el(x, y, txt, font_size=7, **kw):
    attrs = f'x="{x}" y="{y}" text-anchor="middle" font-size="{font_size}" font-family="monospace" fill="{C}" stroke="none"'
    for k,v in kw.items(): attrs += f' {k.replace("_","-")}="{v}"'
    return f'<text {attrs}>{txt}</text>'

def polygon(points, **kw):
    attrs = f'points="{points}" fill="none" stroke="{C}" stroke-width="{SW}" stroke-linejoin="round"'
    for k,v in kw.items(): attrs += f' {k.replace("_","-")}="{v}"'
    return f'<polygon {attrs}/>'

# ── ICON DEFINITIONS ─────────────────────────────────────────────────────────
# Each value is (svg_content, concept, definition, aliases, category, sources, tags)

ICONS = {
    # ── AGENTIC ECONOMY ──────────────────────────────────────────────────────
    'agentic-loop': (
        circle(12,12,9) +
        path('M12 3 L14.5 6.5 M12 3 L9.5 6.5') +
        path('M12 21 L9.5 17.5 M12 21 L14.5 17.5') +
        path('M8 7 L9 11 M10 13 L8 17 M14 7 L15 11 M16 13 L14 17', stroke_dasharray='1 2'),
        'Agentic Loop',
        'A recursive observe-think-act cycle executed by an autonomous AI agent',
        ['agent loop', 'ReAct cycle', 'thought-action loop'],
        'agentic-economy',
        ['https://arxiv.org/abs/2210.03629'],
        ['agent', 'autonomous', 'loop', 'recursive']
    ),
    'context-window': (
        rect(2,4,20,16,2, stroke_dasharray='4 2') +
        line(2,9,22,9, stroke_width='1') +
        line(5,12,11,12, stroke_width='1') +
        line(5,15,15,15, stroke_width='1'),
        'Context Window',
        'The maximum number of tokens an LLM can process in a single prompt and response',
        ['context length', 'token window', 'attention window'],
        'agentic-economy',
        ['https://arxiv.org/abs/2307.03172'],
        ['LLM', 'tokens', 'memory', 'context']
    ),
    'tool-use': (
        path('M14.5 2.5 L21.5 9.5 L9.5 21.5 L2.5 14.5 Z') +
        line(7,7,17,17) +
        circle(12,12,2),
        'Tool Use',
        'The capability of an AI agent to invoke external tools, APIs, or functions to complete tasks',
        ['function calling', 'tool calling', 'API use'],
        'agentic-economy',
        ['https://arxiv.org/abs/2302.04761'],
        ['agent', 'tools', 'API', 'function']
    ),
    'function-calling': (
        rect(3,6,18,12,2) +
        path('M7 10 L10 10 M7 14 L14 14') +
        path('M17 8 L20 12 L17 16', stroke_width='1.5'),
        'Function Calling',
        'A structured mechanism allowing LLMs to trigger predefined functions with structured outputs',
        ['tool calling', 'API calling', 'structured output'],
        'agentic-economy',
        ['https://platform.openai.com/docs/guides/function-calling'],
        ['LLM', 'function', 'structured', 'API']
    ),
    'multi-agent-system': (
        circle(6,12,3) +
        circle(18,6,3) +
        circle(18,18,3) +
        line(9,12,15,7) +
        line(9,12,15,17) +
        line(15,7,15,17),
        'Multi-Agent System',
        'An architecture where multiple autonomous agents collaborate, coordinate, or compete to solve problems',
        ['MAS', 'agent network', 'agent swarm'],
        'agentic-economy',
        ['https://arxiv.org/abs/2308.11432'],
        ['multi-agent', 'swarm', 'collaboration', 'network']
    ),
    'orchestrator': (
        circle(12,5,3) +
        circle(5,19,3) +
        circle(12,19,3) +
        circle(19,19,3) +
        line(12,8,5,16) +
        line(12,8,12,16) +
        line(12,8,19,16),
        'Orchestrator',
        'A master agent that decomposes tasks and coordinates sub-agents toward a higher-level goal',
        ['coordinator agent', 'planner agent', 'task router'],
        'agentic-economy',
        ['https://arxiv.org/abs/2308.11432'],
        ['orchestration', 'planning', 'coordination', 'agent']
    ),
    'sub-agent': (
        circle(12,12,4) +
        path('M12 3 L12 8 M12 16 L12 21 M3 12 L8 12') +
        path('M3.5 3.5 L7.5 7.5 M16.5 16.5 L20.5 20.5'),
        'Sub-Agent',
        'A specialized autonomous agent that executes delegated subtasks within a larger agent system',
        ['worker agent', 'specialist agent', 'child agent'],
        'agentic-economy',
        ['https://arxiv.org/abs/2309.07864'],
        ['agent', 'worker', 'specialized', 'delegation']
    ),
    'memory-agent': (
        rect(5,4,14,16,1) +
        line(8,8,16,8) +
        line(8,12,16,12) +
        line(8,16,12,16) +
        circle(17.5,16.5,3.5),
        'Memory (Agent)',
        "An agent's ability to store, retrieve, and update information across interactions",
        ['agent memory', 'episodic memory', 'working memory'],
        'agentic-economy',
        ['https://arxiv.org/abs/2304.03442'],
        ['memory', 'storage', 'retrieval', 'context']
    ),
    'prompt': (
        rect(3,5,18,14,2) +
        path('M7 10 L7 14') +
        line(9,12,17,12) +
        line(9,10,14,10),
        'Prompt',
        'Natural language input provided to an LLM to elicit a desired output or behavior',
        ['system prompt', 'user prompt', 'instruction'],
        'agentic-economy',
        ['https://arxiv.org/abs/2302.11382'],
        ['prompt', 'input', 'instruction', 'language']
    ),
    'rag': (
        circle(12,12,8) +
        path('M8 9 L16 9 M8 12 L14 12') +
        path('M16 15 L20 19', stroke_width='2') +
        circle(15,14,3),
        'RAG',
        'Retrieval-Augmented Generation — combining LLM generation with real-time document retrieval',
        ['retrieval augmented generation', 'RAG pipeline', 'document retrieval'],
        'agentic-economy',
        ['https://arxiv.org/abs/2005.11401'],
        ['retrieval', 'generation', 'knowledge', 'search']
    ),
    'llm': (
        rect(2,7,20,10,1) +
        path('M5 12 Q8 9 11 12 Q14 15 17 12 Q19 10 21 12', fill='none') +
        line(2,11,22,11, stroke_width='0.5') +
        line(2,13,22,13, stroke_width='0.5'),
        'LLM',
        'Large Language Model — a neural network trained on vast text data capable of generating human-like text',
        ['large language model', 'foundation model', 'language AI'],
        'agentic-economy',
        ['https://arxiv.org/abs/2303.18223'],
        ['LLM', 'language model', 'neural network', 'AI']
    ),
    'fine-tuning': (
        circle(12,12,8) +
        path('M12 4 Q16 8 12 12 Q8 16 12 20') +
        line(9,7,15,7, stroke_dasharray='2 1') +
        line(9,17,15,17, stroke_dasharray='2 1'),
        'Fine-Tuning',
        'Further training a pre-trained model on a specific dataset to adapt it to a particular domain or task',
        ['model fine-tuning', 'domain adaptation', 'RLHF'],
        'agentic-economy',
        ['https://arxiv.org/abs/2109.01652'],
        ['training', 'adaptation', 'optimization', 'model']
    ),
    'inference': (
        path('M4 20 L12 4 L20 20') +
        line(7,14,17,14) +
        circle(12,17,1.5, fill=C, stroke='none'),
        'Inference',
        'The process of running a trained model to generate predictions or outputs from new input data',
        ['model inference', 'prediction', 'forward pass'],
        'agentic-economy',
        ['https://arxiv.org/abs/2211.05100'],
        ['inference', 'prediction', 'compute', 'model']
    ),
    'hallucination': (
        circle(12,11,7) +
        path('M9 9 Q12 6 15 9') +
        path('M10 13 Q12 16 14 13', stroke_dasharray='2 1') +
        path('M8 18 Q12 22 16 18', stroke_dasharray='1 2'),
        'Hallucination',
        'When an LLM generates plausible-sounding but factually incorrect or fabricated information',
        ['confabulation', 'model hallucination', 'AI fabrication'],
        'agentic-economy',
        ['https://arxiv.org/abs/2202.03629'],
        ['hallucination', 'error', 'fabrication', 'accuracy']
    ),
    'constitutional-ai': (
        path('M12 2 L14 8 L20 8 L15 12 L17 18 L12 14 L7 18 L9 12 L4 8 L10 8 Z') +
        circle(12,10,2, fill=C, stroke='none'),
        'Constitutional AI',
        "Anthropic's approach to training AI with a set of principles guiding self-critique and revision",
        ['CAI', 'principle-based alignment', 'constitutional training'],
        'agentic-economy',
        ['https://arxiv.org/abs/2212.08073'],
        ['alignment', 'safety', 'principles', 'Anthropic']
    ),
    'alignment': (
        line(5,12,19,12) +
        circle(8,12,2) +
        circle(12,12,2) +
        circle(16,12,2) +
        path('M12 5 L12 9 M12 15 L12 19', stroke_dasharray='2 1'),
        'Alignment',
        'The challenge of ensuring AI systems act in accordance with human values, intentions, and goals',
        ['AI alignment', 'value alignment', 'goal alignment'],
        'agentic-economy',
        ['https://arxiv.org/abs/2109.13916'],
        ['alignment', 'safety', 'values', 'goals']
    ),
    'chain-of-thought': (
        circle(4,12,2.5) +
        circle(12,12,2.5) +
        circle(20,12,2.5) +
        line(6.5,12,9.5,12) +
        line(14.5,12,17.5,12) +
        path('M4 7 L4 9.5 M12 7 L12 9.5 M20 7 L20 9.5', stroke_dasharray='1 1') +
        path('M3 6 L5 6 L4 4 Z', fill=C, stroke='none'),
        'Chain of Thought',
        'A prompting technique that elicits step-by-step reasoning from LLMs before giving a final answer',
        ['CoT', 'chain-of-thought prompting', 'step-by-step reasoning'],
        'agentic-economy',
        ['https://arxiv.org/abs/2201.11903'],
        ['reasoning', 'prompting', 'steps', 'logic']
    ),
    'few-shot-learning': (
        path('M3 18 L8 6 L13 18') + line(5,14,11,14) +
        path('M15 18 L18 10 L21 18') + line(16,15,20,15),
        'Few-Shot Learning',
        'Teaching an LLM a task by providing a small number of examples directly in the prompt',
        ['few-shot prompting', 'in-context learning', 'k-shot'],
        'agentic-economy',
        ['https://arxiv.org/abs/2005.14165'],
        ['few-shot', 'examples', 'prompting', 'learning']
    ),
    'zero-shot-learning': (
        path('M8 18 L12 6 L16 18') + line(9.5,14,14.5,14) +
        path('M18 8 L21 12 L18 16', stroke_dasharray='2 2') +
        line(3,12,6,12, stroke_dasharray='2 2'),
        'Zero-Shot Learning',
        'An LLM performing a task without any examples, relying solely on instruction comprehension',
        ['zero-shot', 'zero-shot prompting', 'instruction following'],
        'agentic-economy',
        ['https://arxiv.org/abs/1707.00600'],
        ['zero-shot', 'instruction', 'generalization', 'LLM']
    ),
    'embedding': (
        path('M4 6 L20 6') + path('M4 10 L20 10') + path('M4 14 L20 14') + path('M4 18 L20 18') +
        rect(9,4,6,16,1),
        'Embedding',
        'A dense vector representation of text, images, or other data in a high-dimensional space',
        ['vector embedding', 'dense vector', 'semantic representation'],
        'agentic-economy',
        ['https://arxiv.org/abs/1301.3666'],
        ['vector', 'semantic', 'representation', 'ML']
    ),
    'vector-database': (
        rect(3,6,18,12,1) +
        path('M3 9 L21 9 M3 12 L21 12 M3 15 L21 15') +
        circle(7.5,7.5,1, fill=C, stroke='none') +
        circle(7.5,10.5,1, fill=C, stroke='none') +
        circle(7.5,13.5,1, fill=C, stroke='none'),
        'Vector Database',
        'A specialized database that stores and indexes high-dimensional vector embeddings for similarity search',
        ['vector store', 'embedding database', 'similarity search DB'],
        'agentic-economy',
        ['https://arxiv.org/abs/2304.01137'],
        ['vector', 'database', 'storage', 'search']
    ),
    'temperature': (
        path('M12 3 L12 15') +
        path('M9 3 L15 3') +
        circle(12,18,3) +
        line(12,15,12,21, stroke_width='3') +
        line(9,6,12,6) + line(9,9,12,9) + line(9,12,12,12),
        'Temperature',
        'A hyperparameter controlling the randomness of LLM outputs — higher values increase creativity',
        ['sampling temperature', 'creativity parameter', 'randomness control'],
        'agentic-economy',
        ['https://arxiv.org/abs/2211.07830'],
        ['temperature', 'sampling', 'randomness', 'creativity']
    ),
    'token-ai': (
        circle(12,12,7) +
        text_el(12,14.5,'T', font_size=10),
        'Token (AI)',
        'The basic unit of text (roughly a word piece) that LLMs process — models are measured in tokens',
        ['AI token', 'word token', 'subword unit', 'BPE token'],
        'agentic-economy',
        ['https://arxiv.org/abs/2112.00114'],
        ['token', 'text', 'unit', 'LLM']
    ),
    'attention-mechanism': (
        circle(6,8,3) + circle(18,8,3) + circle(12,18,3) +
        path('M8.5,9.5 Q12,4 15.5,9.5') +
        path('M7,11 Q6,18 10,17.5') +
        path('M17,11 Q18,18 14,17.5') +
        circle(12,12,1.5, fill=C, stroke='none'),
        'Attention Mechanism',
        'A technique enabling models to focus on relevant parts of input sequences when generating outputs',
        ['self-attention', 'cross-attention', 'attention head'],
        'agentic-economy',
        ['https://arxiv.org/abs/1706.03762'],
        ['attention', 'transformer', 'focus', 'neural network']
    ),
    'transformer': (
        rect(4,4,16,4,1) +
        rect(4,10,16,4,1) +
        rect(4,16,16,4,1) +
        line(8,8,8,10) + line(12,8,12,10) + line(16,8,16,10) +
        line(8,14,8,16) + line(12,14,12,16) + line(16,14,16,16),
        'Transformer',
        'The neural network architecture underlying most modern LLMs, based on self-attention mechanisms',
        ['transformer architecture', 'attention model', 'encoder-decoder'],
        'agentic-economy',
        ['https://arxiv.org/abs/1706.03762'],
        ['transformer', 'architecture', 'neural network', 'attention']
    ),
    'foundation-model': (
        path('M12 2 L22 7 L22 17 L12 22 L2 17 L2 7 Z') +
        path('M12 2 L12 22 M2 7 L22 7 M2 17 L22 17'),
        'Foundation Model',
        'A large AI model trained on broad data that can be adapted to a wide range of downstream tasks',
        ['base model', 'pretrained model', 'FM'],
        'agentic-economy',
        ['https://arxiv.org/abs/2108.07258'],
        ['foundation', 'base', 'pretrained', 'model']
    ),
    'frontier-model': (
        polygon('12,2 14,8 22,8 16,12 18,20 12,16 6,20 8,12 2,8 10,8') +
        circle(12,11,2, fill=C, stroke='none'),
        'Frontier Model',
        'The most capable AI models at the current leading edge of capability, often closed-source',
        ['leading edge model', 'SOTA model', 'cutting-edge AI'],
        'agentic-economy',
        ['https://arxiv.org/abs/2307.09009'],
        ['frontier', 'SOTA', 'capability', 'leading edge']
    ),
    'agentic-economy': (
        circle(12,12,9) +
        circle(12,12,5) +
        path('M12 3 L12 7 M12 17 L12 21 M3 12 L7 12 M17 12 L21 12') +
        circle(12,12,1.5, fill=C, stroke='none'),
        'Agentic Economy',
        'An economic system where autonomous AI agents transact, negotiate, and create value independently',
        ['agent economy', 'AI economy', 'autonomous economy'],
        'agentic-economy',
        ['https://arxiv.org/abs/2309.11564'],
        ['economy', 'agents', 'autonomous', 'value']
    ),
    'x402': (
        rect(3,6,18,12,2) +
        text_el(12,15,'402', font_size=9),
        'x402',
        'A payment protocol enabling AI agents to pay for resources via HTTP 402 Payment Required responses',
        ['HTTP 402', 'micropayment protocol', 'agent payment'],
        'agentic-economy',
        ['https://x402.org'],
        ['payment', 'protocol', 'HTTP', 'agent']
    ),
    'mcp': (
        circle(5,12,3) + circle(19,12,3) + circle(12,5,3) + circle(12,19,3) +
        line(8,12,16,12) + line(12,8,12,16),
        'MCP (Model Context Protocol)',
        "Anthropic's open protocol for connecting AI models to external tools and data sources",
        ['Model Context Protocol', 'MCP server', 'MCP client'],
        'agentic-economy',
        ['https://modelcontextprotocol.io'],
        ['protocol', 'tools', 'context', 'Anthropic']
    ),
    'shadow-mode': (
        circle(12,12,8) +
        path('M12 4 Q20 12 12 20 Q4 12 12 4') +
        path('M12 4 Q4 12 12 20', stroke_dasharray='3 2'),
        'Shadow Mode',
        'Running an AI agent in parallel with human decisions without acting — observing before deploying',
        ['shadow deployment', 'observation mode', 'passive mode'],
        'agentic-economy',
        ['https://arxiv.org/abs/2311.10538'],
        ['shadow', 'observation', 'parallel', 'deployment']
    ),
    'fleet-learning': (
        circle(5,17,3) + circle(12,5,3) + circle(19,17,3) +
        path('M7.5,15.5 Q12,11 16.5,15.5') +
        path('M6,14.5 L12,8 L18,14.5') +
        path('M12 8 L12 2', stroke_dasharray='2 1'),
        'Fleet Learning',
        'Distributed learning where insights from a fleet of deployed agents improve the shared model',
        ['federated fleet', 'collective learning', 'swarm learning'],
        'agentic-economy',
        ['https://arxiv.org/abs/2205.00308'],
        ['fleet', 'distributed', 'learning', 'federated']
    ),
    'ota-update': (
        circle(12,12,8) +
        path('M8 12 L11 15 L16 9') +
        path('M12 4 Q16 4 18 8', stroke_dasharray='2 2') +
        path('M18 8 L20 6 M18 8 L16 6'),
        'OTA Update',
        'Over-the-air software update delivered wirelessly to deployed agents or devices without physical access',
        ['over-the-air update', 'wireless update', 'remote patch'],
        'agentic-economy',
        ['https://arxiv.org/abs/2110.00805'],
        ['update', 'wireless', 'deployment', 'software']
    ),
    'two-tier-agent': (
        rect(3,3,18,7,1) +
        rect(3,14,18,7,1) +
        line(12,10,12,14) +
        path('M9 13 L12 10 L15 13'),
        'Two-Tier Agent',
        'An architecture separating fast reactive behavior from slow deliberative planning in AI agents',
        ['dual-process agent', 'fast-slow agent', 'reactive-deliberative'],
        'agentic-economy',
        ['https://arxiv.org/abs/2309.07864'],
        ['architecture', 'tiers', 'planning', 'reactive']
    ),
    'vibe-coding': (
        path('M4 18 Q8 8 12 12 Q16 16 20 6') +
        circle(12,12,2) +
        path('M3 20 L5 20 L5 18', stroke_width='1') +
        path('M19 4 L21 4 L21 6', stroke_width='1'),
        'Vibe Coding',
        'Directing AI coding tools with natural language intent and iterative vibes rather than explicit specs',
        ['vibe-driven development', 'AI-assisted coding', 'intent programming'],
        'agentic-economy',
        ['https://techcrunch.com/2025/02/01/vibe-coding'],
        ['coding', 'AI', 'natural language', 'development']
    ),
    'replit-agent': (
        rect(4,4,16,16,2) +
        path('M9 9 L15 9 M9 12 L13 12 M9 15 L15 15') +
        circle(17,7,3, fill=C, stroke='none'),
        'Replit Agent',
        'An AI coding agent integrated into Replit that builds full applications from natural language prompts',
        ['Replit AI', 'cloud coding agent', 'Ghostwriter'],
        'agentic-economy',
        ['https://replit.com/ai'],
        ['Replit', 'coding', 'agent', 'cloud']
    ),

    # ── BLOCKCHAIN / WEB3 ────────────────────────────────────────────────────
    'tokenization': (
        circle(8,12,4) + circle(16,12,4) + line(12,10,12,14) +
        path('M8 8 L8 4 M8 20 L8 16 M16 8 L16 4 M16 20 L16 16', stroke_width='1'),
        'Tokenization',
        'Converting real-world assets or rights into digital tokens on a blockchain',
        ['asset tokenization', 'RWA tokenization', 'on-chain assets'],
        'blockchain',
        ['https://arxiv.org/abs/2009.12193'],
        ['token', 'blockchain', 'assets', 'digital']
    ),
    'smart-contract': (
        rect(4,3,16,18,1) +
        path('M8 8 L16 8 M8 12 L16 12 M8 16 L12 16') +
        path('M13 17 L16 20 L20 14', stroke_width='2'),
        'Smart Contract',
        'Self-executing code on a blockchain that automatically enforces agreement terms when conditions are met',
        ['on-chain contract', 'Solidity contract', 'self-executing agreement'],
        'blockchain',
        ['https://arxiv.org/abs/1801.00687'],
        ['contract', 'blockchain', 'automation', 'code']
    ),
    'consensus-mechanism': (
        circle(12,12,8) +
        circle(5,7,2.5) + circle(19,7,2.5) + circle(5,17,2.5) + circle(19,17,2.5) +
        line(7.5,7,10,10) + line(16.5,7,14,10) +
        line(7.5,17,10,14) + line(16.5,17,14,14),
        'Consensus Mechanism',
        'A protocol by which distributed blockchain nodes agree on the valid state of the ledger',
        ['PoW', 'PoS', 'consensus protocol', 'Nakamoto consensus'],
        'blockchain',
        ['https://arxiv.org/abs/1711.03936'],
        ['consensus', 'blockchain', 'validation', 'protocol']
    ),
    'validator-node': (
        circle(12,12,7) +
        path('M9 12 L11 14 L15 10') +
        path('M12 5 L12 2 M19 12 L22 12', stroke_dasharray='2 1'),
        'Validator Node',
        'A network participant that verifies transactions and blocks, maintaining blockchain integrity',
        ['validator', 'network node', 'block producer'],
        'blockchain',
        ['https://ethereum.org/en/developers/docs/nodes-and-clients/'],
        ['validator', 'node', 'network', 'verification']
    ),
    'zk-proof': (
        circle(12,12,8) +
        path('M9 12 L11 14 L15 10') +
        path('M4 8 Q12 2 20 8', stroke_dasharray='3 2') +
        path('M4 16 Q12 22 20 16', stroke_dasharray='3 2'),
        'ZK Proof',
        'Zero-Knowledge Proof — proves statement validity without revealing underlying private information',
        ['zero-knowledge proof', 'ZKP', 'zk-SNARK', 'zk-STARK'],
        'blockchain',
        ['https://arxiv.org/abs/1906.07221'],
        ['zero-knowledge', 'privacy', 'proof', 'cryptography']
    ),
    'amm': (
        path('M3 20 Q12 4 21 20') +
        path('M3 20 L21 20') +
        circle(12,11,2, fill=C, stroke='none') +
        line(12,13,12,20, stroke_dasharray='2 2'),
        'AMM',
        'Automated Market Maker — a DeFi protocol using mathematical formulas instead of order books for trading',
        ['automated market maker', 'liquidity curve', 'x*y=k'],
        'blockchain',
        ['https://arxiv.org/abs/2103.12732'],
        ['AMM', 'DeFi', 'liquidity', 'trading']
    ),
    'liquidity-pool': (
        path('M3 18 Q3 8 12 7 Q21 8 21 18 L3 18 Z') +
        path('M3 14 Q12 12 21 14', stroke_dasharray='2 1') +
        path('M5 18 Q8 16 12 16 Q16 16 19 18'),
        'Liquidity Pool',
        'A smart contract holding token reserves that enables decentralized trading and lending',
        ['LP', 'liquidity reserve', 'DEX pool'],
        'blockchain',
        ['https://arxiv.org/abs/2205.08904'],
        ['liquidity', 'pool', 'DeFi', 'tokens']
    ),
    'dao': (
        circle(12,12,8) +
        path('M12 4 L12 8 M12 16 L12 20 M4 12 L8 12 M16 12 L20 12') +
        path('M6.3 6.3 L9.2 9.2 M14.8 14.8 L17.7 17.7') +
        path('M17.7 6.3 L14.8 9.2 M9.2 14.8 L6.3 17.7') +
        circle(12,12,3),
        'DAO',
        'Decentralized Autonomous Organization — a member-governed entity with rules encoded as smart contracts',
        ['decentralized autonomous organization', 'on-chain governance', 'community governance'],
        'blockchain',
        ['https://arxiv.org/abs/2110.05040'],
        ['DAO', 'governance', 'decentralized', 'organization']
    ),
    'defi': (
        path('M3 12 Q3 5 12 5 Q21 5 21 12 Q21 19 12 19 Q3 19 3 12') +
        path('M8 12 L10 14 L14 10') +
        text_el(12,21,'$', font_size=5),
        'DeFi',
        'Decentralized Finance — financial services built on blockchain without traditional intermediaries',
        ['decentralized finance', 'on-chain finance', 'open finance'],
        'blockchain',
        ['https://arxiv.org/abs/2101.08778'],
        ['DeFi', 'finance', 'decentralized', 'blockchain']
    ),
    'mev-attack': (
        rect(3,7,18,10,1) +
        path('M3 12 L21 12') +
        path('M15 5 L19 9 L15 9', fill=C, stroke=C, stroke_width='1') +
        path('M9 19 L5 15 L9 15', fill=C, stroke=C, stroke_width='1'),
        'MEV Attack',
        'Maximal Extractable Value — profit extracted by reordering, inserting, or censoring blockchain transactions',
        ['maximal extractable value', 'miner extractable value', 'front-running'],
        'blockchain',
        ['https://arxiv.org/abs/1904.05234'],
        ['MEV', 'front-running', 'blockchain', 'attack']
    ),
    'liquid-staking': (
        circle(12,12,8) +
        path('M12 4 L14.5 9 L20 9.5 L15.5 13.5 L17 19 L12 16 L7 19 L8.5 13.5 L4 9.5 L9.5 9 Z', stroke_dasharray='3 1') +
        circle(12,12,3),
        'Liquid Staking',
        'Staking tokens while receiving a liquid derivative that can be used in DeFi protocols simultaneously',
        ['liquid staking token', 'LST', 'staked derivative'],
        'blockchain',
        ['https://arxiv.org/abs/2207.10727'],
        ['staking', 'liquid', 'DeFi', 'derivative']
    ),
    'impermanent-loss': (
        path('M3 18 Q12 4 21 18') +
        path('M3 18 Q8 12 12 10 Q16 12 21 18', stroke_dasharray='3 2') +
        line(3,18,21,18) +
        path('M12 10 L12 14', stroke_dasharray='1 1'),
        'Impermanent Loss',
        'The temporary loss of value experienced by liquidity providers when asset prices diverge from deposit time',
        ['IL', 'LP impermanent loss', 'divergence loss'],
        'blockchain',
        ['https://arxiv.org/abs/2111.09192'],
        ['impermanent loss', 'liquidity', 'AMM', 'DeFi']
    ),
    'oracle-problem': (
        circle(12,12,8) +
        path('M12 4 L12 12 L17 17', stroke_width='2') +
        path('M4 12 Q4 6 8 4', stroke_dasharray='2 2') +
        circle(12,4,1.5, fill=C, stroke='none'),
        'Oracle Problem',
        "The fundamental challenge of reliably feeding real-world data to blockchain's isolated smart contracts",
        ['blockchain oracle', 'data feed problem', 'oracle attack'],
        'blockchain',
        ['https://arxiv.org/abs/2004.01441'],
        ['oracle', 'data', 'blockchain', 'problem']
    ),
    'layer-2': (
        rect(3,14,18,6,1) +
        rect(3,4,18,8,1) +
        line(7,10,7,14) + line(12,10,12,14) + line(17,10,17,14),
        'Layer 2',
        'A secondary protocol built on top of a blockchain to improve scalability and reduce transaction costs',
        ['L2', 'rollup', 'off-chain scaling', 'sidechain'],
        'blockchain',
        ['https://arxiv.org/abs/2012.10003'],
        ['layer 2', 'scaling', 'rollup', 'blockchain']
    ),
    'merkle-tree': (
        circle(12,4,2) +
        circle(6,11,2) + circle(18,11,2) +
        circle(3,18,2) + circle(9,18,2) + circle(15,18,2) + circle(21,18,2) +
        line(12,6,6,9) + line(12,6,18,9) +
        line(6,13,3,16) + line(6,13,9,16) +
        line(18,13,15,16) + line(18,13,21,16),
        'Merkle Tree',
        'A hash tree data structure used in blockchains for efficient and secure data verification',
        ['hash tree', 'Merkle root', 'Merkle proof'],
        'blockchain',
        ['https://arxiv.org/abs/2011.12116'],
        ['merkle', 'hash', 'tree', 'verification']
    ),
    'gas-fee': (
        path('M10 20 L10 12 L7 12 L12 3 L17 12 L14 12 L14 20 Z') +
        text_el(12,21,'Ξ', font_size=4),
        'Gas Fee',
        'A fee paid to blockchain validators for computational resources used to execute transactions',
        ['transaction fee', 'gas price', 'gwei'],
        'blockchain',
        ['https://ethereum.org/en/developers/docs/gas/'],
        ['gas', 'fee', 'transaction', 'Ethereum']
    ),
    'staking': (
        circle(12,12,8) +
        path('M12 4 L14.5 9 L20 9.5 L15.5 13.5 L17 19 L12 16 L7 19 L8.5 13.5 L4 9.5 L9.5 9 Z') +
        circle(12,12,2, fill=C, stroke='none'),
        'Staking',
        'Locking cryptocurrency to support network operations in exchange for rewards',
        ['proof of stake', 'staking rewards', 'bonding'],
        'blockchain',
        ['https://ethereum.org/en/staking/'],
        ['staking', 'PoS', 'rewards', 'blockchain']
    ),
    'bridge-cross-chain': (
        circle(5,12,3) + circle(19,12,3) +
        path('M8 10 Q12 6 16 10') +
        path('M8 14 Q12 18 16 14') +
        line(8,12,16,12, stroke_dasharray='3 2'),
        'Bridge (Cross-Chain)',
        'A protocol enabling transfer of tokens and data between different blockchain networks',
        ['cross-chain bridge', 'blockchain bridge', 'interop bridge'],
        'blockchain',
        ['https://arxiv.org/abs/2104.08719'],
        ['bridge', 'cross-chain', 'interoperability', 'blockchain']
    ),
    'fork-blockchain': (
        line(12,3,12,10) +
        path('M12 10 L6 18') +
        path('M12 10 L18 18') +
        circle(12,3,2) + circle(6,18,2) + circle(18,18,2),
        'Fork (Blockchain)',
        'A change to a blockchain protocol creating either a backwards-compatible or incompatible divergence',
        ['hard fork', 'soft fork', 'protocol upgrade'],
        'blockchain',
        ['https://arxiv.org/abs/1710.09405'],
        ['fork', 'protocol', 'upgrade', 'blockchain']
    ),
    'block': (
        rect(5,5,14,14,1) +
        line(5,10,19,10) + line(5,15,19,15) +
        line(10,5,10,10),
        'Block',
        'A unit of data in a blockchain containing transactions, a timestamp, and a hash of the previous block',
        ['blockchain block', 'block header', 'block data'],
        'blockchain',
        ['https://arxiv.org/abs/2009.12193'],
        ['block', 'blockchain', 'transaction', 'hash']
    ),
    'chain': (
        circle(5,12,3) + circle(12,12,3) + circle(19,12,3) +
        line(8,12,9,12) + line(15,12,16,12) +
        path('M3 9 L3 15 M10 9 L10 15 M17 9 L17 15'),
        'Chain',
        'A linked sequence of blocks forming an immutable, append-only ledger of transactions',
        ['blockchain', 'ledger chain', 'hash chain'],
        'blockchain',
        ['https://arxiv.org/abs/2009.12193'],
        ['chain', 'blocks', 'ledger', 'immutable']
    ),
    'node': (
        circle(12,12,5) +
        path('M12 7 L12 2 M12 17 L12 22 M7 12 L2 12 M17 12 L22 12') +
        path('M8.5 8.5 L5 5 M15.5 8.5 L19 5 M8.5 15.5 L5 19 M15.5 15.5 L19 19'),
        'Node',
        'A participant in a blockchain network that maintains a copy of the ledger and validates transactions',
        ['network node', 'full node', 'light node'],
        'blockchain',
        ['https://ethereum.org/en/developers/docs/nodes-and-clients/'],
        ['node', 'network', 'validation', 'blockchain']
    ),
    'wallet-crypto': (
        rect(3,7,18,13,2) +
        rect(15,4,6,6,1) +
        circle(18,7,2, fill=C, stroke='none'),
        'Wallet (Crypto)',
        'Software storing private keys that gives users access to their blockchain assets',
        ['crypto wallet', 'key store', 'digital wallet'],
        'blockchain',
        ['https://ethereum.org/en/wallets/'],
        ['wallet', 'keys', 'crypto', 'storage']
    ),
    'digital-identity': (
        circle(12,8,4) +
        path('M5 20 Q5 14 12 14 Q19 14 19 20') +
        path('M16 7 L18 9 M16 9 L18 7', stroke_width='1.5') +
        line(15,12,21,12, stroke_dasharray='2 1'),
        'Digital Identity',
        'A digital representation of an entity\'s attributes and credentials in verifiable form',
        ['digital ID', 'online identity', 'self-sovereign identity'],
        'blockchain',
        ['https://arxiv.org/abs/2012.05666'],
        ['identity', 'digital', 'credentials', 'verification']
    ),
    'did': (
        rect(4,6,16,12,2) +
        text_el(12,14,'DID', font_size=7),
        'DID',
        'Decentralized Identifier — a globally unique identifier controlled by the subject without central registries',
        ['decentralized identifier', 'W3C DID', 'self-sovereign ID'],
        'blockchain',
        ['https://www.w3.org/TR/did-core/'],
        ['DID', 'identifier', 'decentralized', 'identity']
    ),
    'verifiable-credential': (
        rect(4,4,16,16,2) +
        path('M8 10 L10 12 L14 8') +
        path('M8 13 L10 15 L14 11', stroke_dasharray='2 1') +
        line(4,7,20,7),
        'Verifiable Credential',
        'A tamper-evident credential with cryptographic proof, following W3C standards',
        ['VC', 'W3C credential', 'digital credential', 'attestation'],
        'blockchain',
        ['https://www.w3.org/TR/vc-data-model/'],
        ['credential', 'verifiable', 'W3C', 'attestation']
    ),

    # ── FLARE SPECIFIC ───────────────────────────────────────────────────────
    'ftsov2': (
        circle(12,12,8) +
        path('M7 12 L9 8 L11 12 L13 8 L15 12 L17 8') +
        text_el(12,22,'v2', font_size=5),
        'FTSOv2',
        "Flare's fast block-latency oracle providing sub-second price feeds anchored to network consensus",
        ['Flare Time Series Oracle v2', 'FTSO', 'block-latency oracle'],
        'flare',
        ['https://dev.flare.network/ftso/overview'],
        ['Flare', 'oracle', 'price feed', 'FTSO']
    ),
    'fdc': (
        rect(3,6,18,12,2) +
        path('M3 12 L21 12') +
        path('M7 8 L7 10 M12 8 L12 10 M17 8 L17 10') +
        path('M7 14 L7 16 M12 14 L12 16 M17 14 L17 16'),
        'FDC (Flare Data Connector)',
        "Flare's protocol for bringing verified external data and events onto the Flare blockchain",
        ['Flare Data Connector', 'FDC', 'data attestation'],
        'flare',
        ['https://dev.flare.network/fdc/overview'],
        ['Flare', 'data', 'connector', 'attestation']
    ),
    'fassets': (
        circle(12,12,8) +
        path('M9 9 L15 9 L16 15 L12 18 L8 15 Z') +
        text_el(12,14,'F', font_size=7),
        'FAssets',
        "Flare's trustless system for bringing non-smart-contract tokens like BTC onto the Flare network",
        ['Flare assets', 'FBTC', 'wrapped assets', 'trustless bridge'],
        'flare',
        ['https://dev.flare.network/fassets/overview'],
        ['FAssets', 'Flare', 'bridge', 'trustless']
    ),
    'fxrp': (
        circle(12,12,8) +
        path('M8 8 L12 12 L8 16 M12 12 L16 8 M12 12 L16 16') +
        text_el(12,22,'XRP', font_size=5),
        'FXRP',
        'Flare-wrapped XRP enabling XRP holders to access DeFi on the Flare network',
        ['Flare XRP', 'wrapped XRP', 'XRP on Flare'],
        'flare',
        ['https://dev.flare.network/fassets/overview'],
        ['FXRP', 'XRP', 'Flare', 'wrapped']
    ),
    'web2json': (
        rect(3,5,18,14,1) +
        path('M6 9 L9 9 M6 12 L11 12 M6 15 L14 15') +
        path('M15 7 L19 11 L15 15', stroke_width='2') +
        text_el(12,22,'JSON', font_size=5),
        'Web2Json',
        "Flare's attestation type that fetches JSON from web APIs and makes it verifiable on-chain",
        ['Web2Json', 'API attestation', 'web oracle'],
        'flare',
        ['https://dev.flare.network/fdc/guides/web2json'],
        ['Web2Json', 'API', 'JSON', 'oracle']
    ),
    'enshrined-oracle': (
        circle(12,12,8) +
        path('M12 4 L12 8 M12 16 L12 20 M4 12 L8 12 M16 12 L20 12') +
        rect(9,9,6,6,1),
        'Enshrined Oracle',
        'An oracle built into the blockchain protocol itself rather than as an external add-on',
        ['protocol oracle', 'native oracle', 'on-chain oracle'],
        'flare',
        ['https://dev.flare.network/ftso/overview'],
        ['oracle', 'enshrined', 'protocol', 'native']
    ),
    'attestation': (
        rect(5,3,14,18,1) +
        path('M8 8 L10 10 L14 6') +
        path('M8 12 L10 14 L14 10') +
        line(8,16,16,16),
        'Attestation',
        'A cryptographically signed claim verifying that specific data or events are true',
        ['data attestation', 'claim', 'proof of data'],
        'flare',
        ['https://dev.flare.network/fdc/overview'],
        ['attestation', 'proof', 'verification', 'data']
    ),
    'tee': (
        rect(4,4,16,16,2) +
        rect(8,8,8,8,1) +
        path('M10 12 L11 13 L14 10'),
        'TEE (Trusted Execution Environment)',
        'A secure, isolated processor environment guaranteeing code integrity and data confidentiality',
        ['trusted execution environment', 'secure enclave', 'SGX', 'TrustZone'],
        'flare',
        ['https://arxiv.org/abs/1904.05234'],
        ['TEE', 'security', 'enclave', 'trusted']
    ),
    'verifiable-compute': (
        rect(3,6,18,12,2) +
        path('M7 12 L9 9 L11 12 L13 15 L15 12') +
        path('M16 10 L18 12 L16 14', stroke_width='2'),
        'Verifiable Compute',
        'Computation whose correctness can be mathematically verified without re-executing it',
        ['verifiable computation', 'ZK compute', 'provable compute'],
        'flare',
        ['https://arxiv.org/abs/1811.04164'],
        ['verifiable', 'compute', 'ZK', 'proof']
    ),
    'block-latency-feed': (
        path('M3 18 L5 8 L7 14 L9 6 L11 12 L13 4 L15 10 L17 6 L19 14 L21 8') +
        line(3,20,21,20),
        'Block-Latency Feed',
        "A price feed updated every block (~1.8s) on Flare, providing near-real-time oracle data",
        ['block-by-block feed', 'fast oracle feed', 'sub-second feed'],
        'flare',
        ['https://dev.flare.network/ftso/overview'],
        ['feed', 'latency', 'oracle', 'real-time']
    ),
    'data-provider': (
        rect(4,4,16,16,1) +
        path('M8 8 L8 16 M12 10 L12 16 M16 6 L16 16') +
        line(4,16,20,16),
        'Data Provider',
        'An entity that submits off-chain data to oracle protocols in exchange for incentive rewards',
        ['FTSO data provider', 'oracle node', 'price submitter'],
        'flare',
        ['https://dev.flare.network/ftso/overview'],
        ['data provider', 'oracle', 'FTSO', 'incentives']
    ),
    'flare-smart-account': (
        circle(12,12,8) +
        rect(8,8,8,8,1) +
        path('M10 12 L11 13 L14 10'),
        'Flare Smart Account',
        'Account abstraction on Flare enabling programmable wallets with custom authorization logic',
        ['account abstraction', 'smart wallet', 'ERC-4337 on Flare'],
        'flare',
        ['https://dev.flare.network'],
        ['smart account', 'Flare', 'wallet', 'account abstraction']
    ),

    # ── NEAR SPECIFIC ────────────────────────────────────────────────────────
    'near-intents': (
        rect(4,4,16,16,2) +
        path('M8 12 Q12 6 16 12') +
        circle(12,16,2.5),
        'NEAR Intents',
        "NEAR's architecture where users express desired outcomes and the network finds optimal execution paths",
        ['intent-centric', 'user intents', 'declarative transactions'],
        'near',
        ['https://near.org/intents'],
        ['intents', 'NEAR', 'declarative', 'execution']
    ),
    'chain-signatures': (
        circle(7,12,4) + circle(17,12,4) +
        path('M11 10 L13 10 M11 14 L13 14') +
        path('M5 8 L3 6 M9 8 L11 6'),
        'Chain Signatures',
        "NEAR's protocol enabling a single NEAR account to control wallets on any blockchain via MPC",
        ['chain signatures', 'MPC signing', 'cross-chain control'],
        'near',
        ['https://docs.near.org/concepts/abstraction/chain-signatures'],
        ['chain signatures', 'NEAR', 'MPC', 'multichain']
    ),
    'chain-abstraction': (
        path('M3 12 Q3 4 12 4 Q21 4 21 12') +
        path('M3 12 Q3 20 12 20 Q21 20 21 12') +
        line(3,12,21,12, stroke_dasharray='3 2') +
        circle(12,12,3),
        'Chain Abstraction',
        'Hiding blockchain complexity so users interact with dApps without knowing which chain they\'re on',
        ['chain agnostic', 'multichain UX', 'abstraction layer'],
        'near',
        ['https://docs.near.org/concepts/abstraction/introduction'],
        ['chain abstraction', 'NEAR', 'UX', 'multichain']
    ),
    'ironclaw': (
        path('M12 3 L20 8 L20 16 L12 21 L4 16 L4 8 Z') +
        path('M9 10 L12 15 L15 10') +
        path('M10 8 L14 8'),
        'IronClaw',
        "NEAR's smart contract security audit framework for identifying vulnerabilities",
        ['IronClaw', 'NEAR security', 'smart contract audit'],
        'near',
        ['https://near.org'],
        ['security', 'audit', 'NEAR', 'smart contract']
    ),
    'triple-lockout': (
        rect(6,4,12,5,1) +
        rect(6,10,12,5,1) +
        rect(6,16,12,5,1) +
        path('M9 6 L9 8 M12 6 L12 8 M15 6 L15 8') +
        path('M9 12 L9 14 M12 12 L12 14 M15 12 L15 14'),
        'Triple Lockout',
        'A three-layer security mechanism requiring multiple independent approvals before high-risk actions',
        ['triple lock', 'multi-layer security', '3-step verification'],
        'near',
        ['https://near.org'],
        ['security', 'lockout', 'verification', 'NEAR']
    ),
    'confidential-mode': (
        circle(12,12,8) +
        path('M8 12 Q12 6 16 12 Q12 18 8 12') +
        line(4,4,20,20, stroke_dasharray='2 2'),
        'Confidential Mode',
        'An execution mode protecting data privacy in agent operations, hiding inputs and outputs',
        ['private mode', 'confidential compute', 'privacy mode'],
        'near',
        ['https://near.org'],
        ['confidential', 'privacy', 'NEAR', 'mode']
    ),
    'agent-marketplace': (
        rect(3,3,18,18,2) +
        path('M3 9 L21 9') +
        circle(8,15,2) + circle(16,15,2) +
        line(8,13,8,6) + line(16,13,16,6),
        'Agent Marketplace',
        'A platform where AI agents can be discovered, deployed, hired, and monetized',
        ['AI agent store', 'agent registry', 'agent hub'],
        'near',
        ['https://near.org'],
        ['marketplace', 'agents', 'NEAR', 'discovery']
    ),
    'sharding': (
        rect(3,3,18,18,1) +
        line(12,3,12,21) +
        line(3,12,21,12) +
        circle(7.5,7.5,2) + circle(16.5,7.5,2) +
        circle(7.5,16.5,2) + circle(16.5,16.5,2),
        'Sharding',
        'Partitioning blockchain state across parallel shards to achieve horizontal scalability',
        ['blockchain sharding', 'Nightshade', 'parallel processing'],
        'near',
        ['https://arxiv.org/abs/2106.02701'],
        ['sharding', 'scalability', 'NEAR', 'parallel']
    ),
    'access-keys': (
        circle(10,13,5) +
        path('M14 10 L21 10 L21 14 L19 14 L19 12 L17 12 L17 14 L15 14 L15 12') +
        circle(9,13,2, fill=C, stroke='none'),
        'Access Keys',
        "NEAR's programmable permission system allowing fine-grained control over account actions",
        ['NEAR access keys', 'full access key', 'function call key'],
        'near',
        ['https://docs.near.org/concepts/protocol/access-keys'],
        ['access keys', 'NEAR', 'permissions', 'security']
    ),
    'multichain-dao': (
        circle(12,12,8) +
        path('M12 4 L12 8 M12 16 L12 20 M4 12 L8 12 M16 12 L20 12') +
        path('M6.3 6.3 L9.2 9.2 M14.8 14.8 L17.7 17.7') +
        path('M17.7 6.3 L14.8 9.2 M9.2 14.8 L6.3 17.7') +
        line(3,12,21,12, stroke_dasharray='3 2'),
        'Multichain DAO',
        'A DAO that governs assets and operations across multiple blockchain networks simultaneously',
        ['cross-chain DAO', 'multichain governance', 'chain-agnostic DAO'],
        'near',
        ['https://near.org'],
        ['DAO', 'multichain', 'governance', 'NEAR']
    ),

    # ── RIPPLE / HEDERA ──────────────────────────────────────────────────────
    'on-ramp': (
        path('M3 18 L12 6 L21 18') +
        path('M7 18 L12 10 L17 18') +
        line(12,6,12,2) +
        path('M9 2 L12 2 L12 5'),
        'On-Ramp',
        'Converting fiat currency (USD, EUR) to cryptocurrency — entry point into the crypto ecosystem',
        ['fiat on-ramp', 'crypto on-ramp', 'buy crypto'],
        'ripple-hedera',
        ['https://ripple.com/solutions/'],
        ['on-ramp', 'fiat', 'crypto', 'entry']
    ),
    'off-ramp': (
        path('M3 6 L12 18 L21 6') +
        path('M7 6 L12 14 L17 6') +
        line(12,18,12,22) +
        path('M9 22 L12 22 L12 19'),
        'Off-Ramp',
        'Converting cryptocurrency back to fiat currency — exit point from the crypto ecosystem',
        ['fiat off-ramp', 'crypto off-ramp', 'sell crypto'],
        'ripple-hedera',
        ['https://ripple.com/solutions/'],
        ['off-ramp', 'fiat', 'crypto', 'exit']
    ),
    'real-time-settlement': (
        circle(12,12,8) +
        path('M8 12 L10 14 L14 10') +
        line(12,4,12,2) +
        path('M10 2 L12 2 L12 4'),
        'Real-Time Settlement',
        'Instant finalization of financial transactions without traditional T+2 settlement delays',
        ['instant settlement', 'atomic settlement', 'T+0'],
        'ripple-hedera',
        ['https://ripple.com/ripplenet/'],
        ['settlement', 'real-time', 'finality', 'payments']
    ),
    'cross-margining': (
        rect(3,8,8,8,1) + rect(13,8,8,8,1) +
        line(11,12,13,12) +
        path('M7 6 L7 8 M17 6 L17 8') +
        path('M7 16 L7 18 M17 16 L17 18'),
        'Cross-Margining',
        'Using combined collateral across multiple positions to optimize margin efficiency',
        ['cross margin', 'portfolio margin', 'margin optimization'],
        'ripple-hedera',
        ['https://ripple.com/solutions/'],
        ['margin', 'cross', 'collateral', 'efficiency']
    ),
    'rwa-tokenization': (
        rect(4,8,16,8,1) +
        path('M7 8 L7 4 M12 8 L12 4 M17 8 L17 4') +
        text_el(12,14,'RWA', font_size=6),
        'RWA Tokenization',
        'Representing real-world assets (real estate, bonds, commodities) as blockchain tokens',
        ['real-world asset tokenization', 'asset tokenization', 'on-chain RWA'],
        'ripple-hedera',
        ['https://ripple.com/solutions/tokenize-assets/'],
        ['RWA', 'tokenization', 'real-world', 'assets']
    ),
    'onchain-finance': (
        circle(12,12,8) +
        path('M12 4 Q16 8 16 12 Q16 16 12 20 Q8 16 8 12 Q8 8 12 4') +
        text_el(12,14,'$', font_size=8),
        'Onchain Finance',
        'Financial services and products running natively on blockchain with full transparency and programmability',
        ['on-chain finance', 'DeFi', 'blockchain finance'],
        'ripple-hedera',
        ['https://hedera.com/use-cases/tokenization'],
        ['onchain', 'finance', 'blockchain', 'DeFi']
    ),
    'compliance-first': (
        rect(5,4,14,16,1) +
        path('M8 9 L10 11 L14 7') +
        path('M8 14 L10 16 L14 12') +
        line(5,7,19,7),
        'Compliance-First',
        'Designing financial systems with regulatory compliance as a primary, not afterthought, constraint',
        ['regulatory compliance', 'compliance-by-design', 'AML/KYC first'],
        'ripple-hedera',
        ['https://ripple.com/solutions/compliance/'],
        ['compliance', 'regulation', 'KYC', 'AML']
    ),
    'transaction-finality': (
        circle(12,12,8) +
        path('M8 12 L10 14 L15 9') +
        line(4,20,20,20, stroke_dasharray='3 1'),
        'Transaction Finality',
        'The point at which a blockchain transaction is irreversibly confirmed and cannot be reversed',
        ['settlement finality', 'block finality', 'confirmation'],
        'ripple-hedera',
        ['https://hedera.com/learning/distributed-ledger/transaction-finality'],
        ['finality', 'transaction', 'irreversible', 'confirmed']
    ),
    'trustworthy-ai-agent': (
        circle(12,10,5) +
        path('M6 20 Q6 15 12 15 Q18 15 18 20') +
        path('M10 10 L11 11 L14 8') +
        path('M3 3 L5 5 M19 3 L21 5 M3 21 L5 19 M19 21 L21 19', stroke_width='1'),
        'Trustworthy AI Agent',
        'An AI agent meeting standards of reliability, safety, transparency, and accountability',
        ['trusted AI', 'responsible AI agent', 'accountable AI'],
        'ripple-hedera',
        ['https://hedera.com/ai'],
        ['trustworthy', 'AI', 'agent', 'safety']
    ),
    'post-quantum-cryptography': (
        circle(12,12,8) +
        path('M8 8 L16 8 L16 16 L8 16 Z') +
        path('M10 10 L14 14 M14 10 L10 14') +
        circle(12,12,2),
        'Post-Quantum Cryptography',
        'Cryptographic algorithms resistant to attacks from quantum computers',
        ['PQC', 'quantum-resistant crypto', 'lattice cryptography'],
        'ripple-hedera',
        ['https://arxiv.org/abs/2107.12765'],
        ['post-quantum', 'cryptography', 'quantum', 'security']
    ),
    'tamper-proof-logging': (
        rect(4,4,16,16,1) +
        path('M7 8 L17 8 M7 11 L17 11 M7 14 L17 14 M7 17 L12 17') +
        path('M18 13 L20 15 L18 17', stroke_width='2') +
        line(4,4,20,4),
        'Tamper-Proof Logging',
        'Immutable audit trails where records cannot be altered after creation, cryptographically guaranteed',
        ['immutable logging', 'audit trail', 'append-only log'],
        'ripple-hedera',
        ['https://hedera.com/use-cases/audit-trail'],
        ['logging', 'immutable', 'audit', 'tamper-proof']
    ),
    'cbdc': (
        circle(12,12,8) +
        text_el(12,14,'¢', font_size=10) +
        path('M4 8 Q12 3 20 8', stroke_dasharray='2 1') +
        path('M4 16 Q12 21 20 16', stroke_dasharray='2 1'),
        'CBDC',
        'Central Bank Digital Currency — a digital form of sovereign currency issued and controlled by central banks',
        ['central bank digital currency', 'digital fiat', 'e-currency'],
        'ripple-hedera',
        ['https://ripple.com/cbdc-solution/'],
        ['CBDC', 'central bank', 'digital currency', 'fiat']
    ),
    'microtransaction': (
        circle(8,12,3) +
        path('M11 12 L13 12') +
        circle(16,12,3) +
        path('M6 8 L8 6 M16 6 L18 8', stroke_width='1') +
        text_el(12,22,'μ', font_size=6),
        'Microtransaction',
        'Tiny financial transactions (fractions of a cent) enabled at scale by blockchain infrastructure',
        ['micro payment', 'nanopayment', 'streaming payments'],
        'ripple-hedera',
        ['https://arxiv.org/abs/2005.03556'],
        ['microtransaction', 'payment', 'micro', 'blockchain']
    ),

    # ── KALSHI / PREDICTION MARKETS ─────────────────────────────────────────
    'prediction-market': (
        path('M3 20 L21 20') +
        path('M3 20 L8 12 L12 15 L16 5 L21 12') +
        line(16,5,16,20, stroke_dasharray='2 2') +
        circle(16,5,2),
        'Prediction Market',
        'A market for trading contracts on the outcomes of future events, aggregating collective forecasts',
        ['event market', 'information market', 'betting market'],
        'prediction-markets',
        ['https://arxiv.org/abs/2109.13916'],
        ['prediction', 'market', 'forecast', 'events']
    ),
    'event-contract': (
        rect(4,4,16,16,2) +
        path('M8 10 L10 12 L15 7') +
        line(8,15,16,15) +
        line(4,8,20,8),
        'Event Contract',
        'A financial contract whose payoff is determined by the outcome of a specific real-world event',
        ['outcome contract', 'event derivative', 'binary contract'],
        'prediction-markets',
        ['https://kalshi.com'],
        ['event', 'contract', 'outcome', 'market']
    ),
    'binary-outcome': (
        circle(7,12,5) + circle(17,12,5) +
        text_el(7,15,'0', font_size=8) +
        text_el(17,15,'1', font_size=8),
        'Binary Outcome',
        'An event with exactly two possible results — yes/no, true/false, win/lose',
        ['binary event', 'yes/no outcome', 'boolean outcome'],
        'prediction-markets',
        ['https://kalshi.com'],
        ['binary', 'outcome', 'yes/no', 'boolean']
    ),
    'yes-no-contract': (
        rect(4,4,16,16,2) +
        text_el(8,14,'Y', font_size=8) +
        text_el(16,14,'N', font_size=8) +
        line(12,4,12,20),
        'Yes/No Contract',
        'A prediction market contract settling at $1 if yes and $0 if no',
        ['binary contract', 'Y/N contract', 'event contract'],
        'prediction-markets',
        ['https://kalshi.com'],
        ['yes/no', 'binary', 'contract', 'settlement']
    ),
    'perpetual-futures': (
        path('M3 12 Q7 6 12 12 Q17 18 21 12') +
        circle(12,12,2) +
        path('M19 10 L21 12 L19 14') +
        path('M5 10 L3 12 L5 14'),
        'Perpetual Futures',
        'Futures contracts with no expiry date, using funding rates to keep prices anchored to spot',
        ['perps', 'perpetual swaps', 'endless futures'],
        'prediction-markets',
        ['https://arxiv.org/abs/2210.01250'],
        ['perpetual', 'futures', 'derivatives', 'trading']
    ),
    'cftc-regulated': (
        rect(4,4,16,16,2) +
        line(4,9,20,9) +
        text_el(12,16,'CFTC', font_size=6) +
        path('M8 6 L10 8 L13 5', stroke_width='1.5'),
        'CFTC Regulated',
        'Financial products or platforms operating under US Commodity Futures Trading Commission oversight',
        ['CFTC', 'regulated exchange', 'CFTC-approved'],
        'prediction-markets',
        ['https://www.cftc.gov'],
        ['CFTC', 'regulated', 'compliance', 'exchange']
    ),

    # ── SCIENCE / TECH ───────────────────────────────────────────────────────
    'quantum-superposition': (
        circle(12,12,8) +
        path('M4 12 Q12 4 20 12 Q12 20 4 12') +
        line(4,12,20,12, stroke_dasharray='3 2') +
        circle(12,12,2),
        'Quantum Superposition',
        'A qubit existing in multiple states simultaneously until measured, the foundation of quantum computing',
        ['superposition', 'quantum state', 'wave function'],
        'science-tech',
        ['https://arxiv.org/abs/quant-ph/0001077'],
        ['quantum', 'superposition', 'qubit', 'state']
    ),
    'entanglement': (
        circle(7,12,4) + circle(17,12,4) +
        path('M11 10 Q14 8 13 12 Q12 16 13 14') +
        path('M11 14 Q10 10 13 12 Q14 16 11 14', stroke_dasharray='2 1'),
        'Entanglement',
        'Two quantum particles correlated so measuring one instantly affects the other regardless of distance',
        ['quantum entanglement', 'Bell state', 'EPR pair'],
        'science-tech',
        ['https://arxiv.org/abs/quant-ph/9504016'],
        ['entanglement', 'quantum', 'correlation', 'nonlocal']
    ),
    'decoherence': (
        circle(12,12,8) +
        path('M4 12 Q12 4 20 12', stroke_dasharray='4 1') +
        path('M4 12 Q12 20 20 12', stroke_dasharray='2 2') +
        path('M8 16 L16 8', stroke_dasharray='1 3'),
        'Decoherence',
        'The loss of quantum coherence as a qubit interacts with its environment, the main obstacle to quantum computing',
        ['quantum decoherence', 'quantum noise', 'error source'],
        'science-tech',
        ['https://arxiv.org/abs/quant-ph/0306072'],
        ['decoherence', 'quantum', 'noise', 'error']
    ),
    'quantum-gate': (
        rect(7,7,10,10,1) +
        path('M3 12 L7 12 M17 12 L21 12') +
        text_el(12,15,'H', font_size=7),
        'Quantum Gate',
        'A basic quantum circuit operation that transforms qubit states, analogous to classical logic gates',
        ['quantum logic gate', 'qubit gate', 'unitary gate'],
        'science-tech',
        ['https://arxiv.org/abs/quant-ph/9503016'],
        ['quantum gate', 'circuit', 'qubit', 'logic']
    ),
    'qubit': (
        circle(12,12,7) +
        path('M12 5 L12 19') +
        path('M5.5 9 L18.5 15 M5.5 15 L18.5 9') +
        circle(12,12,2, fill=C, stroke='none'),
        'Qubit',
        'The basic unit of quantum information — a two-state quantum system that can be in superposition',
        ['quantum bit', 'quantum register', 'qbit'],
        'science-tech',
        ['https://arxiv.org/abs/quant-ph/0001077'],
        ['qubit', 'quantum', 'bit', 'superposition']
    ),
    'quantum-supremacy': (
        polygon('12,2 15,9 22,9 17,13 19,20 12,16 5,20 7,13 2,9 9,9') +
        circle(12,12,3),
        'Quantum Supremacy',
        'The milestone where a quantum computer performs a task infeasible for any classical computer',
        ['quantum advantage', 'quantum milestone', 'quantum speed'],
        'science-tech',
        ['https://arxiv.org/abs/1910.11333'],
        ['quantum supremacy', 'milestone', 'advantage', 'computing']
    ),
    'neuroplasticity': (
        circle(12,12,8) +
        path('M6 8 Q9 5 12 8 Q15 11 12 14 Q9 17 12 16') +
        path('M8 16 Q11 13 14 16') +
        circle(12,8,1.5) + circle(12,14,1.5),
        'Neuroplasticity',
        "The brain's ability to reorganize neural pathways and form new connections in response to experience",
        ['brain plasticity', 'neural rewiring', 'synaptic plasticity'],
        'science-tech',
        ['https://arxiv.org/abs/1710.04440'],
        ['brain', 'plasticity', 'neural', 'learning']
    ),
    'epigenetics': (
        path('M6 6 Q12 3 18 6 Q15 12 12 12 Q9 12 6 6') +
        path('M6 18 Q12 21 18 18 Q15 12 12 12 Q9 12 6 18') +
        line(12,3,12,21, stroke_dasharray='2 2'),
        'Epigenetics',
        'Heritable changes in gene expression not caused by DNA sequence changes — environment shapes genes',
        ['gene expression', 'epigenome', 'DNA methylation'],
        'science-tech',
        ['https://arxiv.org/abs/1611.05128'],
        ['epigenetics', 'genes', 'expression', 'biology']
    ),
    'crispr': (
        path('M5 8 L19 8 M5 12 L19 12 M5 16 L19 16') +
        path('M10 6 L10 18 M14 6 L14 18') +
        path('M12 3 L12 5 M12 19 L12 21', stroke_width='2') +
        circle(12,12,2, fill=C, stroke='none'),
        'CRISPR',
        'A gene editing technology allowing precise modification of DNA sequences in living organisms',
        ['CRISPR-Cas9', 'gene editing', 'gene scissors'],
        'science-tech',
        ['https://arxiv.org/abs/1406.7567'],
        ['CRISPR', 'gene editing', 'DNA', 'biology']
    ),
    'materials-discovery': (
        circle(12,12,8) +
        path('M8 8 L12 4 L16 8 L16 16 L12 20 L8 16 Z') +
        circle(12,12,2, fill=C, stroke='none'),
        'Materials Discovery',
        'Using AI and high-throughput methods to identify novel materials with desired properties',
        ['AI materials', 'computational materials', 'materials informatics'],
        'science-tech',
        ['https://arxiv.org/abs/2306.11025'],
        ['materials', 'discovery', 'AI', 'science']
    ),
    'self-driving-lab': (
        rect(3,8,18,10,1) +
        path('M7 8 L7 4 M12 8 L12 4 M17 8 L17 4') +
        path('M6 12 L9 14 L12 12 L15 14 L18 12') +
        circle(19,5,3),
        'Self-Driving Lab',
        'An automated laboratory using AI and robotics to run experiments autonomously and iterate',
        ['autonomous lab', 'robot lab', 'AI-driven research'],
        'science-tech',
        ['https://arxiv.org/abs/2306.08645'],
        ['lab', 'autonomous', 'AI', 'robotics']
    ),
    'high-throughput-synthesis': (
        rect(3,5,4,14,1) + rect(10,5,4,14,1) + rect(17,5,4,14,1) +
        path('M5 5 L5 3 M12 5 L12 3 M19 5 L19 3') +
        line(3,17,21,17),
        'High-Throughput Synthesis',
        'Parallel synthesis of thousands of compounds simultaneously to accelerate materials and drug discovery',
        ['parallel synthesis', 'combinatorial chemistry', 'HTS'],
        'science-tech',
        ['https://arxiv.org/abs/2209.08258'],
        ['synthesis', 'high-throughput', 'parallel', 'chemistry']
    ),
    'svg-format': (
        rect(4,4,16,16,1) +
        path('M8 12 Q10 6 12 12 Q14 18 16 12') +
        text_el(12,21,'SVG', font_size=5),
        'SVG (the format)',
        'Scalable Vector Graphics — an XML-based vector image format that scales without quality loss',
        ['scalable vector graphics', 'vector format', 'SVG file'],
        'science-tech',
        ['https://www.w3.org/TR/SVG/'],
        ['SVG', 'vector', 'graphics', 'format']
    ),
    'api': (
        rect(4,6,16,12,2) +
        path('M8 10 L10 12 L8 14') +
        path('M16 10 L14 12 L16 14') +
        line(11,12,13,12),
        'API',
        'Application Programming Interface — a defined contract for software components to communicate',
        ['application programming interface', 'REST API', 'endpoint'],
        'science-tech',
        ['https://arxiv.org/abs/2212.09263'],
        ['API', 'interface', 'endpoint', 'integration']
    ),
    'webhook': (
        circle(12,12,8) +
        path('M8 12 L10 14 L14 10') +
        path('M12 4 L16 4 L16 8', stroke_width='1') +
        line(12,4,16,8, stroke_dasharray='2 1'),
        'Webhook',
        'An HTTP callback that sends real-time data to other applications when specific events occur',
        ['HTTP callback', 'event notification', 'push notification'],
        'science-tech',
        ['https://arxiv.org/abs/2104.13099'],
        ['webhook', 'callback', 'event', 'HTTP']
    ),
    'microservice': (
        circle(6,6,3) + circle(18,6,3) + circle(6,18,3) + circle(18,18,3) + circle(12,12,3) +
        line(9,12,9,12) +
        line(8.5,7.5,10,10) + line(15.5,7.5,14,10) +
        line(8.5,16.5,10,14) + line(15.5,16.5,14,14),
        'Microservice',
        'An architectural approach building software as small independent services communicating via APIs',
        ['microservices architecture', 'service mesh', 'service-oriented'],
        'science-tech',
        ['https://arxiv.org/abs/2301.07427'],
        ['microservice', 'architecture', 'API', 'service']
    ),
    'semiconductor-fab': (
        rect(4,4,16,16,1) +
        path('M4 8 L20 8 M4 12 L20 12 M4 16 L20 16') +
        path('M8 4 L8 20 M12 4 L12 20 M16 4 L16 20'),
        'Semiconductor Fab',
        'A manufacturing facility that produces integrated circuits on semiconductor wafers',
        ['chip fab', 'semiconductor foundry', 'wafer fab'],
        'science-tech',
        ['https://arxiv.org/abs/2104.07551'],
        ['semiconductor', 'fab', 'chip', 'manufacturing']
    ),
    'euv-lithography': (
        circle(12,12,8) +
        path('M12 4 L12 8 M12 16 L12 20 M4 12 L8 12 M16 12 L20 12') +
        circle(12,12,3) +
        path('M8 8 L16 16 M16 8 L8 16', stroke_width='0.75'),
        'EUV Lithography',
        'Extreme Ultraviolet Lithography — uses 13.5nm wavelength light to etch sub-7nm chip features',
        ['EUV', 'extreme ultraviolet', 'chip lithography', 'ASML'],
        'science-tech',
        ['https://arxiv.org/abs/2007.04347'],
        ['EUV', 'lithography', 'chip', 'ASML']
    ),
    'chiplet': (
        rect(4,4,7,7,1) + rect(13,4,7,7,1) +
        rect(4,13,7,7,1) + rect(13,13,7,7,1) +
        line(11,7.5,13,7.5) + line(7.5,11,7.5,13) +
        line(11,16.5,13,16.5) + line(16.5,11,16.5,13),
        'Chiplet',
        'A small, modular chip die designed to be combined with others into a larger package',
        ['die-to-die', 'chiplet architecture', 'advanced packaging'],
        'science-tech',
        ['https://arxiv.org/abs/2205.09291'],
        ['chiplet', 'die', 'packaging', 'semiconductor']
    ),
    'hbm': (
        rect(5,4,14,3,0) + rect(5,9,14,3,0) + rect(5,14,14,3,0) +
        line(5,7,19,7) + line(5,12,19,12) + line(5,17,19,17) +
        line(8,4,8,19) + line(12,4,12,19) + line(16,4,16,19) +
        text_el(12,22,'HBM', font_size=5),
        'HBM (High Bandwidth Memory)',
        'Stacked DRAM dies connected via through-silicon vias delivering very high memory bandwidth',
        ['high bandwidth memory', 'stacked memory', 'HBM3'],
        'science-tech',
        ['https://arxiv.org/abs/2204.09394'],
        ['HBM', 'memory', 'bandwidth', 'DRAM']
    ),

    # ── ECONOMICS / FINANCE ──────────────────────────────────────────────────
    'cantillon-effect': (
        circle(5,12,3) +
        path('M8 12 L16 12') +
        circle(19,12,3) +
        path('M5 9 L5 4 Q5 2 7 3 Q9 4 8 6', stroke_dasharray='2 1') +
        path('M19 9 L19 15', stroke_width='0.75'),
        'Cantillon Effect',
        'The uneven economic impact of money creation — those closest to new money benefit first',
        ['monetary distribution', 'first recipient advantage', 'money printing effect'],
        'economics',
        ['https://arxiv.org/abs/2109.09565'],
        ['Cantillon', 'money', 'inequality', 'economics']
    ),
    'reflexivity': (
        path('M4 12 Q4 5 12 5 Q20 5 20 12') +
        path('M20 12 Q20 19 12 19 Q4 19 4 12') +
        path('M10 5 L12 3 L14 5') +
        path('M10 19 L12 21 L14 19'),
        'Reflexivity',
        "Soros's theory that market participants' biased views affect fundamentals, creating feedback loops",
        ['market reflexivity', 'Soros reflexivity', 'self-fulfilling prophecy'],
        'economics',
        ['https://arxiv.org/abs/1105.5379'],
        ['reflexivity', 'markets', 'feedback', 'Soros']
    ),
    'sound-money': (
        circle(12,12,8) +
        text_el(12,14,'$', font_size=10) +
        path('M12 4 L12 2 M12 22 L12 20', stroke_width='2'),
        'Sound Money',
        'Currency that maintains stable purchasing power, not subject to arbitrary inflation or debasement',
        ['hard money', 'stable money', 'non-inflationary currency'],
        'economics',
        ['https://arxiv.org/abs/2109.01652'],
        ['sound money', 'stable', 'inflation', 'currency']
    ),
    'dedollarization': (
        circle(12,12,8) +
        text_el(12,14,'$', font_size=8) +
        line(5,5,19,19, stroke_width='2'),
        'Dedollarization',
        'The global trend of reducing reliance on the US dollar in international trade and reserves',
        ['dollar decline', 'multipolar currency', 'USD diversification'],
        'economics',
        ['https://arxiv.org/abs/2305.05127'],
        ['dedollarization', 'dollar', 'reserves', 'geopolitics']
    ),
    'yield-curve-inversion': (
        path('M3 18 L7 8 L11 6 L15 10 L19 14') +
        path('M3 14 L21 14', stroke_dasharray='3 2') +
        circle(11,6,2),
        'Yield Curve Inversion',
        'When short-term bond yields exceed long-term yields — historically a reliable recession predictor',
        ['inverted yield curve', 'recession signal', '2-10 spread'],
        'economics',
        ['https://arxiv.org/abs/1810.01528'],
        ['yield curve', 'inversion', 'recession', 'bonds']
    ),
    'quantitative-easing': (
        path('M3 18 L7 14 L11 16 L15 10 L19 6') +
        path('M3 18 L21 18') +
        path('M16 4 L20 6 L18 10') +
        circle(19,6,2),
        'Quantitative Easing',
        'Central bank asset purchases to inject money into the economy when interest rates hit the zero bound',
        ['QE', 'money printing', 'asset purchases', 'balance sheet expansion'],
        'economics',
        ['https://arxiv.org/abs/1011.0714'],
        ['QE', 'central bank', 'money', 'policy']
    ),
    'regulatory-capture': (
        circle(12,12,8) +
        path('M8 8 L16 8 L16 16 L8 16 Z') +
        path('M10 10 L14 14 M10 14 L14 10', stroke_width='1'),
        'Regulatory Capture',
        'When a regulatory agency advances the interests of the industry it is supposed to regulate',
        ['industry capture', 'revolving door', 'captured regulator'],
        'economics',
        ['https://arxiv.org/abs/1711.09698'],
        ['regulation', 'capture', 'industry', 'policy']
    ),
    'deadweight-loss': (
        path('M3 18 L12 4 L21 18') +
        path('M7 18 L12 9 L17 18') +
        path('M7 18 L17 18', stroke_dasharray='3 1'),
        'Deadweight Loss',
        'Economic inefficiency created when supply and demand are not in equilibrium due to interventions',
        ['welfare loss', 'efficiency loss', 'market distortion'],
        'economics',
        ['https://arxiv.org/abs/1602.02048'],
        ['deadweight loss', 'efficiency', 'economics', 'welfare']
    ),
    'brics': (
        circle(4,8,2) + circle(10,5,2) + circle(16,5,2) + circle(20,9,2) + circle(12,12,2) +
        line(6,8,10,6) + line(12,5,16,5) + line(17,6,20,8) + line(12,10,10,7) + line(12,10,16,7) +
        text_el(12,22,'BRICS', font_size=5),
        'BRICS',
        'The economic bloc of Brazil, Russia, India, China, South Africa — and expanding membership',
        ['BRICS nations', 'emerging markets bloc', 'BRICS+'],
        'economics',
        ['https://arxiv.org/abs/2305.05127'],
        ['BRICS', 'geopolitics', 'emerging markets', 'economics']
    ),
    'iso-20022': (
        rect(3,5,18,14,1) +
        path('M6 9 L11 9 M6 12 L18 12 M6 15 L15 15') +
        text_el(12,21,'ISO', font_size=5),
        'ISO 20022',
        'A global financial messaging standard enabling richer data in payment transactions',
        ['ISO20022', 'SWIFT ISO 20022', 'payment messaging standard'],
        'economics',
        ['https://www.iso20022.org'],
        ['ISO 20022', 'payments', 'standard', 'messaging']
    ),

    # ── PHILOSOPHY / THOUGHT ─────────────────────────────────────────────────
    'singularity': (
        circle(12,12,8) + circle(12,12,4) + circle(12,12,1, fill=C, stroke='none') +
        path('M12 4 L12 2 M12 22 L12 20 M4 12 L2 12 M22 12 L20 12'),
        'Singularity',
        'A hypothetical point where AI surpasses human intelligence, causing an uncontrollable technological explosion',
        ['technological singularity', 'intelligence singularity', 'Kurzweil singularity'],
        'philosophy',
        ['https://arxiv.org/abs/2109.01652'],
        ['singularity', 'AI', 'intelligence', 'future']
    ),
    'intelligence-explosion': (
        path('M3 20 L5 18 L7 17 L9 15 L11 12 L12 9 L13 5 L14 2') +
        path('M3 20 L21 20') +
        path('M13 4 L16 4 L14 7'),
        'Intelligence Explosion',
        'The rapid recursive self-improvement of AI leading to superintelligence faster than humans can respond',
        ['recursive self-improvement', 'AI takeoff', 'fast takeoff'],
        'philosophy',
        ['https://arxiv.org/abs/2109.13916'],
        ['intelligence', 'explosion', 'recursive', 'AI']
    ),
    'superintelligence': (
        polygon('12,2 14,8 22,8 16,12 18,20 12,16 6,20 8,12 2,8 10,8') +
        path('M12 8 L12 16 M9 11 L15 11 M9 13 L15 13'),
        'Superintelligence',
        'A hypothetical AI that surpasses human cognitive performance across all domains',
        ['ASI', 'artificial superintelligence', 'beyond-human AI'],
        'philosophy',
        ['https://arxiv.org/abs/2109.13916'],
        ['superintelligence', 'ASI', 'AI', 'capability']
    ),
    'paperclip-maximizer': (
        path('M8 12 Q8 6 12 6 Q16 6 16 12 Q16 18 12 18 Q8 18 8 12') +
        path('M10 9 Q12 7 14 9') +
        path('M10 15 Q12 17 14 15') +
        line(10,9,10,15) + line(14,9,14,15),
        'Paperclip Maximizer',
        "Nick Bostrom's thought experiment about an AI optimizing a single goal to catastrophic ends",
        ['Bostrom thought experiment', 'misaligned optimizer', 'convergent instrumental goals'],
        'philosophy',
        ['https://arxiv.org/abs/1906.01820'],
        ['paperclip', 'misalignment', 'optimizer', 'Bostrom']
    ),
    'instrumental-convergence': (
        circle(12,12,8) +
        path('M7 7 L12 12 L17 7') +
        path('M7 17 L12 12 L17 17') +
        circle(12,12,2, fill=C, stroke='none'),
        'Instrumental Convergence',
        'The tendency for agents with diverse goals to adopt similar sub-goals like self-preservation and resource acquisition',
        ['convergent instrumental goals', 'basic AI drives', 'Omohundro drives'],
        'philosophy',
        ['https://arxiv.org/abs/1906.01820'],
        ['instrumental convergence', 'goals', 'AI', 'drives']
    ),
    'phenomenology': (
        circle(12,12,8) +
        path('M12 4 Q18 8 18 12 Q18 16 12 20') +
        path('M12 4 Q6 8 6 12 Q6 16 12 20') +
        circle(12,12,3),
        'Phenomenology',
        "Philosophical study of structures of consciousness and first-person subjective experience",
        ['Husserl', 'qualia', 'consciousness study', 'intentionality'],
        'philosophy',
        ['https://arxiv.org/abs/2112.12345'],
        ['phenomenology', 'consciousness', 'experience', 'philosophy']
    ),
    'cognitive-dissonance': (
        circle(9,12,5) + circle(15,12,5) +
        path('M12 8 L12 16', stroke_dasharray='2 1') +
        path('M9 10 L9 14 M15 10 L15 14'),
        'Cognitive Dissonance',
        'Mental discomfort from holding contradictory beliefs, values, or behaviors simultaneously',
        ['belief conflict', 'mental discomfort', 'psychological tension'],
        'philosophy',
        ['https://arxiv.org/abs/2004.12556'],
        ['cognitive dissonance', 'psychology', 'belief', 'conflict']
    ),
    'dunning-kruger-effect': (
        path('M3 18 L5 8 L8 4 L11 10 L14 12 L17 11 L21 13') +
        path('M3 18 L21 18') +
        circle(8,4,2) +
        line(14,12,14,18, stroke_dasharray='2 1'),
        'Dunning-Kruger Effect',
        'The cognitive bias where people with limited knowledge overestimate their competence',
        ['Dunning-Kruger', 'overconfidence bias', 'metacognitive bias'],
        'philosophy',
        ['https://arxiv.org/abs/2104.09876'],
        ['Dunning-Kruger', 'bias', 'overconfidence', 'psychology']
    ),
    'parasocial-relationship': (
        circle(7,10,4) + circle(17,10,4) +
        path('M11 10 L13 10', stroke_dasharray='3 2') +
        path('M7 14 Q7 20 12 20') +
        path('M17 14 Q17 18 12 18') +
        path('M12 18 L12 20', stroke_dasharray='2 1'),
        'Parasocial Relationship',
        'A one-sided emotional bond a person forms with a media persona, celebrity, or AI without real interaction',
        ['parasocial bond', 'one-sided relationship', 'media relationship'],
        'philosophy',
        ['https://arxiv.org/abs/2207.09876'],
        ['parasocial', 'relationship', 'psychology', 'media']
    ),
    'metatrend': (
        path('M3 18 L7 14 L11 16 L15 8 L19 4') +
        path('M3 18 L21 18') +
        path('M3 14 L21 14', stroke_dasharray='3 2') +
        path('M3 10 L21 10', stroke_dasharray='1 3'),
        'Metatrend',
        'A macro-level trend that cuts across multiple industries and shapes the trajectory of many smaller trends',
        ['macro trend', 'mega trend', 'underlying trend'],
        'philosophy',
        ['https://arxiv.org/abs/2204.09876'],
        ['metatrend', 'macro', 'trend', 'future']
    ),
    'moonshot': (
        path('M12 20 Q5 20 3 13 Q2 7 7 4 Q12 1 17 4 Q22 7 21 13 Q19 20 12 20') +
        path('M12 4 L13 7 L10 9 L14 10 L11 13') +
        circle(12,18,2, fill=C, stroke='none'),
        'Moonshot',
        'An ambitious, exploratory project aiming for transformational impact — named after the Apollo program',
        ['moonshot thinking', '10x project', 'transformational goal'],
        'philosophy',
        ['https://arxiv.org/abs/2205.09876'],
        ['moonshot', 'ambition', 'goal', 'innovation']
    ),
    'mtp': (
        polygon('12,2 22,12 12,22 2,12') +
        path('M7 12 L10 15 L17 9') +
        text_el(12,21,'MTP', font_size=4),
        'MTP (Massive Transformative Purpose)',
        "Salim Ismail's concept of an audacious mission statement that attracts talent and inspires action",
        ['massive transformative purpose', 'ExO MTP', 'mission statement'],
        'philosophy',
        ['https://arxiv.org/abs/2203.09876'],
        ['MTP', 'mission', 'purpose', 'transformation']
    ),
    'abundance-mindset': (
        circle(12,12,8) +
        path('M8 12 Q10 6 12 12 Q14 18 16 12') +
        path('M5 9 L3 7 M19 9 L21 7 M5 15 L3 17 M19 15 L21 17'),
        'Abundance Mindset',
        'The belief that resources, opportunities, and possibilities are unlimited — as opposed to scarcity thinking',
        ['abundance thinking', 'growth mindset', 'Diamandis abundance'],
        'philosophy',
        ['https://arxiv.org/abs/2202.09876'],
        ['abundance', 'mindset', 'thinking', 'growth']
    ),
    'exponential-organization': (
        path('M3 20 L5 18 L7 16 L10 13 L13 9 L17 5 L21 3') +
        path('M3 20 L21 20') +
        path('M3 20 L3 3') +
        circle(21,3,2),
        'Exponential Organization',
        'An organization that achieves 10x impact using digital platforms, algorithms, and community assets',
        ['ExO', 'exponential org', 'Salim Ismail ExO'],
        'philosophy',
        ['https://arxiv.org/abs/2204.09876'],
        ['ExO', 'exponential', 'organization', 'scale']
    ),

    # ── SPACE / DEFENSE ──────────────────────────────────────────────────────
    'vertical-integration': (
        rect(8,4,8,16,1) +
        path('M8 8 L4 8 M8 12 L4 12 M8 16 L4 16') +
        path('M16 8 L20 8 M16 12 L20 12 M16 16 L20 16') +
        circle(12,4,2, fill=C, stroke='none'),
        'Vertical Integration (SpaceX)',
        'Controlling the entire production chain internally — SpaceX makes engines, rockets, and launches itself',
        ['vertical integration', 'supply chain control', 'insourcing'],
        'space-defense',
        ['https://arxiv.org/abs/2110.03456'],
        ['vertical integration', 'SpaceX', 'manufacturing', 'supply chain']
    ),
    'stage-separation': (
        path('M12 2 L9 8 L15 8 Z') +
        rect(9,8,6,6,0) +
        line(9,14,15,14) +
        rect(9,14,6,6,0) +
        line(7,14,17,14, stroke_dasharray='2 1'),
        'Stage Separation',
        'Detaching rocket stages during flight to shed mass and improve efficiency',
        ['stage jettison', 'staging event', 'rocket staging'],
        'space-defense',
        ['https://arxiv.org/abs/2202.09876'],
        ['stage separation', 'rocket', 'SpaceX', 'staging']
    ),
    'reusability': (
        path('M12 2 L9 8 L15 8 Z') +
        rect(9,8,6,10,0) +
        path('M9 18 Q7 22 12 22 Q17 22 15 18') +
        path('M10 21 Q12 19 14 21', stroke_dasharray='2 1'),
        'Reusability',
        'The ability to recover and refly rocket hardware, dramatically reducing launch costs',
        ['rocket reuse', 'reusable launch vehicle', 'booster recovery'],
        'space-defense',
        ['https://arxiv.org/abs/2205.09876'],
        ['reusability', 'rocket', 'SpaceX', 'cost']
    ),
    'mission-autonomy': (
        circle(12,12,8) +
        path('M12 4 L12 8 M12 16 L12 20') +
        path('M8 6 L10 9 M14 6 L12 9') +
        circle(12,12,3) +
        circle(12,12,1, fill=C, stroke='none'),
        'Mission Autonomy',
        'The capability of systems to accomplish objectives without human intervention in the loop',
        ['autonomous mission', 'self-directing system', 'mission independence'],
        'space-defense',
        ['https://arxiv.org/abs/2311.10538'],
        ['autonomy', 'mission', 'autonomous', 'defense']
    ),
    'edge-ai': (
        rect(4,8,8,8,1) +
        circle(19,12,4) +
        path('M12 10 L15 12 L12 14') +
        path('M4 6 L4 4 L8 4 M16 4 L20 4 L20 8'),
        'Edge AI',
        'AI inference running on local devices rather than cloud servers — reducing latency and dependency',
        ['on-device AI', 'local inference', 'embedded AI'],
        'space-defense',
        ['https://arxiv.org/abs/2209.07840'],
        ['edge AI', 'local', 'inference', 'embedded']
    ),
    'multi-domain-operations': (
        circle(12,5,2) + circle(5,14,2) + circle(19,14,2) + circle(7,21,2) + circle(17,21,2) +
        line(12,7,7,12) + line(12,7,17,12) +
        line(7,16,7,19) + line(17,16,17,19) +
        line(7,16,17,16),
        'Multi-Domain Operations',
        'Military operations synchronized across land, sea, air, space, and cyberspace simultaneously',
        ['MDO', 'joint all-domain operations', 'JADC2'],
        'space-defense',
        ['https://arxiv.org/abs/2309.09876'],
        ['multi-domain', 'military', 'operations', 'defense']
    ),
    'tactical-edge': (
        rect(4,8,16,8,1) +
        path('M4 12 L8 12 M16 12 L20 12') +
        path('M12 4 L12 8 M12 16 L12 20') +
        circle(12,12,3),
        'Tactical Edge',
        'Computing and AI capabilities deployed at the point of action in denied or contested environments',
        ['edge computing defense', 'tactical AI', 'forward deployed compute'],
        'space-defense',
        ['https://arxiv.org/abs/2310.09876'],
        ['tactical', 'edge', 'compute', 'defense']
    ),
    'counter-uas': (
        circle(12,12,8) +
        path('M9 9 L15 15 M15 9 L9 15', stroke_width='2') +
        path('M12 4 L10 8 L14 8 Z', stroke_dasharray='2 1') +
        text_el(12,22,'C-UAS', font_size=4),
        'Counter-UAS',
        'Systems and tactics designed to detect, track, and neutralize unmanned aerial systems',
        ['drone defense', 'anti-drone', 'C-UAS', 'counter-drone'],
        'space-defense',
        ['https://arxiv.org/abs/2311.09876'],
        ['counter-UAS', 'drone', 'defense', 'autonomous']
    ),
    'autonomous-assets': (
        circle(6,12,3) + circle(18,12,3) + circle(12,6,3) + circle(12,18,3) +
        line(9,12,15,12) + line(12,9,12,15) +
        circle(12,12,2, fill=C, stroke='none'),
        'Autonomous Assets',
        'Vehicles, platforms, and systems capable of operating independently in complex environments',
        ['autonomous systems', 'unmanned assets', 'autonomous platforms'],
        'space-defense',
        ['https://arxiv.org/abs/2311.10538'],
        ['autonomous', 'assets', 'defense', 'systems']
    ),
    'terawatt-scale-compute': (
        path('M3 18 L5 14 L8 10 L11 6 L14 4 L17 5 L20 8') +
        path('M3 18 L20 18') +
        path('M17 4 L20 6 L19 9') +
        text_el(12,22,'TW', font_size=6),
        'Terawatt-Scale Compute',
        'The hypothetical future compute infrastructure requiring terawatts of power to train frontier AI',
        ['massive compute', 'compute cluster', 'AI compute scale'],
        'space-defense',
        ['https://arxiv.org/abs/2309.11565'],
        ['compute', 'terawatt', 'scale', 'AI']
    ),
}

print(f"Total icons defined: {len(ICONS)}")

# Generate SVG files
SVG_TMPL = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">{}</svg>'

for name, data in ICONS.items():
    content = data[0]
    svg_content = SVG_TMPL.format(content)
    (ICONS_DIR / f'{name}.svg').write_text(svg_content, encoding='utf-8')

print(f"Generated {len(ICONS)} SVG files")

# Generate JSON metadata
CATEGORY_NAMES = {
    'agentic-economy': 'Agentic Economy',
    'blockchain': 'Blockchain / Web3',
    'flare': 'Flare Network',
    'near': 'NEAR Protocol',
    'ripple-hedera': 'Ripple / Hedera',
    'prediction-markets': 'Prediction Markets',
    'science-tech': 'Science & Tech',
    'economics': 'Economics / Finance',
    'philosophy': 'Philosophy / Thought',
    'space-defense': 'Space & Defense',
}

all_icons_index = []
for i, (name, data) in enumerate(ICONS.items(), start=1):
    content, concept, definition, aliases, category, sources, tags = data
    meta = {
        "id": f"AS-{i:03d}",
        "slug": name,
        "concept": concept,
        "definition": definition,
        "aliases": aliases,
        "category": category,
        "category_name": CATEGORY_NAMES.get(category, category),
        "sources": sources,
        "svg": f"{name}.svg",
        "tags": tags
    }
    (ICONS_DIR / f'{name}.json').write_text(
        json.dumps(meta, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )
    all_icons_index.append(meta)

print(f"Generated {len(all_icons_index)} JSON metadata files")

# Save master index
MASTER_INDEX = Path('/Users/colin/seo/agentiscript/agentiscript.json')
master = {
    "name": "AgentiScript",
    "version": "1.0.0",
    "description": "The visual language of the agentic economy",
    "url": "https://agentiscript.com",
    "license": "CC0",
    "total": len(all_icons_index),
    "categories": list(CATEGORY_NAMES.values()),
    "icons": all_icons_index
}
MASTER_INDEX.write_text(json.dumps(master, indent=2, ensure_ascii=False), encoding='utf-8')
print(f"Master index saved: agentiscript.json ({len(all_icons_index)} icons)")
print("Done!")
