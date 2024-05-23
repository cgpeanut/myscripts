import requests
import csv

def download_lottery_numbers(lottery_type, filename):
    url = f'https://www.lottery.gov.pl/api/v1/games/{lottery_type}/results'
    response = requests.get(url)
    data = response.json()
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
