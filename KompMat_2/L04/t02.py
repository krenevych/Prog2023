# Для заданого натурального числа n
# вивести всі степені двійки менші за n.
# 17 -> 2 4 8 16
n = int(input())
pow2 = 2
while pow2 < n:
    # print(pow2, end="\n")
    print(pow2, end=" ")
    pow2 *= 2
