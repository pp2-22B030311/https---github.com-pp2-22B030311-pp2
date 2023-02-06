
from itertools import permutations

def permutation(string):
  perms = [''.join(p) for p in permutations(string)]
  return perms

input_string = input("Enter a string: ")
result = permutation(input_string)
print("All permutations of the given string:")
for perm in result:
  print(perm)
