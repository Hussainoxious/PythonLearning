import datetime

today_date = datetime.date.today()
result_date = today_date - datetime.timedelta(days=5)

print(f"Today's Date: {today_date}")
print(f"Five Days Ago: {result_date}")