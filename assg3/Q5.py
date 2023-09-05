'''
printing pattern using for loop
in each of 10 lines, * will multiply with line no from 1 or 10 whichever is minimum
'''

for i in range(1,10):
    print("*" * min(i, 10-i))