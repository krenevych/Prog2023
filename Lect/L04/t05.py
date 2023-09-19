x = float(input("x = "))

if x < -1:
    f = -x ** 2 + 1
elif abs(x) <= 1:
    f = 0
else:
    f = x ** 2 - 1

print(f)
