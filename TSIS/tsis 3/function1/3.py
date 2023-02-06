def solve(heads, legs):
    for chickens in range(heads + 1):
        rabbits = heads - chickens
        if 2*chickens + 4*rabbits == legs:
            return (chickens, rabbits)
    return (None, None)



heads = input()
heads = int(heads)
legs = input()
legs = int(legs)
print(solve(heads, legs))