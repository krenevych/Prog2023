N = 15

b = 1  # b_1
P = 3  # P_1

for n in range(2, N + 1):
    b = b / n
    P = P * (2 + b)

print(P)

