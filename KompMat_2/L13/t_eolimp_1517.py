
def F(n):
    if n % 10 > 0:
        return n % 10
    elif n == 0:
        return 0
    else:
        return F(n // 10)

def S(p, q):
    res = 0
    for i in range(p, q+ 1):
        res += F(i)
    return res


while True:
    p, q = [int(el) for el in input().split()]
    if p < 0 or q < 0:
        break

    print(S(p, q))