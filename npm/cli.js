#!/usr/bin/env node
/**
 * AgentiScript CLI
 * Usage:
 *   agentiscript get <slug>
 *   agentiscript search <query>
 *   agentiscript url <slug>
 *   agentiscript categories
 */

'use strict';

const { getIcon, searchIcons, listIcons, iconUrl, getIconMeta } = require('./index');

const [,, command, ...args] = process.argv;

switch (command) {
  case 'get': {
    const name = args.join(' ');
    const meta = getIconMeta(name);
    if (!meta) {
      console.error(`Icon not found: "${name}". Try: agentiscript search ${name}`);
      process.exit(1);
    }
    const slug = meta.slug || (meta.concept ? meta.concept.toLowerCase().replace(/[^a-z0-9]+/g, '-') : meta.name);
    const label = meta.label || meta.concept || meta.name || slug;
    console.log(`Slug:     ${slug}`);
    console.log(`Name:     ${label}`);
    console.log(`Category: ${meta.category}`);
    console.log(`Tags:     ${(meta.tags || []).join(', ')}`);
    console.log(`CDN URL:  ${iconUrl(name)}`);
    console.log(`Store:    https://agentiscript.com/store/${slug}`);
    break;
  }

  case 'search': {
    const query = args.join(' ');
    const results = searchIcons(query, { limit: 20 });
    if (!results.length) {
      console.log(`No icons found for "${query}"`);
      process.exit(0);
    }
    console.log(`Found ${results.length} icons for "${query}":\n`);
    for (const icon of results) {
      const slug = icon.slug || (icon.concept ? icon.concept.toLowerCase().replace(/[^a-z0-9]+/g, '-') : icon.name) || '';
      console.log(`  ${slug.padEnd(40)} ${icon.category || ''}`);
    }
    console.log(`\nBrowse: https://agentiscript.com/?q=${encodeURIComponent(query)}`);
    break;
  }

  case 'url': {
    const name = args.join(' ');
    const url = iconUrl(name);
    if (!url) {
      console.error(`Icon not found: "${name}"`);
      process.exit(1);
    }
    console.log(url);
    break;
  }

  case 'categories': {
    const icons = listIcons();
    const cats = {};
    for (const icon of icons) {
      const c = icon.category || 'uncategorized';
      cats[c] = (cats[c] || 0) + 1;
    }
    const sorted = Object.entries(cats).sort((a, b) => b[1] - a[1]);
    console.log(`AgentiScript — ${icons.length} icons across ${sorted.length} categories:\n`);
    for (const [name, count] of sorted) {
      console.log(`  ${String(count).padStart(5)}  ${name}`);
    }
    break;
  }

  default: {
    console.log(`AgentiScript CLI — The visual language of the agentic economy

Usage:
  agentiscript get <icon-slug>       Get icon info + CDN URL
  agentiscript search <query>        Search icons by keyword
  agentiscript url <icon-slug>       Print CDN URL only
  agentiscript categories            List all categories

Examples:
  agentiscript get x402
  agentiscript search blockchain
  agentiscript url agentic-loop
  
Website: https://agentiscript.com
`);
  }
}
