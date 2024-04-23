import math

x = 0.5

S = x
a = x
k = 0

while True:
    k += 1
    a *= x**2
    b = a / (2*k + 1)
    S += b

    if abs(b) < 0.000001:
        break

print(math.log((1 + x) / (1 - x)))
print(2 * S, k)