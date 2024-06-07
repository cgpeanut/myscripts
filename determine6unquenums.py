import json
def most_unique_numbers(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        unique_numbers = {}
        for i in data:
            for num in i:
                if num not in unique_numbers:
                    unique_numbers[num] = 1
                else:
                    unique_numbers[num] += 1
        sorted_numbers = sorted(unique_numbers.items(), key=lambda x: x[1])
        return sorted_numbers[-6:]

# test the function
print(most_unique_numbers('powerball_numbers.json')) #[/INST]  [end of text]