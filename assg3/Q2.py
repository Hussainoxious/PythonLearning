'''
Write a Python program to create a class representing a Circle.
'''

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def perimeter(self):
        return 2 * math.pi * self.radius
radius = float(input("Enter radius: "))
circle = Circle(radius)
print(f"Area: {circle.area()}")
print(f"Perimeter: {circle.perimeter()}")