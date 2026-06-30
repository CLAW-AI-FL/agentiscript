/**
 * AgentiScript - The visual language of the agentic economy
 * 20,000+ icons for AI, blockchain, quantum, and every concept
 * the agentic economy speaks but cannot show.
 *
 * https://agentiscript.com
 */

'use strict';

const path = require('path');
const fs = require('fs');

const CDN_BASE = 'https://agentiscript.com/icons';
const MANIFEST_PATH = path.join(__dirname, 'agentiscript.json');

let _manifest = null;
let _iconMap = null;

function _loadManifest() {
  if (_manifest) return _manifest;
  try {
    const data = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
    _manifest = data.icons || data;
    return _manifest;
  } catch (e) {
    throw new Error(`AgentiScript: could not load manifest at ${MANIFEST_PATH}. ` +
      'Run: npm install agentiscript or ensure agentiscript.json is present.');
  }
}

function _buildIconMap() {
  if (_iconMap) return _iconMap;
  const icons = _loadManifest();
  _iconMap = {};
  for (const icon of icons) {
    // Support all schema formats:
    // v3: { slug, name, tags, category, description }
    // v1/v2: { name (=slug), label, tags, category }
    // v4 (AS-xxx): { id, slug, concept, definition, aliases, category, svg, tags }
    // derive slug: prefer explicit slug, then concept-slug, then name
    const conceptSlug = icon.concept ? icon.concept.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') : null;
    const slug = icon.slug || conceptSlug || icon.name;
    const displayName = icon.label || icon.concept || icon.name;
    if (slug) _iconMap[slug.toLowerCase()] = icon;
    if (displayName && slug && displayName.toLowerCase() !== slug.toLowerCase()) {
      _iconMap[displayName.toLowerCase()] = icon;
    }
    // Index aliases too (v4)
    if (icon.aliases) {
      for (const alias of icon.aliases) {
        const aKey = alias.toLowerCase().replace(/\s+/g, '-');
        if (!_iconMap[aKey]) _iconMap[aKey] = icon;
      }
    }
  }
  return _iconMap;
}

// Helper: get effective slug
function _slug(icon) {
  if (icon.slug) return icon.slug;
  if (icon.concept) return icon.concept.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  return icon.name;
}

// Helper: get display name
function _displayName(icon) {
  // v4: concept; v1/v2: label; v2/v3: name; fallback: slug
  return icon.label || icon.concept || icon.name || icon.slug || '';
}

/**
 * Get an SVG icon by slug or name.
 * Returns the SVG string if found locally, or a placeholder SVG with metadata.
 *
 * @param {string} name - Icon slug (e.g. 'x402', 'agentic-loop') or display name
 * @returns {string|null} SVG string or null if not found
 */
function getIcon(name) {
  if (!name) return null;
  const map = _buildIconMap();
  const key = name.toLowerCase().replace(/\s+/g, '-');
  const icon = map[key] || map[name.toLowerCase()];
  if (!icon) return null;

  // Try to load local SVG file
  const slug = _slug(icon);
  const svgPath = path.join(__dirname, 'icons', `${slug}.svg`);
  if (fs.existsSync(svgPath)) {
    return fs.readFileSync(svgPath, 'utf8');
  }

  // Return a metadata-embedded placeholder SVG
  const label = _displayName(icon);
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" data-slug="${slug}" data-category="${icon.category || ''}">
  <!-- AgentiScript icon: ${slug} -->
  <!-- CDN: ${CDN_BASE}/${slug}.svg -->
  <!-- Tags: ${(icon.tags || []).join(', ')} -->
  <rect width="100" height="100" fill="#0f172a" rx="12"/>
  <text x="50" y="55" font-family="monospace" font-size="10" fill="#38bdf8" text-anchor="middle">${label.substring(0, 16)}</text>
</svg>`;
}

/**
 * Search icons by query string (matches slug, name, tags, description, category).
 *
 * @param {string} query - Search term
 * @param {object} [opts] - Options
 * @param {number} [opts.limit=20] - Max results
 * @returns {Array} Matching icon objects
 */
function searchIcons(query, opts = {}) {
  if (!query) return [];
  const icons = _loadManifest();
  const q = query.toLowerCase();
  const limit = opts.limit || 20;
  const results = [];

  for (const icon of icons) {
    if (results.length >= limit) break;
    const haystack = [
      _slug(icon) || '',
      _displayName(icon) || '',
      icon.description || '',
      icon.definition || '',
      icon.concept || '',
      ...(icon.aliases || []),
      icon.category || '',
      ...(icon.tags || [])
    ].join(' ').toLowerCase();

    if (haystack.includes(q)) {
      results.push(icon);
    }
  }
  return results;
}

/**
 * Returns the full icon manifest array.
 *
 * @returns {Array} All icon objects
 */
function listIcons() {
  return _loadManifest();
}

/**
 * Returns the CDN URL for an icon by slug or name.
 *
 * @param {string} name - Icon slug or name
 * @returns {string|null} CDN URL or null if icon not found
 */
function iconUrl(name) {
  if (!name) return null;
  const map = _buildIconMap();
  const key = name.toLowerCase().replace(/\s+/g, '-');
  const icon = map[key] || map[name.toLowerCase()];
  if (!icon) return null;
  return `${CDN_BASE}/${_slug(icon)}.svg`;
}

/**
 * Get icon metadata (without SVG content).
 *
 * @param {string} name - Icon slug or name
 * @returns {object|null} Icon metadata object
 */
function getIconMeta(name) {
  if (!name) return null;
  const map = _buildIconMap();
  const key = name.toLowerCase().replace(/\s+/g, '-');
  return map[key] || map[name.toLowerCase()] || null;
}

module.exports = {
  getIcon,
  searchIcons,
  listIcons,
  iconUrl,
  getIconMeta,
  CDN_BASE
};
