def grams_to_ounces(grams):
    ounces = 28.3495231 * int(grams)
    return ounces

grams = input()
print(grams_to_ounces(grams))