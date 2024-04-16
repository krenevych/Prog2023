x = 2

xn = x / 2
n = 0

while True:
    n += 1
    x_prev = xn
    xn = 0.5 * (xn + x / xn)
    if abs(xn - x_prev) < 0.00001:  # для виходу скористаємося підходом різниці між двома сусідніми членам послідовності
        break

print(x**0.5)
print(xn, n)


xn = x / 2
n = 0
while True:
    n += 1
    xn = 0.5 * (xn + x / xn)
    if abs(xn**2 - x) < 0.00001:  # для виходу скористаємося підходом різниці між двома сусідніми членам послідовності
        break

print(xn, n)

