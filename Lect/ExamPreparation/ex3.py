def readMatrix(matrix_file):
    M = []
    with open(matrix_file) as f:
        for line in f:
            # row = list(map(int, line.split()))
            row = [int(elem) for elem in line.split()]
            M.append(row)
    return M

def isMatrixMagicSquare(M):
    n = len(M)
    res = 0
    for elem in M[0]:
        res += elem

    for i in range(n):
        tmp_res = 0
        for j in range(n):
            tmp_res += M[i][j]
        if res != tmp_res:
            return False

    for j in range(n):
        tmp_res = 0
        for i in range(n):
            tmp_res += M[i][j]
        if res != tmp_res:
            return False

    return True

if __name__ == '__main__':
    A = readMatrix("matrix.txt")
    print(A)
    print("matrix.txt:", isMatrixMagicSquare(A))

    A2 = readMatrix("matrix2.txt")
    print(A2)
    print("matrix2.txt:", isMatrixMagicSquare(A2))



