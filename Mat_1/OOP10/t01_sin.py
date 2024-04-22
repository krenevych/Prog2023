import math

def sin(x):
    S = x
    a = x
    n = 0
    while True:
        n += 1
        a = - a * x**2 / ((2*n) * (2*n + 1))
        S = S + a
        if abs(a) < 0.0000001:
            break

    return S


x = math.pi / 3
print(f"math.sin({x})= ", math.sin(x))
print(f"  my.sin({x})= ", sin(x))

