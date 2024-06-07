import requests
# The URL for the API endpoint or form submission
url = 'https://uswest2.calabriocloud.com/api/rest/authorize'
# The data you want to send with the POST request
data = {
    "locale":   "en",  
    "userId":   "classic.wfm@calabrio.com",
    "password": "Cvg!@vumc.ipt"
}
# Making the POST request
response = requests.post(url, data=data)
# Output the response text (the content of the requested file)
print(response.text)
