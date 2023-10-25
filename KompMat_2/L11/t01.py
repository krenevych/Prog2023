def isPrime(n: int):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# print(isPrime(1_000_003))
a = int(input())
for i in range(a, 2*a-2):
    if isPrime(i) and isPrime(i+2):
        print(i, i+2)