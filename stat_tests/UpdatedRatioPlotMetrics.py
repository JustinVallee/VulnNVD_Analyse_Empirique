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

# Selection de la métrique
metric = metrics[1]
print(metric)

# Create the contingency table
contingency_table = pd.crosstab(df[f'{metric}'], df['exploited'])
print(contingency_table)

# Calculate the sum of all values in column 0 (Non Exploited)
sum_non_exploited = contingency_table[0].sum()
print("Sum of Non Exploited values:", sum_non_exploited)

# Calculate the sum of all values in column 1 (Exploited)
sum_exploited = contingency_table[1].sum()
print("Sum of Exploited values:", sum_exploited)

# Calculate the ratio between exploited and non-exploited
ratio_non_exploited = contingency_table[0] / sum_non_exploited
ratio_exploited = contingency_table[1] / sum_exploited

# Plot the contingency table
fig, ax = plt.subplots(figsize=(7, 6))  # Adjust the figsize as needed
contingency_table.plot(kind='bar', stacked=False, ax=ax)
plt.title(' ', size=25)

# Nom de la métrique
formatted_string_metric = metric.rpartition('.')[-1]
plt.xlabel(f'{formatted_string_metric}')

plt.ylabel('Nombre de Vulnérabilités')
plt.legend(labels=['Non Exploited', 'Exploited'])
plt.xticks(rotation=45)
plt.tight_layout()

# Get the current y-axis limits
ylim = ax.get_ylim()

# Extract the maximum value of the y-axis (top of the plot)
max_height_plot = ylim[1]

# Add text annotations for each bar and its ratio
for values in range(len(contingency_table)):
    for exploited in range(len(contingency_table.columns)):
        value = contingency_table.iloc[values, exploited]
        if exploited == 0:  # 'Non Exploited'
            ax.text(values - 0.23, value, str(value), va='bottom')
        else:  # 'Exploited'
            ax.text(values + 0.025, value, str(value), va='bottom')

            # Adjust the vertical position of the ratio annotation based on the maximum height
            ax.text(values, max_height_plot, f'{ratio_exploited.iloc[values] * 100:.2f}%', va='bottom', ha='center', color="darkorange")
            ax.text(values, max_height_plot + 500, f'{ratio_non_exploited.iloc[values] * 100:.2f}%', va='bottom', ha='center', color="royalblue")

plt.show()
