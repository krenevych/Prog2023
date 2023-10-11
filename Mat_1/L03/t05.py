# Для заданого натурального числа n
# виведіть його найменший дільник,
# відмінний від 1.
n = int(input())
# 21 -> 3
# 23 -> 23
k = 2
while True:
    if n % k == 0:
        print(k)
        break
    elif k > n ** 0.5 + 1:
        print(n)
        break
    k +=1