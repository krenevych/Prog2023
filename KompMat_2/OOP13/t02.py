def T():
    t_n3 = 1
    n = 0
    yield t_n3, n
    t_n2 = 0
    n = 1
    yield t_n2, n
    t_n1 = 2
    n = 2
    yield t_n1, n
    while True:
        n += 1
        T = t_n1 + 7 * t_n3
        yield T, n
        t_n3 = t_n2
        t_n2 = t_n1
        t_n1 = T


for t, n in T():
    print(t)
    if n == 10:
        break



