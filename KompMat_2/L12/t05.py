def nsd(a, b):
    if a < b:
        return nsd(b, a)
    if b == 0:
        return a
    return nsd(b, a % b)



print(nsd(30, 105))
print(nsd(12, 15))
print(nsd(14, 15))
