import json

profiles = []
locations = {}

# load existing profiles
with open('profiles.json') as f:
    profiles = json.load(f)

# load exisiting locations
with open('locations.json') as f:
    locations = json.load(f)

for item in profiles:

    # input info for current company
    current_company = item['current_company']
    if current_company != '' and current_company not in locations:
        lat, lon = input('Enter latitude and longitude for {}. Enter "s s" to skip.: '.format(current_company)).split()
        if lat == 's':
            continue
        locations[current_company] = { 'lat': lat, 'lon': lon }
        # ask user if they want to continue
        cont = input('Type "y" to continue and type "n" to exit: ')
        if cont == 'n':
            break

    # input info for asia company
    asia_company = item['asia_internship_company']
    if asia_company != '' and asia_company not in locations:
        lat, lon = input('Enter latitude and longitude for {}. Enter "s s" to skip.: '.format(asia_company)).split()
        if lat == 's':
            continue
        locations[asia_company] = { 'lat': lat, 'lon': lon }
        # ask user if they want to continue
        cont = input('Type "y" to continue and type "n" to exit: ')
        if cont == 'n':
            break
    

# write to json file
with open('locations.json', 'w', encoding='utf-8') as f:
    json.dump(locations, f, ensure_ascii=False, indent=4)
