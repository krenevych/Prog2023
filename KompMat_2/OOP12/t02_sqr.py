x = 20
print(f"{x}**0.5 = {x ** 0.5}")

xn = x
n = 0
while True:
    n += 1
    xn = 0.5 * (xn + x / xn)
    if abs(xn ** 2 - x) < 0.0001:
        break

print(f"{x}**0.5 = {xn}, n = {n}")
