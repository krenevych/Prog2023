a = [1, 2, 3]
try:
    print(a[12])
except IndexError as e:
    print(e)

print(a[12])