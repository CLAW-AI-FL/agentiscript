import json, os, time, requests, base64
from pathlib import Path

env = open(os.path.expanduser('~/.hermes/.env')).read()
api_key = ''
for line in env.split('\n'):
    if 'OPENAI_API_KEY' in line and '=' in line:
        api_key = line.split('=',1)[1].strip().strip('"').strip("'")
        break

print(f'API Key: {api_key[:10]}...')

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

manifest = json.load(open('/Users/colin/seo/agentiscript/mint/founding-500-manifest.json'))
items = manifest['items']

NAMES = {
    'bitcoin-strategic-reserve': 'Bitcoin Strategic Reserve',
    'ethereum-strategic-reserve': 'Ethereum Strategic Reserve',
    'solana-strategic-reserve': 'Solana Strategic Reserve',
    'cardano-strategic-reserve': 'Cardano Strategic Reserve',
    'xrp-strategic-reserve': 'XRP Strategic Reserve',
    'declaration-of-independence': 'Declaration of Independence',
    'us-constitution': 'U.S. Constitution',
    'bill-of-rights': 'Bill of Rights',
    'bald-eagle': 'Bald Eagle',
    'americas-250th': 'Americas 250th Anniversary',
    'drill-baby-drill': 'Drill Baby Drill',
    'second-amendment': 'Second Amendment',
    'dont-tread-on-me': "Don't Tread on Me - Gadsden Flag",
    'statue-of-liberty': 'Statue of Liberty',
    'liberty-bell': 'Liberty Bell',
    'mount-rushmore': 'Mount Rushmore',
    'american-flag': 'American Flag',
    'gold': 'Gold bar and coins',
    'silver': 'Silver bar and coins',
    'capitalism': 'Free market capitalism scales of commerce',
}

def get_name(slug):
    if slug in NAMES: return NAMES[slug]
    if slug.endswith('-president'): return slug.replace('-president','').replace('-',' ').title() + ' President'
    if slug.endswith('-founding'): return slug.replace('-founding','').replace('-',' ').title() + ' Founding Father'
    return slug.replace('-',' ').title()

out_dir = Path('/Users/colin/seo/agentiscript/icons')
out_dir.mkdir(exist_ok=True)

results = []
errors = []

test_slugs = [i['slug'] for i in items[:20]]
print(f'Total items: {len(items)}')
print(f'Test batch (20 slugs): {test_slugs}')
print()

for slug in test_slugs:
    png_path = out_dir / f'{slug}.png'
    if png_path.exists():
        print(f'SKIP (exists): {slug}')
        results.append(slug)
        continue
    
    name = get_name(slug)
    prompt = f'Minimalist icon of "{name}" for an American patriotic NFT collection. Dark navy background (#060610), gold and silver metallic line art, clean geometric style, centered composition, no text, professional digital art, 1024x1024'
    
    try:
        resp = requests.post(
            'https://api.openai.com/v1/images/generations',
            headers=headers,
            json={
                'model': 'gpt-image-1',
                'prompt': prompt,
                'n': 1,
                'size': '1024x1024',
                'quality': 'medium'
            },
            timeout=90
        )
        
        if resp.status_code == 200:
            data = resp.json()
            img_data = data['data'][0]
            if 'url' in img_data:
                url = img_data['url']
                img_resp = requests.get(url, timeout=30)
                if img_resp.status_code == 200:
                    png_path.write_bytes(img_resp.content)
                    print(f'OK (url): {slug} -> {png_path.name} ({len(img_resp.content):,} bytes)')
                    results.append(slug)
                else:
                    errors.append(f'{slug}: download failed {img_resp.status_code}')
                    print(f'ERROR download: {slug}: {img_resp.status_code}')
            elif 'b64_json' in img_data:
                img_bytes = base64.b64decode(img_data['b64_json'])
                png_path.write_bytes(img_bytes)
                print(f'OK (b64): {slug} -> {png_path.name} ({len(img_bytes):,} bytes)')
                results.append(slug)
            else:
                errors.append(f'{slug}: no url or b64_json in response: {list(img_data.keys())}')
                print(f'ERROR: {slug}: unexpected response keys: {list(img_data.keys())}')
        else:
            errors.append(f'{slug}: API error {resp.status_code} {resp.text[:200]}')
            print(f'ERROR API: {slug}: {resp.status_code} {resp.text[:200]}')
    except Exception as e:
        errors.append(f'{slug}: {e}')
        print(f'EXCEPTION: {slug}: {e}')
    
    time.sleep(2)

print(f'\n=== RESULTS ===')
print(f'Generated: {len(results)}')
print(f'Errors: {len(errors)}')
if errors:
    print('Error details:')
    for e in errors[:10]:
        print(f'  {e}')
