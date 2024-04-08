N = int(input('Enter N: '))
x = float(input('Enter x: '))

a = 1
for n in range(1, N + 1):
    a = x / n * a

print(a)