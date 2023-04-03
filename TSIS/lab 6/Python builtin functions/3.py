#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def ispalindrome(string):
    reversed_string = ''.join(reversed(string))
    return (string == reversed_string)
a=input()
a = ispalindrome(a)
print(a)