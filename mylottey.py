import random

def winning_numbers():
    numbers = []
    while len(numbers) < 6:
        num = random.randint(1, 59)
        if num not in numbers:
            numbers.append(num)
        return numbers
print(winning_numbers())
