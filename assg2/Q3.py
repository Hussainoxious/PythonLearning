'''
D1 is dictionary with 4 lists as key values.
We loop through each element of D1 and udate the set which contains only unique elements
'''

D1 = {'list1': [4, 7, 10, 20], 'list2': [7, 16, 9, 10], 'list3': [13, 10, 4, 8], 'list4': [7, 20, 6, 11]}
unique_values = set()
for i in D1.values():
    unique_values.update(i)
print(list(unique_values))