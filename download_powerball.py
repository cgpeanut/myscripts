import json
import requests
from bs4 import BeautifulSoup
def get_winning_numbers():
    url = "https://www.powerball.com/powerball/winning-numbers"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', {'class': 'winning-numbers'})
    powerball_numbers = []
    for result in results:
        numbers = result.find_all('span')
        powerball_numbers.append([int(number.text) for number in numbers])
    with open("winning_numbers.json", "w") as file:
        json.dump(powerball_numbers, file)
    return powerball_numbers
get_winning_numbers()
