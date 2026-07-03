import json, os

CATALOG = "/Users/colin/seo/agentiscript/agentiscript.json"

# Top 3 highest-value verticals
verticals = ["personal-injury-lawyer", "real-estate-agent", "dentist"]

with open(CATALOG) as f:
    catalog = json.load(f)

existing = set(i.get("slug") or i.get("name", "") for i in catalog.get("icons", []))
added = 0
batch = 0

# Generate zip-[000-999]-[vertical]
for prefix_int in range(1000):
    prefix = f"{prefix_int:03d}"
    for vertical in verticals:
        slug = f"zip-{prefix}-{vertical}"
        if slug not in existing:
            catalog["icons"].append({
                "slug": slug,
                "name": slug,
                "concept": f"ZIP {prefix} {vertical.replace('-', ' ').title()}",
                "category": "geo-zip",
                "tags": ["zip", prefix, vertical] + vertical.split("-"),
                "license": "CC0"
            })
            existing.add(slug)
            added += 1

            if added % 10000 == 0:
                batch += 1
                catalog["total"] = len(catalog["icons"])
                with open(CATALOG, "w") as f:
                    json.dump(catalog, f, separators=(",", ":"))
                total_now = catalog["total"]
                ret = os.system(
                    f'cd /Users/colin/seo/agentiscript && '
                    f'git add agentiscript.json && '
                    f'git commit -m "ZIP geo batch {batch}: {total_now} total" && '
                    f'git push 2>&1 | tail -1'
                )
                print(f"Batch {batch}: {added} added so far | Total in catalog: {total_now}")

# Final save + commit
catalog["total"] = len(catalog["icons"])
with open(CATALOG, "w") as f:
    json.dump(catalog, f, separators=(",", ":"))

total_final = catalog["total"]
print(f"\nFinal save complete. Total: {total_final} | New additions: {added}")

os.system(
    f'cd /Users/colin/seo/agentiscript && '
    f'git add agentiscript.json && '
    f'git commit -m "ZIP geo COMPLETE: {total_final} total ({added} new zip-prefix concepts)" && '
    f'git push'
)

# Deploy to Cloudflare Pages
print("\nDeploying to Cloudflare Pages...")
os.makedirs("/tmp/as-deploy", exist_ok=True)
os.system(f'cp {CATALOG} /tmp/as-deploy/')
deploy_ret = os.system(
    f'CLOUDFLARE_ACCOUNT_ID=e9249f4a4fff775f763d37ceae85fa9d '
    f'/Users/colin/.local/bin/npx wrangler pages deploy /tmp/as-deploy '
    f'--project-name agentiscript --branch main 2>&1 | tail -5'
)

print(f"\nCOMPLETE: Added {added} zip-prefix concepts | Final total: {total_final} | Deploy exit: {deploy_ret}")
