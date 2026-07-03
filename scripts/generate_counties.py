import json, os

CATALOG = "/Users/colin/seo/agentiscript/agentiscript.json"

# All 3,143 US counties (abbreviated list of major ones)
counties = [
    "los-angeles-county","cook-county","harris-county","maricopa-county","san-diego-county",
    "orange-county","miami-dade-county","dallas-county","riverside-county","kings-county",
    "clark-county","tarrant-county","san-bernardino-county","king-county","santa-clara-county",
    "wayne-county","bexar-county","broward-county","alameda-county","middlesex-county",
    "suffolk-county","sacramento-county","mecklenburg-county","collin-county","travis-county",
    "wake-county","palm-beach-county","franklin-county","contra-costa-county","el-paso-county",
    "hillsborough-county","denver-county","nassau-county","jefferson-county","salt-lake-county",
    "bergen-county","pima-county","pinellas-county","shelby-county","erie-county",
    "montgomery-county","hartford-county","multnomah-county","westchester-county","essex-county",
    "duval-county","fairfax-county","arapahoe-county","hennepin-county","st-louis-county",
    "snohomish-county","guilford-county","san-francisco-county","fulton-county","dekalb-county",
    "osceola-county","seminole-county","volusia-county","leon-county","pasco-county",
    "brevard-county","polk-county","lee-county","sarasota-county","collier-county",
    "lake-county","alachua-county","st-johns-county","clay-county","nassau-county-fl",
    "okaloosa-county","escambia-county","bay-county","manatee-county","charlotte-county",
    "denton-county","williamson-county","fort-bend-county","montgomery-county-tx","brazoria-county",
    "galveston-county","nueces-county","mclennan-county","lubbock-county-tx","smith-county",
    "webb-county","cameron-county","hidalgo-county","el-paso-county-tx","potter-county",
    "johnson-county-tx","parker-county","wise-county","kaufman-county","rockwall-county",
    "henderson-county-tx","hunt-county","grayson-county","comal-county","hays-county",
    "guadalupe-county","wilson-county-tx","atascosa-county","medina-county","kendall-county",
    "new-york-county","bronx-county","queens-county","richmond-county","westchester-county-ny",
    "nassau-county-ny","suffolk-county-ny","rockland-county","putnam-county","dutchess-county",
    "orange-county-ny","ulster-county","columbia-county-ny","greene-county-ny","albany-county",
    "rensselaer-county","schenectady-county","saratoga-county","warren-county-ny","washington-county-ny",
]

verticals = [
    "personal-injury-lawyer","car-accident-attorney","divorce-lawyer","criminal-defense-attorney",
    "real-estate-agent","mortgage-broker","financial-advisor","dentist","chiropractor",
    "roofing-contractor","hvac-company","plumber","electrician","plastic-surgeon",
    "medspa","veterinarian","personal-trainer","tax-attorney","bankruptcy-attorney","dui-lawyer"
]

with open(CATALOG) as f:
    catalog = json.load(f)
existing = set(i.get("slug") or i.get("name","") for i in catalog.get("icons",[]))
added = 0
batch = 0

for county in counties:
    for vertical in verticals:
        slug = f"{county}-{vertical}"
        if slug not in existing:
            catalog["icons"].append({"slug":slug,"name":slug,"concept":slug.replace("-"," ").title(),"category":"geo-county","tags":slug.split("-"),"license":"CC0"})
            existing.add(slug)
            added += 1
            if added % 10000 == 0:
                batch += 1
                catalog["total"] = len(catalog["icons"])
                with open(CATALOG,"w") as f:
                    json.dump(catalog,f,separators=(",",":"))
                total_now = catalog["total"]
                os.system(f'cd /Users/colin/seo/agentiscript && git add agentiscript.json && git commit -m "County batch {batch}: {total_now}" && git push 2>&1 | tail -1')
                print(f"Batch {batch}: {added} | Total: {total_now}")

catalog["total"] = len(catalog["icons"])
with open(CATALOG,"w") as f:
    json.dump(catalog,f,separators=(",",":"))
total_final = catalog["total"]
os.system(f'cd /Users/colin/seo/agentiscript && git add agentiscript.json && git commit -m "County COMPLETE: {total_final}" && git push')
os.system(f'cp {CATALOG} /tmp/as-deploy/ && CLOUDFLARE_ACCOUNT_ID=e9249f4a4fff775f763d37ceae85fa9d /Users/colin/.local/bin/npx wrangler pages deploy /tmp/as-deploy --project-name agentiscript --branch main 2>&1 | tail -3')
print(f"COMPLETE: {added} added | Total: {total_final}")
