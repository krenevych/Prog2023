# Обчислимо суму послідовності цілих чисел, що вводяться користувачем.
# Завершувати підрахунок будемо у випадку, коли користувач введе з клавіатури слово “стоп”.
suma = 0
while True:
    a = input("Введіть ціле число (або 'stop' для завершення): ")
    try:
        suma += int(a)
    except ValueError:
        if a == 'stop':
            break
        print("Е, ні! Введи, будь ласка, ціле!!!!!!!!!!!!!")

print(suma)





