def readMatrix(file):
    M = []
    with open(file) as f:
        for i in range(2):
            row = [int(el) for el in f.readline().split()]
            M.append(row)
    return M

def printMatrix(M):
    for row in M:
        # print(*row)
        for el in row:
            print(f"{el:7.1f}", end="")
        print()

A = readMatrix("input.txt")
# printMatrix(A)

d  = A[0][0] * A[1][1] - A[0][1] * A[1][0]
dx = A[0][2] * A[1][1] - A[0][1] * A[1][2]
dy = A[0][0] * A[1][2] - A[0][2] * A[1][0]
x = dx / d
y = dy / d
print(f"{x:0.3f}")
print(f"{y:0.3f}")
