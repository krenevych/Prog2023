N = int(input('Enter N'))

f = 1
for n in range(1, N + 1):
    f = n * f

print(f"{N}! = {f}")