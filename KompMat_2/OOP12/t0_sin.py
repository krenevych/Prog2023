import math

x = math.pi / 6
print(f"math.sin({x}) =", math.sin(x))

n = 0
a = x
s = x

while abs(a) >= 0.00001:
    n = n + 1
    a = - x**2 / (2*n*(2*n+1)) * a
    s = s + a

print(f"     sin({x}) = {s}, n = {n}")





