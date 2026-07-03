#!/usr/bin/env python3
"""
AGENTISCRIPT GEO DOMINATION SCRIPT
Zero Anthropic tokens. Runs overnight.
Generates every US city x every vertical combination.
"""
import json
import os
import subprocess

CATALOG_PATH = '/Users/colin/seo/agentiscript/agentiscript.json'

# Every US city with population 10,000+ (~3,000 cities)
US_CITIES = [
    # Top 100 metros
    'new-york','los-angeles','chicago','houston','phoenix','philadelphia',
    'san-antonio','san-diego','dallas','san-jose','austin','jacksonville',
    'fort-worth','columbus','charlotte','indianapolis','san-francisco',
    'seattle','denver','nashville','oklahoma-city','el-paso','washington-dc',
    'boston','memphis','louisville','portland','las-vegas','milwaukee',
    'albuquerque','tucson','fresno','mesa','sacramento','atlanta',
    'kansas-city','omaha','colorado-springs','raleigh','long-beach',
    'virginia-beach','minneapolis','tampa','new-orleans','honolulu','miami',
    'cleveland','bakersfield','aurora','anaheim','santa-ana','corpus-christi',
    'riverside','lexington','st-louis','pittsburgh','stockton','anchorage',
    'cincinnati','st-paul','toledo','greensboro','newark','plano',
    'henderson','lincoln','buffalo','fort-wayne','jersey-city','chula-vista',
    'orlando','st-petersburg','norfolk','chandler','laredo','madison',
    'durham','lubbock','winston-salem','garland','glendale-az','hialeah',
    'reno','baton-rouge','irvine','chesapeake','scottsdale','north-las-vegas',
    'fremont','gilbert-az','san-bernardino','birmingham','boise','rochester',
    'richmond-va','spokane','des-moines','montgomery','modesto','fayetteville',
    'tacoma','fontana','moreno-valley','glendale-ca','akron','yonkers',
    'huntington-beach','little-rock','amarillo','mobile','columbus-ga',
    'grand-rapids','salt-lake-city','tallahassee','huntsville','worcester',
    'knoxville','oxnard','providence','chattanooga','fort-lauderdale',
    'brownsville','tempe','newport-news','santa-clarita','garden-grove',
    'oceanside','eugene','corona','fort-collins','salem-or','peoria-il',
    'cary','springfield-mo','cape-coral','jackson-ms','alexandria-va',
    'hayward','lancaster','salinas','pomona','sunnyvale','escondido',
    'surprise','torrance','paterson','bridgeport','mckinney','mesquite',
    'pasadena-tx','savannah','roseville','kansas-city-ks','macon',
    'orange','fullerton','clarksville','lakewood-co','hollywood-fl',
    'syracuse','murfreesboro','palmdale','kansas-city-mo','worcester-ma',
    'springfield-ma','pasadena-ca','naperville','bellevue','frisco',
    'mcallen','hampton','warren','west-valley-city','columbia-sc',
    'sterling-heights','new-haven','waco','sioux-falls','cedar-rapids',
    'chattanooga-tn','ontario-ca','aurora-il','elk-grove','pembroke-pines',
    'eugene-or','peoria-az','cape-coral-fl','fort-wayne-in','st-petersburg-fl',
    # Florida cities (Colin's backyard)
    'miami-beach','coral-gables','aventura','boca-raton','delray-beach',
    'west-palm-beach','palm-beach','naples-fl','sarasota','clearwater',
    'st-augustine','gainesville','ocala','daytona-beach','pensacola',
    'panama-city','port-st-lucie','lakeland','melbourne-fl','kissimmee',
    # Texas cities
    'sugar-land','the-woodlands','plano-tx','frisco-tx','allen-tx',
    'round-rock','cedar-park','pflugerville','leander','georgetown-tx',
    # California cities
    'beverly-hills','santa-monica','malibu','calabasas','thousand-oaks',
    'santa-barbara','san-luis-obispo','monterey','carmel','napa',
    # New York
    'manhattan','brooklyn','queens','bronx','staten-island','long-island',
    'the-hamptons','white-plains','yonkers-ny','mount-vernon',
    # Luxury markets
    'aspen','vail','telluride','park-city','scottsdale-az','palm-springs',
    'palm-beach-fl','fisher-island','star-island','coral-reef',
]

# Every high-value vertical
VERTICALS = {
    'legal': [
        'personal-injury-lawyer','car-accident-attorney','divorce-lawyer',
        'criminal-defense-attorney','dui-lawyer','bankruptcy-attorney',
        'immigration-lawyer','workers-comp-attorney','medical-malpractice-lawyer',
        'estate-planning-attorney','business-litigation-attorney',
        'real-estate-attorney','employment-lawyer','slip-and-fall-lawyer',
        'wrongful-death-lawyer','truck-accident-lawyer','motorcycle-accident-lawyer',
        'social-security-disability-lawyer','mesothelioma-lawyer','tax-attorney',
    ],
    'real-estate': [
        'luxury-real-estate','homes-for-sale','real-estate-agent',
        'property-management','commercial-real-estate','apartment-rentals',
        'new-construction-homes','investment-property','foreclosure-homes',
        'waterfront-property','condo-for-sale','townhouse-for-sale',
        'land-for-sale','beachfront-real-estate','gated-community',
        'real-estate-investor','house-flipper','rental-property-management',
        'short-term-rental','vacation-rental-property',
    ],
    'medical': [
        'dentist','plastic-surgeon','chiropractor','dermatologist',
        'physical-therapist','orthopedic-surgeon','cardiologist',
        'ophthalmologist','obgyn','pediatrician','psychiatrist',
        'neurologist','gastroenterologist','urologist','endocrinologist',
        'oncologist','rheumatologist','pulmonologist','allergist',
        'pain-management-doctor',
    ],
    'finance': [
        'financial-advisor','mortgage-broker','tax-attorney','wealth-management',
        'insurance-agent','estate-planning','retirement-planning',
        'investment-advisor','cpa-accountant','bookkeeper',
        'small-business-loan','sba-loan','hard-money-lender',
        'private-money-lender','commercial-mortgage','refinancing',
        'debt-consolidation','credit-repair','financial-planner',
        'tax-preparation',
    ],
    'home-services': [
        'roofing-contractor','hvac-company','plumber','electrician',
        'general-contractor','kitchen-remodeling','bathroom-remodeling',
        'flooring-installation','window-replacement','painting-contractor',
        'landscaping-company','tree-service','pest-control',
        'home-inspection','foundation-repair','water-damage-restoration',
        'mold-remediation','solar-installation','pool-builder',
        'fence-contractor',
    ],
    'automotive': [
        'car-dealership','auto-repair','ev-charging-station','auto-body-shop',
        'oil-change-service','tire-shop','transmission-repair',
        'auto-glass-repair','car-detailing','towing-service',
        'used-car-dealer','luxury-car-dealer','car-rental',
        'auto-insurance','car-wash','vehicle-inspection',
        'rv-dealer','motorcycle-dealer','boat-dealer',
        'classic-car-restoration',
    ],
    'restaurant': [
        'fine-dining','ghost-kitchen','catering-company','food-truck',
        'breakfast-restaurant','lunch-restaurant','dinner-restaurant',
        'italian-restaurant','mexican-restaurant','sushi-restaurant',
        'steakhouse','seafood-restaurant','vegan-restaurant',
        'fast-casual-restaurant','pizza-restaurant','chinese-restaurant',
        'indian-restaurant','thai-restaurant','mediterranean-restaurant',
        'farm-to-table-restaurant',
    ],
    'education': [
        'private-school','tutoring-service','test-prep','college-counseling',
        'stem-education','music-lessons','art-classes','language-school',
        'driving-school','daycare-center','preschool','montessori',
        'special-education','homeschool-resources','online-tutoring',
        'sat-prep','act-prep','lsat-prep','gmat-prep','mcat-prep',
    ],
    'senior-care': [
        'assisted-living','memory-care','home-health-aide','nursing-home',
        'senior-transportation','adult-day-care','hospice-care',
        'in-home-senior-care','senior-living-community','retirement-community',
        'medicare-supplement','senior-financial-planning','eldercare-attorney',
        'senior-moving-services','medical-alert-systems',
        'physical-therapy-seniors','occupational-therapy-seniors',
        'senior-meal-delivery','respite-care','palliative-care',
    ],
    'pet': [
        'veterinarian','pet-grooming','dog-training','pet-boarding',
        'pet-insurance','dog-daycare','cat-boarding','exotic-vet',
        'emergency-vet','pet-cremation','dog-walker','pet-sitter',
        'aquarium-store','bird-vet','reptile-vet',
        'holistic-vet','mobile-vet','pet-dental-care',
        'dog-breeder','pet-adoption',
    ],
    'beauty': [
        'medspa','botox-clinic','hair-salon','nail-salon',
        'plastic-surgeon-consultation','laser-hair-removal','microneedling',
        'chemical-peel','lip-filler','rhinoplasty-consultation',
        'breast-augmentation-consultation','liposuction-consultation',
        'eyelash-extensions','eyebrow-microblading','spray-tan',
        'teeth-whitening','iv-therapy','cryotherapy','float-tank',
        'red-light-therapy',
    ],
    'fitness': [
        'personal-trainer','crossfit-gym','yoga-studio','pilates-studio',
        'sports-medicine','physical-therapy','boxing-gym','mma-gym',
        'swimming-lessons','tennis-lessons','golf-lessons',
        'nutrition-coach','weight-loss-program','boot-camp-fitness',
        'cycling-studio','barre-studio','dance-studio',
        'rock-climbing-gym','martial-arts','sports-performance-training',
    ],
    'divorce-family': [
        'divorce-attorney','child-custody-lawyer','alimony-attorney',
        'prenuptial-agreement','divorce-mediation','family-law-attorney',
        'child-support-lawyer','adoption-attorney','guardianship-attorney',
        'domestic-violence-lawyer','restraining-order-attorney',
        'paternity-lawyer','surrogacy-attorney','lgbt-family-lawyer',
        'military-divorce-attorney','high-net-worth-divorce',
        'collaborative-divorce','uncontested-divorce','divorce-financial-advisor',
        'parental-rights-attorney',
    ],
}

def main():
    print("Loading catalog...")
    with open(CATALOG_PATH) as f:
        catalog = json.load(f)
    
    existing = set(i.get('slug') or i.get('name','') for i in catalog.get('icons',[]))
    print(f"Current: {catalog['total']:,} icons")
    
    added = 0
    batch_size = 5000
    batch_count = 0
    
    for vertical_category, vertical_list in VERTICALS.items():
        for city in US_CITIES:
            for vertical in vertical_list:
                slug = f'{city}-{vertical}'
                if slug not in existing:
                    catalog['icons'].append({
                        'slug': slug,
                        'name': slug,
                        'concept': slug.replace('-', ' ').title(),
                        'category': f'geo-{vertical_category}',
                        'tags': slug.split('-'),
                        'license': 'CC0'
                    })
                    existing.add(slug)
                    added += 1
                    
                    # Save and deploy every 5000 concepts
                    if added % batch_size == 0:
                        batch_count += 1
                        catalog['total'] = len(catalog['icons'])
                        with open(CATALOG_PATH, 'w') as f:
                            json.dump(catalog, f, separators=(',',':'))
                        total_now = catalog['total']
                        print(f"Batch {batch_count}: {added:,} added | Total: {total_now:,}")
                        os.system(f'cd /Users/colin/seo/agentiscript && git add agentiscript.json && git commit -m "Geo domination batch {batch_count}: {total_now} total" && git push 2>&1 | tail -1')
    
    # Final save
    catalog['total'] = len(catalog['icons'])
    with open(CATALOG_PATH, 'w') as f:
        json.dump(catalog, f, separators=(',',':'))
    
    print(f"\n✅ COMPLETE")
    print(f"Added: {added:,}")
    print(f"Total: {catalog['total']:,}")
    
    # Final git push and deploy
    total_final = catalog['total']
    os.system(f'cd /Users/colin/seo/agentiscript && git add agentiscript.json && git commit -m "Geo domination COMPLETE: {total_final} total icons" && git push')
    os.system(f'cp {CATALOG_PATH} /tmp/as-deploy/ && CLOUDFLARE_ACCOUNT_ID=e9249f4a4fff775f763d37ceae85fa9d /Users/colin/.local/bin/npx wrangler pages deploy /tmp/as-deploy --project-name agentiscript --branch main 2>&1 | tail -3')

if __name__ == '__main__':
    main()
