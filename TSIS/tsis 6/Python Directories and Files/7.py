#Write a Python program to copy the contents of a file to another file
with open('D:/pp2/TSIS/tsis 6/Python Directories and Files/input.txt', 'r') as f:
    content = f.read()

with open('D:/pp2/TSIS/tsis 6/Python Directories and Files/output.txt', 'w') as k:
    k.write( content )
