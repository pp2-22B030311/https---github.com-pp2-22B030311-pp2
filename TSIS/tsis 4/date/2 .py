import datetime

dt_today = datetime.datetime.today()
dt_tod = datetime.datetime.isoweekday(dt_today)
dt_yest = abs(dt_tod - 1)
dt_tom = abs(dt_tod + 1)


dates = {0 : "Sunday", 1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday", 7 : "Sunday"}

for num in dates:
    if dt_yest == num:
        print(dates[num])

for num in dates:
    if dt_tod == num:
        print(dates[num])

for num in dates:
    if dt_tom == num:
        print(dates[num])
