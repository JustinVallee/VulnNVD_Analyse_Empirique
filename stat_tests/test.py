import re

# Your JSON string
json_str = '[{"operator": "AND", "children": [{"operator": "OR", "children": [], "cpe_match": [{"vulnerable": true, "cpe23Uri": "cpe:2.3:o:google:android:11.0:*:*:*:*:*:*:*", "cpe_name": []}]}, {"operator": "OR", "children": [], "cpe_match": [{"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a12:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a15:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a15s:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a31:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a33:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a5_2020:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a52:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a53:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a54_5g:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a73_5g:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a74_5g:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a9_2020:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a91:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a92:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a93:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_a94:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_f11_pro:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_f11_pro:-:*:*:*:marvel\\"s_avengers:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_find_x:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_find_x_lamborghini:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_find_x2:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_find_x2_pro:-:*:*:*:automobili_lamborghini:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_find_x2_pro:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_find_x3_pro:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_reno:-:*:*:*:fc_barcelona:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_reno_10x_zoom:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_reno_5g:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_reno_z:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_reno3:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_reno3_pro:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_reno4_5g:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_reno4_pro_5g:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_reno4_z_5g:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_reno5_4g:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_reno5_5g:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_reno5_pro_5g:-:*:*:*:*:*:*:*", "cpe_name": []}, {"vulnerable": false, "cpe23Uri": "cpe:2.3:h:oppo:oppo_x_2021:-:*:*:*:*:*:*:*", "cpe_name": []}]}], "cpe_match": []}]'

# Pattern to find matches starting with cpe:2.3 and stopping at the fourth colon
pattern = r'cpe:2\.3:[^:]+:[^:]+:[^:]+'

# Find all matches using re.findall
cpe_matches = re.findall(pattern, json_str)

print('HERE1',cpe_matches)

# Initialize an empty dictionary to store the results
results = {}

# Extract the 3rd and 4th positions after the colon and store in the dictionary (Vendor and Product)
for cpe in cpe_matches:
    array_parts_string_cpe = cpe.split(':')
    print('HERE2',array_parts_string_cpe)
    print(len(array_parts_string_cpe))

    if len(array_parts_string_cpe) == 5:  # Ensure there are enough parts
        vendor = array_parts_string_cpe[3]
        product = array_parts_string_cpe[4]
        results[cpe] = {'Vendor': vendor, 'Product': product}

# Print the dict results with key value pair Vendor/Product
for result, resultsCPE in results.items():
    print(f"{result}: Vendor: {resultsCPE['Vendor']}, Product: {resultsCPE['Product']}")


'''
import pandas as pd
import json
import re

# Read the CSV file into a DataFrame
year = 2021
df = pd.read_csv(f'../DataBoolExploited/cves_{year}_BoolExploited.csv')

# Function to preprocess JSON string, because if not error when load the json
def preprocess_json_string(json_str):
    # Replace single quotes with double quotes
    json_str = json_str.replace("'", '"')

    # Replace `True`, `False`, and `None` with `true`, `false`, and `null`
    json_str = re.sub(r'\bTrue\b', 'true', json_str)
    json_str = re.sub(r'\bFalse\b', 'false', json_str)
    json_str = re.sub(r'\bNone\b', 'null', json_str)

    return json_str


# Function to recursively extract cpe_match from JSON
def extract_cpe_matches(obj):
    matches = []

    # Extract cpe_match from the current level
    if isinstance(obj, dict):
        if 'cpe_match' in obj:
            matches.extend(obj['cpe_match'])
        # Recursively traverse children
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                matches.extend(extract_cpe_matches(value))
    elif isinstance(obj, list):
        for item in obj:
            matches.extend(extract_cpe_matches(item))

    return matches


# Initialize columns for vendor and product
df['Vendor'] = None
df['Product'] = None

# Process each row in the DataFrame to extract vendor and product
for index, row in df.iterrows():
    cpe_strings = row['configurations.nodes']

    try:
        # Preprocess the JSON string
        cpe_strings = preprocess_json_string(cpe_strings)

        # Load the list of JSON objects from the string
        data = json.loads(cpe_strings)

        # Initialize lists to collect vendors and products
        vendors = []
        products = []

        # Extract cpe_match entries recursively
        for obj in data:
            cpe_matches = extract_cpe_matches(obj)

            # Process each entry in cpe_matches
            for entry in cpe_matches:
                cpe_uri = entry.get('cpe23Uri', '')

                if cpe_uri:
                    # Split the CPE URI to extract vendor and product
                    split_uri = cpe_uri.split(':')
                    if len(split_uri) > 4:
                        vendor = split_uri[3]
                        product = split_uri[4]
                        vendors.append(vendor)
                        products.append(product)

        # Assign vendors and products to DataFrame columns
        if vendors and products:
            df.at[index, 'Vendor'] = ', '.join(vendors)
            df.at[index, 'Product'] = ', '.join(products)
            #(f"Row {index}: Vendors: {', '.join(vendors)}, Products: {', '.join(products)}")
        #else:
            #print(f"No 'cpe_match' entries found in row {index}, skipping.")

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON in row {index}: {e}")
        print(cpe_strings)
        break
        #continue

# Print the updated DataFrame
print(df)


'''