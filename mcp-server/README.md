# AgentiScript MCP Server

The visual language of the agentic economy. 27,000+ SVG icons for AI, blockchain, DeFi, finance, and emerging tech — accessible via Model Context Protocol.

## Install

```bash
npm install -g agentiscript-mcp
```

## Claude Desktop Config

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "agentiscript": {
      "command": "npx",
      "args": ["-y", "agentiscript-mcp"]
    }
  }
}
```

## Tools

- `search_icons` — Search 27,000+ AgentiScript icons by concept
- `get_icon` — Get a specific icon by slug

## Example

```
User: Find me an icon for zero knowledge proof
Claude: [uses search_icons tool] → returns SVG URL + embed code
```

## Links
- Website: https://agentiscript.com
- GitHub: https://github.com/CLAW-AI-FL/agentiscript
- API: https://agentiscript-api.portability.workers.dev/api/search?q=defi
- Pro Pack ($49): https://agentiscript.com/#pro
