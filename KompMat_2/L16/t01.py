# Знайдіть кількість і суму її
# парних чисел, # що менші нуля.
# 1 - введення матриці
def readMatrix(file):
    M = []
    with open(file) as f:
        N = int(f.readline())
        for i in range(N):
            row = [int(el) for el in f.readline().split()]
            M.append(row)
    return M

def printMatrix(M):
    for row in M:
        # print(*row)
        for el in row:
            print(f"{el:7.1f}", end="")
        print()

M = readMatrix("input.txt")
# print(M)
printMatrix(M)
