a, b, c = [int(s) for s in input().split()]

cond = ((a > 0) and (b > 0) and (c > 0)
        and (a + b > c)
        and (a + c > b)
        and (b + c > a))

print(cond)
