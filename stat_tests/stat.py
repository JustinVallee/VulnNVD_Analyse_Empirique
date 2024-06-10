import pandas as pd
from scipy.stats import chi2_contingency

# Read the CSV file into a DataFrame
year = 2019
df = pd.read_csv(f'datasets/correctedCves/cves_{year}.csv')

#Converts the graynoise_reports_count to binary (0/1) like the other sources/companies
df['graynoise_reports_count'] = df['graynoise_reports_count'].apply(lambda x: 1 if x > 0 else 0)


#CrossTab function in pandas to create contingency tables
dfContingTableSecureworksCisa = pd.crosstab(df['secureworks'], df['cisa'])
dfContingTableCisaClam = pd.crosstab(df['cisa'], df['clam'])
dfContingTableSecureworksClam = pd.crosstab(df['secureworks'], df['clam'])

dfContingTableSecureworksGreynoise = pd.crosstab(df['secureworks'], df['graynoise_reports_count'])
dfContingTableClamGreynoise = pd.crosstab(df['clam'], df['graynoise_reports_count'])
dfContingTableCisaGreynoise = pd.crosstab(df['cisa'], df['graynoise_reports_count'])


#!!!Select the right Contingency Table to use!!!
dfContingencyTable = dfContingTableCisaGreynoise

print("Contingency Table:")
print(dfContingencyTable)

# Perform the Chi-Square Test
chi2, p, dof, expected = chi2_contingency(dfContingencyTable.values)

# Output the results
print(f"\nChi2 Statistic: {chi2}")
print(f"P-value: {p}")
#print(f"Degrees of Freedom: {dof}")
#print(f"Expected Frequencies: \n{expected}")


# Interpret the p-value
alpha = 0.01
if p <= alpha:
    print("\nReject the null hypothesis - There is a significant association between the companies' reports.")
else:
    print("\nFail to reject the null hypothesis - There is no significant association between the companies' reports.")
