# Нехай задано натуральне число 𝑁
# і послідовність чисел 𝑎_1,…,𝑎_𝑁.
# Потрібно знайти max(𝑎_1,…,𝑎_𝑁).

# N = 5
# a_i: 12 4 65 1 54
# print(max(12, 4, 65, 1, 54))


# max = 144

# 12   4    65   144    54


N = int(input("Введіть кількість чисел "))
max = int(input("a = "))
for i in range(N-1):
    a = int(input("a = "))
    if a > max:
        max = a

print("найбільше серед введених чисел =", max)


