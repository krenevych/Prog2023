N = int(input())
lst = input().split()

d = {}
for el in lst:
    if el in d:
        d[el] += 1
    else:
        d[el] = 1

for num, count in d.items():
    if count > N // 2:
        print(num)
        break
else:
    print(-1)
