from scipy.stats import friedmanchisquare

# Define filtered rankings for each year
filtered_rankings_2019 = {
    'Microsoft': 1,
    'Apple': 2,
    'Google': 3,
    'Cisco': 5,
    'Debian': 6,
    'Oracle': 8
}

filtered_rankings_2020 = {
    'Microsoft': 1,
    'Debian': 2,
    'Cisco': 4,
    'Google': 6,
    'Apple': 7,
    'Oracle': 5
}

filtered_rankings_2021 = {
    'Microsoft': 1,
    'Oracle': 3,
    'Debian': 4,
    'Google': 5,
    'Apple': 7,
    'Cisco': 8
}

# Convert rankings to a list of lists
rankings_list = [list(filtered_rankings_2019.values()),
                 list(filtered_rankings_2020.values()),
                 list(filtered_rankings_2021.values())]

# Perform Friedman test
statistic, p_value = friedmanchisquare(*rankings_list)

# Output results
print("Friedman test:")
print(f"   Test statistic: {statistic}")
print(f"   P-value: {p_value}")

# Compare p-value to significance level (e.g., alpha = 0.05)
alpha = 0.05
if p_value < alpha:
    print(f"\nSince the p-value ({p_value}) is less than alpha ({alpha}), we reject the null hypothesis.")
    print("There are significant differences in rankings among the years.")
else:
    print(f"\nSince the p-value ({p_value}) is greater than or equal to alpha ({alpha}), we accept the null hypothesis.")
    print("There are no significant differences in rankings among the years.")
