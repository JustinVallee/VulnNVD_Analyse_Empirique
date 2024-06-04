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
countCisa = df['cisa'].astype(bool).sum()

# Calculate correlation counts
countABC = ((df['clam'] != 0) & (df['cisa'] != 0) & (df['graynoise_reports_count'] != 0)).sum()
countClamCisa = ((df['clam'] != 0) & (df['cisa'] != 0) & (df['graynoise_reports_count'] == 0)).sum()
countClamGraynoise = ((df['clam'] != 0) & (df['cisa'] == 0) & (df['graynoise_reports_count'] != 0)).sum()
countCisaGraynoise = ((df['clam'] == 0) & (df['cisa'] != 0) & (df['graynoise_reports_count'] != 0)).sum()


# Print counts
print("countGraynoise:", countGraynoise)
print("countClam:", countClam)
print("countSecureworks:", countCisa)

print("\ncountABC:", countABC)
print("countClamSecureworks:", countClamCisa)
print("countClamGraynoise:", countClamGraynoise)
print("countSecureworksGraynoise:", countCisaGraynoise)


# Create Venn diagram
plt.figure()
venn3(subsets=(countClam - countABC - countClamCisa - countClamGraynoise,
               countCisa - countABC - countClamCisa - countCisaGraynoise,
               countClamCisa,
               countGraynoise - countABC - countClamGraynoise - countCisaGraynoise,
               countClamGraynoise,
               countCisaGraynoise,
               countABC),
      set_labels=('Clam', 'Cisa', 'Graynoise'))


plt.title(f"Corrélation des 3 sources (Common Exploited) en {year}")
plt.show()
