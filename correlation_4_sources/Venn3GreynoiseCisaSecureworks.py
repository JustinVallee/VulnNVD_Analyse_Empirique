import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn3

# Read the CSV file into a DataFrame
year = 2021
df = pd.read_csv(f'datasets/correctedCves/cves_{year}.csv')

#Converts the graynoise_reports_count to binary (0/1) like the other sources/companies
df['graynoise_reports_count'] = df['graynoise_reports_count'].apply(lambda x: 1 if x > 0 else 0)

# Calculate counts for each column
countGreynoise = df['graynoise_reports_count'].astype(bool).sum()
countCisa = df['cisa'].astype(bool).sum()
countSecureworks = df['secureworks'].astype(bool).sum()

# Calculate correlation counts
countABC = ((df['cisa'] != 0) & (df['secureworks'] != 0) & (df['graynoise_reports_count'] != 0)).sum()
countCisaSecureworks = ((df['cisa'] != 0) & (df['secureworks'] != 0) & (df['graynoise_reports_count'] == 0)).sum()
countCisaGreynoise = ((df['cisa'] != 0) & (df['secureworks'] == 0) & (df['graynoise_reports_count'] != 0)).sum()
countSecureworksGreynoise = ((df['cisa'] == 0) & (df['secureworks'] != 0) & (df['graynoise_reports_count'] != 0)).sum()


# Print counts
print("countGreynoise:", countGreynoise)
print("countClam:", countCisa)
print("countSecureworks:", countSecureworks)

print("\ncountABC:", countABC)
print("countClamSecureworks:", countCisaSecureworks)
print("countClamGreynoise:", countCisaGreynoise)
print("countSecureworksGreynoise:", countSecureworksGreynoise)


# Create Venn diagram
plt.figure()
venn3(subsets=(countCisa - countABC - countCisaSecureworks - countCisaGreynoise,
               countSecureworks - countABC - countCisaSecureworks - countSecureworksGreynoise,
               countCisaSecureworks,
               countGreynoise - countABC - countCisaGreynoise - countSecureworksGreynoise,
               countCisaGreynoise,
               countSecureworksGreynoise,
               countABC),
      set_labels=('Cisa', 'Secureworks', 'Greynoise'))

plt.show()
