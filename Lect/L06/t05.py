# перевести число з десятковго подання в (десяткове) вісімкове.
n = int(input())

pow10 = 1
inDec = 0
while n > 0:
    dig = n % 8
    inDec += dig * pow10
    print(dig, pow10)

    pow10 = pow10 * 10
    n = n // 8

print(inDec)


