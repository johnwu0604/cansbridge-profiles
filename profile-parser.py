import pandas as pd
import json

# load csv file
original_df = pd.read_csv('profiles.csv')

# change column names
original_df.rename(columns={
    'Name': 'name', 
    'Internship Year': 'internship_year', 
    'School': 'school', 
    'Degree(s)': 'degree', 
    'Graduated?': 'graduated',
    'Graduation Year': 'graduation_year', 
    'Current Location': 'current_location', 
    'Current Company': 'current_company',
    'Current Position': 'current_position', 
    'Past Jobs (Position @ Company)': 'past_jobs', 
    'Past Schools': 'past_schools',
    'Other Fellowships/Programs': 'other_programs', 
    'Email': 'email', 
    'Asia Internship Company': 'asia_internship_company',
    'Asia Internship City': 'asia_internship_city', 
    'Asia Internship Country': 'asia_internship_country'
}, inplace=True)

# fill all nan values with empty string
original_df.fillna('', inplace=True)

# create fellow map array
fellow_map = []
for index, row in original_df.iterrows():
    item = {}
    item['name'] = row['name']
    item['school'] = row['school']
    item['degree'] = row['degree']
    item['graduation_year'] = row['graduation_year']
    item['current_location'] = row['current_location'] 
    item['current_company'] = row['current_company']
    item['internship_year'] = row['internship_year']
    item['asia_internship_company'] = row['asia_internship_company']
    item['asia_internship_city'] = row['asia_internship_city']
    item['asia_internship_country'] = row['asia_internship_country']
    fellow_map.append(item)

# write to json file
with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(fellow_map, f, ensure_ascii=False, indent=4)
