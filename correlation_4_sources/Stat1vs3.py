import pandas as pd
from scipy.stats import chi2_contingency

# Read the CSV file into a DataFrame
year = 2019
df = pd.read_csv(f'datasets/correctedCves/cves_{year}.csv')

# Converts the graynoise_reports_count to binary (0/1) like the other sources/companies
df['graynoise_reports_count'] = df['graynoise_reports_count'].apply(lambda x: 1 if x > 0 else 0)

# Create a others_combined for the three sources
df['others_combined'] = df[['clam', 'secureworks', 'cisa']].sum(axis=1).apply(lambda x: 1 if x > 0 else 0)

# Define the source of interest
source_of_interest = 'graynoise_reports_count'

# Create the contingency table
contingency_table = pd.crosstab(df[source_of_interest], df['others_combined'])

print("Contingency Table:")
print(contingency_table)

# Perform the Chi-Square Test
chi2, p, dof, expected = chi2_contingency(contingency_table.values)

# Output the results
print(f"\nChi2 Statistic: {chi2}")
print(f"P-value: {p}")
#print(f"Degrees of Freedom: {dof}")
#print(f"Expected Frequencies: \n{expected}")

# Interpret the p-value
alpha = 0.01
if p <= alpha:
    print("\nReject the null hypothesis - There is a significant association between the sources' reports.")
else:
    print("\nFail to reject the null hypothesis - There is no significant association between the sources' reports.")
