'''
Python program to check whether a given number is palindrome or not
'''

num = str(int(input("Enter a number: ")))
num1 = num[::-1]

if num == num1:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")