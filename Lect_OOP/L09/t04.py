N  = int(input('Enter N: '))
S = 1
for n in range(2,N+1):
    S = 2 * S + n**2

print(S)