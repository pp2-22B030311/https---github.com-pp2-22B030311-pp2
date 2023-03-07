import datetime

dt1 = datetime.datetime(2023, 3, 7, 12, 0, 0)
dt2 = datetime.datetime(2022, 3, 8, 12, 0, 0)

diff = abs(dt2 - dt1)
seconds = diff.total_seconds()
print(seconds)