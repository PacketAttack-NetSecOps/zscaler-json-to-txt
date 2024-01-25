#### This Python script parses the json file at config.zscaler.com for zscalertwo.net and exports CIDR ranges to a .txt file #####
#### Created by Justin Jones SecEng 1/23/2024 ####

import requests
import json

def fetch_json(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch JSON. Status code: {response.status_code}")
        return None

def extract_and_print_ranges(json_data, output_file):
    try:
        ranges = []
        for domain, domain_data in json_data.items():
            for continent, continent_data in domain_data.items():
                for city, entries in continent_data.items():
                    for entry in entries:
                        range_value = entry.get("range", "")
                        if range_value:
                            ranges.append(range_value)

        with open(output_file, 'w') as file:
            file.write("\n".join(str(range_value) for range_value in ranges))
        print(f"IP CIDR ranges written to {output_file}")
    except AttributeError:
        print("Error: Unable to extract CIDR blocks from the JSON data")

# Replace 'your_json_url' with the cloud URL of the JSON data from https://config.zscaler.com/
json_url = 'https://config.zscaler.com/api/zscalertwo.net/cenr/json'

# Replace 'zscalertwo_cidrs.txt' with the desired output file name
output_file_name = './test/zscalertwo_cidrs.txt'

# Fetch JSON data from the URL
json_data = fetch_json(json_url)

# If JSON data is fetched successfully, extract and print all ranges to a file
if json_data:
    extract_and_print_ranges(json_data, output_file_name)
