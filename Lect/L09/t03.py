# Задано лінійний масив цілих чисел.

N = int(input())
lst = [
    int(el) if int(el) < 0 else int(el) + 2
       for el in input().split()
]

print(*lst)
