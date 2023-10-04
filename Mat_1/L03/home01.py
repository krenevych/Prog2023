n = int(input("Enter number"))

suma = 0
while n > 0:
    last = n % 10
    if last % 2 == 0:
        suma += last
    n = n // 10
print(suma)

