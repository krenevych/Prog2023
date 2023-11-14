a, b, c = map(int, input().split())

cond1 = a**2 + b**2 == c**2
cond2 = a**2 + c**2 == b**2
cond3 = b**2 + c**2 == a**2

if cond1 or cond2 or cond3:
    print("YES")
else:
    print("NO")

