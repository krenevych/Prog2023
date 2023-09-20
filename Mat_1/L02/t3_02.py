# 17 => 2 4 8 16

n = int(input())

pow2 = 1

while True:
    pow2 *= 2
    if pow2 >= n:
        break
    # print(pow2, end="\n")
    print(pow2, end=" ")
