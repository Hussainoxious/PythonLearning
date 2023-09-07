'''
How to count the number of lines, words, and characters in python for a given text file
'''

file_name = "Q1.txt"
chars = 0
words = 0
lines = 0

with open(file_name, 'r') as file:
    for line in file:
        lines += 1
        words += (len(line.split()))
        chars += len(line)
        
print(f"Number of lines: {lines}")
print(f"Number of words: {words}")
print(f"Number of characters: {chars}")