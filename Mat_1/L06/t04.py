N = int(input())
numbers = [int(el) for el in input().split()]
d = {} # словник входжень кількості кожного числа
for e in numbers:
    if e in d:
        d[e] += 1
    else:
        d[e] = 1

new = []
for elem in numbers:
    if d[elem] == 1:
        continue
    if elem not in new:
        new.append(elem)
    else:
        new.remove(elem)
        new.append(elem)

print(*new)