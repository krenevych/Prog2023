# Згенерувати текстовий файл, що буде містити
# послідовність квадратів натуральних чисел,
# що не перевищують N.

N = 10
f_out = open("out09.txt", "w")
for n in range(1, N):
    print(n**2, file=f_out)
f_out.close()
