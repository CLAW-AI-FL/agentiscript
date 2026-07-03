import json, os

CATALOG = "/Users/colin/seo/agentiscript/agentiscript.json"

# 7 more high-value verticals for every zip
verticals = ["divorce-attorney","financial-advisor","roofing-contractor","chiropractor","medspa","plastic-surgeon","mortgage-broker"]

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
            if added % 100000 == 0:
                batch += 1
                catalog["total"] = len(catalog["icons"])
                with open(CATALOG,"w") as f:
                    json.dump(catalog,f,separators=(",",":"))
                total_now = catalog["total"]
                os.system(f'cd /Users/colin/seo/agentiscript && git add agentiscript.json && git commit -m "ZIP2 batch {batch}: {total_now}" && git push 2>&1 | tail -1')
                print(f"ZIP2 Batch {batch}: {added:,} added | Total: {total_now:,}")

catalog["total"] = len(catalog["icons"])
with open(CATALOG,"w") as f:
    json.dump(catalog,f,separators=(",",":"))
total_final = catalog["total"]
os.system(f'cd /Users/colin/seo/agentiscript && git add agentiscript.json && git commit -m "ZIP2 COMPLETE: {total_final}" && git push')
print(f"COMPLETE: {added:,} added | Total: {total_final:,}")
