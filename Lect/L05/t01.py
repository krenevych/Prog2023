N = int(input("N = "))
i = 2

while i < N:
    if N % i == 0:
        print("Число не просте")
        break
    i += 1
else:
    print("Число просте")

