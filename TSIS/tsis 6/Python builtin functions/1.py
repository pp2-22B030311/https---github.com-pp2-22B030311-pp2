#Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce

mylist = list((1, 2, 3, 4))
multiplication =  reduce(lambda x, y: x*y, mylist)
print(multiplication)
