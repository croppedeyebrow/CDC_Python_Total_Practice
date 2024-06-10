



import random

def generate_lotto_numbers():
    lotto_numbers = []
    while len(lotto_numbers) < 7:
        number = random.randint(1, 45)
        if number not in lotto_numbers:
            lotto_numbers.append(number)
    return lotto_numbers

for _ in range(8):
    print(generate_lotto_numbers())