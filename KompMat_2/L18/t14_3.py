# d = {2: 4, 4: 1}
# print(d[7])

lst = [int(el) for el in input().split()]
print(lst)
assert len(lst) % 2 == 0
d = {}
for i in range(0, len(lst), 2):
    d[lst[i]] = lst[i + 1]
print(d)

M = int(input())
suma = 0
for i in range(1, M + 1):
    try:
        suma += d[i] * i
    except KeyError:
        pass

print('в гаманці', suma)