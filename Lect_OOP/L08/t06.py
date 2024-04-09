def fact(n):
    f = 1
    yield f
    for i in range(1, n + 1):
        f *= i
        yield f

for i in fact(5):
    print(i)

# f_gen = iter(fact(5))
# print(next(f_gen))
# print(next(f_gen))
# print(next(f_gen))
