N = int(input())
lst = input().split()

d = {}
for el in lst:
    if el in d:
        d[el] += 1
    else:
        d[el] = 1


for el in lst:
    # if lst.count(el) == 1:
    if d[el] == 1:
        print(el, end=" ")