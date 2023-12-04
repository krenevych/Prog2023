# print("my_main:", __name__)

from modul import isPrime

if __name__ == '__main__':

    for i in range(2, 100):
        if isPrime(i):
            print(i)
