import json, os

CATALOG = "/Users/colin/seo/agentiscript/agentiscript.json"

# NYC neighborhoods
nyc = ["manhattan-upper-east-side","manhattan-upper-west-side","manhattan-midtown","manhattan-downtown","manhattan-tribeca","manhattan-soho","manhattan-chelsea","manhattan-harlem","manhattan-washington-heights","brooklyn-williamsburg","brooklyn-park-slope","brooklyn-bedstuy","brooklyn-crown-heights","brooklyn-flatbush","brooklyn-bay-ridge","brooklyn-coney-island","queens-astoria","queens-flushing","queens-jamaica","queens-jackson-heights","bronx-riverdale","bronx-fordham","staten-island-north"]

# LA neighborhoods  
la = ["los-angeles-beverly-hills","los-angeles-bel-air","los-angeles-brentwood","los-angeles-santa-monica","los-angeles-malibu","los-angeles-venice","los-angeles-culver-city","los-angeles-west-hollywood","los-angeles-silver-lake","los-angeles-echo-park","los-angeles-downtown","los-angeles-koreatown","los-angeles-mid-wilshire","los-angeles-encino","los-angeles-sherman-oaks","los-angeles-studio-city","los-angeles-burbank","los-angeles-pasadena","los-angeles-long-beach","los-angeles-compton"]

# Chicago neighborhoods
chi = ["chicago-lincoln-park","chicago-wicker-park","chicago-bucktown","chicago-logan-square","chicago-old-town","chicago-gold-coast","chicago-river-north","chicago-loop","chicago-south-loop","chicago-pilsen","chicago-bronzeville","chicago-hyde-park","chicago-andersonville","chicago-rogers-park","chicago-evanston","chicago-oak-park","chicago-naperville","chicago-schaumburg","chicago-aurora"]

# Miami neighborhoods
miami = ["miami-brickell","miami-wynwood","miami-design-district","miami-little-havana","miami-coconut-grove","miami-coral-gables","miami-south-beach","miami-mid-beach","miami-north-beach","miami-aventura","miami-bal-harbour","miami-sunny-isles","miami-doral","miami-kendall","miami-homestead","miami-key-biscayne","miami-bay-harbor","miami-surfside"]

# Houston neighborhoods
houston = ["houston-heights","houston-montrose","houston-midtown","houston-downtown","houston-river-oaks","houston-memorial","houston-energy-corridor","houston-galleria","houston-sugar-land","houston-woodlands","houston-pearland","houston-katy","houston-cypress","houston-spring","houston-humble"]

# Dallas neighborhoods
dallas = ["dallas-uptown","dallas-downtown","dallas-oak-lawn","dallas-deep-ellum","dallas-bishop-arts","dallas-lake-highlands","dallas-preston-hollow","dallas-university-park","dallas-highland-park","dallas-frisco","dallas-plano","dallas-mckinney","dallas-allen","dallas-garland","dallas-irving"]

all_neighborhoods = nyc + la + chi + miami + houston + dallas

verticals = ["personal-injury-lawyer","real-estate-agent","dentist","financial-advisor","medspa","divorce-attorney","chiropractor","plastic-surgeon","roofing-contractor","mortgage-broker"]

with open(CATALOG) as f:
    catalog = json.load(f)
existing = set(i.get("slug") or i.get("name","") for i in catalog.get("icons",[]))
added = 0
batch = 0

for hood in all_neighborhoods:
    for vertical in verticals:
        slug = f"{hood}-{vertical}"
        if slug not in existing:
            catalog["icons"].append({"slug":slug,"name":slug,"concept":slug.replace("-"," ").title(),"category":"geo-neighborhood","tags":slug.split("-"),"license":"CC0"})
            existing.add(slug)
            added += 1
            if added % 5000 == 0:
                batch += 1
                catalog["total"] = len(catalog["icons"])
                with open(CATALOG,"w") as f:
                    json.dump(catalog,f,separators=(",",":"))
                total_now = catalog["total"]
                os.system(f'cd /Users/colin/seo/agentiscript && git add agentiscript.json && git commit -m "Neighborhood batch {batch}: {total_now}" && git push 2>&1 | tail -1')
                print(f"Batch {batch}: {added} | Total: {total_now}")

catalog["total"] = len(catalog["icons"])
with open(CATALOG,"w") as f:
    json.dump(catalog,f,separators=(",",":"))
total_final = catalog["total"]
os.system(f'cd /Users/colin/seo/agentiscript && git add agentiscript.json && git commit -m "Neighborhoods COMPLETE: {total_final}" && git push')
os.system(f'cp {CATALOG} /tmp/as-deploy/ && CLOUDFLARE_ACCOUNT_ID=e9249f4a4fff775f763d37ceae85fa9d /Users/colin/.local/bin/npx wrangler pages deploy /tmp/as-deploy --project-name agentiscript --branch main 2>&1 | tail -3')
print(f"COMPLETE: {added} added | Total: {total_final}")
