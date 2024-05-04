def find_primes(min_num, max_num):
    primes = []
    for num in range(min_num, max_num + 1):
        if checkOf(num):
            primes.append(num)
    return primes

def checkOf(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
#print(find_primes(11,20))