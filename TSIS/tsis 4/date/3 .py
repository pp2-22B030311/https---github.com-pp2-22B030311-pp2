import datetime

tod = datetime.datetime.now()
tod = tod.replace(microsecond = 0)
print( tod )