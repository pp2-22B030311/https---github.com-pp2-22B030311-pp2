def squares(a,b):
    for i in range(a, b+1):
        yield i*i

a = int(input())
b = int(input())
for i in squares(a,b):
    print(i, end=" ")
print() 
for i in range(a, b+1):
    print(i*i, end=" ")