import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
year = 2021
df = pd.read_csv(f'cves_{year}_BoolExploited_with_vendors_products.csv')

# Métrique à tester
metrics = [
    ## CATEGORICAL

    # Metadata
    'cve.CVE_data_meta.ASSIGNER',  # metrics[0]

    # Base Metrics
    'impact.baseMetricV3.cvssV3.attackVector',  # metrics[1]
    'impact.baseMetricV3.cvssV3.attackComplexity',  # metrics[2]
    'impact.baseMetricV3.cvssV3.privilegesRequired',  # metrics[3]
    'impact.baseMetricV3.cvssV3.userInteraction',  # metrics[4]

    # Scope
    'impact.baseMetricV3.cvssV3.scope',  # metrics[5]

    # Impact Metrics
    'impact.baseMetricV3.cvssV3.confidentialityImpact',  # metrics[6]
    'impact.baseMetricV3.cvssV3.integrityImpact',  # metrics[7]
    'impact.baseMetricV3.cvssV3.availabilityImpact',  # metrics[8]

    # Base severity
    'impact.baseMetricV3.cvssV3.baseSeverity',  # metrics[9]

    ## NUMBERS FLOATS

    # Score
    'impact.baseMetricV3.cvssV3.baseScore',  # metrics[10]
    'impact.baseMetricV3.exploitabilityScore',  # metrics[11]
    'impact.baseMetricV3.impactScore'  # metrics[12]
]

# Selection de la métrique
metric = metrics[2]
print(metric)

contingency_table = pd.crosstab(df[f'{metric}'], df['exploited'])
print(contingency_table)

countHigh = 0
# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Check if the value in the 'cisa' column is 1
    if row['impact.baseMetricV3.cvssV3.attackComplexity'] == 'HIGH' and row['exploited'] == 1:
        countHigh += 1
        print(row['Unique Vendors'])
print(countHigh)