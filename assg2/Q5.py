'''
program to remove an empty tuple(s) from a list of tuples
'''

data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
data1 = []
for tup in data:
    if tup:
        data1.append(tup)
print(data1)