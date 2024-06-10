import pandas as pd
import matplotlib.pyplot as plt
from venn import venn,pseudovenn


year = 2019
df = pd.read_csv(f'datasets/correctedCves/cves_{year}.csv')

#Converts the graynoise_reports_count to binary (0/1) like the other sources/companies
df['graynoise_reports_count'] = df['graynoise_reports_count'].apply(lambda x: 1 if x > 0 else 0)


# Define the sets
sets = {
    'Greynoise': set(),
    'Clam': set(),
    'Cisa': set(),
    'Secureworks': set()
}

vulnIdCounter = 0
nonExplCounter = 0

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    vulnIdCounter += 1
    if row['graynoise_reports_count'] == 1:
        sets['Greynoise'].add(vulnIdCounter)
    if row['clam'] == 1:
        sets['Clam'].add(vulnIdCounter)
    if row['cisa'] == 1:
        sets['Cisa'].add(vulnIdCounter)
    if row['secureworks'] == 1:
        sets['Secureworks'].add(vulnIdCounter)

    #count non exploited
    if row['graynoise_reports_count'] == 0 and row['clam'] == 0 and row['cisa'] == 0 and row['secureworks'] == 0:
        nonExplCounter += 1

print(sets)

# Create a 4-way Venn diagram
venn(sets)

# Write non epxloited in plot blank space
plt.annotate(f'{nonExplCounter}', xy=(0.5, 0.8), xycoords='axes fraction', fontsize=16, ha="center")

# The plot
plt.show()
