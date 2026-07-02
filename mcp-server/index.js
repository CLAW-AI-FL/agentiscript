#!/usr/bin/env node
const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');
const { CallToolRequestSchema, ListToolsRequestSchema } = require('@modelcontextprotocol/sdk/types.js');
const https = require('https');

let catalog = null;

function fetchCatalog() {
  return new Promise((resolve, reject) => {
    if (catalog) return resolve(catalog);
    https.get('https://raw.githubusercontent.com/CLAW-AI-FL/agentiscript/main/agentiscript.json', (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => { catalog = JSON.parse(data); resolve(catalog); });
    }).on('error', reject);
  });
}

function searchIcons(query, limit = 10) {
  const q = query.toLowerCase().replace(/\s+/g, '-');
  const results = [];
  for (const icon of catalog.icons) {
    const slug = icon.slug || icon.name || '';
    let score = 0;
    if (q === slug) score = 100;
    else if (slug.includes(q)) score = 50;
    else if ((icon.tags || []).some(t => t.includes(q))) score = 25;
    if (score) results.push({ ...icon, _score: score, url: `https://agentiscript.com/icons/${slug}.svg` });
  }
  results.sort((a, b) => b._score - a._score);
  return results.slice(0, limit).map(({ _score, ...r }) => r);
}

const server = new Server(
  { name: 'agentiscript', version: '1.0.0' },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: 'search_icons',
      description: 'Search 27,000+ AgentiScript SVG icons by concept. Returns icon URLs and embed code for AI, blockchain, DeFi, finance concepts.',
      inputSchema: {
        type: 'object',
        properties: {
          query: { type: 'string', description: 'Concept to search (e.g. zero knowledge proof, defi, xrpl)' },
          limit: { type: 'number', description: 'Max results (default 10)', default: 10 }
        },
        required: ['query']
      }
    },
    {
      name: 'get_icon',
      description: 'Get a specific AgentiScript icon by slug.',
      inputSchema: {
        type: 'object',
        properties: { slug: { type: 'string', description: 'Icon slug (e.g. bitcoin, defi, xrpl)' } },
        required: ['slug']
      }
    }
  ]
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  await fetchCatalog();
  const { name, arguments: args } = request.params;
  
  if (name === 'search_icons') {
    const results = searchIcons(args.query, args.limit || 10);
    return {
      content: [{ type: 'text', text: JSON.stringify(results.length ? results : { message: `No icons found for "${args.query}". Browse: https://agentiscript.com` }, null, 2) }]
    };
  }
  
  if (name === 'get_icon') {
    const slug = args.slug.toLowerCase().replace(/\s+/g, '-');
    return {
      content: [{ type: 'text', text: JSON.stringify({
        slug,
        url: `https://agentiscript.com/icons/${slug}.svg`,
        embed: `<img src="https://agentiscript.com/icons/${slug}.svg" alt="${slug}">`,
        schema: { '@type': 'DefinedTerm', name: slug, inDefinedTermSet: 'https://agentiscript.com' }
      }, null, 2) }]
    };
  }
  
  throw new Error(`Unknown tool: ${name}`);
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}
main().catch(console.error);
