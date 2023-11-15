# Задано масив довжини n, знайдіть його мажоруючий елемент.
# Елемент називається мажоруючий, якщо він зустрічається в
# масиві більше ніж [n/2] рази.
# 3 5 -7 7 5 -9 -4
N = int(input())
numbers = [int(el) for el in input().split()]
d = {} # словник входжень кількості кожного числа
for e in numbers:
    if e in d:
        d[e] += 1
    else:
        d[e] = 1
# for e in numbers:
#     d[e] = numbers.count(e)

for k, v in d.items():
    if v > N // 2:
# for k in d:
#     if d[k] > N // 2:

        print(k)
        break
else:
    print(-1)


# print(d)
