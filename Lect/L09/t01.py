# Задано лінійний масив цілих чисел.

N = int(input())
lst = [int(el) for el in input().split()]

# print(N)
print(lst)

a, b, c, d = lst
print(a, b, c, d, end="\n", sep="**=**")

print(*lst)
