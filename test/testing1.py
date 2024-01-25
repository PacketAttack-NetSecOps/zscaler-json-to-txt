import requests
import json

def process_json(url, output_file):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'range' in data:
            with open(output_file, 'w') as txt_file:
                txt_file.write(str(data['range']))

if __name__ == "__main__":
    json_url = "https://config.zscaler.com/api/zscalertwo.net/cenr/json"
    output_txt_file = "output.txt"
    process_json(json_url, output_txt_file)
