'''
sort a tuple by its float element
using lambda as the key function when sorting a list
'''

data= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
print(sorted_data)