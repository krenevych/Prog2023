import math

S = 1
a = 1
x = 1
for n in range(1, 10 + 1):
    a *= x / n
    S += a


print("math.e =", math.e)
print("e      =", S)
