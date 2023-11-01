def isPrime(p):
    p2 = int(p**0.5) + 1
    for i in range(2, p2):
        if p % i == 0:
            return False
    return True

n = 30
for i in range(n, 2*n-2):
    if isPrime(i) and isPrime(i+2):
        print(i, i+2)
