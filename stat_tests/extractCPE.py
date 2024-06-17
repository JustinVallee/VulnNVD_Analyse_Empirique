import pandas as pd
import re

#####Start Functions#####
def save_vendors_procucts_CSV():
    # Save the updated DataFrame to a new CSV file
    output_filename = f'cves_{year}_BoolExploited_with_vendors_products.csv'
    df.to_csv(output_filename, index=False)


def get_all_unique_vendors():
    # Initialize an empty set to store unique vendors
    unique_vendors = set()

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        row_vendors_products = row['vendors/products']

        # Iterate through each tuple (vendor, product) in the current row's list
        for vendor, product in row_vendors_products:
            # Add the vendor to the set (sets automatically handle uniqueness)
            unique_vendors.add(vendor)

    print("Set of unique vendors:", unique_vendors)


#####End Functions#####


# Read the CSV file into a DataFrame
year = 2021
df = pd.read_csv(f'../DataBoolExploited/cves_{year}_BoolExploited.csv')

# Initialize an empty list to store results
vendor_product_list = []

# Process each row in the DataFrame to extract vendor and product
for index, row in df.iterrows():
    cpe_string = row['configurations.nodes']

    # Pattern to find matches starting with cpe:2.3 and stopping at the fourth colon
    pattern = r'cpe:2\.3:[^:]+:[^:]+:[^:]+'

    # Find all matches using re.findall
    cpe_matches = re.findall(pattern, cpe_string)

    # Initialize a set to store vendors and products for the current row
    vendors_products_set = set()

    # Extract the 3rd and 4th positions after the colon and store in the set
    for cpe in cpe_matches:
        array_parts_string_cpe = cpe.split(':')

        vendor = array_parts_string_cpe[3]
        product = array_parts_string_cpe[4]
        vendors_products_set.add((vendor, product))

    # Append the list of vendors/products to the results list
    vendor_product_list.append(list(vendors_products_set))

# Add the results to the DataFrame as a new column
df['vendors/products'] = vendor_product_list

unique_vendors_all_rows = []

# Print each row's 'vendors/products' column
for index, row in df.iterrows():
    row_vendors_products = row['vendors/products']

    unique_vendors_row_set = set()
    for vendor, product in row_vendors_products:
        unique_vendors_row_set.add(vendor)

    #print(index,list(unique_vendors_row_set))
    unique_vendors_all_rows.append(list(unique_vendors_row_set))

df['Unique Vendors'] = unique_vendors_all_rows

df_row = 1
print('row', df_row, ':', df['Unique Vendors'][df_row])
print('row', df_row, ': vendor 1 -', df['Unique Vendors'][df_row][0])
print('row', df_row, ': vendor 2 -', df['Unique Vendors'][df_row][1])

#save_vendors_procucts_CSV()