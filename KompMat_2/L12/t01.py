def f(n):
    if n == 0:
        return 1
    else:
        return f(n-1) * n

print(f(5))