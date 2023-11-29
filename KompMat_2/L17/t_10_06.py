def readMatrix(file):
    A = []
    B = []
    with open(file) as f:
        n, m = [int(el) for el in f.readline().split()]
        for i in range(n):
            row = [int(el) for el in f.readline().split()]
            A.append(row)

        k, p = [int(el) for el in f.readline().split()]
        for i in range(k):
            row = [int(el) for el in f.readline().split()]
            B.append(row)
    return A, B


def printMatrix(M):
    for row in M:
        # print(*row)
        for el in row:
            print(f"{el:7.1f}", end="")
        print()

def mult(A, B):
    n = len(A)
    m = len(A[0])
    k = len(B)
    p = len(B[0])
    assert m == k
    C = []
    for i in range(n):
        row = [0] * p
        C.append(row)

    for i in range(n):
        for j in range(p):
            for r in range(m):
                C[i][j] += A[i][r] * B[r][j]
    return C



A, B = readMatrix("input.txt")
printMatrix(A)
printMatrix(B)
printMatrix(mult(A, B))
