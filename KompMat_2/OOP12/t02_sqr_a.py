x = 20
print(f"{x}**0.5 = {x ** 0.5}")

xn = x
n = 0
while True:
    n += 1
    xn_1 = xn
    xn = 0.5 * (xn + x / xn)
    if abs(xn - xn_1) < 0.0001:
        break

print(f"{x}**0.5 = {xn}, n = {n}")
