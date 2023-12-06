
# Задано рядок, серед елементів якого містяться
# цифри.
# Використовуючи для всіх символів рядка
# функцію int перетворення символа у число,
# обчислити суму цифр заданого рядка.
suma = 0
try:
    with open("input14_2.txt") as f:
        # f = open("input14_2.txt")
        s = f.read().rstrip()
        for c in s:
            try:
                suma += int(c)
            except ValueError:
                1/0
                pass

except FileNotFoundError as err:
    print("file is not found", err.filename)
except ZeroDivisionError as err:
    print(err)


print(suma)