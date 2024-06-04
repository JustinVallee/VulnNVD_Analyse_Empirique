import pandas as pd
import matplotlib.pyplot as plt
from venn import venn,pseudovenn


year = 2021
df = pd.read_csv(f'datasets/correctedCves/cves_{year}.csv')

#Converts the graynoise_reports_count to binary (0/1) like the other sources/companies
df['graynoise_reports_count'] = df['graynoise_reports_count'].apply(lambda x: 1 if x > 0 else 0)


# Define the sets
sets = {
    'Graynoise': set(),
    'Clam': set(),
    'Cisa': set(),
    'Secureworks': set()
}

counter = 0

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    counter+=1
    if row['graynoise_reports_count'] == 1:
        sets['Graynoise'].add(counter)
    if row['clam'] == 1:
        sets['Clam'].add(counter)
    if row['cisa'] == 1:
        sets['Cisa'].add(counter)
    if row['secureworks'] == 1:
        sets['Secureworks'].add(counter)

print(sets)

# Create a 4-way Venn diagram
venn(sets)

# The plot
plt.title(f"Corrélation des 4 sources (Common Exploited) en {year}")
plt.show()