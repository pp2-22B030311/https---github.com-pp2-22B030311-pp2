#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os

path = 'D:/pp2/TSIS/tsis 6/Python Directories and Files'
if os.path.exists(path):
    print("exist")
    if os.access(path, os.R_OK):
        print("readable")
    if os.access(path, os.W_OK):
        print("writable")
    if os.access(path, os.X_OK):
        print("executable")