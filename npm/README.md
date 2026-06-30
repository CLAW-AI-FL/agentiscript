# AgentiScript

**The visual language of the agentic economy.**

20,000+ icons for AI, blockchain, quantum computing, DeFi, x402 payments, and every concept the agentic economy speaks but cannot show.

🌐 [agentiscript.com](https://agentiscript.com) · [GitHub](https://github.com/CLAW-AI-FL/agentiscript)

---

## Install

```bash
npm install agentiscript
```

---

## Usage

```javascript
const { getIcon, searchIcons, listIcons, iconUrl } = require('agentiscript');

// Get an icon by slug or name
const svg = getIcon('x402');
console.log(svg); // <svg ...>...</svg>

// Get CDN URL
const url = iconUrl('agentic-loop');
// => https://agentiscript.com/icons/agentic-loop.svg

// Search for icons
const results = searchIcons('blockchain', { limit: 10 });
results.forEach(icon => {
  console.log(icon.slug, icon.name, icon.category);
});

// List all 20,000+ icons
const all = listIcons();
console.log(`${all.length} icons available`);
```

---

## MCP Integration (Claude Code / AI Agents)

AgentiScript ships a full **Model Context Protocol (MCP) server** so AI agents can discover and retrieve icons natively.

### Add to Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "agentiscript": {
      "command": "node",
      "args": ["/path/to/node_modules/agentiscript/mcp-server.js", "--stdio"]
    }
  }
}
```

Or with npx:

```json
{
  "mcpServers": {
    "agentiscript": {
      "command": "npx",
      "args": ["-y", "agentiscript", "--stdio"]
    }
  }
}
```

### MCP Tools Available

| Tool | Description |
|------|-------------|
| `get_agentiscript_icon` | Get SVG + metadata for any concept |
| `search_agentiscript` | Search icons by keyword |
| `list_agentiscript_categories` | Browse all categories |

### Example Agent Usage

Once connected, Claude (or any MCP-compatible agent) can:

```
"Find me an icon for 'smart contract'"
→ search_agentiscript({ query: "smart contract" })

"Get the x402 payment icon"
→ get_agentiscript_icon({ concept: "x402" })

"What icon categories exist?"
→ list_agentiscript_categories()
```

---

## x402 Micropayments

AgentiScript supports **x402 protocol** for AI-native micropayments. Bots can autonomously purchase premium icon licenses:

```javascript
// x402 payment flow (coming soon)
// POST https://agentiscript.com/x402/icon/{slug}
// Headers: X-Payment: <402 token>
// Returns: { licensed_svg, license_key, expires }
```

Premium icons include:
- Full commercial license
- No attribution required
- Vector source files
- Animation variants

Visit [agentiscript.com/store](https://agentiscript.com/store) for pricing.

---

## Icon Categories

AgentiScript covers 20,000+ concepts across:

- **AI & Machine Learning** — neural networks, agents, embeddings, inference
- **Blockchain & Web3** — smart contracts, DeFi, NFTs, DAOs, L2s
- **Quantum Computing** — qubits, entanglement, quantum gates, algorithms
- **Agentic Economy** — x402, MCP, agent loops, tool use, autonomous systems
- **Infrastructure** — cloud, edge computing, APIs, microservices
- **Finance & DeFi** — tokens, vaults, yield, liquidity pools
- **Cryptography** — ZK proofs, signatures, key management
- **And much more...**

---

## API Reference

### `getIcon(name: string): string | null`
Returns the SVG string for an icon by slug or display name. Falls back to CDN-linked placeholder if local file not found.

### `searchIcons(query: string, opts?: { limit?: number }): Icon[]`
Full-text search across slug, name, tags, description, and category. Default limit: 20.

### `listIcons(): Icon[]`
Returns the complete icon manifest (20,000+ entries).

### `iconUrl(name: string): string | null`
Returns the CDN URL: `https://agentiscript.com/icons/{slug}.svg`

### `getIconMeta(name: string): Icon | null`
Returns icon metadata without SVG content.

---

## License

Icons: **CC0 1.0 Universal** (public domain)
Package code: MIT

---

*AgentiScript — Because the agentic economy needs a visual language.*
