def divide(n, p, lst : list):
    if n == 0:
        print(*lst)
    else:
        for i in range(p, n+1):
            newlst = lst[:]

            newlst.insert(0, i)
            divide(n - i, i, newlst)


# n = int(input())
n = 4
divide(n, 1, [])