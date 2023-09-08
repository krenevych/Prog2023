x1, y1, x2, y2, x3, y3 = [float(d) for d in input().split()]
# print(x1, y1, x2, y2, x3, y3)

a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
c = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5

P = a + b + c
p = P / 2
# використаємо формулу Герона
S = (
    p * (p - a) * (p - b) * (p - c)
    )**0.5

print(f"{P:0.4f} {S:0.4f}")



