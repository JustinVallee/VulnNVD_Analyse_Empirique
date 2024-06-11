import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
year = 2021
df = pd.read_csv(f'../DataBoolExploited/cves_{year}_BoolExploited.csv')

# Métrique à tester
metrics = [
    ## CATEGORICAL

    # Base Metrics
    'impact.baseMetricV3.cvssV3.attackVector',  # metrics[0]
    'impact.baseMetricV3.cvssV3.attackComplexity',  # metrics[1]
    'impact.baseMetricV3.cvssV3.privilegesRequired',  # metrics[2]
    'impact.baseMetricV3.cvssV3.userInteraction',  # metrics[3]

    # Scope
    'impact.baseMetricV3.cvssV3.scope',  # metrics[4]

    # Impact Metrics
    'impact.baseMetricV3.cvssV3.confidentialityImpact',  # metrics[5]
    'impact.baseMetricV3.cvssV3.integrityImpact',  # metrics[6]
    'impact.baseMetricV3.cvssV3.availabilityImpact',  # metrics[7]

    # Base severity
    'impact.baseMetricV3.cvssV3.baseSeverity',  # metrics[8]

    ## NUMBERS FLOATS

    # Score
    'impact.baseMetricV3.cvssV3.baseScore',  # metrics[9]
    'impact.baseMetricV3.exploitabilityScore',  # metrics[10]
    'impact.baseMetricV3.impactScore'  # metrics[11]
]

# Selection de la métrique
metric = metrics[11]
print(metric)

# Create the contingency table
contingency_table = pd.crosstab(df[f'{metric}'], df['exploited'])
print(contingency_table)

# Calculate the ratio between exploited and non-exploited
ratio_exploited_nonexploited = contingency_table[1] / contingency_table[0]
print(ratio_exploited_nonexploited)

# Plot the contingency table
fig, ax = plt.subplots(figsize=(7, 6))  # Adjust the figsize as needed
contingency_table.plot(kind='bar', stacked=False, ax=ax)
plt.title(' ', size=25)

# nom de la métrique (27 pour enlever les 27 premier charactères impact.baseMetricV3.cvssV3.)
plt.xlabel(f'{metric[27:]}')

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
            # Add ratio annotation
            ratio_value = ratio_exploited_nonexploited.iloc[values] * 100
            # Adjust the vertical position of the ratio annotation based on the maximum height
            ax.text(values, max_height_plot, f'{ratio_value:.2f}%', va='bottom', ha='center', color="red")


plt.show()
