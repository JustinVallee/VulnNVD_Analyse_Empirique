import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn3

# Read the CSV file into a DataFrame
year = 2021
df = pd.read_csv(f'datasets/correctedCves/cves_{year}.csv')

# Calculate counts for each column
countClam = df['clam'].astype(bool).sum()
countSecureworks = df['secureworks'].astype(bool).sum()
countCisa = df['cisa'].astype(bool).sum()

# Calculate correlation counts
countABC = ((df['clam'] != 0) & (df['secureworks'] != 0) & (df['cisa'] != 0)).sum()
countClamSecureworks = ((df['clam'] != 0) & (df['secureworks'] != 0) & (df['cisa'] == 0)).sum()
countClamCisa = ((df['clam'] != 0) & (df['secureworks'] == 0) & (df['cisa'] != 0)).sum()
countSecureworksCisa = ((df['clam'] == 0) & (df['secureworks'] != 0) & (df['cisa'] != 0)).sum()


# Print counts
print("countClam:", countClam)
print("countSecureworks:", countSecureworks)
print("countCisa:", countCisa)
print("\ncountABC:", countABC)
print("countClamSecureworks:", countClamSecureworks)
print("countClamCisa:", countClamCisa)
print("countSecureworksCisa:", countSecureworksCisa)

# Create Venn diagram
plt.figure()
venn3(subsets=(countClam - countABC - countClamSecureworks - countClamCisa,
               countSecureworks - countABC - countClamSecureworks - countSecureworksCisa,
               countClamSecureworks,
               countCisa - countABC - countClamCisa - countSecureworksCisa,
               countClamCisa,
               countSecureworksCisa,
               countABC),
      set_labels=('Clam', 'Secureworks', 'Cisa'))


plt.show()
