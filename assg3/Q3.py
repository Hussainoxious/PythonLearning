'''
a class with two methods:
getString: to get a string from console input
printString: to print the string in upper case.
'''

class MyString:
    def __init__(self):
        self.input_string = ""
    def getString(self):
        self.input_string = input("Enter a string: ")
    def printString(self):
        print("Output String is:", self.input_string.upper())

myString = MyString()
myString.getString()
myString.printString()