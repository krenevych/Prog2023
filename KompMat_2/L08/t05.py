A = [int(el) for el in input().split()]
B = [int(el) for el in input().split()]
# x1  y1  x2 y2
# [5,  1, 2,  6]
#  0   1  2   3
a = [A[2] - A[0], A[3] - A[1]]
b = [B[2] - B[0], B[3] - B[1]]
# print(a, b)
# Довжину першого та другого вектора (два числа)
len_a = (a[0]**2 + a[1]**2)**0.5
len_b = (b[0]**2 + b[1]**2)**0.5
print(f"{len_a:0.9f} {len_b:0.9f}")

# Вектор, утворений додаванням заданих двох векторів
# Скалярний та векторний добуток заданих векторів
# Площу трикутника, побудованого з цих векторів
