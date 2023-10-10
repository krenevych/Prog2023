# Задано лінійний масив цілих чисел.
# Збільшити на 2 кожний невід’ємний елемент масиву.

N = int(input())
lst = [int(el) for el in input().split()]

newLst = []  # будуємо новий список на базі вихідного
for e in lst:
    if e >= 0:
        newLst.append(e + 2)
    else:
        newLst.append(e)


print(*newLst)
