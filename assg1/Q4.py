'''
swapping two tuples in python
'''
a = (100,90)
b=(200,80)
print(f"Tuples before swapping a: {a}, b: {b}")
temp = a
a = b
b = temp
'''a,b = b,a can also be used instead'''
print(f"Tuples after swapping a: {a}, b: {b}")