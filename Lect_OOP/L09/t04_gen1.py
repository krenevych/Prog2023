def SN(N):
    S = 1
    yield S
    for n in range(2,N+1):
        S = 2 * S + n**2
        yield S


N = int(input('Enter N: '))
for s in SN(N):
    print(s)


