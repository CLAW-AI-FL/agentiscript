# AgentiScript Icon Search

Search **30,000+ SVG icons** for the agentic economy — AI, blockchain, DeFi, finance, crypto, XRPL, and more.

## What it does
- Search by concept: `defi`, `xrpl`, `zero-knowledge-proof`, `prompt-engineering`
- Returns SVG URL, Schema.org structured data, category, tags
- x402 micropayment enabled: bots pay 0.001 XRP per icon automatically
- CC0 license — free to use

## Input
```json
{"query": "defi", "limit": 10}
```

## Output
```json
{
  "results": [
    {
      "slug": "defi",
      "concept": "DeFi",
      "category": "blockchain",
      "url": "https://agentiscript.com/icons/defi.svg",
      "schema": {"@type": "DefinedTerm", "name": "DeFi"}
    }
  ]
}
```

## x402 Payment
Bots pay 0.001 XRP per icon via XRPL Payment Channels. No account required.

API: https://agentiscript-api.portability.workers.dev/api/search?q=defi

## Links
- Website: https://agentiscript.com
- GitHub: https://github.com/CLAW-AI-FL/agentiscript
- npm: https://www.npmjs.com/package/agentiscript
