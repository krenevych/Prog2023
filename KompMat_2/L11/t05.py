def toBin(n):
    b = ""
    print(bin(n))
    while n > 0:
        b = str(n & 1) + b
        n = n >> 1
    return b

def toDec(b: str):
    # b = "110" # n = 6
    n = 0
    pow2 = 1
    for d in b[::-1]:
        n += int(d) * pow2
        pow2 *= 2
    return n

print(toDec("110"))