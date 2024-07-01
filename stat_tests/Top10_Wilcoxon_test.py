from scipy.stats import wilcoxon

# Define rankings for each year
"""rankings_2019 = {
    'Microsoft': 1,
    'Apple': 2,
    'Google': 3,
    'Adobe': 4,
    'Cisco': 5,
    'Debian': 6,
    'Canonical': 7,
    'Oracle': 8,
    'Red Hat': 9,
    'openSUSE': 10
}

rankings_2020 = {
    'Microsoft': 1,
    'Debian': 2,
    'Fedora Project': 3,
    'Cisco': 4,
    'Oracle': 5,
    'Google': 6,
    'Apple': 7,
    'openSUSE': 8,
    'Canonical': 9,
    'Palo Alto Networks': 10
}

rankings_2021 = {
    'Microsoft': 1,
    'Fedora Project': 2,
    'Oracle': 3,
    'Debian': 4,
    'Google': 5,
    'NetApp': 6,
    'Apple': 7,
    'Cisco': 8,
    'Apache': 9,
    'FiberHome': 10
}"""

"""filtered_rankings_2019 = {
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
}"""
"""
filtered_rankings_2019 = {
    'Microsoft': 1,
    'Apple': 2,
    'Google': 3,
    'Cisco': 4,
    'Debian': 5,
    'Oracle': 6
}
filtered_rankings_2020 = {
    'Microsoft': 1,
    'Debian': 2,
    'Cisco': 3,
    'Google': 5,
    'Apple': 6,
    'Oracle': 4
}
filtered_rankings_2021 = {
    'Microsoft': 1,
    'Oracle': 2,
    'Debian': 3,
    'Google': 4,
    'Apple': 5,
    'Cisco': 6
}"""

filtered_rankings_2019 = {
    'Microsoft': 1,
    'Apple': 6,
    'Google': 3,
    'Cisco': 4,
    'Debian': 5,
    'Oracle': 2
}
filtered_rankings_2020 = {
    'Microsoft': 1,
    'Debian': 4,
    'Cisco': 5,
    'Google': 3,
    'Apple': 6,
    'Oracle': 2
}
filtered_rankings_2021 = {
    'Microsoft': 1,
    'Oracle': 2,
    'Debian': 3,
    'Google': 4,
    'Apple': 6,
    'Cisco': 5
}


# Calculate differences in ranks between 2019 and 2020
differences_2020 = {company: filtered_rankings_2019[company] - filtered_rankings_2020[company] for company in filtered_rankings_2019}

# Calculate differences in ranks between 2019 and 2021
differences_2021 = {company: filtered_rankings_2019[company] - filtered_rankings_2021[company] for company in filtered_rankings_2019}

# Calculate signed ranks
signed_ranks_2020 = [abs(rank) for rank in differences_2020.values()]
signed_ranks_2021 = [abs(rank) for rank in differences_2021.values()]

# Perform Wilcoxon signed-rank test
stat_2020, pval_2020 = wilcoxon(signed_ranks_2020)
stat_2021, pval_2021 = wilcoxon(signed_ranks_2021)

# Output results
print("Wilcoxon signed-rank test for 2019 vs 2020:")
print(f"   Test statistic: {stat_2020}")
print(f"   P-value: {pval_2020}")

print("\nWilcoxon signed-rank test for 2019 vs 2021:")
print(f"   Test statistic: {stat_2021}")
print(f"   P-value: {pval_2021}")
