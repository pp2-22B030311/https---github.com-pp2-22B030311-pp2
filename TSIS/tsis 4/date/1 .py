import datetime

dt_today = datetime.datetime.today()
dt_num = datetime.datetime.isoweekday(dt_today)
dt_subtr = abs(dt_num - 5)

dates = {0 : "Sunday", 1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday", 7 : "Sunday"}

for num in dates:
    if dt_subtr == num:
        print(dates[num])

