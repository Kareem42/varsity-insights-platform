import pandas as pd
import random

random.seed(42)

sports = [
    'Football', 'Basketball', 'Baseball', 'Softball',
    'Soccer', 'Volleyball', 'Track and Field', 'Swimming',
    'Tennis', 'Golf', 'Cross Country', 'Wrestling',
    'Cheerleading', 'Band', 'Dance Team'
]

# Load and normalize the 4 columns that actually exist
districts = pd.read_csv('data/raw/districts.csv')
districts.columns = [
    'district_name',
    'district_number',
    'tea_district_type',
    'tea_description',
    'nces_district_type',
    'nces_description',
    'charter_school'
]

# Force district_number to string to preserve leading zeros
districts['district_number'] = districts['district_number'].astype(str).str.zfill(6)

print("Columns normalized:", districts.columns.tolist())
print("Sample district numbers:", districts['district_number'].head(3).tolist())

rows = []
for _, district in districts.iterrows():
    if district['charter_school'] == 'Y':
        num_sports = random.randint(2, 6)
        base_participants = random.randint(10, 150)
    elif 'Rural' in str(district['tea_description']):
        num_sports = random.randint(3, 8)
        base_participants = random.randint(50, 300)
    else:
        num_sports = random.randint(6, 12)
        base_participants = random.randint(100, 800)

    selected_sports = random.sample(sports, num_sports)

    for sport in selected_sports:
        rows.append({
            'district_number': district['district_number'],
            'district_name': district['district_name'],
            'sport': sport,
            'participants': random.randint(
                base_participants // 2,
                base_participants
            ),
            'academic_year': '2023-2024',
            'charter_school': district['charter_school'],
            'tea_description': district['tea_description']
        })

df = pd.DataFrame(rows)
df.to_csv('data/raw/sports_participation.csv', index=False)
print(f"Generated {len(df)} rows")
print(f"Districts covered: {df['district_number'].nunique()}")
print(df.head(5))