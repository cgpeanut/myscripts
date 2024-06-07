# This function opens the JSON file in read mode (`'r'`) and uses the `json.load()` 
# method to load the data from the file into a Python dictionary.

import json
def read_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

#data = read_json('data.json')
data = read_json('powerball_numbers.json')
print(data)
