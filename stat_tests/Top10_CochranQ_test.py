import pingouin as pg
import pandas as pd

# Define rankings for each year
rankings_2019 = {
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
}

# Define all companies
all_companies = list(sorted(set(rankings_2019.keys()).union(set(rankings_2020.keys())).union(set(rankings_2021.keys()))))

# Create binary lists for each year indicating if a company is in top 10
def create_binary_list(rankings):
    binary_list = []
    for company in all_companies:
        if company in rankings and rankings[company] <= 10:
            binary_list.append(1)
        else:
            binary_list.append(0)
    return binary_list

# Generate binary lists for each year
binary_2019 = create_binary_list(rankings_2019)
binary_2020 = create_binary_list(rankings_2020)
binary_2021 = create_binary_list(rankings_2021)

# Print the generated binary lists
print("Binary list for 2019:", binary_2019)
print("Binary list for 2020:", binary_2020)
print("Binary list for 2021:", binary_2021)



#This is the Good data, function above dont work properly
#binary_2019 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
#binary_2020 = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0]
#binary_2021 = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1]

# Convert to DataFrame
data = pd.DataFrame({'2019': binary_2019, '2020': binary_2020, '2021': binary_2021})

# Perform Cochran's Q test
cochran_q = pg.cochran(data)

# Output results
print("Cochran's Q test:")
print(cochran_q)

# Compare p-value to significance level (e.g., alpha = 0.05)
alpha = 0.05
if cochran_q['p-unc'][0] < alpha:
    print(f"\nSince the p-value ({cochran_q['p-unc'][0]}) is less than alpha ({alpha}), we reject the null hypothesis.")
    print("There are significant differences in rankings among the years.")
else:
    print(f"\nSince the p-value ({cochran_q['p-unc'][0]}) is greater than or equal to alpha ({alpha}), we accept the null hypothesis.")
    print("There are no significant differences in rankings among the years.")
