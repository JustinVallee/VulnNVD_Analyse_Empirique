import ast
from collections import Counter, defaultdict

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
year = 2021
df = pd.read_csv(f'cves_{year}_BoolExploited_with_vendors_products.csv')

#all_unique_exploited_vendors = set() # un set pour garder seulement les uniques pour savoir qui compter
all_exploited_vendors = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    if row['exploited'] == 1:
        if row['Unique Vendors'] != '[]':
            list_cell = ast.literal_eval(row['Unique Vendors'])
            for vendor in list_cell:
                #all_unique_exploited_vendors.add(vendor)
                all_exploited_vendors.append(vendor)


# Count occurrences of each vendor
vendor_counts = Counter(all_exploited_vendors) # Counts as a Counter obj, same format as a dict but its an obj

# Convert Counter object to dictionary
count_all_vendors = dict(vendor_counts)


# Sort vendors by count in descending order
sorted_vendors = sorted(count_all_vendors.items(), key=lambda item: item[1], reverse=True) # reverse ou décroissant

# Get the top 10 vendors
top_10_vendors = sorted_vendors[:10]
print(top_10_vendors)

top_10_vendors_name = []
for tuple_vendor in top_10_vendors:
    top_10_vendors_name.append(tuple_vendor[0])

print(top_10_vendors_name)

#-----STARTs- OLD method ------
'''top_10_vendors_NonExploited_count = [0] * 10

# Iterate over each row in the DataFrame
for vendor_name in top_10_vendors_name:
    for index, row in df.iterrows():
        if row['exploited'] == 0 and row['Unique Vendors'] != '[]':
            list_cell = ast.literal_eval(row['Unique Vendors'])
            for vendor in list_cell:
                if vendor == vendor_name:
                    top_10_vendors_NonExploited_count[top_10_vendors_name.index(vendor_name)] += 1
                    break

print(top_10_vendors_NonExploited_count)'''
#-----ENDS- OLD method ------

#-----STARTs- Optimal method ------
# Initialize dictionary to store counts of non-exploited vulnerabilities per vendor
top_10_vendors_non_exploited_count = defaultdict(int)

# Create a set of top 10 vendor names for fast lookup
top_10_vendors_set = set(top_10_vendors_name)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    if row['exploited'] == 0 and row['Unique Vendors'] != '[]':
        list_cell = ast.literal_eval(row['Unique Vendors'])
        for vendor in list_cell:
            if vendor in top_10_vendors_set:
                top_10_vendors_non_exploited_count[vendor] += 1

# Convert the defaultdict back to a list to match the order of top_10_vendors_name
top_10_vendors_non_exploited_count_list = [top_10_vendors_non_exploited_count[vendor] for vendor in top_10_vendors_name]

print(top_10_vendors_non_exploited_count_list)
#-----ENDS- Optimal method ------

top_10_vendors_percentage_exploited = []

# Iterate over each vendor tuple in top_10_vendors using enumerate to get the index
for index, (vendor, count) in enumerate(top_10_vendors):
    # Access non-exploited count using the index
    non_exploited_count = top_10_vendors_non_exploited_count_list[index]
    total = non_exploited_count + count
    percent = count / total * 100
    formatted_percent = f"{percent:.2f}"
    # Print vendor information
    print(f"{vendor}, Expl: {count}, Non-Expl {non_exploited_count}, Percentage: {formatted_percent}%")

    tuple_vendor_percent = (vendor, percent)
    top_10_vendors_percentage_exploited.append(tuple_vendor_percent)

print(top_10_vendors_percentage_exploited)

# Sort the list in descending order based on the percentage (second element of each tuple)
sorted_top_10_vendors_percentage_exploited = sorted(top_10_vendors_percentage_exploited, key=lambda x: x[1], reverse=True)

print(sorted_top_10_vendors_percentage_exploited)

for vendor, percentage in sorted_top_10_vendors_percentage_exploited:
    print(f"{vendor}: {percentage:.2f}%")