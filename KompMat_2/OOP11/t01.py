x3 = 0 # n-3 член послідовності
x2 = 1 # n-2 член послідовності
x1 = 1 # n-1 член послідовності

#   x3
#       x2
#          x1
#             xn
# 0  1  1  1  2

for n in range(3, 24 + 1):
    xn = x1 + x3
    x3 = x2
    x2 = x1
    x1 = xn

print(x1)
