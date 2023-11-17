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
count = 0
suma = 0
for row in M:
    for el in row:
        # if el < 0 and el % 2 == 0:
        #     count += 1
        #     suma += el
        if el < 0:
            el = -el
print()
for i in range(len(M)):
    for j in range(len(M[0])):
        if M[i][j] < 0:
            M[i][j] = -M[i][j]
printMatrix(M)


