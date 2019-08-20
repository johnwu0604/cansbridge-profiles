import json

profiles = []
current_companies = {}
asia_companies = {}
schools = {}

# load existing profiles
with open('profiles.json') as f:
    profiles = json.load(f)

# load exisiting locations
with open('current-companies.json') as f:
    current_companies = json.load(f)

with open('asia-companies.json') as f:
    asia_companies = json.load(f)

with open('schools.json') as f:
    schools = json.load(f)

for item in profiles:

    # input info for current company
    current_company = item['current_company']
    if current_company != '' and current_company not in current_companies:
        lat, lon = input('Enter latitude and longitude for {}. Enter "s s" to skip. Enter "n n" to end: '.format(current_company)).split()
        if lat == 's':
            continue
        if lat == 'n':
            break
        current_companies[current_company] = { 'lat': lat, 'lon': lon }

    # input info for asia company
    asia_company = item['asia_internship_company']
    if asia_company != '' and asia_company not in asia_companies:
        lat, lon = input('Enter latitude and longitude for {}. Enter "s s" to skip. Enter "n n" to end: '.format(asia_company)).split()
        if lat == 's':
            continue
        if lat == 'n':
            break
        asia_companies[asia_company] = { 'lat': lat, 'lon': lon }

    # input for schools
    school = item['school']
    if school != '' and school not in schools:
        lat, lon = input('Enter latitude and longitude for {}. Enter "s s" to skip. Enter "n n" to end: '.format(school)).split()
        if lat == 's':
            continue
        if lat == 'n':
            break
        schools[school] = { 'lat': lat, 'lon': lon }
    

# write to json file
with open('current-companies.json', 'w', encoding='utf-8') as f:
    json.dump(current_companies, f, ensure_ascii=False, indent=4)

with open('asia-companies.json', 'w', encoding='utf-8') as f:
    json.dump(asia_companies, f, ensure_ascii=False, indent=4)

with open('schools.json', 'w', encoding='utf-8') as f:
    json.dump(schools, f, ensure_ascii=False, indent=4)
