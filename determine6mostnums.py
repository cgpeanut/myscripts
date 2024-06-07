import json
from collections import Counter

def most_used_numbers(json_file):
    # Opening the json file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # List of all numbers in the file
    numbers = []
    for i in data:
        numbers += i.values()

    # Counter object to count the frequency of each number
    counter = Counter(numbers)

    # Getting the 6 most common numbers
    most_common = counter.most_common(6)

    # Returning the 6 most common numbers as a list
    return [num[0] for num in most_common]

# Testing the function
print(most_used_numbers('powerball_numbers.json'))