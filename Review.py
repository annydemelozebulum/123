import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
#continue
for number in random_numbers[:]:
    if number % 2 == 1:
        random_numbers.remove(number)
    else:
        index = random_numbers.index(number)
        random_numbers[index] = number * 2