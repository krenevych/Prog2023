def C(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return C(n-1, k-1) + C(n-1, k)
#
# c = C(5, 2)
# print(c)
N = 5
for n in range(N+1):
    for k in range(n+1):
        print(C(n, k), end=" ")
    print()