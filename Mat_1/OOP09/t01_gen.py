def gen(n, x):
    a = x  # спочатку в змінній а буде нульовий член послідовності a_0,
           # а далі поточний член послідовності
    yield a
    for k in range(1, n + 1):
        a = -x ** 2 / (2 * k * (2 * k + 1)) * a
        yield a


N = int(input("N = "))
x = float(input("x = "))
# gen_iter = iter(gen(N, x))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))

# myList = list(gen(3, 3))
# print(myList)

for a in gen(N, x):
    print(a)