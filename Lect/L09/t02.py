# Задано лінійний масив цілих чисел.
# Збільшити на 2 кожний невід’ємний елемент масиву.

N = int(input())
lst = [int(el) for el in input().split()]

# for e in lst:
#     if e >= 0:
#         e = e + 2
# for i, e in enumerate(lst):
#     if e >= 0:
#         e = e + 2

for i in range(N):
    if lst[i] >= 0:
        lst[i] += 2

print(*lst)
