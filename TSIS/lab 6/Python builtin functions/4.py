#Write a Python program that invoke square root function after specific milliseconds.
from time import sleep
import math
def function(num, delay):
    sleep(delay / 1000.0)
    return math.sqrt(num)

b = int(input())
t = int(input())
print("Square root of {} after {} miliseconds is {}".format(b, t, function(b, t)))