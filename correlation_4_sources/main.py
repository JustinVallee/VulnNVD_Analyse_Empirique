import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn3

year = 2021
#Convert CSV to parquet file
df = pd.read_csv(f'datasets/cves_{year}.csv', index_col=[0])
#df.to_parquet('datasets/cves_2021.parquet')
#df = pd.read_parquet(f'datasets/cves_{year}.parquet')

df.info()
#df['graynoise_reports_count'].astype('int8')
print("\nMAX:", df['graynoise_reports_count'].max(), "\n")

#Reduce the memory usage by reducing type
def set_dtypes(df):
    #df['clam'] = df['clam'].map({1:True,0:False})
    #df['secureworks'] = df['secureworks'].map({1:True,0:False})
    #df['cisa'] = df['cisa'].map({1:True,0:False})
    df['clam'] = df['clam'].astype('int8')
    df['secureworks'] = df['secureworks'].astype('int8')
    df['cisa'] = df['cisa'].astype('int8')
    return df

df.info()
df = set_dtypes(df)
print(df.head(10))

# Initialize a counter variable
countGraynoise = 0
countClam = 0
countSecureworks = 0
countCisa = 0

countABC = 0
countClamSecureworks = 0
countClamCisa = 0
countSecureworksCisa = 0

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Check if the value in the 'cisa' column is 1
    if row['graynoise_reports_count'] != 0:
        # Increment the counter
        countGraynoise += 1
    if row['clam'] != 0:
        # Increment the counter
        countClam += 1
    if row['secureworks'] != 0:
        # Increment the counter
        countSecureworks += 1
    if row['cisa'] != 0:
        # Increment the counter
        countCisa += 1

    # CorrelationsABC
    if row['clam'] and row['secureworks'] and row['cisa'] !=0:
        countABC +=1
    # Correlations CountClamSecureworks
    if (row['clam'] and row['secureworks'] !=0) and (row['cisa'] == 0):
        countClamSecureworks +=1
    # CorrelationsAC
    if (row['clam'] and row['cisa'] !=0) and (row['secureworks'] == 0):
        countClamCisa +=1
    # CorrelationsBC
    if (row['secureworks'] and row['cisa'] !=0) and (row['clam'] == 0):
        countSecureworksCisa +=1


print("\ncountGraynoise: " + str(countGraynoise))
print("countClam: " + str(countClam))
print("countSecureworks: " + str(countSecureworks))
print("countCisa: " + str(countCisa))

print("\ncountABC: " + str(countABC))
print("countClamSecureworks: " + str(countClamSecureworks))
print("countClamCisa: " + str(countClamCisa))
print("countSecureworksCisa: " + str(countSecureworksCisa))

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
plt.title(f"Corrélation des 3 sources (Common Non-Zero Values) en {year}")
plt.show()