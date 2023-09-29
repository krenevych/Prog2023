# перевести число з двійкового подання в десяткове.
n = int(input())

pow2 = 1
inDec = 0
while n > 0:
    bit = n % 10
    inDec += bit * pow2
    # print(bit, pow2)
    pow2 = pow2 * 2
    n = n // 10

print(inDec)


