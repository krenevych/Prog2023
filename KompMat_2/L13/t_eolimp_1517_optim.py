cash = {0: 0}
def F(n):
    if n in cash:
        return cash[n]
    if n % 10 > 0:
        f = n % 10
        cash[n] = f
        return cash[n]
    else:
        f = F(n // 10)
        cash[n] = f
        return cash[n]

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