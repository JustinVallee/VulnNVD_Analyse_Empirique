import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
year = 2021
df = pd.read_csv(f'../DataBoolExploited/cves_{year}_BoolExploited.csv')

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

# Select the metric
metric = metrics[11]
print(metric)

# Create the contingency table
contingency_table = pd.crosstab(df[f'{metric}'], df['exploited'])
print(contingency_table)

# Prepare data for scatter plot
x = contingency_table.index
#y_nonexploited = contingency_table[0]
y_exploited = contingency_table[1]
print(x)


# Plot the scatter plot
fig, ax = plt.subplots(figsize=(7, 6))  # Adjust the figsize as needed
#ax.scatter(x, y_nonexploited, label='Non Exploited')
ax.scatter(x, y_exploited, color='darkorange', label='Exploited')

formatted_string_metric = metric.rpartition('.')[-1]  # Format the metric name
plt.xlabel(f'{formatted_string_metric}')
plt.ylabel('Nombre de Vulnérabilités')
plt.legend(loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()


plt.show()
