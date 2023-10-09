# Введення матриці з клавіатури
# 1 2 3
# 3 6 9
# 1 1 0


N = int(input("Задайте кількість рядків матриці "))
A = [] # список рядків матриці, спочатку порожній
for i in range(N):
    row = [int(el) for el in input().split()]
    A.append(row)

print(A)

