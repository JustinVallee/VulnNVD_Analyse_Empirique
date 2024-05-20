import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn2_circles, venn3, venn3_circles

df = pd.read_csv('datasets/cves_2020.csv')
#graynoise_reports_count, clam, secureworks,cisa

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

    print(row['graynoise_reports_count'])

print("countGraynoise: " + str(countGraynoise))
print("countClam: " + str(countClam))
print("countSecureworks: " + str(countSecureworks))
print("countCisa: " + str(countCisa))

print("\ncountABC: " + str(countABC))
print("countClamSecureworks: " + str(countClamSecureworks))
print("countClamCisa: " + str(countClamCisa))
print("countSecureworksCisa: " + str(countSecureworksCisa))

# Create Venn diagram
plt.figure()
venn3(subsets=(countClam-countABC-countClamSecureworks-countClamCisa,countSecureworks-countABC-countClamSecureworks-countSecureworksCisa,countClamSecureworks,countCisa-countABC-countClamCisa-countSecureworksCisa,countClamCisa,countSecureworksCisa,countABC), set_labels=('Clam', 'Secureworks', 'Cisa'))
plt.title("Venn Diagram of Common Non-Zero Values")
#plt.show()