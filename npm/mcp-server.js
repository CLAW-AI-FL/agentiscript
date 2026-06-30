#!/usr/bin/env node
/**
 * AgentiScript MCP Server
 *
 * A Model Context Protocol (MCP) compatible server exposing AgentiScript
 * icon tools so AI agents can discover, search, and retrieve icons for
 * the agentic economy.
 *
 * Usage:
 *   node mcp-server.js
 *
 * MCP config (claude_desktop_config.json):
 *   {
 *     "mcpServers": {
 *       "agentiscript": {
 *         "command": "node",
 *         "args": ["/path/to/mcp-server.js"]
 *       }
 *     }
 *   }
 */

'use strict';

const path = require('path');
const fs = require('fs');
const readline = require('readline');

// Load manifest
const MANIFEST_PATH = path.join(__dirname, 'agentiscript.json');
let icons = [];
try {
  const raw = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
  icons = raw.icons || raw;
} catch (e) {
  process.stderr.write(`[AgentiScript MCP] Warning: could not load manifest: ${e.message}\n`);
}

const CDN_BASE = 'https://agentiscript.com/icons';

// Build search index
const iconMap = {};
for (const icon of icons) {
  // Support both schema formats:
  // v3: { slug, name, tags, category, description }
  // v1/v2: { name (=slug), label, tags, category }
  // v4 (AS-xxx): { id, slug, concept, definition, aliases, category, svg, tags }
  const conceptSlug = icon.concept ? icon.concept.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') : null;
  const slug = icon.slug || conceptSlug || icon.name;
  const displayName = icon.label || icon.concept || icon.name;
  if (slug) iconMap[slug.toLowerCase()] = icon;
  if (displayName && displayName.toLowerCase() !== (slug || '').toLowerCase()) {
    iconMap[displayName.toLowerCase()] = icon;
  }
  // Index aliases (v4)
  if (icon.aliases) {
    for (const alias of icon.aliases) {
      const aKey = alias.toLowerCase().replace(/\s+/g, '-');
      if (!iconMap[aKey]) iconMap[aKey] = icon;
    }
  }
}

// MCP tool definitions
const tools = [
  {
    name: "get_agentiscript_icon",
    description: "Get an AgentiScript SVG icon for any agentic economy concept. Returns SVG code, CDN URL, and metadata. Covers 20,000+ concepts: AI, blockchain, quantum computing, DeFi, x402 payments, and more.",
    inputSchema: {
      type: "object",
      properties: {
        concept: {
          type: "string",
          description: "The concept name or slug (e.g. 'x402', 'agentic-loop', 'smart-contract', 'neural-network')"
        }
      },
      required: ["concept"]
    }
  },
  {
    name: "search_agentiscript",
    description: "Search AgentiScript for icons matching a concept or keyword. Returns up to 20 matching icons with metadata and CDN URLs.",
    inputSchema: {
      type: "object",
      properties: {
        query: {
          type: "string",
          description: "Search term (e.g. 'blockchain', 'agent', 'payment', 'quantum')"
        },
        limit: {
          type: "number",
          description: "Maximum results to return (default: 10, max: 50)"
        }
      },
      required: ["query"]
    }
  },
  {
    name: "list_agentiscript_categories",
    description: "List all AgentiScript icon categories with counts.",
    inputSchema: {
      type: "object",
      properties: {}
    }
  }
];

// Tool handlers
function _iconSlug(icon) {
  if (icon.slug) return icon.slug;
  if (icon.concept) return icon.concept.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  return icon.name;
}
function _iconLabel(icon) { return icon.label || icon.concept || icon.name || icon.slug || ''; }

function handleGetIcon(args) {
  const concept = (args.concept || '').toLowerCase().replace(/\s+/g, '-');
  const icon = iconMap[concept] || iconMap[args.concept.toLowerCase()];

  if (!icon) {
    // Try partial match
    const partial = icons.find(i =>
      (_iconSlug(i) && _iconSlug(i).includes(concept)) ||
      (_iconLabel(i) && _iconLabel(i).toLowerCase().includes(concept))
    );
    if (!partial) {
      return {
        found: false,
        concept: args.concept,
        message: `No AgentiScript icon found for "${args.concept}". Try search_agentiscript to find similar icons.`,
        searchUrl: `https://agentiscript.com/?q=${encodeURIComponent(args.concept)}`
      };
    }
    return formatIconResult(partial, true);
  }
  return formatIconResult(icon, false);
}

function formatIconResult(icon, partial) {
  const slug = _iconSlug(icon);
  const cdnUrl = `${CDN_BASE}/${slug}.svg`;
  const svgPath = path.join(__dirname, 'icons', `${slug}.svg`);
  let svg = null;
  if (fs.existsSync(svgPath)) {
    svg = fs.readFileSync(svgPath, 'utf8');
  }

  return {
    found: true,
    partial_match: partial || false,
    slug: slug,
    name: _iconLabel(icon),
    category: icon.category,
    tags: icon.tags || [],
    description: icon.description,
    cdn_url: cdnUrl,
    svg: svg || `<!-- SVG available at ${cdnUrl} -->`,
    purchase_url: `https://agentiscript.com/store/${slug}`,
    embed_html: `<img src="${cdnUrl}" alt="${_iconLabel(icon)}" width="64" height="64" />`
  };
}

function handleSearch(args) {
  const q = (args.query || '').toLowerCase();
  const limit = Math.min(args.limit || 10, 50);
  const results = [];

  for (const icon of icons) {
    if (results.length >= limit) break;
    const haystack = [
      _iconSlug(icon) || '',
      _iconLabel(icon) || '',
      icon.description || '',
      icon.definition || '',
      icon.concept || '',
      ...(icon.aliases || []),
      icon.category || '',
      ...(icon.tags || [])
    ].join(' ').toLowerCase();

    if (haystack.includes(q)) {
      results.push({
        slug: _iconSlug(icon),
        name: _iconLabel(icon),
        category: icon.category,
        tags: icon.tags || [],
        cdn_url: `${CDN_BASE}/${_iconSlug(icon)}.svg`,
        purchase_url: `https://agentiscript.com/store/${_iconSlug(icon)}`
      });
    }
  }

  return {
    query: args.query,
    count: results.length,
    total_icons: icons.length,
    results,
    browse_url: `https://agentiscript.com/?q=${encodeURIComponent(args.query)}`
  };
}

function handleListCategories() {
  const cats = {};
  for (const icon of icons) {
    const c = icon.category || 'uncategorized';
    cats[c] = (cats[c] || 0) + 1;
  }
  const sorted = Object.entries(cats)
    .sort((a, b) => b[1] - a[1])
    .map(([name, count]) => ({ name, count }));

  return {
    total_icons: icons.length,
    categories: sorted,
    browse_url: 'https://agentiscript.com'
  };
}

// MCP JSON-RPC 2.0 protocol handler
function handleRequest(req) {
  const { id, method, params } = req;

  if (method === 'initialize') {
    return {
      jsonrpc: '2.0',
      id,
      result: {
        protocolVersion: '2024-11-05',
        capabilities: { tools: {} },
        serverInfo: {
          name: 'agentiscript',
          version: '1.0.0'
        }
      }
    };
  }

  if (method === 'tools/list') {
    return {
      jsonrpc: '2.0',
      id,
      result: { tools }
    };
  }

  if (method === 'tools/call') {
    const { name, arguments: args } = params;
    let result;

    try {
      if (name === 'get_agentiscript_icon') {
        result = handleGetIcon(args);
      } else if (name === 'search_agentiscript') {
        result = handleSearch(args);
      } else if (name === 'list_agentiscript_categories') {
        result = handleListCategories();
      } else {
        return {
          jsonrpc: '2.0',
          id,
          error: { code: -32601, message: `Unknown tool: ${name}` }
        };
      }

      return {
        jsonrpc: '2.0',
        id,
        result: {
          content: [{
            type: 'text',
            text: JSON.stringify(result, null, 2)
          }]
        }
      };
    } catch (e) {
      return {
        jsonrpc: '2.0',
        id,
        error: { code: -32603, message: e.message }
      };
    }
  }

  // Unknown method
  return {
    jsonrpc: '2.0',
    id,
    error: { code: -32601, message: `Method not found: ${method}` }
  };
}

// Check if running in stdio MCP mode or standalone mode
if (process.stdin.isTTY === false || process.argv.includes('--stdio')) {
  // MCP stdio mode — read JSON-RPC from stdin, write to stdout
  const rl = readline.createInterface({ input: process.stdin });
  rl.on('line', (line) => {
    if (!line.trim()) return;
    try {
      const req = JSON.parse(line);
      const response = handleRequest(req);
      process.stdout.write(JSON.stringify(response) + '\n');
    } catch (e) {
      process.stdout.write(JSON.stringify({
        jsonrpc: '2.0',
        id: null,
        error: { code: -32700, message: 'Parse error' }
      }) + '\n');
    }
  });

  process.stderr.write(`[AgentiScript MCP] Server ready. ${icons.length} icons loaded.\n`);
} else {
  // Standalone info mode
  process.stdout.write(JSON.stringify({
    server: 'AgentiScript MCP Server',
    version: '1.0.0',
    icons_loaded: icons.length,
    tools: tools.map(t => ({ name: t.name, description: t.description })),
    usage: 'Run with --stdio flag or pipe JSON-RPC requests to stdin',
    mcp_config: {
      mcpServers: {
        agentiscript: {
          command: 'node',
          args: [path.resolve(__filename)]
        }
      }
    }
  }, null, 2) + '\n');
}
