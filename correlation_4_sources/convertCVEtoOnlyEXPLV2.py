import pandas as pd
from time import time

# Read the CSV file into a DataFrame
df = pd.read_csv('datasets/cves_2021.csv')

# Add a new column 'exploited' using vectorized operations
df['exploited'] = ((df['graynoise_reports_count'] != 0) |
                   (df['clam'] != 0) |
                   (df['secureworks'] != 0) |
                   (df['cisa'] != 0)).astype(int)


"""
# Non vectorized
start_time = time()
exploited = []

for index, row in df.iterrows():
    if row['graynoise_reports_count'] != 0 or row['clam'] != 0 or row['secureworks'] != 0 or row['cisa'] != 0:
        exploited.append(1)
    else:
        exploited.append(0)
        
df['exploited'] = exploited

end_time = time()
t1 = end_time - start_time
print(t1)
"""

# Specify the columns to delete
columns_to_delete = ['graynoise_reports_count', 'clam', 'secureworks', 'cisa']
df.drop(columns=columns_to_delete, inplace=True)

# Write the updated DataFrame to a new CSV file
df.to_csv('datasets/cves_2021_NonAndExpl.csv', index=False)
