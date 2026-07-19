const PAGES_ORIGIN = "https://agentiscript.pages.dev";

export default {
  async fetch(request) {
    const incoming = new URL(request.url);

    if (!incoming.pathname.startsWith("/icons/")) {
      return new Response("Not found", { status: 404 });
    }

    if (request.method !== "GET" && request.method !== "HEAD") {
      return new Response("Method not allowed", {
        status: 405,
        headers: { Allow: "GET, HEAD" },
      });
    }

    const upstream = new URL(incoming.pathname + incoming.search, PAGES_ORIGIN);
    return fetch(new Request(upstream, request));
  },
};
