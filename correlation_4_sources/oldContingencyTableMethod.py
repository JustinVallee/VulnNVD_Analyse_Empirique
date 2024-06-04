import pandas as pd
from scipy.stats import chi2_contingency
import Venn3CisaClamSecureworks

#Was in mainOptimized
"""
countNOTClamNOTSecureworks = ((df['clam'] == 0) & (df['secureworks'] == 0)).sum()
countNOTClamNOTCisa = ((df['clam'] == 0) & (df['cisa'] == 0)).sum()
countNOTSecureworksNOTCisa = ((df['secureworks'] == 0) & (df['cisa'] == 0)).sum()
print("countNOTClamNOTSecureworks:", countNOTClamNOTSecureworks)
print("countNOTClamNOTCisa:", countNOTClamNOTCisa)
print("countNOTSecureworksNOTCisa:", countNOTSecureworksNOTCisa)
"""

# Create a DataFrame
BothAB = mainOptimized.countClamSecureworks
AOnly = mainOptimized.countClam
BOnly = mainOptimized.countSecureworks
NorAB = mainOptimized.countNOTClamNOTSecureworks

dataClamSecureworks = {
    'Company B: Exploited': [BothAB, AOnly],
    'Company B: Not Exploited': [BOnly, NorAB]
}

dataClamCisa = {
    'Company B: Exploited': [mainOptimized.countClamCisa, mainOptimized.countClam],
    'Company B: Not Exploited': [mainOptimized.countCisa, mainOptimized.countNOTClamNOTCisa]
}

dataSecureworksCisa = {
    'Company B: Exploited': [mainOptimized.countSecureworksCisa, mainOptimized.countSecureworks],
    'Company B: Not Exploited': [mainOptimized.countCisa, mainOptimized.countNOTSecureworksNOTCisa]
}


dfContingencyTable = pd.DataFrame(dataSecureworksCisa, index=['Company A: Exploited', 'Company A: Not Exploited'])
print("Contingency Table of: SecureworksCisa")
print(dfContingencyTable)

# Perform the Chi-Square Test
chi2, p, dof, expected = chi2_contingency(dfContingencyTable.values)

# Output the results
print(f"\nChi2 Statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of Freedom: {dof}")
print(f"Expected Frequencies: \n{expected}")


observed_true_true = dfContingencyTable.at['Company A: Exploited', 'Company B: Exploited']
expected_true_true = expected[0][0]

print(f"\nObserved count for both True: {observed_true_true}")
print(f"Expected count for both True: {expected_true_true}")


# Interpret the p-value
alpha = 0.03
if p <= alpha:
    print("\nReject the null hypothesis - There is a significant association between the companies' reports.")
else:
    print("\nFail to reject the null hypothesis - There is no significant association between the companies' reports.")
