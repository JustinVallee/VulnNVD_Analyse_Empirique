import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn3

# Read the CSV file into a DataFrame
year = 2021
df = pd.read_csv(f'datasets/correctedCves/cves_{year}.csv')

#Converts the graynoise_reports_count to binary (0/1) like the other sources/companies
df['graynoise_reports_count'] = df['graynoise_reports_count'].apply(lambda x: 1 if x > 0 else 0)

# Calculate counts for each column
countGraynoise = df['graynoise_reports_count'].astype(bool).sum()
countClam = df['clam'].astype(bool).sum()
countSecureworks = df['secureworks'].astype(bool).sum()

# Calculate correlation counts
countABC = ((df['clam'] != 0) & (df['secureworks'] != 0) & (df['graynoise_reports_count'] != 0)).sum()
countClamSecureworks = ((df['clam'] != 0) & (df['secureworks'] != 0) & (df['graynoise_reports_count'] == 0)).sum()
countClamGraynoise = ((df['clam'] != 0) & (df['secureworks'] == 0) & (df['graynoise_reports_count'] != 0)).sum()
countSecureworksGraynoise = ((df['clam'] == 0) & (df['secureworks'] != 0) & (df['graynoise_reports_count'] != 0)).sum()


# Print counts
print("countGraynoise:", countGraynoise)
print("countClam:", countClam)
print("countSecureworks:", countSecureworks)

print("\ncountABC:", countABC)
print("countClamSecureworks:", countClamSecureworks)
print("countClamGraynoise:", countClamGraynoise)
print("countSecureworksGraynoise:", countSecureworksGraynoise)


# Create Venn diagram
plt.figure()
venn3(subsets=(countClam - countABC - countClamSecureworks - countClamGraynoise,
               countSecureworks - countABC - countClamSecureworks - countSecureworksGraynoise,
               countClamSecureworks,
               countGraynoise - countABC - countClamGraynoise - countSecureworksGraynoise,
               countClamGraynoise,
               countSecureworksGraynoise,
               countABC),
      set_labels=('Clam', 'Secureworks', 'Graynoise'))


plt.title(f"Corrélation des 3 sources (Common Exploited) en {year}")
plt.show()
