eps = 0.000000001 # Точність обчислення

def exp_gen(x):
    S = 1
    a = 1
    n = 0
    yield S, a, n

    while True:
        n += 1
        a *= x / n
        S += a
        yield S, a, n


for S, a, n in exp_gen(3):
    print(S, a, n)
    if abs(a) < eps:
        break
