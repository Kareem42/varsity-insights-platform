import pandas as pd
import numpy as np
import random

# Sports Varsity Brands would actually distribute for
sports = [
    'Football', 'Basketball', 'Baseball', 'Softball',
    'Soccer', 'Volleyball', 'Track and Field', 'Swimming',
    'Tennis', 'Golf', 'Cross Country', 'Wrestling'
]

# Load your real districts as the foundation
districts = pd.read_csv('data/raw/districts.csv')

rows = []
for _, district in districts.iterrows():
    # Charter schools and rural districts have lower participation
    if district['Charter School (Y/N)'] == 'Y':
        num_sports = random.randint(2, 6)
        base_participants = random.randint(10, 150)
    elif 'Rural' in str(district['TEA_Description']):
        num_sports = random.randint(3, 8)
        base_participants = random.randint(50, 300)
    else:
        num_sports = random.randint(6, 12)
        base_participants = random.randint(100, 800)
    
    selected_sports = random.sample(sports, num_sports)
    
    for sport in selected_sports:
        rows.append({
            'district_number': district['District Number'],
            'district_name': district['District'],
            'sport': sport,
            'participants': random.randint(
                base_participants // 2,
                base_participants
            ),
            'academic_year': '2023-2024'
        })

df = pd.DataFrame(rows)
df.to_csv('data/raw/sports_participation.csv', index=False)
print(f"Generated {len(df)} rows")
print(df.head(10))