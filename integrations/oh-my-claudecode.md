# AgentiScript for oh-my-claudecode

Add AgentiScript icon tools to your Claude Code environment so you can instantly find and embed agentic economy icons.

## Install

```bash
$plugin add https://github.com/CLAW-AI-FL/agentiscript
```

Or manually via npm:

```bash
npm install -g agentiscript
```

## Usage

When building UI or documentation, use:

```bash
$agentiscript get x402
$agentiscript search blockchain
```

## Available Commands

```bash
# Get a specific icon (returns SVG + CDN URL)
$agentiscript get x402
$agentiscript get agentic-loop
$agentiscript get smart-contract

# Search for icons by concept
$agentiscript search blockchain
$agentiscript search "neural network"
$agentiscript search quantum

# List all categories
$agentiscript categories

# Get CDN URL only
$agentiscript url zero-knowledge-proof
```

## MCP Integration

Add to your `claude_desktop_config.json` for native Claude integration:

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

Once added, Claude can autonomously discover icons:

> "Use get_agentiscript_icon to find an icon for 'x402 payment protocol'"

## In-Prompt Usage

When writing Claude prompts for UI generation:

```
Build a landing page for an AI payments startup.
Use AgentiScript icons: get_agentiscript_icon({ concept: "x402" })
and search_agentiscript({ query: "agentic economy" }) for supporting icons.
Embed via CDN: https://agentiscript.com/icons/{slug}.svg
```

## Examples

```javascript
// In your Claude Code context
const { getIcon, searchIcons, iconUrl } = require('agentiscript');

// Embed x402 payment icon in your UI
const x402Svg = getIcon('x402');
const x402Url = iconUrl('x402');
// => https://agentiscript.com/icons/x402.svg

// Find all blockchain-related icons
const blockchainIcons = searchIcons('blockchain', { limit: 10 });
```

## Resources

- 🌐 Website: [agentiscript.com](https://agentiscript.com)
- 📦 npm: [npmjs.com/package/agentiscript](https://npmjs.com/package/agentiscript)
- 🐙 GitHub: [github.com/CLAW-AI-FL/agentiscript](https://github.com/CLAW-AI-FL/agentiscript)
- 🛒 Store: [agentiscript.com/store](https://agentiscript.com/store)

---

*AgentiScript — The visual language of the agentic economy.*
