import json, os

CATALOG = "/Users/colin/seo/agentiscript/agentiscript.json"

verticals = ["personal-injury-lawyer","real-estate-agent","dentist"]

with open(CATALOG) as f:
    catalog = json.load(f)
existing = set(i.get("slug") or i.get("name","") for i in catalog.get("icons",[]))
added = 0
batch = 0

for zipnum in range(1, 100000):
    zipstr = str(zipnum).zfill(5)
    for vertical in verticals:
        slug = f"zip-{zipstr}-{vertical}"
        if slug not in existing:
            catalog["icons"].append({"slug":slug,"name":slug,"concept":slug.replace("-"," ").title(),"category":"geo-zip","tags":["zip",zipstr,vertical],"license":"CC0"})
            existing.add(slug)
            added += 1
            if added % 50000 == 0:
                batch += 1
                catalog["total"] = len(catalog["icons"])
                with open(CATALOG,"w") as f:
                    json.dump(catalog,f,separators=(",",":"))
                total_now = catalog["total"]
                os.system(f'cd /Users/colin/seo/agentiscript && git add agentiscript.json && git commit -m "ZIP batch {batch}: {total_now}" && git push 2>&1 | tail -1')
                print(f"ZIP Batch {batch}: {added:,} added | Total: {total_now:,}")

catalog["total"] = len(catalog["icons"])
with open(CATALOG,"w") as f:
    json.dump(catalog,f,separators=(",",":"))
total_final = catalog["total"]
os.system(f'cd /Users/colin/seo/agentiscript && git add agentiscript.json && git commit -m "ZIP COMPLETE: {total_final}" && git push')
os.system(f'cp {CATALOG} /tmp/as-deploy/ && CLOUDFLARE_ACCOUNT_ID=e9249f4a4fff775f763d37ceae85fa9d /Users/colin/.local/bin/npx wrangler pages deploy /tmp/as-deploy --project-name agentiscript --branch main 2>&1 | tail -3')
print(f"COMPLETE: {added:,} added | Total: {total_final:,}")
