import json, os

CATALOG = "/Users/colin/seo/agentiscript/agentiscript.json"

all_icons = []
for i in range(30):
    try:
        with open(f'/Users/colin/seo/agentiscript/agentiscript-chunk-{i:02d}.json') as f:
            all_icons.extend(json.load(f)['icons'])
    except: pass

print(f'Loaded: {len(all_icons)}')

# 10 more high-value verticals - two waves at once
verticals = [
    'criminal-defense-attorney','estate-planning-attorney',
    'workers-comp-attorney','slip-and-fall-lawyer',
    'medspa','botox-clinic','hair-salon','auto-body-shop',
    'kitchen-remodeling','bathroom-remodeling'
]

existing = set(i.get('slug') or i.get('name','') for i in all_icons)
added = 0
batch = 0

for zipnum in range(1, 100000):
    zipstr = str(zipnum).zfill(5)
    for vertical in verticals:
        slug = f'zip-{zipstr}-{vertical}'
        if slug not in existing:
            all_icons.append({'slug':slug,'name':slug,'concept':slug.replace('-',' ').title(),'category':'geo-zip','tags':['zip',zipstr,vertical],'license':'CC0'})
            existing.add(slug)
            added += 1
            if added % 200000 == 0:
                batch += 1
                catalog_data = {'total':len(all_icons),'chunks':0,'icons':[]}
                chunk_size = 100000
                chunks = [all_icons[i:i+chunk_size] for i in range(0, len(all_icons), chunk_size)]
                for ci, chunk in enumerate(chunks):
                    with open(f'/Users/colin/seo/agentiscript/agentiscript-chunk-{ci:02d}.json','w') as f:
                        json.dump({'chunk':ci,'total_chunks':len(chunks),'icons':chunk}, f, separators=(',',':'))
                total_now = len(all_icons)
                with open('/Users/colin/seo/agentiscript/agentiscript-index.json','w') as f:
                    json.dump({'total':total_now,'chunks':len(chunks),'chunk_size':chunk_size,'version':'7.0.0'}, f, separators=(',',':'))
                with open(CATALOG) as f:
                    main = json.load(f)
                main['total'] = total_now
                main['chunks'] = len(chunks)
                with open(CATALOG,'w') as f:
                    json.dump(main, f, separators=(',',':'))
                os.system(f'cd /Users/colin/seo/agentiscript && git add agentiscript.json agentiscript-index.json agentiscript-chunk-*.json && git commit -m "ZIP7 batch {batch}: {total_now}" && git push 2>&1 | tail -1')
                print(f'Batch {batch}: {added:,} | Total: {total_now:,}')

# Final
chunk_size = 100000
chunks = [all_icons[i:i+chunk_size] for i in range(0, len(all_icons), chunk_size)]
for ci, chunk in enumerate(chunks):
    with open(f'/Users/colin/seo/agentiscript/agentiscript-chunk-{ci:02d}.json','w') as f:
        json.dump({'chunk':ci,'total_chunks':len(chunks),'icons':chunk}, f, separators=(',',':'))
total_final = len(all_icons)
with open('/Users/colin/seo/agentiscript/agentiscript-index.json','w') as f:
    json.dump({'total':total_final,'chunks':len(chunks),'chunk_size':chunk_size,'version':'7.0.0'}, f, separators=(',',':'))
with open(CATALOG) as f:
    main = json.load(f)
main['total'] = total_final
main['chunks'] = len(chunks)
with open(CATALOG,'w') as f:
    json.dump(main, f, separators=(',',':'))
os.system(f'cd /Users/colin/seo/agentiscript && git add agentiscript.json agentiscript-index.json agentiscript-chunk-*.json && git commit -m "ZIP7 COMPLETE: {total_final}" && git push')
print(f'COMPLETE: {added:,} added | Total: {total_final:,}')
