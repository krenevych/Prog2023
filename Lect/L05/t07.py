# Знайти суму парних чисел з
# діапазону від 1 до N.
N = 15
suma = 0
for i in range(2, N + 1, 2):
    # print(i)
    suma += i
    # if i % 2 != 0:  # якщо число непарне
    #     continue    # пропускаємо його

    suma += i

print(suma)
