import pandas as pd
from scipy.stats import chi2_contingency

# Read the CSV file into a DataFrame
year = 2021
df = pd.read_csv(f'../DataBoolExploited/cves_{year}_BoolExploited.csv')

# Fonction pour tester les variables catégorielles avec le test du Chi-carré
def chi2_test(df, col):
    contingency_table = pd.crosstab(df[col], df['exploited'])
    print(contingency_table)

    chi2, p_value, _, _ = chi2_contingency(contingency_table)
    return p_value

# Facteurs à tester
factors = [
    'impact.baseMetricV3.cvssV3.attackVector',
    'impact.baseMetricV3.cvssV3.attackComplexity',
    'impact.baseMetricV3.cvssV3.privilegesRequired',
    'impact.baseMetricV3.cvssV3.userInteraction'
]

# Appliquer les tests
results = {}
for factor in factors:
    p_value = chi2_test(df, factor)
    results[factor] = {'p-value': p_value}

# Afficher les résultats
for factor, result in results.items():
    print(f"Facteur: {factor}")
    print(f"p-value: {result['p-value']}\n")
