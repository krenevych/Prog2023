def Fib(n):
    global fibs
    print("in Fib")

    if fibs[n] != 0:
        return fibs[n]
    else:
        f = Fib(n-1) + Fib(n-2)
        fibs[n] = f
        return f


N = 40
fibs = [0] * (N + 1)
fibs[0] = fibs[1] = 1
# 1 1 2 3 5 8 13
# [1 1 2 3 5 0 0 0 0 0 0]
#  0 1 2 3 4 5 6 7 8 9 10
print(Fib(N))
