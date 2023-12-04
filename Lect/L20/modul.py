# print("module:", __name__)
def isPrime(N):
    i = 2
    while i < N:
        if N % i == 0:
            return False
        i += 1
    return True

if __name__ == '__main__':
    print(isPrime(2))
    print(isPrime(27))
    print(isPrime(29))
    print(isPrime(9))
