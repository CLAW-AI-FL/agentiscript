import json, os

CATALOG = "/Users/colin/seo/agentiscript/agentiscript.json"

world_cities = [
    # UK
    "london-city","london-canary-wharf","london-mayfair","london-knightsbridge","london-chelsea",
    "london-kensington","london-notting-hill","london-shoreditch","london-hackney",
    "manchester","birmingham-uk","leeds","glasgow","edinburgh","bristol","liverpool",
    # Europe
    "paris-france","paris-8th-arrondissement","paris-16th-arrondissement",
    "berlin","munich","frankfurt-germany","hamburg","dusseldorf","cologne",
    "amsterdam-netherlands","rotterdam","the-hague",
    "madrid","barcelona","seville","valencia-spain",
    "milan","rome","florence","venice-italy",
    "zurich","geneva","basel","lugano",
    "vienna","salzburg",
    "stockholm","oslo","copenhagen","helsinki",
    "lisbon","porto",
    "brussels","antwerp",
    "monaco-city","luxembourg-city","liechtenstein",
    # Middle East
    "dubai-uae","abu-dhabi","sharjah","ajman",
    "riyadh","jeddah","neom",
    "doha-qatar","kuwait-city","manama-bahrain",
    "tel-aviv","jerusalem",
    "istanbul","ankara",
    # Asia Pacific
    "singapore-city","singapore-cbd","singapore-orchard",
    "hong-kong-central","hong-kong-wan-chai","hong-kong-kowloon",
    "tokyo-shibuya","tokyo-shinjuku","tokyo-ginza","tokyo-roppongi",
    "osaka","kyoto","yokohama","nagoya",
    "shanghai","beijing","shenzhen","guangzhou",
    "sydney-cbd","sydney-north-shore","melbourne","brisbane","perth",
    "seoul","busan",
    "mumbai","delhi","bangalore","hyderabad","chennai",
    "kuala-lumpur","jakarta","bangkok","ho-chi-minh-city",
    # Americas
    "toronto-canada","vancouver","calgary","montreal","ottawa",
    "mexico-city","guadalajara","monterrey-mexico",
    "sao-paulo","rio-de-janeiro","brasilia",
    "buenos-aires","bogota","lima","santiago-chile",
    "panama-city","san-jose-costa-rica",
    # Africa
    "johannesburg","cape-town","lagos","nairobi","cairo","casablanca",
]

verticals = [
    "luxury-real-estate","family-office","wealth-management",
    "private-banking","hedge-fund","yacht-charter",
    "private-aviation","fine-dining","crypto-hub","fintech-hub"
]

with open(CATALOG) as f:
    catalog = json.load(f)
existing = set(i.get("slug") or i.get("name","") for i in catalog.get("icons",[]))
added = 0
batch = 0

for city in world_cities:
    for vertical in verticals:
        slug = f"{city}-{vertical}"
        if slug not in existing:
            catalog["icons"].append({"slug":slug,"name":slug,"concept":slug.replace("-"," ").title(),"category":"geo-world","tags":slug.split("-"),"license":"CC0"})
            existing.add(slug)
            added += 1
            if added % 5000 == 0:
                batch += 1
                catalog["total"] = len(catalog["icons"])
                with open(CATALOG,"w") as f:
                    json.dump(catalog,f,separators=(",",":"))
                total_now = catalog["total"]
                os.system(f'cd /Users/colin/seo/agentiscript && git add agentiscript.json && git commit -m "World cities batch {batch}: {total_now}" && git push 2>&1 | tail -1')
                print(f"Batch {batch}: {added} | Total: {total_now}")

catalog["total"] = len(catalog["icons"])
with open(CATALOG,"w") as f:
    json.dump(catalog,f,separators=(",",":"))
total_final = catalog["total"]
os.system(f'cd /Users/colin/seo/agentiscript && git add agentiscript.json && git commit -m "World cities COMPLETE: {total_final}" && git push')
os.system(f'cp {CATALOG} /tmp/as-deploy/ && CLOUDFLARE_ACCOUNT_ID=e9249f4a4fff775f763d37ceae85fa9d /Users/colin/.local/bin/npx wrangler pages deploy /tmp/as-deploy --project-name agentiscript --branch main 2>&1 | tail -3')
print(f"COMPLETE: {added} added | Total: {total_final}")
