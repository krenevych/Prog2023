def gen():
    S = 1
    n = 1
    yield S, n
    while True:
        n += 1
        S += 1/n
        yield S, n


for S, n in gen():
    print(S, n)
    if S > 10:
        break


