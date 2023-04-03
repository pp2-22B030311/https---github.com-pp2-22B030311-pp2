#Write a Python program to count the number of lines in a text file.
import os

path = 'C:/saFDSA.txt'
with open( path , 'r', encoding='UTF8') as f:
    lines = f.readlines()
    print( len(lines) )
    