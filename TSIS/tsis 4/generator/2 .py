def check_to_even(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i


n = int(input())
for num in check_to_even(n):
    print(num, end =',')
print('\n')
a = [i for i in range(n+1)]

for num in a:
    if num % 2 == 0:
        print(num, end =',')