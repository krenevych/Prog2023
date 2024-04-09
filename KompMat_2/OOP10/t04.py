N = int(input("Вкажіть порядок визначника, що хочете знайти "))

D2 = 5  # D_n-2
D1 = 19 # D_n-1

#    D2
#        D1
#        D
# 5  19  65


for n in range(3, N+1):
    D = 5 * D1 - 6 * D2
    D2 = D1
    D1 = D

print(D1)

