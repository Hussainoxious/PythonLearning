'''
Dictionary will store and display count of each item in the list
'''

List1 = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]
count={}
for i in List1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)