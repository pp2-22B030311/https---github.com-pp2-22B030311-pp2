import re
txt = input()
x = re.findall("[a-z]+_[a-a]+",txt)

if x:
    print("yes")
else:
    print("no")