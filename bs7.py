import json

def most_used_numbers(file_path):
    with open(file_path) as f:
        data = json.load(f)

    num_dict = {}
    for key in data:
        if isinstance(data[key], int):
            num_dict[data[key]] = num_dict.get(data[key], 0) + 1

    sorted_nums = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_nums[:6]

print(most_used_numbers("powerball_numbers.json"))