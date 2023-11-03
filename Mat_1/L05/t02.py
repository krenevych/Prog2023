def isPrime(p):
    p2 = int(p**0.5) + 1
    for i in range(2, p2):
        if p % i == 0:
            return False
    return True
def isSqr(p):
    return (int(p ** 0.5))**2 == p

def isPow5(p):
    while p > 1:
        if p % 5 != 0:
            return False
        p = p // 5

    return True

# n = int(input())
# seq = [int(el) for el in input().split()]
seq = [23, 125, 36, 625, 13, 55]
seqPrime = []
seqSqr = []
seqPow5 = []
for c in seq:
    if isPrime(c): seqPrime.append(c)
    if isSqr(c): seqSqr.append(c)
    if isPow5(c): seqPow5.append(c)

print("Прості числа:", *seqPrime)
print("Повні квадрати:", *seqSqr)
print("Степені 5:", *seqPow5)