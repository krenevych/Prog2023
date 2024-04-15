import math

eps = 0.000000001

x = 5
S = 1
a = 1
n = 0
# for n in range(1, 10 + 1):
while abs(a) >= eps:
    n += 1
    a *= x / n
    S += a


print(f"math.e({x}) = {math.exp(x)}")
print(f"     e({x}) = {S}, n = {n}")
