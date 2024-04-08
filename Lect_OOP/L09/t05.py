# F(0) = F(1) = 1
# F(n) = F(n-1) + F(n-2), n >= 2

#               f2
#                  f1
#                  f
# 1  1   2   3  5  8

f2 = 1
f1 = 1
for n in range(2, 6 + 1):
    f = f2 + f1
    f2 = f1
    f1 = f

print(f, f1, f2)


