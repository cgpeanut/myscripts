import requests
from bs4 import BeautifulSoup

def get_latest_powerball_results():
    url = "https://www.powerball.com/powerball-winning-numbers/latest-winning-numbers"

    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table containing the latest results
        results_table = soup.find('table', class_='latest-winning-numbers-table')

        # Extract the winning numbers and jackpot amount from the table
        rows = results_table.find_all('tr')
        white_balls = [int(cell.text) for cell in rows[0].select('td:not(:last-child)')]
        red_ball = int(rows[1].select('td')[0].text)

        # Get the jackpot amount from the text
        jackpot_amount = soup.find('div',
        class_='winning-numbers-prize').text.strip().split()[-1]

        # Return the results as a dictionary
        return {
            'white_balls': white_balls,
            'red_ball': red_ball,
            'jackpot': jackpot_amount
        }
    else
           return None
       # Call the function and print the results
       latest_results = get_latest_powerball_results()
       if latest_results is not None:
           print("White balls:", ', '.join(map(str, latest_results['white_balls'])))
           print("Red ball:", latest_results['red_ball'])
           print("Jackpot:", latest_results['jackpot'])
       else:
           print("Failed to fetch the results.")
