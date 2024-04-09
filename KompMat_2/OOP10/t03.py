def gen():
    a = 1
    n = 1
    yield a, n
    while True: # цей генератор буде генерувати нескінченну послідовність
        n += 1
        a += 1 / n
        yield a, n


for a, n in gen():
    print(a, n)
    if a > 10:
        break

