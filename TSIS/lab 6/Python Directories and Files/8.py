#Write a Python program to delete file by specified path. 
#Before deleting check for access and whether a given path exists or not.
import os

path = 'C:/python/lab6/Python Directories and Files/delete.txt'
if os.path.exists(path):
    if os.path.access(path, os.R_OK):
        os.remove(path)