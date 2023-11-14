# У текстовому файл містить набір чисел,
# кожне з яких записано з нового рядка.
# Потрібно знайти cуму цих чисел.
f = open("input06.txt", encoding="utf-8")
suma = 0
for line in f:
    # print(line)
    d = float(line)
    # print(d)
    suma += d

print(suma)

f.close()



