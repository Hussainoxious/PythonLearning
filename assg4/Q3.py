'''
Validate US phone numbers
Use of regular expression
'''
import re

def validate_number(phone_number):
    pattern = r'^(\(\d{3}\)\s?|\d{3}-)\d{3}-\d{4}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False

phone_numbers = [
    "(123)456-7890",
    "(123) 456-7890",
    "123-456-7890",
    "(123)4567890",
    "1234567890",
    "(123)-456-7890",
    "123 456-7890",
]

for phone_number in phone_numbers:
    if validate_number(phone_number):
        print(f"{phone_number} is a valid US phone number.")
    else:
        print(f"{phone_number} is not a valid US phone number.")