def nsd(a, b):
    # a >= b
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b

    return a

print(nsd(30, 105))
print(nsd(12, 15))
print(nsd(14, 15))

