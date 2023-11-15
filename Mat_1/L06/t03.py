N = int(input())
numbers = [int(el) for el in input().split()]
d = {} # словник входжень кількості кожного числа
for e in numbers:
    if e in d:
        d[e] += 1
    else:
        d[e] = 1

uniq = [e for e in numbers if d[e] == 1]
print(*uniq)
# for e in numbers:
#     if d[e] == 1:
#         print(e, end=" ")

# for k, v in d.items():
#     if v == 1:
#         print(k, end=" ")

