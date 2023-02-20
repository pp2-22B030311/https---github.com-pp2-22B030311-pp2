

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    
def filter_prime(numbers):
    primes = []
    for number in numbers:
        if is_prime(number):
            primes.append(number)
    return primes
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_prime(numbers))