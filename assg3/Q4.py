'''
for loop will iterate from 1500 to 2700 and print numbers divisible by 7 and 5
'''

for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)