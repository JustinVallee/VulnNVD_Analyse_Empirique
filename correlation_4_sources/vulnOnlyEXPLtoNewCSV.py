import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('datasets/cves_2021_exploited.csv')

# Initialize an empty list to store rows that meet the condition
filtered_rows = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Check if any of the specified columns have a value different from 0
    if row['graynoise_reports_count'] != 0 or row['clam'] != 0 or row['secureworks'] != 0 or row['cisa'] != 0:
        # Append the row to the list of filtered rows
        filtered_rows.append(row)

# Convert the list of filtered rows to a new DataFrame
filtered_df = pd.DataFrame(filtered_rows)

# Write the filtered DataFrame to a new CSV file
filtered_df.to_csv('datasets/cves_2021_OnlyExploited.csv')

