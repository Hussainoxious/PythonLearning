'''
Python program to print vowels and consonants in a given string
'''

myString = input("Enter a string: ")
vowels = ""
consonants = ""

for char in myString:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels += char
        else:
            consonants += char

print("Vowels: ",vowels)
print("Consonants: ",consonants)