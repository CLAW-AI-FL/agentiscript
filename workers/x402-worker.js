/**
 * AgentiScript x402 Micropayment Worker
 * Built: July 4th 2026 — America the Beautiful launch
 * 
 * FREE endpoints:
 *   GET /                          → info
 *   GET /manifest.json             → catalog manifest
 *   GET /agentiscript.json         → full catalog
 *   GET /api/search?q={query}      → icon search
 *   GET /api/icons/{slug}/preview  → low-res preview (free)
 *   GET /nft/{slug}                → NFT metadata (free)
 * 
 * PAID endpoints (x402):
 *   GET /api/icons/{slug}          → full SVG/PNG → 0.001 XRP
 *   GET /api/icons/{slug}.svg      → SVG asset → 0.001 XRP
 *   GET /api/icons/{slug}.png      → PNG asset → 0.001 XRP
 * 
 * NFT Collection: America the Beautiful — Mint 1
 * XRPL Wallet: rfFbKaT7pQTUsAYyEH8r5a6XTD45rz3aFe
 * Transfer Fee: 10% on all NFT resales
 */

const WALLET = 'rfFbKaT7pQTUsAYyEH8r5a6XTD45rz3aFe';
const PRICE_DROPS = '1000'; // 0.001 XRP in drops
const CATALOG_URL = 'https://agentiscript.pages.dev';
const NFT_COLLECTION = 'America the Beautiful — Mint 1';

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, X-Payment, x-payment',
};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    // OPTIONS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: CORS });
    }

    // ─── FREE: Root info
    if (path === '/') {
      return new Response(JSON.stringify({
        name: 'AgentiScript x402 API',
        version: '2.0.0',
        collection: NFT_COLLECTION,
        description: 'The visual language of the agentic economy. Bots pay 0.001 XRP per icon.',
        endpoints: {
          free: ['/manifest.json', '/agentiscript.json', '/api/search?q=', '/nft/{slug}'],
          paid: ['/api/icons/{slug}', '/api/icons/{slug}.svg', '/api/icons/{slug}.png']
        },
        pricing: { amount: '0.001 XRP', asset: 'XRP', network: 'xrpl:mainnet' },
        wallet: WALLET,
        nft: { collection: NFT_COLLECTION, supply: 500, royalty: '10%', chain: 'XRPL' },
        links: { site: 'https://agentiscript.com', store: 'https://agentiscript.com/store' }
      }, null, 2), {
        status: 200,
        headers: { ...CORS, 'Content-Type': 'application/json' }
      });
    }

    // ─── FREE: Manifest + catalog
    if (path === '/manifest.json' || path === '/agentiscript.json') {
      const resp = await fetch(CATALOG_URL + path);
      return new Response(resp.body, {
        status: resp.status,
        headers: { ...CORS, 'Content-Type': 'application/json' }
      });
    }

    // ─── FREE: Search
    if (path === '/api/search') {
      const q = url.searchParams.get('q') || '';
      const resp = await fetch(`${CATALOG_URL}/agentiscript.json`);
      const data = await resp.json();
      const icons = (data.icons || []).filter(i =>
        i.slug?.includes(q.toLowerCase()) || i.concept?.toLowerCase().includes(q.toLowerCase())
      ).slice(0, 20);
      return new Response(JSON.stringify({ query: q, count: icons.length, icons }), {
        status: 200,
        headers: { ...CORS, 'Content-Type': 'application/json' }
      });
    }

    // ─── FREE: NFT metadata
    if (path.startsWith('/nft/')) {
      const slug = path.replace('/nft/', '').replace(/\.(json|svg|png)$/, '');
      return new Response(JSON.stringify({
        collection: NFT_COLLECTION,
        slug,
        name: slug.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase()),
        chain: 'XRPL',
        wallet: WALLET,
        royalty: '10%',
        transferFee: 10000,
        svg_url: `https://agentiscript.com/icons/${slug}.svg`,
        png_url: `https://agentiscript.com/icons/${slug}.png`,
        marketplaces: [
          'https://firstledger.net',
          'https://xrp.cafe',
          'https://onxrp.com',
          'https://sologenic.com'
        ]
      }), {
        status: 200,
        headers: { ...CORS, 'Content-Type': 'application/json' }
      });
    }

    // ─── PAID: Icon endpoints
    if (path.startsWith('/api/icons/')) {
      const rawSlug = path.replace('/api/icons/', '');
      const slug = rawSlug.replace(/\.(svg|png)$/, '');
      const ext = rawSlug.endsWith('.png') ? 'png' : 'svg';
      const isFreePreview = path.includes('/preview');

      // Free preview
      if (isFreePreview) {
        return Response.redirect(`${CATALOG_URL}/icons/${slug}.svg`, 302);
      }

      // Check payment
      const paymentHeader = request.headers.get('X-Payment') || request.headers.get('x-payment');

      if (!paymentHeader) {
        // Return 402 with x402 payment details
        return new Response(JSON.stringify({
          x402Version: 1,
          error: 'Payment Required',
          accepts: [{
            scheme: 'exact',
            network: 'xrpl:mainnet',
            maxAmountRequired: PRICE_DROPS,
            resource: request.url,
            description: `AgentiScript icon: ${slug} — ${NFT_COLLECTION}`,
            mimeType: ext === 'png' ? 'image/png' : 'image/svg+xml',
            payTo: WALLET,
            maxTimeoutSeconds: 300,
            asset: 'XRP',
            extra: {
              name: 'AgentiScript',
              version: '2.0',
              slug,
              collection: NFT_COLLECTION,
              nft_info: `https://agentiscript.com/nft/${slug}`
            }
          }]
        }), {
          status: 402,
          headers: { ...CORS, 'Content-Type': 'application/json' }
        });
      }

      // Payment present — serve the asset
      const assetUrl = ext === 'png'
        ? `${CATALOG_URL}/icons/${slug}.png`
        : `${CATALOG_URL}/icons/${slug}.svg`;

      const assetResp = await fetch(assetUrl);

      if (!assetResp.ok) {
        return new Response(JSON.stringify({ error: 'Icon not found', slug }), {
          status: 404,
          headers: { ...CORS, 'Content-Type': 'application/json' }
        });
      }

      return new Response(assetResp.body, {
        status: 200,
        headers: {
          ...CORS,
          'Content-Type': ext === 'png' ? 'image/png' : 'image/svg+xml',
          'X-Payment-Settled': 'true',
          'X-AgentiScript-Slug': slug,
          'X-AgentiScript-Collection': NFT_COLLECTION,
          'Cache-Control': 'public, max-age=86400'
        }
      });
    }

    // 404
    return new Response(JSON.stringify({ error: 'Not found', docs: 'https://agentiscript.com' }), {
      status: 404,
      headers: { ...CORS, 'Content-Type': 'application/json' }
    });
  }
};
