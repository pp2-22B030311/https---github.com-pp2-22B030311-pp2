import datetime

dt1 = datetime.datetime(2022, 6, 15, 12, 0, 0)
dt2 = datetime.datetime(2022, 6, 16, 15, 30, 0)

diff = dt2 - dt1
seconds = diff.total_seconds()
print(seconds)