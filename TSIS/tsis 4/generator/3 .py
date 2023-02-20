def _3to4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for num in _3to4(n):
    print(num, end =' ')