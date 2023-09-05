'''
calculate total wage and pay 110% for overtime
'''

hrs = float(input("Enter hours worked:"))
wage = float(input("Enter hourly wage:"))
if(hrs <= 40):
    print(hrs * wage)
else:
    print(40*wage + (hrs-40)*1.1*wage)