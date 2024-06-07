import requests
import json
url = 'https://uswest2.calabriocloud.com/api/rest/authorize'
data = {
    'userId': 'classic.wfm@calabrio.com',
    'password': 'Cvg!@vumc.ipt',
    'locale':   'en'
}
# Convert the dictionary to a JSON formatted string
json_data = json.dumps(data)
# Making the POST request with JSON data
response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
print(response.text)
