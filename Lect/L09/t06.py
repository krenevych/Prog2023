N = int(input())
lst = \
    [int(el) for el in input().split()]

# print(*lst)
# lst.sort()

# 4 2 3 1 4 5
# N = len(lst)
for step in range(N - 1):
    for i in range(1, N - step):
        if lst[i-1] > lst[i]:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]

    print(*lst)
