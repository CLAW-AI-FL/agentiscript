// x402-worker.js
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;
    
    // CORS headers for bot access
    const headers = {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'application/json',
    };
    
    // Serve manifest for bot discovery (free)
    if (path === '/manifest.json' || path === '/agentiscript.json') {
      return fetch('https://agentiscript.pages.dev' + path);
    }
    
    // Icon endpoint — requires payment
    if (path.startsWith('/api/icons/')) {
      const slug = path.replace('/api/icons/', '').replace('.svg', '');
      
      // Check x402 payment header
      const paymentHeader = request.headers.get('X-Payment') || request.headers.get('x-payment');
      
      if (!paymentHeader) {
        // Return 402 Payment Required with x402 details
        return new Response(JSON.stringify({
          x402Version: 1,
          error: 'Payment Required',
          accepts: [{
            scheme: 'exact',
            network: 'hedera:mainnet',
            maxAmountRequired: '1000', // $0.001 in USDC tinycents
            resource: request.url,
            description: `AgentiScript icon: ${slug}`,
            mimeType: 'image/svg+xml',
            payTo: env.HBAR_WALLET_ADDRESS || 'HBAR_WALLET_PLACEHOLDER',
            maxTimeoutSeconds: 300,
            asset: '0.0.456858', // USDC on Hedera HTS
            extra: {
              name: 'AgentiScript',
              version: '3.0',
              iconSlug: slug
            }
          }]
        }), { status: 402, headers });
      }
      
      // Payment present — serve the icon
      const iconUrl = `https://agentiscript.pages.dev/icons/${slug}.svg`;
      const iconResponse = await fetch(iconUrl);
      
      if (!iconResponse.ok) {
        return new Response(JSON.stringify({error: 'Icon not found', slug}), { status: 404, headers });
      }
      
      const svg = await iconResponse.text();
      return new Response(JSON.stringify({
        slug,
        svg,
        license: 'commercial',
        source: 'agentiscript.com'
      }), { status: 200, headers: {...headers, 'X-Payment-Settled': 'true'} });
    }
    
    // Free search endpoint for bot discovery
    if (path === '/api/search') {
      const query = url.searchParams.get('q') || '';
      const manifestResponse = await fetch('https://agentiscript.pages.dev/agentiscript.json');
      const manifest = await manifestResponse.json();
      const results = manifest.icons
        .filter(i => i.concept?.toLowerCase().includes(query.toLowerCase()) || i.name?.toLowerCase().includes(query.toLowerCase()))
        .slice(0, 20)
        .map(i => ({slug: i.id || i.name, concept: i.concept, category: i.category}));
      return new Response(JSON.stringify({query, results, count: results.length}), {headers});
    }
    
    return new Response(JSON.stringify({name: 'AgentiScript x402 API', version: '1.0', docs: 'https://agentiscript.com/docs'}), {headers});
  }
};
