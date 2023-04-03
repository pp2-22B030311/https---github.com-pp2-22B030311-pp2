#Write a Python program to copy the contents of a file to another file
with open('C:/pp2/lab6/Python Directories and Files/input.txt', 'r') as f:
    content = f.read()

with open('C:/pp2/lab6/Python Directories and Files/output.txt', 'w') as k:
    k.write( content )
