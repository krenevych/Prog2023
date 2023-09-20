n = int(input())
cond1 = n % 2 == 1 # умова того, що
 # число парне

cond2 = 100 <= n < 1000
if cond1 or cond2:
    print("YES")
else:
    print("NO")

