'''
print list of numbers excluding divisible by 3
'''
number=1
listNotDivisibleBy3 = []
while number <= 10:
    if number % 3 != 0:
        listNotDivisibleBy3.append(number)
    number += 1
print(listNotDivisibleBy3)