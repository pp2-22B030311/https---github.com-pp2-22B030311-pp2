#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

path = 'C:/Users/modik/Documents/pp2/Word.txt'
if os.path.exists(path):
    print( os.path.basename(path) )
    print( os.path.dirname(path) )
else:
    print( 'not exist' )