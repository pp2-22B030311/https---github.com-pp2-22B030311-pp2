#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count_upper_lower(string):
    upper = 0
    lower = 0

    for i in string:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1

    return upper, lower